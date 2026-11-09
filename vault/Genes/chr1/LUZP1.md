---
symbol: "LUZP1"
type: "gene"
col: 9831
ensembl_id: "ENSG00000169641"
name: "leucine zipper protein 1"
location: "1p36.12"
module: 160
arm: "+"
pooled_cpm: 125.18
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# LUZP1

*leucine zipper protein 1* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.56× (z +20.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.585× (z -11.3, q 5e-27, down in 33 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.772× (z -5.7, q 2e-06, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.1000×, A-427 0.147×, AsPC-1 0.284×, LOX-IMVI 0.396×, …; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.635×, HOP62 0.699×, NCI-H1792 0.652×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.326×, HepG2/C3A 0.260×, NCI-H2347 0.339×; ⚠ toxic; transcription drop); [[Ponatinib (drug)]] 5 µM in 1 line (NCI-H23 0.446×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLIN3]] (+0.64, fdr 1e-05), [[SMURF1]] (+0.62, fdr 1e-05), [[CD59]] (+0.62, fdr 1e-05); moves opposite to [[BOD1]] (-0.62, fdr 1e-05), [[EIF2D]] (-0.61, fdr 1e-05), [[NELFCD]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ST3GAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9831.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +20.7 | 0e+00 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.40×** | +19.3 | 0e+00 | 45/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.39×** | +19.3 | 0e+00 | 47/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +12.0 | 3e-31 | 32/49 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.18×** | +9.0 | 2e-17 | 36/49 (AsPC-1, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +8.9 | 4e-17 | 41/48 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +8.8 | 2e-16 | 40/48 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.31×** | +8.5 | 1e-15 | 27/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +6.4 | 9e-09 | 31/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.34×** | +6.4 | 9e-09 | 36/48 (SW480, SHP-77, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +6.1 | 7e-08 | 26/48 (A-172, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.30×** | +5.8 | 3e-07 | 32/48 (SW480, SNU-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.30×** | +5.8 | 3e-07 | 32/48 (BT-474, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.26×** | +5.2 | 9e-06 | 26/48 (SW480, NCI-H460, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.0 | 2e-05 | 23/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +4.6 | 1e-04 | 22/47 (COLO 205, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.5 | 2e-04 | 23/49 (A-427, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.3 | 5e-04 | 17/48 (SNU-1, A498, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | **1.45×** | +4.3 | 6e-04 | 19/46 (COLO 205, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.29×** | +4.0 | 0.001 | 28/48 (COLO 205, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.011 | 15/47 (COLO 205, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9831.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (SHP-77 0.1000×, A-427 0.147×, AsPC-1 0.284×, LOX-IMVI 0.396×, …; ⚠ toxic; transcription drop); [[Adagrasib (drug)]] 0.05 µM in 3 lines (NCI-H23 0.635×, HOP62 0.699×, NCI-H1792 0.652×; ⚠ position not correctable); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (RKO 0.326×, HepG2/C3A 0.260×, NCI-H2347 0.339×; ⚠ toxic; transcription drop); [[Ponatinib (drug)]] 5 µM in 1 line (NCI-H23 0.446×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -11.3 | 5e-27 | 33/44 (SHP-77, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.678×** | -8.6 | 3e-15 | 32/49 (RKO, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.772×** | -5.7 | 2e-06 | 32/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.764×** | -5.5 | 7e-06 | 23/45 (Panc 03.27, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.843× | -3.8 | 0.019 | 23/48 (NCI-H1792, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.857× | -3.4 | 0.056 | 18/48 (SW 1088, KATO III, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.845× | -3.4 | 0.056 | 19/48 (NCI-H23, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.860× | -3.3 | 0.064 | 16/49 (NCI-H23, Hs 766T, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.886× | -3.2 | 0.090 | 16/48 (NCI-H23, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | 0.903× | -3.2 | 0.090 | 15/48 (NCI-H2347, Panc 03.27, …) | all doses, flat | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -3.0 | 0.14 | 4/50 (NCI-H23, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.28 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9831. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 135 | 3 | 6 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -13.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 80.2 | 9 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.94× (z +20.5) | — |
| [[A498 (line)]] | wt | 84.2 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +19.9) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.48× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 45.0 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.32× (z +14.7) | — |
| [[Panc 03.27 (line)]] | alt | 109 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +12.3) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -14.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 139 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -12.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 240 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -14.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 147 | 5 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.52× (z +14.0) | [[Lonafarnib (drug)]] 5 µM 0.184× (z -9.8) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 154 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 97.8 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.37× (z +12.7) | — |
| [[RKO (line)]] | wt | 165 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -15.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 99.5 | 5 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.03× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -10.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 84.7 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.77× (z +16.5) | — |
| [[A-427 (line)]] | wt | 73.9 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.15× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.147× (z -21.3) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 135 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -8.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.20× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 83.8 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +13.1) | — |
| [[RPMI-7951 (line)]] | alt | 101 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +13.8) | — |
| [[SNU-1 (line)]] | wt | 88.6 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 95.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.44× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 120 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.65× (z +10.0) | — |
| [[KATO III (line)]] | alt | 80.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 69.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.479× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 178 | 0 | 4 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.635× (z -17.1) ⚠ position not correctable · without an alert: [[Ponatinib (drug)]] 5 µM 0.446× (z -8.6) |
| [[SHP-77 (line)]] | alt | 91.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -25.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 61.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.96× (z +12.0) | — |
| [[A-172 (line)]] | wt | 77.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 222 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.24× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -14.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 120 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.51× (z +9.9) | — |
| [[COLO 205 (line)]] | alt | 114 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 142 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 218 | 0 | 3 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.652× (z -12.2) ⚠ position not correctable |
| [[H4 (line)]] | wt | 121 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.59× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 323 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 65.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.5) | — |
| [[J82 (line)]] | alt | 228 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.662× (z -8.9) ⚠ cell-cycle shift, explains ~94% of this change |
| [[LoVo (line)]] | wt | 161 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.0) | — |
| [[A549 (line)]] | wt | 150 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 175 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 135 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9831), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLIN3]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SMURF1]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CD59]] | +0.62 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[C11orf91]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ARHGEF18]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MAPKAPK2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[BCAR3]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[NECTIN2]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SMURF2]] | +0.59 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BOD1]] | -0.62 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[EIF2D]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[NELFCD]] | -0.55 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[SPG21]] | -0.54 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[PHOSPHO2]] | -0.53 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ARFGEF2]] | -0.51 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[DNAJC13]] | -0.51 | -0.46 / -0.54 | both halves | 2e-05 |  |
| [[SRP72]] | -0.51 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[TMEM268]] | -0.51 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[HINT3]] | -0.51 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[CISD2]] | -0.50 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[ZFAND1]] | -0.50 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL1]] | B | ST3GAL1 activity raises LUZP1's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.49× lower at baseline in the lines without ST3GAL1 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[TIAM1]] | B | TIAM1 activity lowers LUZP1's level | lines that do not express TIAM1 (11) vs lines expressing it (39) | 1.56× higher at baseline in the lines without TIAM1 | 0.010 | ⚠ within organs, on part of the lines; also absent: RASSF2, SPATC1L, DNAH2 |
| [[C11orf91]] | B | C11orf91 activity raises LUZP1's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without C11orf91 | 0.067 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[STRIP2]] | B | STRIP2 activity raises LUZP1's level | lines that do not express STRIP2 (6) vs lines expressing it (44) | 1.83× lower at baseline in the lines without STRIP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: STK31, HLA-F-AS1, MIR181A2HG; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.784). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (36.0, 5.0); signed map (-4.6, 41.7). **Vector** length 135, 44.1% of its response variance represented; |z| ≥ 3 in 1,402 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +6.4 | +8.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.8 | +19.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.3 | +8.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.2 | +19.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.7 | +4.0 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +3.6 | +3.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +3.6 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.5 | +4.6 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -7.1 | -5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.0 | -11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.5 | -8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | -5.3 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.7 | -5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.1 | -3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | leucine zipper protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:23,084,030-23,178,152 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LUZP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V48](https://www.uniprot.org/uniprotkb/Q86V48) (Leucine zipper protein 1):

> F-actin cross-linking protein. Stabilizes actin and acts as a negative regulator of primary cilium formation. Positively regulates the phosphorylation of both myosin II and protein phosphatase 1 regulatory subunit PPP1R12A/MYPT1 and promotes the assembly of myosin II stacks within actin stress fibers. Inhibits the phosphorylation of myosin light chain MYL9 by DAPK3 and suppresses the constriction velocity of the contractile ring during cytokinesis. Binds to microtubules and promotes epithelial …

**Summary**, from NCBI Gene [7798](https://www.ncbi.nlm.nih.gov/gene/7798):

> This gene encodes a protein that contains a leucine zipper motif. The exact function of the encoded protein is not known. In mice this gene affects neural tube closure. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:14985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14985) · Entrez [7798](https://www.ncbi.nlm.nih.gov/gene/7798) · UniProt [Q86V48](https://www.uniprot.org/uniprotkb/Q86V48) · Ensembl [ENSG00000169641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169641)

## Data

Gene col 9831: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9831); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9831, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9831]; `tensor/DDL_lfc|DDL_z.npy` [9831]; `embed/gene_vectors.npy` [9831]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9831 or target_col == 9831). Every well: [[LUZP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LUZP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
