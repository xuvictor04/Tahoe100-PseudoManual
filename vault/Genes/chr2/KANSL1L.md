---
symbol: "KANSL1L"
type: "gene"
col: 6879
ensembl_id: "ENSG00000144445"
name: "KAT8 regulatory NSL complex subunit 1 like"
location: "2q34"
module: 23
arm: "+"
pooled_cpm: 84.34
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 16
n_dd_up_clean: 30
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# KANSL1L

*KAT8 regulatory NSL complex subunit 1 like* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.29× (z +23.3, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.540× (z -12.2, q 1e-31, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.599× (z -10.2, q 5e-22, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAI4]] (+0.73, fdr 4e-05), [[PPP1R12A-AS2]] (+0.73, fdr 4e-05), [[N4BP2L1]] (+0.73, fdr 1e-05); moves opposite to [[SDHAF3]] (-0.68, fdr 5e-05), [[WASF3]] (-0.68, fdr 2e-04), [[ELP1]] (-0.67, fdr 8e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 53 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.29×** | +23.3 | 0e+00 | 47/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +10.1 | 2e-21 | 35/48 (NCI-H1792, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +9.1 | 1e-17 | 29/49 (AsPC-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +9.1 | 1e-17 | 36/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.3 | 3e-11 | 34/48 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.39×** | +6.6 | 5e-09 | 27/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +6.4 | 1e-08 | 36/47 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +6.3 | 2e-08 | 32/50 (HEC-1-A, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.80×** | +5.9 | 2e-07 | 37/50 (LoVo, J82, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +5.9 | 3e-07 | 28/48 (HEC-1-A, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.27×** | +5.6 | 1e-06 | 29/48 (LoVo, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +5.5 | 2e-06 | 29/48 (HOP62, SW1417, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +5.3 | 5e-06 | 26/49 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.30×** | +5.3 | 6e-06 | 27/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.31×** | +5.2 | 7e-06 | 29/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.28×** | +5.0 | 2e-05 | 25/49 (HEC-1-A, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +5.0 | 2e-05 | 29/48 (C32, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.540×** | -12.2 | 1e-31 | 44/48 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.586×** | -10.6 | 7e-24 | 42/48 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.599×** | -10.2 | 5e-22 | 45/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.633×** | -9.1 | 2e-17 | 41/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.633×** | -8.4 | 5e-15 | 35/44 (LS 180, NCI-H661, …) | all doses, flat | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.452×** | -7.9 | 2e-13 | 31/37 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.685×** | -7.5 | 5e-12 | 36/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **0.703×** | -6.7 | 1e-09 | 28/42 (NCI-H23, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **0.718×** | -6.6 | 3e-09 | 30/49 (NCI-H1573, SK-MEL-2, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.585×** | -5.4 | 5e-06 | 30/48 (COLO 205, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.785×** | -4.8 | 8e-05 | 23/48 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.643×** | -4.4 | 5e-04 | 25/49 (LS 180, hTERT-HPNE, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.700×** | -3.6 | 0.015 | 16/48 (SW480, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Naproxen (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.020 | 18/48 (SW 900, J82, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.887× | -3.4 | 0.028 | 6/48 (SNU-423, LS 180, …) | all doses, stronger at high dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | 0.851× | -3.2 | 0.047 | 13/48 (RKO, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.733×** | -3.1 | 0.062 | 13/49 (SNU-423, NCI-H1573, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 0.896× | -3.1 | 0.063 | 5/49 (LS 180, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.850× | -3.0 | 0.079 | 13/47 (CHP-212, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.861× | -3.0 | 0.079 | 11/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.812×** | -3.0 | 0.079 | 16/48 (HT-29, NCI-H460, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.6 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +32.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.514× (z -8.8) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 78.5 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +16.0) | [[Belinostat (drug)]] 0.5 µM 0.381× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 107 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +13.0) | [[Panobinostat (drug)]] 5 µM 0.357× (z -12.0) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.415× (z -10.2) |
| [[SNU-423 (line)]] | alt | 128 | 1 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[C32 (line)]] | wt | 87.3 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +17.2) | [[Lonafarnib (drug)]] 5 µM 0.0597× (z -11.8) ⚠ toxic |
| [[SW480 (line)]] | alt | 88.0 | 1 | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.9) | [[Belinostat (drug)]] 5 µM 0.482× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1573 (line)]] | alt | 129 | 0 | 5 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.282× (z -14.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 76.7 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.388× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[J82 (line)]] | alt | 96.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +23.0) | [[Belinostat (drug)]] 5 µM 0.440× (z -10.0) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.486× (z -8.8) |
| [[PANC-1 (line)]] | alt | 72.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +17.7) | [[Belinostat (drug)]] 0.5 µM 0.476× (z -10.0) |
| [[RPMI-7951 (line)]] | alt | 142 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +12.1) | [[Belinostat (drug)]] 5 µM 0.408× (z -9.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SK-MEL-2 (line)]] | alt | 117 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[A498 (line)]] | wt | 77.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +17.8) | — |
| [[hTERT-HPNE (line)]] | wt | 98.0 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.7) | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[LoVo (line)]] | wt | 53.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +21.7) | — |
| [[LS 180 (line)]] | wt | 90.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.163× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 69.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +14.0) | — |
| [[NCI-H23 (line)]] | alt | 84.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.185× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[SW1417 (line)]] | alt | 72.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.4) | — |
| [[A-172 (line)]] | wt | 84.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +9.6) | [[Belinostat (drug)]] 0.5 µM 0.405× (z -9.1) |
| [[AN3 CA (line)]] | alt | 75.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[AsPC-1 (line)]] | alt | 56.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +19.9) | — |
| [[H4 (line)]] | wt | 85.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.201× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[HEC-1-A (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 60.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +16.2) | — |
| [[HS-578T (line)]] | alt | 74.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +11.1) | [[Panobinostat (drug)]] 0.5 µM 0.387× (z -8.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 74.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +13.3) | [[Belinostat (drug)]] 0.5 µM 0.405× (z -8.5) |
| [[SHP-77 (line)]] | alt | 67.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change |
| [[COLO 205 (line)]] | alt | 102 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 62.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.1) | — |
| [[HepG2_C3A (line)]] | wt | 115 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +13.0) | — |
| [[NCI-H2030 (line)]] | alt | 178 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 38.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +16.9) | — |
| [[NCI-H661 (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0763× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[Panc 03.27 (line)]] | alt | 48.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.9) | — |
| [[RKO (line)]] | wt | 39.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +14.7) | — |
| [[SNU-1 (line)]] | wt | 62.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.0) | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.182× (z -8.7) |
| [[SW 900 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.372× (z -9.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 95.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAI4]] | +0.73 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[N4BP2L1]] | +0.73 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.73 | +0.72 / +0.28 | both halves | 3e-04 |  |
| [[ANKHD1-EIF4EBP3]] | +0.71 | +0.70 / +0.46 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.71 | +0.66 / +0.26 | both halves | 4e-04 |  |
| [[LINC01004]] | +0.70 | +0.63 / +0.36 | both halves | 9e-05 |  |
| [[KLRK1-AS1]] | +0.70 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[FBXL19-AS1]] | +0.70 | +0.65 / +0.31 | both halves | 2e-04 |  |
| [[GIPC2]] | +0.69 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[BAZ2B]] | +0.69 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[MED13]] | +0.69 | +0.54 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAF3]] | -0.68 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[WASF3]] | -0.68 | -0.62 / -0.32 | both halves | 2e-04 |  |
| [[ELP1]] | -0.67 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[GTPBP3]] | -0.66 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[MINK1]] | -0.64 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[ATG16L1]] | -0.64 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[POMGNT2]] | -0.63 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ACTR5]] | -0.63 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[TRIM35]] | -0.62 | -0.62 / -0.27 | both halves | 3e-04 |  |
| [[TAF5L]] | -0.62 | -0.66 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KANSL1L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (8.3, 13.2); signed map (24.5, -5.2). **Vector** length 143, 47.1% of its response variance represented; |z| ≥ 3 in 1,470 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +23.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +10.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.7 | +5.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +6.4 | +6.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +6.0 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +5.4 | +5.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -10.9 | -12.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -9.9 | -10.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -9.4 | -10.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -8.7 | -9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -7.7 | -7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.3 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.7 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.9 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | KAT8 regulatory NSL complex subunit 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:210,021,421-210,171,409 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23861, FLJ32349, MSL1v2, KIAA1267L; previously C2orf67 |
| Matched by | ensembl_id |

UniProt [A0AUZ9](https://www.uniprot.org/uniprotkb/A0AUZ9) carries no function annotation.

**Summary**, from NCBI Gene [151050](https://www.ncbi.nlm.nih.gov/gene/151050):

> Predicted to enable histone acetyltransferase binding activity. Predicted to be part of NSL complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26310](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26310) · Entrez [151050](https://www.ncbi.nlm.nih.gov/gene/151050) · UniProt [A0AUZ9](https://www.uniprot.org/uniprotkb/A0AUZ9) · Ensembl [ENSG00000144445](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144445)

## Data

Gene col 6879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6879); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6879]; `tensor/DDL_lfc|DDL_z.npy` [6879]; `embed/gene_vectors.npy` [6879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6879 or target_col == 6879). Every well: [[KANSL1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANSL1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
