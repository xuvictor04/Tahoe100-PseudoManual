---
symbol: "RNF19A"
type: "gene"
col: 423
ensembl_id: "ENSG00000034677"
name: "ring finger protein 19A, RBR E3 ubiquitin protein ligase"
location: "8q22.2"
module: 33
arm: "-"
pooled_cpm: 206.37
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 21
n_dd_up_clean: 4
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# RNF19A

*ring finger protein 19A, RBR E3 ubiquitin protein ligase* — 8q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.53× (z +11.8, q 1e-29, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.440× (z -21.9, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.05 µM: 0.806× (z -6.0, q 1e-07, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTG1]] (+0.59, fdr 1e-05), [[ANKRD12]] (+0.58, fdr 1e-05), [[SHOC2]] (+0.55, fdr 1e-05); moves opposite to [[DROSHA]] (-0.60, fdr 1e-05), [[GCN1]] (-0.58, fdr 1e-05), [[DFFB]] (-0.57, fdr 4e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[UACA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +11.8 | 1e-29 | 41/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +9.0 | 5e-17 | 25/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.37×** | +8.7 | 4e-16 | 29/48 (BT-474, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +8.3 | 1e-14 | 31/48 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +7.9 | 4e-13 | 31/48 (RKO, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.33×** | +7.6 | 2e-12 | 27/48 (PANC-1, C32, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.22×** | +5.6 | 2e-06 | 23/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.21×** | +5.3 | 7e-06 | 23/48 (C32, PANC-1, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +5.1 | 2e-05 | 28/48 (C32, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +4.5 | 4e-04 | 20/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.17× | +4.4 | 5e-04 | 18/47 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.17× | +4.4 | 5e-04 | 16/48 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.8 | 0.007 | 16/49 (LS 180, RKO, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.14× | +3.5 | 0.022 | 18/47 (HT-29, COLO 205, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.026 | 12/47 (AN3 CA, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.029 | 15/47 (A549, SNU-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Terfenadine (drug)]] 5 µM |  | 1.08× | +3.1 | 0.062 | 2/48 (NCI-H661, SW 1271) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 19 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.440×** | -21.9 | 0e+00 | 41/44 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -18.0 | 0e+00 | 45/49 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.632×** | -11.8 | 1e-29 | 33/45 (Hs 766T, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -11.0 | 4e-26 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.711×** | -9.5 | 4e-19 | 31/48 (AsPC-1, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.717×** | -9.2 | 3e-18 | 30/48 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -8.8 | 1e-16 | 34/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.822×** | -7.7 | 1e-12 | 23/48 (NCI-H1573, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.631×** | -6.7 | 1e-09 | 31/45 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.786×** | -6.7 | 1e-09 | 36/48 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.781×** | -6.5 | 5e-09 | 24/48 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.806×** | -6.0 | 1e-07 | 28/48 (Panc 03.27, NCI-H460, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.682×** | -5.6 | 1e-06 | 29/48 (C32, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.821×** | -5.4 | 2e-06 | 25/48 (LoVo, RKO, …) | two highest doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.687×** | -5.4 | 2e-06 | 34/48 (NCI-H1573, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.818×** | -5.4 | 3e-06 | 26/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.702×** | -5.1 | 9e-06 | 29/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.845× | -4.7 | 9e-05 | 20/48 (C32, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.734×** | -4.5 | 2e-04 | 25/48 (NCI-H460, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.740×** | -4.4 | 3e-04 | 22/48 (NCI-H1792, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.859× | -4.2 | 7e-04 | 21/48 (Panc 03.27, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.765×** | -3.9 | 0.002 | 15/49 (C32, A549, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.013 | 17/49 (SK-MEL-2, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 0.889× | -3.2 | 0.025 | 9/48 (HepG2/C3A, C32, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.897× | -3.0 | 0.050 | 11/48 (Panc 03.27, HepG2/C3A, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.898× | -3.0 | 0.055 | 10/48 (LOX-IMVI, C32, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.903× | -2.8 | 0.083 | 12/48 (Panc 03.27, HepG2/C3A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 414 | 4 (4 ⚠) | 22 (9 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.22× (z +14.2) ⚠ cell-cycle shift, explains ~10% of this change | [[Panobinostat (drug)]] 5 µM 0.310× (z -14.3) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.398× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 367 | 0 | 21 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.421× (z -17.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.429× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 342 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.513× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 278 | 1 (1 ⚠) | 11 (7 ⚠) | [[Harringtonine (drug)]] 5 µM 1.97× (z +8.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.389× (z -12.4) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.438× (z -10.8) |
| [[PANC-1 (line)]] | alt | 154 | 7 (5 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +20.2) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.531× (z -12.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 532 | 4 (1 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 2.30× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.26× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.462× (z -14.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 213 | 2 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +12.5) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -12.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 299 | 4 (4 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.20× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.344× (z -14.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 373 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 262 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -14.4) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 279 | 1 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +10.3) ⚠ cell-cycle shift, explains ~49% of this change | [[Panobinostat (drug)]] 5 µM 0.339× (z -15.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H460 (line)]] | wt | 282 | 4 (3 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 200 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -13.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 220 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -17.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 101 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +20.9) ⚠ cell-cycle shift, explains ~49% of this change | [[Dinaciclib (drug)]] 5 µM 0.403× (z -10.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 356 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +13.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.441× (z -9.2) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 152 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.34× (z +9.1) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.26× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -18.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 325 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.414× (z -8.7) |
| [[Hs 766T (line)]] | wt | 213 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -14.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 259 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -13.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 101 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +10.0) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +8.7) | — |
| [[A498 (line)]] | wt | 162 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -13.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 161 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -14.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 104 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.43× (z +19.4) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1792 (line)]] | alt | 152 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.416× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 147 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.4) ⚠ cell-cycle shift, explains ~49% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.550× (z -9.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 132 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +13.6) ⚠ cell-cycle shift, explains ~49% of this change | [[Dinaciclib (drug)]] 5 µM 0.300× (z -15.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 159 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +11.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +10.7) | — |
| [[A-427 (line)]] | wt | 60.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.00× (z +11.9) | — |
| [[A549 (line)]] | wt | 214 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -18.1) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 167 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.54× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -10.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 137 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 174 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 112 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.12× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.279× (z -15.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 286 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -9.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0567× (z -20.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 139 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.535× (z -9.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -12.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.471× (z -9.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 159 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.461× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.578× (z -8.5) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 219 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*35 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTG1]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.58 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SHOC2]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PIM3]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ACAP1]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[POLR2L]] | +0.54 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[RNF24]] | +0.53 | +0.52 / +0.61 | both halves | 1e-05 | same gene group |
| [[S100A6]] | +0.52 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[MAK]] | +0.52 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[NDUFV2-AS1]] | +0.51 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[HMGCL]] | +0.51 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[FOXC1]] | +0.51 | +0.40 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*65 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DROSHA]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[GCN1]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[DFFB]] | -0.57 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[UTP18]] | -0.56 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[MRPL3]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[NOL10]] | -0.54 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[NSUN2]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[ELAC2]] | -0.54 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[HERC2P3]] | -0.54 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[KAT2A]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[POMT2]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TRRAP]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UACA]] | B | UACA activity lowers RNF19A's level | lines that do not express UACA (5) vs lines expressing it (45) | 1.74× higher at baseline in the lines without UACA | 0.060 | ⚠ within organs, on part of the lines; also absent: IGF2BP2, PNCK, SPTBN5; maybe low, not absent |
| [[HOTAIRM1]] | B | HOTAIRM1 activity lowers RNF19A's level | lines that do not express HOTAIRM1 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without HOTAIRM1 | 0.072 | ⚠ within organs, on part of the lines; also absent: GXYLT2, HOXA5, SOBP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-18.9, -29.7); signed map (-6.6, 10.4). **Vector** length 118, 36.0% of its response variance represented; |z| ≥ 3 in 1,597 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +7.1 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +6.3 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.1 | +0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.7 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +1.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.7 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -7.3 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.1 | -4.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | -5.6 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.6 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 19A, RBR E3 ubiquitin protein ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.2 — chr8:100,257,060-100,336,218 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dorfin, DKFZp566B1346; previously RNF19 |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NV58](https://www.uniprot.org/uniprotkb/Q9NV58) (E3 ubiquitin-protein ligase RNF19A):

> E3 ubiquitin-protein ligase which accepts ubiquitin from E2 ubiquitin-conjugating enzymes UBE2L3 and UBE2L6 in the form of a thioester and then directly transfers the ubiquitin to targeted substrates, such as SNCAIP or CASR. Specifically ubiquitinates pathogenic SOD1 variants, which leads to their proteasomal degradation and to neuronal protection.

**Summary**, from NCBI Gene [25897](https://www.ncbi.nlm.nih.gov/gene/25897):

> This gene encodes a member of the ring between ring fingers (RBR) protein family, and the encoded protein contains two RING-finger motifs and an in between RING fingers motif. This protein is an E3 ubiquitin ligase that is localized to Lewy bodies, and ubiquitylates synphilin-1, which is an interacting protein of alpha synuclein in neurons. The encoded protein may be involved in amyotrophic lateral sclerosis and Parkinson's disease. Alternative splicing results in multiple transcript variants. …

**Accessions** — [HGNC:13432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13432) · Entrez [25897](https://www.ncbi.nlm.nih.gov/gene/25897) · UniProt [Q9NV58](https://www.uniprot.org/uniprotkb/Q9NV58) · Ensembl [ENSG00000034677](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000034677)

## Data

Gene col 423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 423); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 423]; `tensor/DDL_lfc|DDL_z.npy` [423]; `embed/gene_vectors.npy` [423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 423 or target_col == 423). Every well: [[RNF19A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF19A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
