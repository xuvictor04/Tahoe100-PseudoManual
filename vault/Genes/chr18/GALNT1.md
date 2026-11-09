---
symbol: "GALNT1"
type: "gene"
col: 6517
ensembl_id: "ENSG00000141429"
name: "polypeptide N-acetylgalactosaminyltransferase 1"
location: "18q12.2"
module: 78
arm: "+"
pooled_cpm: 102.93
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# GALNT1

*polypeptide N-acetylgalactosaminyltransferase 1* — 18q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.25× (z +20.6, q 0e+00, up in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.20× (z +6.5, q 5e-09, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Radotinib (drug)]] 5 µM: 0.841× (z -6.2, q 2e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNM1L]] (+0.59, fdr 1e-05), [[ITGB1]] (+0.57, fdr 4e-05), [[MSN]] (+0.55, fdr 7e-05); moves opposite to [[TTC9C]] (-0.59, fdr 1e-05), [[NR1H3]] (-0.59, fdr 3e-05), [[WHAMM]] (-0.59, fdr 3e-05).
> It is in [[Module 078]], a single-armed module (apical junction).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6517.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +20.6 | 0e+00 | 45/49 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.10×** | +18.1 | 0e+00 | 38/43 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +14.8 | 0e+00 | 38/45 (SNU-423, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.48×** | +9.9 | 4e-21 | 33/48 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.37×** | +8.0 | 2e-13 | 30/48 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.35×** | +7.6 | 2e-12 | 32/48 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +6.5 | 5e-09 | 22/48 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.26×** | +5.9 | 3e-07 | 25/48 (Panc 03.27, SW1417, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +5.3 | 9e-06 | 24/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.21×** | +4.9 | 5e-05 | 19/49 (A-172, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 18/49 (HEC-1-A, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.14× | +4.5 | 3e-04 | 18/49 (A498, NCI-H2347, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.18× | +4.1 | 0.002 | 17/48 (RPMI-7951, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.002 | 18/49 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.005 | 17/48 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.16× | +3.8 | 0.006 | 6/48 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.008 | 8/48 (Hs 766T, KATO III, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.022 | 8/49 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | 1.14× | +3.2 | 0.034 | 5/48 (NCI-H1792, A-172, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | 1.09× | +3.1 | 0.054 | 8/49 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.054 | 10/48 (A549, HS-578T, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.054 | 11/48 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Allantoin (drug)]] 5 µM |  | 1.08× | +2.9 | 0.078 | 2/48 (A549, HS-578T) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.088 | 11/49 (MIA PaCa-2, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6517.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.841× | -6.2 | 2e-07 | 25/48 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -6.2 | 2e-07 | 23/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.809×** | -5.4 | 2e-05 | 24/48 (NCI-H1792, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.684×** | -5.0 | 7e-05 | 22/49 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.881× | -4.5 | 7e-04 | 14/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.842× | -4.4 | 0.001 | 19/48 (KATO III, NCI-H1792, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.855× | -4.0 | 0.006 | 20/48 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.812×** | -3.8 | 0.012 | 17/48 (SHP-77, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.870× | -3.5 | 0.025 | 11/49 (MIA PaCa-2, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.875× | -3.4 | 0.039 | 20/48 (NCI-H1792, LOX-IMVI, …) | rises with dose | composition shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.915× | -3.2 | 0.071 | 7/48 (J82, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.883× | -3.2 | 0.074 | 15/48 (H4, SNU-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.789×** | -3.1 | 0.075 | 19/48 (SNU-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.887× | -3.0 | 0.098 | 12/48 (KATO III, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6517. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 288 | 1 (1 ⚠) | 5 (5 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 74.1 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 91.1 | 2 | 4 (1 ⚠) | [[Fulvestrant (drug)]] 5 µM 2.36× (z +10.7) | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.170× (z -22.5) |
| [[A498 (line)]] | wt | 44.7 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +14.8) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[HEC-1-A (line)]] | alt | 54.6 | 5 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +11.3) | — |
| [[A-172 (line)]] | wt | 139 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 99.2 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.22× (z +10.7) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[PANC-1 (line)]] | alt | 257 | 0 | 4 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -15.7) ⚠ cell-cycle shift, explains ~59% of this change |
| [[A-427 (line)]] | wt | 171 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.02× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 89.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +17.8) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 76.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 54.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 129 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +12.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 28.7 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.25× (z +8.6) | — |
| [[KATO III (line)]] | alt | 111 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +17.6) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 74.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.93× (z +11.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 114 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.470× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.270× (z -8.6) |
| [[SNU-423 (line)]] | alt | 51.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +13.7) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 177 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 107 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -16.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 50.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +11.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 147 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CHP-212 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +10.1) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 98.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 90.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.58× (z +8.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 86.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 200 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.58× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 42.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.5) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 96.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 164 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0813× (z -12.4) |
| [[SW 900 (line)]] | alt | 41.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.05× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 49.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +11.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 131 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 82.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 97.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6517), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNM1L]] | +0.59 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ITGB1]] | +0.57 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[MSN]] | +0.55 | +0.37 / +0.53 | both halves | 7e-05 |  |
| [[ASPH]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[NUP188]] | +0.55 | +0.47 / +0.58 | both halves | 2e-05 | pathway: SARS-CoV-2 Infection |
| [[GALNT10]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 | same gene group; pathway: O-linked glycosylation |
| [[ACLY]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[MACROH2A1]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[INO80C]] | +0.53 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[NCBP1]] | +0.53 | +0.35 / +0.56 | both halves | 1e-04 |  |
| [[KPNA4]] | +0.53 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[APMAP]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC9C]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[NR1H3]] | -0.59 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[WHAMM]] | -0.59 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[THAP3]] | -0.58 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[YJU2B]] | -0.58 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[CIR1]] | -0.58 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[SAT2]] | -0.57 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[BET1]] | -0.57 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ZNF766]] | -0.57 | -0.46 / -0.60 | both halves | 2e-05 | same gene group |
| [[MPHOSPH8]] | -0.56 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[GOLPH3L]] | -0.56 | -0.54 / -0.64 | both halves | 1e-05 |  |
| [[RRAGC]] | -0.55 | -0.43 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, -26.5); signed map (-8.5, 37.9). **Vector** length 117, 32.0% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +20.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +14.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +6.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +18.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.8 | +4.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +2.6 |
| fall | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -5.1 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.9 | -4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.9 | -6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | +0.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.5 | -3.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -4.1 | -1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.2 — chr18:35,581,117-35,711,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T1 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases; MicroRNA protein coding host genes |
| Hallmark sets | ALLOGRAFT_REJECTION |
| Reactome | 16 pathways, smallest: Maturation of protein 3a_9683673; Maturation of protein 3a_9694719; Translation of Structural Proteins_9683701 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10472](https://www.uniprot.org/uniprotkb/Q10472) (Polypeptide N-acetylgalactosaminyltransferase 1):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Has a broad spectrum of substrates such as apomucin-, MUC5AC-, MUC1- and MUC2-derived peptides.

**Summary**, from NCBI Gene [2589](https://www.ncbi.nlm.nih.gov/gene/2589):

> This gene encodes a member of the UDP-N-acetyl-alpha-D-galactosamine:polypeptide N-acetylgalactosaminyltransferase (GalNAc-T) family of enzymes. GalNAc-Ts initiate mucin-type O-linked glycosylation in the Golgi apparatus by catalyzing the transfer of GalNAc to serine and threonine residues on target proteins. They are characterized by an N-terminal transmembrane domain, a stem region, a lumenal catalytic domain containing a GT1 motif and Gal/GalNAc transferase motif, and a C-terminal …

**Accessions** — [HGNC:4123](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4123) · Entrez [2589](https://www.ncbi.nlm.nih.gov/gene/2589) · UniProt [Q10472](https://www.uniprot.org/uniprotkb/Q10472) · Ensembl [ENSG00000141429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141429)

## Data

Gene col 6517: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6517); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6517, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6517]; `tensor/DDL_lfc|DDL_z.npy` [6517]; `embed/gene_vectors.npy` [6517]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6517 or target_col == 6517). Every well: [[GALNT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
