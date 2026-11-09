---
symbol: "MACF1"
type: "gene"
col: 4826
ensembl_id: "ENSG00000127603"
name: "microtubule actin crosslinking factor 1"
location: "1p34.3"
module: 147
arm: "+"
pooled_cpm: 650.8
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# MACF1

*microtubule actin crosslinking factor 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[BAY1125976 (drug)]] 5 µM: 1.61× (z +5.4, q 3e-05, up in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (A498 3.01×, A-427 2.54×, SW1417 2.06×, A-172 2.13×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A498 2.62×, A-427 2.24×, NCI-H23 2.25×, A-172 1.87×); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 2.15×, SW1417 1.78×); [[TAK-901 (drug)]] 5 µM in 2 lines (MIA PaCa-2 4.85×, C32 2.72×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.498× (z -15.0, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSN]] (+0.72, fdr 7e-06), [[MAP4K4]] (+0.68, fdr 7e-06), [[CAPN2]] (+0.68, fdr 7e-06); moves opposite to [[CNNM2]] (-0.59, fdr 1e-05), [[FNTB]] (-0.54, fdr 1e-04), [[P4HTM]] (-0.54, fdr 1e-05).
> It is in [[Module 147]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4826.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (A498 3.01×, A-427 2.54×, SW1417 2.06×, A-172 2.13×, …; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 4 lines (A498 2.62×, A-427 2.24×, NCI-H23 2.25×, A-172 1.87×); [[Harringtonine (drug)]] 5 µM in 2 lines (A498 2.15×, SW1417 1.78×); [[TAK-901 (drug)]] 5 µM in 2 lines (MIA PaCa-2 4.85×, C32 2.72×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[BAY1125976 (drug)]] 5 µM |  | **1.61×** | +5.4 | 3e-05 | 34/48 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.20×** | +4.0 | 0.015 | 25/48 (COLO 205, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.032 | 23/48 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.10 | 21/47 (SW48, NCI-H460, …) | two highest doses | low cells (technical?) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.34× | +3.3 | 0.12 | 27/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.32× | +3.2 | 0.14 | 25/48 (SW480, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.16 | 21/47 (COLO 205, HT-29, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.15× | +3.0 | 0.16 | 20/47 (COLO 205, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.0 | 0.16 | 17/48 (BT-474, SNU-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.498×** | -15.0 | 0e+00 | 36/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.470×** | -14.7 | 0e+00 | 47/47 (HepG2/C3A, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.521×** | -14.1 | 1e-42 | 34/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -12.4 | 2e-33 | 41/49 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.581×** | -11.7 | 1e-29 | 35/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.651×** | -9.2 | 2e-18 | 44/48 (C32, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.754×** | -6.1 | 1e-07 | 30/48 (NCI-H460, RKO, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.784×** | -5.2 | 1e-05 | 28/48 (RKO, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.820×** | -5.0 | 3e-05 | 25/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.807×** | -4.6 | 2e-04 | 26/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.834× | -4.5 | 3e-04 | 26/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.838× | -4.2 | 0.001 | 22/49 (MIA PaCa-2, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.829×** | -4.0 | 0.002 | 24/48 (RKO, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.833×** | -3.9 | 0.004 | 25/48 (NCI-H460, SNU-1, …) | rises with dose | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.818×** | -3.9 | 0.004 | 25/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.830×** | -3.8 | 0.006 | 25/48 (NCI-H23, CFPAC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.881× | -3.7 | 0.007 | 19/49 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.831×** | -3.7 | 0.007 | 23/47 (RKO, A-427, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.890× | -3.5 | 0.010 | 12/48 (NCI-H2030, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 365 | 1 | 14 (8 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 1.58× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.329× (z -21.2) |
| [[RKO (line)]] | wt | 599 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -18.1) |
| [[A498 (line)]] | wt | 461 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +32.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.62× (z +20.0) | — |
| [[LOX-IMVI (line)]] | wt | 858 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.284× (z -18.1) |
| [[MIA PaCa-2 (line)]] | alt | 1,127 | 2 | 7 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +11.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.292× (z -15.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -13.3) |
| [[H4 (line)]] | wt | 707 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.361× (z -11.8) |
| [[A-427 (line)]] | wt | 480 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +22.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.24× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.358× (z -17.1) |
| [[NCI-H1573 (line)]] | alt | 606 | 0 | 7 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.263× (z -16.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.303× (z -16.2) |
| [[NCI-H1792 (line)]] | alt | 630 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.327× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 924 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.357× (z -18.0) |
| [[NCI-H23 (line)]] | alt | 644 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.417× (z -14.0) |
| [[SW 900 (line)]] | alt | 499 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -10.3) |
| [[C32 (line)]] | wt | 690 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.72× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.277× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 652 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.390× (z -14.1) |
| [[SW48 (line)]] | wt | 648 | 2 (1 ⚠) | 4 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.50× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.393× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 630 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.453× (z -14.3) |
| [[HOP62 (line)]] | alt | 614 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -12.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.512× (z -10.9) |
| [[HS-578T (line)]] | alt | 699 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -15.1) |
| [[KATO III (line)]] | alt | 546 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.74× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -16.5) |
| [[SW1417 (line)]] | alt | 423 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +19.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.78× (z +9.7) | — |
| [[SW480 (line)]] | alt | 759 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.508× (z -17.0) |
| [[BT-474 (line)]] | alt | 507 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +15.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.10× (z +10.0) | — |
| [[HT-29 (line)]] | alt | 532 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +16.2) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.341× (z -16.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -10.6) |
| [[J82 (line)]] | alt | 504 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.490× (z -10.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 1,259 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -15.9) |
| [[PANC-1 (line)]] | alt | 992 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -11.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -10.0) |
| [[SHP-77 (line)]] | alt | 503 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.467× (z -12.4) |
| [[SNU-1 (line)]] | wt | 348 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.392× (z -13.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 633 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +18.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.87× (z +10.6) | — |
| [[AN3 CA (line)]] | alt | 613 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.396× (z -11.8) |
| [[C-33 A (line)]] | alt | 392 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.419× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 889 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.434× (z -11.8) |
| [[COLO 205 (line)]] | alt | 470 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.05× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 781 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.247× (z -18.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.610× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 361 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -10.0) |
| [[A549 (line)]] | wt | 505 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 551 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.426× (z -9.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.509× (z -8.6) |
| [[CHP-212 (line)]] | wt | 502 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.321× (z -10.1) |
| [[Hs 766T (line)]] | wt | 806 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.357× (z -9.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -8.9) |
| [[SNU-423 (line)]] | alt | 727 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.54× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -11.7) |
| [[SW 1271 (line)]] | alt | 979 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.9) |
| [[LoVo (line)]] | wt | 506 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.469× (z -10.5) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 540 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.527× (z -9.2) |
| [[HCT15 (line)]] | alt | 468 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 615 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 773 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 670 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 591 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 628 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 812 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSN]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 | STRING 534 |
| [[MAP4K4]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[CAPN2]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | same gene group |
| [[ACTN1]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.67 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[ELK3]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[MYO10]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PXN]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[TPM4]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CORO1C]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[KPNA4]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM2]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[FNTB]] | -0.54 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[P4HTM]] | -0.54 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[DPM3]] | -0.53 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[RHOXF1]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SPCS2]] | -0.52 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[NUDT2]] | -0.51 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PKDCC]] | -0.51 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[APTR]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[CA5BP1]] | -0.51 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[TMEM161B-DT]] | -0.50 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[SASS6]] | -0.49 | -0.25 / -0.55 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.7, 7.1); signed map (6.9, 44.6). **Vector** length 130, 44.5% of its response variance represented; |z| ≥ 3 in 1,929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.4 | -1.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.4 | +4.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.4 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +5.3 | -1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.7 | +1.4 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.4 | +1.2 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.4 | +2.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.6 | -14.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -6.3 | -6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -6.2 | -5.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.0 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -5.9 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.6 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -5.6 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | microtubule actin crosslinking factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:39,081,316-39,487,177 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0465, ACF7, ABP620, KIAA1251, MACF, FLJ45612, FLJ46776, Lnc-PMIF; previously KIAA0754 |
| Gene groups (HGNC) | EF-hand domain containing; Plakins; Spectrin repeat containing; SH3 domain containing |
| Matched by | ensembl_id |

UniProt [O94854](https://www.uniprot.org/uniprotkb/O94854) carries no function annotation.

**Summary**, from NCBI Gene [23499](https://www.ncbi.nlm.nih.gov/gene/23499):

> This gene encodes a large protein containing numerous spectrin and leucine-rich repeat (LRR) domains. The encoded protein is a member of a family of proteins that form bridges between different cytoskeletal elements. This protein facilitates actin-microtubule interactions at the cell periphery and couples the microtubule network to cellular junctions. Alternative splicing results in multiple transcript variants, but the full-length nature of some of these variants has not been determined. …

**Accessions** — [HGNC:13664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13664) · Entrez [23499](https://www.ncbi.nlm.nih.gov/gene/23499) · UniProt [O94854](https://www.uniprot.org/uniprotkb/O94854) · Ensembl [ENSG00000127603](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127603)

## Data

Gene col 4826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4826); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4826]; `tensor/DDL_lfc|DDL_z.npy` [4826]; `embed/gene_vectors.npy` [4826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4826 or target_col == 4826). Every well: [[MACF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
