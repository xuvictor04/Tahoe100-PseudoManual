---
symbol: "SPAG9"
type: "gene"
col: 166
ensembl_id: "ENSG00000008294"
name: "sperm associated antigen 9"
location: "17q21.33"
module: 5
arm: "-"
pooled_cpm: 621.31
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 9
n_dd_up_clean: 21
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SPAG9

*sperm associated antigen 9* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.47× (z +30.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.476× (z -12.3, q 4e-32, down in 47 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.621× (z -8.2, q 6e-14, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAST]] (+0.77, fdr 7e-06), [[NBEAL1]] (+0.69, fdr 1e-05), [[DNAAF3]] (+0.61, fdr 5e-04); moves opposite to [[PATZ1]] (-0.65, fdr 1e-05), [[TGFBRAP1]] (-0.65, fdr 1e-05), [[PRCC]] (-0.64, fdr 3e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AHNAK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.47×** | +30.2 | 0e+00 | 46/48 (Panc 03.27, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.54×** | +16.0 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.28×** | +14.2 | 2e-43 | 43/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +13.7 | 2e-40 | 43/48 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.05×** | +12.3 | 9e-33 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +11.9 | 2e-30 | 46/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +11.2 | 4e-27 | 46/48 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.86×** | +10.7 | 9e-25 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +10.0 | 1e-21 | 45/48 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +9.9 | 1e-21 | 46/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +9.4 | 2e-19 | 40/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.48×** | +8.2 | 2e-14 | 46/49 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.39×** | +5.6 | 8e-07 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +4.9 | 4e-05 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.72×** | +4.8 | 5e-05 | 35/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.7 | 7e-05 | 38/49 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.3 | 6e-04 | 30/48 (A-427, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.476×** | -12.3 | 4e-32 | 47/47 (HT-29, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.621×** | -8.2 | 6e-14 | 46/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -7.9 | 7e-13 | 32/49 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.762×** | -6.7 | 4e-09 | 36/48 (A549, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.774×** | -4.4 | 1e-03 | 34/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.776×** | -4.2 | 0.002 | 28/44 (CFPAC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.791×** | -4.1 | 0.004 | 29/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.819×** | -3.5 | 0.031 | 24/49 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.869× | -3.5 | 0.031 | 14/48 (CFPAC-1, LoVo, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.821×** | -3.4 | 0.031 | 26/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.870× | -3.4 | 0.031 | 22/48 (NCI-H2347, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.835× | -3.1 | 0.081 | 23/48 (A549, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.957× | -3.0 | 0.11 | 1/50 (NCI-H23) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 858 | 14 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.42× (z +27.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -10.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -9.7) |
| [[LoVo (line)]] | wt | 421 | 12 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +26.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.510× (z -10.6) ⚠ toxic |
| [[A-427 (line)]] | wt | 470 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +20.5) | — |
| [[KATO III (line)]] | alt | 436 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +24.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.482× (z -8.9) ⚠ toxic |
| [[SW480 (line)]] | alt | 324 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +21.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.493× (z -9.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 448 | 9 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +28.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -9.2) |
| [[HOP62 (line)]] | alt | 720 | 9 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +27.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.384× (z -11.4) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.442× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 640 | 7 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +28.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.448× (z -11.3) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.534× (z -9.2) |
| [[PANC-1 (line)]] | alt | 723 | 9 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +25.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -12.1) |
| [[SW1417 (line)]] | alt | 484 | 10 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +26.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.532× (z -9.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 538 | 7 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +32.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.481× (z -10.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 446 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +22.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.467× (z -9.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 591 | 8 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +23.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.449× (z -10.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -8.8) |
| [[SNU-423 (line)]] | alt | 815 | 8 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +29.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 1,129 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +25.8) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.336× (z -13.8) |
| [[BT-474 (line)]] | alt | 327 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +19.4) | — |
| [[HT-29 (line)]] | alt | 455 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +23.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -12.4) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 476 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +29.2) | — |
| [[Panc 03.27 (line)]] | alt | 549 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.16× (z +35.3) | — |
| [[RKO (line)]] | wt | 316 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +20.8) | — |
| [[SNU-1 (line)]] | wt | 354 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +13.3) | — |
| [[COLO 205 (line)]] | alt | 546 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.02× (z +27.4) | — |
| [[HCT15 (line)]] | alt | 461 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.66× (z +12.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.458× (z -9.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 935 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +21.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.326× (z -12.2) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.466× (z -8.6) |
| [[J82 (line)]] | alt | 539 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +20.9) | — |
| [[RPMI-7951 (line)]] | alt | 398 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +28.4) | — |
| [[SW 900 (line)]] | alt | 730 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +20.4) | — |
| [[SW48 (line)]] | wt | 418 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +15.3) | — |
| [[A498 (line)]] | wt | 819 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +31.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -10.2) |
| [[A549 (line)]] | wt | 1,004 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +20.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -19.5) |
| [[CFPAC-1 (line)]] | alt | 1,003 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.493× (z -10.3) |
| [[Hs 766T (line)]] | wt | 544 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +22.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.433× (z -9.0) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 947 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +16.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -10.3) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 873 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +21.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 808 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +28.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.480× (z -8.6) ⚠ toxic |
| [[H4 (line)]] | wt | 657 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -9.1) |
| [[HS-578T (line)]] | alt | 798 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +22.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.377× (z -11.0) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 296 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.23× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 456 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 441 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -10.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 286 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +12.2) | — |
| [[C32 (line)]] | wt | 455 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +22.4) | — |
| [[CHP-212 (line)]] | wt | 636 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.73× (z +11.7) | — |
| [[NCI-H2030 (line)]] | alt | 523 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.6) | — |
| [[LOX-IMVI (line)]] | wt | 750 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.405× (z -9.1) ⚠ toxic |
| [[SW 1088 (line)]] | alt | 542 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +11.9) | — |
| [[SW 1271 (line)]] | alt | 730 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.0) | — |
| [[NCI-H2122 (line)]] | alt | 682 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 617 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 755 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*22 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAST]] | +0.77 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[NBEAL1]] | +0.69 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.61 | +0.53 / +0.24 | both halves | 5e-04 |  |
| [[SMG1]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[MAGT1]] | +0.58 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[DDAH2]] | +0.58 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[PJA2]] | +0.58 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[SKAP2]] | +0.58 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[F11R]] | +0.58 | +0.49 / +0.40 | both halves | 5e-05 |  |
| [[GNAI2]] | +0.58 | +0.43 / +0.25 | both halves | 4e-04 |  |
| [[PTPRH]] | +0.57 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[KLF2]] | +0.57 | +0.35 / +0.46 | both halves | 1e-04 |  |

## Genes that move opposite

*78 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PATZ1]] | -0.65 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | -0.65 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PRCC]] | -0.64 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[KLHL42]] | -0.64 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[STARD7-AS1]] | -0.63 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[SMAD1]] | -0.63 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ITPKB]] | -0.63 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[AKAP8]] | -0.63 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[GABPB1]] | -0.62 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[DUS3L]] | -0.62 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TLCD3A]] | -0.62 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[CCNJ]] | -0.61 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHNAK2]] | B | AHNAK2 activity raises SPAG9's level | lines that do not express AHNAK2 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without AHNAK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: CAV1, CAV2, ITGA2; maybe low, not absent |
| [[LRRC61]] | B | LRRC61 activity lowers SPAG9's level | lines that do not express LRRC61 (16) vs lines expressing it (34) | 1.38× higher at baseline in the lines without LRRC61 | 0.084 | ⚠ within organs, on part of the lines; also absent: ACTR3C, ARHGEF5, ENPP4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.548). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-7.0, 9.9); signed map (-19.0, 24.1). **Vector** length 109, 51.0% of its response variance represented; |z| ≥ 3 in 1,710 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +8.7 | +12.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.2 | +10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.2 | +11.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.7 | +2.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +5.7 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.6 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -13.3 | -12.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -9.6 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.0 | -7.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -6.3 | -3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.5 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -6.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -5.1 | -0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.7 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | sperm associated antigen 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,962,174-51,120,868 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSS, SYD1, KIAA0516, MGC14967, MGC74461, MGC117291, JLP, PHET |
| Reactome | 1 pathways, smallest: Myogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O60271](https://www.uniprot.org/uniprotkb/O60271) (C-Jun-amino-terminal kinase-interacting protein 4):

> The JNK-interacting protein (JIP) group of scaffold proteins selectively mediates JNK signaling by aggregating specific components of the MAPK cascade to form a functional JNK signaling module. Regulates lysosomal positioning by acting as an adapter protein which links PIP4P1-positive lysosomes to the dynein-dynactin complex. Assists PIKFYVE selective functionality in microtubule-based endosome-to-TGN trafficking (By similarity).

**Summary**, from NCBI Gene [9043](https://www.ncbi.nlm.nih.gov/gene/9043):

> This gene encodes a member of the cancer testis antigen gene family. The encoded protein functions as a scaffold protein that structurally organizes mitogen-activated protein kinases and mediates c-Jun-terminal kinase signaling. This protein also binds to kinesin-1 and may be involved in microtubule-based membrane transport. This protein may play a role in tumor growth and development. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:14524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14524) · Entrez [9043](https://www.ncbi.nlm.nih.gov/gene/9043) · UniProt [O60271](https://www.uniprot.org/uniprotkb/O60271) · Ensembl [ENSG00000008294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008294)

## Data

Gene col 166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 166); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 166]; `tensor/DDL_lfc|DDL_z.npy` [166]; `embed/gene_vectors.npy` [166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 166 or target_col == 166). Every well: [[SPAG9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPAG9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
