---
symbol: "PUM1"
type: "gene"
col: 5585
ensembl_id: "ENSG00000134644"
name: "pumilio RNA binding family member 1"
location: "1p35.2"
module: 52
arm: "-"
pooled_cpm: 308.51
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# PUM1

*pumilio RNA binding family member 1* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.60× (z +25.7, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.385× (z -24.1, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.673× (z -10.4, q 4e-23, down in 36 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW480 0.238×, SK-MEL-2 0.188×, NCI-H23 0.252×, PANC-1 0.271×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 9 lines (HOP62 0.476×, CFPAC-1 0.514×, SW480 0.621×, SK-MEL-2 0.520×, …); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.289×, NCI-H2347 0.232×, MIA PaCa-2 0.282×, SW480 0.389×, …; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 4 lines (NCI-H23 0.590×, SK-MEL-2 0.589×, Panc 03.27 0.607×, HOP62 0.583×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WAC]] (+0.63, fdr 1e-05), [[PUM2]] (+0.63, fdr 1e-05), [[GPBP1]] (+0.55, fdr 2e-05); moves opposite to [[DPP9]] (-0.64, fdr 4e-05), [[RER1]] (-0.57, fdr 6e-05), [[EVI5L]] (-0.57, fdr 1e-04).
> It sits in the **-** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EPS8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.60×** | +25.7 | 0e+00 | 49/49 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +21.4 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.69×** | +21.1 | 0e+00 | 48/48 (SW480, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +19.6 | 0e+00 | 47/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +17.6 | 0e+00 | 41/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +13.6 | 2e-40 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +13.3 | 2e-38 | 46/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +10.7 | 6e-25 | 38/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +10.0 | 1e-21 | 43/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +8.5 | 2e-15 | 34/48 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +7.3 | 2e-11 | 28/48 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.30×** | +6.9 | 2e-10 | 31/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +5.1 | 2e-05 | 25/48 (HT-29, HCT15, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.1 | 2e-05 | 15/48 (PANC-1, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.8 | 6e-05 | 24/38 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.11× | +3.9 | 0.003 | 8/48 (C-33 A, HepG2/C3A, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.032 | 19/49 (Hs 766T, RKO, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.040 | 17/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.12× | +3.0 | 0.065 | 6/48 (NCI-H2347, HT-29, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5585.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW480 0.238×, SK-MEL-2 0.188×, NCI-H23 0.252×, PANC-1 0.271×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 9 lines (HOP62 0.476×, CFPAC-1 0.514×, SW480 0.621×, SK-MEL-2 0.520×, …); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (NCI-H23 0.289×, NCI-H2347 0.232×, MIA PaCa-2 0.282×, SW480 0.389×, …; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 5 µM in 4 lines (NCI-H23 0.590×, SK-MEL-2 0.589×, Panc 03.27 0.607×, HOP62 0.583×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.385×** | -24.1 | 0e+00 | 44/44 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.423×** | -22.6 | 0e+00 | 48/49 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -14.9 | 0e+00 | 41/45 (NCI-H2347, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.673×** | -10.4 | 4e-23 | 36/48 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.752×** | -7.5 | 9e-12 | 29/48 (NCI-H23, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.844× | -6.3 | 3e-08 | 20/49 (NCI-H23, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.802×** | -5.8 | 6e-07 | 27/48 (NCI-H23, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.825×** | -5.0 | 3e-05 | 26/48 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 0.838× | -4.6 | 2e-04 | 22/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.839× | -4.6 | 2e-04 | 22/48 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | 0.846× | -4.2 | 0.001 | 22/47 (MIA PaCa-2, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.878× | -3.4 | 0.029 | 17/48 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.883× | -3.3 | 0.045 | 4/48 (C-33 A, SW 900, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.884× | -3.2 | 0.048 | 15/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.889× | -3.1 | 0.069 | 11/48 (HEC-1-A, C32, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.920× | -3.1 | 0.069 | 1/48 (RKO) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.849× | -3.1 | 0.073 | 20/47 (CHP-212, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 255 | 14 (4 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.65× (z +27.9) | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -16.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 309 | 12 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.86× (z +28.5) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -26.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 220 | 12 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.03× (z +25.4) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -20.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 269 | 8 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.63× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.476× (z -11.7) |
| [[SW480 (line)]] | alt | 371 | 8 (2 ⚠) | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.80× (z +25.5) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -33.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.621× (z -11.5) |
| [[HT-29 (line)]] | alt | 297 | 9 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.64× (z +21.4) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 413 | 6 (1 ⚠) | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.94× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -27.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.590× (z -11.0) |
| [[LoVo (line)]] | wt | 356 | 7 (2 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +28.6) | [[Dinaciclib (drug)]] 5 µM 0.555× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.634× (z -9.0) |
| [[LS 180 (line)]] | wt | 344 | 8 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.17× (z +27.7) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -19.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 310 | 7 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.39× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -20.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 328 | 7 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 8.65× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.479× (z -12.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 249 | 4 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.30× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.542× (z -10.7) |
| [[SW 900 (line)]] | alt | 241 | 8 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.49× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.501× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 250 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.55× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.393× (z -11.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 330 | 3 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.75× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.514× (z -11.5) |
| [[HS-578T (line)]] | alt | 245 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.432× (z -11.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 299 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +27.8) | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -20.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 350 | 6 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.19× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.284× (z -13.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 492 | 4 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.60× (z +17.5) | [[Dinaciclib (drug)]] 5 µM 0.234× (z -25.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 241 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -15.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 418 | 3 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 6.62× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.232× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.588× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 300 | 3 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 8.62× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.188× (z -27.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.520× (z -11.3) |
| [[SNU-423 (line)]] | alt | 271 | 6 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -11.6) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 437 | 7 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 5.21× (z +16.9) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -22.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 202 | 5 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -14.2) ⚠ cell-cycle shift, explains ~13% of this change |
| [[COLO 205 (line)]] | alt | 338 | 7 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.5× (z +20.3) | [[Dinaciclib (drug)]] 0.5 µM 0.483× (z -11.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 192 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +16.5) | [[Dinaciclib (drug)]] 5 µM 0.263× (z -18.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 364 | 3 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.40× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -21.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 241 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.46× (z +15.4) | — |
| [[Hs 766T (line)]] | wt | 267 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.84× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.478× (z -11.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 270 | 6 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.94× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.516× (z -9.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 329 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.9× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -13.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 131 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.7) | [[Dinaciclib (drug)]] 0.5 µM 0.523× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 286 | 6 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.44× (z +14.7) | — |
| [[A498 (line)]] | wt | 189 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.400× (z -14.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 440 | 4 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.27× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -19.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 361 | 4 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 8.37× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -18.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 290 | 4 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.08× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -12.3) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 346 | 3 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -21.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 412 | 3 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.21× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.143× (z -16.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 360 | 4 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.74× (z +16.4) | [[Dinaciclib (drug)]] 5 µM 0.300× (z -20.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 419 | 3 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 7.48× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -12.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 271 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 9.59× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -13.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 403 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.62× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 540 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -10.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 216 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 286 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -8.6) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 211 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +9.3) | — |
| [[NCI-H2122 (line)]] | alt | 286 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 329 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WAC]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 | STRING 527 |
| [[PUM2]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 | same gene group; STRING 721 |
| [[GPBP1]] | +0.55 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[DHX36]] | +0.55 | +0.32 / +0.58 | both halves | 2e-04 | STRING 410 |
| [[MKLN1]] | +0.54 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[ASXL1]] | +0.54 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[RAF1]] | +0.53 | +0.59 / +0.35 | both halves | 1e-04 |  |
| [[TLK2]] | +0.53 | +0.56 / +0.36 | both halves | 1e-04 | STRING 466 |
| [[MED13L]] | +0.53 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[ZNF207]] | +0.52 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[CNOT4]] | +0.52 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[CTNNB1]] | +0.52 | +0.43 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.64 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[RER1]] | -0.57 | -0.38 / -0.58 | both halves | 6e-05 |  |
| [[EVI5L]] | -0.57 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[OSBPL2]] | -0.53 | -0.42 / -0.57 | both halves | 4e-05 |  |
| [[GOLGA3]] | -0.52 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[YKT6]] | -0.52 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[ATP6V0A2]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[WIPI1]] | -0.52 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[TPD52L2]] | -0.51 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[ODF2]] | -0.51 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[SZT2]] | -0.51 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[DAP]] | -0.50 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8]] | B | EPS8 activity lowers PUM1's level | lines that do not express EPS8 (5) vs lines expressing it (45) | 1.40× higher at baseline in the lines without EPS8 | 0.048 | ⚠ within organs, on part of the lines; also absent: ASPH, SCML1, PTPRK; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PUM1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-17.8, 1.6); signed map (13.1, -34.4). **Vector** length 94.0, 37.0% of its response variance represented; |z| ≥ 3 in 1,500 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +3.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.0 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | +7.4 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.2 | +10.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.6 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.3 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.3 | -0.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.6 | -4.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | +13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.2 | -7.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | -3.6 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | +13.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | +1.9 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.4 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | +0.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | pumilio RNA binding family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:30,931,506-31,065,991 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PUMH1, KIAA0099 |
| Gene groups (HGNC) | Pumilio homology domain containing; Small nucleolar RNA protein coding host genes |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14671](https://www.uniprot.org/uniprotkb/Q14671) (Pumilio homolog 1):

> Sequence-specific RNA-binding protein that acts as a post-transcriptional repressor by binding the 3'-UTR of mRNA targets. Binds to an RNA consensus sequence, the Pumilio Response Element (PRE), 5'-UGUANAUA-3', that is related to the Nanos Response Element (NRE). Mediates post-transcriptional repression of transcripts via different mechanisms: acts via direct recruitment of the CCR4-POP2-NOT deadenylase leading to translational inhibition and mRNA degradation. Also mediates …

**Summary**, from NCBI Gene [9698](https://www.ncbi.nlm.nih.gov/gene/9698):

> This gene encodes a member of the PUF family, evolutionarily conserved RNA-binding proteins related to the Pumilio proteins of Drosophila and the fem-3 mRNA binding factor proteins of C. elegans. The encoded protein contains a sequence-specific RNA binding domain comprised of eight repeats and N- and C-terminal flanking regions, and serves as a translational regulator of specific mRNAs by binding to their 3' untranslated regions. The evolutionarily conserved function of the encoded protein in …

**Accessions** — [HGNC:14957](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14957) · Entrez [9698](https://www.ncbi.nlm.nih.gov/gene/9698) · UniProt [Q14671](https://www.uniprot.org/uniprotkb/Q14671) · Ensembl [ENSG00000134644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134644)

## Data

Gene col 5585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5585); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5585]; `tensor/DDL_lfc|DDL_z.npy` [5585]; `embed/gene_vectors.npy` [5585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5585 or target_col == 5585). Every well: [[PUM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PUM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
