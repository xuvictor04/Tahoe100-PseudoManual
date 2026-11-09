---
symbol: "SOS1"
type: "gene"
col: 3735
ensembl_id: "ENSG00000115904"
name: "SOS Ras/Rac guanine nucleotide exchange factor 1"
location: "2p22.1"
module: 231
arm: "+"
pooled_cpm: 315.51
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/231"]
generated_by: "tahoemap"
---

# SOS1

*SOS Ras/Rac guanine nucleotide exchange factor 1* — 2p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.27× (z +10.0, q 9e-21, up in 31 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.429× (z -35.7, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PMS2P4-1]] (+0.67, fdr 1e-05), [[LINC02680]] (+0.65, fdr 1e-05), [[GPBP1L1]] (+0.64, fdr 9e-06); moves opposite to [[C15orf39]] (-0.65, fdr 1e-05), [[TMEM185B]] (-0.64, fdr 7e-06), [[CSRP1]] (-0.64, fdr 1e-05).
> It is in [[Module 231]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3735.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +10.0 | 9e-21 | 31/49 (AsPC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +8.9 | 2e-16 | 27/48 (RKO, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.18× | +5.0 | 9e-05 | 23/47 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.0 | 9e-05 | 19/50 (RKO, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.16× | +4.4 | 0.001 | 16/48 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.11× | +4.3 | 0.002 | 7/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.15× | +4.2 | 0.002 | 12/47 (A498, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.14× | +4.2 | 0.002 | 11/47 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.13× | +3.9 | 0.007 | 9/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.10× | +3.8 | 0.007 | 6/48 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.14× | +3.8 | 0.007 | 14/49 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.13× | +3.8 | 0.007 | 13/49 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | 1.12× | +3.8 | 0.007 | 12/50 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.13× | +3.7 | 0.008 | 5/49 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.12× | +3.4 | 0.025 | 12/48 (NCI-H23, A549, …) | all doses, flat |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.11× | +3.4 | 0.025 | 2/48 (C-33 A, COLO 205) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.08× | +3.3 | 0.029 | 2/48 (MIA PaCa-2, SW 900) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.051 | 3/47 (SK-MEL-2, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.11× | +3.1 | 0.059 | 13/48 (LoVo, MIA PaCa-2, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.28×** | +3.0 | 0.071 | 12/50 (A-427, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 17 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3735.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.429×** | -35.7 | 0e+00 | 44/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.425×** | -26.7 | 0e+00 | 47/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.414×** | -26.5 | 0e+00 | 46/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.432×** | -26.2 | 0e+00 | 47/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.450×** | -24.9 | 0e+00 | 46/48 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.452×** | -24.8 | 0e+00 | 48/49 (NCI-H23, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.494×** | -22.0 | 0e+00 | 46/48 (SW480, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.489×** | -21.5 | 0e+00 | 42/44 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.492×** | -20.4 | 0e+00 | 44/45 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.672×** | -12.4 | 2e-33 | 41/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.678×** | -12.1 | 4e-32 | 40/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.692×** | -11.0 | 1e-26 | 39/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.794×** | -9.5 | 6e-20 | 30/48 (LOX-IMVI, MIA PaCa-2, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -9.1 | 2e-18 | 38/49 (A-172, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.747×** | -9.1 | 3e-18 | 30/48 (NCI-H1573, NCI-H460, …) | rises with dose | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.751×** | -8.6 | 3e-16 | 32/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.811×** | -6.5 | 2e-09 | 27/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.815×** | -6.4 | 5e-09 | 26/48 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.898× | -4.4 | 2e-04 | 12/48 (A-172, HOP62, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.865× | -4.3 | 3e-04 | 15/48 (SW 900, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.884× | -3.8 | 0.003 | 16/48 (SW 900, CFPAC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.732×** | -3.8 | 0.003 | 23/48 (A-172, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.882× | -3.6 | 0.006 | 11/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3735. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 407 | 6 | 18 (11 ⚠) | [[Betamethasone dipropionate (drug)]] 5 µM 1.98× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -41.0) |
| [[NCI-H460 (line)]] | wt | 309 | 1 (1 ⚠) | 17 (11 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.54× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -29.1) |
| [[A-172 (line)]] | wt | 353 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -48.9) |
| [[MIA PaCa-2 (line)]] | alt | 336 | 1 | 15 (10 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -25.1) |
| [[SW480 (line)]] | alt | 293 | 0 | 16 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -21.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -19.9) |
| [[AsPC-1 (line)]] | alt | 323 | 3 (1 ⚠) | 12 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +20.4) | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -26.5) |
| [[LOX-IMVI (line)]] | wt | 370 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -24.3) |
| [[NCI-H23 (line)]] | alt | 371 | 3 (1 ⚠) | 11 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -38.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.314× (z -28.5) |
| [[SW 900 (line)]] | alt | 506 | 1 | 13 (7 ⚠) | [[Menadione (drug)]] 5 µM 2.76× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -14.0) |
| [[A549 (line)]] | wt | 393 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -27.7) |
| [[PANC-1 (line)]] | alt | 291 | 2 (1 ⚠) | 11 (6 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.56× (z +9.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.436× (z -18.5) |
| [[CFPAC-1 (line)]] | alt | 414 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -36.9) |
| [[A498 (line)]] | wt | 224 | 2 | 9 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -20.5) |
| [[HOP62 (line)]] | alt | 285 | 1 | 10 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -31.0) |
| [[HT-29 (line)]] | alt | 271 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -15.6) |
| [[RKO (line)]] | wt | 255 | 3 (1 ⚠) | 8 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -33.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.404× (z -14.2) |
| [[A-427 (line)]] | wt | 357 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.426× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.547× (z -17.2) |
| [[BT-474 (line)]] | alt | 181 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -16.9) |
| [[HepG2_C3A (line)]] | wt | 533 | 3 | 7 (6 ⚠) | [[Gemcitabine (drug)]] 0.05 µM 1.98× (z +12.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.320× (z -14.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -13.7) |
| [[HS-578T (line)]] | alt | 244 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -23.8) |
| [[SNU-423 (line)]] | alt | 278 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -34.9) |
| [[COLO 205 (line)]] | alt | 241 | 2 (1 ⚠) | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +11.2) | [[Harringtonine (drug)]] 5 µM 0.289× (z -16.7) |
| [[HCT15 (line)]] | alt | 451 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.371× (z -18.5) |
| [[HEC-1-A (line)]] | alt | 288 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -18.2) |
| [[Hs 766T (line)]] | wt | 267 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 301 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -22.8) |
| [[LoVo (line)]] | wt | 401 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -20.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -20.1) |
| [[Panc 03.27 (line)]] | alt | 298 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -29.5) |
| [[SNU-1 (line)]] | wt | 289 | 0 | 9 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.385× (z -13.9) |
| [[C32 (line)]] | wt | 273 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -30.2) |
| [[KATO III (line)]] | alt | 427 | 1 | 7 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.274× (z -21.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -19.3) |
| [[LS 180 (line)]] | wt | 397 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -15.1) |
| [[RPMI-7951 (line)]] | alt | 291 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -21.8) |
| [[SK-MEL-2 (line)]] | alt | 270 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -22.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.392× (z -20.7) |
| [[SW1417 (line)]] | alt | 273 | 1 | 7 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +15.0) | [[Panobinostat (drug)]] 5 µM 0.426× (z -15.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.476× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 301 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.271× (z -16.5) |
| [[NCI-H2347 (line)]] | alt | 210 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -18.9) |
| [[C-33 A (line)]] | alt | 439 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.426× (z -10.6) |
| [[H4 (line)]] | wt | 395 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.475× (z -11.2) |
| [[SW48 (line)]] | wt | 296 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.412× (z -13.5) |
| [[SHP-77 (line)]] | alt | 207 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.60× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.552× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.589× (z -8.6) |
| [[AN3 CA (line)]] | alt | 308 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.298× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -11.2) |
| [[J82 (line)]] | alt | 145 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -24.7) |
| [[NCI-H1792 (line)]] | alt | 465 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[CHP-212 (line)]] | wt | 300 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.365× (z -9.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[NCI-H661 (line)]] | alt | 243 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.292× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW 1271 (line)]] | alt | 318 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.5) |
| [[NCI-H2122 (line)]] | alt | 347 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 284 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3735), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P4-1]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[LINC02680]] | +0.65 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[GPBP1L1]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[ARID4B]] | +0.64 | +0.49 / +0.59 | both halves | 1e-05 | pathway: Potential therapeutics for SARS |
| [[CDK13]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[RAB6A]] | +0.63 | +0.58 / +0.76 | both halves | 8e-06 |  |
| [[ZNF248]] | +0.62 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[BBX]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[UBE4B]] | +0.61 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[MFSD8]] | +0.61 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[CDK19]] | +0.60 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[BMPR1A]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf39]] | -0.65 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.64 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[CSRP1]] | -0.64 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.61 | -0.54 / -0.67 | both halves | 1e-05 |  |
| [[JUNB]] | -0.61 | -0.51 / -0.55 | both halves | 1e-05 | pathway: Signaling by NTRK1 (TRKA) |
| [[IER2]] | -0.61 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[CSRNP1]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PCNX2]] | -0.60 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[FARSB]] | -0.58 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.57 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[EGR1]] | -0.57 | -0.57 / -0.47 | both halves | 2e-05 | pathway: Signaling by NTRK1 (TRKA); STRING 426 |
| [[CDC42EP2]] | -0.56 | -0.54 / -0.59 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 231]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.795). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-14.6, 25.6); signed map (4.8, 3.1). **Vector** length 121, 44.7% of its response variance represented; |z| ≥ 3 in 1,702 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.0 | +10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +8.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.1 | +5.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | +6.0 | +4.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.9 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.1 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +3.1 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.1 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -10.4 | -20.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -9.4 | -9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.1 | -5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | -6.7 | -21.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -6.1 | -24.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -6.5 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -3.4 | -3.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | SOS Ras/Rac guanine nucleotide exchange factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.1 — chr2:38,962,206-39,124,345 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HGF, GF1; previously GINGF |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 128 pathways, smallest: SOS-mediated signalling; Activated NTRK2 signals through RAS; Activated NTRK3 signals through RAS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07889](https://www.uniprot.org/uniprotkb/Q07889) (Son of sevenless homolog 1):

> Promotes the exchange of Ras-bound GDP by GTP. Probably by promoting Ras activation, regulates phosphorylation of MAP kinase MAPK3/ERK1 in response to EGF. Catalytic component of a trimeric complex that participates in transduction of signals from Ras to Rac by promoting the Rac-specific guanine nucleotide exchange factor (GEF) activity (By similarity).

**Summary**, from NCBI Gene [6654](https://www.ncbi.nlm.nih.gov/gene/6654):

> This gene encodes a protein that is a guanine nucleotide exchange factor for RAS proteins, membrane proteins that bind guanine nucleotides and participate in signal transduction pathways. GTP binding activates and GTP hydrolysis inactivates RAS proteins. The product of this gene may regulate RAS proteins by facilitating the exchange of GTP for GDP. Mutations in this gene are associated with gingival fibromatosis 1 and Noonan syndrome type 4. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11187) · Entrez [6654](https://www.ncbi.nlm.nih.gov/gene/6654) · UniProt [Q07889](https://www.uniprot.org/uniprotkb/Q07889) · Ensembl [ENSG00000115904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115904)

## Data

Gene col 3735: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3735); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3735, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3735]; `tensor/DDL_lfc|DDL_z.npy` [3735]; `embed/gene_vectors.npy` [3735]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3735 or target_col == 3735). Every well: [[SOS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
