---
symbol: "AFF4"
type: "gene"
col: 1016
ensembl_id: "ENSG00000072364"
name: "ALF transcription elongation factor 4"
location: "5q31.1"
module: 16
arm: "+"
pooled_cpm: 369.28
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# AFF4

*ALF transcription elongation factor 4* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.52× (z +29.5, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -11.3, q 1e-26, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYRM2]] (+0.62, fdr 5e-05), [[FNBP1P1]] (+0.56, fdr 8e-05), [[ATP7A]] (+0.56, fdr 3e-05); moves opposite to [[TAF5]] (-0.62, fdr 2e-04), [[NDC1]] (-0.60, fdr 4e-05), [[NUP93]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAR2P1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1016.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.52×** | +29.5 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +16.1 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.91×** | +14.1 | 9e-43 | 48/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +13.4 | 5e-39 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +11.2 | 3e-27 | 48/49 (NCI-H1573, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +11.2 | 3e-27 | 41/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +10.7 | 1e-24 | 41/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +10.6 | 2e-24 | 42/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +9.3 | 8e-19 | 45/48 (SW480, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +8.8 | 1e-16 | 44/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +8.1 | 3e-14 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +5.4 | 4e-06 | 32/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.0 | 0.002 | 23/48 (PANC-1, Panc 03.27, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.9 | 0.004 | 21/48 (KATO III, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.8 | 0.006 | 15/48 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.008 | 23/48 (PANC-1, A498, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.035 | 11/48 (KATO III, AN3 CA, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.045 | 18/47 (NCI-H460, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1016.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -11.3 | 1e-26 | 45/49 (NCI-H1792, SNU-423, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -7.8 | 2e-12 | 42/47 (NCI-H2347, CHP-212, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.747×** | -6.6 | 1e-08 | 35/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.754×** | -6.1 | 2e-07 | 37/50 (C32, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.765×** | -5.8 | 7e-07 | 35/48 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.779×** | -5.4 | 6e-06 | 26/44 (SK-MEL-2, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -4.6 | 3e-04 | 0/50 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.817×** | -4.6 | 4e-04 | 27/48 (AN3 CA, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 0.873× | -4.3 | 1e-03 | 4/48 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.826×** | -4.3 | 1e-03 | 26/48 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.877× | -4.2 | 0.002 | 15/48 (A-172, AN3 CA, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.833×** | -4.1 | 0.002 | 23/48 (SW 900, C32, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.835× | -4.1 | 0.002 | 24/48 (C32, HOP62, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.020 | 29/48 (AN3 CA, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.823×** | -3.1 | 0.063 | 22/49 (RPMI-7951, HepG2/C3A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 0.5 µM |  | 0.871× | -3.1 | 0.063 | 5/48 (NCI-H1573, SW 1271, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.909× | -3.0 | 0.080 | 3/48 (AsPC-1, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1016. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 381 | 15 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +37.5) | — |
| [[SW480 (line)]] | alt | 284 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +21.2) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -9.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[PANC-1 (line)]] | alt | 242 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +33.2) | — |
| [[NCI-H1573 (line)]] | alt | 366 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +32.9) | [[Dinaciclib (drug)]] 5 µM 0.521× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SNU-1 (line)]] | wt | 308 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +19.6) | — |
| [[C32 (line)]] | wt | 432 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 504 | 4 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +18.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -13.6) |
| [[RKO (line)]] | wt | 320 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +22.3) | — |
| [[A-172 (line)]] | wt | 487 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +22.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.637× (z -9.1) |
| [[A-427 (line)]] | wt | 411 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 305 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +29.2) | [[Dinaciclib (drug)]] 0.05 µM 0.560× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[BT-474 (line)]] | alt | 277 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -11.6) |
| [[Hs 766T (line)]] | wt | 364 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +28.3) | — |
| [[HS-578T (line)]] | alt | 419 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +19.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.3) |
| [[KATO III (line)]] | alt | 236 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +19.0) | — |
| [[LoVo (line)]] | wt | 352 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.655× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 555 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +25.6) | — |
| [[Panc 03.27 (line)]] | alt | 399 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +22.2) | — |
| [[SNU-423 (line)]] | alt | 571 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +18.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -14.8) |
| [[A549 (line)]] | wt | 265 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +26.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 463 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +25.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 427 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 276 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +20.6) | — |
| [[NCI-H2030 (line)]] | alt | 381 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +22.2) | — |
| [[SK-MEL-2 (line)]] | alt | 523 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +26.5) | [[Dinaciclib (drug)]] 5 µM 0.370× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW 900 (line)]] | alt | 385 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.588× (z -8.5) ⚠ cell-cycle shift, explains ~63% of this change |
| [[SW1417 (line)]] | alt | 226 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +20.2) | — |
| [[A498 (line)]] | wt | 315 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +27.6) | — |
| [[CFPAC-1 (line)]] | alt | 544 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -11.5) |
| [[HT-29 (line)]] | alt | 325 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +24.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.579× (z -9.2) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 329 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +21.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.470× (z -10.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1792 (line)]] | alt | 332 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -17.1) |
| [[RPMI-7951 (line)]] | alt | 367 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +18.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -8.5) |
| [[AN3 CA (line)]] | alt | 705 | 1 | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.42× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -12.8) |
| [[COLO 205 (line)]] | alt | 400 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +18.0) | — |
| [[HEC-1-A (line)]] | alt | 376 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +21.2) | — |
| [[HOP62 (line)]] | alt | 457 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +18.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[J82 (line)]] | alt | 413 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +23.4) | — |
| [[H4 (line)]] | wt | 416 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +15.9) | — |
| [[HCT15 (line)]] | alt | 442 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.5) | — |
| [[LS 180 (line)]] | wt | 266 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +13.3) | — |
| [[SW48 (line)]] | wt | 283 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +13.1) | — |
| [[CHP-212 (line)]] | wt | 389 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.359× (z -10.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -8.6) |
| [[SHP-77 (line)]] | alt | 215 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.6) | — |
| [[SW 1088 (line)]] | alt | 520 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 410 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 371 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 312 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 530 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1016), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYRM2]] | +0.62 | +0.40 / +0.57 | both halves | 5e-05 |  |
| [[FNBP1P1]] | +0.56 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[ATP7A]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[BCL10]] | +0.55 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ZNF770]] | +0.54 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[PABIR1]] | +0.54 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[FMO4]] | +0.54 | +0.27 / +0.55 | both halves | 3e-04 |  |
| [[SDCBP]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[TOR1AIP1]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ZNF426]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[NKIRAS2]] | +0.53 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[HULC]] | +0.53 | +0.28 / +0.46 | both halves | 3e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF5]] | -0.62 | -0.31 / -0.76 | both halves | 2e-04 | pathway: Affinity selection of immunoglobulins |
| [[NDC1]] | -0.60 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[NUP93]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[POC1A]] | -0.57 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[MFSD14CP]] | -0.56 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[NDUFAF6]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[FOXK2]] | -0.56 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[CMC2]] | -0.55 | -0.34 / -0.61 | both halves | 1e-04 |  |
| [[GLRX5]] | -0.55 | -0.39 / -0.66 | both halves | 6e-05 |  |
| [[TOMM5]] | -0.54 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[ZMYND19]] | -0.54 | -0.39 / -0.66 | both halves | 6e-05 |  |
| [[DTYMK]] | -0.53 | -0.49 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAR2P1]] | B | FAR2P1 activity lowers AFF4's level | lines that do not express FAR2P1 (29) vs lines expressing it (21) | 1.15× higher at baseline in the lines without FAR2P1 | 0.047 | ⚠ within organs, on part of the lines; co-absent genes; also absent: POTEE, ENSG00000264660, ENSG00000286329 |
| [[TOP2A]] | B | TOP2A activity raises AFF4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.5, -46.0); signed map (9.1, -0.7). **Vector** length 97.7, 40.9% of its response variance represented; |z| ≥ 3 in 1,416 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.3 | +9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.0 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +7.9 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +7.7 | -6.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +5.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.0 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.6 | +3.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.5 | +1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.4 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -11.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.5 | -6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | +0.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | ALF transcription elongation factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,875,395-132,963,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AF5Q31, MCEF |
| Gene groups (HGNC) | AF4/FMR2 family; Super elongation complex |
| Reactome | 7 pathways, smallest: Formation of RNA Pol II elongation complex; RNA Polymerase II Transcription Elongation; RNA Polymerase II Pre-transcription Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHB7](https://www.uniprot.org/uniprotkb/Q9UHB7) (AF4/FMR2 family member 4):

> Key component of the super elongation complex (SEC), a complex required to increase the catalytic rate of RNA polymerase II transcription by suppressing transient pausing by the polymerase at multiple sites along the DNA. In the SEC complex, AFF4 acts as a central scaffold that recruits other factors through direct interactions with ELL proteins (ELL, ELL2 or ELL3) and the P-TEFb complex. In case of infection by HIV-1 virus, the SEC complex is recruited by the viral Tat protein to stimulate …

**Summary**, from NCBI Gene [27125](https://www.ncbi.nlm.nih.gov/gene/27125):

> The protein encoded by this gene belongs to the AF4 family of transcription factors involved in leukemia. It is a component of the positive transcription elongation factor b (P-TEFb) complex. A chromosomal translocation involving this gene and MLL gene on chromosome 11 is found in infant acute lymphoblastic leukemia with ins(5;11)(q31;q31q23). [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:17869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17869) · Entrez [27125](https://www.ncbi.nlm.nih.gov/gene/27125) · UniProt [Q9UHB7](https://www.uniprot.org/uniprotkb/Q9UHB7) · Ensembl [ENSG00000072364](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072364)

## Data

Gene col 1016: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1016); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1016, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1016]; `tensor/DDL_lfc|DDL_z.npy` [1016]; `embed/gene_vectors.npy` [1016]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1016 or target_col == 1016). Every well: [[AFF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
