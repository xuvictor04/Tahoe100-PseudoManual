---
symbol: "LIMA1"
type: "gene"
col: 565
ensembl_id: "ENSG00000050405"
name: "LIM domain and actin binding 1"
location: "12q13.12"
module: 224
arm: "+"
pooled_cpm: 200.62
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/224"]
generated_by: "tahoemap"
---

# LIMA1

*LIM domain and actin binding 1* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.31× (z +22.4, q 0e+00, up in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.12× (z +14.2, q 2e-43, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.687× (z -10.0, q 7e-21, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUFT1]] (+0.69, fdr 7e-06), [[CCDC148]] (+0.62, fdr 7e-06), [[NUAK2]] (+0.62, fdr 1e-05); moves opposite to [[TMEM11-DT]] (-0.61, fdr 1e-05), [[THAP4]] (-0.61, fdr 1e-05), [[PSMB5]] (-0.56, fdr 2e-05).
> It is in [[Module 224]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SPTLC3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.31×** | +22.4 | 0e+00 | 38/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.20×** | +14.3 | 3e-44 | 32/42 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +14.2 | 2e-43 | 41/46 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.28×** | +14.2 | 2e-43 | 36/47 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.12×** | +13.6 | 3e-40 | 42/46 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +13.2 | 1e-37 | 37/46 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +12.7 | 8e-35 | 34/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +12.0 | 1e-31 | 37/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +9.6 | 4e-20 | 40/46 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.67×** | +8.9 | 5e-17 | 36/46 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +8.1 | 3e-14 | 38/47 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.47×** | +7.3 | 2e-11 | 36/46 (NCI-H460, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.45×** | +6.4 | 6e-09 | 23/43 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.80×** | +5.8 | 3e-07 | 25/47 (MIA PaCa-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +4.3 | 7e-04 | 23/45 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.002 | 21/46 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.012 | 21/47 (SK-MEL-2, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.1 | 0.056 | 19/45 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | 1.17× | +3.0 | 0.070 | 12/46 (NCI-H2030, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.070 | 19/45 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Flutamide (drug)]] 5 µM |  | 1.17× | +2.9 | 0.098 | 8/46 (KATO III, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -10.0 | 7e-21 | 32/47 (COLO 205, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.632×** | -8.7 | 9e-16 | 32/46 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.615×** | -8.7 | 9e-16 | 38/46 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.588×** | -5.2 | 2e-05 | 33/47 (A498, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -4.6 | 5e-04 | 27/46 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -4.4 | 0.001 | 23/46 (HT-29, Panc 03.27, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.795×** | -4.3 | 0.001 | 21/46 (Hs 766T, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.645×** | -4.3 | 0.001 | 23/43 (SW48, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.812×** | -3.9 | 0.005 | 22/46 (Hs 766T, H4, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.818×** | -3.8 | 0.008 | 22/46 (Hs 766T, AsPC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.872× | -3.7 | 0.013 | 16/46 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.834× | -3.3 | 0.044 | 23/46 (Hs 766T, NCI-H23, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 0.885× | -3.3 | 0.047 | 14/46 (A498, H4, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.728×** | -3.1 | 0.068 | 17/46 (LS 180, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 0.845× | -3.1 | 0.084 | 15/45 (SNU-423, LoVo, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 267 | 0 | 22 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -24.4) |
| [[A-172 (line)]] | wt | 140 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.86× (z +26.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.78× (z +19.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 136 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +25.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.59× (z +19.6) | — |
| [[H4 (line)]] | wt | 183 | 4 (3 ⚠) | 7 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +14.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.14× (z +8.5) | [[Dexamethasone (drug)]] 0.5 µM 0.255× (z -10.2) |
| [[SW1417 (line)]] | alt | 243 | 8 (4 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +21.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.54× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -20.0) |
| [[A-427 (line)]] | wt | 102 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +23.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.04× (z +18.5) | — |
| [[A498 (line)]] | wt | 268 | 5 (3 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.8) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.88× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.3) |
| [[AsPC-1 (line)]] | alt | 234 | 4 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.43× (z +9.9) | [[Auranofin (drug)]] 5 µM 0.387× (z -10.5) |
| [[BT-474 (line)]] | alt | 195 | 7 (6 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.23× (z +8.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.367× (z -10.8) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 315 | 5 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +17.7) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.22× (z +11.0) | [[Auranofin (drug)]] 5 µM 0.405× (z -12.5) |
| [[LoVo (line)]] | wt | 437 | 2 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +16.6) ⚠ cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 164 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +15.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.87× (z +14.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.533× (z -8.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 117 | 7 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.15× (z +13.6) | [[Bortezomib (drug)]] 5 µM 0.0442× (z -15.5) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 158 | 7 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +18.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.27× (z +16.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 94.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.4) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.15× (z +13.3) | — |
| [[NCI-H1573 (line)]] | alt | 76.1 | 7 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.74× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 56.9 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 560 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -25.1) |
| [[HOP62 (line)]] | alt | 92.6 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +22.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.68× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 520 | 2 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.6) ⚠ cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -21.6) |
| [[hTERT-HPNE (line)]] | wt | 121 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +18.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.73× (z +13.2) | — |
| [[J82 (line)]] | alt | 335 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +15.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H23 (line)]] | alt | 173 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.284× (z -17.6) |
| [[SNU-423 (line)]] | alt | 179 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +21.9) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.72× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 206 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +14.1) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 156 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.70× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 110 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.05× (z +9.7) | — |
| [[C32 (line)]] | wt | 163 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +19.6) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.14× (z +15.9) | — |
| [[KATO III (line)]] | alt | 459 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -14.7) |
| [[LOX-IMVI (line)]] | wt | 517 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -16.2) |
| [[C-33 A (line)]] | alt | 95.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[CFPAC-1 (line)]] | alt | 314 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.58× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 187 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 335 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +10.2) ⚠ cell-cycle shift, explains ~36% of this change | [[Dinaciclib (drug)]] 5 µM 0.487× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 167 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -8.6) |
| [[RKO (line)]] | wt | 149 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 149 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +13.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.48× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 95.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +9.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[HepG2_C3A (line)]] | wt | 84.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 68.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 118 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.1) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 44.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 164 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 152 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUFT1]] | +0.69 | +0.64 / +0.68 | both halves | 7e-06 | same gene group |
| [[CCDC148]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[NUAK2]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PICALM]] | +0.61 | +0.27 / +0.65 | both halves | 3e-04 |  |
| [[LMCD1]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |
| [[SYTL2]] | +0.60 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[ENPP1]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CTNND1]] | +0.60 | +0.45 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_APICAL_JUNCTION; STRING 820 |
| [[CD2AP]] | +0.59 | +0.45 / +0.67 | both halves | 3e-05 |  |
| [[TSPAN2]] | +0.58 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ATP8B1]] | +0.58 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[EXT1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11-DT]] | -0.61 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[THAP4]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[PSMB5]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[C8orf76]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[METTL3]] | -0.54 | -0.56 / -0.39 | both halves | 5e-05 |  |
| [[METTL4]] | -0.53 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[ZNF718]] | -0.53 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[KCTD15]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[RPUSD4]] | -0.53 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PPP1R26-AS1]] | -0.52 | -0.40 / -0.51 | both halves | 4e-05 |  |
| [[C1orf216]] | -0.52 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[GARS1-DT]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPTLC3]] | B | SPTLC3 activity raises LIMA1's level | lines that do not express SPTLC3 (16) vs lines expressing it (34) | 1.79× lower at baseline in the lines without SPTLC3 | 0.033 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[FGD6]] | B | FGD6 activity raises LIMA1's level | lines that do not express FGD6 (12) vs lines expressing it (38) | 1.61× lower at baseline in the lines without FGD6 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000290957, PKP2, EPHA2-AS1; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises LIMA1's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without GBP2 | 0.091 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 224]] — hypoxia; 9 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.8, 9.0); signed map (48.9, 7.0). **Vector** length 146, 49.7% of its response variance represented; |z| ≥ 3 in 1,646 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.1 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.9 | +22.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +7.8 | +13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +12.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.6 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +4.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -8.8 | -8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -10.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -8.0 | -4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -7.8 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.6 | -4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.6 | -3.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.2 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | LIM domain and actin binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:50,175,788-50,283,520 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EPLIN |
| Gene groups (HGNC) | LIM domain containing; MicroRNA protein coding host genes |
| Hallmark sets | APICAL_JUNCTION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHB6](https://www.uniprot.org/uniprotkb/Q9UHB6) (LIM domain and actin-binding protein 1):

> Actin-binding protein involved in actin cytoskeleton regulation and dynamics. Increases the number and size of actin stress fibers and inhibits membrane ruffling. Inhibits actin filament depolymerization. Bundles actin filaments, delays filament nucleation and reduces formation of branched filaments. Acts as a negative regulator of primary cilium formation. Plays a role in cholesterol homeostasis. Influences plasma cholesterol levels through regulation of intestinal cholesterol absorption. May …

**Summary**, from NCBI Gene [51474](https://www.ncbi.nlm.nih.gov/gene/51474):

> This gene encodes a cytoskeleton-associated protein that inhibits actin filament depolymerization and cross-links filaments in bundles. It is downregulated in some cancer cell lines. Alternatively spliced transcript variants encoding different isoforms have been described for this gene, and expression of some of the variants maybe independently regulated. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:24636](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24636) · Entrez [51474](https://www.ncbi.nlm.nih.gov/gene/51474) · UniProt [Q9UHB6](https://www.uniprot.org/uniprotkb/Q9UHB6) · Ensembl [ENSG00000050405](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050405)

## Data

Gene col 565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 565); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 565]; `tensor/DDL_lfc|DDL_z.npy` [565]; `embed/gene_vectors.npy` [565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 565 or target_col == 565). Every well: [[LIMA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIMA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
