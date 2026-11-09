---
symbol: "ANKHD1"
type: "gene"
col: 5219
ensembl_id: "ENSG00000131503"
name: "ankyrin repeat and KH domain containing 1"
location: "5q31.3"
module: 74
arm: "+"
pooled_cpm: 388.95
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# ANKHD1

*ankyrin repeat and KH domain containing 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.75× (z +22.8, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.494× (z -19.6, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-427 0.270×, HCT15 0.244×, KATO III 0.265×, LoVo 0.361×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HEC-1-A 0.332×, A549 0.371×, A-172 0.338×, LoVo 0.406×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.392×, PANC-1 0.453×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.679×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASH1L]] (+0.67, fdr 7e-06), [[RSF1]] (+0.64, fdr 7e-06), [[ZMYM5]] (+0.63, fdr 7e-06); moves opposite to [[DLST]] (-0.62, fdr 1e-05), [[LINC03009]] (-0.60, fdr 1e-05), [[RFT1]] (-0.60, fdr 2e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5219.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +22.8 | 0e+00 | 46/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.79×** | +16.8 | 0e+00 | 46/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +16.4 | 0e+00 | 48/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +13.1 | 5e-37 | 44/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +12.9 | 5e-36 | 42/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.17×** | +11.7 | 7e-30 | 43/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +10.6 | 3e-24 | 44/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +10.4 | 1e-23 | 37/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +8.3 | 7e-15 | 33/48 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +6.4 | 7e-09 | 21/49 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.13× | +3.6 | 0.018 | 15/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | 1.13× | +3.4 | 0.034 | 19/47 (NCI-H23, SHP-77, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.060 | 16/48 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.066 | 13/48 (A-427, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5219.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A-427 0.270×, HCT15 0.244×, KATO III 0.265×, LoVo 0.361×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HEC-1-A 0.332×, A549 0.371×, A-172 0.338×, LoVo 0.406×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 0.392×, PANC-1 0.453×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW480 0.679×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -19.6 | 0e+00 | 44/44 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.501×** | -18.2 | 0e+00 | 48/49 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.588×** | -14.2 | 9e-44 | 45/45 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -9.2 | 7e-18 | 44/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.889× | -4.8 | 1e-04 | 9/48 (KATO III, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -4.4 | 1e-03 | 18/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.848× | -4.3 | 0.001 | 20/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.927× | -3.1 | 0.12 | 0/48 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5219. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 374 | 13 (4 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +30.3) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -17.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 395 | 10 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +27.6) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -17.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 362 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +18.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.482× (z -12.6) ⚠ toxic |
| [[LoVo (line)]] | wt | 567 | 8 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +25.2) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -22.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 291 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -12.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 304 | 8 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -13.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 424 | 6 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.48× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -17.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 365 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.494× (z -12.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 331 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +25.2) | [[Dinaciclib (drug)]] 5 µM 0.642× (z -8.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 369 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +18.9) | [[Dinaciclib (drug)]] 0.5 µM 0.496× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 532 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +18.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -19.1) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 352 | 7 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.392× (z -13.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 324 | 4 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -20.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 414 | 5 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -15.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 295 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +22.0) | — |
| [[A-427 (line)]] | wt | 395 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.77× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -29.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 383 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -18.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 245 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +24.5) | — |
| [[HT-29 (line)]] | alt | 521 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -14.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 433 | 3 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.18× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -22.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 472 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 330 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +18.9) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -14.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 446 | 2 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.81× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.487× (z -13.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 309 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -14.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 324 | 6 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.64× (z +13.0) | [[Dinaciclib (drug)]] 0.05 µM 0.438× (z -10.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 392 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +13.9) | — |
| [[COLO 205 (line)]] | alt | 657 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.85× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -13.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 451 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.73× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.332× (z -19.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 364 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.348× (z -16.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 388 | 5 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.66× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.516× (z -13.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 298 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.513× (z -13.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 303 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -14.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 539 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -23.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 276 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -11.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 311 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +23.5) | [[Dinaciclib (drug)]] 0.5 µM 0.509× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 412 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.415× (z -15.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 352 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.386× (z -15.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 660 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.445× (z -15.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 314 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +18.1) | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -19.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 306 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.30× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -14.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 366 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.54× (z +8.6) | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -13.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 291 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.463× (z -9.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 316 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +11.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.403× (z -14.2) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 536 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -11.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 345 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 430 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 397 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 301 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 443 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 567 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5219), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASH1L]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 | STRING 457 |
| [[RSF1]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[ANKHD1-EIF4EBP3]] | +0.63 | +0.60 / +0.70 | both halves | 7e-06 | ⚠ **readthrough risk**: ANKHD1-EIF4EBP3 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[FKBP2]] ⚠ | +0.60 | +0.47 / +0.56 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ANKRD12]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 | same gene group |
| [[CHD2]] | +0.60 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[FAM193A]] | +0.59 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[UPF2]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[UXT]] | +0.58 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[GGNBP2]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[OSBP]] | +0.57 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[AKAP9]] | +0.57 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[YY1]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLST]] | -0.62 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[LINC03009]] | -0.60 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[RFT1]] | -0.60 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[BTBD1]] | -0.59 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[NAE1]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[POMGNT1]] | -0.57 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[GLO1]] | -0.57 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[ATP13A2]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TOMM34]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SORD]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SMYD2]] | -0.56 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ZDHHC21]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.6, -45.8); signed map (-8.0, 5.7). **Vector** length 128, 49.8% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Binimetinib (drug)]] 0.05 µM |  | +5.0 | +1.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +1.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +4.2 | +2.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.1 | +16.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.0 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.3 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.4 | -14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -4.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.3 | -19.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -5.7 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -1.9 |
|  | [[Adenine (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and KH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:140,401,814-140,539,856 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MASK, FLJ20288, FLJ11979, FLJ10042, FLJ14127, KIAA1085, MASK1 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWZ3](https://www.uniprot.org/uniprotkb/Q8IWZ3) (Ankyrin repeat and KH domain-containing protein 1):

> May play a role as a scaffolding protein that may be associated with the abnormal phenotype of leukemia cells. Isoform 2 may possess an antiapoptotic effect and protect cells during normal cell survival through its regulation of caspases.

**Summary**, from NCBI Gene [54882](https://www.ncbi.nlm.nih.gov/gene/54882):

> This gene encodes a protein with multiple ankyrin repeat domains and a single KH-domain. The protein is thought to function as a scaffolding protein, and it may be involved in the regulation of caspases and thereby play an antiapoptotic role in cell survival. Alternative splicing results in multiple transcript variants, one of which generates a fusion transcript (MASK-BP3) with the downstream eIF4E-binding protein 3 (EIF4EBP3) gene, resulting in a protein comprised of the ANKHD1 sequence for …

**Accessions** — [HGNC:24714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24714) · Entrez [54882](https://www.ncbi.nlm.nih.gov/gene/54882) · UniProt [Q8IWZ3](https://www.uniprot.org/uniprotkb/Q8IWZ3) · Ensembl [ENSG00000131503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131503)

## Data

Gene col 5219: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5219); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5219, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5219]; `tensor/DDL_lfc|DDL_z.npy` [5219]; `embed/gene_vectors.npy` [5219]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5219 or target_col == 5219). Every well: [[ANKHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
