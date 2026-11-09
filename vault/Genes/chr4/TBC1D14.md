---
symbol: "TBC1D14"
type: "gene"
col: 5314
ensembl_id: "ENSG00000132405"
name: "TBC1 domain family member 14"
location: "4p16.1"
module: 33
arm: "+"
pooled_cpm: 54.71
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# TBC1D14

*TBC1 domain family member 14* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.63× (z +13.0, q 9e-36, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.464× (z -20.3, q 0e+00, down in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.504× (z -17.5, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBPL]] (+0.70, fdr 7e-06), [[WDR3]] (+0.67, fdr 7e-06), [[DDX54]] (+0.67, fdr 7e-06); moves opposite to [[GPR137C]] (-0.62, fdr 3e-05), [[RO60]] (-0.61, fdr 1e-05), [[TIA1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ARHGAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +13.0 | 9e-36 | 34/48 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +11.4 | 1e-27 | 34/48 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +9.3 | 4e-18 | 31/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.60×** | +6.2 | 8e-08 | 25/48 (A-172, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.54×** | +5.7 | 1e-06 | 21/49 (PANC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +5.1 | 4e-05 | 19/48 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.20×** | +4.9 | 8e-05 | 16/47 (RKO, KATO III, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.16× | +3.9 | 0.006 | 17/47 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | 1.15× | +3.7 | 0.013 | 13/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.10× | +3.5 | 0.024 | 16/49 (RPMI-7951, C32, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.10× | +3.5 | 0.024 | 5/48 (A-172, LoVo, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.5 | 0.026 | 10/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.031 | 10/47 (COLO 205, A-427, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | 1.14× | +3.4 | 0.031 | 16/47 (NCI-H460, NCI-H1792, …) | two highest doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.033 | 8/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.048 | 16/49 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.061 | 6/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.061 | 12/47 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.464×** | -20.3 | 0e+00 | 38/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -18.9 | 0e+00 | 33/43 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.504×** | -17.5 | 0e+00 | 40/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.651×** | -16.1 | 0e+00 | 37/48 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.589×** | -13.0 | 2e-36 | 32/45 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.639×** | -11.9 | 1e-30 | 32/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.660×** | -10.9 | 1e-25 | 31/48 (SNU-1, SW48, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.682×** | -10.2 | 2e-22 | 28/48 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.725×** | -8.5 | 1e-15 | 30/48 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.751×** | -7.6 | 2e-12 | 26/47 (LS 180, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.798×** | -6.0 | 1e-07 | 23/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.824×** | -4.9 | 4e-05 | 19/47 (LoVo, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.839× | -4.7 | 1e-04 | 20/48 (RKO, SW480, …) | rises with dose |  |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.870× | -3.6 | 0.011 | 15/48 (Panc 03.27, HCT15, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.832×** | -3.5 | 0.020 | 12/48 (J82, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.843× | -3.2 | 0.046 | 10/48 (RKO, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.919× | -3.2 | 0.051 | 2/48 (A-172, RKO) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.889× | -3.1 | 0.056 | 16/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.924× | -2.9 | 0.091 | 14/48 (NCI-H2030, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 108 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.359× (z -12.9) |
| [[A498 (line)]] | wt | 77.3 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.395× (z -10.9) |
| [[LoVo (line)]] | wt | 79.5 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.303× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 68.6 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.489× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 52.8 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -14.0) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.344× (z -10.9) |
| [[SW48 (line)]] | wt | 86.8 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.342× (z -9.4) |
| [[SW480 (line)]] | alt | 62.2 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -13.6) |
| [[A-427 (line)]] | wt | 61.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -21.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.460× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 49.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.348× (z -10.9) |
| [[PANC-1 (line)]] | alt | 64.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.340× (z -12.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 42.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.290× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 50.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.257× (z -12.4) |
| [[HOP62 (line)]] | alt | 41.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.392× (z -9.7) |
| [[J82 (line)]] | alt | 49.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.333× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 51.9 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.323× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.395× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -12.4) |
| [[SNU-1 (line)]] | wt | 68.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -13.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -11.4) |
| [[SW1417 (line)]] | alt | 52.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -11.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 83.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -18.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 88.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.297× (z -12.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 79.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 44.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0505× (z -30.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 64.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.401× (z -9.4) |
| [[RKO (line)]] | wt | 59.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.296× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 59.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.361× (z -10.1) |
| [[A-172 (line)]] | wt | 44.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.2) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[AN3 CA (line)]] | alt | 78.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 51.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -11.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 48.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0880× (z -16.1) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 50.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[Hs 766T (line)]] | wt | 28.0 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.294× (z -9.1) |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.314× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 67.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -11.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 63.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 57.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +13.3) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[SNU-423 (line)]] | alt | 44.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.388× (z -9.1) |
| [[SW 1271 (line)]] | alt | 67.4 | 0 | 1 | — | [[Verteporfin (drug)]] 0.05 µM 0.0820× (z -9.0) |
| [[SW 900 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBPL]] | +0.70 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[WDR3]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[DDX54]] | +0.67 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.64 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TAF5L]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[EIF3B]] | +0.63 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PPARGC1B]] | +0.62 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[WDR5]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.62 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[PRMT7]] | +0.62 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TSEN54]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR137C]] | -0.62 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[RO60]] | -0.61 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[TIA1]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[UBE2A]] | -0.59 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[SGO1-AS1]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[OCIAD1]] | -0.54 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.54 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[CDKN2B-AS1]] | -0.54 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PLA2G4C]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TTC6]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP8]] | B | ARHGAP8 activity raises TBC1D14's level | lines that do not express ARHGAP8 (22) vs lines expressing it (28) | 1.43× lower at baseline in the lines without ARHGAP8 | 0.046 | ⚠ within organs, on part of the lines; also absent: AP1M2, SPINT2, FUT3 |
| [[HDAC6]] | B | HDAC6 activity lowers TBC1D14's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.704). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.1, -39.1); signed map (-6.5, -51.7). **Vector** length 99.4, 24.1% of its response variance represented; |z| ≥ 3 in 1,177 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.50 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.50 to 10); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.54 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +5.2 | +6.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +3.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.3 | +11.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +13.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.7 | +2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.3 | +3.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -6.8 | -16.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.7 | -17.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -10.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.7 | -10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.2 | -20.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.0 | -0.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:6,909,242-7,033,118 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1322 |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2M4](https://www.uniprot.org/uniprotkb/Q9P2M4) (TBC1 domain family member 14):

> Plays a role in the regulation of starvation-induced autophagosome formation. Together with the TRAPPIII complex, regulates a constitutive trafficking step from peripheral recycling endosomes to the early Golgi, maintaining the cycling pool of ATG9 required for initiation of autophagy.

**Summary**, from NCBI Gene [57533](https://www.ncbi.nlm.nih.gov/gene/57533):

> Enables protein kinase binding activity. Involved in negative regulation of autophagy; recycling endosome to Golgi transport; and regulation of autophagosome assembly. Located in Golgi apparatus; autophagosome; and recycling endosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29246) · Entrez [57533](https://www.ncbi.nlm.nih.gov/gene/57533) · UniProt [Q9P2M4](https://www.uniprot.org/uniprotkb/Q9P2M4) · Ensembl [ENSG00000132405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132405)

## Data

Gene col 5314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5314); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5314]; `tensor/DDL_lfc|DDL_z.npy` [5314]; `embed/gene_vectors.npy` [5314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5314 or target_col == 5314). Every well: [[TBC1D14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
