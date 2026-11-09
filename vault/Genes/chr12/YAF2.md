---
symbol: "YAF2"
type: "gene"
col: 292
ensembl_id: "ENSG00000015153"
name: "YY1 associated factor 2"
location: "12q12"
module: 2
arm: "-"
pooled_cpm: 96.75
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 8
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# YAF2

*YY1 associated factor 2* — 12q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +35.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.636× (z -12.3, q 5e-32, down in 31 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.616× (z -5.4, q 7e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATXN2]] (+0.61, fdr 1e-05), [[KDSR]] (+0.57, fdr 1e-05), [[TNRC6C]] (+0.54, fdr 1e-05); moves opposite to [[VDAC2]] (-0.57, fdr 1e-05), [[ZDHHC16]] (-0.55, fdr 1e-05), [[ATP5F1B]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 292.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +35.5 | 0e+00 | 48/48 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.60×** | +26.0 | 0e+00 | 46/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.07×** | +20.6 | 0e+00 | 41/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +18.4 | 0e+00 | 44/47 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +16.1 | 0e+00 | 41/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +12.7 | 3e-35 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.11×** | +12.7 | 3e-35 | 43/49 (SW480, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.56×** | +12.6 | 1e-34 | 37/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +8.9 | 4e-17 | 31/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.19×** | +8.8 | 8e-17 | 33/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +8.7 | 3e-16 | 29/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.22×** | +8.1 | 4e-14 | 25/49 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.19× | +4.9 | 3e-05 | 19/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.17× | +4.4 | 5e-04 | 18/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.15× | +4.0 | 0.002 | 19/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.020 | 7/49 (KATO III, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.08× | +3.0 | 0.070 | 0/49 | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +3.0 | 0.074 | 9/48 (SW48, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.11× | +2.9 | 0.081 | 15/48 (C-33 A, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 292.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -12.3 | 5e-32 | 31/44 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -9.0 | 8e-17 | 33/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.751×** | -8.1 | 1e-13 | 31/49 (SHP-77, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 0.840× | -7.0 | 5e-10 | 22/48 (AsPC-1, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.616×** | -5.4 | 7e-06 | 25/48 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.829×** | -4.9 | 9e-05 | 21/45 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.845× | -4.7 | 2e-04 | 22/48 (HT-29, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.851× | -4.6 | 4e-04 | 16/49 (AsPC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.684×** | -4.3 | 0.001 | 20/48 (SW480, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.700×** | -4.0 | 0.004 | 17/48 (SW480, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.906× | -3.8 | 0.006 | 11/48 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 0.858× | -3.8 | 0.007 | 13/50 (HOP62, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.881× | -3.7 | 0.011 | 12/49 (NCI-H23, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.878× | -3.5 | 0.017 | 9/47 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.888× | -3.5 | 0.017 | 10/48 (HOP62, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.884× | -3.5 | 0.018 | 12/49 (SW480, HOP62, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.735×** | -3.5 | 0.018 | 17/48 (SW480, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.886× | -3.4 | 0.021 | 11/48 (C32, H4, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 0.884× | -3.3 | 0.030 | 14/48 (CHP-212, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.889× | -3.1 | 0.059 | 7/48 (SW480, HOP62, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.925× | -3.0 | 0.064 | 3/49 (HOP62, SW 1271, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 292. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 10 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.79× (z +21.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.529× (z -10.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 132 | 10 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.11× (z +19.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.462× (z -12.9) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 87.0 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +20.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.443× (z -9.9) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 119 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -15.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 81.8 | 7 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.15× (z +20.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.13× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -11.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 93.1 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +28.1) | — |
| [[SHP-77 (line)]] | alt | 139 | 2 (1 ⚠) | 6 (6 ⚠) | [[Digitoxin (drug)]] 5 µM 3.02× (z +13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -18.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 95.3 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.4) | [[Selinexor (drug)]] 5 µM 0.485× (z -12.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HepG2_C3A (line)]] | wt | 143 | 4 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.268× (z -13.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 133 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +29.7) | — |
| [[BT-474 (line)]] | alt | 82.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +21.5) | — |
| [[HEC-1-A (line)]] | alt | 106 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +25.7) | [[Dinaciclib (drug)]] 5 µM 0.311× (z -16.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 66.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +18.3) | — |
| [[NCI-H23 (line)]] | alt | 121 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +23.4) | — |
| [[RKO (line)]] | wt | 167 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -14.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 112 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -14.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 99.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 86.2 | 3 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.65× (z +16.3) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -12.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 116 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -17.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 75.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.7) | — |
| [[SW 900 (line)]] | alt | 81.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.3) | — |
| [[A-172 (line)]] | wt | 67.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.6) | — |
| [[A-427 (line)]] | wt | 113 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +14.5) | — |
| [[A498 (line)]] | wt | 111 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.499× (z -8.5) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 67.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -8.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 94.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +21.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.9 | 3 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.64× (z +13.2) | — |
| [[NCI-H2347 (line)]] | alt | 61.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +24.2) | — |
| [[SNU-1 (line)]] | wt | 134 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.2) | — |
| [[AN3 CA (line)]] | alt | 182 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -9.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 81.8 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.14× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.375× (z -10.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 44.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +19.8) | — |
| [[HCT15 (line)]] | alt | 80.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 81.4 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.39× (z +10.0) | — |
| [[J82 (line)]] | alt | 103 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.546× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 79.1 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.83× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.362× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +17.2) | — |
| [[RPMI-7951 (line)]] | alt | 67.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 73.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +15.6) | — |
| [[SNU-423 (line)]] | alt | 91.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.9) | — |
| [[CHP-212 (line)]] | wt | 75.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +8.7) | — |
| [[H4 (line)]] | wt | 55.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 114 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.21× (z +10.6) | — |
| [[C-33 A (line)]] | alt | 133 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 292), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN2]] | +0.61 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KDSR]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TNRC6C]] | +0.54 | +0.54 / +0.49 | both halves | 1e-05 | pathway: Transcriptional regulation by RUNX1 |
| [[SATB2]] | +0.54 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[NR2F1]] | +0.54 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[RBX1]] | +0.53 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[PPP1R35]] ⚠ | +0.52 | +0.49 / +0.48 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TGIF2]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[FOXA2]] | +0.52 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[DNMT3A]] | +0.51 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[UBALD1]] | +0.51 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[PRPF38B]] | +0.51 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[HIVEP1]] | +0.50 | +0.50 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VDAC2]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ZDHHC16]] | -0.55 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[ATP5F1B]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[INTS11]] | -0.52 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[VAMP3]] | -0.52 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[HECTD3]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[MDH2]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[CYB5R4]] | -0.50 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[TMED2]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NSDHL]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[EDEM2]] | -0.49 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ESYT1]] | -0.49 | -0.30 / -0.55 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **-** arm (projection on the module's main direction -0.274). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (0.3, -25.9); signed map (10.6, -3.3). **Vector** length 102, 29.5% of its response variance represented; |z| ≥ 3 in 1,103 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +26.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | +5.2 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.2 | +35.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +3.6 | +4.4 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +2.3 | +0.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +2.2 | +2.1 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.0 | +2.0 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.9 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.1 | -9.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -6.0 | -7.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.1 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -5.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.4 | -3.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | YY1 associated factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q12 — chr12:42,157,104-42,238,349 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers RANBP2-type |
| Reactome | 3 pathways, smallest: Transcriptional Regulation by E2F6; RUNX1 interacts with co-factors whose precise effect on RUNX1 targets is not known; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY57](https://www.uniprot.org/uniprotkb/Q8IY57) (YY1-associated factor 2):

> Binds to MYC and inhibits MYC-mediated transactivation. Also binds to MYCN and enhances MYCN-dependent transcriptional activation. Increases calpain 2-mediated proteolysis of YY1 in vitro. Component of the E2F6.com-1 complex, a repressive complex that methylates 'Lys-9' of histone H3, suggesting that it is involved in chromatin-remodeling.

**Summary**, from NCBI Gene [10138](https://www.ncbi.nlm.nih.gov/gene/10138):

> This gene encodes a zinc finger containing protein that functions in the regulation of transcription. This protein was identified as an interacting partner of transcriptional repressor protein Yy1, and also interacts with other transcriptional regulators, including Myc and Polycomb. This protein can promote proteolysis of Yy1. Multiple alternatively spliced transcript variants have been found. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:17363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17363) · Entrez [10138](https://www.ncbi.nlm.nih.gov/gene/10138) · UniProt [Q8IY57](https://www.uniprot.org/uniprotkb/Q8IY57) · Ensembl [ENSG00000015153](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000015153)

## Data

Gene col 292: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 292); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 292, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 292]; `tensor/DDL_lfc|DDL_z.npy` [292]; `embed/gene_vectors.npy` [292]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 292 or target_col == 292). Every well: [[YAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
