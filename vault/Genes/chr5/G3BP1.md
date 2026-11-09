---
symbol: "G3BP1"
type: "gene"
col: 7038
ensembl_id: "ENSG00000145907"
name: "G3BP stress granule assembly factor 1"
location: "5q33.1"
module: 4
arm: "+"
pooled_cpm: 209.48
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# G3BP1

*G3BP stress granule assembly factor 1* — 5q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.87× (z +21.8, q 0e+00, up in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.67× (z +12.7, q 1e-34, up in 37 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HEC-1-A 0.607×, SK-MEL-2 0.537×, C32 0.517×, NCI-H460 0.635×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.489×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX9]] (+0.73, fdr 7e-06), [[RUVBL1]] (+0.69, fdr 7e-06), [[CCT2]] (+0.69, fdr 7e-06); moves opposite to [[FBXL12]] (-0.72, fdr 7e-06), [[TMEM258]] (-0.65, fdr 7e-06), [[TERF2IP]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SACS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7038.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.87×** | +21.8 | 0e+00 | 42/48 (LoVo, hTERT-HPNE, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.95×** | +16.4 | 0e+00 | 48/49 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.97×** | +16.1 | 0e+00 | 44/44 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +15.5 | 0e+00 | 46/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.72×** | +13.4 | 8e-39 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +12.7 | 1e-34 | 37/48 (Panc 03.27, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.87×** | +12.4 | 1e-33 | 48/49 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.65×** | +12.3 | 7e-33 | 45/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.82×** | +12.2 | 1e-32 | 47/48 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.61×** | +11.7 | 6e-30 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.62×** | +11.5 | 7e-29 | 39/48 (COLO 205, HEC-1-A, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +11.0 | 2e-26 | 44/48 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +10.6 | 9e-25 | 45/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.57×** | +10.3 | 3e-23 | 32/45 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +9.9 | 2e-21 | 41/48 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +8.7 | 1e-16 | 35/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +5.3 | 3e-06 | 25/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.002 | 24/49 (NCI-H1573, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +3.9 | 0.002 | 10/48 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.9 | 0.002 | 18/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.006 | 10/49 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.12× | +2.8 | 0.080 | 10/47 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.13× | +2.8 | 0.081 | 17/48 (NCI-H460, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7038.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (HEC-1-A 0.607×, SK-MEL-2 0.537×, C32 0.517×, NCI-H460 0.635×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (SW1417 0.489×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.870× | -4.9 | 6e-04 | 10/48 (A-427, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -4.6 | 0.001 | 20/49 (HEC-1-A, SK-MEL-2, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.847× | -4.1 | 0.006 | 19/48 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.862× | -3.5 | 0.056 | 19/47 (SW1417, HEC-1-A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.873× | -3.4 | 0.072 | 11/47 (NCI-H2030, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.869× | -3.4 | 0.072 | 13/48 (SW 1088, KATO III, …) | top dose only |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.882× | -3.1 | 0.14 | 11/48 (LS 180, SNU-423, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.883× | -3.1 | 0.14 | 10/48 (KATO III, COLO 205, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.882× | -3.0 | 0.15 | 11/49 (NCI-H1792, A-172, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7038. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 208 | 13 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +16.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +12.0) | — |
| [[LoVo (line)]] | wt | 234 | 13 (10 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +20.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.34× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 209 | 13 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +17.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.21× (z +11.2) | — |
| [[COLO 205 (line)]] | alt | 126 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +20.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 207 | 12 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +19.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +14.4) | — |
| [[NCI-H460 (line)]] | wt | 204 | 10 (9 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +15.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.69× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 232 | 11 (10 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.40× (z +18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.09× (z +8.7) | — |
| [[A549 (line)]] | wt | 160 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.19× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 388 | 9 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +20.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.92× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 103 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +18.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 135 | 10 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +18.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +9.2) | — |
| [[A-172 (line)]] | wt | 216 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +19.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.70× (z +12.3) | — |
| [[C32 (line)]] | wt | 209 | 8 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 7.82× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 138 | 9 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +20.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +10.9) | — |
| [[KATO III (line)]] | alt | 160 | 9 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.91× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 135 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +14.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.23× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 199 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +16.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.54× (z +13.5) | — |
| [[HT-29 (line)]] | alt | 180 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 1.97× (z +9.9) | — |
| [[LS 180 (line)]] | wt | 224 | 8 (7 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +15.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.26× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 203 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 276 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.61× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 5.16× (z +10.9) | — |
| [[PANC-1 (line)]] | alt | 232 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.26× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.49× (z +10.2) | — |
| [[SW48 (line)]] | wt | 184 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.18× (z +14.2) | — |
| [[Hs 766T (line)]] | wt | 201 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[J82 (line)]] | alt | 248 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 248 | 3 (3 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.56× (z +13.0) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 164 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | — |
| [[HS-578T (line)]] | alt | 204 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +17.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.14× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 190 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.07× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 154 | 3 (3 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.83× (z +14.1) ⚠ toxic | — |
| [[SW1417 (line)]] | alt | 300 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.92× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.489× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 286 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 115 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[BT-474 (line)]] | alt | 136 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.86× (z +14.2) | — |
| [[RKO (line)]] | wt | 237 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.92× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW 900 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.7) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A-427 (line)]] | wt | 250 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.50× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 205 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H23 (line)]] | alt | 210 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SNU-1 (line)]] | wt | 223 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.10× (z +10.0) ⚠ toxic | — |
| [[SW 1271 (line)]] | alt | 317 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[C-33 A (line)]] | alt | 225 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 186 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 209 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 185 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7038), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX9]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 | STRING 472 |
| [[RUVBL1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[CCT2]] | +0.69 | +0.67 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[CCT5]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[STIP1]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 | STRING 410 |
| [[ATIC]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PRKDC]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[AGPS]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[USP14]] | +0.64 | +0.56 / +0.68 | both halves | 1e-05 | STRING 523 |
| [[PRPS1]] | +0.63 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[GLO1]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL12]] | -0.72 | -0.59 / -0.75 | both halves | 7e-06 |  |
| [[TMEM258]] | -0.65 | -0.59 / -0.70 | both halves | 7e-06 | pathway: SARS-CoV-2 Infection |
| [[TERF2IP]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[ZSWIM8]] | -0.64 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[ZMYM5]] | -0.64 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[ZFYVE1]] | -0.63 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[SYNRG]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TMEM134]] | -0.62 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[INAFM1]] | -0.61 | -0.56 / -0.68 | both halves | 1e-05 |  |
| [[TMEM106A]] | -0.61 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[FKBP2]] ⚠ | -0.60 | -0.57 / -0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DNAJC4]] | -0.60 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[TXNL4B]] | -0.60 | -0.42 / -0.53 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SACS]] | B | SACS activity raises G3BP1's level | lines that do not express SACS (5) vs lines expressing it (45) | 1.45× lower at baseline in the lines without SACS | 0.024 | ⚠ within organs, on part of the lines; also absent: CRTAP, SNTA1, TMCC2; maybe low, not absent |
| [[ALDH5A1]] | B | ALDH5A1 activity raises G3BP1's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.20× lower at baseline in the lines without ALDH5A1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.2, -32.8); signed map (-12.2, -45.1). **Vector** length 100, 37.2% of its response variance represented; |z| ≥ 3 in 1,542 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.58 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.1 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +5.1 | +16.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +4.9 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.8 | +10.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +12.2 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | +2.4 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.2 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -6.8 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.7 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.7 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -1.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.6 | -0.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | G3BP stress granule assembly factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.1 — chr5:151,771,045-151,812,911 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HDH-VIII, G3BP |
| Gene groups (HGNC) | RNA binding motif containing; Endoribonucleases |
| Hallmark sets | G2M_CHECKPOINT, MYC_TARGETS_V1 |
| Reactome | 5 pathways, smallest: SARS-CoV-2 activates/modulates innate and adaptive immune responses; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13283](https://www.uniprot.org/uniprotkb/Q13283) (Ras GTPase-activating protein-binding protein 1):

> Protein involved in various processes, such as stress granule formation and innate immunity. Plays an essential role in stress granule formation. Stress granules are membraneless compartments that store mRNAs and proteins, such as stalled translation pre-initiation complexes, in response to stress. Promotes formation of stress granules phase-separated membraneless compartment by undergoing liquid-liquid phase separation (LLPS) upon unfolded RNA-binding: functions as a molecular switch that …

**Summary**, from NCBI Gene [10146](https://www.ncbi.nlm.nih.gov/gene/10146):

> This gene encodes one of the DNA-unwinding enzymes which prefers partially unwound 3'-tailed substrates and can also unwind partial RNA/DNA and RNA/RNA duplexes in an ATP-dependent fashion. This enzyme is a member of the heterogeneous nuclear RNA-binding proteins and is also an element of the Ras signal transduction pathway. It binds specifically to the Ras-GTPase-activating protein by associating with its SH3 domain. Several alternatively spliced transcript variants of this gene have been …

**Accessions** — [HGNC:30292](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30292) · Entrez [10146](https://www.ncbi.nlm.nih.gov/gene/10146) · UniProt [Q13283](https://www.uniprot.org/uniprotkb/Q13283) · Ensembl [ENSG00000145907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145907)

## Data

Gene col 7038: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7038); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7038, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7038]; `tensor/DDL_lfc|DDL_z.npy` [7038]; `embed/gene_vectors.npy` [7038]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7038 or target_col == 7038). Every well: [[G3BP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/G3BP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
