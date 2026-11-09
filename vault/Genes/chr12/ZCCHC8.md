---
symbol: "ZCCHC8"
type: "gene"
col: 409
ensembl_id: "ENSG00000033030"
name: "zinc finger CCHC-type containing 8"
location: "12q24.31"
module: 46
arm: "+"
pooled_cpm: 84.77
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# ZCCHC8

*zinc finger CCHC-type containing 8* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.49× (z +22.4, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.497× (z -12.2, q 1e-31, down in 45 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.675× (z -6.8, q 1e-09, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC59]] (+0.65, fdr 2e-05), [[RAF1]] (+0.65, fdr 3e-05), [[PGLS-DT]] (+0.65, fdr 2e-05); moves opposite to [[NDFIP2]] (-0.62, fdr 5e-05), [[APEH]] (-0.62, fdr 4e-05), [[CORO1C]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +22.4 | 0e+00 | 46/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.92×** | +18.7 | 0e+00 | 47/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +16.8 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.96×** | +11.7 | 1e-29 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.94×** | +11.5 | 1e-28 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +10.4 | 2e-23 | 43/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +9.6 | 4e-20 | 45/49 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +9.1 | 6e-18 | 41/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.70×** | +8.9 | 4e-17 | 41/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.65×** | +8.9 | 4e-17 | 43/48 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +8.2 | 1e-14 | 42/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +7.9 | 1e-13 | 35/49 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +7.5 | 3e-12 | 37/48 (LoVo, A-427, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.44×** | +6.3 | 1e-08 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +6.1 | 3e-08 | 37/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 1e-07 | 37/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 3e-04 | 32/49 (PANC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.497×** | -12.2 | 1e-31 | 45/49 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -12.2 | 1e-31 | 37/44 (AsPC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.591×** | -8.5 | 4e-15 | 32/45 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.675×** | -6.8 | 1e-09 | 43/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.697×** | -6.3 | 3e-08 | 38/48 (A498, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.782×** | -6.1 | 1e-07 | 36/48 (SW480, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.759×** | -4.8 | 1e-04 | 33/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -4.6 | 3e-04 | 26/49 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -4.3 | 0.001 | 0/50 | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.792×** | -4.1 | 0.003 | 26/48 (HepG2/C3A, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.830×** | -3.1 | 0.083 | 18/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.836× | -3.1 | 0.083 | 15/48 (NCI-H1792, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 88.9 | 11 (3 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 6.85× (z +21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 6.76× (z +21.3) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 74.0 | 12 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.14× (z +21.3) | [[Tucidinostat (drug)]] 0.5 µM 0.547× (z -9.0) |
| [[PANC-1 (line)]] | alt | 89.4 | 9 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +19.2) | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.526× (z -8.6) |
| [[LoVo (line)]] | wt | 97.9 | 9 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.94× (z +22.1) | [[Dinaciclib (drug)]] 0.5 µM 0.444× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 90.5 | 8 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 3.09× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -16.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 89.7 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.81× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.192× (z -19.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 102 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +20.9) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.399× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 79.8 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +17.8) | — |
| [[COLO 205 (line)]] | alt | 62.3 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.1) | — |
| [[HepG2_C3A (line)]] | wt | 117 | 3 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.91× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.374× (z -9.6) |
| [[HOP62 (line)]] | alt | 59.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 105 | 5 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.38× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.12× (z +14.6) | — |
| [[KATO III (line)]] | alt | 55.4 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.85× (z +18.2) | — |
| [[LS 180 (line)]] | wt | 67.3 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.74× (z +17.8) | — |
| [[SW1417 (line)]] | alt | 80.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 79.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 76.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.1) | — |
| [[J82 (line)]] | alt | 95.0 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.4) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 97.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 108 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.3) | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -14.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 102 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -11.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 77.5 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.272× (z -11.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 87.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.424× (z -8.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 53.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 61.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 118 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 51.9 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.05× (z +13.1) | — |
| [[SW 900 (line)]] | alt | 82.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.1) | — |
| [[A-172 (line)]] | wt | 77.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.293× (z -12.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 95.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.52× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 85.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -9.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 96.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.1) | — |
| [[H4 (line)]] | wt | 61.2 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.09× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 93.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 53.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -16.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 70.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -10.4) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 126 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +12.5) | — |
| [[SNU-1 (line)]] | wt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -14.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +11.0) | — |
| [[NCI-H596 (line)]] | alt | 93.6 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.145× (z -8.7) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +12.8) | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0884× (z -10.8) |
| [[SW48 (line)]] | wt | 84.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC59]] | +0.65 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[RAF1]] | +0.65 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[PGLS-DT]] | +0.65 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ARID4B]] | +0.64 | +0.53 / +0.52 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[LRRC37B]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[HOXB7]] | +0.63 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[ZNF785]] | +0.62 | +0.33 / +0.43 | both halves | 1e-04 |  |
| [[NRSN2-AS1]] | +0.61 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[TP53]] | +0.61 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[TMEM267]] | +0.61 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[TRPM7]] | +0.61 | +0.70 / +0.38 | both halves | 7e-05 |  |
| [[UFC1]] | +0.61 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDFIP2]] | -0.62 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[APEH]] | -0.62 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[CORO1C]] | -0.60 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[RNF123]] | -0.59 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[R3HDM4]] | -0.58 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ACTN1]] | -0.57 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[HIF1AN]] | -0.56 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[FAM3C]] | -0.56 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[DCBLD2]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[PHC2]] | -0.56 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[ARHGDIA]] | -0.55 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[RALB]] | -0.54 | -0.37 / -0.38 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ZCCHC8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ZCCHC8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLS3-AS1]] | B | PLS3-AS1 activity lowers ZCCHC8's level | lines that do not express PLS3-AS1 (10) vs lines expressing it (40) | 1.32× higher at baseline in the lines without PLS3-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: COPZ2, CAV2, DNAI1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-8.7, 24.9); signed map (1.1, 0.7). **Vector** length 90.1, 30.0% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +7.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +7.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.2 | +3.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +0.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.7 | -6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.3 | -6.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.1 | -4.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.6 | -4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -6.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.7 | -0.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger CCHC-type containing 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:122,471,600-122,500,932 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434E2220 |
| Gene groups (HGNC) | Zinc fingers CCHC-type; Nuclear exosome targeting complex |
| Reactome | 5 pathways, smallest: Regulation of endogenous retroelements by the Human Silencing Hub (HUSH) complex; Nuclear RNA decay; Regulation of endogenous retroelements |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NZY4](https://www.uniprot.org/uniprotkb/Q6NZY4) (Zinc finger CCHC domain-containing protein 8):

> Scaffolding subunit of the trimeric nuclear exosome targeting (NEXT) complex that is involved in the surveillance and turnover of aberrant transcripts and non-coding RNAs. NEXT functions as an RNA exosome cofactor that directs a subset of non-coding short-lived RNAs for exosomal degradation. May be involved in pre-mRNA splicing (Probable). It is required for 3'-end maturation of telomerase RNA component (TERC), TERC 3'-end targeting to the nuclear RNA exosome, and for telomerase function.

**Summary**, from NCBI Gene [55596](https://www.ncbi.nlm.nih.gov/gene/55596):

> This gene encodes a scaffold protein which serves as an assessory factor to the nuclear RNA exosome complex. The encoded protein forms a trimeric human nuclear exosome targeting (NEXT) complex, together with hMTR4 and the RNA-binding factor RBM7 which promotes the exosomal degradation of non-coding promoter-upstream transcripts, enhancer RNAs and 3'-extended products of histone- and small nuclear RNA transcription. This complex is also thought to recruit the exosome to degrade intronic RNAs via …

**Accessions** — [HGNC:25265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25265) · Entrez [55596](https://www.ncbi.nlm.nih.gov/gene/55596) · UniProt [Q6NZY4](https://www.uniprot.org/uniprotkb/Q6NZY4) · Ensembl [ENSG00000033030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033030)

## Data

Gene col 409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 409); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 409]; `tensor/DDL_lfc|DDL_z.npy` [409]; `embed/gene_vectors.npy` [409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 409 or target_col == 409). Every well: [[ZCCHC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZCCHC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
