---
symbol: "CDCA2"
type: "gene"
col: 11563
ensembl_id: "ENSG00000184661"
name: "cell division cycle associated 2"
location: "8p21.2"
module: 22
arm: "+"
pooled_cpm: 68.73
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CDCA2

*cell division cycle associated 2* — 8p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.74× (z +16.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (16 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.600× (z -11.9, q 1e-29, down in 39 of 48 measured lines) ⚠ cell-cycle shift, explains ~78% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.684× (z -6.2, q 4e-08, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCA8]] (+0.88, fdr 7e-06), [[PTTG1]] (+0.87, fdr 7e-06), [[KIF2C]] (+0.87, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11563.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.74×** | +16.6 | 0e+00 | 46/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.41×** | +14.5 | 4e-45 | 46/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +14.0 | 5e-42 | 43/48 (KATO III, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +12.0 | 9e-31 | 32/48 (KATO III, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.97×** | +11.1 | 9e-27 | 40/48 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.61×** | +11.1 | 2e-26 | 33/48 (RKO, Panc 03.27, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | **1.80×** | +9.7 | 3e-20 | 38/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +7.2 | 5e-11 | 32/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.47×** | +6.3 | 2e-08 | 34/48 (KATO III, H4, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.47×** | +6.3 | 2e-08 | 31/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.41×** | +5.6 | 1e-06 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.27×** | +5.6 | 1e-06 | 32/48 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.39×** | +5.5 | 2e-06 | 27/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +5.2 | 7e-06 | 25/48 (RKO, HEC-1-A, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.33×** | +4.7 | 1e-04 | 21/47 (AsPC-1, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.6 | 2e-04 | 22/48 (A549, A498, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.64×** | +4.3 | 6e-04 | 19/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.7 | 0.005 | 15/48 (RKO, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.010 | 19/48 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.015 | 14/48 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11563.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.600×** | -11.9 | 1e-29 | 39/48 (A-427, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.577×** | -8.9 | 1e-16 | 39/48 (A-427, LS 180, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.619×** | -7.9 | 6e-13 | 30/46 (A549, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.627×** | -7.4 | 3e-11 | 33/43 (A549, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.641×** | -6.9 | 6e-10 | 34/48 (A-172, SNU-423, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.661×** | -6.8 | 1e-09 | 31/48 (HOP62, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.684×** | -6.2 | 4e-08 | 27/48 (A-427, SHP-77, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.691×** | -6.1 | 1e-07 | 32/48 (SNU-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.716×** | -5.5 | 3e-06 | 30/48 (SNU-1, C-33 A, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.746×** | -4.8 | 9e-05 | 21/48 (C32, LOX-IMVI, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.754×** | -4.4 | 5e-04 | 24/48 (SW 1271, NCI-H2347, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.761×** | -4.3 | 8e-04 | 22/48 (CHP-212, NCI-H1573, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.783×** | -4.0 | 0.003 | 23/48 (LS 180, SNU-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.844× | -3.9 | 0.003 | 18/48 (RKO, A-427, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.797×** | -3.4 | 0.022 | 20/48 (SNU-1, CHP-212, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.814×** | -3.4 | 0.024 | 15/48 (A498, HOP62, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.871× | -3.2 | 0.038 | 14/48 (Hs 766T, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.82 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11563. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 49.0 | 8 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 8.12× (z +15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 5.76× (z +13.2) | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 97.9 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +15.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.19× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -14.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 36.3 | 5 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.62× (z +11.3) | [[Amsacrine (drug)]] 5 µM 0.435× (z -8.7) |
| [[RKO (line)]] | wt | 60.5 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +19.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.94× (z +12.4) | — |
| [[A-427 (line)]] | wt | 113 | 0 | 5 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.233× (z -16.7) ⚠ cell-cycle shift, explains ~78% of this change |
| [[A498 (line)]] | wt | 90.2 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.39× (z +9.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -8.8) |
| [[A549 (line)]] | wt | 219 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.1) |
| [[HS-578T (line)]] | alt | 69.9 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +14.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.58× (z +11.9) | — |
| [[J82 (line)]] | alt | 39.9 | 5 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.34× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 36.3 | 3 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.86× (z +10.1) | [[Selinexor (drug)]] 5 µM 0.179× (z -15.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[NCI-H460 (line)]] | wt | 48.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.26× (z +10.3) | [[Selinexor (drug)]] 5 µM 0.366× (z -12.3) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SNU-423 (line)]] | alt | 129 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -13.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 107 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -14.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 61.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.21× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 36.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.4) | [[Selinexor (drug)]] 5 µM 0.490× (z -8.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SW480 (line)]] | alt | 75.3 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.39× (z +12.5) | — |
| [[A-172 (line)]] | wt | 107 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.378× (z -13.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[LS 180 (line)]] | wt | 42.9 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.225× (z -12.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[NCI-H23 (line)]] | alt | 71.1 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.93× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 45.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +15.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 25.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +13.9) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.489× (z -9.2) ⚠ cell-cycle shift, explains ~78% of this change |
| [[AsPC-1 (line)]] | alt | 54.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +9.6) | — |
| [[C-33 A (line)]] | alt | 83.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -13.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 82.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 78.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 73.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -11.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -11.8) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 25.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 31.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 44.9 | 0 | 1 | — | [[Sinomenine (drug)]] 0.05 µM 0.0680× (z -8.5) |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0966× (z -9.6) |
| [[HCT15 (line)]] | alt | 92.6 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.155× (z -11.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 84.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 73.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.443× (z -8.6) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SNU-1 (line)]] | wt | 80.0 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.161× (z -9.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0871× (z -8.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 69.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11563), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCA8]] | +0.88 | +0.87 / +0.87 | both halves | 7e-06 | STRING 889 |
| [[PTTG1]] | +0.87 | +0.85 / +0.84 | both halves | 7e-06 | STRING 555 |
| [[KIF2C]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 | STRING 885 |
| [[SGO2]] | +0.86 | +0.87 / +0.86 | both halves | 7e-06 | STRING 578 |
| [[CDK1]] | +0.86 | +0.85 / +0.87 | both halves | 7e-06 | STRING 832 |
| [[DLGAP5]] | +0.86 | +0.87 / +0.83 | both halves | 7e-06 | STRING 898 |
| [[CDCA3]] | +0.85 | +0.79 / +0.83 | both halves | 7e-06 | STRING 910 |
| [[KIF18A]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | same gene group; STRING 658 |
| [[CKAP2]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 | STRING 618 |
| [[TOP2A]] | +0.84 | +0.84 / +0.84 | both halves | 7e-06 | STRING 789 |
| [[CCNF]] | +0.84 | +0.82 / +0.82 | both halves | 7e-06 | STRING 476 |
| [[DEPDC1B]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | STRING 723 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.849). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-36.1, -57.3); signed map (-51.0, -41.3). **Vector** length 148, 51.9% of its response variance represented; |z| ≥ 3 in 1,516 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *G2/M checkpoint* (hallmark, mean cos +0.68 to 60); *DREAM G2/M down* (control, mean cos +0.77 to 28); *Mitotic Prometaphase* (reactome, mean cos +0.64 to 48).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.4 | +14.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.8 | +7.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +4.7 | +4.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.5 | +3.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | +4.5 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.4 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.5 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -9.5 | -11.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | -9.3 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | -8.4 | -6.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -8.0 | -8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.8 | -6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.3 | -4.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.2 | -2.7 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -3.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cell division cycle associated 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.2 — chr8:25,459,199-25,507,911 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Repo-Man, PPP1R81 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q69YH5](https://www.uniprot.org/uniprotkb/Q69YH5) (Cell division cycle-associated protein 2):

> Regulator of chromosome structure during mitosis required for condensin-depleted chromosomes to retain their compact architecture through anaphase. Acts by mediating the recruitment of phosphatase PP1-gamma subunit (PPP1CC) to chromatin at anaphase and into the following interphase. At anaphase onset, its association with chromatin targets a pool of PPP1CC to dephosphorylate substrates.

**Summary**, from NCBI Gene [157313](https://www.ncbi.nlm.nih.gov/gene/157313):

> This gene encodes a targeting subunit of the cell-cycle associated protein, protein phosphatase 1, with a role in targeting this protein to chromatin during anaphase. These two proteins comprise a phosphatase complex that is involved in nuclear envelope reformation and regulation of the DNA damage response. The encoded protein may also play a role in cancer progression. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2015]

**Accessions** — [HGNC:14623](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14623) · Entrez [157313](https://www.ncbi.nlm.nih.gov/gene/157313) · UniProt [Q69YH5](https://www.uniprot.org/uniprotkb/Q69YH5) · Ensembl [ENSG00000184661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184661)

## Data

Gene col 11563: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11563); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11563, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11563]; `tensor/DDL_lfc|DDL_z.npy` [11563]; `embed/gene_vectors.npy` [11563]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11563 or target_col == 11563). Every well: [[CDCA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
