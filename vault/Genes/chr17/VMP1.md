---
symbol: "VMP1"
type: "gene"
col: 715
ensembl_id: "ENSG00000062716"
name: "vacuole membrane protein 1"
location: "17q23.1"
module: 109
arm: "+"
pooled_cpm: 552.19
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# VMP1

*vacuole membrane protein 1* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.36× (z +6.7, q 1e-08, up in 34 of 48 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.33× (z +6.1, q 3e-07, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.562× (z -12.0, q 3e-30, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.698× (z -11.0, q 1e-25, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GP6-AS1]] (+0.59, fdr 8e-06), [[POMP]] (+0.58, fdr 1e-05), [[TMEM41B]] (+0.57, fdr 1e-05); moves opposite to [[NFYB]] (-0.64, fdr 7e-06), [[FOXJ2]] (-0.60, fdr 1e-05), [[CEPT1]] (-0.55, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FMN1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.36×** | +6.7 | 1e-08 | 34/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +6.1 | 3e-07 | 36/48 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | 1.20× | +5.5 | 7e-06 | 22/48 (HS-578T, HEC-1-A, …) | all doses, flat | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.3 | 1e-05 | 29/48 (HEC-1-A, SNU-1, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.23×** | +4.5 | 6e-04 | 28/49 (MIA PaCa-2, HS-578T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +4.4 | 7e-04 | 26/48 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +4.4 | 7e-04 | 25/48 (SK-MEL-2, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.16× | +4.4 | 7e-04 | 20/48 (SNU-1, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.20×** | +4.0 | 0.004 | 22/49 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.27×** | +3.9 | 0.005 | 29/48 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.19× | +3.7 | 0.012 | 22/48 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.4 | 0.034 | 0/50 | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | 1.16× | +3.2 | 0.052 | 15/48 (SNU-1, Hs 766T, …) | all doses, flat |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.23×** | +3.2 | 0.066 | 22/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.090 | 26/49 (RKO, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 715.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -12.0 | 3e-30 | 41/44 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.698×** | -11.0 | 1e-25 | 37/49 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.641×** | -9.6 | 2e-19 | 43/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.733×** | -9.5 | 4e-19 | 32/48 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **0.757×** | -8.5 | 2e-15 | 41/48 (MIA PaCa-2, AsPC-1, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **0.685×** | -8.2 | 3e-14 | 45/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.700×** | -7.4 | 1e-11 | 34/48 (PANC-1, H4, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.727×** | -6.9 | 4e-10 | 34/48 (NCI-H1792, C-33 A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.740×** | -6.5 | 5e-09 | 34/48 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.743×** | -6.4 | 8e-09 | 32/49 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.756×** | -5.8 | 3e-07 | 33/47 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.605×** | -5.7 | 7e-07 | 40/47 (RKO, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.809×** | -4.6 | 2e-04 | 29/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.812×** | -4.5 | 3e-04 | 31/48 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.825×** | -4.2 | 0.001 | 22/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -4.1 | 0.001 | 25/48 (A-427, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.831×** | -4.0 | 0.002 | 24/48 (A-427, A549, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.835× | -3.9 | 0.003 | 23/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.844× | -3.7 | 0.008 | 22/48 (PANC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.847× | -3.4 | 0.016 | 18/48 (RKO, SW48, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.884× | -3.2 | 0.033 | 13/48 (NCI-H23, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.864× | -3.2 | 0.037 | 12/48 (HCT15, PANC-1, …) | two highest doses |  |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 0.905× | -3.1 | 0.051 | 0/48 | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 1,095 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -15.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.578× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 406 | 8 (7 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.31× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.71× (z +9.1) | [[Ponatinib (drug)]] 5 µM 0.595× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 502 | 7 (7 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +16.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Radotinib (drug)]] 5 µM 0.665× (z -9.5) |
| [[PANC-1 (line)]] | alt | 649 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -16.3) |
| [[KATO III (line)]] | alt | 644 | 2 (1 ⚠) | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.93× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -13.7) ⚠ cell-cycle shift, explains ~57% of this change |
| [[LS 180 (line)]] | wt | 538 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -15.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.627× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 687 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.426× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 641 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -12.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.453× (z -11.5) |
| [[SNU-1 (line)]] | wt | 407 | 6 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.19× (z +13.3) | — |
| [[C-33 A (line)]] | alt | 784 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -12.9) |
| [[H4 (line)]] | wt | 578 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.391× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.498× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 490 | 4 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.13× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.502× (z -12.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 429 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.35× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 2,024 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -12.1) |
| [[hTERT-HPNE (line)]] | wt | 555 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 492 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.545× (z -12.1) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -9.9) |
| [[A498 (line)]] | wt | 422 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.572× (z -8.8) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.591× (z -8.6) |
| [[A549 (line)]] | wt | 703 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -21.1) |
| [[CFPAC-1 (line)]] | alt | 625 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.552× (z -9.3) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 900 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 650 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -13.1) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 464 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 1.72× (z +10.8) ⚠ cell-cycle shift, explains ~60% of this change | [[Harringtonine (drug)]] 0.5 µM 0.476× (z -10.4) |
| [[HT-29 (line)]] | alt | 598 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.372× (z -14.2) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 591 | 0 | 3 (1 ⚠) | — | [[Radotinib (drug)]] 5 µM 0.623× (z -10.0) |
| [[SW480 (line)]] | alt | 590 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -12.2) |
| [[LoVo (line)]] | wt | 398 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.94× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.498× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 382 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.80× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.544× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 538 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 428 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.526× (z -9.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -8.9) |
| [[SHP-77 (line)]] | alt | 345 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.598× (z -10.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SNU-423 (line)]] | alt | 623 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -10.4) |
| [[SW1417 (line)]] | alt | 631 | 1 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 1.85× (z +9.7) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.663× (z -9.2) |
| [[SW48 (line)]] | wt | 598 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.4) |
| [[COLO 205 (line)]] | alt | 869 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.477× (z -8.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 345 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.6) ⚠ cell-cycle shift, explains ~57% of this change | — |
| [[NCI-H1573 (line)]] | alt | 495 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.451× (z -11.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 604 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.489× (z -9.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 491 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.513× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 320 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 301 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 441 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 422 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 511 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 374 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 276 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 579 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 540 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 360 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 519 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GP6-AS1]] | +0.59 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[POMP]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TMEM41B]] | +0.57 | +0.60 / +0.51 | both halves | 1e-05 | STRING 867 |
| [[RALY]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 | same gene group |
| [[SYAP1]] | +0.55 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[DCUN1D3]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[ZSWIM6]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[ITGB1]] | +0.53 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[DUSP5]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[NEAT1]] | +0.52 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[CYTH1]] | +0.52 | +0.60 / +0.37 | both halves | 7e-05 |  |
| [[BIN3]] | +0.52 | +0.55 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFYB]] | -0.64 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[FOXJ2]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[CEPT1]] | -0.55 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[DIS3L]] | -0.54 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[COQ9]] | -0.53 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[RNF146]] | -0.53 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[DICER1]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 | same gene group |
| [[ACBD5]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[WHAMMP3]] | -0.51 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[ZNF592]] | -0.50 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[PHC3]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[CFAP418]] | -0.49 | -0.47 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMN1]] | B | FMN1 activity raises VMP1's level | lines that do not express FMN1 (17) vs lines expressing it (33) | 1.09× lower at baseline in the lines without FMN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000278266, LINC02405, ENSG00000286016; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.468). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.3, -24.2); signed map (2.8, 26.9). **Vector** length 148, 53.3% of its response variance represented; |z| ≥ 3 in 1,508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.0 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.3 | +6.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +6.1 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.9 | +6.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +5.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +1.9 |
|  | [[Auranofin (drug)]] 0.5 µM |  | +2.7 | +1.4 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -10.5 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -10.1 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -9.4 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -11.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -8.0 | -8.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -5.7 | -4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -4.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -4.7 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | vacuole membrane protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:59,707,192-59,842,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EPG3, TANGO5; previously TMEM49 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GC9](https://www.uniprot.org/uniprotkb/Q96GC9) (Vacuole membrane protein 1):

> Phospholipid scramblase involved in lipid homeostasis and membrane dynamics processes. Has phospholipid scramblase activity toward cholesterol and phosphatidylserine, as well as phosphatidylethanolamine and phosphatidylcholine. Required for autophagosome formation: participates in early stages of autophagosome biogenesis at the endoplasmic reticulum (ER) membrane by reequilibrating the leaflets of the ER as lipids are extracted by ATG2 (ATG2A or ATG2B) to mediate autophagosome assembly. …

**Summary**, from NCBI Gene [81671](https://www.ncbi.nlm.nih.gov/gene/81671):

> This gene encodes a transmembrane protein that plays a key regulatory role in the process of autophagy. The ectopic overexpression of the encoded protein in cultured cells triggers autophagy even under nutrient-rich conditions. This gene is overexpressed in pancreatitis affected acinar cells where the encoded protein mediates sequestration and degradation of potentially deleterious activated zymogen granules in a process termed, zymophagy. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:29559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29559) · Entrez [81671](https://www.ncbi.nlm.nih.gov/gene/81671) · UniProt [Q96GC9](https://www.uniprot.org/uniprotkb/Q96GC9) · Ensembl [ENSG00000062716](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062716)

## Data

Gene col 715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 715); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 715]; `tensor/DDL_lfc|DDL_z.npy` [715]; `embed/gene_vectors.npy` [715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 715 or target_col == 715). Every well: [[VMP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VMP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
