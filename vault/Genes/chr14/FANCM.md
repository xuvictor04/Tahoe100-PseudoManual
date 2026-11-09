---
symbol: "FANCM"
type: "gene"
col: 11949
ensembl_id: "ENSG00000187790"
name: "FA complementation group M"
location: "14q21.2"
module: 71
arm: "+"
pooled_cpm: 35.46
n_lines_expressing: 49
n_dd_up: 27
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# FANCM

*FA complementation group M* — 14q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (18 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.23× (z +24.6, q 0e+00, up in 46 of 47 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.12× (z +22.2, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.478× (z -15.5, q 0e+00, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Rapamycin (drug)]] 5 µM: 0.872× (z -4.1, q 0.004, down in 11 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SHP-77 0.118×, HT-29 0.0672×, Hs 766T 0.107×, NCI-H460 0.217×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HCT15 0.0683×, SHP-77 0.128×, C-33 A 0.0946×, NCI-H1792 0.239×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.0602×, NCI-H2030 0.225×, SW480 0.392×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (LS 180 0.300×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN9]] (+0.80, fdr 7e-06), [[ATAD5]] (+0.79, fdr 7e-06), [[CDCA5]] (+0.78, fdr 7e-06).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 24 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11949.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **3.23×** | +24.6 | 0e+00 | 46/47 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **3.00×** | +23.0 | 0e+00 | 46/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.12×** | +22.2 | 0e+00 | 43/47 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.58×** | +19.9 | 0e+00 | 45/47 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.46×** | +18.2 | 0e+00 | 43/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.17×** | +15.6 | 0e+00 | 40/47 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +10.4 | 2e-23 | 33/47 (SW1417, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.47×** | +7.7 | 7e-13 | 31/45 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.43×** | +7.6 | 3e-12 | 26/47 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.43×** | +7.4 | 6e-12 | 30/47 (RKO, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +7.2 | 4e-11 | 24/47 (RKO, NCI-H2347, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +6.2 | 3e-08 | 21/47 (SW480, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.33×** | +5.9 | 1e-07 | 20/46 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.33×** | +5.7 | 6e-07 | 23/47 (RKO, MIA PaCa-2, …) | top dose only | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.61×** | +5.2 | 7e-06 | 17/46 (RKO, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +5.1 | 1e-05 | 23/47 (NCI-H2030, A549, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.002 | 9/47 (Panc 03.27, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.003 | 11/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +3.7 | 0.004 | 13/47 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.5 | 0.011 | 5/46 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.016 | 9/47 (J82, MIA PaCa-2, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.11× | +3.2 | 0.031 | 8/47 (A549, NCI-H1792, …) | top dose only |  |
| [[Trimetrexate (drug)]] 5 µM |  | 1.11× | +3.1 | 0.037 | 3/47 (SNU-1, HT-29, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.11× | +3.1 | 0.038 | 12/47 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.045 | 6/47 (LS 180, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.048 | 6/47 (A549, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11949.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (SHP-77 0.118×, HT-29 0.0672×, Hs 766T 0.107×, NCI-H460 0.217×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HCT15 0.0683×, SHP-77 0.128×, C-33 A 0.0946×, NCI-H1792 0.239×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (HT-29 0.0602×, NCI-H2030 0.225×, SW480 0.392×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (LS 180 0.300×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.478×** | -15.5 | 0e+00 | 35/44 (HCT15, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.515×** | -13.4 | 1e-38 | 29/38 (SHP-77, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.559×** | -11.3 | 2e-27 | 33/41 (HT-29, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.777×** | -4.6 | 6e-04 | 19/47 (LS 180, SHP-77, …) | two highest doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.794×** | -4.2 | 0.003 | 19/47 (A498, LS 180, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.872× | -4.1 | 0.004 | 11/47 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.828×** | -4.0 | 0.006 | 12/47 (A498, Hs 766T, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.876× | -3.9 | 0.006 | 17/47 (RPMI-7951, C32, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.882× | -3.8 | 0.011 | 14/47 (A-427, C32, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.831×** | -3.7 | 0.012 | 11/47 (SNU-1, NCI-H460, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.721×** | -3.6 | 0.016 | 6/46 (LOX-IMVI, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.858× | -3.2 | 0.058 | 13/46 (LS 180, A-172, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.747×** | -3.2 | 0.058 | 12/41 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.862× | -3.1 | 0.066 | 6/46 (SW480, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11949. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 57.5 | 6 (5 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.18× (z +14.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -11.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 30.8 | 6 (5 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.15× (z +13.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -9.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 40.4 | 6 (5 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +11.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -8.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H460 (line)]] | wt | 30.9 | 4 (4 ⚠) | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.82× (z +12.7) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 5 µM 0.217× (z -14.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 36.0 | 4 (3 ⚠) | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.8) | [[Lonafarnib (drug)]] 5 µM 0.133× (z -10.1) ⚠ toxic |
| [[J82 (line)]] | alt | 33.4 | 5 (5 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +11.2) ⚠ cell-cycle shift, explains ~31% of this change | [[Dinaciclib (drug)]] 5 µM 0.279× (z -10.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.4 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +13.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 54.7 | 5 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +15.3) | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -10.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 35.8 | 5 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 53.4 | 5 (4 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +10.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 53.6 | 3 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 48.3 | 3 (2 ⚠) | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.70× (z +9.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.225× (z -13.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 35.4 | 5 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +17.1) ⚠ cell-cycle shift, explains ~14% of this change | — |
| [[SW1417 (line)]] | alt | 35.2 | 5 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 25.8 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.75× (z +10.6) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 5 µM 0.107× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 39.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.97× (z +10.4) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.331× (z -9.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 47.9 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.11× (z +10.6) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A498 (line)]] | wt | 20.3 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +11.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A549 (line)]] | wt | 27.2 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.30× (z +14.2) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 19.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0602× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 45.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +12.8) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[SHP-77 (line)]] | alt | 68.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.118× (z -19.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.6 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 54.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0946× (z -17.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 32.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.2) | — |
| [[H4 (line)]] | wt | 31.3 | 0 | 2 (2 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.127× (z -8.8) ⚠ cell-cycle shift, explains ~87% of this change |
| [[HCT15 (line)]] | alt | 64.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0683× (z -21.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 53.1 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 17.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +10.3) | — |
| [[KATO III (line)]] | alt | 38.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.90× (z +9.1) ⚠ cell-cycle shift, explains ~38% of this change | [[Dinaciclib (drug)]] 5 µM 0.249× (z -11.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.300× (z -9.5) |
| [[SK-MEL-2 (line)]] | alt | 31.1 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +10.4) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 15.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +9.0) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[C32 (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -8.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 27.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SNU-1 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SW48 (line)]] | wt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11949), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN9]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[ATAD5]] | +0.79 | +0.79 / +0.79 | both halves | 7e-06 | STRING 814 |
| [[CDCA5]] | +0.78 | +0.66 / +0.82 | both halves | 7e-06 |  |
| [[MTBP]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[TICRR]] | +0.77 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[ZGRF1]] | +0.77 | +0.78 / +0.77 | both halves | 7e-06 | STRING 546 |
| [[SLF1]] | +0.77 | +0.75 / +0.78 | both halves | 7e-06 | STRING 495 |
| [[PLK4]] | +0.76 | +0.78 / +0.76 | both halves | 7e-06 | STRING 400 |
| [[RFWD3]] | +0.75 | +0.63 / +0.77 | both halves | 7e-06 | same gene group; STRING 666 |
| [[CCDC77]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CENPO]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[KIF22]] | +0.73 | +0.67 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FANCM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers FANCM's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.3% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DSCC1]] | C | DSCC1 activity raises FANCM's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without DSCC1 | 0.018 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[RBL1]] | C | RBL1's natural level strengthens FANCM's drug response | RBL1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.04; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PBK]] | C | PBK activity raises FANCM's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without PBK | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[MELK]] | C | MELK activity raises FANCM's level | lines that do not express MELK (3) vs lines expressing it (47) | 2.72× lower at baseline in the lines without MELK | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |
| [[TP53]] | C | TP53 activity weakens FANCM's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 17 not recorded | the TP53-altered lines respond 1.21× as strongly (z diff -1.31); strongest at Doxorubicin (hydrochloride) 5 µM: 2.67x vs 2.12x (z diff -2.6) | 0.907 over the table, 0.086 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.6, -49.3); signed map (-41.9, -42.1). **Vector** length 106, 30.1% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *HDR through Homologous Recombination (HRR)* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.8 | +18.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +5.9 | +15.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.3 | +4.5 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +3.1 | +3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.1 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +10.4 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.1 | -15.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.1 | -13.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.2 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -7.3 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -3.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | FA complementation group M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.2 — chr14:45,135,930-45,200,890 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAAP250; previously KIAA1596 |
| Gene groups (HGNC) | DEAH-box helicases; FA complementation groups; FA core complex |
| Reactome | 6 pathways, smallest: Fanconi Anemia Pathway; PKR-mediated signaling; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYD8](https://www.uniprot.org/uniprotkb/Q8IYD8) (Fanconi anemia group M protein):

> DNA-dependent ATPase component of the Fanconi anemia (FA) core complex. Required for the normal activation of the FA pathway, leading to monoubiquitination of the FANCI-FANCD2 complex in response to DNA damage, cellular resistance to DNA cross-linking drugs, and prevention of chromosomal breakage. In complex with CENPS and CENPX, binds double-stranded DNA (dsDNA), fork-structured DNA (fsDNA) and Holliday junction substrates. Its ATP-dependent DNA branch migration activity can process branched …

**Summary**, from NCBI Gene [57697](https://www.ncbi.nlm.nih.gov/gene/57697):

> The Fanconi anemia complementation group (FANC) currently includes FANCA, FANCB, FANCC, FANCD1 (also called BRCA2), FANCD2, FANCE, FANCF, FANCG, FANCI, FANCJ (also called BRIP1), FANCL, FANCM and FANCN (also called PALB2). The previously defined group FANCH is the same as FANCA. Fanconi anemia is a genetically heterogeneous recessive disorder characterized by cytogenetic instability, hypersensitivity to DNA crosslinking agents, increased chromosomal breakage, and defective DNA repair. The …

**Accessions** — [HGNC:23168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23168) · Entrez [57697](https://www.ncbi.nlm.nih.gov/gene/57697) · UniProt [Q8IYD8](https://www.uniprot.org/uniprotkb/Q8IYD8) · Ensembl [ENSG00000187790](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187790)

## Data

Gene col 11949: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11949); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11949, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11949]; `tensor/DDL_lfc|DDL_z.npy` [11949]; `embed/gene_vectors.npy` [11949]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11949 or target_col == 11949). Every well: [[FANCM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FANCM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
