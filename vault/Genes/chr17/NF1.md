---
symbol: "NF1"
type: "gene"
col: 12272
ensembl_id: "ENSG00000196712"
name: "neurofibromin 1"
location: "17q11.2"
module: 213
arm: "+"
pooled_cpm: 549.72
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# NF1

*neurofibromin 1* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.53× (z +11.4, q 1e-27, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.522× (z -24.2, q 0e+00, down in 49 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTC27]] (+0.58, fdr 3e-05), [[OMG]] (+0.57, fdr 3e-05, ⚠ same locus), [[ZNF609]] (+0.55, fdr 4e-05), [[EIF4G3]] (+0.54, fdr 1e-04); moves opposite to [[DUSP11]] (-0.48, fdr 3e-04), [[CNEP1R1]] (-0.47, fdr 5e-04), [[SEPTIN7P2]] (-0.46, fdr 5e-05).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12272.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +11.4 | 1e-27 | 44/48 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +7.9 | 1e-12 | 37/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +5.9 | 9e-07 | 30/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.8 | 1e-06 | 26/48 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +4.8 | 2e-04 | 23/48 (HS-578T, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.39×** | +3.9 | 0.011 | 27/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.048 | 16/48 (A498, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.13× | +3.3 | 0.059 | 11/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.16× | +3.3 | 0.059 | 13/48 (HS-578T, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | 1.30× | +3.0 | 0.13 | 23/48 (NCI-H1573, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12272.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.522×** | -24.2 | 0e+00 | 49/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.417×** | -23.5 | 0e+00 | 48/48 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.437×** | -22.3 | 0e+00 | 48/49 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.440×** | -22.1 | 0e+00 | 48/48 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.459×** | -21.0 | 0e+00 | 48/48 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.494×** | -18.3 | 0e+00 | 43/44 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.479×** | -16.7 | 0e+00 | 44/45 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -15.5 | 0e+00 | 47/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.688×** | -10.1 | 6e-22 | 45/48 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.704×** | -9.5 | 2e-19 | 44/48 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.695×** | -9.4 | 3e-19 | 38/50 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -9.1 | 3e-18 | 38/48 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.722×** | -8.8 | 7e-17 | 46/48 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -8.7 | 1e-16 | 38/48 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.785×** | -6.5 | 3e-09 | 33/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.855× | -5.1 | 1e-05 | 18/48 (NCI-H23, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.831×** | -4.8 | 6e-05 | 25/48 (NCI-H23, C32, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.668×** | -4.7 | 1e-04 | 38/49 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.853× | -4.3 | 6e-04 | 18/49 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.855× | -4.2 | 7e-04 | 12/49 (NCI-H2347, HS-578T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12272. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 648 | 2 | 12 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -19.3) |
| [[SW480 (line)]] | alt | 570 | 1 | 13 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -21.5) |
| [[NCI-H23 (line)]] | alt | 853 | 0 | 13 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -28.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -18.9) |
| [[SNU-423 (line)]] | alt | 486 | 0 | 13 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -26.3) |
| [[H4 (line)]] | wt | 535 | 0 | 12 (6 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -15.0) |
| [[HEC-1-A (line)]] | alt | 809 | 0 | 12 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -23.7) |
| [[LoVo (line)]] | wt | 460 | 3 (1 ⚠) | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.438× (z -16.9) |
| [[RPMI-7951 (line)]] | alt | 495 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 349 | 4 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +16.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.432× (z -14.9) |
| [[HepG2_C3A (line)]] | wt | 337 | 3 | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.81× (z +9.6) | [[Panobinostat (drug)]] 0.5 µM 0.378× (z -15.8) |
| [[HT-29 (line)]] | alt | 808 | 3 (2 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.320× (z -19.3) |
| [[NCI-H1792 (line)]] | alt | 570 | 2 | 9 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.335× (z -28.9) |
| [[NCI-H460 (line)]] | wt | 540 | 2 | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -19.8) |
| [[Panc 03.27 (line)]] | alt | 644 | 1 | 10 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -23.7) |
| [[PANC-1 (line)]] | alt | 652 | 2 (1 ⚠) | 9 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -21.9) |
| [[SW1417 (line)]] | alt | 534 | 0 | 11 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.349× (z -21.4) |
| [[C32 (line)]] | wt | 450 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -19.4) |
| [[J82 (line)]] | alt | 493 | 1 | 9 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.53× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -23.2) |
| [[LOX-IMVI (line)]] | wt | 774 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -24.8) |
| [[MIA PaCa-2 (line)]] | alt | 458 | 0 | 10 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.276× (z -23.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.382× (z -17.9) |
| [[SK-MEL-2 (line)]] | alt | 480 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.369× (z -19.5) |
| [[A-172 (line)]] | wt | 455 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -22.1) |
| [[C-33 A (line)]] | alt | 634 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -24.8) |
| [[CFPAC-1 (line)]] | alt | 431 | 0 | 9 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.378× (z -18.8) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.414× (z -17.7) |
| [[KATO III (line)]] | alt | 609 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.313× (z -22.1) |
| [[NCI-H1573 (line)]] | alt | 541 | 2 | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +15.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.386× (z -16.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.434× (z -15.1) |
| [[A498 (line)]] | wt | 517 | 1 (1 ⚠) | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 1.53× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.472× (z -21.0) |
| [[A549 (line)]] | wt | 715 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -31.8) |
| [[COLO 205 (line)]] | alt | 714 | 2 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.328× (z -18.5) |
| [[HCT15 (line)]] | alt | 770 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.521× (z -14.1) |
| [[Hs 766T (line)]] | wt | 361 | 1 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -13.4) |
| [[HS-578T (line)]] | alt | 340 | 2 (1 ⚠) | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -18.3) |
| [[hTERT-HPNE (line)]] | wt | 469 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -17.9) |
| [[NCI-H2030 (line)]] | alt | 464 | 0 | 8 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.406× (z -14.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -14.2) |
| [[SNU-1 (line)]] | wt | 631 | 2 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.449× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -13.6) |
| [[SW48 (line)]] | wt | 559 | 0 | 8 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -18.0) |
| [[A-427 (line)]] | wt | 646 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -11.7) |
| [[BT-474 (line)]] | alt | 568 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -18.6) |
| [[CHP-212 (line)]] | wt | 548 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -17.4) |
| [[LS 180 (line)]] | wt | 476 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -17.9) |
| [[NCI-H2347 (line)]] | alt | 446 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -16.3) |
| [[RKO (line)]] | wt | 668 | 1 | 6 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.381× (z -14.5) |
| [[SW 900 (line)]] | alt | 204 | 1 | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -12.5) |
| [[SHP-77 (line)]] | alt | 397 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.484× (z -13.0) |
| [[AN3 CA (line)]] | alt | 532 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -16.3) |
| [[SW 1088 (line)]] | alt | 465 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.268× (z -9.6) |
| [[SW 1271 (line)]] | alt | 576 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.336× (z -9.7) |
| [[NCI-H661 (line)]] | alt | 354 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -11.2) |
| [[NCI-H2122 (line)]] | alt | 501 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 543 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12272), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC27]] | +0.58 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[OMG]] | +0.57 | +0.55 / +0.44 | both halves | 3e-05 | STRING 696; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ZNF609]] | +0.55 | +0.55 / +0.41 | both halves | 4e-05 |  |
| [[EIF4G3]] | +0.54 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[TAS2R14]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LARS2]] | +0.54 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[COMMD10]] | +0.54 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[RALGAPA1]] | +0.53 | +0.29 / +0.40 | both halves | 2e-04 |  |
| [[EHBP1]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[INO80]] | +0.53 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[USP34]] | +0.53 | +0.59 / +0.44 | both halves | 3e-05 | same gene group |
| [[PHF14]] | +0.51 | +0.31 / +0.52 | both halves | 2e-04 |  |
| [[HDAC8]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP11]] | -0.48 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[CNEP1R1]] | -0.47 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[SEPTIN7P2]] | -0.46 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[C2CD2L]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[SEPTIN7P14]] | -0.46 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[FAM220A]] | -0.46 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[FRG1DP]] | -0.45 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[LNX2]] | -0.45 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[MMUT]] | -0.45 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[ZNF230]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[EEF1AKMT3]] | -0.44 | -0.42 / -0.27 | both halves | 3e-04 |  |
| [[SUGT1P4-STRA6LP]] | -0.44 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-22.6, 14.8); signed map (8.2, -43.9). **Vector** length 93.1, 39.9% of its response variance represented; |z| ≥ 3 in 1,575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | -18.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.4 | -22.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.5 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.5 | +0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +0.9 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.6 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | neurofibromin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:31,094,927-31,382,116 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Armadillo like helical domain containing; CRAL-TRIO lipid binding domain containing |
| Hallmark sets | HEDGEHOG_SIGNALING, APICAL_JUNCTION, MITOTIC_SPINDLE |
| Reactome | 7 pathways, smallest: RAS signaling downstream of NF1 loss-of-function variants; Regulation of RAS by GAPs; Oncogenic MAPK signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P21359](https://www.uniprot.org/uniprotkb/P21359) (Neurofibromin):

> Stimulates the GTPase activity of Ras. NF1 shows greater affinity for Ras GAP, but lower specific activity. May be a regulator of Ras activity.

**Summary**, from NCBI Gene [4763](https://www.ncbi.nlm.nih.gov/gene/4763):

> This gene product appears to function as a negative regulator of the ras signal transduction pathway. Mutations in this gene have been linked to neurofibromatosis type 1, juvenile myelomonocytic leukemia and Watson syndrome. The mRNA for this gene is subject to RNA editing (CGA>UGA->Arg1306Term) resulting in premature translation termination. Alternatively spliced transcript variants encoding different isoforms have also been described for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7765](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7765) · Entrez [4763](https://www.ncbi.nlm.nih.gov/gene/4763) · UniProt [P21359](https://www.uniprot.org/uniprotkb/P21359) · Ensembl [ENSG00000196712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196712)

## Data

Gene col 12272: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12272); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12272, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12272]; `tensor/DDL_lfc|DDL_z.npy` [12272]; `embed/gene_vectors.npy` [12272]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12272 or target_col == 12272). Every well: [[NF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
