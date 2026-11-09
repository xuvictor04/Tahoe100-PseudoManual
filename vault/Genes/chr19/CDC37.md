---
symbol: "CDC37"
type: "gene"
col: 2597
ensembl_id: "ENSG00000105401"
name: "cell division cycle 37, HSP90 cochaperone"
location: "19p13.2"
module: 78
arm: "+"
pooled_cpm: 82.64
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# CDC37

*cell division cycle 37, HSP90 cochaperone* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.83× (z +17.9, q 0e+00, up in 48 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +13.0, q 1e-36, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.826× (z -3.7, q 0.073, down in 22 of 48 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Anethole trithione (drug)]] 0.5 µM: 0.762× (z -3.7, q 0.073, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0990×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0697×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSN]] (+0.64, fdr 3e-05), [[TPM3]] (+0.61, fdr 5e-05), [[ACTN1]] (+0.58, fdr 6e-05); moves opposite to [[FBXO9]] (-0.57, fdr 3e-05), [[C15orf61]] (-0.57, fdr 1e-05, ⚠ C15orf61 in the vector space only through flagged drug-doses), [[PUM2]] (-0.57, fdr 3e-05), [[RSBN1L]] (-0.56, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 20 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.83×** | +17.9 | 0e+00 | 48/49 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.43×** | +15.8 | 0e+00 | 44/44 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **3.13×** | +14.1 | 1e-42 | 45/45 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +13.0 | 1e-36 | 46/49 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.65×** | +13.0 | 2e-36 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.45×** | +11.9 | 9e-31 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.34×** | +11.3 | 6e-28 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.21×** | +10.5 | 4e-24 | 46/48 (SW480, BT-474, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.52×** | +7.9 | 3e-13 | 40/48 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.73×** | +7.3 | 2e-11 | 44/48 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.71×** | +7.2 | 4e-11 | 43/48 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +6.2 | 2e-08 | 44/48 (NCI-H23, A498, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.62×** | +6.2 | 3e-08 | 35/50 (MIA PaCa-2, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.59×** | +6.0 | 1e-07 | 36/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +5.8 | 2e-07 | 37/48 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +4.9 | 3e-05 | 35/48 (NCI-H2030, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.5 | 2e-04 | 28/48 (A-172, BT-474, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.85×** | +4.3 | 5e-04 | 38/48 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.011 | 28/48 (J82, A-427, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.64×** | +3.4 | 0.013 | 27/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.048 | 25/48 (SW 900, HT-29, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.53×** | +2.9 | 0.055 | 20/48 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2597.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0990×); [[Neratinib (maleate) (drug)]] 0.5 µM in 1 line (SW 1088 0.0697×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.826×** | -3.7 | 0.073 | 22/48 (A498, KATO III, …) | rises with dose | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.762×** | -3.7 | 0.073 | 36/48 (KATO III, CFPAC-1, …) | rises with dose | position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | **0.825×** | -3.5 | 0.084 | 26/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 0.753× | -3.3 | 0.16 | 24/50 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.795× | -3.1 | 0.18 | 24/49 (NCI-H2122, SW1417, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.782× | -3.1 | 0.18 | 22/48 (C-33 A, LoVo, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 0.790× | -3.1 | 0.18 | 26/47 (C32, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.2 | 15 (13 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.56× (z +17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.28× (z +11.2) | — |
| [[A-172 (line)]] | wt | 69.5 | 12 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +14.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 93.7 | 10 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 50.0 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.65× (z +14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +11.3) | — |
| [[SW480 (line)]] | alt | 63.3 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.52× (z +18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.36× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 104 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +13.3) | — |
| [[LoVo (line)]] | wt | 73.9 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.53× (z +17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.50× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 52.4 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.87× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 73.2 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.76× (z +17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +11.8) | — |
| [[LS 180 (line)]] | wt | 80.7 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[Panc 03.27 (line)]] | alt | 83.9 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 103 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +9.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[SNU-423 (line)]] | alt | 68.6 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +12.0) | — |
| [[SW 900 (line)]] | alt | 78.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.8) | — |
| [[A549 (line)]] | wt | 58.3 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 80.2 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.67× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +11.3) | — |
| [[C32 (line)]] | wt | 56.9 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 83.2 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[KATO III (line)]] | alt | 57.4 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H23 (line)]] | alt | 120 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.72× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 100 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[A498 (line)]] | wt | 147 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[H4 (line)]] | wt | 86.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.1) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[Hs 766T (line)]] | wt | 89.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[J82 (line)]] | alt | 90.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 90.8 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.9) | — |
| [[A-427 (line)]] | wt | 121 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[CFPAC-1 (line)]] | alt | 57.2 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.8) | — |
| [[HCT15 (line)]] | alt | 149 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[HT-29 (line)]] | alt | 51.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[LOX-IMVI (line)]] | wt | 61.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[NCI-H1573 (line)]] | alt | 53.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.0) | — |
| [[RKO (line)]] | wt | 155 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.03× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 154 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.70× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 77.2 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 101 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.9) | — |
| [[C-33 A (line)]] | alt | 94.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[COLO 205 (line)]] | alt | 65.5 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.84× (z +10.3) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.7) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[NCI-H2030 (line)]] | alt | 98.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SNU-1 (line)]] | wt | 68.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SW 1088 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0697× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 89.3 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0990× (z -10.0) |
| [[AN3 CA (line)]] | alt | 83.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 58.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSN]] | +0.64 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[TPM3]] | +0.61 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[ACTN1]] | +0.58 | +0.39 / +0.59 | both halves | 6e-05 | pathway: RHOBTB GTPase Cycle |
| [[DBNL]] | +0.58 | +0.64 / +0.49 | both halves | 1e-05 | same gene group; pathway: Programmed Cell Death |
| [[CDC42EP2]] | +0.57 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[DNAH1]] | +0.56 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NOC2L]] | +0.56 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[BRD9]] | +0.54 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[MACF1]] | +0.54 | +0.40 / +0.51 | both halves | 4e-05 |  |
| [[KCTD5]] | +0.54 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[LRRC59]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[MYH9]] | +0.53 | +0.54 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*42 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO9]] | -0.57 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[C15orf61]] ⚠ | -0.57 | -0.57 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PUM2]] | -0.57 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[RSBN1L]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[MAP3K2]] | -0.56 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[FBXL5]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[C2orf69]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[DPM3]] | -0.55 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[HOXA10]] | -0.55 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[PHIP]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 | pathway: RHOBTB GTPase Cycle |
| [[RANGRF]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[HOXA5]] | -0.54 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[RCOR3]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA10]] | B | HOXA10 activity lowers CDC37's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 1.12× higher at baseline in the lines without HOXA10 | 0.031 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |
| [[TOP2A]] | B | TOP2A activity lowers CDC37's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.555). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.7, 10.0); signed map (-8.5, 38.9). **Vector** length 69.9, 23.4% of its response variance represented; |z| ≥ 3 in 1,147 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.1 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +2.8 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.5 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +3.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +1.8 | -0.3 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | +1.7 | -1.1 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +1.4 | -0.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | -5.7 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.3 | -2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.4 | +3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~95% of this change | -3.1 | +3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | +0.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.3 | -1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle 37, HSP90 cochaperone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,391,133-10,420,121 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P50CDC37 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Reactome | 34 pathways, smallest: Drug resistance in ERBB2 KD mutants; Drug resistance in ERBB2 TMD/JMD mutants; Drug-mediated inhibition of ERBB2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16543](https://www.uniprot.org/uniprotkb/Q16543) (Hsp90 co-chaperone Cdc37):

> Co-chaperone that binds to numerous kinases and promotes their interaction with the Hsp90 complex, resulting in stabilization and promotion of their activity. Inhibits HSP90AA1 ATPase activity.

**Summary**, from NCBI Gene [11140](https://www.ncbi.nlm.nih.gov/gene/11140):

> The protein encoded by this gene is highly similar to Cdc 37, a cell division cycle control protein of Sacchromyces cerevisiae. This protein is a molecular chaperone with specific function in cell signal transduction. It has been shown to form complex with Hsp90 and a variety of protein kinases including CDK4, CDK6, SRC, RAF-1, MOK, as well as eIF2 alpha kinases. It is thought to play a critical role in directing Hsp90 to its target kinases. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1735](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1735) · Entrez [11140](https://www.ncbi.nlm.nih.gov/gene/11140) · UniProt [Q16543](https://www.uniprot.org/uniprotkb/Q16543) · Ensembl [ENSG00000105401](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105401)

## Data

Gene col 2597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2597); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2597]; `tensor/DDL_lfc|DDL_z.npy` [2597]; `embed/gene_vectors.npy` [2597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2597 or target_col == 2597). Every well: [[CDC37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDC37.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
