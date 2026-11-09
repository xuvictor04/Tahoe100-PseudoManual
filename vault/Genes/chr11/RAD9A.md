---
symbol: "RAD9A"
type: "gene"
col: 10275
ensembl_id: "ENSG00000172613"
name: "RAD9 checkpoint clamp component A"
location: "11q13.2"
module: 72
arm: "+"
pooled_cpm: 46.91
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# RAD9A

*RAD9 checkpoint clamp component A* — 11q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.23× (z +20.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.593× (z -13.0, q 8e-36, down in 31 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.633× (z -11.4, q 1e-27, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED31]] (+0.77, fdr 7e-06), [[FTL]] (+0.68, fdr 7e-06), [[SLC25A29]] (+0.65, fdr 7e-06); moves opposite to [[SF3B3]] (-0.64, fdr 1e-05), [[CPNE1]] (-0.62, fdr 1e-05), [[GUF1]] (-0.61, fdr 1e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ATG9B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +20.0 | 0e+00 | 48/48 (NCI-H1792, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.15×** | +19.0 | 0e+00 | 47/48 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +18.2 | 0e+00 | 45/48 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.07×** | +18.1 | 0e+00 | 45/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.00×** | +16.3 | 0e+00 | 47/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +14.4 | 4e-45 | 33/49 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.73×** | +13.7 | 1e-40 | 41/48 (HOP62, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +8.8 | 1e-16 | 37/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +7.4 | 1e-11 | 34/47 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +7.3 | 2e-11 | 26/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +7.0 | 1e-10 | 33/49 (NCI-H1792, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +6.3 | 2e-08 | 25/49 (HEC-1-A, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.47×** | +5.0 | 3e-05 | 15/43 (PANC-1, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.3 | 6e-04 | 16/48 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.17× | +4.0 | 0.003 | 8/49 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.003 | 9/47 (SNU-1, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.593×** | -13.0 | 8e-36 | 31/45 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.618×** | -11.5 | 3e-28 | 30/48 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.633×** | -11.4 | 1e-27 | 33/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.650×** | -10.7 | 1e-24 | 29/48 (CFPAC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -10.3 | 1e-22 | 25/41 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.698×** | -8.9 | 4e-17 | 28/48 (MIA PaCa-2, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -8.8 | 2e-16 | 33/49 (BT-474, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.813×** | -7.3 | 3e-11 | 25/48 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.612×** | -6.4 | 1e-08 | 25/48 (BT-474, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.790×** | -5.6 | 1e-06 | 23/47 (C-33 A, NCI-H23, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.790×** | -5.4 | 3e-06 | 22/42 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.791×** | -5.4 | 4e-06 | 22/47 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.830×** | -4.6 | 2e-04 | 19/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.886× | -4.3 | 8e-04 | 13/49 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.841× | -4.1 | 0.001 | 16/47 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.023 | 14/48 (AsPC-1, CFPAC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Vismodegib (drug)]] 0.5 µM |  | 0.876× | -3.3 | 0.030 | 7/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | 0.877× | -3.3 | 0.031 | 5/48 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.047 | 9/47 (AsPC-1, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.878× | -3.1 | 0.049 | 11/48 (NCI-H2347, LoVo, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.790×** | -3.1 | 0.054 | 13/48 (AsPC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.881× | -3.0 | 0.058 | 9/48 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.888× | -2.9 | 0.075 | 13/47 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 95.9 | 5 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.43× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[PANC-1 (line)]] | alt | 45.9 | 3 | 5 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.75× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.479× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 67.4 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -14.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[BT-474 (line)]] | alt | 99.1 | 5 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.65× (z +11.6) | [[TAK-901 (drug)]] 5 µM 0.233× (z -9.1) |
| [[HOP62 (line)]] | alt | 24.7 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.30× (z +12.1) | — |
| [[A-172 (line)]] | wt | 30.7 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.76× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.305× (z -9.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.324× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 50.4 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.64× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 51.1 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.0744× (z -26.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 86.1 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -13.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 55.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.457× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 83.5 | 1 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.17× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -20.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 54.1 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -12.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 67.3 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.41× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.0536× (z -28.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 58.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 68.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.387× (z -9.0) |
| [[RKO (line)]] | wt | 22.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.99× (z +9.5) | — |
| [[A-427 (line)]] | wt | 53.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.41× (z +9.6) | — |
| [[A498 (line)]] | wt | 26.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 36.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.47× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -14.1) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 70.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -10.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 56.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -11.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 65.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[J82 (line)]] | alt | 25.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.227× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SW1417 (line)]] | alt | 74.2 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.28× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 66.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -9.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.231× (z -13.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 20.0 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0788× (z -12.9) |
| [[Hs 766T (line)]] | wt | 44.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 20.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +14.6) | — |
| [[SHP-77 (line)]] | alt | 54.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change |
| [[SNU-423 (line)]] | alt | 38.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +8.7) | — |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -9.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 65.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -13.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 63.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED31]] | +0.77 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[FTL]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SLC25A29]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MBOAT7]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ABHD3]] | +0.63 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[CCDC32]] | +0.62 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PHF1]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[HSPA1B]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[HSPA1A]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[BAHD1]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[VRK3]] | +0.61 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[FLYWCH1]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3B3]] | -0.64 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[CPNE1]] | -0.62 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[GUF1]] | -0.61 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CEP63]] | -0.61 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[AASDHPPT]] | -0.61 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ANAPC13]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[AGL]] | -0.60 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZNF252P-1]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[COX18]] | -0.57 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[RAD50]] | -0.57 | -0.48 / -0.53 | both halves | 2e-05 | pathway: Cell Cycle Checkpoints; STRING 612 |
| [[POLI]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 | STRING 525 |
| [[POGLUT1]] | -0.56 | -0.50 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATG9B]] | B | ATG9B activity raises RAD9A's level | lines that do not express ATG9B (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without ATG9B | 0.007 | ⚠ within organs, on part of the lines; also absent: AFAP1L2, GJB3, EREG |
| [[MICB]] | B | MICB activity lowers RAD9A's level | lines that do not express MICB (13) vs lines expressing it (37) | 1.71× higher at baseline in the lines without MICB | 0.025 | ⚠ within organs, on part of the lines; also absent: SPHK1, ENSG00000234405, MYL9 |
| [[CLDN1]] | B | CLDN1 activity raises RAD9A's level | lines that do not express CLDN1 (23) vs lines expressing it (27) | 1.40× lower at baseline in the lines without CLDN1 | 0.053 | ⚠ within organs, on part of the lines; also absent: EDN1, CRIP1, SHH |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.7, -6.4); signed map (-25.0, 10.1). **Vector** length 115, 32.1% of its response variance represented; |z| ≥ 3 in 1,324 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.0 | +18.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.9 | +13.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.5 | +16.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.6 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +7.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.6 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.5 | -10.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.5 | -11.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.3 | -7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -7.1 | -11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.6 | -4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -6.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -5.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | RAD9 checkpoint clamp component A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.2 — chr11:67,317,871-67,398,410 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously RAD9 |
| Gene groups (HGNC) | Checkpoint clamp complex |
| Hallmark sets | P53_PATHWAY |
| Reactome | 21 pathways, smallest: Impaired BRCA2 binding to RAD51; Activation of ATR in response to replication stress; HDR through Single Strand Annealing (SSA) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99638](https://www.uniprot.org/uniprotkb/Q99638) (Cell cycle checkpoint control protein RAD9A):

> Component of the 9-1-1 cell-cycle checkpoint response complex that plays a major role in DNA repair. The 9-1-1 complex is recruited to DNA lesion upon damage by the RAD17-replication factor C (RFC) clamp loader complex. Acts then as a sliding clamp platform on DNA for several proteins involved in long-patch base excision repair (LP-BER). The 9-1-1 complex stimulates DNA polymerase beta (POLB) activity by increasing its affinity for the 3'-OH end of the primer-template and stabilizes POLB to …

**Summary**, from NCBI Gene [5883](https://www.ncbi.nlm.nih.gov/gene/5883):

> This gene product is highly similar to Schizosaccharomyces pombe rad9, a cell cycle checkpoint protein required for cell cycle arrest and DNA damage repair. This protein possesses 3' to 5' exonuclease activity, which may contribute to its role in sensing and repairing DNA damage. It forms a checkpoint protein complex with RAD1 and HUS1. This complex is recruited by checkpoint protein RAD17 to the sites of DNA damage, which is thought to be important for triggering the checkpoint-signaling …

**Accessions** — [HGNC:9827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9827) · Entrez [5883](https://www.ncbi.nlm.nih.gov/gene/5883) · UniProt [Q99638](https://www.uniprot.org/uniprotkb/Q99638) · Ensembl [ENSG00000172613](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172613)

## Data

Gene col 10275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10275); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10275]; `tensor/DDL_lfc|DDL_z.npy` [10275]; `embed/gene_vectors.npy` [10275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10275 or target_col == 10275). Every well: [[RAD9A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD9A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
