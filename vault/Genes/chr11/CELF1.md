---
symbol: "CELF1"
type: "gene"
col: 7348
ensembl_id: "ENSG00000149187"
name: "CUGBP Elav-like family member 1"
location: "11p11.2"
module: 58
arm: "+"
pooled_cpm: 293.99
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# CELF1

*CUGBP Elav-like family member 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 2.10× (z +17.8, q 0e+00, up in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.72× (z +13.0, q 2e-36, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.651× (z -14.6, q 3e-45, down in 45 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (A-172 0.476×, SNU-423 0.490×, Hs 766T 0.508×, J82 0.545×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.205×, SNU-1 0.168×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.435×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.649×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPKBP1]] (+0.60, fdr 9e-05), [[NSUN5P2-1]] (+0.60, fdr 2e-04, ⚠ NSUN5P2-1 in the vector space only through flagged drug-doses), [[ZNF316]] (+0.59, fdr 4e-05), [[NSUN5P1-1]] (+0.59, fdr 2e-04); moves opposite to [[ARF1]] (-0.60, fdr 3e-05), [[TWF1]] (-0.60, fdr 1e-05), [[PGRMC1]] (-0.58, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +17.8 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +13.0 | 2e-36 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +11.2 | 1e-26 | 44/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +10.8 | 4e-25 | 46/49 (Panc 03.27, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +9.7 | 2e-20 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +8.6 | 5e-16 | 42/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +6.9 | 4e-10 | 38/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +6.4 | 1e-08 | 34/48 (C32, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +5.7 | 9e-07 | 42/48 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +5.3 | 6e-06 | 24/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 4e-05 | 40/48 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +4.7 | 1e-04 | 15/49 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.21×** | +4.6 | 2e-04 | 25/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +4.4 | 4e-04 | 24/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +4.2 | 8e-04 | 22/48 (Hs 766T, HEC-1-A, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.0 | 0.002 | 22/48 (SW480, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.18× | +3.9 | 0.003 | 19/48 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.009 | 26/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.014 | 25/49 (PANC-1, hTERT-HPNE, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.016 | 25/48 (CFPAC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7348.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 14 lines (A-172 0.476×, SNU-423 0.490×, Hs 766T 0.508×, J82 0.545×, …); [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.205×, SNU-1 0.168×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.435×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-172 0.649×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.651×** | -14.6 | 3e-45 | 45/49 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.813×** | -5.0 | 2e-04 | 28/48 (BT-474, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | 0.834× | -4.2 | 0.005 | 23/47 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.835× | -4.2 | 0.005 | 21/44 (SK-MEL-2, SNU-1, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.850× | -3.8 | 0.020 | 21/50 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.907× | -3.3 | 0.094 | 13/48 (A-172, HOP62, …) | rises with dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.882× | -3.0 | 0.21 | 6/48 (A498, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 192 | 6 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.91× (z +16.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.483× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -9.9) |
| [[SW480 (line)]] | alt | 347 | 8 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.76× (z +20.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +17.0) | — |
| [[HT-29 (line)]] | alt | 259 | 6 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.29× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 215 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.11× (z +19.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +16.6) | — |
| [[PANC-1 (line)]] | alt | 322 | 6 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.39× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +16.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 358 | 5 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 6.42× (z +14.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -8.6) |
| [[Hs 766T (line)]] | wt | 291 | 5 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.29× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -16.5) |
| [[J82 (line)]] | alt | 410 | 5 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.09× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -16.2) |
| [[KATO III (line)]] | alt | 264 | 5 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.47× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.660× (z -10.6) |
| [[BT-474 (line)]] | alt | 327 | 3 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -14.7) |
| [[COLO 205 (line)]] | alt | 178 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.59× (z +12.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.10× (z +9.9) | — |
| [[H4 (line)]] | wt | 248 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.79× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 213 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.88× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 227 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.63× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 324 | 2 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.79× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -14.5) |
| [[Panc 03.27 (line)]] | alt | 352 | 4 (1 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 5.45× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -13.2) |
| [[SNU-423 (line)]] | alt | 330 | 4 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.10× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -17.0) |
| [[SW1417 (line)]] | alt | 356 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.42× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.548× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 357 | 1 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.56× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -20.3) |
| [[CFPAC-1 (line)]] | alt | 340 | 3 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.87× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.30× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -14.0) |
| [[HOP62 (line)]] | alt | 270 | 3 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.12× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.63× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -12.5) |
| [[LoVo (line)]] | wt | 254 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.45× (z +14.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.6) | — |
| [[LOX-IMVI (line)]] | wt | 368 | 3 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.599× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 424 | 1 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.82× (z +9.9) ⚠ toxic; transcription drop | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.452× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 261 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.39× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.87× (z +9.8) | — |
| [[RKO (line)]] | wt | 407 | 2 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.81× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.08× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 203 | 2 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.14× (z +10.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 305 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -11.3) |
| [[SNU-1 (line)]] | wt | 281 | 1 (1 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.00× (z +8.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.168× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.3) |
| [[SW48 (line)]] | wt | 292 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.49× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -9.4) |
| [[A498 (line)]] | wt | 337 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.07× (z +9.3) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -8.6) |
| [[A549 (line)]] | wt | 298 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 1.92× (z +11.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -13.1) |
| [[C-33 A (line)]] | alt | 320 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.77× (z +9.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.497× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 216 | 2 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 4.55× (z +9.7) | — |
| [[HCT15 (line)]] | alt | 348 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.91× (z +10.2) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.559× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 332 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -15.5) |
| [[HS-578T (line)]] | alt | 222 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.26× (z +11.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -11.4) |
| [[SHP-77 (line)]] | alt | 271 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +10.2) | — |
| [[A-427 (line)]] | wt | 274 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.68× (z +9.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 284 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 217 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.12× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 216 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.23× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 250 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.97× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 126 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.35× (z +9.7) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 303 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 316 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKBP1]] | +0.60 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[NSUN5P2-1]] ⚠ | +0.60 | +0.32 / +0.57 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF316]] | +0.59 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[NSUN5P1-1]] | +0.59 | +0.31 / +0.60 | both halves | 2e-04 |  |
| [[RPS26]] | +0.57 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[ANTKMT]] | +0.56 | +0.30 / +0.46 | both halves | 2e-04 |  |
| [[RBM6]] | +0.56 | +0.46 / +0.46 | both halves | 3e-05 | same gene group |
| [[DVL1]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[B3GALT6]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[HAGHL]] | +0.55 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[SELENOO]] | +0.55 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[VPS37C]] | +0.55 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[EIF5B]] | +0.55 | +0.32 / +0.50 | both halves | 2e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARF1]] | -0.60 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[TWF1]] | -0.60 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[PGRMC1]] | -0.58 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[THAP9]] | -0.57 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CMPK1]] | -0.56 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[NCSTN]] | -0.55 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[PRKAR1A]] | -0.54 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[EIF4G2]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[HDLBP]] | -0.54 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[TLN1]] | -0.53 | -0.43 / -0.45 | both halves | 4e-05 |  |
| [[EIF4H]] | -0.53 | -0.40 / -0.48 | both halves | 4e-05 | same gene group |
| [[STYX]] | -0.53 | -0.52 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.8, -21.7); signed map (-29.4, 5.1). **Vector** length 114, 42.1% of its response variance represented; |z| ≥ 3 in 1,223 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +6.7 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.4 | +0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +5.0 | +2.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +17.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | -0.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +4.1 | +2.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.9 | +4.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +3.8 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -14.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.2 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.9 | -5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | +1.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -3.3 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.8 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -2.8 | -1.3 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -2.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | CUGBP Elav-like family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,465,933-47,565,569 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CUG-BP, hNab50, BRUNOL2, NAB50, CUGBP, NAPOR, EDEN-BP; previously CUGBP1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92879](https://www.uniprot.org/uniprotkb/Q92879) (CUGBP Elav-like family member 1):

> RNA-binding protein implicated in the regulation of several post-transcriptional events. Involved in pre-mRNA alternative splicing, mRNA translation and stability. Mediates exon inclusion and/or exclusion in pre-mRNA that are subject to tissue-specific and developmentally regulated alternative splicing. Specifically activates exon 5 inclusion of cardiac isoforms of TNNT2 during heart remodeling at the juvenile to adult transition. Acts both as an activator and as a repressor of a pair of …

**Summary**, from NCBI Gene [10658](https://www.ncbi.nlm.nih.gov/gene/10658):

> Members of the CELF/BRUNOL protein family contain two N-terminal RNA recognition motif (RRM) domains, one C-terminal RRM domain, and a divergent segment of 160-230 aa between the second and third RRM domains. Members of this protein family regulate pre-mRNA alternative splicing and may also be involved in mRNA editing, and translation. This gene may play a role in myotonic dystrophy type 1 (DM1) via interactions with the dystrophia myotonica-protein kinase (DMPK) gene. Alternative splicing …

**Accessions** — [HGNC:2549](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2549) · Entrez [10658](https://www.ncbi.nlm.nih.gov/gene/10658) · UniProt [Q92879](https://www.uniprot.org/uniprotkb/Q92879) · Ensembl [ENSG00000149187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149187)

## Data

Gene col 7348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7348); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7348]; `tensor/DDL_lfc|DDL_z.npy` [7348]; `embed/gene_vectors.npy` [7348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7348 or target_col == 7348). Every well: [[CELF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CELF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
