---
symbol: "NR3C1"
type: "gene"
col: 3476
ensembl_id: "ENSG00000113580"
name: "nuclear receptor subfamily 3 group C member 1"
location: "5q31.3"
module: 14
arm: "+"
pooled_cpm: 261.64
n_lines_expressing: 37
n_dd_up: 10
n_dd_down: 42
n_dd_up_clean: 7
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 16
direction_downstream: 315
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NR3C1

*nuclear receptor subfamily 3 group C member 1* — 5q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.97× (z +15.3, q 0e+00, up in 34 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.324× (z -23.8, q 0e+00, down in 34 of 35 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 0.640× (z -8.9, q 5e-17, down in 27 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSC]] (+0.71, fdr 7e-06), [[MARCKS]] (+0.70, fdr 7e-06), [[IL6]] (+0.67, fdr 7e-06); moves opposite to [[GPR89A]] (-0.57, fdr 1e-05), [[PHKA1]] (-0.55, fdr 1e-05), [[GLMN]] (-0.54, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[NHS]] → it (grade B ⚠); 315 go from it, the strongest it → [[ENSG00000243797]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.97×** | +15.3 | 0e+00 | 34/36 (LoVo, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +9.0 | 8e-17 | 24/35 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.46×** | +8.1 | 7e-14 | 25/35 (A-427, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +7.8 | 6e-13 | 23/35 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.21×** | +5.7 | 1e-06 | 16/35 (LoVo, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.66×** | +5.7 | 1e-06 | 22/35 (HOP62, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 0.002 | 17/35 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.21×** | +3.9 | 0.007 | 17/37 (LOX-IMVI, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.9 | 0.007 | 17/35 (NCI-H460, NCI-H2030, …) | rises with dose | composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.007 | 18/34 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.008 | 19/37 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.010 | 15/35 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.013 | 14/35 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.11× | +3.2 | 0.053 | 8/35 (NCI-H1573, MIA PaCa-2, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.16× | +3.2 | 0.059 | 11/35 (BT-474, LoVo, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.11× | +3.1 | 0.064 | 1/35 (NCI-H1573) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.074 | 12/35 (MIA PaCa-2, LOX-IMVI, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 61 in all, 19 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.324×** | -23.8 | 0e+00 | 34/35 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.393×** | -19.8 | 0e+00 | 34/35 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.380×** | -19.7 | 0e+00 | 32/33 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.464×** | -16.2 | 0e+00 | 32/35 (HOP62, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.487×** | -15.2 | 0e+00 | 32/36 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.608×** | -14.8 | 0e+00 | 24/36 (NCI-H1792, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **0.525×** | -13.1 | 4e-37 | 30/34 (CFPAC-1, SHP-77, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.640×** | -8.9 | 5e-17 | 27/35 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.674×** | -8.3 | 6e-15 | 27/35 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.683×** | -7.7 | 7e-13 | 26/37 (A-172, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.704×** | -7.1 | 7e-11 | 23/35 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -6.8 | 7e-10 | 22/35 (H4, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.550×** | -6.6 | 2e-09 | 26/32 (HOP62, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.740×** | -6.3 | 1e-08 | 24/35 (J82, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.729×** | -6.2 | 3e-08 | 20/33 (A-172, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **0.827×** | -5.6 | 7e-07 | 19/35 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.766×** | -5.6 | 7e-07 | 21/35 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.781×** | -5.2 | 7e-06 | 21/35 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -4.9 | 2e-05 | 20/35 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.791×** | -4.9 | 3e-05 | 23/35 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.785×** | -4.9 | 3e-05 | 19/36 (HS-578T, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.796×** | -4.8 | 5e-05 | 18/35 (NCI-H1573, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.800×** | -4.7 | 7e-05 | 18/35 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.654×** | -4.7 | 7e-05 | 22/35 (HOP62, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **0.800×** | -4.7 | 7e-05 | 20/35 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.751×** | -4.3 | 4e-04 | 22/35 (NCI-H1573, A-172, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.814×** | -4.3 | 4e-04 | 18/35 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.827×** | -4.0 | 0.001 | 17/35 (NCI-H1573, HS-578T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.52 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 489 | 3 | 15 (11 ⚠) | [[PH-797804 (drug)]] 5 µM 4.64× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.225× (z -21.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.340× (z -14.7) |
| [[NCI-H460 (line)]] | wt | 366 | 11 (5 ⚠) | 6 (6 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.54× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.321× (z -18.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 526 | 6 (2 ⚠) | 9 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 5.80× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -21.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.544× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 622 | 1 | 13 (11 ⚠) | [[TAK-901 (drug)]] 5 µM 4.76× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -26.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.415× (z -10.5) |
| [[A-172 (line)]] | wt | 411 | 1 (1 ⚠) | 12 (11 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.136× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.498× (z -13.0) |
| [[hTERT-HPNE (line)]] | wt | 476 | 1 | 12 (10 ⚠) | [[PH-797804 (drug)]] 5 µM 4.64× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.248× (z -15.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.394× (z -9.9) |
| [[H4 (line)]] | wt | 421 | 1 (1 ⚠) | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Auranofin (drug)]] 5 µM 0.291× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 332 | 3 | 8 (8 ⚠) | [[TAK-901 (drug)]] 5 µM 6.13× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.324× (z -16.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 302 | 3 (2 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +19.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.44× (z +13.2) | [[Panobinostat (drug)]] 5 µM 0.315× (z -17.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 561 | 3 (1 ⚠) | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.8× (z +13.5) | [[Panobinostat (drug)]] 5 µM 0.323× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.505× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 330 | 5 (2 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.54× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A498 (line)]] | wt | 416 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 2.94× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.211× (z -24.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 397 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 6.87× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.375× (z -14.5) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-423 (line)]] | alt | 497 | 0 | 8 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -14.0) ⚠ cell-cycle shift, explains ~27% of this change |
| [[J82 (line)]] | alt | 238 | 3 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.54× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -13.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LOX-IMVI (line)]] | wt | 222 | 3 (1 ⚠) | 4 (4 ⚠) | [[Trametinib (drug)]] 5 µM 2.16× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.08× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.383× (z -12.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 121 | 3 (2 ⚠) | 4 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +17.4) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 1.91× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.320× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SHP-77 (line)]] | alt | 560 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.221× (z -22.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 430 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -17.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.358× (z -9.5) |
| [[Hs 766T (line)]] | wt | 421 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.17× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.306× (z -15.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 110 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +30.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 16.8× (z +20.7) | [[Dinaciclib (drug)]] 5 µM 0.517× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 422 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -14.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.470× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 306 | 1 | 5 (5 ⚠) | [[PH-797804 (drug)]] 5 µM 3.08× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HepG2_C3A (line)]] | wt | 287 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -14.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[PANC-1 (line)]] | alt | 204 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.93× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.500× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 94.2 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.09× (z +18.4) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.297× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Panc 03.27 (line)]] | alt | 283 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.85× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.379× (z -10.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 413 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.305× (z -12.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C32 (line)]] | wt | 182 | 1 | 2 (2 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.61× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.50× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.213× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H23 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.7) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[AN3 CA (line)]] | alt | 37.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 135 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 60.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 59.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 22.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.1 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 639 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 488 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 25.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSC]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MARCKS]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[IL6]] | +0.67 | +0.66 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 630 |
| [[KMO]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MYPN]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[AHR]] | +0.62 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[KYNU]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[ZEB2]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[CYP1B1]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CCDC148]] | +0.60 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[CPEB2]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR89A]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[PHKA1]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[GLMN]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[GK5]] | -0.53 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[TRMT2B]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[WRN]] | -0.52 | -0.55 / -0.47 | both halves | 2e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[GPR89B]] | -0.51 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[CMTM4]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TMEM181]] | -0.50 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SLC30A6]] | -0.50 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[IQCB1]] | -0.49 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ENTPD6]] | -0.49 | -0.51 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NHS]] | B | NHS activity raises NR3C1's level | lines that do not express NHS (17) vs lines expressing it (33) | 2.67× lower at baseline in the lines without NHS | 0.009 | ⚠ within organs, on part of the lines; also absent: ANKRD29, WNT7B, ABCC3 |
| [[DUSP10]] | B | DUSP10 activity raises NR3C1's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 4.32× lower at baseline in the lines without DUSP10 | 0.012 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[INHBA]] | B | INHBA activity raises NR3C1's level | lines that do not express INHBA (32) vs lines expressing it (18) | 3.51× lower at baseline in the lines without INHBA | 0.037 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, DSCAM, TNIP3 |
| [[RRAD]] | B | RRAD activity raises NR3C1's level | lines that do not express RRAD (31) vs lines expressing it (19) | 4.03× lower at baseline in the lines without RRAD | 0.048 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[GEM]] | B | GEM activity raises NR3C1's level | lines that do not express GEM (9) vs lines expressing it (41) | 2.47× lower at baseline in the lines without GEM | 0.054 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[GBP5]] | B | GBP5 activity raises NR3C1's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 4.51× lower at baseline in the lines without GBP5 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3 |
| [[IL6]] | B | IL6 activity raises NR3C1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 4.35× lower at baseline in the lines without IL6 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[EDIL3]] | B | EDIL3 activity raises NR3C1's level | lines that do not express EDIL3 (28) vs lines expressing it (22) | 4.60× lower at baseline in the lines without EDIL3 | 0.068 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, ENSG00000232949, STAC |
| [[ABI3BP]] | B | ABI3BP activity raises NR3C1's level | lines that do not express ABI3BP (32) vs lines expressing it (18) | 3.92× lower at baseline in the lines without ABI3BP | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000280241, FLI1, DKK3; maybe low, not absent |
| [[ARID5B]] | B | ARID5B activity raises NR3C1's level | lines that do not express ARID5B (6) vs lines expressing it (44) | 2.71× lower at baseline in the lines without ARID5B | 0.082 | ⚠ within organs, on part of the lines; also absent: TNFAIP3, ATXN1, SSUH2 |
| [[MSC-AS1]] | B | MSC-AS1 activity raises NR3C1's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.48× lower at baseline in the lines without MSC-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[EBF1]] | B | EBF1 activity raises NR3C1's level | lines that do not express EBF1 (30) vs lines expressing it (20) | 3.37× lower at baseline in the lines without EBF1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAM12, MSC, ITGA4 |

### Downstream of this gene

*315 arrows, 315 of them with an alert ⚠; grade A 0, B 250, C 65. Shown: the 12 strongest; 303 more arrows (303 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENSG00000243797]] | B | NR3C1 activity lowers ENSG00000243797's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |
| [[OLFM2]] | B | NR3C1 activity lowers OLFM2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |
| [[SQSTM1]] | B | NR3C1 activity lowers SQSTM1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 1.7% of all compounds | 0.014 | ⚠ off-target possible; 3 compounds |
| [[C15orf48]] | B | NR3C1 activity lowers C15orf48's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[GATM]] | B | NR3C1 activity lowers GATM's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[MT2A]] | B | NR3C1 activity raises MT2A's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[TNS2]] | B | NR3C1 activity raises TNS2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.0% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds |
| [[ABI3BP]] | B | NR3C1 activity lowers ABI3BP's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[CA8]] | B | NR3C1 activity lowers CA8's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[DPF3]] | B | NR3C1 activity lowers DPF3's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.2% of all compounds | 0.020 | ⚠ off-target possible; 3 compounds |
| [[ADAMTS1]] | B | NR3C1 activity lowers ADAMTS1's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |
| [[CACNA1A]] | B | NR3C1 activity lowers CACNA1A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.5% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.9, 19.6); signed map (47.9, 23.0). **Vector** length 131, 44.9% of its response variance represented; |z| ≥ 3 in 1,517 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.5 | +8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.5 | +9.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.5 | +15.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.9 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.9 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -6.8 | -8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.7 | -8.9 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.9 | -6.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -4.4 | -4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.1 | -3.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -4.0 | -4.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.9 | -5.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.7 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | nuclear receptor subfamily 3 group C member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.3 — chr5:143,277,931-143,435,512 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GR; previously GRL |
| Gene groups (HGNC) | Nuclear receptor subfamily 3 group C |
| Hallmark sets | UV_RESPONSE_DN, HEME_METABOLISM, HYPOXIA |
| Reactome | 20 pathways, smallest: Regulation of NPAS4 gene transcription; PTK6 Expression; Regulation of NPAS4 gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [P04150](https://www.uniprot.org/uniprotkb/P04150) (Glucocorticoid receptor):

> Receptor for glucocorticoids (GC). Has a dual mode of action: as a transcription factor that binds to glucocorticoid response elements (GRE), both for nuclear and mitochondrial DNA, and as a modulator of other transcription factors. Affects inflammatory responses, cellular proliferation and differentiation in target tissues. Involved in chromatin remodeling. Plays a role in rapid mRNA degradation by binding to the 5' UTR of target mRNAs and interacting with PNRC2 in a ligand-dependent manner …

**Summary**, from NCBI Gene [2908](https://www.ncbi.nlm.nih.gov/gene/2908):

> This gene encodes glucocorticoid receptor, which can function both as a transcription factor that binds to glucocorticoid response elements in the promoters of glucocorticoid responsive genes to activate their transcription, and as a regulator of other transcription factors. This receptor is typically found in the cytoplasm, but upon ligand binding, is transported into the nucleus. It is involved in inflammatory responses, cellular proliferation, and differentiation in target tissues. Mutations …

**Accessions** — [HGNC:7978](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7978) · Entrez [2908](https://www.ncbi.nlm.nih.gov/gene/2908) · UniProt [P04150](https://www.uniprot.org/uniprotkb/P04150) · Ensembl [ENSG00000113580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113580)

## Data

Gene col 3476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3476); `tables/drug_effects.parquet` (78 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3476]; `tensor/DDL_lfc|DDL_z.npy` [3476]; `embed/gene_vectors.npy` [3476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3476 or target_col == 3476). Every well: [[NR3C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NR3C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
