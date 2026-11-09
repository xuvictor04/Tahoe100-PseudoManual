---
symbol: "RBM26"
type: "gene"
col: 6344
ensembl_id: "ENSG00000139746"
name: "RNA binding motif protein 26"
location: "13q31.1"
module: 213
arm: "+"
pooled_cpm: 199.33
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/213"]
generated_by: "tahoemap"
---

# RBM26

*RNA binding motif protein 26* — 13q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.30× (z +12.4, q 2e-32, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.520× (z -20.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZZZ3]] (+0.71, fdr 1e-05), [[MTREX]] (+0.69, fdr 7e-06), [[ACBD6]] (+0.66, fdr 1e-05); moves opposite to [[HECA]] (-0.66, fdr 1e-05), [[MAP1LC3B]] (-0.62, fdr 2e-05), [[F11R]] (-0.60, fdr 1e-05).
> It is in [[Module 213]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6344.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.30×** | +12.4 | 2e-32 | 44/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.05×** | +10.6 | 6e-24 | 41/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.26×** | +7.5 | 2e-11 | 28/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +6.8 | 2e-09 | 29/48 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +6.5 | 7e-09 | 30/48 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.13× | +5.5 | 4e-06 | 18/48 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.40×** | +5.0 | 5e-05 | 33/47 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 5e-04 | 23/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.13× | +3.8 | 0.008 | 6/48 (HEC-1-A, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 1.09× | +3.8 | 0.008 | 0/48 | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.008 | 19/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.6 | 0.013 | 16/48 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.038 | 12/48 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.040 | 17/48 (AsPC-1, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.07× | +3.3 | 0.040 | 0/48 | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6344.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.520×** | -20.9 | 0e+00 | 48/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.538×** | -19.8 | 0e+00 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -18.3 | 0e+00 | 41/49 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.573×** | -17.8 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.632×** | -14.7 | 0e+00 | 39/48 (C32, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.660×** | -12.8 | 2e-35 | 32/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.683×** | -12.2 | 3e-32 | 40/49 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.705×** | -10.3 | 4e-23 | 30/45 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.752×** | -9.1 | 6e-18 | 40/48 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -8.4 | 2e-15 | 31/50 (NCI-H460, SW48, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.779×** | -8.0 | 9e-14 | 37/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.791×** | -7.2 | 3e-11 | 30/48 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.822×** | -6.3 | 2e-08 | 24/48 (KATO III, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.817×** | -6.2 | 2e-08 | 26/47 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.851× | -5.2 | 9e-06 | 20/48 (RKO, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.899× | -4.8 | 5e-05 | 7/48 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.006 | 20/48 (HT-29, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | 0.892× | -3.5 | 0.013 | 9/47 (HT-29, LoVo, …) | rises with dose |  |
| [[OTS514 (drug)]] 5 µM |  | **0.793×** | -3.4 | 0.016 | 18/46 (NCI-H460, KATO III, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 0.898× | -3.4 | 0.016 | 11/48 (SW 1088, SNU-1, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.900× | -3.4 | 0.020 | 12/47 (HOP62, LoVo, …) | rises with dose | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | 0.865× | -3.3 | 0.023 | 11/48 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6344. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 424 | 2 | 8 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.23× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.383× (z -18.1) |
| [[HEC-1-A (line)]] | alt | 255 | 2 | 7 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.01× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.343× (z -19.6) |
| [[Panc 03.27 (line)]] | alt | 231 | 1 | 8 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.90× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.577× (z -13.4) |
| [[PANC-1 (line)]] | alt | 205 | 3 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +17.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.88× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -15.7) |
| [[RKO (line)]] | wt | 309 | 1 | 8 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.00× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -17.7) |
| [[LoVo (line)]] | wt | 187 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.20× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -17.5) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.586× (z -10.2) |
| [[NCI-H460 (line)]] | wt | 195 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -18.6) |
| [[SW48 (line)]] | wt | 273 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -12.2) |
| [[A549 (line)]] | wt | 136 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +22.0) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.18× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -16.9) |
| [[HCT15 (line)]] | alt | 338 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.460× (z -11.9) |
| [[HOP62 (line)]] | alt | 139 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.405× (z -15.4) |
| [[HT-29 (line)]] | alt | 201 | 1 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.96× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -14.9) |
| [[LOX-IMVI (line)]] | wt | 244 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.337× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 241 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -16.8) |
| [[NCI-H23 (line)]] | alt | 214 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.76× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.274× (z -22.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.467× (z -13.3) |
| [[NCI-H2347 (line)]] | alt | 115 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.84× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.665× (z -9.6) |
| [[A498 (line)]] | wt | 183 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -20.7) |
| [[J82 (line)]] | alt | 243 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.537× (z -16.9) |
| [[KATO III (line)]] | alt | 194 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.414× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 255 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.35× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.304× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -12.1) |
| [[SNU-1 (line)]] | wt | 355 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -13.9) |
| [[A-172 (line)]] | wt | 136 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +14.8) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 1.78× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -13.4) |
| [[A-427 (line)]] | wt | 159 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0518× (z -40.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.429× (z -12.1) |
| [[BT-474 (line)]] | alt | 140 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.7) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 1.96× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.496× (z -9.8) |
| [[CHP-212 (line)]] | wt | 271 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.418× (z -12.1) |
| [[COLO 205 (line)]] | alt | 402 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -10.9) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.555× (z -8.6) |
| [[Hs 766T (line)]] | wt | 250 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.512× (z -11.2) |
| [[LS 180 (line)]] | wt | 204 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -11.1) |
| [[SW1417 (line)]] | alt | 155 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -15.9) |
| [[C32 (line)]] | wt | 200 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.252× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.288× (z -17.1) |
| [[H4 (line)]] | wt | 148 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.381× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.421× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 99.6 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 1.95× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.495× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 197 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.398× (z -12.8) |
| [[AN3 CA (line)]] | alt | 245 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 121 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 100 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.98× (z +9.3) ⚠ unreliable plate only | — |
| [[C-33 A (line)]] | alt | 164 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.490× (z -9.6) |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.393× (z -10.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 116 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.05× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -9.9) |
| [[SHP-77 (line)]] | alt | 169 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.562× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 123 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.284× (z -17.0) |
| [[SNU-423 (line)]] | alt | 146 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.404× (z -13.3) |
| [[SW 1088 (line)]] | alt | 173 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.181× (z -9.2) |
| [[SW 900 (line)]] | alt | 153 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.538× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 237 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 252 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6344), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZZZ3]] | +0.71 | +0.50 / +0.79 | both halves | 1e-05 |  |
| [[MTREX]] | +0.69 | +0.59 / +0.70 | both halves | 7e-06 | pathway: Nuclear RNA decay; STRING 642 |
| [[ACBD6]] | +0.66 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[USP24]] | +0.66 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[LTV1]] | +0.65 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[MRPL1]] | +0.65 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PTBP2]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 | same gene group |
| [[SREK1]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 | same gene group; STRING 460 |
| [[HMG20A]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SHPRH]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DCPS]] | +0.62 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MRPS9]] | +0.62 | +0.51 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HECA]] | -0.66 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[MAP1LC3B]] | -0.62 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[F11R]] | -0.60 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[LINC01128]] | -0.60 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SERINC2]] | -0.60 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[LRP10]] | -0.58 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[RHOC]] | -0.58 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[ORMDL2]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[LRRC8A]] | -0.58 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[PNPLA8]] | -0.57 | -0.36 / -0.67 | both halves | 9e-05 |  |
| [[TMEM184B]] | -0.56 | -0.39 / -0.62 | both halves | 6e-05 |  |
| [[CYTH1]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 213]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.723). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-19.7, 3.0); signed map (7.0, -39.2). **Vector** length 114, 37.7% of its response variance represented; |z| ≥ 3 in 1,290 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.9 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +7.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.6 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.5 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.1 | +10.6 |
|  | [[EX229 (drug)]] 5 µM |  | +4.9 | +3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.7 | +2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.5 | +3.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.0 | -14.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.5 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -4.3 | -3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.6 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q31.1 — chr13:79,311,824-79,406,477 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRO1777, SE70-2, FLJ20957, ZC3H17, ARRS2, PPP1R132; previously C13orf10 |
| Gene groups (HGNC) | Zinc fingers CCCH-type; Protein phosphatase 1 regulatory subunits; RNA binding motif containing |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T8P6](https://www.uniprot.org/uniprotkb/Q5T8P6) (RNA-binding protein 26):

> May be involved in the turnover of nuclear polyadenylated (pA+) RNA.

**Summary**, from NCBI Gene [64062](https://www.ncbi.nlm.nih.gov/gene/64062):

> Enables RNA binding activity. Predicted to be involved in RNA catabolic process. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20327](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20327) · Entrez [64062](https://www.ncbi.nlm.nih.gov/gene/64062) · UniProt [Q5T8P6](https://www.uniprot.org/uniprotkb/Q5T8P6) · Ensembl [ENSG00000139746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139746)

## Data

Gene col 6344: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6344); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6344, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6344]; `tensor/DDL_lfc|DDL_z.npy` [6344]; `embed/gene_vectors.npy` [6344]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6344 or target_col == 6344). Every well: [[RBM26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
