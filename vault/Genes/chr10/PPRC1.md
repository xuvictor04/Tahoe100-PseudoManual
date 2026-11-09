---
symbol: "PPRC1"
type: "gene"
col: 7320
ensembl_id: "ENSG00000148840"
name: "PPARG related coactivator 1"
location: "10q24.32"
module: 5
arm: "+"
pooled_cpm: 38.69
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 25
n_dd_up_clean: 22
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PPRC1

*PPARG related coactivator 1* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.65× (z +16.2, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.419× (z -13.9, q 2e-41, down in 27 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 0.583× (z -9.0, q 3e-17, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP2]] (+0.80, fdr 7e-06), [[PUS1]] (+0.80, fdr 7e-06), [[UTP14A]] (+0.75, fdr 7e-06); moves opposite to [[SARAF]] (-0.62, fdr 7e-06), [[CCDC28A]] (-0.60, fdr 7e-06), [[USP33]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CHSY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.65×** | +16.2 | 0e+00 | 46/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.68×** | +15.8 | 0e+00 | 42/48 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.96×** | +15.8 | 0e+00 | 36/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +12.4 | 3e-33 | 42/46 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.07×** | +12.1 | 1e-31 | 36/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.94×** | +11.0 | 3e-26 | 42/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.93×** | +10.9 | 7e-26 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.41×** | +10.7 | 8e-25 | 43/48 (PANC-1, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.39×** | +10.6 | 1e-24 | 39/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.87×** | +10.4 | 1e-23 | 38/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +8.6 | 3e-16 | 40/47 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.03×** | +8.3 | 5e-15 | 42/48 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +6.5 | 4e-09 | 31/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.80×** | +5.1 | 1e-05 | 26/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.9 | 3e-05 | 22/43 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.71×** | +4.7 | 9e-05 | 19/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.71×** | +4.7 | 1e-04 | 18/47 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.70×** | +4.6 | 1e-04 | 23/48 (HEC-1-A, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.002 | 17/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.005 | 15/48 (Hs 766T, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7320.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.419×** | -13.9 | 2e-41 | 27/39 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.515×** | -11.1 | 6e-26 | 34/46 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.676×** | -9.2 | 7e-18 | 37/48 (LoVo, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.583×** | -9.0 | 3e-17 | 37/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.612×** | -8.2 | 4e-14 | 30/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -7.9 | 3e-13 | 32/47 (A498, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.636×** | -7.5 | 4e-12 | 30/48 (A498, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.651×** | -7.1 | 7e-11 | 32/48 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.639×** | -6.9 | 3e-10 | 28/44 (NCI-H2030, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -5.6 | 1e-06 | 25/48 (A498, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.714×** | -5.6 | 1e-06 | 30/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.742×** | -4.8 | 9e-05 | 24/47 (SW480, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.738×** | -4.7 | 1e-04 | 17/48 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.756×** | -4.7 | 1e-04 | 21/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.748×** | -4.7 | 1e-04 | 21/48 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.592×** | -4.6 | 2e-04 | 22/48 (A498, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.761×** | -4.5 | 2e-04 | 24/48 (KATO III, J82, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.770×** | -4.4 | 4e-04 | 20/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.813×** | -4.1 | 0.001 | 21/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.783×** | -4.1 | 0.001 | 18/48 (MIA PaCa-2, SW480, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 59.1 | 11 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +15.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -16.4) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 58.9 | 3 (1 ⚠) | 7 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.15× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.198× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -13.5) |
| [[AsPC-1 (line)]] | alt | 48.5 | 5 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.69× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.243× (z -11.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 41.6 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +10.4) | [[Adagrasib (drug)]] 0.05 µM 0.602× (z -14.1) ⚠ position not correctable · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.90× (z +12.2) | — |
| [[SW480 (line)]] | alt | 42.0 | 5 (1 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 3.55× (z +11.7) | [[Cobimetinib (drug)]] 5 µM 0.370× (z -8.8) |
| [[A-172 (line)]] | wt | 35.2 | 2 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.05× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0479× (z -25.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 36.3 | 5 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.15× (z +11.2) | — |
| [[CFPAC-1 (line)]] | alt | 17.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +13.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.68× (z +10.7) | — |
| [[SNU-423 (line)]] | alt | 27.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.33× (z +17.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.48× (z +12.1) | — |
| [[A-427 (line)]] | wt | 50.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -9.4) |
| [[HT-29 (line)]] | alt | 27.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.17× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -10.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 35.9 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.8) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.191× (z -14.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 24.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +14.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.49× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 46.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -17.2) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 74.2 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 33.2 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 6.09× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -8.5) |
| [[A549 (line)]] | wt | 39.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +9.6) ⚠ cell-cycle shift, explains ~27% of this change | [[Dinaciclib (drug)]] 5 µM 0.115× (z -15.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 59.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -12.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 41.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -13.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 39.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -10.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 27.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.267× (z -9.2) |
| [[LoVo (line)]] | wt | 48.6 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.361× (z -13.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.357× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 37.3 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.89× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 33.4 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.202× (z -9.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 52.1 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.312× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.61× (z +8.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 30.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +9.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HS-578T (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -9.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -12.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.321× (z -10.0) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SHP-77 (line)]] | alt | 38.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.244× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP2]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 536 |
| [[PUS1]] | +0.80 | +0.84 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[UTP14A]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[WDR4]] | +0.75 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[NOP16]] | +0.73 | +0.74 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[BYSL]] | +0.73 | +0.72 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 442 |
| [[MRTO4]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[GRWD1]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 410 |
| [[GTPBP4]] | +0.71 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[TASOR2]] | +0.71 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[NOP56]] | +0.70 | +0.65 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[DDX31]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SARAF]] | -0.62 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[CCDC28A]] | -0.60 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[USP33]] | -0.60 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[MXD1]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[VAMP7]] | -0.59 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[KCTD9]] | -0.59 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SNX3]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[CYB5R4]] | -0.58 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[TMEM59]] | -0.58 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[MKRN1]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.56 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[RNF11]] | -0.56 | -0.47 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHSY3]] | B | CHSY3 activity lowers PPRC1's level | lines that do not express CHSY3 (23) vs lines expressing it (27) | 1.27× higher at baseline in the lines without CHSY3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ADAMTS1, ZNF365, GBP5 |
| [[MAP2K1]] | B | MAP2K1 activity raises PPRC1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[FTH1]] | C | FTH1 activity lowers PPRC1's level | lines that do not express FTH1 (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without FTH1 | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000284716, ZFP36, DDR1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.2, -36.4); signed map (-1.2, -46.3). **Vector** length 120, 40.1% of its response variance represented; |z| ≥ 3 in 1,439 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.57 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.57 to 19); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.62 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.5 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +15.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +12.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +4.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.4 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -4.3 | -5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -11.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -3.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | PPARG related coactivator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,132,994-102,150,333 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRC, KIAA0595, MGC74642 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | MYC_TARGETS_V2 |
| Reactome | 3 pathways, smallest: Transcriptional activation of mitochondrial biogenesis; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VV67](https://www.uniprot.org/uniprotkb/Q5VV67) (Peroxisome proliferator-activated receptor gamma coactivator-related protein 1):

> Acts as a coactivator during transcriptional activation of nuclear genes related to mitochondrial biogenesis and cell growth. Involved in the transcription coactivation of CREB and NRF1 target genes.

**Summary**, from NCBI Gene [23082](https://www.ncbi.nlm.nih.gov/gene/23082):

> The protein encoded by this gene is similar to PPAR-gamma coactivator 1 (PPARGC1/PGC-1), a protein that can activate mitochondrial biogenesis in part through a direct interaction with nuclear respiratory factor 1 (NRF1). This protein has been shown to interact with NRF1. It is thought to be a functional relative of PPAR-gamma coactivator 1 that activates mitochondrial biogenesis through NRF1 in response to proliferative signals. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:30025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30025) · Entrez [23082](https://www.ncbi.nlm.nih.gov/gene/23082) · UniProt [Q5VV67](https://www.uniprot.org/uniprotkb/Q5VV67) · Ensembl [ENSG00000148840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148840)

## Data

Gene col 7320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7320); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7320]; `tensor/DDL_lfc|DDL_z.npy` [7320]; `embed/gene_vectors.npy` [7320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7320 or target_col == 7320). Every well: [[PPRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
