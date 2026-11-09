---
symbol: "JMJD1C"
type: "gene"
col: 10194
ensembl_id: "ENSG00000171988"
name: "jumonji domain containing 1C"
location: "10q21.3"
module: 168
arm: "-"
pooled_cpm: 758.54
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# JMJD1C

*jumonji domain containing 1C* — 10q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.52× (z +15.2, q 0e+00, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.365× (z -24.9, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.630× (z -16.8, q 0e+00, down in 47 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.372×, NCI-H1792 0.365×, A-172 0.463×, LOX-IMVI 0.364×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (AsPC-1 0.238×, A549 0.307×, SNU-423 0.222×, Panc 03.27 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (Panc 03.27 0.261×, SW1417 0.299×, SNU-423 0.226×, SW480 0.327×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF103-CHMP3]] (+0.62, fdr 1e-05), [[BACH2]] (+0.61, fdr 1e-05), [[BRAF]] (+0.61, fdr 1e-05); moves opposite to [[SEPTIN7P14]] (-0.62, fdr 4e-05), [[STT3A]] (-0.62, fdr 2e-05), [[MTRR]] (-0.61, fdr 1e-05).
> It sits in the **-** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10194.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.52×** | +15.2 | 0e+00 | 39/48 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.75×** | +14.4 | 2e-44 | 47/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +11.2 | 6e-27 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +10.9 | 2e-25 | 43/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.51×** | +10.6 | 5e-24 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.50×** | +10.0 | 9e-22 | 39/48 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.3 | 2e-08 | 32/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.60×** | +5.7 | 1e-06 | 33/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.55×** | +5.2 | 1e-05 | 33/48 (SW480, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.21×** | +4.9 | 6e-05 | 24/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.2 | 0.001 | 22/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.18× | +4.0 | 0.003 | 20/47 (NCI-H2030, NCI-H460, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.16× | +3.8 | 0.005 | 19/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.16× | +3.7 | 0.008 | 20/47 (COLO 205, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.6 | 0.014 | 12/49 (KATO III, SHP-77, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.041 | 28/48 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.2 | 0.047 | 14/48 (SNU-1, NCI-H1573, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.056 | 23/49 (A-427, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.092 | 0/48 | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10194.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 15 lines (A549 0.372×, NCI-H1792 0.365×, A-172 0.463×, LOX-IMVI 0.364×, …); [[Dinaciclib (drug)]] 5 µM in 7 lines (AsPC-1 0.238×, A549 0.307×, SNU-423 0.222×, Panc 03.27 0.272×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (Panc 03.27 0.261×, SW1417 0.299×, SNU-423 0.226×, SW480 0.327×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.365×** | -24.9 | 0e+00 | 44/44 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.407×** | -23.1 | 0e+00 | 48/49 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.472×** | -17.8 | 0e+00 | 42/45 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.630×** | -16.8 | 0e+00 | 47/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.617×** | -12.4 | 4e-33 | 38/48 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.637×** | -11.6 | 5e-29 | 40/48 (HT-29, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.703×** | -9.0 | 1e-17 | 45/48 (HT-29, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.736×** | -7.9 | 2e-13 | 32/48 (HT-29, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.752×** | -7.0 | 1e-10 | 36/50 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.756×** | -6.9 | 3e-10 | 35/47 (CFPAC-1, HepG2/C3A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.786×** | -5.9 | 2e-07 | 30/48 (SNU-423, C32, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.822×** | -5.0 | 2e-05 | 26/48 (HT-29, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.834× | -4.7 | 1e-04 | 24/48 (HT-29, HOP62, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.950× | -4.3 | 6e-04 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.895× | -4.0 | 0.002 | 8/48 (A549, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 0.886× | -3.1 | 0.063 | 16/48 (SK-MEL-2, HCT15, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.775×** | -3.0 | 0.069 | 25/48 (C32, Hs 766T, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10194. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 791 | 8 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -23.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -12.5) |
| [[KATO III (line)]] | alt | 482 | 7 (2 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +20.1) | [[Dinaciclib (drug)]] 0.05 µM 0.446× (z -14.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 663 | 7 (2 ⚠) | 7 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +14.4) | [[Panobinostat (drug)]] 0.5 µM 0.413× (z -16.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 718 | 11 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -13.8) |
| [[SW1417 (line)]] | alt | 873 | 5 (1 ⚠) | 9 (8 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -24.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -13.1) |
| [[C32 (line)]] | wt | 539 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -20.4) |
| [[HepG2_C3A (line)]] | wt | 1,047 | 4 (1 ⚠) | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.348× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.514× (z -16.7) |
| [[HOP62 (line)]] | alt | 589 | 6 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.419× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 554 | 2 | 10 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -20.6) |
| [[PANC-1 (line)]] | alt | 1,259 | 5 (1 ⚠) | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -23.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -19.2) |
| [[A549 (line)]] | wt | 722 | 7 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +22.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -32.0) |
| [[BT-474 (line)]] | alt | 693 | 7 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.25× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -13.4) |
| [[LOX-IMVI (line)]] | wt | 1,030 | 3 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 834 | 10 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.537× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 647 | 6 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -16.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 557 | 4 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +27.2) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -22.2) |
| [[CFPAC-1 (line)]] | alt | 750 | 2 | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.72× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.319× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -13.0) |
| [[Hs 766T (line)]] | wt | 745 | 6 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.05× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.253× (z -20.2) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 837 | 2 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -20.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 570 | 6 | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.44× (z +14.5) | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -17.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 860 | 2 | 8 (7 ⚠) | [[Harringtonine (drug)]] 5 µM 1.80× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -24.4) |
| [[COLO 205 (line)]] | alt | 497 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +25.8) | [[Panobinostat (drug)]] 5 µM 0.467× (z -13.3) ⚠ cell-cycle shift, explains ~47% of this change |
| [[LoVo (line)]] | wt | 758 | 4 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 936 | 4 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +17.8) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -19.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 1,094 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +27.0) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -26.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 421 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.520× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 426 | 2 | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.438× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.648× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 893 | 1 | 7 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 501 | 3 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 935 | 4 (1 ⚠) | 4 (3 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.17× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -9.6) |
| [[A498 (line)]] | wt | 513 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +19.5) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -19.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 735 | 1 | 6 (6 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.60× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -19.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 1,419 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +17.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -19.9) |
| [[SNU-423 (line)]] | alt | 992 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.60× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -24.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 712 | 2 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -12.8) |
| [[SK-MEL-2 (line)]] | alt | 697 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.314× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -13.3) |
| [[A-427 (line)]] | wt | 1,127 | 1 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -12.3) |
| [[HCT15 (line)]] | alt | 634 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.332× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.551× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 624 | 1 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.61× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.526× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -11.5) |
| [[SW48 (line)]] | wt | 619 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.41× (z +13.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -17.6) |
| [[AN3 CA (line)]] | alt | 1,120 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -11.8) |
| [[C-33 A (line)]] | alt | 981 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.582× (z -12.2) |
| [[H4 (line)]] | wt | 528 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +11.8) | — |
| [[NCI-H661 (line)]] | alt | 870 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -13.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 511 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.376× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.3) |
| [[SHP-77 (line)]] | alt | 353 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.84× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 754 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 754 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 518 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 694 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10194), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*46 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF103-CHMP3]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[BACH2]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[BRAF]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.61 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[ING3]] | +0.60 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[RALGAPA1]] | +0.56 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[ZNF609]] | +0.56 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ERVK3-1]] | +0.55 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[JUND]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ABL2]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ZSWIM4]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[DCTN6]] | +0.54 | +0.34 / +0.53 | both halves | 1e-04 |  |

## Genes that move opposite

*54 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN7P14]] | -0.62 | -0.43 / -0.58 | both halves | 4e-05 |  |
| [[STT3A]] | -0.62 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MTRR]] | -0.61 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[RNF4]] | -0.60 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[SDHA]] | -0.59 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[CCAR2]] | -0.58 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[NOMO2]] | -0.58 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[SDHAP4]] | -0.58 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PMS2P3-1]] | -0.58 | -0.34 / -0.60 | both halves | 1e-04 |  |
| [[DDOST]] | -0.58 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[MSTO2P]] | -0.57 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[MLEC]] | -0.57 | -0.30 / -0.63 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises JMJD1C's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **-** arm (projection on the module's main direction -0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-8.0, -16.4); signed map (7.5, -11.9). **Vector** length 99.5, 41.9% of its response variance represented; |z| ≥ 3 in 1,725 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +6.9 | +3.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +15.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +6.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.8 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | -1.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.6 | +2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +3.3 | +1.0 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +5.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -3.4 | -9.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | +0.5 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.8 | -1.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -0.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | jumonji domain containing 1C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.3 — chr10:63,167,221-63,521,850 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761F0118, KIAA1380, FLJ14374, KDM3C; previously TRIP8 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Lysine demethylase 3 family |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15652](https://www.uniprot.org/uniprotkb/Q15652) (Jumonji domain-containing protein 1C):

> Demethylates lysine in proteins, such as STAT3 or MDC1 (By similarity). Demethylates MDC1, thereby promoting MDC1-RNF8 interaction and facilitating RNF8-dependent MDC1 ubiquitination essential for double-strand break (DSB) repair. Demethylation of STAT3 at 'Lys-140' facilitates its interactions with the phosphatase PTPN6 and restrains STAT3 activation (By similarity). It is uncertain whether JMJD1C removes methyl groups from histone proteins as the other JMJD1/KDM3 proteins do. Nevertheless, …

**Summary**, from NCBI Gene [221037](https://www.ncbi.nlm.nih.gov/gene/221037):

> The protein encoded by this gene interacts with thyroid hormone receptors and contains a jumonji domain. It is a candidate histone demethylase and is thought to be a coactivator for key transcription factors. It plays a role in the DNA-damage response pathway by demethylating the mediator of DNA damage checkpoint 1 (MDC1) protein, and is required for the survival of acute myeloid leukemia. Mutations in this gene are associated with Rett syndrome and intellectual disability. Alternative splicing …

**Accessions** — [HGNC:12313](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12313) · Entrez [221037](https://www.ncbi.nlm.nih.gov/gene/221037) · UniProt [Q15652](https://www.uniprot.org/uniprotkb/Q15652) · Ensembl [ENSG00000171988](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171988)

## Data

Gene col 10194: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10194); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10194, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10194]; `tensor/DDL_lfc|DDL_z.npy` [10194]; `embed/gene_vectors.npy` [10194]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10194 or target_col == 10194). Every well: [[JMJD1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/JMJD1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
