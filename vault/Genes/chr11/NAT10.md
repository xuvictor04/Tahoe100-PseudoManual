---
symbol: "NAT10"
type: "gene"
col: 5692
ensembl_id: "ENSG00000135372"
name: "N-acetyltransferase 10"
location: "11p13"
module: 5
arm: "+"
pooled_cpm: 68.46
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# NAT10

*N-acetyltransferase 10* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.73× (z +18.2, q 0e+00, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.634× (z -11.6, q 3e-28, down in 27 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.846× (z -6.3, q 5e-08, down in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (C-33 A 0.0909×, H4 0.212×, SK-MEL-2 0.295×, KATO III 0.271×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.136×, HEC-1-A 0.290×, A549 0.210×, SNU-423 0.274×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.153×, C32 0.254×, A-427 0.367×; ⚠ toxic; transcription drop); [[5-Azacytidine (drug)]] 0.05 µM in 1 line (SW 1088 0.0685×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSR1]] (+0.77, fdr 7e-06), [[PPAN]] (+0.73, fdr 7e-06), [[DHODH]] (+0.69, fdr 7e-06); moves opposite to [[P2RX4]] (-0.55, fdr 3e-05), [[RNF11]] (-0.54, fdr 4e-05), [[CHP1]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MEX3A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5692.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.73×** | +18.2 | 0e+00 | 44/49 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.27×** | +16.3 | 0e+00 | 44/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +13.9 | 9e-42 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +13.8 | 2e-41 | 44/48 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.56×** | +11.7 | 1e-29 | 40/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.33×** | +7.4 | 9e-12 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +7.4 | 1e-11 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.70×** | +7.3 | 1e-11 | 35/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +6.7 | 2e-09 | 26/48 (A-172, HT-29, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +6.3 | 2e-08 | 32/48 (SW1417, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.27×** | +6.2 | 2e-08 | 28/48 (SW480, LOX-IMVI, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +6.2 | 2e-08 | 24/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.53×** | +5.8 | 3e-07 | 30/48 (SW1417, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.52×** | +5.8 | 3e-07 | 27/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +5.6 | 9e-07 | 22/47 (LOX-IMVI, BT-474, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.46×** | +5.2 | 7e-06 | 24/48 (SW1417, A549, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 6e-05 | 22/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.20× | +4.7 | 7e-05 | 20/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.007 | 6/48 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.20× | +3.3 | 0.017 | 7/48 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5692.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 6 lines (C-33 A 0.0909×, H4 0.212×, SK-MEL-2 0.295×, KATO III 0.271×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 6 lines (C-33 A 0.136×, HEC-1-A 0.290×, A549 0.210×, SNU-423 0.274×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (C-33 A 0.153×, C32 0.254×, A-427 0.367×; ⚠ toxic; transcription drop); [[5-Azacytidine (drug)]] 0.05 µM in 1 line (SW 1088 0.0685×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -11.6 | 3e-28 | 27/43 (C-33 A, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.632×** | -11.2 | 8e-27 | 31/45 (C-33 A, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.714×** | -8.9 | 9e-17 | 33/49 (C-33 A, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -6.3 | 5e-08 | 21/48 (LS 180, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.811×** | -5.6 | 3e-06 | 26/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.885× | -4.6 | 4e-04 | 4/48 (NCI-H1792, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.856× | -4.1 | 0.003 | 13/48 (J82, C-33 A, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.861× | -4.0 | 0.005 | 17/48 (SW48, hTERT-HPNE, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.868× | -3.8 | 0.011 | 13/48 (CFPAC-1, CHP-212, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.016 | 16/47 (SW1417, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **0.786×** | -3.3 | 0.045 | 8/47 (LoVo, H4, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.885× | -3.3 | 0.054 | 14/47 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.888× | -3.2 | 0.071 | 11/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.890× | -3.1 | 0.082 | 12/49 (RKO, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.902× | -3.1 | 0.082 | 10/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5692. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 101 | 8 (5 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.03× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.499× (z -10.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 86.5 | 6 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.474× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 55.8 | 5 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 59.9 | 5 (2 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 5.90× (z +11.4) | — |
| [[A549 (line)]] | wt | 55.2 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +13.8) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.73× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -14.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 103 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0909× (z -23.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 99.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -15.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 107 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.75× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -13.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 40.9 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.9) ⚠ cell-cycle shift, explains ~62% of this change | [[Dinaciclib (drug)]] 5 µM 0.371× (z -8.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 83.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.469× (z -10.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 89.6 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.57× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -9.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 56.1 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 105 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.51× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 75.5 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 5.82× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 69.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 84.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.509× (z -10.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 74.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -16.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 64.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 27.2 | 2 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.79× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[RKO (line)]] | wt | 106 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 7.14× (z +13.2) | — |
| [[SW1417 (line)]] | alt | 78.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.89× (z +8.6) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 5 µM 0.443× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 57.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.89× (z +8.9) | — |
| [[A-427 (line)]] | wt | 76.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -11.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 42.9 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +8.5) ⚠ unreliable plate only | — |
| [[CHP-212 (line)]] | wt | 56.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -8.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 39.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 93.2 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.400× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.305× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 37.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 54.1 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 68.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.03× (z +9.6) | — |
| [[NCI-H2347 (line)]] | alt | 54.0 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.76× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -10.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 72.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.403× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 81.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -12.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 59.0 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.05 µM 0.0685× (z -8.5) |
| [[SW48 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -12.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 115 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 89.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5692), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSR1]] | +0.77 | +0.74 / +0.77 | both halves | 7e-06 | pathway: rRNA processing; STRING 981 |
| [[PPAN]] | +0.73 | +0.72 / +0.71 | both halves | 7e-06 | STRING 651 |
| [[DHODH]] | +0.69 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[MRTO4]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 | STRING 868 |
| [[NOP16]] | +0.67 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[EIF3B]] | +0.66 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.63 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[TTI1]] | +0.62 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[BYSL]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 | same gene group; pathway: rRNA processing; STRING 999 |
| [[MDN1]] | +0.62 | +0.64 / +0.63 | both halves | 7e-06 | STRING 442 |
| [[DHX33]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 | STRING 432 |
| [[DDX31]] | +0.61 | +0.53 / +0.64 | both halves | 1e-05 | STRING 833 |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P2RX4]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[RNF11]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[CHP1]] | -0.53 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[SVIP]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[SLC30A4]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[GRHL1]] | -0.52 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[ABI1]] | -0.51 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEX3A]] | B | MEX3A activity raises NAT10's level | lines that do not express MEX3A (6) vs lines expressing it (44) | 1.55× lower at baseline in the lines without MEX3A | 0.037 | ⚠ within organs, on part of the lines; also absent: SNTA1, POGLUT3, FMNL3; maybe low, not absent |
| [[MPZL3]] | B | MPZL3 activity lowers NAT10's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.22× higher at baseline in the lines without MPZL3 | 0.062 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[ALDH1B1]] | C | ALDH1B1 activity raises NAT10's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 1.97× lower at baseline in the lines without ALDH1B1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.8, -37.2); signed map (-2.0, -46.6). **Vector** length 102, 27.1% of its response variance represented; |z| ≥ 3 in 1,204 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.53 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +13.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.5 | +16.3 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.6 | +6.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +5.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.0 | +5.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.1 | -11.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.1 | -6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -3.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -3.8 | -5.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | +1.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | N-acetyltransferase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:34,105,617-34,147,670 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hALP, FLJ10774, FLJ12179, NET43, KIAA1709, Kre33 |
| Gene groups (HGNC) | GCN5 related N-acetyltransferases; SSU processome |
| Reactome | 4 pathways, smallest: rRNA modification in the nucleus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0A0](https://www.uniprot.org/uniprotkb/Q9H0A0) (RNA cytidine acetyltransferase):

> RNA cytidine acetyltransferase that catalyzes the formation of N(4)-acetylcytidine (ac4C) modification on mRNAs, 18S rRNA and tRNAs. Catalyzes ac4C modification of a broad range of mRNAs, enhancing mRNA stability and translation. mRNA ac4C modification is frequently present within wobble cytidine sites and promotes translation efficiency. Mediates the formation of ac4C at position 1842 in 18S rRNA. May also catalyze the formation of ac4C at position 1337 in 18S rRNA (By similarity). Required …

**Summary**, from NCBI Gene [55226](https://www.ncbi.nlm.nih.gov/gene/55226):

> The protein encoded by this gene is an RNA cytidine acetyltransferase involved in histone acetylation, tRNA acetylation, the biosynthesis of 18S rRNA, and the enhancement of nuclear architecture and chromatin organization. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:29830](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29830) · Entrez [55226](https://www.ncbi.nlm.nih.gov/gene/55226) · UniProt [Q9H0A0](https://www.uniprot.org/uniprotkb/Q9H0A0) · Ensembl [ENSG00000135372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135372)

## Data

Gene col 5692: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5692); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5692, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5692]; `tensor/DDL_lfc|DDL_z.npy` [5692]; `embed/gene_vectors.npy` [5692]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5692 or target_col == 5692). Every well: [[NAT10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAT10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
