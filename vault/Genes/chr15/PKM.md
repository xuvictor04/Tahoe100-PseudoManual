---
symbol: "PKM"
type: "gene"
col: 857
ensembl_id: "ENSG00000067225"
name: "pyruvate kinase M1/2"
location: "15q23"
module: 99
arm: "+"
pooled_cpm: 618.77
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 1
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# PKM

*pyruvate kinase M1/2* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.27× (z +12.2, q 1e-31, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.44× (z +5.3, q 2e-05, up in 40 of 50 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1792 5.16×, A498 4.04×, MIA PaCa-2 3.50×, NCI-H460 3.47×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1792 4.15×, C-33 A 3.82×, A498 3.52×, J82 2.97×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 2.01×, A498 1.85×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.41×, A-172 2.12×).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.675× (z -8.3, q 6e-14, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGK1]] (+0.68, fdr 7e-06), [[CFL1]] (+0.67, fdr 7e-06), [[ENO1]] (+0.65, fdr 7e-06); moves opposite to [[DNAJC2]] (-0.66, fdr 7e-06), [[TIMM44]] (-0.59, fdr 1e-05), [[EPB41L4A-AS1]] (-0.58, fdr 1e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PLOD2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 10 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 857.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (NCI-H1792 5.16×, A498 4.04×, MIA PaCa-2 3.50×, NCI-H460 3.47×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change); [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H1792 4.15×, C-33 A 3.82×, A498 3.52×, J82 2.97×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H1792 2.01×, A498 1.85×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 2.41×, A-172 2.12×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.27×** | +12.2 | 1e-31 | 48/49 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.06×** | +10.4 | 8e-23 | 42/44 (NCI-H1792, C-33 A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.71×** | +7.4 | 3e-11 | 36/45 (C-33 A, A498, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.3 | 2e-05 | 40/50 (MIA PaCa-2, A-172, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.5 | 9e-04 | 0/50 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.33×** | +4.3 | 0.002 | 30/48 (NCI-H1792, A549, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.67×** | +4.0 | 0.005 | 36/49 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.27×** | +3.6 | 0.022 | 26/48 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +3.5 | 0.028 | 28/48 (NCI-H460, SW480, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.24×** | +3.2 | 0.076 | 29/48 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.24× | +3.1 | 0.11 | 29/48 (A-172, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 857.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.675×** | -8.3 | 6e-14 | 32/48 (SNU-1, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.757×** | -4.2 | 0.007 | 36/48 (RKO, C32, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.711×** | -4.1 | 0.007 | 43/50 (SNU-1, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.620×** | -3.7 | 0.024 | 43/50 (SNU-1, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.622×** | -3.7 | 0.024 | 32/45 (RPMI-7951, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.771×** | -3.7 | 0.024 | 34/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.651×** | -3.3 | 0.067 | 35/49 (BT-474, HCT15, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.660×** | -3.2 | 0.086 | 40/49 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 0.800× | -3.1 | 0.11 | 36/49 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.814× | -3.1 | 0.12 | 27/48 (H4, NCI-H2347, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 857. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 550 | 8 (7 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.01× (z +10.2) | — |
| [[C-33 A (line)]] | alt | 300 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -13.4) |
| [[SW480 (line)]] | alt | 540 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 493 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -12.8) |
| [[NCI-H460 (line)]] | wt | 453 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-1 (line)]] | wt | 1,227 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -26.5) |
| [[A498 (line)]] | wt | 540 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 827 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -14.2) |
| [[HOP62 (line)]] | alt | 781 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 602 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.59× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -14.2) |
| [[A-172 (line)]] | wt | 697 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.1) | — |
| [[A-427 (line)]] | wt | 221 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.35× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -17.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -16.9) |
| [[A549 (line)]] | wt | 777 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AsPC-1 (line)]] | alt | 389 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.495× (z -12.9) |
| [[J82 (line)]] | alt | 612 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 448 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SHP-77 (line)]] | alt | 428 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.54× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -15.6) |
| [[SNU-423 (line)]] | alt | 466 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.29× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW1417 (line)]] | alt | 524 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[AN3 CA (line)]] | alt | 521 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[BT-474 (line)]] | alt | 429 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -20.0) |
| [[C32 (line)]] | wt | 768 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HepG2_C3A (line)]] | wt | 380 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -19.7) |
| [[HS-578T (line)]] | alt | 600 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 525 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.479× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 652 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LoVo (line)]] | wt | 870 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -14.3) |
| [[LOX-IMVI (line)]] | wt | 897 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[LS 180 (line)]] | wt | 707 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -18.4) |
| [[NCI-H23 (line)]] | alt | 449 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -18.1) |
| [[SK-MEL-2 (line)]] | alt | 744 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -11.7) |
| [[SW 900 (line)]] | alt | 611 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[CFPAC-1 (line)]] | alt | 808 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[CHP-212 (line)]] | wt | 606 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.9) |
| [[COLO 205 (line)]] | alt | 822 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.415× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[H4 (line)]] | wt | 815 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HCT15 (line)]] | alt | 763 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -22.2) |
| [[Hs 766T (line)]] | wt | 443 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 1,024 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -16.2) |
| [[NCI-H2030 (line)]] | alt | 754 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2347 (line)]] | alt | 712 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.536× (z -13.1) |
| [[NCI-H596 (line)]] | alt | 627 | 0 | 1 | — | [[Fulvestrant (drug)]] 5 µM 0.257× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 450 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RKO (line)]] | wt | 539 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.20× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[RPMI-7951 (line)]] | alt | 880 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H2122 (line)]] | alt | 675 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 759 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 961 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 549 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 857), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGK1]] | +0.68 | +0.71 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 936 |
| [[CFL1]] | +0.67 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[ENO1]] | +0.65 | +0.72 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 997 |
| [[BSG]] | +0.65 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[SLC2A1]] | +0.62 | +0.61 / +0.64 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives; STRING 814 |
| [[G6PD]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 941 |
| [[ALDOA]] | +0.60 | +0.63 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS; STRING 983 |
| [[FKBP1A]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[EPB41L2]] | +0.59 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TPI1]] | +0.57 | +0.67 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 963 |
| [[LDHA]] | +0.56 | +0.63 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS; STRING 997 |
| [[ITM2C]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC2]] | -0.66 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[TIMM44]] | -0.59 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[EPB41L4A-AS1]] | -0.58 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[NSUN4]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[MTO1]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[CCZ1P1]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PLEKHM2]] | -0.54 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[GUSBP11]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[VPS33A]] | -0.53 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SNHG32]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[MAU2]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[TAF1D]] | -0.52 | -0.56 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLOD2]] | B | PLOD2 activity raises PKM's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without PLOD2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[SMAD3]] | B | SMAD3 activity raises PKM's level | lines that do not express SMAD3 (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without SMAD3 | 0.009 | ⚠ within organs, on part of the lines; also absent: ITGA3, NIBAN2, IER3; maybe low, not absent |
| [[ITGA3]] | B | ITGA3 activity raises PKM's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 1.50× lower at baseline in the lines without ITGA3 | 0.047 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises PKM's level | compounds that target MTOR: 3 of 8 lower it (Bimiralisib, GSK1059615, Sapanisertib) | 38% of the class's compounds vs 2.0% of all compounds | 0.088 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, 22.4); signed map (-37.2, 29.3). **Vector** length 132, 55.7% of its response variance represented; |z| ≥ 3 in 1,253 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Gluconeogenesis* (reactome, mean cos +0.56 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.4 | +4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.6 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +3.3 | +2.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -8.2 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~80% of this change | -6.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | -4.9 | -3.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.9 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -1.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -2.4 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -3.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate kinase M1/2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:72,199,029-72,231,819 (-) |
| Ensembl biotype | protein_coding |
| Also known as | THBP1, OIP3, PK3; previously PKM2 |
| Gene groups (HGNC) | Pyruvate kinase family |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 17 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Negative Regulation of CDH1 Gene Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P14618](https://www.uniprot.org/uniprotkb/P14618) (Pyruvate kinase PKM):

> Catalyzes the final rate-limiting step of glycolysis by mediating the transfer of a phosphoryl group from phosphoenolpyruvate (PEP) to ADP, generating ATP. The ratio between the highly active tetrameric form and nearly inactive dimeric form determines whether glucose carbons are channeled to biosynthetic processes or used for glycolytic ATP production. The transition between the 2 forms contributes to the control of glycolysis and is important for tumor cell proliferation and survival.; …

**Summary**, from NCBI Gene [5315](https://www.ncbi.nlm.nih.gov/gene/5315):

> This gene encodes a protein involved in glycolysis. The encoded protein is a pyruvate kinase that catalyzes the transfer of a phosphoryl group from phosphoenolpyruvate to ADP, generating ATP and pyruvate. This protein has been shown to interact with thyroid hormone and may mediate cellular metabolic effects induced by thyroid hormones. This protein has been found to bind Opa protein, a bacterial outer membrane protein involved in gonococcal adherence to and invasion of human cells, suggesting a …

**Accessions** — [HGNC:9021](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9021) · Entrez [5315](https://www.ncbi.nlm.nih.gov/gene/5315) · UniProt [P14618](https://www.uniprot.org/uniprotkb/P14618) · Ensembl [ENSG00000067225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067225)

## Data

Gene col 857: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 857); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 857, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 857]; `tensor/DDL_lfc|DDL_z.npy` [857]; `embed/gene_vectors.npy` [857]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 857 or target_col == 857). Every well: [[PKM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
