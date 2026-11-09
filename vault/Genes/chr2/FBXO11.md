---
symbol: "FBXO11"
type: "gene"
col: 6122
ensembl_id: "ENSG00000138081"
name: "F-box protein 11"
location: "2p16.3"
module: 25
arm: "-"
pooled_cpm: 402.54
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# FBXO11

*F-box protein 11* — 2p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +10.7, q 6e-24, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.387× (z -24.8, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.432× (z -22.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00685]] (+0.66, fdr 6e-05), [[RABGEF1]] (+0.60, fdr 8e-06), [[ARIH1]] (+0.60, fdr 1e-05); moves opposite to [[PRPF19]] (-0.56, fdr 3e-05), [[FYCO1]] (-0.55, fdr 9e-04, ⚠ one half only (not replicated)), [[TRUB1]] (-0.54, fdr 1e-05), [[OCRL]] (-0.54, fdr 4e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6122.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +10.7 | 6e-24 | 35/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +8.5 | 7e-15 | 31/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +7.8 | 1e-12 | 32/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +5.0 | 1e-04 | 31/49 (SW480, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.9 | 1e-04 | 24/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.13× | +4.6 | 3e-04 | 9/48 (KATO III, A-427, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.003 | 26/48 (SW480, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | 1.15× | +3.8 | 0.009 | 11/48 (KATO III, A-427, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.088 | 20/48 (CFPAC-1, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.093 | 8/48 (NCI-H2030, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.099 | 19/49 (RKO, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.1 | 0.099 | 16/47 (NCI-H460, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6122.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.387×** | -24.8 | 0e+00 | 43/44 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.422×** | -23.4 | 0e+00 | 48/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.432×** | -22.8 | 0e+00 | 48/48 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.466×** | -20.7 | 0e+00 | 47/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.469×** | -19.0 | 0e+00 | 44/45 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.586×** | -14.5 | 1e-45 | 46/48 (AsPC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.719×** | -9.0 | 2e-17 | 36/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -7.6 | 2e-12 | 24/48 (NCI-H2347, HT-29, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.768×** | -7.2 | 5e-11 | 35/48 (HT-29, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.790×** | -6.4 | 9e-09 | 25/48 (LoVo, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.795×** | -6.2 | 2e-08 | 30/48 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.792×** | -6.1 | 5e-08 | 30/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.854× | -6.1 | 6e-08 | 18/48 (A549, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.815×** | -5.4 | 4e-06 | 25/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.879× | -4.9 | 3e-05 | 3/48 (HT-29, SNU-423, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.885× | -4.7 | 9e-05 | 12/48 (AsPC-1, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.678×** | -4.6 | 2e-04 | 35/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.858× | -4.2 | 8e-04 | 19/48 (LoVo, HT-29, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.877× | -3.6 | 0.009 | 12/48 (NCI-H1573, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.882× | -3.4 | 0.013 | 10/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.887× | -3.3 | 0.022 | 13/48 (NCI-H1792, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6122. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 344 | 9 (7 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +19.9) | [[Dinaciclib (drug)]] 0.5 µM 0.436× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.534× (z -11.4) |
| [[SW480 (line)]] | alt | 283 | 7 (3 ⚠) | 5 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.75× (z +23.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +22.7) | [[Panobinostat (drug)]] 0.5 µM 0.553× (z -13.4) |
| [[HT-29 (line)]] | alt | 385 | 0 | 10 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.388× (z -16.2) |
| [[LoVo (line)]] | wt | 530 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.374× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 332 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -23.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.329× (z -18.0) |
| [[A549 (line)]] | wt | 539 | 1 (1 ⚠) | 8 (5 ⚠) | [[Harringtonine (drug)]] 5 µM 1.74× (z +8.7) ⚠ cell-cycle shift, explains ~52% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -19.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 749 | 3 (1 ⚠) | 6 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.67× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.65× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.258× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.429× (z -16.2) |
| [[PANC-1 (line)]] | alt | 363 | 3 (2 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.471× (z -17.0) |
| [[SW1417 (line)]] | alt | 442 | 3 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.396× (z -17.6) |
| [[A-172 (line)]] | wt | 367 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.516× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 427 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.350× (z -19.4) |
| [[HepG2_C3A (line)]] | wt | 321 | 3 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.403× (z -14.3) |
| [[NCI-H1792 (line)]] | alt | 420 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.346× (z -15.1) |
| [[A-427 (line)]] | wt | 601 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -27.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.438× (z -17.8) |
| [[A498 (line)]] | wt | 327 | 2 (2 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +17.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.369× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -13.3) |
| [[BT-474 (line)]] | alt | 282 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -13.9) |
| [[H4 (line)]] | wt | 388 | 3 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.03× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.421× (z -12.4) |
| [[KATO III (line)]] | alt | 443 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.390× (z -14.1) |
| [[LOX-IMVI (line)]] | wt | 444 | 1 | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.321× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.374× (z -18.2) |
| [[MIA PaCa-2 (line)]] | alt | 583 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.430× (z -14.6) |
| [[AsPC-1 (line)]] | alt | 676 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -22.9) |
| [[HEC-1-A (line)]] | alt | 367 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.363× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.466× (z -13.6) |
| [[HOP62 (line)]] | alt | 429 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.340× (z -16.0) |
| [[HS-578T (line)]] | alt | 322 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.349× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -16.2) |
| [[hTERT-HPNE (line)]] | wt | 380 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.315× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.456× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 567 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 344 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.432× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 381 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.418× (z -12.8) |
| [[SNU-423 (line)]] | alt | 378 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -16.5) |
| [[SW 900 (line)]] | alt | 431 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.402× (z -15.0) |
| [[NCI-H2030 (line)]] | alt | 494 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.275× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.515× (z -10.0) |
| [[RKO (line)]] | wt | 454 | 1 | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.389× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.514× (z -12.4) |
| [[SK-MEL-2 (line)]] | alt | 292 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.491× (z -12.1) |
| [[C-33 A (line)]] | alt | 383 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.597× (z -8.5) |
| [[C32 (line)]] | wt | 379 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.509× (z -10.6) |
| [[Hs 766T (line)]] | wt | 314 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -13.9) |
| [[LS 180 (line)]] | wt | 345 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.484× (z -8.9) |
| [[SNU-1 (line)]] | wt | 437 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.03× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -15.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 506 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.276× (z -14.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 301 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.384× (z -11.6) |
| [[J82 (line)]] | alt | 211 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.481× (z -12.0) |
| [[NCI-H661 (line)]] | alt | 548 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -12.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 204 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 398 | 0 | 1 | — | [[Eplerenone (drug)]] 0.05 µM 0.225× (z -9.3) |
| [[CHP-212 (line)]] | wt | 319 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 438 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 409 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 381 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 388 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6122), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 10 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00685]] | +0.66 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[RABGEF1]] | +0.60 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[ARIH1]] | +0.60 | +0.57 / +0.55 | both halves | 1e-05 | STRING 402 |
| [[NECTIN2]] | +0.57 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PSEN1]] | +0.57 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.54 | +0.38 / +0.55 | both halves | 7e-05 |  |
| [[SPACDR]] | +0.54 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[SPSB2]] | +0.53 | +0.16 / +0.52 | ⚠ one half (not replicated) | 0.001 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[DCTN6-DT]] | +0.53 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[ZSWIM6]] | +0.53 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[SOS2]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[PPP1R13B]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[STX5]] | +0.52 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF19]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[FYCO1]] | -0.55 | -0.19 / -0.59 | ⚠ one half (not replicated) | 9e-04 |  |
| [[TRUB1]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[OCRL]] | -0.54 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[MBTPS2]] | -0.53 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SF3A1]] | -0.53 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[NELFCD]] | -0.53 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[ATIC]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MANBAL]] | -0.53 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[NEK6]] | -0.53 | -0.18 / -0.41 | ⚠ not reproduced | 1e-03 |  |
| [[WASH8P]] ⚠ | -0.52 | -0.34 / -0.50 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP13A1]] | -0.52 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[TOP3B]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[RFT1]] | -0.51 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[ZC3HAV1L]] | -0.51 | -0.26 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-22.2, -6.2); signed map (4.4, 18.8). **Vector** length 104, 40.7% of its response variance represented; |z| ≥ 3 in 1,494 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +7.2 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +0.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +3.0 | +4.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.8 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +1.7 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | +2.0 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.8 | -4.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -3.9 | -0.7 |
|  | [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.3 | -6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.3 — chr2:47,789,316-47,906,498 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FBX11, UBR6 |
| Gene groups (HGNC) | F-boxes other; Ubiquitin protein ligase E3 component n-recognins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XK2](https://www.uniprot.org/uniprotkb/Q86XK2) (F-box only protein 11):

> Substrate recognition component of a SCF (SKP1-CUL1-F-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as DTL/CDT2, BCL6, SNAI1 and PRDM1/BLIMP1. The SCF(FBXO11) complex mediates ubiquitination and degradation of BCL6, thereby playing a role in the germinal center B-cells terminal differentiation toward memory B-cells and plasma cells. The SCF(FBXO11) complex also mediates ubiquitination and …

**Summary**, from NCBI Gene [80204](https://www.ncbi.nlm.nih.gov/gene/80204):

> This gene encodes a member of the F-box protein family which is characterized by an approximately 40 amino acid motif, the F-box. The F-box proteins constitute one of the four subunits of ubiquitin protein ligase complex called SCFs (SKP1-cullin-F-box), which function in phosphorylation-dependent ubiquitination. The F-box proteins are divided into 3 classes: Fbws containing WD-40 domains, Fbls containing leucine-rich repeats, and Fbxs containing either different protein-protein interaction …

**Accessions** — [HGNC:13590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13590) · Entrez [80204](https://www.ncbi.nlm.nih.gov/gene/80204) · UniProt [Q86XK2](https://www.uniprot.org/uniprotkb/Q86XK2) · Ensembl [ENSG00000138081](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138081)

## Data

Gene col 6122: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6122); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6122, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6122]; `tensor/DDL_lfc|DDL_z.npy` [6122]; `embed/gene_vectors.npy` [6122]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6122 or target_col == 6122). Every well: [[FBXO11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
