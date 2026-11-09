---
symbol: "UXS1"
type: "gene"
col: 3706
ensembl_id: "ENSG00000115652"
name: "UDP-glucuronate decarboxylase 1"
location: "2q12.2"
module: 78
arm: "+"
pooled_cpm: 61.88
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# UXS1

*UDP-glucuronate decarboxylase 1* — 2q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (19 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.71× (z +26.7, q 0e+00, up in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.91× (z +17.4, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.05 µM: 0.794× (z -5.5, q 2e-05, down in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.193×, A549 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.642×, MIA PaCa-2 0.531×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.714×; ⚠ position not correctable); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (A498 0.488×); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.101×); [[Triamcinolone (drug)]] 5 µM in 1 line (A498 0.613×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ENDOD1]] (+0.61, fdr 1e-05), [[NFE2L3]] (+0.57, fdr 1e-05), [[IL1RAP]] (+0.57, fdr 5e-05); moves opposite to [[NGDN]] (-0.57, fdr 4e-05), [[CCDC59]] (-0.57, fdr 1e-04), [[SART3]] (-0.56, fdr 1e-04).
> It is in [[Module 078]], a single-armed module (apical junction).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 27 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.71×** | +26.7 | 0e+00 | 47/48 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.33×** | +22.6 | 0e+00 | 48/48 (SW1417, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.25×** | +21.7 | 0e+00 | 46/48 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.91×** | +17.4 | 0e+00 | 43/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.85×** | +16.5 | 0e+00 | 42/49 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +15.6 | 0e+00 | 41/48 (SW480, C32, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.49×** | +15.1 | 0e+00 | 35/48 (AsPC-1, CFPAC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.55×** | +11.8 | 3e-30 | 37/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.54×** | +11.1 | 6e-27 | 27/42 (HOP62, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.51×** | +11.0 | 4e-26 | 34/48 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.51×** | +9.8 | 4e-21 | 28/45 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.44×** | +9.8 | 5e-21 | 33/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.45×** | +9.5 | 7e-20 | 32/48 (HOP62, PANC-1, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.42×** | +9.4 | 1e-19 | 31/48 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.85×** | +8.3 | 4e-15 | 30/49 (HOP62, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.63×** | +6.6 | 1e-09 | 30/48 (HOP62, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.21×** | +5.1 | 8e-06 | 14/49 (HT-29, SW1417, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.016 | 8/48 (HT-29, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 1.13× | +3.2 | 0.022 | 3/48 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.032 | 12/48 (BT-474, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.0 | 0.049 | 15/48 (LS 180, HT-29, …) | two highest doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 1.12× | +2.9 | 0.055 | 6/48 (H4, hTERT-HPNE, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.14× | +2.9 | 0.055 | 4/48 (HT-29, Hs 766T, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.08× | +2.9 | 0.059 | 11/48 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 1.11× | +2.7 | 0.096 | 10/47 (HT-29, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3706.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.193×, A549 0.402×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (SW480 0.642×, MIA PaCa-2 0.531×; ⚠ cell-cycle shift, would explain all of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.714×; ⚠ position not correctable); [[Clobetasol propionate (drug)]] 0.05 µM in 1 line (A498 0.488×); [[Harringtonine (drug)]] 0.05 µM in 1 line (AN3 CA 0.101×); [[Triamcinolone (drug)]] 5 µM in 1 line (A498 0.613×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **0.794×** | -5.5 | 2e-05 | 20/47 (AN3 CA, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.856× | -5.2 | 5e-05 | 20/48 (SW480, SW 900, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.833×** | -4.7 | 4e-04 | 18/50 (SW480, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.841× | -4.5 | 0.001 | 16/48 (SW480, A498, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.870× | -3.7 | 0.021 | 13/48 (SW 900, A498, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.766×** | -3.6 | 0.027 | 10/50 (A498, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 0.912× | -3.5 | 0.034 | 10/48 (A498, H4, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.879× | -3.5 | 0.034 | 10/48 (SW480, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.881× | -3.4 | 0.041 | 18/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.890× | -3.2 | 0.091 | 13/48 (SW 900, RKO, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.892× | -3.1 | 0.10 | 10/48 (HT-29, BT-474, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.889× | -3.0 | 0.12 | 8/48 (SW480, A498, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 84.2 | 9 (7 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.28× (z +13.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 2.17× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 41.2 | 9 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +15.1) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[HOP62 (line)]] | alt | 42.1 | 9 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +15.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 3.06× (z +11.6) | — |
| [[NCI-H460 (line)]] | wt | 56.9 | 9 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.64× (z +14.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 1.93× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 47.1 | 8 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.3) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.49× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 53.0 | 8 (7 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +11.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.53× (z +10.2) | — |
| [[C32 (line)]] | wt | 33.6 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.06× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.11× (z +10.4) | — |
| [[PANC-1 (line)]] | alt | 68.4 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 159 | 0 | 5 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.537× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.488× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 49.8 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.82× (z +18.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.91× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 44.6 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.92× (z +13.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 47.1 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.84× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 55.4 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +20.6) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 40.6 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +13.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[LOX-IMVI (line)]] | wt | 37.6 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.15× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 84.9 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H23 (line)]] | alt | 68.7 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.85× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 5 µM 0.193× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[SK-MEL-2 (line)]] | alt | 43.6 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.12× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[COLO 205 (line)]] | alt | 30.6 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +13.7) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 44.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +12.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.53× (z +8.6) | — |
| [[LoVo (line)]] | wt | 35.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.21× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 61.5 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.0) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 54.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.1) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[A549 (line)]] | wt | 114 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.443× (z -8.7) |
| [[H4 (line)]] | wt | 70.9 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.95× (z +9.2) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Hs 766T (line)]] | wt | 21.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[HS-578T (line)]] | alt | 33.4 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 75.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.02× (z +9.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 69.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.378× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[AN3 CA (line)]] | alt | 43.0 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.101× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 90.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.07× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[KATO III (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[NCI-H1573 (line)]] | alt | 49.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.81× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.38× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 1271 (line)]] | alt | 53.4 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0647× (z -9.2) |
| [[SW 900 (line)]] | alt | 149 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.08× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 93.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 82.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENDOD1]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[NFE2L3]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[IL1RAP]] | +0.57 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[ATP13A3]] | +0.56 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[EML4]] | +0.56 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[SHB]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[ECE1]] | +0.54 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[OSBPL3]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ITGA6]] | +0.54 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[DPY19L1]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[EHD4]] | +0.54 | +0.47 / +0.35 | both halves | 1e-04 |  |
| [[TIAM1]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NGDN]] | -0.57 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CCDC59]] | -0.57 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[SART3]] | -0.56 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[BRAP]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ZNF830]] | -0.55 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[GCC1]] | -0.55 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[SLC4A1AP]] | -0.54 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[PAAF1]] | -0.53 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[AEBP2]] | -0.53 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[NKAPD1]] | -0.52 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[VPS39]] | -0.52 | -0.38 / -0.49 | both halves | 7e-05 |  |
| [[PRANCR]] | -0.52 | -0.36 / -0.40 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.1, 15.4); signed map (3.0, 43.1). **Vector** length 107, 29.0% of its response variance represented; |z| ≥ 3 in 1,388 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.7 | +15.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.1 | +17.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.0 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +4.0 | +22.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +8.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.5 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.4 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.6 | -3.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.8 | -5.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | UDP-glucuronate decarboxylase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q12.2 — chr2:106,093,308-106,194,301 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23591, UGD, SDR6E1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily; Decarboxylases |
| Reactome | 7 pathways, smallest: Formation of the active cofactor, UDP-glucuronate; Glucuronidation; Glycosaminoglycan-protein linkage region biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBZ7](https://www.uniprot.org/uniprotkb/Q8NBZ7) (UDP-glucuronic acid decarboxylase 1):

> Catalyzes the NAD-dependent decarboxylation of UDP-glucuronic acid to UDP-xylose. Necessary for the biosynthesis of the core tetrasaccharide in glycosaminoglycan biosynthesis. Catalyzes the synthesis of UDP-xylose in two steps: the hydroxyl group of UDP-glucuronic acid is first oxidized using an enzyme-bound NAD(+) as electron acceptor, favoring the decarboxylation yielding a UDP-4-ketoxylose reaction intermediate and a reduced cofactor NADH bound to the catalytic pocket. In the second step, …

**Summary**, from NCBI Gene [80146](https://www.ncbi.nlm.nih.gov/gene/80146):

> This gene encodes an enzyme found in the perinuclear Golgi which catalyzes the synthesis of UDP-xylose used in glycosaminoglycan (GAG) synthesis on proteoglycans. The GAG chains are covalently attached to proteoglycans which participate in signaling pathways during development. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2014]

**Accessions** — [HGNC:17729](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17729) · Entrez [80146](https://www.ncbi.nlm.nih.gov/gene/80146) · UniProt [Q8NBZ7](https://www.uniprot.org/uniprotkb/Q8NBZ7) · Ensembl [ENSG00000115652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115652)

## Data

Gene col 3706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3706); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3706]; `tensor/DDL_lfc|DDL_z.npy` [3706]; `embed/gene_vectors.npy` [3706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3706 or target_col == 3706). Every well: [[UXS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UXS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
