---
symbol: "DOP1A"
type: "gene"
col: 1361
ensembl_id: "ENSG00000083097"
name: "DOP1 leucine zipper like protein A"
location: "6q14.1"
module: 60
arm: "-"
pooled_cpm: 45.86
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# DOP1A

*DOP1 leucine zipper like protein A* — 6q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.48× (z +26.1, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.458× (z -15.9, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HCFC2]] (+0.75, fdr 7e-06), [[LCOR]] (+0.63, fdr 7e-06), [[TMEM14C]] (+0.55, fdr 2e-05); moves opposite to [[AHSA1]] (-0.65, fdr 7e-06), [[ADCY7]] (-0.60, fdr 1e-05), [[ABCA15P]] (-0.59, fdr 3e-05).
> It sits in the **-** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1361.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.48×** | +26.1 | 0e+00 | 44/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.08×** | +22.9 | 0e+00 | 48/48 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.88×** | +21.5 | 0e+00 | 48/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.49×** | +18.6 | 0e+00 | 46/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +14.7 | 0e+00 | 42/48 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +12.1 | 9e-32 | 42/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +11.8 | 2e-30 | 36/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.50×** | +9.7 | 1e-20 | 44/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +9.1 | 4e-18 | 38/48 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +5.8 | 3e-07 | 29/49 (RKO, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.27×** | +4.8 | 8e-05 | 24/48 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.7 | 1e-04 | 17/48 (RPMI-7951, NCI-H1573, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 17/47 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.25×** | +4.1 | 0.002 | 16/48 (MIA PaCa-2, C32, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.23×** | +4.0 | 0.003 | 19/49 (MIA PaCa-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1361.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.458×** | -15.9 | 0e+00 | 46/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.533×** | -12.8 | 4e-35 | 35/48 (SHP-77, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.623×** | -9.6 | 1e-19 | 38/48 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -8.9 | 1e-16 | 27/38 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -8.3 | 1e-14 | 34/48 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.536×** | -6.6 | 3e-09 | 28/44 (SNU-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -6.5 | 8e-09 | 24/47 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.736×** | -6.2 | 3e-08 | 31/48 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.737×** | -5.9 | 3e-07 | 23/48 (Hs 766T, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.751×** | -5.8 | 4e-07 | 29/47 (H4, NCI-H460, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.829×** | -5.4 | 4e-06 | 24/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.766×** | -4.9 | 5e-05 | 22/43 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.791×** | -4.8 | 8e-05 | 24/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.651×** | -4.6 | 2e-04 | 18/48 (NCI-H1792, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.792×** | -4.6 | 2e-04 | 19/47 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.693×** | -4.6 | 2e-04 | 23/48 (PANC-1, HT-29, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.782×** | -4.5 | 2e-04 | 20/48 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **0.695×** | -3.9 | 0.003 | 17/46 (COLO 205, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.833×** | -3.6 | 0.010 | 15/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.841× | -3.3 | 0.022 | 11/48 (NCI-H23, MIA PaCa-2, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.900× | -3.0 | 0.058 | 13/49 (HT-29, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1361. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 50.9 | 4 | 8 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.0452× (z -37.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -14.5) |
| [[SW480 (line)]] | alt | 75.7 | 6 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +20.4) | [[Auranofin (drug)]] 5 µM 0.347× (z -13.7) |
| [[BT-474 (line)]] | alt | 70.9 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +18.4) | [[Auranofin (drug)]] 5 µM 0.362× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 21.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +18.2) | — |
| [[PANC-1 (line)]] | alt | 32.0 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +22.7) | [[Auranofin (drug)]] 5 µM 0.419× (z -9.8) |
| [[SNU-423 (line)]] | alt | 57.1 | 5 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 3.81× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.401× (z -9.0) |
| [[LoVo (line)]] | wt | 59.2 | 5 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.8) | [[Ixazomib citrate (drug)]] 5 µM 0.452× (z -9.1) |
| [[LS 180 (line)]] | wt | 51.9 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -12.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +17.6) | [[Auranofin (drug)]] 5 µM 0.333× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 61.3 | 3 | 3 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.54× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.240× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.429× (z -9.2) |
| [[HOP62 (line)]] | alt | 39.0 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.9) | [[Auranofin (drug)]] 5 µM 0.356× (z -9.3) |
| [[A-427 (line)]] | wt | 22.3 | 5 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.91× (z +12.3) | — |
| [[KATO III (line)]] | alt | 60.5 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.0587× (z -26.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 63.2 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 24.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +16.7) | — |
| [[RKO (line)]] | wt | 59.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.199× (z -12.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 43.5 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.74× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 52.9 | 1 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.54× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 17.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.69× (z +13.6) | — |
| [[C32 (line)]] | wt | 99.5 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.229× (z -14.7) |
| [[HT-29 (line)]] | alt | 44.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +17.1) | — |
| [[hTERT-HPNE (line)]] | wt | 28.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.09× (z +10.3) | — |
| [[J82 (line)]] | alt | 32.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.42× (z +13.2) | — |
| [[NCI-H23 (line)]] | alt | 24.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.75× (z +14.8) | — |
| [[RPMI-7951 (line)]] | alt | 47.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.315× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 36.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 142 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.181× (z -10.8) |
| [[C-33 A (line)]] | alt | 42.5 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.53× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -9.3) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 25.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +8.8) | [[Peretinoin (drug)]] 0.5 µM 0.173× (z -9.0) |
| [[Hs 766T (line)]] | wt | 34.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +11.1) | — |
| [[HS-578T (line)]] | alt | 44.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 49.2 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.04× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -15.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.61× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.183× (z -11.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 42.3 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.390× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 33.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +11.2) | [[Ixazomib citrate (drug)]] 5 µM 0.386× (z -9.1) |
| [[COLO 205 (line)]] | alt | 36.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.0) | [[vincristine (drug)]] 5 µM 0.0691× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 50.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.2) | [[Auranofin (drug)]] 5 µM 0.290× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 68.2 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.327× (z -10.8) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 61.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +12.4) | [[Bortezomib (drug)]] 5 µM 0.0620× (z -10.2) ⚠ toxic |
| [[A498 (line)]] | wt | 30.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +9.3) | — |
| [[CHP-212 (line)]] | wt | 94.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HCT15 (line)]] | alt | 56.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 32.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0895× (z -14.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 32.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +14.0) | — |
| [[A549 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1361), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC2]] | +0.75 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[LCOR]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TMEM14C]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[SUCLG1]] | +0.55 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ZNF592]] | +0.55 | +0.34 / +0.62 | both halves | 1e-04 |  |
| [[ASB8]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | +0.54 | +0.58 / +0.41 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RAB30]] | +0.53 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[CEPT1]] | +0.52 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[MIER1]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[POGZ]] | +0.51 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[YY1AP1]] | +0.49 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[PRDX2]] | +0.49 | +0.36 / +0.41 | both halves | 9e-05 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA1]] | -0.65 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[ADCY7]] | -0.60 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[ABCA15P]] | -0.59 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[HSPE1]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[C17orf67]] | -0.59 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[HSPH1]] | -0.59 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[HSP90AA2P]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SFXN5]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[HSPE1-MOB4]] | -0.57 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[MRPL18]] | -0.57 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[CACYBP]] | -0.57 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[HSPA8]] | -0.56 | -0.62 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.0, -10.6); signed map (11.4, -14.1). **Vector** length 93.2, 25.0% of its response variance represented; |z| ≥ 3 in 1,396 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.8 | +14.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +26.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +11.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +9.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.6 | +3.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -13.3 | -15.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -7.8 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -7.6 | -9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -8.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -6.5 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -5.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.5 | -2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | DOP1 leucine zipper like protein A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q14.1 — chr6:83,067,666-83,171,350 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ202D23.2; previously KIAA1117, DOPEY1 |
| Gene groups (HGNC) | DOP1 leucine zipper like protein family |
| Hallmark sets | PROTEIN_SECRETION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JWR5](https://www.uniprot.org/uniprotkb/Q5JWR5) (Protein DOP1A):

> May be involved in protein traffic between late Golgi and early endosomes.

**Summary**, from NCBI Gene [23033](https://www.ncbi.nlm.nih.gov/gene/23033):

> Predicted to be involved in Golgi to endosome transport and endoplasmic reticulum organization. Located in Golgi apparatus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21194](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21194) · Entrez [23033](https://www.ncbi.nlm.nih.gov/gene/23033) · UniProt [Q5JWR5](https://www.uniprot.org/uniprotkb/Q5JWR5) · Ensembl [ENSG00000083097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083097)

## Data

Gene col 1361: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1361); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1361, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1361]; `tensor/DDL_lfc|DDL_z.npy` [1361]; `embed/gene_vectors.npy` [1361]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1361 or target_col == 1361). Every well: [[DOP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DOP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
