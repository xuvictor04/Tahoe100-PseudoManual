---
symbol: "HSDL2"
type: "gene"
col: 4070
ensembl_id: "ENSG00000119471"
name: "hydroxysteroid dehydrogenase like 2"
location: "9q32"
module: 45
arm: "+"
pooled_cpm: 74.54
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# HSDL2

*hydroxysteroid dehydrogenase like 2* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +14.8, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.85× (z +13.7, q 1e-40, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.673× (z -8.7, q 2e-15, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNG1]] (+0.67, fdr 1e-05), [[ATP6AP2]] (+0.64, fdr 1e-05), [[EI24]] (+0.59, fdr 2e-05); moves opposite to [[CLCF1]] (-0.57, fdr 1e-05), [[DDX28]] (-0.56, fdr 4e-05), [[ZNF75A]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4070.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +14.8 | 0e+00 | 47/49 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.90×** | +14.4 | 2e-44 | 43/48 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.85×** | +13.7 | 1e-40 | 43/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +12.6 | 4e-34 | 45/48 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +11.0 | 5e-26 | 36/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +10.7 | 9e-25 | 34/45 (LoVo, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.74×** | +10.3 | 5e-23 | 34/42 (MIA PaCa-2, LoVo, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +8.5 | 2e-15 | 33/48 (NCI-H2347, HEC-1-A, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.4 | 2e-15 | 37/50 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +7.3 | 1e-11 | 34/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +7.3 | 2e-11 | 41/49 (NCI-H23, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.44×** | +6.8 | 4e-10 | 36/48 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +6.2 | 2e-08 | 29/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **1.26×** | +4.3 | 6e-04 | 24/47 (A498, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.011 | 22/47 (A549, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.014 | 16/48 (LS 180, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Mifepristone (drug)]] 0.5 µM |  | 1.16× | +3.4 | 0.020 | 17/48 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.022 | 12/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.027 | 9/48 (SW480, A-427, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.055 | 10/49 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +2.9 | 0.095 | 4/48 (HepG2/C3A, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4070.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.673×** | -8.7 | 2e-15 | 32/48 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.896× | -8.4 | 1e-14 | 2/50 (SW 1088, CHP-212) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.512×** | -7.8 | 9e-13 | 40/48 (RKO, Panc 03.27, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.794×** | -7.3 | 3e-11 | 28/48 (NCI-H23, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.707×** | -6.5 | 1e-08 | 30/48 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.594×** | -6.1 | 1e-07 | 31/49 (SW480, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.777×** | -5.7 | 1e-06 | 27/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.791×** | -5.3 | 1e-05 | 23/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.806×** | -4.8 | 9e-05 | 23/48 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.812×** | -4.7 | 2e-04 | 23/48 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.826×** | -4.3 | 9e-04 | 21/48 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.834× | -4.1 | 0.002 | 21/48 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.846× | -3.7 | 0.008 | 18/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.852× | -3.6 | 0.013 | 14/48 (NCI-H460, SNU-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.848× | -3.5 | 0.018 | 19/47 (RKO, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.859× | -3.3 | 0.030 | 17/48 (LS 180, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4070. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 95.0 | 7 (3 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +14.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 87.6 | 5 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.17× (z +15.3) | [[Digitoxin (drug)]] 5 µM 0.490× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.531× (z -8.7) |
| [[PANC-1 (line)]] | alt | 66.4 | 4 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.02× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.502× (z -10.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 84.7 | 4 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[KATO III (line)]] | alt | 93.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.36× (z +10.9) | — |
| [[LoVo (line)]] | wt | 82.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +15.3) | — |
| [[LS 180 (line)]] | wt | 99.9 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +13.5) | [[Ixazomib citrate (drug)]] 5 µM 0.464× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 41.2 | 4 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.96× (z +10.3) | — |
| [[RKO (line)]] | wt | 122 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -15.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.145× (z -12.5) |
| [[SW1417 (line)]] | alt | 58.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.68× (z +10.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.54× (z +10.0) | — |
| [[SW480 (line)]] | alt | 76.4 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +13.0) ⚠ toxic; transcription drop | [[PH-797804 (drug)]] 5 µM 0.320× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 78.0 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.16× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -14.2) |
| [[NCI-H23 (line)]] | alt | 45.0 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.7) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.278× (z -12.0) |
| [[HS-578T (line)]] | alt | 52.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HT-29 (line)]] | alt | 99.5 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +9.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.23× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 74.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +12.1) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 133 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.464× (z -9.3) |
| [[A-172 (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -9.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HCT15 (line)]] | alt | 97.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 90.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +11.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 51.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.430× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 167 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -13.3) ⚠ cell-cycle shift, explains ~18% of this change |
| [[NCI-H1573 (line)]] | alt | 25.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +11.5) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.165× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.500× (z -8.6) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW48 (line)]] | wt | 54.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[A-427 (line)]] | wt | 57.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 95.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 84.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4070), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNG1]] | +0.67 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[ATP6AP2]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[EI24]] | +0.59 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[PDK3]] | +0.59 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[BBS7]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[AP3S1]] | +0.57 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[DDHD2]] | +0.57 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[PGAP1]] | +0.57 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[SEPTIN2]] | +0.56 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[PIK3C2A]] | +0.56 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ACO1]] | +0.56 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[RNPEP]] | +0.56 | +0.43 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLCF1]] | -0.57 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[DDX28]] | -0.56 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ZNF75A]] | -0.56 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CD2BP2]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CENPBD1P]] | -0.55 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[FEM1A]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[ZNF513]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[DNAJB12]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[TOE1]] | -0.54 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[NIP7]] | -0.53 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[JAGN1]] | -0.53 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[TSSC4]] | -0.53 | -0.40 / -0.52 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HSDL2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.440). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-19.7, -18.5); signed map (-51.2, -6.7). **Vector** length 101, 28.1% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.1 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.1 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.7 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.6 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -6.1 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.6 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.4 | -3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | +0.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | hydroxysteroid dehydrogenase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:112,380,080-112,472,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SDR13C1; previously C9orf99 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; SCP2 domain containing |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6YN16](https://www.uniprot.org/uniprotkb/Q6YN16) (Hydroxysteroid dehydrogenase-like protein 2):

> Has apparently no steroid dehydrogenase activity. Controls bile acid (BA) and lipid metabolism in response to nutritional cues.

**Summary**, from NCBI Gene [84263](https://www.ncbi.nlm.nih.gov/gene/84263):

> Predicted to enable oxidoreductase activity. Involved in cholesterol homeostasis. Located in mitochondrion and peroxisome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18572) · Entrez [84263](https://www.ncbi.nlm.nih.gov/gene/84263) · UniProt [Q6YN16](https://www.uniprot.org/uniprotkb/Q6YN16) · Ensembl [ENSG00000119471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119471)

## Data

Gene col 4070: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4070); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4070, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4070]; `tensor/DDL_lfc|DDL_z.npy` [4070]; `embed/gene_vectors.npy` [4070]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4070 or target_col == 4070). Every well: [[HSDL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSDL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
