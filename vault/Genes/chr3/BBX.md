---
symbol: "BBX"
type: "gene"
col: 3553
ensembl_id: "ENSG00000114439"
name: "BBX high mobility group box domain containing"
location: "3q13.12"
module: 231
arm: "+"
pooled_cpm: 387.71
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 36
n_dd_up_clean: 2
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/231"]
generated_by: "tahoemap"
---

# BBX

*BBX high mobility group box domain containing* — 3q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.26× (z +7.7, q 7e-12, up in 29 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 1.86×, COLO 205 1.97×, A498 1.53×, hTERT-HPNE 1.68×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 1.74×, C-33 A 1.87×, SW480 1.46×, SW48 1.85×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 1.98×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 1.44×).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.278× (z -44.6, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDK19]] (+0.65, fdr 7e-06), [[ACBD5]] (+0.64, fdr 1e-05), [[NCOA2]] (+0.63, fdr 1e-05); moves opposite to [[MIER2]] (-0.55, fdr 1e-04), [[ADAMTSL5]] (-0.54, fdr 5e-05), [[ZNF865]] (-0.52, fdr 5e-05).
> It is in [[Module 231]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3553.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 6 lines (LoVo 1.86×, COLO 205 1.97×, A498 1.53×, hTERT-HPNE 1.68×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 4 lines (A498 1.74×, C-33 A 1.87×, SW480 1.46×, SW48 1.85×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 1.98×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 1.44×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +7.7 | 7e-12 | 29/48 (A498, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +7.2 | 2e-10 | 26/50 (Panc 03.27, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.15× | +4.9 | 2e-04 | 14/48 (A498, KATO III, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.15× | +4.7 | 4e-04 | 14/47 (A549, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.10× | +4.0 | 0.007 | 5/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 1.12× | +3.8 | 0.012 | 8/49 (PANC-1, KATO III, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.12× | +3.7 | 0.015 | 9/47 (HOP62, SHP-77, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.11× | +3.6 | 0.021 | 9/49 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.10× | +3.4 | 0.049 | 5/47 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.08× | +3.3 | 0.049 | 4/48 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.11× | +3.3 | 0.051 | 6/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.10× | +3.2 | 0.067 | 7/48 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 1.09× | +3.2 | 0.070 | 5/48 (HT-29, HS-578T, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.09× | +3.1 | 0.075 | 8/49 (HOP62, AsPC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 56 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3553.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.278×** | -44.6 | 0e+00 | 48/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.284×** | -43.8 | 0e+00 | 48/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.386×** | -33.1 | 0e+00 | 48/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.485×** | -24.2 | 0e+00 | 47/47 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.631×** | -22.6 | 0e+00 | 35/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.704×** | -17.2 | 0e+00 | 41/48 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.626×** | -15.0 | 0e+00 | 41/45 (SK-MEL-2, Panc 03.27, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.662×** | -14.3 | 1e-44 | 47/48 (SNU-1, AsPC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -14.3 | 2e-44 | 45/49 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.680×** | -13.4 | 4e-39 | 41/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.696×** | -12.6 | 1e-34 | 45/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.700×** | -12.4 | 2e-33 | 34/48 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.696×** | -12.1 | 4e-32 | 29/44 (A-427, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.721×** | -11.3 | 4e-28 | 36/48 (HT-29, NCI-H23, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.743×** | -10.3 | 3e-23 | 32/49 (SK-MEL-2, NCI-H23, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.627×** | -7.8 | 2e-13 | 42/48 (SHP-77, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.800×** | -7.4 | 3e-12 | 27/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.641×** | -7.4 | 3e-12 | 37/49 (SK-MEL-2, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.808×** | -7.4 | 4e-12 | 30/49 (Panc 03.27, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.650×** | -7.2 | 2e-11 | 42/48 (AsPC-1, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3553. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 324 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -37.3) |
| [[C32 (line)]] | wt | 641 | 2 | 15 (6 ⚠) | [[Ponatinib (drug)]] 5 µM 1.98× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -27.0) |
| [[SK-MEL-2 (line)]] | alt | 671 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -33.5) |
| [[NCI-H23 (line)]] | alt | 719 | 0 | 14 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -37.1) |
| [[Panc 03.27 (line)]] | alt | 615 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.185× (z -39.4) |
| [[PANC-1 (line)]] | alt | 301 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.428× (z -18.1) |
| [[SW48 (line)]] | wt | 536 | 1 | 12 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -22.3) |
| [[BT-474 (line)]] | alt | 409 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.173× (z -30.1) |
| [[HT-29 (line)]] | alt | 473 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -31.3) |
| [[NCI-H2030 (line)]] | alt | 247 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -21.3) |
| [[SW 900 (line)]] | alt | 312 | 0 | 12 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -25.2) |
| [[HepG2_C3A (line)]] | wt | 338 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -19.8) |
| [[LoVo (line)]] | wt | 326 | 1 (1 ⚠) | 10 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +17.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -23.8) |
| [[SNU-1 (line)]] | wt | 234 | 0 | 11 (8 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -16.9) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.432× (z -11.5) |
| [[SW1417 (line)]] | alt | 471 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -26.9) |
| [[AsPC-1 (line)]] | alt | 234 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -23.7) |
| [[HCT15 (line)]] | alt | 617 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -27.2) |
| [[NCI-H2347 (line)]] | alt | 465 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -24.1) |
| [[AN3 CA (line)]] | alt | 566 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -17.0) |
| [[CFPAC-1 (line)]] | alt | 390 | 0 | 9 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -21.4) |
| [[LOX-IMVI (line)]] | wt | 386 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -26.4) |
| [[RKO (line)]] | wt | 517 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -21.2) |
| [[RPMI-7951 (line)]] | alt | 471 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -25.7) |
| [[A-427 (line)]] | wt | 294 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -31.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.446× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 695 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.237× (z -31.8) |
| [[HS-578T (line)]] | alt | 537 | 1 (1 ⚠) | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.54× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.250× (z -27.6) |
| [[NCI-H1573 (line)]] | alt | 428 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -23.8) |
| [[SHP-77 (line)]] | alt | 314 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -22.2) |
| [[C-33 A (line)]] | alt | 391 | 1 | 6 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.248× (z -21.5) |
| [[Hs 766T (line)]] | wt | 257 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.254× (z -23.0) |
| [[NCI-H1792 (line)]] | alt | 363 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -30.1) |
| [[SNU-423 (line)]] | alt | 496 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -27.8) |
| [[SW480 (line)]] | alt | 281 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -36.5) |
| [[A-172 (line)]] | wt | 341 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.284× (z -20.7) |
| [[A498 (line)]] | wt | 248 | 2 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.53× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.456× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 154 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -13.1) |
| [[A549 (line)]] | wt | 276 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.223× (z -25.9) |
| [[CHP-212 (line)]] | wt | 433 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.170× (z -20.0) |
| [[H4 (line)]] | wt | 334 | 2 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -15.6) |
| [[HOP62 (line)]] | alt | 436 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -23.9) |
| [[KATO III (line)]] | alt | 283 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -24.6) |
| [[LS 180 (line)]] | wt | 379 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -19.6) |
| [[COLO 205 (line)]] | alt | 235 | 1 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 313 | 1 (1 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -17.4) |
| [[J82 (line)]] | alt | 495 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -23.9) |
| [[SW 1271 (line)]] | alt | 399 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -10.0) |
| [[NCI-H596 (line)]] | alt | 395 | 0 | 1 | — | [[Oxaprozin (drug)]] 5 µM 0.385× (z -11.2) |
| [[NCI-H2122 (line)]] | alt | 363 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 287 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 245 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3553), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDK19]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ACBD5]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[NCOA2]] | +0.63 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[ZMYM2]] | +0.63 | +0.61 / +0.65 | both halves | 7e-06 | STRING 434 |
| [[SOS1]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[WDFY3]] | +0.59 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[DIPK2A]] | +0.58 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[JMY]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ARID4B]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 | STRING 440 |
| [[ATOSA]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ARID1B]] | +0.56 | +0.37 / +0.63 | both halves | 7e-05 |  |
| [[PHF21A]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER2]] | -0.55 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[ADAMTSL5]] | -0.54 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ZNF865]] | -0.52 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ZNF473]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[C13orf46]] | -0.51 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ZNF583]] | -0.51 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ARAP3]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[ZNF787]] | -0.51 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TMEM44]] | -0.50 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[AP1M1]] | -0.50 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[ZNF529]] | -0.49 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[GPSM1]] | -0.49 | -0.33 / -0.45 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BBX's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Epirubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 231]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.765). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (4.8, -26.7); signed map (-11.2, 11.1). **Vector** length 136, 50.8% of its response variance represented; |z| ≥ 3 in 1,989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.2 | +7.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.0 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.8 | +2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.5 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.9 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.6 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.6 | +3.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -12.8 | -24.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -11.9 | -17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | -9.2 | -15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -9.1 | -7.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -7.6 | -14.3 |
|  | [[EX229 (drug)]] 5 µM |  | -5.9 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.6 | -7.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -11.3 |

## What is on record

|  |  |
|---|---|
| Name | BBX high mobility group box domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.12 — chr3:107,522,936-107,811,339 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MDS001, HSPC339, HBP2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WY36](https://www.uniprot.org/uniprotkb/Q8WY36) (HMG box transcription factor BBX):

> Transcription factor that is necessary for cell cycle progression from G1 to S phase.

**Summary**, from NCBI Gene [56987](https://www.ncbi.nlm.nih.gov/gene/56987):

> Enables sequence-specific double-stranded DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within bone development. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14422](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14422) · Entrez [56987](https://www.ncbi.nlm.nih.gov/gene/56987) · UniProt [Q8WY36](https://www.uniprot.org/uniprotkb/Q8WY36) · Ensembl [ENSG00000114439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114439)

## Data

Gene col 3553: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3553); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3553, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3553]; `tensor/DDL_lfc|DDL_z.npy` [3553]; `embed/gene_vectors.npy` [3553]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3553 or target_col == 3553). Every well: [[BBX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BBX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
