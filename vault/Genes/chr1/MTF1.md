---
symbol: "MTF1"
type: "gene"
col: 12050
ensembl_id: "ENSG00000188786"
name: "metal regulatory transcription factor 1"
location: "1p34.3"
module: 119
arm: "+"
pooled_cpm: 50.03
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# MTF1

*metal regulatory transcription factor 1* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.34× (z +22.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.388× (z -23.7, q 0e+00, down in 36 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.0918×, J82 0.165×, NCI-H2030 0.188×, H4 0.0878×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 0.192×, PANC-1 0.244×, A-427 0.127×, RPMI-7951 0.123×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HEC-1-A 0.0455×, NCI-H2030 0.101×, A498 0.249×, HT-29 0.194×; ⚠ toxic; transcription drop); [[Pralsetinib (drug)]] 5 µM in 1 line (C32 0.133×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM11]] (+0.74, fdr 7e-06), [[C16orf91]] (+0.74, fdr 7e-06), [[YIPF5]] (+0.73, fdr 7e-06); moves opposite to [[HNRNPH3]] (-0.61, fdr 1e-04), [[CCDC50]] (-0.59, fdr 2e-04), [[MYEF2]] (-0.57, fdr 6e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12050.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.34×** | +22.1 | 0e+00 | 47/48 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.09×** | +19.2 | 0e+00 | 42/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +19.0 | 0e+00 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.89×** | +18.5 | 0e+00 | 43/49 (SW480, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +15.1 | 0e+00 | 42/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +9.4 | 4e-19 | 36/48 (HT-29, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +9.2 | 4e-18 | 36/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +9.2 | 4e-18 | 37/48 (SW480, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +8.1 | 3e-14 | 29/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +6.4 | 7e-09 | 24/48 (LoVo, NCI-H2347, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +6.4 | 7e-09 | 25/43 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.25×** | +5.8 | 4e-07 | 22/48 (HepG2/C3A, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +5.4 | 3e-06 | 24/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.23×** | +5.2 | 9e-06 | 23/47 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.21×** | +5.0 | 2e-05 | 20/48 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +4.5 | 2e-04 | 14/48 (PANC-1, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +4.2 | 8e-04 | 18/48 (LoVo, HT-29, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.003 | 15/48 (NCI-H460, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.015 | 5/48 (SW480, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.015 | 9/48 (HT-29, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.015 | 6/48 (HT-29, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12050.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 6 lines (Panc 03.27 0.0918×, J82 0.165×, NCI-H2030 0.188×, H4 0.0878×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (A498 0.192×, PANC-1 0.244×, A-427 0.127×, RPMI-7951 0.123×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 4 lines (HEC-1-A 0.0455×, NCI-H2030 0.101×, A498 0.249×, HT-29 0.194×; ⚠ toxic; transcription drop); [[Pralsetinib (drug)]] 5 µM in 1 line (C32 0.133×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.388×** | -23.7 | 0e+00 | 36/42 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.431×** | -21.9 | 0e+00 | 42/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.496×** | -16.9 | 0e+00 | 35/44 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 0.834× | -4.5 | 8e-04 | 19/47 (NCI-H1573, RPMI-7951, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.869× | -3.5 | 0.050 | 15/47 (SW 1271, SW480, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | 0.889× | -3.1 | 0.21 | 13/48 (J82, Hs 766T, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12050. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 35.1 | 7 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.431× (z -9.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 45.0 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.07× (z +18.2) | [[Dinaciclib (drug)]] 0.05 µM 0.342× (z -12.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 45.6 | 4 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0455× (z -35.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 51.2 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.23× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.384× (z -9.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 60.9 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.34× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -13.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 66.0 | 3 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -21.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 51.8 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.49× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -11.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 61.5 | 2 | 3 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.33× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -19.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 55.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -9.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 67.8 | 2 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.56× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -26.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 48.8 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.05× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -12.4) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 52.4 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.80× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.368× (z -9.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 44.9 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.85× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.165× (z -20.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 55.5 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.101× (z -24.3) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 70.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -22.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.4 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.36× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -10.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 50.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -12.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 57.2 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.35× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.125× (z -15.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 69.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -13.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 50.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.57× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 39.4 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +8.8) ⚠ cell-cycle shift, explains ~1% of this change | [[Dinaciclib (drug)]] 5 µM 0.219× (z -15.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 48.8 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.95× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.0 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -16.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 70.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -20.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 39.7 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -10.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 45.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -21.2) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 50.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.59× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 47.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.95× (z +9.2) | — |
| [[RKO (line)]] | wt | 47.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.71× (z +11.8) | — |
| [[A-172 (line)]] | wt | 31.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.48× (z +8.5) | — |
| [[C32 (line)]] | wt | 32.0 | 0 | 1 | — | [[Pralsetinib (drug)]] 5 µM 0.133× (z -8.5) |
| [[H4 (line)]] | wt | 54.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0878× (z -18.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 74.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -10.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.320× (z -10.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 60.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -13.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 49.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.9) | — |
| [[SW48 (line)]] | wt | 52.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -11.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 38.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12050), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM11]] | +0.74 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[C16orf91]] | +0.74 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[YIPF5]] | +0.73 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SCNM1]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[MRPL55]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[TMEM208]] | +0.68 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[BRPF1]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[MIEF1]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[BFAR]] | +0.66 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[IGBP1]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[NUDT22]] | +0.66 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[EIF1AD]] | +0.65 | +0.50 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPH3]] | -0.61 | -0.34 / -0.67 | both halves | 1e-04 |  |
| [[CCDC50]] | -0.59 | -0.31 / -0.63 | both halves | 2e-04 |  |
| [[MYEF2]] | -0.57 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[HP1BP3]] | -0.56 | -0.27 / -0.61 | both halves | 3e-04 |  |
| [[GNG12]] | -0.56 | -0.33 / -0.63 | both halves | 1e-04 |  |
| [[HMGN1]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[DHFR]] | -0.55 | -0.26 / -0.64 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.1, -9.3); signed map (-11.6, -9.4). **Vector** length 104, 27.0% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.4 | +18.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +19.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +22.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.9 | +3.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -9.1 | -21.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.9 | -23.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.2 | -16.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -5.1 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -1.7 | -1.9 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | metal regulatory transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,809,574-37,859,592 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Reactome | 8 pathways, smallest: Response to metal ions; Activation of gene expression by SREBF (SREBP); Regulation of cholesterol biosynthesis by SREBP (SREBF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14872](https://www.uniprot.org/uniprotkb/Q14872) (Metal regulatory transcription factor 1):

> Zinc-dependent transcriptional regulator of cellular adaption to conditions of exposure to heavy metals. Binds to metal responsive elements (MRE) in promoters and activates the transcription of metallothionein genes like metallothionein-2/MT2A. Also regulates the expression of metalloproteases in response to intracellular zinc and functions as a catabolic regulator of cartilages (By similarity).

**Summary**, from NCBI Gene [4520](https://www.ncbi.nlm.nih.gov/gene/4520):

> This gene encodes a transcription factor that induces expression of metallothioneins and other genes involved in metal homeostasis in response to heavy metals such as cadmium, zinc, copper, and silver. The protein is a nucleocytoplasmic shuttling protein that accumulates in the nucleus upon heavy metal exposure and binds to promoters containing a metal-responsive element (MRE). [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7428) · Entrez [4520](https://www.ncbi.nlm.nih.gov/gene/4520) · UniProt [Q14872](https://www.uniprot.org/uniprotkb/Q14872) · Ensembl [ENSG00000188786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188786)

## Data

Gene col 12050: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12050); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12050, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12050]; `tensor/DDL_lfc|DDL_z.npy` [12050]; `embed/gene_vectors.npy` [12050]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12050 or target_col == 12050). Every well: [[MTF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
