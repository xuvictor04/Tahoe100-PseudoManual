---
symbol: "BIN3"
type: "gene"
col: 7184
ensembl_id: "ENSG00000147439"
name: "bridging integrator 3"
location: "8p21.3"
module: 212
arm: "+"
pooled_cpm: 72.73
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 13
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/212"]
generated_by: "tahoemap"
---

# BIN3

*bridging integrator 3* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.87× (z +14.5, q 8e-45, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.394× (z -21.5, q 0e+00, down in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.672× (z -9.2, q 5e-18, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAP30BP]] (+0.69, fdr 7e-06), [[SDF2]] (+0.65, fdr 7e-06), [[IGBP1]] (+0.65, fdr 7e-06); moves opposite to [[COX11]] (-0.59, fdr 1e-05), [[CFL2]] (-0.56, fdr 1e-05), [[RAB14]] (-0.54, fdr 2e-05).
> It is in [[Module 212]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7184.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.87×** | +14.5 | 8e-45 | 44/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +14.0 | 3e-42 | 43/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.79×** | +12.8 | 5e-35 | 41/48 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +10.4 | 2e-23 | 40/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +9.4 | 4e-19 | 38/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.13×** | +9.1 | 6e-18 | 33/48 (SW480, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +7.1 | 1e-10 | 31/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +6.7 | 1e-09 | 34/49 (MIA PaCa-2, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +6.2 | 3e-08 | 23/48 (NCI-H1792, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +6.2 | 4e-08 | 28/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.28×** | +5.8 | 4e-07 | 29/49 (LOX-IMVI, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.6 | 9e-07 | 27/47 (BT-474, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.17× | +5.1 | 2e-05 | 20/49 (SW 900, NCI-H460, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +5.0 | 2e-05 | 26/48 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.7 | 1e-04 | 21/45 (SNU-423, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.011 | 12/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Folic acid (drug)]] 5 µM |  | 1.10× | +3.1 | 0.052 | 5/48 (Hs 766T, H4, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.20×** | +3.1 | 0.052 | 13/47 (H4, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7184.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.394×** | -21.5 | 0e+00 | 46/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.421×** | -19.2 | 0e+00 | 37/44 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.578×** | -12.2 | 8e-32 | 40/47 (H4, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.517×** | -11.6 | 4e-29 | 34/45 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -9.2 | 5e-18 | 37/48 (LoVo, A549, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.718×** | -7.6 | 2e-12 | 39/48 (C32, A-427, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.801×** | -7.2 | 4e-11 | 25/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.744×** | -6.6 | 4e-09 | 31/48 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.754×** | -6.3 | 2e-08 | 28/48 (LoVo, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -6.1 | 6e-08 | 27/49 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.776×** | -5.8 | 3e-07 | 29/49 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.779×** | -5.7 | 4e-07 | 25/48 (KATO III, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.732×** | -5.5 | 2e-06 | 28/48 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -5.5 | 2e-06 | 26/48 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.782×** | -5.5 | 2e-06 | 27/47 (SW480, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.846× | -5.4 | 3e-06 | 21/48 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.785×** | -5.4 | 3e-06 | 25/48 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -4.7 | 8e-05 | 24/50 (A-427, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.819×** | -4.6 | 1e-04 | 23/47 (SW480, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7184. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 132 | 2 | 6 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.574× (z -10.3) |
| [[LoVo (line)]] | wt | 78.4 | 2 | 6 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.98× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.139× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.411× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 200 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0640× (z -34.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.582× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 76.4 | 4 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.77× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -15.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 124 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -19.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 65.4 | 1 | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.24× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -15.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 141 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 80.2 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.78× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -14.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 56.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -10.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 97.3 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +22.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.268× (z -13.2) ⚠ toxic |
| [[SW480 (line)]] | alt | 116 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.25× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -26.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 77.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 68.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +18.7) | [[Ponatinib (drug)]] 5 µM 0.361× (z -9.7) |
| [[H4 (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -22.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 113 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 82.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +29.5) | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -18.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 66.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -10.1) |
| [[A549 (line)]] | wt | 77.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -14.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 81.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -12.4) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 77.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0575× (z -22.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 57.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 74.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -16.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 61.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -19.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 81.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0989× (z -25.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 59.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -16.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 69.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -16.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 63.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.03× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -11.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 46.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 30.4 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.69× (z +9.7) | — |
| [[RKO (line)]] | wt | 86.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.24× (z +9.0) | — |
| [[SW48 (line)]] | wt | 74.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 85.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7184), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAP30BP]] | +0.69 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[SDF2]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[IGBP1]] | +0.65 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[SYCE1L]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SENP5]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[RAB7A]] | +0.62 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ATAT1]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[BLZF1]] | +0.60 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[GP6-AS1]] | +0.59 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[TBC1D22A]] | +0.59 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ZKSCAN5]] | +0.59 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COX11]] | -0.59 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[CFL2]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[RAB14]] | -0.54 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[CASC3]] | -0.53 | -0.36 / -0.63 | both halves | 1e-04 |  |
| [[RDX]] | -0.53 | -0.44 / -0.63 | both halves | 3e-05 |  |
| [[TNPO1]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[HNRNPH3]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[MATR3]] | -0.53 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[EFR3A]] | -0.52 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[PATL1]] | -0.52 | -0.43 / -0.55 | both halves | 4e-05 |  |
| [[TMEM106B]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[RAB23]] | -0.52 | -0.59 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 212]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.7, -24.9); signed map (7.9, 15.8). **Vector** length 132, 40.6% of its response variance represented; |z| ≥ 3 in 1,267 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.6 | +12.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.4 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +14.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +7.1 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.0 | +10.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.9 | +6.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.2 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.2 | -9.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.5 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.5 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -7.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.7 | -5.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -5.8 |

## What is on record

|  |  |
|---|---|
| Name | bridging integrator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,620,418-22,669,148 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | N-BAR domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQY0](https://www.uniprot.org/uniprotkb/Q9NQY0) (Bridging integrator 3):

> Involved in cytokinesis and septation where it has a role in the localization of F-actin.

**Summary**, from NCBI Gene [55909](https://www.ncbi.nlm.nih.gov/gene/55909):

> The product of this gene is a member of the BAR domain protein family. The encoded protein is comprised solely of a BAR domain which is predicted to form coiled-coil structures and proposed to mediate dimerization, sense and induce membrane curvature, and bind small GTPases. BAR domain proteins have been implicated in endocytosis, intracellular transport, and a diverse set of other processes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1054) · Entrez [55909](https://www.ncbi.nlm.nih.gov/gene/55909) · UniProt [Q9NQY0](https://www.uniprot.org/uniprotkb/Q9NQY0) · Ensembl [ENSG00000147439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147439)

## Data

Gene col 7184: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7184); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7184, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7184]; `tensor/DDL_lfc|DDL_z.npy` [7184]; `embed/gene_vectors.npy` [7184]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7184 or target_col == 7184). Every well: [[BIN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
