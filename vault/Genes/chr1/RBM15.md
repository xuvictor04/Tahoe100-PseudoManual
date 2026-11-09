---
symbol: "RBM15"
type: "gene"
col: 8577
ensembl_id: "ENSG00000162775"
name: "RNA binding motif protein 15"
location: "1p13.3"
module: 91
arm: "+"
pooled_cpm: 45.32
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# RBM15

*RNA binding motif protein 15* — 1p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 3.54× (z +25.7, q 0e+00, up in 47 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.27× (z +24.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.813× (z -6.0, q 9e-07, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.181×, NCI-H23 0.419×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.245×, C-33 A 0.263×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (HT-29 0.105×, HEC-1-A 0.223×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MGME1]] (+0.63, fdr 7e-06), [[KIF24]] (+0.62, fdr 8e-06), [[CSTF1]] (+0.60, fdr 1e-05); moves opposite to [[LTA4H]] (-0.55, fdr 2e-05), [[MYO5A]] (-0.52, fdr 7e-05), [[PAPSS1]] (-0.52, fdr 9e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.54×** | +25.7 | 0e+00 | 47/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.27×** | +24.1 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.80×** | +16.9 | 0e+00 | 40/48 (SNU-423, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.24×** | +16.4 | 0e+00 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.09×** | +15.0 | 0e+00 | 46/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +11.3 | 9e-28 | 39/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +11.3 | 1e-27 | 44/49 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.74×** | +10.8 | 4e-25 | 38/48 (BT-474, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +10.4 | 2e-23 | 6/48 (SHP-77, C-33 A, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.59×** | +9.5 | 2e-19 | 41/48 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.5 | 1e-15 | 30/48 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.52×** | +8.4 | 1e-15 | 36/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +8.1 | 3e-14 | 38/48 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.10×** | +7.9 | 2e-13 | 30/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.46×** | +7.7 | 6e-13 | 32/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +7.7 | 6e-13 | 32/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.33×** | +5.7 | 4e-07 | 24/48 (NCI-H23, BT-474, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.3 | 4e-04 | 21/48 (J82, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 6e-04 | 18/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.002 | 13/48 (PANC-1, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8577.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SK-MEL-2 0.181×, NCI-H23 0.419×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.245×, C-33 A 0.263×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 2 lines (HT-29 0.105×, HEC-1-A 0.223×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.813×** | -6.0 | 9e-07 | 26/48 (A498, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.818×** | -5.8 | 1e-06 | 24/48 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.841× | -3.6 | 0.050 | 16/48 (RKO, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 0.835× | -3.5 | 0.050 | 19/48 (RKO, SW480, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.835× | -3.5 | 0.050 | 15/48 (A-172, A-427, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -3.4 | 0.058 | 14/48 (NCI-H1573, J82, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.846× | -3.3 | 0.070 | 15/42 (SK-MEL-2, NCI-H23, …) | rises with dose | composition shift |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.070 | 13/48 (NCI-H1792, LOX-IMVI, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.855× | -3.2 | 0.078 | 21/46 (NCI-H23, C-33 A, …) | rises with dose | composition shift |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 0.861× | -3.1 | 0.11 | 11/48 (SW480, SW 1271, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 103 | 8 (4 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 5.15× (z +17.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.23× (z +15.7) | [[Dinaciclib (drug)]] 0.5 µM 0.245× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 43.0 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.79× (z +18.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +15.9) | — |
| [[SW480 (line)]] | alt | 56.9 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.45× (z +23.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +21.8) | — |
| [[BT-474 (line)]] | alt | 39.8 | 6 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.52× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +12.0) | — |
| [[HT-29 (line)]] | alt | 55.9 | 4 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.76× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +13.7) | [[Lonafarnib (drug)]] 5 µM 0.105× (z -11.5) ⚠ toxic |
| [[J82 (line)]] | alt | 64.8 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.50× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +13.8) | — |
| [[LS 180 (line)]] | wt | 41.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.61× (z +14.4) | [[Selinexor (drug)]] 5 µM 0.496× (z -9.4) ⚠ cell-cycle shift, explains ~88% of this change |
| [[PANC-1 (line)]] | alt | 43.6 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.04× (z +15.1) | — |
| [[SNU-423 (line)]] | alt | 35.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +17.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.0) | — |
| [[A-172 (line)]] | wt | 43.9 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.81× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 32.6 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.19× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 42.6 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +12.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +11.5) | — |
| [[KATO III (line)]] | alt | 42.0 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.51× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +14.5) | — |
| [[LoVo (line)]] | wt | 35.2 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.46× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +12.9) | — |
| [[NCI-H1573 (line)]] | alt | 30.1 | 4 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.30× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.89× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 46.9 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +13.7) | — |
| [[CFPAC-1 (line)]] | alt | 30.3 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.43× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.91× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 55.6 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.67× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.3) | [[Lonafarnib (drug)]] 5 µM 0.223× (z -8.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 45.8 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.71× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.24× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 34.3 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.04× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 29.4 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.38× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +8.8) | — |
| [[RKO (line)]] | wt | 50.4 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.02× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 56.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.79× (z +12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.336× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 33.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.0) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[C-33 A (line)]] | alt | 64.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.88× (z +9.3) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 46.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.37× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.81× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.10× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.38× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 52.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.48× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.21× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 59.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.90× (z +10.6) | — |
| [[SW 900 (line)]] | alt | 44.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +9.2) | — |
| [[A-427 (line)]] | wt | 38.8 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.09× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 27.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.16× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 71.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.96× (z +8.8) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 46.5 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.66× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 28.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.81× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 41.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +10.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.20× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MGME1]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[KIF24]] | +0.62 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[CSTF1]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.59 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[KMT2B]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[BRD8]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[LIN9]] | +0.58 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[DLEU2]] | +0.57 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NDC80]] | +0.57 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[DBF4B]] | +0.55 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[KIF20B]] | +0.55 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SGO2]] | +0.55 | +0.44 / +0.66 | both halves | 3e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTA4H]] | -0.55 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[MYO5A]] | -0.52 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[PAPSS1]] | -0.52 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[KIFAP3]] | -0.50 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ZDHHC21]] | -0.50 | -0.37 / -0.42 | both halves | 9e-05 |  |
| [[EIF1AX]] | -0.48 | -0.36 / -0.42 | both halves | 1e-04 |  |
| [[MBOAT2]] | -0.47 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ATP13A2]] | -0.46 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[VAMP7]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[OLA1]] | -0.46 | -0.48 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-39.2, -49.8); signed map (-50.9, -47.9). **Vector** length 77.9, 18.0% of its response variance represented; |z| ≥ 3 in 1,100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.4 | +16.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.4 | +24.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +25.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +3.5 | +15.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +0.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +7.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.1 | +4.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -4.7 | -5.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.3 | -3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.1 | -3.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:110,338,506-110,346,681 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OTT, OTT1 |
| Gene groups (HGNC) | RNA binding motif containing; WTAP complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T37](https://www.uniprot.org/uniprotkb/Q96T37) (RNA-binding protein 15):

> RNA-binding protein that acts as a key regulator of N6-methyladenosine (m6A) methylation of RNAs, thereby regulating different processes, such as hematopoietic cell homeostasis, alternative splicing of mRNAs and X chromosome inactivation mediated by Xist RNA. Associated component of the WMM complex, a complex that mediates N6-methyladenosine (m6A) methylation of RNAs, a modification that plays a role in the efficiency of mRNA splicing and RNA processing (By similarity). Plays a key role in m6A …

**Summary**, from NCBI Gene [64783](https://www.ncbi.nlm.nih.gov/gene/64783):

> Members of the SPEN (Split-end) family of proteins, including RBM15, have repressor function in several signaling pathways and may bind to RNA through interaction with spliceosome components (Hiriart et al., 2005 [PubMed 16129689]).[supplied by OMIM, Feb 2009]

**Accessions** — [HGNC:14959](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14959) · Entrez [64783](https://www.ncbi.nlm.nih.gov/gene/64783) · UniProt [Q96T37](https://www.uniprot.org/uniprotkb/Q96T37) · Ensembl [ENSG00000162775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162775)

## Data

Gene col 8577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8577); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8577]; `tensor/DDL_lfc|DDL_z.npy` [8577]; `embed/gene_vectors.npy` [8577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8577 or target_col == 8577). Every well: [[RBM15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
