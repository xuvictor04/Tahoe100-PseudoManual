---
symbol: "PUM3"
type: "gene"
col: 1287
ensembl_id: "ENSG00000080608"
name: "pumilio RNA binding family member 3"
location: "9p24.2"
module: 5
arm: "+"
pooled_cpm: 114.36
n_lines_expressing: 49
n_dd_up: 37
n_dd_down: 2
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PUM3

*pumilio RNA binding family member 3* — 9p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (14 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.11× (z +17.1, q 0e+00, up in 47 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.03× (z +16.3, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.772× (z -6.1, q 8e-07, down in 27 of 48 measured lines) ⚠ cell-cycle shift, explains ~20% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.854× (z -5.3, q 4e-05, down in 18 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A498 0.519×, SNU-1 0.417×, RKO 0.538×, SK-MEL-2 0.553×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.370×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.649×; ⚠ position not correctable); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.495×); [[Binimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.533×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYBBP1A]] (+0.82, fdr 7e-06), [[HEATR1]] (+0.81, fdr 7e-06), [[POLR1A]] (+0.81, fdr 7e-06).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMCC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1287.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.11×** | +17.1 | 0e+00 | 47/47 (NCI-H460, SW1417, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +16.3 | 0e+00 | 39/47 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.84×** | +11.6 | 1e-28 | 35/43 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.63×** | +11.2 | 3e-27 | 34/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.61×** | +10.9 | 1e-25 | 38/47 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.63×** | +10.4 | 2e-23 | 34/44 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +9.6 | 4e-20 | 38/47 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +9.4 | 5e-19 | 37/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +8.8 | 6e-17 | 34/47 (MIA PaCa-2, SK-MEL-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.44×** | +8.4 | 3e-15 | 30/47 (NCI-H1792, A-172, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.98×** | +8.1 | 3e-14 | 39/47 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.93×** | +7.7 | 4e-13 | 41/47 (NCI-H460, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +7.7 | 7e-13 | 32/47 (LOX-IMVI, LoVo, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.37×** | +7.3 | 1e-11 | 26/47 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +7.3 | 1e-11 | 33/47 (MIA PaCa-2, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.78×** | +6.8 | 3e-10 | 37/47 (SW1417, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +6.8 | 4e-10 | 34/47 (NCI-H1792, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.77×** | +6.7 | 5e-10 | 35/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +6.7 | 7e-10 | 32/47 (J82, HOP62, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.72×** | +6.4 | 4e-09 | 33/47 (NCI-H460, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +5.2 | 4e-06 | 30/46 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 8e-06 | 28/47 (NCI-H460, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1287.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (A498 0.519×, SNU-1 0.417×, RKO 0.538×, SK-MEL-2 0.553×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.370×; ⚠ cell-cycle shift, explains ~0% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.649×; ⚠ position not correctable); [[Binimetinib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.495×); [[Binimetinib (drug)]] 5 µM in 1 line (MIA PaCa-2 0.533×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.772×** | -6.1 | 8e-07 | 27/48 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.854× | -5.3 | 4e-05 | 18/47 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.848× | -4.5 | 0.001 | 16/47 (MIA PaCa-2, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.049 | 19/46 (MIA PaCa-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 0.862× | -3.5 | 0.049 | 10/47 (KATO III, HCT15, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.837× | -3.4 | 0.056 | 13/46 (A549, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.868× | -3.2 | 0.094 | 15/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.848× | -3.2 | 0.10 | 13/47 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.884× | -3.2 | 0.10 | 17/47 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.878× | -3.1 | 0.12 | 15/48 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.879× | -3.0 | 0.12 | 7/47 (J82, NCI-H460, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.867× | -3.0 | 0.13 | 14/47 (SK-MEL-2, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1287. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 74.0 | 11 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.02× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 100 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.97× (z +15.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 143 | 4 (1 ⚠) | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.66× (z +11.5) | [[Adagrasib (drug)]] 0.05 µM 0.649× (z -17.3) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.495× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 53.7 | 7 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +10.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 107 | 6 (4 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.13× (z +13.6) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.42× (z +10.6) | — |
| [[LoVo (line)]] | wt | 107 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +10.9) | — |
| [[SK-MEL-2 (line)]] | alt | 224 | 4 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.22× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.553× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 79.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.88× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 78.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +14.7) | — |
| [[J82 (line)]] | alt | 153 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.94× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 179 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.72× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 68.4 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +11.9) ⚠ cell-cycle shift, explains ~18% of this change | — |
| [[Panc 03.27 (line)]] | alt | 93.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.70× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 70.8 | 4 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.44× (z +11.7) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.09× (z +10.8) | — |
| [[A-172 (line)]] | wt | 82.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.28× (z +10.8) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A498 (line)]] | wt | 245 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 122 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.41× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 33.9 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.79× (z +14.7) | — |
| [[RPMI-7951 (line)]] | alt | 141 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.94× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 185 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +11.8) | — |
| [[SNU-423 (line)]] | alt | 69.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.99× (z +10.9) | — |
| [[SW480 (line)]] | alt | 184 | 2 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.28× (z +10.7) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.16× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 44.7 | 2 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.36× (z +9.8) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.33× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 63.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.83× (z +10.9) | — |
| [[H4 (line)]] | wt | 81.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.30× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.16× (z +9.1) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[RKO (line)]] | wt | 222 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.02× (z +8.9) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -11.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 136 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 122 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 121 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +8.7) | — |
| [[KATO III (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.13× (z +8.7) ⚠ unreliable plate only | — |
| [[NCI-H23 (line)]] | alt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 204 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -13.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 125 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.64× (z +12.9) ⚠ unreliable plate only | — |
| [[SW48 (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 153 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 70.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1287), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBBP1A]] | +0.82 | +0.80 / +0.84 | both halves | 7e-06 | STRING 851 |
| [[HEATR1]] | +0.81 | +0.74 / +0.83 | both halves | 7e-06 | same gene group; STRING 837 |
| [[POLR1A]] | +0.81 | +0.78 / +0.82 | both halves | 7e-06 | STRING 862 |
| [[MDN1]] | +0.81 | +0.73 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[WDR4]] | +0.81 | +0.83 / +0.78 | both halves | 7e-06 | STRING 427 |
| [[GNL3L]] | +0.80 | +0.76 / +0.87 | both halves | 7e-06 | STRING 876 |
| [[PNO1]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | STRING 665 |
| [[PUS1]] | +0.78 | +0.83 / +0.73 | both halves | 7e-06 |  |
| [[URB1]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | STRING 688 |
| [[MAK16]] | +0.76 | +0.75 / +0.76 | both halves | 7e-06 | STRING 966 |
| [[DKC1]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 | STRING 928 |
| [[NOL10]] | +0.76 | +0.69 / +0.82 | both halves | 7e-06 | STRING 850 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMCC2]] | B | TMCC2 activity raises PUM3's level | lines that do not express TMCC2 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without TMCC2 | 0.050 | ⚠ within organs, on part of the lines; also absent: AXDND1, SUCLG2-DT, SACS; maybe low, not absent |
| [[ENTPD1-AS1]] | C | ENTPD1-AS1 activity raises PUM3's level | lines that do not express ENTPD1-AS1 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without ENTPD1-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LRRIQ3, WDR35, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.777). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.2, -35.8); signed map (-3.6, -47.9). **Vector** length 137, 48.2% of its response variance represented; |z| ≥ 3 in 1,494 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.63 to 13); *rRNA processing* (reactome, mean cos +0.59 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.60 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.9 | +17.1 |
|  | [[EX229 (drug)]] 5 µM |  | +6.9 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +6.7 | +7.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.7 | +6.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.9 | +6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.3 | +6.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.2 | -5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.7 | -6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | -1.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | +4.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.9 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.2 | -3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | pumilio RNA binding family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.2 — chr9:2,720,469-2,844,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XTP5, PEN, PUF6, hPUF-A, HA-8, Puf-A; previously KIAA0020 |
| Gene groups (HGNC) | Minor histocompatibility antigens; Pumilio homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15397](https://www.uniprot.org/uniprotkb/Q15397) (Pumilio homolog 3):

> Inhibits the poly(ADP-ribosyl)ation activity of PARP1 and the degradation of PARP1 by CASP3 following genotoxic stress. Binds to double-stranded RNA or DNA without sequence specificity. Involved in development of the eye and of primordial germ cells (By similarity).

**Summary**, from NCBI Gene [9933](https://www.ncbi.nlm.nih.gov/gene/9933):

> Enables RNA binding activity. Predicted to be involved in regulation of translation. Located in chromosome; endoplasmic reticulum; and nuclear lumen. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29676) · Entrez [9933](https://www.ncbi.nlm.nih.gov/gene/9933) · UniProt [Q15397](https://www.uniprot.org/uniprotkb/Q15397) · Ensembl [ENSG00000080608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080608)

## Data

Gene col 1287: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1287); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1287, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1287]; `tensor/DDL_lfc|DDL_z.npy` [1287]; `embed/gene_vectors.npy` [1287]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1287 or target_col == 1287). Every well: [[PUM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
