---
symbol: "ACOT7"
type: "gene"
col: 1775
ensembl_id: "ENSG00000097021"
name: "acyl-CoA thioesterase 7"
location: "1p36.31"
module: 195
arm: "+"
pooled_cpm: 34.91
n_lines_expressing: 48
n_dd_up: 32
n_dd_down: 15
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/195"]
generated_by: "tahoemap"
---

# ACOT7

*acyl-CoA thioesterase 7* — 1p36.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (20 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.52× (z +36.7, q 0e+00, up in 46 of 46 measured lines) ⚠ position correction uncertain. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 3.27× (z +25.4, q 0e+00, up in 45 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.667× (z -8.4, q 3e-14, down in 26 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NIBAN2]] (+0.72, fdr 7e-06), [[PLXNA1]] (+0.69, fdr 7e-06), [[ASAP2]] (+0.67, fdr 7e-06); moves opposite to [[DNAJC27]] (-0.64, fdr 1e-05), [[ZNF226]] (-0.63, fdr 1e-05), [[RAB9A]] (-0.61, fdr 1e-05).
> It is in [[Module 195]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ST3GAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 26 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ position correction uncertain | **5.52×** | +36.7 | 0e+00 | 46/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ position correction uncertain | **4.61×** | +27.1 | 0e+00 | 45/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **3.27×** | +25.4 | 0e+00 | 45/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +18.7 | 0e+00 | 34/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.12×** | +16.2 | 0e+00 | 43/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.13×** | +15.7 | 0e+00 | 31/39 (PANC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.07×** | +15.6 | 0e+00 | 33/42 (HOP62, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ position correction uncertain | **2.00×** | +14.9 | 0e+00 | 43/46 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +14.0 | 1e-42 | 39/46 (SW480, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.96×** | +13.4 | 4e-39 | 33/42 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.81×** | +12.0 | 2e-31 | 35/46 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.94×** | +11.8 | 3e-30 | 39/46 (PANC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.58×** | +9.1 | 4e-18 | 38/46 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.50×** | +8.7 | 1e-16 | 35/45 (MIA PaCa-2, NCI-H460, …) | all doses, flat |  |
| [[Peretinoin (drug)]] 5 µM | ⚠ position correction uncertain | **1.50×** | +8.4 | 1e-15 | 30/45 (MIA PaCa-2, A-427, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.58×** | +8.1 | 2e-14 | 32/45 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +7.3 | 1e-11 | 28/46 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +6.7 | 6e-10 | 24/46 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.20×** | +3.8 | 0.003 | 11/46 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +3.5 | 0.008 | 4/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.028 | 9/44 (hTERT-HPNE, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.044 | 11/46 (BT-474, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.051 | 11/45 (A549, NCI-H2030, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.14× | +2.8 | 0.084 | 11/46 (Hs 766T, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.667×** | -8.4 | 3e-14 | 26/45 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.650×** | -8.3 | 4e-14 | 28/46 (SK-MEL-2, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.745×** | -6.8 | 2e-09 | 24/46 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.738×** | -6.5 | 9e-09 | 22/45 (C32, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.810×** | -6.3 | 3e-08 | 22/46 (C32, SW48, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.739×** | -6.2 | 4e-08 | 21/45 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.724×** | -6.2 | 4e-08 | 20/46 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.776×** | -5.9 | 3e-07 | 23/46 (SK-MEL-2, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.776×** | -5.4 | 3e-06 | 21/46 (SK-MEL-2, Panc 03.27, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.841× | -5.3 | 8e-06 | 20/46 (Hs 766T, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.774×** | -5.1 | 2e-05 | 19/46 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.794×** | -5.0 | 3e-05 | 19/46 (SK-MEL-2, C32, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.797×** | -4.6 | 2e-04 | 17/46 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.857× | -4.6 | 2e-04 | 17/46 (SW48, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 0.876× | -4.0 | 0.002 | 10/46 (SW 1088, AN3 CA, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.821×** | -3.9 | 0.003 | 19/45 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.664×** | -3.2 | 0.042 | 9/46 (SK-MEL-2, C32, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 76.9 | 1 | 9 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +11.2) | [[Cobimetinib (drug)]] 0.5 µM 0.295× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 95.3 | 1 (1 ⚠) | 9 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.34× (z +9.7) ⚠ position correction uncertain | [[Trametinib (drug)]] 5 µM 0.357× (z -11.7) |
| [[PANC-1 (line)]] | alt | 31.4 | 7 (4 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.04× (z +17.2) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.93× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 29.3 | 9 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.08× (z +17.7) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 4.16× (z +14.0) | — |
| [[J82 (line)]] | alt | 54.9 | 8 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.20× (z +14.9) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.78× (z +10.6) | — |
| [[NCI-H460 (line)]] | wt | 22.0 | 8 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +19.2) | — |
| [[A498 (line)]] | wt | 16.5 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +12.3) | — |
| [[A549 (line)]] | wt | 23.0 | 6 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +15.5) | — |
| [[HOP62 (line)]] | alt | 34.3 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.10× (z +14.3) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 3.23× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 5 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.79× (z +12.5) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 67.0 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +11.8) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.76× (z +10.2) | [[Adagrasib (drug)]] 0.05 µM 0.651× (z -14.6) ⚠ position not correctable |
| [[HEC-1-A (line)]] | alt | 41.1 | 3 (2 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.92× (z +10.6) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +9.1) | [[Cobimetinib (drug)]] 0.5 µM 0.382× (z -9.5) |
| [[Hs 766T (line)]] | wt | 36.1 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.78× (z +12.2) ⚠ position correction uncertain | [[Selinexor (drug)]] 5 µM 0.326× (z -11.0) ⚠ cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 23.5 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.5) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[HT-29 (line)]] | alt | 11.3 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +12.1) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 6.73× (z +9.7) | — |
| [[RKO (line)]] | wt | 34.7 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.53× (z +13.1) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +11.7) | — |
| [[SW48 (line)]] | wt | 108 | 0 | 4 | — | [[Cobimetinib (drug)]] 5 µM 0.266× (z -9.6) |
| [[A-172 (line)]] | wt | 37.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 23.9 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.43× (z +12.2) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 4.52× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.87× (z +11.4) ⚠ position correction uncertain | — |
| [[LS 180 (line)]] | wt | 31.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +16.1) | — |
| [[NCI-H2030 (line)]] | alt | 84.4 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +11.9) ⚠ position correction uncertain | — |
| [[NCI-H23 (line)]] | alt | 49.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.07× (z +9.8) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 2.69× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -8.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SW1417 (line)]] | alt | 26.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.19× (z +14.1) ⚠ position correction uncertain · without an alert: [[Belinostat (drug)]] 5 µM 4.71× (z +11.0) | — |
| [[H4 (line)]] | wt | 21.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.62× (z +10.4) ⚠ position correction uncertain | — |
| [[HepG2_C3A (line)]] | wt | 42.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.75× (z +10.9) ⚠ position correction uncertain | — |
| [[hTERT-HPNE (line)]] | wt | 11.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.48× (z +10.6) | — |
| [[KATO III (line)]] | alt | 21.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.62× (z +10.9) ⚠ position correction uncertain | — |
| [[LoVo (line)]] | wt | 29.0 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.69× (z +10.9) ⚠ position correction uncertain · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +10.5) ⚠ position correction uncertain | — |
| [[RPMI-7951 (line)]] | alt | 38.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +10.0) ⚠ position correction uncertain | — |
| [[SNU-423 (line)]] | alt | 20.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.64× (z +11.1) ⚠ position correction uncertain | — |
| [[AN3 CA (line)]] | alt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.61× (z +9.1) ⚠ position correction uncertain | — |
| [[HCT15 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.95× (z +11.8) ⚠ position correction uncertain | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.51× (z +10.8) ⚠ position correction uncertain | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.73× (z +11.0) ⚠ position correction uncertain | — |
| [[SNU-1 (line)]] | wt | 50.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.74× (z +10.0) ⚠ position correction uncertain | — |
| [[SW 900 (line)]] | alt | 19.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.19× (z +10.9) ⚠ position correction uncertain | — |
| [[A-427 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NIBAN2]] | +0.72 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[PLXNA1]] | +0.69 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[GATAD2A]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[CAP1]] | +0.66 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RAP1GAP2]] | +0.66 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SH3TC2]] | +0.65 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MPRIP]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[BCR]] | +0.64 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[VAV2]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[DOCK9]] | +0.63 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC27]] | -0.64 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.63 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.61 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[THAP6]] | -0.60 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[PHC3]] | -0.60 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZC3H6]] | -0.60 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CDKN1B]] | -0.60 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CLK4]] | -0.60 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[LRRC27]] | -0.60 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[YY1AP1]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[REL]] | -0.59 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[XPA]] | -0.59 | -0.60 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ST3GAL1]] | B | ST3GAL1 activity lowers ACOT7's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 2.29× higher at baseline in the lines without ST3GAL1 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[PLXNA2]] | B | PLXNA2 activity lowers ACOT7's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.67× higher at baseline in the lines without PLXNA2 | 0.007 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[MICAL2]] | B | MICAL2 activity lowers ACOT7's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.01× higher at baseline in the lines without MICAL2 | 0.008 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[MAP2K1]] | B | MAP2K1 activity raises ACOT7's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.7% of all compounds | 0.025 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TBXAS1]] | B | TBXAS1 activity lowers ACOT7's level | lines that do not express TBXAS1 (8) vs lines expressing it (42) | 1.74× higher at baseline in the lines without TBXAS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: OSBPL7, PYROXD2, SESTD1; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises ACOT7's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 195]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.6, 5.4); signed map (-11.4, 41.6). **Vector** length 112, 32.2% of its response variance represented; |z| ≥ 3 in 1,428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +8.7 | +15.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +8.4 | +15.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +7.0 | +13.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.6 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +14.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +6.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +7.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.5 | -8.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -5.4 | -8.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.4 | -6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.4 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.2 | -5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.1 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA thioesterase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.31 — chr1:6,264,269-6,393,767 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BACH, ACH1, ACT, CTE-II, LACH1, MGC1126, hBACH |
| Gene groups (HGNC) | Acyl-CoA thioesterases; Thioester hydrolases |
| Reactome | 3 pathways, smallest: Mitochondrial Fatty Acid Beta-Oxidation; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [O00154](https://www.uniprot.org/uniprotkb/O00154) (Cytosolic acyl coenzyme A thioester hydrolase):

> Catalyzes the hydrolysis of acyl-CoAs into free fatty acids and coenzyme A (CoASH), regulating their respective intracellular levels. Preferentially hydrolyzes palmitoyl-CoA, but has a broad specificity acting on other fatty acyl-CoAs with chain-lengths of C8-C18. May play an important physiological function in brain.

**Summary**, from NCBI Gene [11332](https://www.ncbi.nlm.nih.gov/gene/11332):

> This gene encodes a member of the acyl coenzyme family. The encoded protein hydrolyzes the CoA thioester of palmitoyl-CoA and other long-chain fatty acids. Decreased expression of this gene may be associated with mesial temporal lobe epilepsy. Alternatively spliced transcript variants encoding distinct isoforms with different subcellular locations have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24157) · Entrez [11332](https://www.ncbi.nlm.nih.gov/gene/11332) · UniProt [O00154](https://www.uniprot.org/uniprotkb/O00154) · Ensembl [ENSG00000097021](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000097021)

## Data

Gene col 1775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1775); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1775]; `tensor/DDL_lfc|DDL_z.npy` [1775]; `embed/gene_vectors.npy` [1775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1775 or target_col == 1775). Every well: [[ACOT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
