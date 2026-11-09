---
symbol: "CAST"
type: "gene"
col: 7691
ensembl_id: "ENSG00000153113"
name: "calpastatin"
location: "5q15"
module: 111
arm: "+"
pooled_cpm: 500.37
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/111"]
generated_by: "tahoemap"
---

# CAST

*calpastatin* — 5q15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.77× (z +14.5, q 4e-45, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 5 µM: 1.24× (z +5.2, q 3e-05, up in 27 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HS-578T 2.39×, PANC-1 2.18×, MIA PaCa-2 2.09×, HOP62 2.18×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 4.30×, SK-MEL-2 2.72×, MIA PaCa-2 1.60×); [[Auranofin (drug)]] 5 µM in 3 lines (SNU-1 2.18×, C-33 A 2.42×, SK-MEL-2 1.63×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 6.17×, SK-MEL-2 6.30×).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.564× (z -20.5, q 0e+00, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPAG9]] (+0.77, fdr 7e-06), [[IQGAP1]] (+0.71, fdr 7e-06), [[PRKCI]] (+0.63, fdr 1e-05); moves opposite to [[MRM1]] (-0.62, fdr 3e-05), [[STARD7-AS1]] (-0.60, fdr 4e-05), [[SLC5A6]] (-0.58, fdr 1e-04).
> It is in [[Module 111]], a single-armed module (Cell-Cell communication).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ATP2B4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7691.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HS-578T 2.39×, PANC-1 2.18×, MIA PaCa-2 2.09×, HOP62 2.18×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A-172 4.30×, SK-MEL-2 2.72×, MIA PaCa-2 1.60×); [[Auranofin (drug)]] 5 µM in 3 lines (SNU-1 2.18×, C-33 A 2.42×, SK-MEL-2 1.63×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A-172 6.17×, SK-MEL-2 6.30×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +14.5 | 4e-45 | 44/49 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +11.8 | 2e-29 | 35/44 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.47×** | +9.1 | 1e-17 | 40/45 (C-33 A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.24×** | +5.2 | 3e-05 | 27/47 (H4, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.20× | +4.6 | 4e-04 | 23/47 (H4, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | 1.18× | +4.1 | 0.004 | 22/47 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.067 | 17/48 (A498, MIA PaCa-2, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.14× | +3.3 | 0.067 | 16/48 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.1 | 0.12 | 13/49 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.13 | 4/49 (Panc 03.27, COLO 205, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7691.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -20.5 | 0e+00 | 44/49 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.668×** | -14.5 | 6e-45 | 37/48 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -10.6 | 4e-24 | 39/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.749×** | -10.3 | 6e-23 | 36/48 (HS-578T, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.740×** | -7.6 | 3e-12 | 41/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -7.5 | 7e-12 | 35/48 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.787×** | -6.0 | 1e-07 | 27/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.796×** | -5.8 | 6e-07 | 27/48 (A549, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.813×** | -5.0 | 3e-05 | 27/48 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.689×** | -4.9 | 5e-05 | 28/49 (Panc 03.27, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.830×** | -4.7 | 1e-04 | 25/48 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.2 | 0.001 | 21/48 (LoVo, COLO 205, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.890× | -4.1 | 0.002 | 10/48 (SNU-1, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.746×** | -3.9 | 0.004 | 28/48 (A-427, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.9 | 0.004 | 20/48 (LoVo, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.871× | -3.3 | 0.033 | 16/47 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.889× | -3.0 | 0.092 | 6/48 (Hs 766T, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7691. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 778 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -25.9) |
| [[HS-578T (line)]] | alt | 622 | 3 (3 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.39× (z +16.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -16.9) |
| [[NCI-H1573 (line)]] | alt | 623 | 2 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Peretinoin (drug)]] 5 µM 1.67× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -21.7) |
| [[Panc 03.27 (line)]] | alt | 738 | 1 (1 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.71× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -22.3) |
| [[A549 (line)]] | wt | 560 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -25.6) |
| [[HOP62 (line)]] | alt | 475 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +14.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -18.9) |
| [[NCI-H460 (line)]] | wt | 910 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.88× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -28.6) |
| [[Hs 766T (line)]] | wt | 895 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.79× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -21.6) |
| [[KATO III (line)]] | alt | 390 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -22.1) |
| [[LoVo (line)]] | wt | 610 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -18.6) |
| [[C32 (line)]] | wt | 367 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +10.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 505 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.09× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.60× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -23.2) |
| [[NCI-H2030 (line)]] | alt | 480 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.90× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.56× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -17.0) |
| [[PANC-1 (line)]] | alt | 474 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +14.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.549× (z -15.4) |
| [[SNU-1 (line)]] | wt | 388 | 4 (3 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.18× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -10.3) |
| [[SW480 (line)]] | alt | 374 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +13.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.608× (z -12.0) |
| [[A498 (line)]] | wt | 345 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.63× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 204 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.9) |
| [[C-33 A (line)]] | alt | 205 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.42× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 554 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -13.3) |
| [[H4 (line)]] | wt | 502 | 2 | 2 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.08× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 359 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +10.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.454× (z -17.4) |
| [[NCI-H2347 (line)]] | alt | 988 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -23.3) |
| [[SK-MEL-2 (line)]] | alt | 627 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +49.2) | — |
| [[SNU-423 (line)]] | alt | 584 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.69× (z +8.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -12.8) |
| [[SW 900 (line)]] | alt | 252 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.29× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -13.4) |
| [[A-172 (line)]] | wt | 575 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +51.8) | — |
| [[HEC-1-A (line)]] | alt | 173 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.77× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.1) |
| [[HT-29 (line)]] | alt | 413 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 381 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +9.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -13.9) |
| [[A-427 (line)]] | wt | 273 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +12.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 780 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -14.5) |
| [[HCT15 (line)]] | alt | 405 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 334 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -15.5) |
| [[J82 (line)]] | alt | 417 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.61× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 308 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +11.2) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.537× (z -8.8) |
| [[RKO (line)]] | wt | 472 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -17.3) |
| [[SW 1271 (line)]] | alt | 997 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -11.6) |
| [[SW1417 (line)]] | alt | 242 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +14.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 372 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.51× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 284 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.88× (z +9.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 378 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 348 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +10.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 564 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -14.1) |
| [[SHP-77 (line)]] | alt | 229 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.556× (z -10.7) |
| [[SW 1088 (line)]] | alt | 758 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 723 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 486 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 378 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7691), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | +0.77 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[IQGAP1]] | +0.71 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[PRKCI]] | +0.63 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[LRRFIP1]] | +0.63 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ANXA2]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[RAC1]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[RHOA]] | +0.58 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[EZR]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[RTN4]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ANXA1]] | +0.58 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[CHP1]] | +0.58 | +0.35 / +0.51 | both halves | 1e-04 |  |
| [[NBEAL1]] | +0.57 | +0.51 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRM1]] | -0.62 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[STARD7-AS1]] | -0.60 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SLC5A6]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[SPRYD4]] | -0.58 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[DUS3L]] | -0.56 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[LATS1]] | -0.56 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[UQCRFS1]] | -0.56 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[PATZ1]] | -0.56 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[C2orf42]] | -0.55 | -0.37 / -0.37 | both halves | 9e-05 |  |
| [[TIRAP-AS1]] | -0.55 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[ZNF689]] | -0.55 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[ZCCHC3]] | -0.55 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2B4]] | B | ATP2B4 activity raises CAST's level | lines that do not express ATP2B4 (8) vs lines expressing it (42) | 1.86× lower at baseline in the lines without ATP2B4 | 0.022 | ⚠ within organs, on part of the lines; also absent: PROCR, ARSJ, LAMB1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 111]] — Cell-Cell communication; 43 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.3, 9.6); signed map (-10.5, 33.9). **Vector** length 133, 46.2% of its response variance represented; |z| ≥ 3 in 1,392 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *RHOV GTPase cycle* (reactome, mean cos +0.53 to 4); *RHO GTPases activate PKNs* (reactome, mean cos +0.52 to 4); *RHO GTPases activate KTN1* (reactome, mean cos +0.52 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.3 | +14.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.6 | +0.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.2 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +5.2 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.8 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.8 | -10.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.3 | -10.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -8.0 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -4.9 | -2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.1 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | calpastatin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q15 — chr5:96,525,267-96,779,595 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MIR583HG |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 6 pathways, smallest: Deregulated CDK5 triggers multiple neurodegenerative pathways in Alzheimer's disease models; Neurodegenerative Diseases; Defective Intrinsic Pathway for Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P20810](https://www.uniprot.org/uniprotkb/P20810) (Calpastatin):

> Specific inhibition of calpain (calcium-dependent cysteine protease). Plays a key role in postmortem tenderization of meat and have been proposed to be involved in muscle protein degradation in living tissue.

**Summary**, from NCBI Gene [831](https://www.ncbi.nlm.nih.gov/gene/831):

> The protein encoded by this gene is an endogenous calpain (calcium-dependent cysteine protease) inhibitor. It consists of an N-terminal domain L and four repetitive calpain-inhibition domains (domains 1-4), and it is involved in the proteolysis of amyloid precursor protein. The calpain/calpastatin system is involved in numerous membrane fusion events, such as neural vesicle exocytosis and platelet and red-cell aggregation. The encoded protein is also thought to affect the expression levels of …

**Accessions** — [HGNC:1515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1515) · Entrez [831](https://www.ncbi.nlm.nih.gov/gene/831) · UniProt [P20810](https://www.uniprot.org/uniprotkb/P20810) · Ensembl [ENSG00000153113](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153113)

## Data

Gene col 7691: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7691); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7691, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7691]; `tensor/DDL_lfc|DDL_z.npy` [7691]; `embed/gene_vectors.npy` [7691]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7691 or target_col == 7691). Every well: [[CAST — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAST.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
