---
symbol: "ANKRD17"
type: "gene"
col: 5323
ensembl_id: "ENSG00000132466"
name: "ankyrin repeat domain 17"
location: "4q13.3"
module: 1
arm: "+"
pooled_cpm: 434.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ANKRD17

*ankyrin repeat domain 17* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.47× (z +14.4, q 3e-44, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.472× (z -19.9, q 0e+00, down in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.721× (z -8.7, q 5e-16, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTREX]] (+0.64, fdr 1e-05), [[TTC27]] (+0.60, fdr 2e-05), [[MRPL50]] (+0.59, fdr 2e-05); moves opposite to [[LYSMD4]] (-0.58, fdr 5e-05), [[KCTD9]] (-0.53, fdr 3e-05), [[PLCB3]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +14.4 | 3e-44 | 42/48 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.60×** | +12.0 | 7e-31 | 44/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +11.7 | 2e-29 | 46/48 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +9.1 | 2e-17 | 44/48 (NCI-H460, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.99×** | +8.6 | 1e-15 | 42/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +8.5 | 2e-15 | 45/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.96×** | +8.4 | 4e-15 | 44/49 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +7.5 | 5e-12 | 34/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +7.4 | 1e-11 | 35/48 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.17× | +5.8 | 3e-07 | 17/48 (PANC-1, C32, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +5.8 | 4e-07 | 31/48 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +5.6 | 1e-06 | 30/48 (NCI-H2347, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +4.6 | 2e-04 | 23/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.4 | 4e-04 | 23/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.25×** | +4.4 | 5e-04 | 29/48 (Hs 766T, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.1 | 0.002 | 18/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.08× | +3.0 | 0.089 | 3/48 (KATO III, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.472×** | -19.9 | 0e+00 | 47/49 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -17.4 | 0e+00 | 43/44 (HEC-1-A, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.603×** | -10.4 | 3e-23 | 41/45 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.721×** | -8.7 | 5e-16 | 41/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.733×** | -8.2 | 2e-14 | 42/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.823×** | -7.4 | 2e-11 | 26/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.784×** | -6.5 | 8e-09 | 31/48 (RKO, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.811×** | -5.6 | 2e-06 | 30/48 (SW480, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~1% of this change | 0.834× | -4.6 | 2e-04 | 23/47 (MIA PaCa-2, RKO, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.870× | -3.7 | 0.011 | 20/48 (BT-474, A498, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 0.913× | -3.5 | 0.027 | 2/48 (RKO, NCI-H2347) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.885× | -3.3 | 0.051 | 13/48 (AN3 CA, HepG2/C3A, …) | rises with dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.822×** | -3.2 | 0.059 | 25/48 (Hs 766T, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.832× | -3.0 | 0.11 | 22/48 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 437 | 11 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -16.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 642 | 7 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +20.1) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -16.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 591 | 5 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.635× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 349 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.457× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -10.5) |
| [[SW480 (line)]] | alt | 556 | 4 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.491× (z -14.4) |
| [[HS-578T (line)]] | alt | 313 | 6 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.88× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.587× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 486 | 3 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +17.6) | [[Dinaciclib (drug)]] 0.5 µM 0.405× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.585× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 471 | 3 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +18.3) | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.560× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 544 | 6 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.66× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.408× (z -18.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 705 | 2 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.424× (z -14.2) |
| [[A549 (line)]] | wt | 331 | 4 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +20.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -20.8) |
| [[SNU-1 (line)]] | wt | 581 | 5 | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.93× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.356× (z -17.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 423 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.401× (z -15.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 305 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -13.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 434 | 2 | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.64× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.568× (z -11.1) |
| [[SW 900 (line)]] | alt | 446 | 2 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.74× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -14.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 446 | 3 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 530 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -21.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 329 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.511× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 357 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -12.4) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 495 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -11.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 558 | 1 | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 1.68× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -20.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 564 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -16.0) |
| [[COLO 205 (line)]] | alt | 523 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.556× (z -10.2) |
| [[H4 (line)]] | wt | 602 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -19.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.519× (z -9.8) |
| [[Hs 766T (line)]] | wt | 318 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.480× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 465 | 1 | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.27× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.647× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 369 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.464× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 461 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.56× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.481× (z -14.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 427 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -13.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 366 | 2 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.470× (z -14.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 197 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.606× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 390 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +14.3) | [[Docetaxel (drug)]] 0.05 µM 0.591× (z -9.3) ⚠ transcription drop |
| [[C32 (line)]] | wt | 361 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.580× (z -8.9) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 577 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -11.8) |
| [[hTERT-HPNE (line)]] | wt | 390 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -20.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 358 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.58× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.576× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 367 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.589× (z -9.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 547 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -12.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 575 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.469× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 223 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.472× (z -11.2) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 507 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.508× (z -11.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 343 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 411 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.557× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 391 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 416 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 468 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 418 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 542 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTREX]] | +0.64 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[TTC27]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[MRPL50]] | +0.59 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[PHF14]] | +0.58 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[SDAD1]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[GPHN]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ATF1]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[TAF2]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[INO80]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[FNDC3A]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ZMYM4]] | +0.55 | +0.37 / +0.64 | both halves | 8e-05 |  |
| [[LINC01278]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYSMD4]] | -0.58 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[KCTD9]] | -0.53 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[PLCB3]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[C7orf57]] | -0.52 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[MARF1]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[SEC61A2]] | -0.51 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[TNFRSF11A]] | -0.50 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DNAAF3]] | -0.50 | -0.38 / -0.37 | both halves | 9e-05 |  |
| [[MPND]] | -0.50 | -0.38 / -0.37 | both halves | 8e-05 |  |
| [[MXD1]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ZFYVE21]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[PPP2R5B]] | -0.50 | -0.47 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ANKRD17's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.452). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.3, 12.8); signed map (6.3, -42.0). **Vector** length 107, 42.9% of its response variance represented; |z| ≥ 3 in 1,264 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +7.8 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.5 | +12.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.1 | +3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.0 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +3.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.1 | +1.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.3 | +1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.1 | +2.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.2 | -8.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -5.2 | -5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -3.6 | -8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.3 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -0.8 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 17 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:73,073,376-73,258,798 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GTAR, KIAA0697, FLJ22206, NY-BR-16, MASK2 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75179](https://www.uniprot.org/uniprotkb/O75179) (Ankyrin repeat domain-containing protein 17):

> Could play pivotal roles in cell cycle and DNA regulation. Involved in innate immune defense against viruse by positively regulating the viral dsRNA receptors DDX58 and IFIH1 signaling pathways. Involves in NOD2- and NOD1-mediated responses to bacteria suggesting a role in innate antibacterial immune pathways too. Target of enterovirus 71 which is the major etiological agent of HFMD (hand, foot and mouth disease). Could play a central role for the formation and/or maintenance of the blood …

**Summary**, from NCBI Gene [26057](https://www.ncbi.nlm.nih.gov/gene/26057):

> The protein encoded by this gene belongs to the family of ankyrin repeat-containing proteins, and contains two distinct arrays of ankyrin repeats in its amino-terminal region, one with 15 ankyrin repeats, and the other with 10 ankyrin repeats. It also contains a nuclear export signal, nuclear localization signal, and a cyclin-binding RXL motif. Localization of this protein to the nucleus has been shown experimentally, and interactions between this protein and cyclin-dependent kinase 2 have been …

**Accessions** — [HGNC:23575](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23575) · Entrez [26057](https://www.ncbi.nlm.nih.gov/gene/26057) · UniProt [O75179](https://www.uniprot.org/uniprotkb/O75179) · Ensembl [ENSG00000132466](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132466)

## Data

Gene col 5323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5323); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5323]; `tensor/DDL_lfc|DDL_z.npy` [5323]; `embed/gene_vectors.npy` [5323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5323 or target_col == 5323). Every well: [[ANKRD17 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD17.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
