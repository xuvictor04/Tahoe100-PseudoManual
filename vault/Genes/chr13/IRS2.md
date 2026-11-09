---
symbol: "IRS2"
type: "gene"
col: 11758
ensembl_id: "ENSG00000185950"
name: "insulin receptor substrate 2"
location: "13q34"
module: 113
arm: "+"
pooled_cpm: 166.6
n_lines_expressing: 44
n_dd_up: 37
n_dd_down: 18
n_dd_up_clean: 30
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# IRS2

*insulin receptor substrate 2* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.77× (z +10.7, q 1e-23, up in 32 of 42 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.30× (z +8.2, q 5e-14, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.455× (z -10.0, q 9e-21, down in 28 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.397× (z -6.4, q 2e-08, down in 38 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT1F]] (+0.70, fdr 7e-06), [[MT1E]] (+0.68, fdr 7e-06), [[MT1M]] (+0.67, fdr 7e-06); moves opposite to [[MACROH2A1]] (-0.49, fdr 3e-05), [[KLC2]] (-0.49, fdr 3e-05), [[STX16]] (-0.49, fdr 4e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TXNIP]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FAM227A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11758.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.77×** | +10.7 | 1e-23 | 32/42 (COLO 205, AsPC-1, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.30×** | +8.2 | 5e-14 | 38/43 (Panc 03.27, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +7.2 | 1e-10 | 35/42 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.4 | 2e-08 | 36/42 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.62×** | +6.4 | 2e-08 | 28/42 (Hs 766T, SW 900, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.44×** | +6.2 | 7e-08 | 29/42 (SW48, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +6.0 | 1e-07 | 36/42 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.59×** | +5.9 | 3e-07 | 26/43 (SW 900, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.55×** | +5.8 | 4e-07 | 24/42 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.55×** | +5.8 | 4e-07 | 27/42 (Hs 766T, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.33×** | +5.3 | 7e-06 | 26/42 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.48×** | +5.2 | 1e-05 | 29/42 (C32, A-172, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 3e-05 | 32/42 (NCI-H1573, NCI-H1792, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 9e-05 | 22/42 (Hs 766T, SW 900, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.43×** | +4.7 | 9e-05 | 23/42 (Hs 766T, SW 900, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +4.7 | 9e-05 | 26/42 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dexamethasone (drug)]] 5 µM |  | **1.42×** | +4.6 | 1e-04 | 22/42 (Hs 766T, SW 900, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.46×** | +4.6 | 1e-04 | 23/41 (Hs 766T, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11758.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -10.0 | 9e-21 | 28/37 (SHP-77, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.480×** | -9.7 | 1e-19 | 37/42 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.619×** | -8.9 | 1e-16 | 30/43 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -6.4 | 2e-08 | 29/39 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.397×** | -6.4 | 2e-08 | 38/42 (NCI-H460, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.608×** | -6.3 | 3e-08 | 30/42 (A498, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.623×** | -6.2 | 4e-08 | 29/43 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **0.460×** | -5.4 | 6e-06 | 29/42 (NCI-H460, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.521×** | -4.5 | 4e-04 | 28/42 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.720×** | -4.2 | 0.002 | 26/44 (HEC-1-A, A498, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.568×** | -3.9 | 0.005 | 24/42 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.580×** | -3.8 | 0.008 | 24/42 (NCI-H460, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.760×** | -3.6 | 0.013 | 23/42 (CFPAC-1, HT-29, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.834× | -3.4 | 0.030 | 16/42 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.700×** | -3.4 | 0.030 | 22/42 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.770×** | -3.3 | 0.033 | 22/41 (LS 180, LoVo, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.782×** | -3.2 | 0.040 | 18/42 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -3.2 | 0.051 | 15/42 (HEC-1-A, A498, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.790×** | -3.1 | 0.057 | 18/42 (LOX-IMVI, HT-29, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.794×** | -3.0 | 0.065 | 16/43 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.46 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11758. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 220 | 17 (2 ⚠) | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.40× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 88.5 | 18 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 4.02× (z +11.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.476× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW 900 (line)]] | alt | 166 | 17 | 1 (1 ⚠) | [[Budesonide (drug)]] 0.05 µM 3.77× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -9.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 349 | 16 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 3.26× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 266 | 8 (4 ⚠) | 7 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.68× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -21.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-733 (drug)]] 5 µM 0.221× (z -9.4) |
| [[SHP-77 (line)]] | alt | 534 | 0 | 12 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -28.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.386× (z -13.1) |
| [[A549 (line)]] | wt | 124 | 10 | 0 | [[Betamethasone dipropionate (drug)]] 0.5 µM 3.33× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 294 | 4 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +12.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 9.22× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -16.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 431 | 1 (1 ⚠) | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -20.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HEC-1-A (line)]] | alt | 256 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -18.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 99.5 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +14.2) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.32× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -10.0) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 200 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +18.9) ⚠ cell-cycle shift, explains ~45% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -14.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 196 | 3 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.30× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.507× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 363 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +20.9) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +10.5) | — |
| [[C32 (line)]] | wt | 178 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +17.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 7.84× (z +8.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 120 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 8.32× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.276× (z -10.5) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 197 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 81.4 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +10.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LS 180 (line)]] | wt | 127 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 162 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.59× (z +10.4) | — |
| [[H4 (line)]] | wt | 67.1 | 1 | 0 | [[Triamcinolone (drug)]] 5 µM 3.33× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 214 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +11.9) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[J82 (line)]] | alt | 161 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 148 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.432× (z -9.3) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 265 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +11.6) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[RPMI-7951 (line)]] | alt | 74.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.0) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 153 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 12.7× (z +10.6) | — |
| [[A-427 (line)]] | wt | 70.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 290 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 60.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 220 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11758), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT1F]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[MT1E]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[MT1M]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[CEBPB]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[KLF9]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[DUSP1]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[PNRC1]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[IRX3]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[MT2A]] | +0.62 | +0.51 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[MT1X]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[TSC22D3]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZFP36L1]] | +0.59 | +0.58 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MACROH2A1]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[KLC2]] | -0.49 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[STX16]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[BMS1P20]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ZCCHC4]] | -0.47 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[MFN2]] | -0.46 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[SELENOI]] | -0.46 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[ANXA10]] | -0.46 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[DHRS11]] | -0.46 | -0.37 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNIP]] | B | TXNIP activity raises IRS2's level | lines that do not express TXNIP (11) vs lines expressing it (39) | 2.27× lower at baseline in the lines without TXNIP | 0.015 | ⚠ within organs, on part of the lines; also absent: FAM3B, CADPS2, PLAC4; maybe low, not absent |
| [[PDK4]] | B | PDK4 activity raises IRS2's level | lines that do not express PDK4 (25) vs lines expressing it (25) | 1.62× lower at baseline in the lines without PDK4 | 0.058 | ⚠ within organs, on part of the lines; also absent: TNS4, HPGD, IL20RA |
| [[SNAI2]] | B | SNAI2 activity raises IRS2's level | lines that do not express SNAI2 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without SNAI2 | 0.067 | ⚠ within organs, on part of the lines; also absent: GNG2, LBH, PLAT |
| [[NR3C1]] | B | NR3C1 activity raises IRS2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[MFGE8]] | B | MFGE8 activity lowers IRS2's level | lines that do not express MFGE8 (7) vs lines expressing it (43) | 2.12× higher at baseline in the lines without MFGE8 | 0.090 | ⚠ within organs, on part of the lines; also absent: P3H1, HAPLN3, FAM171B |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM227A]] | B | IRS2 activity lowers FAM227A's level | lines that do not express IRS2 (6) vs lines expressing it (44) | 1.56× higher at baseline in the lines without IRS2 | 0.088 | ⚠ within organs, on part of the lines; also absent: MAP3K5 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.6, 13.5); signed map (14.7, 30.4). **Vector** length 153, 52.6% of its response variance represented; |z| ≥ 3 in 1,596 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.63 to 5); *metallothionein* (control, mean cos +0.63 to 5); *Response to metal ions* (reactome, mean cos +0.63 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +6.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +8.0 | +6.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +7.4 | +5.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +7.3 | +5.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +7.2 | +4.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.1 | -9.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.2 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.1 | -4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.9 | -3.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.3 | -5.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | insulin receptor substrate 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:109,752,695-109,786,583 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Insulin receptor substrate family |
| Hallmark sets | GLYCOLYSIS, HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 37 pathways, smallest: IRS activation; Erythropoietin activates Phospholipase C gamma (PLCG); Erythropoietin activates STAT5 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4H2](https://www.uniprot.org/uniprotkb/Q9Y4H2) (Insulin receptor substrate 2):

> Signaling adapter protein that participates in the signal transduction from two prominent receptor tyrosine kinases, insulin receptor/INSR and insulin-like growth factor I receptor/IGF1R. Plays therefore an important role in development, growth, glucose homeostasis as well as lipid metabolism. Upon phosphorylation by the insulin receptor, functions as a signaling scaffold that propagates insulin action through binding to SH2 domain-containing proteins including the p85 regulatory subunit of …

**Summary**, from NCBI Gene [8660](https://www.ncbi.nlm.nih.gov/gene/8660):

> This gene encodes the insulin receptor substrate 2, a cytoplasmic signaling molecule that mediates effects of insulin, insulin-like growth factor 1, and other cytokines by acting as a molecular adaptor between diverse receptor tyrosine kinases and downstream effectors. The product of this gene is phosphorylated by the insulin receptor tyrosine kinase upon receptor stimulation, as well as by an interleukin 4 receptor-associated kinase in response to IL4 treatment. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6126](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6126) · Entrez [8660](https://www.ncbi.nlm.nih.gov/gene/8660) · UniProt [Q9Y4H2](https://www.uniprot.org/uniprotkb/Q9Y4H2) · Ensembl [ENSG00000185950](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185950)

## Data

Gene col 11758: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11758); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11758, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11758]; `tensor/DDL_lfc|DDL_z.npy` [11758]; `embed/gene_vectors.npy` [11758]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11758 or target_col == 11758). Every well: [[IRS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
