---
symbol: "CHD8"
type: "gene"
col: 2035
ensembl_id: "ENSG00000100888"
name: "chromodomain helicase DNA binding protein 8"
location: "14q11.2"
module: 7
arm: "+"
pooled_cpm: 121.77
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CHD8

*chromodomain helicase DNA binding protein 8* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.67× (z +20.2, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.532× (z -19.6, q 0e+00, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.820× (z -4.4, q 0.001, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1573 0.178×, H4 0.0902×, NCI-H460 0.391×, NCI-H23 0.341×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.155×, C32 0.273×, NCI-H2030 0.386×, PANC-1 0.445×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.211×, CFPAC-1 0.352×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.541×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMG8]] (+0.73, fdr 7e-06), [[MED1]] (+0.70, fdr 7e-06), [[MRM3]] (+0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2035.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.67×** | +20.2 | 0e+00 | 48/49 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +14.0 | 6e-42 | 41/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +13.0 | 2e-36 | 35/48 (HEC-1-A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +10.9 | 2e-25 | 37/48 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +10.8 | 3e-25 | 44/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +10.6 | 2e-24 | 37/48 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +10.4 | 3e-23 | 37/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.22×** | +8.8 | 1e-16 | 30/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +8.3 | 5e-15 | 32/48 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +8.3 | 9e-15 | 34/48 (HOP62, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +8.0 | 5e-14 | 33/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +7.3 | 1e-11 | 34/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +5.9 | 1e-07 | 11/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.20× | +5.6 | 9e-07 | 22/48 (SW480, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.0 | 2e-05 | 20/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.23×** | +5.0 | 2e-05 | 26/47 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +4.8 | 4e-05 | 22/47 (BT-474, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2035.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1573 0.178×, H4 0.0902×, NCI-H460 0.391×, NCI-H23 0.341×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (NCI-H1573 0.155×, C32 0.273×, NCI-H2030 0.386×, PANC-1 0.445×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.211×, CFPAC-1 0.352×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (MIA PaCa-2 0.541×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.532×** | -19.6 | 0e+00 | 45/49 (NCI-H1573, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.560×** | -17.3 | 0e+00 | 34/44 (NCI-H1573, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.521×** | -16.1 | 0e+00 | 38/45 (C32, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.820×** | -4.4 | 0.001 | 20/48 (HCT15, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.887× | -3.6 | 0.037 | 14/47 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.889× | -3.3 | 0.090 | 15/48 (SW 1271, HEC-1-A, …) | inconsistent across doses |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.865× | -3.2 | 0.097 | 14/48 (LS 180, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 132 | 9 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +17.9) | [[Dinaciclib (drug)]] 0.5 µM 0.599× (z -10.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 105 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +17.5) | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -11.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 135 | 5 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.32× (z +19.3) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -14.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 227 | 5 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.34× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.534× (z -9.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 117 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.99× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.544× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 137 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.11× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.541× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 117 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.83× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.569× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 168 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.14× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -15.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 98.6 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.88× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -14.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 101 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.16× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.428× (z -13.5) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 100.0 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.41× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 152 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.28× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -32.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 143 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.513× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 122 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -10.2) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 160 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.75× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.352× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 108 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.57× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -18.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 138 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.74× (z +14.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.511× (z -9.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 96.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.9) ⚠ cell-cycle shift, explains ~43% of this change | [[Dinaciclib (drug)]] 5 µM 0.451× (z -10.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 131 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.88× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.474× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 140 | 1 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 2.71× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.475× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 128 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -15.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 183 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.579× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 73.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.418× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 167 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -10.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.273× (z -18.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 135 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -10.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 132 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.77× (z +13.4) | — |
| [[H4 (line)]] | wt | 121 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0902× (z -25.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 80.4 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -8.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 80.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.18× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 177 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -16.4) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 109 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.310× (z -12.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 91.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 78.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.314× (z -11.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 72.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 243 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.6) | — |
| [[HepG2_C3A (line)]] | wt | 89.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -8.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 94.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.454× (z -9.4) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -11.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 208 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.75× (z +10.4) | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 168 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG8]] | +0.73 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[MED1]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[MRM3]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CDK12]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 | STRING 417 |
| [[ZNF629]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[SART3]] | +0.68 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[C12orf43]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[WDR33]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[GTF3C4]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[PRCC]] | +0.64 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[WAPL]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.699). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.4, 9.5); signed map (-2.7, -25.3). **Vector** length 115, 34.3% of its response variance represented; |z| ≥ 3 in 1,153 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +10.3 | +8.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +20.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.7 | +10.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.4 | +7.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.3 | +5.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +14.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.6 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +8.3 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.4 | -16.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.2 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.8 | -19.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.7 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | chromodomain helicase DNA binding protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:21,385,194-21,456,126 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1564, DUPLIN; previously HELSNF1 |
| Gene groups (HGNC) | SNF2 related family; Small nucleolar RNA protein coding host genes |
| Reactome | 7 pathways, smallest: CHD6, CHD7, CHD8, CHD9 subfamily; Deactivation of the beta-catenin transactivating complex; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCK8](https://www.uniprot.org/uniprotkb/Q9HCK8) (ATP-dependent chromatin remodeler CHD8):

> ATP-dependent chromatin-remodeling factor, it slides nucleosomes along DNA; nucleosome sliding requires ATP. Acts as a transcription repressor by remodeling chromatin structure and recruiting histone H1 to target genes. Suppresses p53/TP53-mediated apoptosis by recruiting histone H1 and preventing p53/TP53 transactivation activity. Acts as a negative regulator of Wnt signaling pathway by regulating beta-catenin (CTNNB1) activity. Negatively regulates CTNNB1-targeted gene expression by being …

**Summary**, from NCBI Gene [57680](https://www.ncbi.nlm.nih.gov/gene/57680):

> This gene encodes a member of the chromodomain-helicase-DNA binding protein family, which is characterized by a SNF2-like domain and two chromatin organization modifier domains. The encoded protein also contains brahma and kismet domains, which are common to the subfamily of chromodomain-helicase-DNA binding proteins to which this protein belongs. This gene has been shown to function in several processes that include transcriptional regulation, epigenetic remodeling, promotion of cell …

**Accessions** — [HGNC:20153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20153) · Entrez [57680](https://www.ncbi.nlm.nih.gov/gene/57680) · UniProt [Q9HCK8](https://www.uniprot.org/uniprotkb/Q9HCK8) · Ensembl [ENSG00000100888](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100888)

## Data

Gene col 2035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2035); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2035]; `tensor/DDL_lfc|DDL_z.npy` [2035]; `embed/gene_vectors.npy` [2035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2035 or target_col == 2035). Every well: [[CHD8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHD8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
