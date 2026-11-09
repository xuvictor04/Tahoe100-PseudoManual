---
symbol: "CNTRL"
type: "gene"
col: 4060
ensembl_id: "ENSG00000119397"
name: "centriolin"
location: "9q33.2"
module: 22
arm: "+"
pooled_cpm: 65.88
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 22
n_dd_up_clean: 10
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CNTRL

*centriolin* — 9q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.97× (z +24.2, q 0e+00, up in 41 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.78× (z +14.6, q 1e-45, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.472× (z -19.0, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPF]] (+0.82, fdr 7e-06), [[NDC80]] (+0.80, fdr 7e-06), [[DEPDC1]] (+0.78, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.97×** | +24.2 | 0e+00 | 41/48 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +14.6 | 1e-45 | 37/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.76×** | +13.7 | 2e-40 | 40/48 (RKO, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +10.6 | 3e-24 | 33/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +9.6 | 1e-19 | 37/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +8.7 | 3e-16 | 27/48 (NCI-H1792, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.41×** | +8.7 | 3e-16 | 30/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +8.0 | 6e-14 | 27/48 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.6 | 2e-12 | 27/48 (J82, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +7.5 | 4e-12 | 25/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.63×** | +6.5 | 5e-09 | 27/47 (NCI-H23, A498, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.23×** | +5.2 | 1e-05 | 19/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +5.2 | 1e-05 | 23/48 (LoVo, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~81% of this change | **1.22×** | +5.1 | 2e-05 | 22/48 (HT-29, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Docetaxel (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 1.19× | +4.5 | 3e-04 | 13/48 (HT-29, KATO III, …) | all doses, flat |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.11× | +3.7 | 0.006 | 10/49 (NCI-H2030, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 1.11× | +3.6 | 0.009 | 12/48 (HT-29, KATO III, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.3 | 0.024 | 13/48 (J82, LOX-IMVI, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.024 | 12/47 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.031 | 5/48 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 1.13× | +2.9 | 0.086 | 9/48 (SW 900, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.472×** | -19.0 | 0e+00 | 45/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.679×** | -9.7 | 5e-20 | 40/48 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.503×** | -9.1 | 2e-17 | 35/49 (PANC-1, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.705×** | -8.8 | 2e-16 | 33/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.696×** | -8.6 | 7e-16 | 32/48 (HEC-1-A, SW480, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.808×** | -7.6 | 3e-12 | 25/48 (PANC-1, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -7.2 | 5e-11 | 25/45 (SHP-77, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.580×** | -7.2 | 5e-11 | 29/48 (NCI-H460, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.583×** | -7.1 | 6e-11 | 31/48 (HEC-1-A, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -6.4 | 1e-08 | 25/48 (HEC-1-A, SW480, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.628×** | -6.1 | 4e-08 | 27/48 (A-427, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.657×** | -5.5 | 1e-06 | 22/48 (Hs 766T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.663×** | -5.4 | 2e-06 | 20/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.663×** | -5.4 | 2e-06 | 20/48 (Hs 766T, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.764×** | -4.8 | 5e-05 | 18/48 (Hs 766T, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.709×** | -4.5 | 2e-04 | 20/48 (LS 180, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.803×** | -3.9 | 0.002 | 12/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.746×** | -3.9 | 0.003 | 16/47 (PANC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.861× | -3.8 | 0.004 | 10/48 (SW1417, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.818×** | -3.6 | 0.007 | 11/48 (C-33 A, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 47.1 | 9 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +14.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.9) | — |
| [[SW480 (line)]] | alt | 101 | 0 | 8 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.328× (z -15.4) |
| [[A-427 (line)]] | wt | 86.1 | 3 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.74× (z +11.6) | [[PH-797804 (drug)]] 5 µM 0.153× (z -11.2) |
| [[LoVo (line)]] | wt | 36.9 | 5 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.391× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -8.6) |
| [[RKO (line)]] | wt | 164 | 3 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +20.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.13× (z +14.6) | [[Auranofin (drug)]] 5 µM 0.372× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 76.5 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.299× (z -15.4) |
| [[PANC-1 (line)]] | alt | 103 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.556× (z -13.0) ⚠ cell-cycle shift, explains ~74% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.283× (z -10.3) |
| [[A498 (line)]] | wt | 46.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.491× (z -11.6) ⚠ cell-cycle shift, explains ~74% of this change |
| [[J82 (line)]] | alt | 113 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +22.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.7) | — |
| [[SHP-77 (line)]] | alt | 149 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.1) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.466× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 73.3 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.7) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.265× (z -12.6) |
| [[C-33 A (line)]] | alt | 116 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +9.5) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 5 µM 0.119× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 63.8 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +23.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.320× (z -12.1) |
| [[Hs 766T (line)]] | wt | 87.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +18.3) ⚠ cell-cycle shift, explains ~35% of this change | [[Selinexor (drug)]] 5 µM 0.510× (z -9.0) ⚠ cell-cycle shift, explains ~74% of this change |
| [[LOX-IMVI (line)]] | wt | 63.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +17.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 75.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 40.6 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +14.7) | — |
| [[NCI-H23 (line)]] | alt | 96.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.487× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 33.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +21.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.86× (z +12.5) | — |
| [[CFPAC-1 (line)]] | alt | 28.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +16.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +9.8) | — |
| [[KATO III (line)]] | alt | 61.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +11.7) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.391× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 43.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +26.4) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 54.4 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.451× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 59.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +15.1) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.392× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 61.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change | [[Auranofin (drug)]] 5 µM 0.341× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.378× (z -8.7) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.4) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[C32 (line)]] | wt | 59.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +10.2) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[HT-29 (line)]] | alt | 38.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.7) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SNU-1 (line)]] | wt | 88.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 48.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.20× (z +22.3) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SW 1271 (line)]] | alt | 143 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.154× (z -9.7) |
| [[SW 900 (line)]] | alt | 41.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[SW1417 (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[A549 (line)]] | wt | 81.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 130 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 67.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPF]] | +0.82 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[NDC80]] | +0.80 | +0.74 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[DEPDC1]] | +0.78 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[CENPE]] | +0.78 | +0.80 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[ASPM]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[MKI67]] | +0.77 | +0.67 / +0.78 | both halves | 7e-06 |  |
| [[SGO1]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 | pathway: G2/M Transition |
| [[TOP2A]] | +0.76 | +0.68 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[KIF18A]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[SMC4]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[CDK1]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[KNL1]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | pathway: Mitotic Prometaphase |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-38.8, -56.2); signed map (-50.2, -44.6). **Vector** length 125, 36.9% of its response variance represented; |z| ≥ 3 in 1,322 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.60 to 60); *DREAM G2/M down* (control, mean cos +0.69 to 28); *E2F targets* (hallmark, mean cos +0.58 to 46).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.7 | +24.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +6.6 | +13.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +14.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.5 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +7.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.1 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.4 | -19.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -9.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -6.7 | -8.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -6.5 | -8.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | -6.2 | -7.6 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -7.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.6 | -6.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.4 | -5.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -7.2 |

## What is on record

|  |  |
|---|---|
| Name | centriolin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.2 — chr9:121,074,660-121,177,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CEP1, CEP110 |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 22 pathways, smallest: Signaling by cytosolic FGFR1 fusion mutants; FGFR1 mutant receptor activation; Signaling by FGFR1 in disease |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7A1](https://www.uniprot.org/uniprotkb/Q7Z7A1) (Centriolin):

> Involved in cell cycle progression and cytokinesis. During the late steps of cytokinesis, anchors exocyst and SNARE complexes at the midbody, thereby allowing secretory vesicle-mediated abscission.

**Summary**, from NCBI Gene [11064](https://www.ncbi.nlm.nih.gov/gene/11064):

> This gene encodes a centrosomal protein required for the centrosome to function as a microtubule organizing center. The gene product is also associated with centrosome maturation. One version of stem cell myeloproliferative disorder is the result of a reciprocal translocation between chromosomes 8 and 9, with the breakpoint associated with fibroblast growth factor receptor 1 and centrosomal protein 1. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1858) · Entrez [11064](https://www.ncbi.nlm.nih.gov/gene/11064) · UniProt [Q7Z7A1](https://www.uniprot.org/uniprotkb/Q7Z7A1) · Ensembl [ENSG00000119397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119397)

## Data

Gene col 4060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4060); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4060]; `tensor/DDL_lfc|DDL_z.npy` [4060]; `embed/gene_vectors.npy` [4060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4060 or target_col == 4060). Every well: [[CNTRL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTRL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
