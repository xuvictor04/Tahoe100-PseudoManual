---
symbol: "CYFIP2"
type: "gene"
col: 623
ensembl_id: "ENSG00000055163"
name: "cytoplasmic FMR1 interacting protein 2"
location: "5q33.3"
module: 62
arm: "+"
pooled_cpm: 23.09
n_lines_expressing: 41
n_dd_up: 27
n_dd_down: 24
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# CYFIP2

*cytoplasmic FMR1 interacting protein 2* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.71× (z +25.4, q 0e+00, up in 35 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.450× (z -20.4, q 0e+00, down in 31 of 38 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.446× (z -14.6, q 0e+00, down in 27 of 38 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PINCR]] (+0.63, fdr 1e-05), [[EDA2R]] (+0.62, fdr 7e-06), [[EI24]] (+0.60, fdr 1e-05); moves opposite to [[ZNF100]] (-0.44, fdr 2e-04), [[MFSD11]] (-0.42, fdr 1e-04), [[CENPL]] (-0.40, fdr 5e-04).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); 12 go from it, the strongest it → [[ZMAT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 13 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.71×** | +25.4 | 0e+00 | 35/38 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.99×** | +19.8 | 0e+00 | 28/38 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.90×** | +19.3 | 0e+00 | 35/37 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.87×** | +19.1 | 0e+00 | 31/38 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.60×** | +17.2 | 0e+00 | 30/38 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.51×** | +16.6 | 0e+00 | 31/38 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.67×** | +12.3 | 1e-32 | 30/39 (LoVo, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.86×** | +11.2 | 2e-27 | 24/37 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +7.1 | 8e-11 | 14/27 (HCT15, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.41×** | +6.2 | 3e-08 | 21/37 (SW480, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.38×** | +5.8 | 4e-07 | 18/37 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.23×** | +4.7 | 1e-04 | 13/39 (BT-474, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.6 | 2e-04 | 15/38 (LoVo, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.27×** | +4.2 | 9e-04 | 14/38 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +4.2 | 1e-03 | 16/39 (HCT15, LoVo, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **1.26×** | +4.1 | 0.001 | 13/37 (A549, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.0 | 0.002 | 9/37 (KATO III, LoVo, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.004 | 13/38 (NCI-H2030, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.450×** | -20.4 | 0e+00 | 31/38 (NCI-H460, J82, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.446×** | -14.6 | 0e+00 | 27/38 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.473×** | -13.6 | 1e-39 | 30/37 (HCT15, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.495×** | -12.7 | 5e-35 | 25/37 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.490×** | -12.5 | 2e-33 | 30/38 (NCI-H460, AN3 CA, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.528×** | -11.6 | 5e-29 | 28/38 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -11.1 | 1e-26 | 29/38 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.706×** | -9.0 | 2e-17 | 21/38 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -7.8 | 4e-13 | 21/37 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.684×** | -6.9 | 3e-10 | 23/38 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -6.5 | 5e-09 | 20/38 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.702×** | -6.4 | 7e-09 | 21/37 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.740×** | -5.5 | 2e-06 | 16/38 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.810×** | -5.4 | 2e-06 | 13/38 (SW480, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.750×** | -5.2 | 6e-06 | 16/38 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.9 | 4e-05 | 15/39 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.773×** | -4.7 | 1e-04 | 12/37 (LoVo, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.772×** | -4.4 | 3e-04 | 13/37 (HEC-1-A, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.778×** | -4.4 | 3e-04 | 8/37 (H4, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.657×** | -4.0 | 0.002 | 16/37 (A549, BT-474, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 0.5 µM |  | **0.815×** | -3.7 | 0.005 | 10/37 (C32, NCI-H2030, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.061 | 6/38 (SW48, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.4 | 11 (6 ⚠) | 8 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.58× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -18.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.324× (z -10.0) |
| [[HT-29 (line)]] | alt | 23.2 | 5 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.20× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -13.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.140× (z -13.5) |
| [[SW480 (line)]] | alt | 22.3 | 6 | 5 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.91× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.362× (z -12.8) |
| [[A498 (line)]] | wt | 17.9 | 10 (7 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.79× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 26.4 | 4 | 5 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.58× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -11.1) |
| [[LoVo (line)]] | wt | 58.1 | 5 (2 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.71× (z +12.3) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.48× (z +12.0) | [[Auranofin (drug)]] 5 µM 0.241× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 16.2 | 5 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.97× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.155× (z -11.0) |
| [[AN3 CA (line)]] | alt | 82.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.199× (z -8.6) |
| [[KATO III (line)]] | alt | 9.44 | 5 | 1 | [[Tucidinostat (drug)]] 5 µM 3.98× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.150× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 7.81 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 9.41× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -8.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LOX-IMVI (line)]] | wt | 38.5 | 3 (2 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.80× (z +11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.35× (z +9.5) | [[Auranofin (drug)]] 5 µM 0.202× (z -12.5) |
| [[NCI-H2347 (line)]] | alt | 7.83 | 5 | 0 | [[Tucidinostat (drug)]] 5 µM 4.54× (z +11.4) | — |
| [[A549 (line)]] | wt | 86.9 | 3 (3 ⚠) | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 2.65× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[J82 (line)]] | alt | 10.6 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.83× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -15.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 31.3 | 3 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.78× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2030 (line)]] | alt | 22.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.0) |
| [[RKO (line)]] | wt | 78.4 | 1 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.24× (z +10.5) ⚠ cell-cycle shift, explains ~71% of this change | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -15.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.276× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 2 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.75× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.1) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW 900 (line)]] | alt | 12.6 | 4 | 0 | [[Belinostat (drug)]] 5 µM 6.55× (z +9.6) | — |
| [[A-427 (line)]] | wt | 76.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.70× (z +9.5) ⚠ cell-cycle shift, explains ~71% of this change | [[Auranofin (drug)]] 5 µM 0.349× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 14.0 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.44× (z +9.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.157× (z -9.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.201× (z -8.5) |
| [[C-33 A (line)]] | alt | 53.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -10.5) |
| [[SNU-1 (line)]] | wt | 48.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW1417 (line)]] | alt | 9.09 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.53× (z +11.2) | — |
| [[A-172 (line)]] | wt | 39.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 4.33× (z +9.0) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[C32 (line)]] | wt | 12.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.04× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 73.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.115× (z -10.4) |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -13.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 10.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.85× (z +9.1) | — |
| [[Panc 03.27 (line)]] | alt | 6.73 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.18× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 66.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PINCR]] | +0.63 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.62 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[EI24]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[ZMAT3]] | +0.60 | +0.51 / +0.73 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[TM7SF3]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[FDXR]] | +0.57 | +0.45 / +0.66 | both halves | 3e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[NTPCR]] | +0.57 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ADAMTS7]] | +0.56 | +0.39 / +0.68 | both halves | 5e-05 |  |
| [[RRM2B]] | +0.56 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[ACER2]] | +0.55 | +0.33 / +0.64 | both halves | 1e-04 |  |
| [[CCDC69]] | +0.54 | +0.34 / +0.57 | both halves | 1e-04 |  |
| [[GDF15]] | +0.54 | +0.47 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF100]] | -0.44 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[MFSD11]] | -0.42 | -0.40 / -0.35 | both halves | 1e-04 |  |
| [[CENPL]] | -0.40 | -0.23 / -0.41 | both halves | 5e-04 | pathway: RHO GTPase Effectors |
| [[MYLK4]] | -0.40 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[CDR2]] | -0.39 | -0.29 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity raises CYFIP2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.54× lower at baseline in the lines without PINCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises CYFIP2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.78× lower at baseline in the lines without EDA2R | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[FDXR]] | B | FDXR activity raises CYFIP2's level | lines that do not express FDXR (8) vs lines expressing it (42) | 3.00× lower at baseline in the lines without FDXR | 0.030 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[CASZ1]] | B | CASZ1 activity raises CYFIP2's level | lines that do not express CASZ1 (10) vs lines expressing it (40) | 3.51× lower at baseline in the lines without CASZ1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SBK1, CPLX1, LLGL2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CYFIP2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BTG2]] | C | BTG2 activity raises CYFIP2's level | lines that do not express BTG2 (6) vs lines expressing it (44) | 4.51× lower at baseline in the lines without BTG2 | 0.024 | ⚠ within organs, on part of the lines; also absent: CYFIP2, SLC37A1; maybe low, not absent; co-absent with the target |
| [[GRIN2C]] | C | GRIN2C activity raises CYFIP2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 3.24× lower at baseline in the lines without GRIN2C | 0.056 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent; co-absent with the target |
| [[TP53]] | C | TP53 activity weakens CYFIP2's drug response | recorded loss-of-function mutation of TP53 in 23 lines vs 16 not recorded | the TP53-altered lines respond 1.31× as strongly (z diff -1.70); strongest at Panobinostat 5 µM: 3.62x vs 1.92x (z diff -3.3) | 0.312 over the table, 0.012 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZMAT3]] | B | CYFIP2 activity raises ZMAT3's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.93× lower at baseline in the lines without CYFIP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[PPM1D]] | B | CYFIP2 activity raises PPM1D's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.01× lower at baseline in the lines without CYFIP2 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[FDXR]] | B | CYFIP2 activity raises FDXR's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.62× lower at baseline in the lines without CYFIP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[TRIAP1]] | B | CYFIP2 activity raises TRIAP1's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.49× lower at baseline in the lines without CYFIP2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[ENPP5]] | B | CYFIP2 activity raises ENPP5's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.32× lower at baseline in the lines without CYFIP2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[EDA2R]] | B | CYFIP2 activity raises EDA2R's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.46× lower at baseline in the lines without CYFIP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[RALGPS1]] | B | CYFIP2 activity raises RALGPS1's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.51× lower at baseline in the lines without CYFIP2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[GXYLT1]] | B | CYFIP2 activity raises GXYLT1's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without CYFIP2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[MGAT4A]] | B | CYFIP2 activity raises MGAT4A's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 3.60× lower at baseline in the lines without CYFIP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[GLS2]] | B | CYFIP2 activity raises GLS2's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.97× lower at baseline in the lines without CYFIP2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[MDM2]] | B | CYFIP2 activity raises MDM2's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 1.77× lower at baseline in the lines without CYFIP2 | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A |
| [[GRIN2C]] | C | CYFIP2 activity raises GRIN2C's level | lines that do not express CYFIP2 (9) vs lines expressing it (41) | 2.29× lower at baseline in the lines without CYFIP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: ENSG00000226965, GRIN2C, SEMA6A; co-absent with the target |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.574). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.8, 37.4); signed map (43.7, -25.3). **Vector** length 115, 33.4% of its response variance represented; |z| ≥ 3 in 1,406 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +25.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.4 | +19.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.5 | +16.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +12.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.9 | +6.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.4 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -1.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.4 | -12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -5.3 | -20.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.1 | -12.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -3.5 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -4.9 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -6.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic FMR1 interacting protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,266,079-157,395,595 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIR121 |
| Gene groups (HGNC) | SCAR/WAVE complex |
| Hallmark sets | XENOBIOTIC_METABOLISM, P53_PATHWAY |
| Reactome | 17 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; FCGR3A-mediated phagocytosis; Leishmania phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96F07](https://www.uniprot.org/uniprotkb/Q96F07) (Cytoplasmic FMR1-interacting protein 2):

> Involved in T-cell adhesion and p53/TP53-dependent induction of apoptosis. Does not bind RNA. As component of the WAVE1 complex, required for BDNF-NTRK2 endocytic trafficking and signaling from early endosomes (By similarity).

**Summary**, from NCBI Gene [26999](https://www.ncbi.nlm.nih.gov/gene/26999):

> Predicted to enable small GTPase binding activity. Involved in several processes, including cell-cell adhesion; positive regulation of proteolysis; and regulation of postsynapse assembly. Located in cytosol; perinuclear region of cytoplasm; and synapse. Part of SCAR complex. Implicated in developmental and epileptic encephalopathy 65. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13760) · Entrez [26999](https://www.ncbi.nlm.nih.gov/gene/26999) · UniProt [Q96F07](https://www.uniprot.org/uniprotkb/Q96F07) · Ensembl [ENSG00000055163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055163)

## Data

Gene col 623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 623); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 623]; `tensor/DDL_lfc|DDL_z.npy` [623]; `embed/gene_vectors.npy` [623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 623 or target_col == 623). Every well: [[CYFIP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYFIP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
