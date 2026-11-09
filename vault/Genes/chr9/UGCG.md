---
symbol: "UGCG"
type: "gene"
col: 7246
ensembl_id: "ENSG00000148154"
name: "UDP-glucose ceramide glucosyltransferase"
location: "9q31.3"
module: 167
arm: "+"
pooled_cpm: 294.26
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 20
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# UGCG

*UDP-glucose ceramide glucosyltransferase* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.85× (z +11.0, q 3e-25, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +10.4, q 8e-23, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.428× (z -21.4, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIFR]] (+0.63, fdr 2e-05), [[PPP2R2A]] (+0.61, fdr 1e-05), [[GPR37]] (+0.60, fdr 2e-05); moves opposite to [[MCM3AP]] (-0.64, fdr 1e-05), [[KMT2D]] (-0.64, fdr 2e-05), [[RCC1L]] (-0.62, fdr 1e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[CCL20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7246.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +11.0 | 3e-25 | 46/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +10.4 | 8e-23 | 44/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +9.6 | 1e-19 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.44×** | +8.3 | 1e-14 | 42/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.37×** | +8.0 | 1e-13 | 27/48 (MIA PaCa-2, H4, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.23×** | +7.5 | 7e-12 | 39/48 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +7.3 | 2e-11 | 41/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +6.9 | 2e-10 | 35/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +6.9 | 2e-10 | 42/49 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.42×** | +6.2 | 3e-08 | 27/48 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +6.1 | 4e-08 | 37/48 (CFPAC-1, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +5.9 | 1e-07 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.3 | 4e-06 | 29/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.72×** | +5.0 | 2e-05 | 25/38 (PANC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 1e-04 | 31/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.005 | 24/47 (CFPAC-1, COLO 205, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.040 | 22/48 (A549, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.050 | 20/48 (SK-MEL-2, A-172, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.058 | 17/48 (Panc 03.27, SHP-77, …) | all doses, stronger at high dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.20× | +3.0 | 0.063 | 15/49 (A-172, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |
| [[vincristine (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.067 | 17/46 (CFPAC-1, HCT15, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7246.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.428×** | -21.4 | 0e+00 | 42/49 (SNU-423, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.575×** | -9.2 | 7e-18 | 34/44 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.609×** | -8.8 | 2e-16 | 35/48 (LOX-IMVI, NCI-H2347, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.746×** | -7.4 | 2e-11 | 31/48 (SNU-423, J82, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -6.2 | 5e-08 | 5/50 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.698×** | -6.0 | 1e-07 | 34/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -5.7 | 9e-07 | 33/48 (LOX-IMVI, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.714×** | -5.6 | 1e-06 | 31/47 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.732×** | -5.5 | 2e-06 | 31/48 (BT-474, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.724×** | -5.4 | 4e-06 | 34/50 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.584×** | -5.0 | 3e-05 | 29/48 (Panc 03.27, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.748×** | -4.8 | 6e-05 | 29/48 (SNU-423, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.630×** | -4.3 | 8e-04 | 23/48 (A498, SNU-423, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.851× | -4.1 | 0.002 | 23/48 (J82, NCI-H1573, …) | top dose only | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **0.667×** | -3.8 | 0.006 | 23/48 (KATO III, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.675×** | -3.7 | 0.009 | 22/48 (LOX-IMVI, A549, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.824×** | -3.3 | 0.032 | 15/49 (SW1417, A-172, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.837× | -3.1 | 0.047 | 18/48 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.076 | 19/48 (NCI-H661, A-172, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.728×** | -2.9 | 0.076 | 18/48 (A498, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.840× | -2.9 | 0.076 | 16/48 (A-172, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7246. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 283 | 9 (4 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.3) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.83× (z +11.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -24.8) |
| [[A498 (line)]] | wt | 499 | 1 (1 ⚠) | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +11.6) ⚠ cell-cycle shift, explains ~95% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -26.3) |
| [[LOX-IMVI (line)]] | wt | 580 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -27.1) |
| [[NCI-H460 (line)]] | wt | 263 | 8 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -24.8) |
| [[BT-474 (line)]] | alt | 359 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -18.0) |
| [[PANC-1 (line)]] | alt | 223 | 7 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.08× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -20.0) |
| [[CFPAC-1 (line)]] | alt | 474 | 3 (2 ⚠) | 4 (3 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.69× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -21.9) |
| [[J82 (line)]] | alt | 960 | 2 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -22.3) |
| [[NCI-H1792 (line)]] | alt | 293 | 4 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.20× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.73× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -21.5) |
| [[SNU-423 (line)]] | alt | 1,019 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -27.9) |
| [[HS-578T (line)]] | alt | 284 | 5 (3 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 3.96× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 289 | 2 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.83× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.270× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 102 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.2) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.62× (z +11.8) | — |
| [[Panc 03.27 (line)]] | alt | 641 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -22.7) |
| [[C32 (line)]] | wt | 143 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +15.6) ⚠ cell-cycle shift, explains ~95% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.96× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 331 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.272× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -14.2) |
| [[A-172 (line)]] | wt | 220 | 1 | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -16.2) |
| [[A-427 (line)]] | wt | 138 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.83× (z +11.9) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.39× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 274 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.40× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.584× (z -8.6) |
| [[LoVo (line)]] | wt | 219 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.12× (z +9.3) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -12.1) |
| [[SW 900 (line)]] | alt | 372 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -15.3) |
| [[H4 (line)]] | wt | 153 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.7) ⚠ cell-cycle shift, explains ~95% of this change | — |
| [[HOP62 (line)]] | alt | 280 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 9.35× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.4) |
| [[Hs 766T (line)]] | wt | 224 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 5.70× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 272 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +8.5) ⚠ cell-cycle shift, explains ~51% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -9.8) |
| [[KATO III (line)]] | alt | 361 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 143 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 6.01× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -14.3) |
| [[RKO (line)]] | wt | 197 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.99× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -10.0) |
| [[CHP-212 (line)]] | wt | 164 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.1) ⚠ cell-cycle shift, explains ~95% of this change | — |
| [[HepG2_C3A (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.88× (z +9.4) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 218 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -12.6) |
| [[LS 180 (line)]] | wt | 220 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 252 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +8.6) | — |
| [[RPMI-7951 (line)]] | alt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -10.0) |
| [[SW 1088 (line)]] | alt | 371 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -9.4) |
| [[SW 1271 (line)]] | alt | 398 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.6) |
| [[SW1417 (line)]] | alt | 224 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.0) ⚠ cell-cycle shift, explains ~95% of this change | — |
| [[SW480 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +8.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 122 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 236 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7246), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIFR]] | +0.63 | +0.46 / +0.54 | both halves | 2e-05 | same gene group |
| [[PPP2R2A]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[GPR37]] | +0.60 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[CFD]] | +0.59 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[GPRC5A]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[RNF114]] | +0.58 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[PIM3]] | +0.56 | +0.43 / +0.56 | both halves | 3e-05 | same gene group |
| [[TSC22D2]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[GPX4]] | +0.56 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[NEDD9]] | +0.56 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[IRS2]] | +0.55 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[PAG1]] | +0.55 | +0.40 / +0.42 | both halves | 5e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP]] | -0.64 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[KMT2D]] | -0.64 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[RCC1L]] | -0.62 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[METTL4]] | -0.61 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[MFN2]] | -0.61 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.61 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[DVL3]] | -0.59 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ACO2]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[DPP3]] | -0.58 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.57 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[PSMC3]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[LIG3]] | -0.55 | -0.37 / -0.48 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCL20]] | B | CCL20 activity raises UGCG's level | lines that do not express CCL20 (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without CCL20 | 0.002 | ⚠ within organs, on part of the lines; also absent: TGM2, CLDN16, GPR39 |
| [[TOP2A]] | B | TOP2A activity raises UGCG's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PLD1]] | B | PLD1 activity raises UGCG's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without PLD1 | 0.033 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity raises UGCG's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without NEDD9 | 0.033 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[RNF144B]] | B | RNF144B activity raises UGCG's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without RNF144B | 0.035 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |
| [[ADRB2]] | B | ADRB2 activity raises UGCG's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 1.64× lower at baseline in the lines without ADRB2 | 0.052 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |
| [[PTGER4]] | B | PTGER4 activity raises UGCG's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 1.95× lower at baseline in the lines without PTGER4 | 0.057 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[REPS2]] | B | REPS2 activity raises UGCG's level | lines that do not express REPS2 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without REPS2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GALNT9, ENSG00000227486, PLPP2; maybe low, not absent |
| [[BASP1]] | B | BASP1 activity raises UGCG's level | lines that do not express BASP1 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without BASP1 | 0.066 | ⚠ within organs, on part of the lines; also absent: S1PR3, VEGFC, SRGN |
| [[VSIR]] | B | VSIR activity raises UGCG's level | lines that do not express VSIR (14) vs lines expressing it (36) | 1.61× lower at baseline in the lines without VSIR | 0.090 | ⚠ within organs, on part of the lines; also absent: PLAAT4, NEURL3, SEPTIN9-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.495). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.9, 16.8); signed map (-9.1, 18.2). **Vector** length 137, 49.4% of its response variance represented; |z| ≥ 3 in 1,528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +14.8 | +10.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +11.5 | +6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.4 | +2.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +7.3 | +2.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.3 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.1 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +4.0 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +6.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.4 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | -10.8 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | -9.7 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -9.1 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.6 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.5 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.7 | -5.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.6 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | UDP-glucose ceramide glucosyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:111,896,814-111,935,369 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GCS |
| Gene groups (HGNC) | UDP-glucose ceramide glucosyltransferases; MicroRNA protein coding host genes |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 4 pathways, smallest: Glycosphingolipid biosynthesis; Glycosphingolipid metabolism; Sphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16739](https://www.uniprot.org/uniprotkb/Q16739) (Ceramide glucosyltransferase):

> Participates in the initial step of the glucosylceramide-based glycosphingolipid/GSL synthetic pathway at the cytosolic surface of the Golgi. Catalyzes the transfer of glucose from UDP-glucose to ceramide to produce glucosylceramide/GlcCer (such as beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine). GlcCer is the core component of glycosphingolipids/GSLs, amphipathic molecules consisting of a ceramide lipid moiety embedded in the outer leaflet of the membrane, linked to one of hundreds of different …

**Summary**, from NCBI Gene [7357](https://www.ncbi.nlm.nih.gov/gene/7357):

> This gene encodes an enzyme that catalyzes the first glycosylation step in the biosynthesis of glycosphingolipids, which are membrane components containing lipid and sugar moieties. The product of this reaction is glucosylceramide, which is the core structure of many glycosphingolipids. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:12524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12524) · Entrez [7357](https://www.ncbi.nlm.nih.gov/gene/7357) · UniProt [Q16739](https://www.uniprot.org/uniprotkb/Q16739) · Ensembl [ENSG00000148154](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148154)

## Data

Gene col 7246: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7246); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7246, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7246]; `tensor/DDL_lfc|DDL_z.npy` [7246]; `embed/gene_vectors.npy` [7246]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7246 or target_col == 7246). Every well: [[UGCG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGCG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
