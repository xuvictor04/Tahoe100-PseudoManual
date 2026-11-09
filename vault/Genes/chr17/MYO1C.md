---
symbol: "MYO1C"
type: "gene"
col: 12481
ensembl_id: "ENSG00000197879"
name: "myosin IC"
location: "17p13.3"
module: 101
arm: "+"
pooled_cpm: 79.15
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 2
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# MYO1C

*myosin IC* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.44× (z +18.3, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[vincristine (drug)]] 0.5 µM: 1.36× (z +4.5, q 7e-04, up in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 4.51×, PANC-1 3.58×, SNU-423 5.09×, A549 2.95×, …; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 4.15×, A498 3.08×, A549 3.51×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 4.04×, A549 3.80×; ⚠ cell-cycle shift, explains ~38% of this change); [[Bimiralisib (drug)]] 5 µM in 1 line (NCI-H596 3.69×); [[Elimusertib hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H596 1.96×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.559× (z -12.0, q 3e-30, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ABR]] (+0.69, fdr 7e-06), [[ZYX]] (+0.66, fdr 7e-06), [[ARHGAP23]] (+0.66, fdr 7e-06); moves opposite to [[NDUFAF7]] (-0.68, fdr 1e-05), [[CDADC1]] (-0.61, fdr 1e-05), [[ASB7]] (-0.61, fdr 1e-05).
> It is in [[Module 101]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12481.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (MIA PaCa-2 4.51×, PANC-1 3.58×, SNU-423 5.09×, A549 2.95×, …; ⚠ cell-cycle shift, explains ~31% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 4.15×, A498 3.08×, A549 3.51×; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 4.04×, A549 3.80×; ⚠ cell-cycle shift, explains ~38% of this change); [[Bimiralisib (drug)]] 5 µM in 1 line (NCI-H596 3.69×); [[Elimusertib hydrochloride (drug)]] 0.5 µM in 1 line (NCI-H596 1.96×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +18.3 | 0e+00 | 45/49 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +16.5 | 0e+00 | 35/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.63×** | +14.2 | 9e-44 | 28/48 (MIA PaCa-2, PANC-1, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +8.7 | 5e-16 | 29/44 (NCI-H2030, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +5.4 | 6e-06 | 25/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 7e-04 | 23/48 (NCI-H460, A-172, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.005 | 21/45 (RPMI-7951, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.3 | 0.068 | 0/49 | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.3 | 0.070 | 14/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.085 | 16/48 (HCT15, HEC-1-A, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.12 | 15/47 (HepG2/C3A, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.12 | 19/48 (SW480, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12481.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.559×** | -12.0 | 3e-30 | 41/48 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.572×** | -11.5 | 5e-28 | 38/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.688×** | -10.9 | 3e-25 | 40/48 (SNU-1, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.614×** | -10.0 | 1e-21 | 36/48 (BT-474, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.706×** | -7.2 | 9e-11 | 36/48 (LOX-IMVI, H4, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.715×** | -6.5 | 7e-09 | 36/48 (SNU-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.727×** | -6.3 | 3e-08 | 30/47 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -5.9 | 2e-07 | 31/48 (KATO III, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.755×** | -5.8 | 5e-07 | 30/48 (HS-578T, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.749×** | -5.7 | 6e-07 | 26/48 (HT-29, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.814×** | -4.2 | 0.001 | 24/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.866× | -4.2 | 0.001 | 16/48 (BT-474, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.867× | -4.2 | 0.001 | 19/49 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.681×** | -4.1 | 0.001 | 25/45 (SW48, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.819×** | -4.1 | 0.002 | 20/48 (COLO 205, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.820×** | -4.1 | 0.002 | 21/48 (SW480, KATO III, …) | top dose only | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | 0.869× | -4.1 | 0.002 | 14/48 (C32, A549, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.702×** | -3.8 | 0.004 | 21/49 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.824×** | -3.8 | 0.004 | 18/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.829×** | -3.7 | 0.005 | 20/47 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.828×** | -3.6 | 0.008 | 14/47 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.843× | -3.5 | 0.009 | 19/48 (SW480, NCI-H23, …) | top dose only | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.742×** | -3.2 | 0.026 | 14/48 (SW480, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 97.1 | 7 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +19.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 141 | 5 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +18.4) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.477× (z -10.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[MIA PaCa-2 (line)]] | alt | 91.0 | 4 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +24.3) ⚠ cell-cycle shift, explains ~31% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -12.0) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H460 (line)]] | wt | 50.5 | 6 (6 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.51× (z +14.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[PANC-1 (line)]] | alt | 83.3 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +23.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 129 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +17.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 111 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -12.8) ⚠ cell-cycle shift, explains ~56% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.306× (z -9.5) |
| [[SNU-1 (line)]] | wt | 169 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +15.7) ⚠ cell-cycle shift, explains ~31% of this change | [[Selinexor (drug)]] 5 µM 0.379× (z -14.2) |
| [[AsPC-1 (line)]] | alt | 124 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -11.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.344× (z -9.9) |
| [[HS-578T (line)]] | alt | 94.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +11.5) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.487× (z -8.7) |
| [[J82 (line)]] | alt | 102 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +13.3) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 73.4 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H23 (line)]] | alt | 98.0 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.311× (z -13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.360× (z -11.4) |
| [[SNU-423 (line)]] | alt | 54.1 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.09× (z +22.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 102 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.352× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.518× (z -11.3) |
| [[HOP62 (line)]] | alt | 55.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +11.7) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 71.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | [[Panobinostat (drug)]] 5 µM 0.294× (z -9.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 37.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.2) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 105 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +14.2) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 96.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -9.4) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.428× (z -8.8) |
| [[A-427 (line)]] | wt | 69.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.0) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 88.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 80.6 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.424× (z -9.6) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H596 (line)]] | alt | 59.5 | 2 | 0 | [[Bimiralisib (drug)]] 5 µM 3.69× (z +13.6) | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +18.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 39.1 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +10.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SW 900 (line)]] | alt | 87.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +14.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[BT-474 (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -12.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[COLO 205 (line)]] | alt | 52.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.313× (z -9.2) |
| [[H4 (line)]] | wt | 91.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +12.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +12.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 45.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +8.9) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 52.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.339× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[RKO (line)]] | wt | 87.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.457× (z -8.6) |
| [[SHP-77 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.73× (z +8.8) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 50.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 98.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABR]] | +0.69 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ZYX]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[ARHGAP23]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CYFIP1]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[NAB1]] | +0.64 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[WDR1]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[THOC6]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[PIEZO1]] | +0.62 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[AXL]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[RGL2]] | +0.59 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[CSRP1]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PHF19]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFAF7]] | -0.68 | -0.57 / -0.67 | both halves | 1e-05 |  |
| [[CDADC1]] | -0.61 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[ASB7]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[FNTB]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 | pathway: Sensory Perception |
| [[PEX3]] | -0.59 | -0.53 / -0.62 | both halves | 1e-05 |  |
| [[NENF]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ZNF148]] | -0.57 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[VDAC3]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[CNOT8]] | -0.56 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[CRYZL1]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[SPATA7]] | -0.56 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[MRPL34]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.9, 1.9); signed map (-3.5, 34.3). **Vector** length 122, 37.4% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +14.1 | +14.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +10.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.3 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.0 | +18.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.7 | +0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.0 | +2.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.4 | -10.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.6 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.7 | -6.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.5 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.9 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | myosin IC |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:1,464,186-1,492,686 (-) |
| Ensembl biotype | protein_coding |
| Also known as | myr2, NMI, MyoIC |
| Gene groups (HGNC) | Myosin heavy chains, class I; B-WICH chromatin-remodelling complex subunits |
| Hallmark sets | MYOGENESIS, IL2_STAT5_SIGNALING |
| Reactome | 18 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; B-WICH complex positively regulates rRNA expression; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O00159](https://www.uniprot.org/uniprotkb/O00159) (Unconventional myosin-Ic):

> Myosins are actin-based motor molecules with ATPase activity. Unconventional myosins serve in intracellular movements. Their highly divergent tails are presumed to bind to membranous compartments, which would be moved relative to actin filaments. Involved in glucose transporter recycling in response to insulin by regulating movement of intracellular GLUT4-containing vesicles to the plasma membrane. Component of the hair cell's (the sensory cells of the inner ear) adaptation-motor complex. Acts …

**Summary**, from NCBI Gene [4641](https://www.ncbi.nlm.nih.gov/gene/4641):

> This gene encodes a member of the unconventional myosin protein family, which are actin-based molecular motors. The protein is found in the cytoplasm, and one isoform with a unique N-terminus is also found in the nucleus. The nuclear isoform associates with RNA polymerase I and II and functions in transcription initiation. The mouse ortholog of this protein also functions in intracellular vesicle transport to the plasma membrane. Multiple transcript variants encoding different isoforms have …

**Accessions** — [HGNC:7597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7597) · Entrez [4641](https://www.ncbi.nlm.nih.gov/gene/4641) · UniProt [O00159](https://www.uniprot.org/uniprotkb/O00159) · Ensembl [ENSG00000197879](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197879)

## Data

Gene col 12481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12481); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12481]; `tensor/DDL_lfc|DDL_z.npy` [12481]; `embed/gene_vectors.npy` [12481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12481 or target_col == 12481). Every well: [[MYO1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYO1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
