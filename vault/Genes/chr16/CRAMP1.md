---
symbol: "CRAMP1"
type: "gene"
col: 151
ensembl_id: "ENSG00000007545"
name: "cramped chromatin regulator 1"
location: "16p13.3"
module: 145
arm: "+"
pooled_cpm: 54.34
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# CRAMP1

*cramped chromatin regulator 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.82× (z +20.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.388× (z -18.0, q 0e+00, down in 42 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.653× (z -11.2, q 1e-26, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZER1]] (+0.68, fdr 1e-05), [[FBXL20]] (+0.64, fdr 1e-05), [[MAP3K3]] (+0.62, fdr 2e-05); moves opposite to [[RABGGTB]] (-0.61, fdr 1e-05), [[ZDHHC21]] (-0.57, fdr 4e-05), [[FKTN]] (-0.56, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 151.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.82×** | +20.1 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +20.0 | 0e+00 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +18.8 | 0e+00 | 44/48 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.43×** | +17.2 | 0e+00 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +16.1 | 0e+00 | 44/49 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +15.5 | 0e+00 | 47/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +14.9 | 0e+00 | 45/48 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.37×** | +14.9 | 0e+00 | 46/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +14.5 | 0e+00 | 47/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.10×** | +14.4 | 4e-45 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.74×** | +13.3 | 7e-39 | 44/48 (A-172, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.46×** | +7.3 | 2e-11 | 35/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.43×** | +7.0 | 1e-10 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +6.8 | 4e-10 | 31/48 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +6.4 | 7e-09 | 27/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +6.2 | 3e-08 | 26/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 151.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.388×** | -18.0 | 0e+00 | 42/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.384×** | -17.8 | 0e+00 | 39/43 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.653×** | -11.2 | 1e-26 | 45/48 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.569×** | -10.9 | 1e-25 | 42/49 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.580×** | -9.8 | 2e-20 | 36/45 (NCI-H2030, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.739×** | -7.6 | 2e-12 | 33/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.665×** | -4.1 | 0.003 | 23/48 (LOX-IMVI, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.812×** | -4.0 | 0.004 | 19/48 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.835× | -3.5 | 0.022 | 19/48 (A-427, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.835× | -3.5 | 0.022 | 15/49 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.868× | -3.5 | 0.022 | 10/48 (NCI-H1573, Hs 766T, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.708×** | -3.5 | 0.022 | 13/46 (MIA PaCa-2, H4, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.853× | -3.0 | 0.11 | 7/48 (NCI-H1573, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 151. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 46.6 | 15 (2 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 7.27× (z +25.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.87× (z +24.3) | [[Tucidinostat (drug)]] 0.5 µM 0.453× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 42.9 | 12 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.0518× (z -32.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 51.2 | 8 (1 ⚠) | 3 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 3.17× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -13.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 67.4 | 8 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.10× (z +17.3) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -13.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 38.8 | 8 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.86× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 45.5 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.77× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -14.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 51.4 | 7 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.28× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -13.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 55.0 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -14.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 59.4 | 6 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -9.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 62.3 | 6 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.216× (z -16.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 51.4 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -10.1) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 31.1 | 7 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.31× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 5.63× (z +10.8) | — |
| [[A498 (line)]] | wt | 61.1 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.537× (z -9.1) |
| [[BT-474 (line)]] | alt | 46.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 55.0 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.98× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -12.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 32.8 | 6 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.14× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +13.2) | — |
| [[NCI-H1573 (line)]] | alt | 74.7 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.77× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.0906× (z -25.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 57.2 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +15.8) | — |
| [[SW1417 (line)]] | alt | 52.2 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +12.2) | — |
| [[AsPC-1 (line)]] | alt | 54.1 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 26.6 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 6.25× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.90× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 45.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.08× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.87× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -10.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 45.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +11.6) | — |
| [[J82 (line)]] | alt | 61.8 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.54× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 83.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -12.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 43.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -19.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 68.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -10.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 56.5 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.86× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -9.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 45.9 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 48.1 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 88.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -24.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 45.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.41× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 45.8 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.64× (z +8.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 37.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 48.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.4) | [[Tucidinostat (drug)]] 5 µM 0.414× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 57.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.419× (z -10.0) |
| [[SNU-1 (line)]] | wt | 73.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.52× (z +8.9) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.195× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 77.3 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.68× (z +9.7) | — |
| [[CHP-212 (line)]] | wt | 75.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -9.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -16.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 43.7 | 0 | 1 | — | [[Carbamazepine (drug)]] 0.5 µM 0.0602× (z -10.2) |
| [[SHP-77 (line)]] | alt | 58.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.19× (z +9.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 79.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 57.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 151), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 9 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZER1]] | +0.68 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MAP3K3]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[RAB40C]] | +0.61 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[NARF]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PITPNA]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[HINFP]] | +0.58 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ZNF324]] | +0.57 | +0.10 / +0.66 | ⚠ one half (not replicated) | 0.003 |  |
| [[ZFTRAF1]] | +0.57 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[IFT140]] | +0.57 | +0.30 / +0.65 | both halves | 2e-04 | ⚠ same locus (0.3 kb: neighbours can correlate without regulation) |
| [[DCAF11]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[YY1]] | +0.56 | +0.43 / +0.68 | both halves | 3e-05 |  |
| [[SIRT3]] | +0.55 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[TAF5]] | +0.54 | +0.30 / +0.55 | both halves | 2e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGGTB]] | -0.61 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[ZDHHC21]] | -0.57 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[FKTN]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[GMFB]] | -0.55 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[MOCS2]] | -0.53 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[RPAP3]] | -0.52 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[FAM171B]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[LINC01399]] | -0.51 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[STK26]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[DNAH14]] | -0.50 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[INO80C]] | -0.50 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[ZRANB2]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.706). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.4, -41.5); signed map (-17.6, 12.4). **Vector** length 92.9, 29.1% of its response variance represented; |z| ≥ 3 in 1,343 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +16.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +20.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +4.1 | +14.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +13.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.4 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +0.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.3 | +0.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.8 | -11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.3 | -10.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.2 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.5 | -1.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -4.9 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | +1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.1 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.9 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | cramped chromatin regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,612,337-1,677,908 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1426; previously CRAMP1L |
| Gene groups (HGNC) | Myb/SANT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96RY5](https://www.uniprot.org/uniprotkb/Q96RY5) (Protein cramped-like):

> Transcription factor, which specifically drives expression of histone H1 genes. Binds to the promoters of H1 genes (H1-2, H1-3, H1-4, H1-5 and H1-10/H1x) together with NPAT and GON4L, positively regulating their transcription.

**Summary**, from NCBI Gene [57585](https://www.ncbi.nlm.nih.gov/gene/57585):

> Enables DNA-binding transcription factor activity. Involved in positive regulation of DNA-templated transcription. Is active in histone locus body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14122) · Entrez [57585](https://www.ncbi.nlm.nih.gov/gene/57585) · UniProt [Q96RY5](https://www.uniprot.org/uniprotkb/Q96RY5) · Ensembl [ENSG00000007545](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007545)

## Data

Gene col 151: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 151); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 151, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 151]; `tensor/DDL_lfc|DDL_z.npy` [151]; `embed/gene_vectors.npy` [151]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 151 or target_col == 151). Every well: [[CRAMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRAMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
