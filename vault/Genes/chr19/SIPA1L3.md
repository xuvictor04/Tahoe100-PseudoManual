---
symbol: "SIPA1L3"
type: "gene"
col: 2659
ensembl_id: "ENSG00000105738"
name: "signal induced proliferation associated 1 like 3"
location: "19q13.13-q13.2"
module: 13
arm: "+"
pooled_cpm: 302.6
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 18
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# SIPA1L3

*signal induced proliferation associated 1 like 3* — 19q13.13-q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.50× (z +10.6, q 1e-23, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.521× (z -17.0, q 0e+00, down in 36 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.688× (z -13.8, q 4e-41, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM158]] (+0.63, fdr 7e-06), [[SAMD3]] (+0.59, fdr 1e-05), [[SHANK1]] (+0.59, fdr 1e-05); moves opposite to [[C1RL]] (-0.56, fdr 2e-05), [[MGST1]] (-0.51, fdr 4e-05), [[ABHD4]] (-0.51, fdr 2e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2659.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +10.6 | 1e-23 | 32/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +8.8 | 5e-16 | 31/47 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +8.0 | 2e-13 | 27/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.099 | 8/47 (CFPAC-1, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.14× | +3.3 | 0.099 | 18/47 (NCI-H1792, RKO, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.13× | +3.1 | 0.15 | 13/48 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.15 | 11/47 (C32, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 20 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2659.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.521×** | -17.0 | 0e+00 | 36/48 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -15.2 | 0e+00 | 30/43 (HEC-1-A, A549, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.547×** | -14.5 | 1e-45 | 36/44 (A549, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -13.8 | 4e-41 | 30/48 (LOX-IMVI, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.676×** | -10.2 | 2e-22 | 37/47 (LOX-IMVI, HOP62, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.701×** | -8.9 | 5e-17 | 33/46 (HOP62, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -8.5 | 2e-15 | 31/47 (LOX-IMVI, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.727×** | -8.3 | 8e-15 | 35/47 (PANC-1, SW1417, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.722×** | -8.2 | 2e-14 | 27/46 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.790×** | -6.2 | 4e-08 | 24/47 (LOX-IMVI, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.793×** | -5.7 | 6e-07 | 27/47 (LOX-IMVI, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.804×** | -5.7 | 7e-07 | 24/47 (HT-29, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.828×** | -4.7 | 1e-04 | 22/47 (HOP62, HS-578T, …) | rises with dose | composition shift |
| [[Budesonide (drug)]] 0.05 µM |  | 0.844× | -4.4 | 4e-04 | 23/47 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.840× | -4.4 | 5e-04 | 20/47 (LOX-IMVI, J82, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.879× | -4.1 | 0.001 | 18/47 (HEC-1-A, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.855× | -4.1 | 0.001 | 19/48 (J82, HEC-1-A, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.811×** | -3.9 | 0.003 | 22/46 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.860× | -3.6 | 0.007 | 20/47 (HEC-1-A, Hs 766T, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.877× | -3.4 | 0.014 | 20/47 (J82, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.785×** | -3.3 | 0.021 | 21/48 (HS-578T, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.883× | -3.2 | 0.025 | 15/47 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.885× | -3.2 | 0.027 | 18/48 (HEC-1-A, J82, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2659. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 1,472 | 0 | 37 (15 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0788× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -16.2) |
| [[J82 (line)]] | alt | 477 | 0 | 27 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -22.4) |
| [[LOX-IMVI (line)]] | wt | 636 | 0 | 27 (15 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -29.6) |
| [[HEC-1-A (line)]] | alt | 1,113 | 0 | 25 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -28.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -21.4) |
| [[hTERT-HPNE (line)]] | wt | 578 | 0 | 20 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 254 | 0 | 19 (11 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.562× (z -24.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -12.4) |
| [[A-172 (line)]] | wt | 524 | 0 | 15 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -21.9) |
| [[Hs 766T (line)]] | wt | 263 | 0 | 15 (3 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.303× (z -12.1) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.398× (z -11.0) |
| [[HS-578T (line)]] | alt | 314 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -18.0) |
| [[A549 (line)]] | wt | 658 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -26.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -16.1) |
| [[PANC-1 (line)]] | alt | 253 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.270× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.485× (z -12.3) |
| [[KATO III (line)]] | alt | 218 | 5 (5 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +26.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.429× (z -13.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 274 | 5 (5 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Auranofin (drug)]] 5 µM 0.540× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 273 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -12.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.431× (z -9.2) |
| [[HT-29 (line)]] | alt | 370 | 1 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +16.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.265× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.426× (z -12.8) |
| [[SW480 (line)]] | alt | 201 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -21.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 165 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +17.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -12.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 281 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.238× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 279 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.4) |
| [[C-33 A (line)]] | alt | 168 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 162 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -9.1) ⚠ cell-cycle shift, explains ~9% of this change |
| [[LoVo (line)]] | wt | 154 | 1 (1 ⚠) | 3 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.86× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 5 µM 0.425× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.602× (z -8.7) |
| [[SW1417 (line)]] | alt | 199 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.396× (z -12.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 314 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -14.1) |
| [[COLO 205 (line)]] | alt | 184 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.467× (z -9.7) |
| [[LS 180 (line)]] | wt | 166 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 114 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.55× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 93.5 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.02× (z +9.6) | [[Harringtonine (drug)]] 5 µM 0.508× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[RKO (line)]] | wt | 123 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.37× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 282 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.87× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 104 | 2 (1 ⚠) | 0 | [[Trametinib (drug)]] 0.05 µM 1.96× (z +8.7) | — |
| [[C32 (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -13.3) |
| [[SW48 (line)]] | wt | 191 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -9.0) |
| [[HCT15 (line)]] | alt | 193 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.486× (z -9.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 117 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 104 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 78.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.334× (z -9.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 91.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.13× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0719× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +16.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 150 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 75.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 398 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 245 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2659), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM158]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[SAMD3]] | +0.59 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SHANK1]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 | same gene group |
| [[C2CD2]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[ARHGAP22]] | +0.59 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[INSYN2B]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[ARL4C]] | +0.57 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[ADAMTS6]] | +0.57 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[CALM1]] | +0.57 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[RASA3]] | +0.55 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[NLRP3]] | +0.55 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CD82]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1RL]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MGST1]] | -0.51 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[ABHD4]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[GLUL]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[GSR]] | -0.50 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[FTH1]] | -0.50 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[FBXO7]] | -0.49 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[ADI1]] | -0.49 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[NAXD]] | -0.47 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[SETD7]] | -0.47 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[BEST1]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ROS1]] | -0.46 | -0.40 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SIPA1L3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.446). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.2, 11.7); signed map (15.9, 49.2). **Vector** length 139, 45.3% of its response variance represented; |z| ≥ 3 in 2,008 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.9 | +10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.5 | +8.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.8 | +2.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change | +4.6 | -3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.8 | +1.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +3.6 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[vincristine (drug)]] 5 µM |  | +3.0 | +1.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -6.4 | -3.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -5.9 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -5.9 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.6 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -5.3 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | signal induced proliferation associated 1 like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.13-q13.2 — chr19:37,907,208-38,208,369 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0545, SPAR3 |
| Gene groups (HGNC) | PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O60292](https://www.uniprot.org/uniprotkb/O60292) (Signal-induced proliferation-associated 1-like protein 3):

> Plays a critical role in epithelial cell morphogenesis, polarity, adhesion and cytoskeletal organization in the lens.

**Summary**, from NCBI Gene [23094](https://www.ncbi.nlm.nih.gov/gene/23094):

> This gene belongs to the signal induced proliferation associated 1 family of genes, which encode GTPase-activating proteins specific for the GTP-binding protein Rap1. Rap1 has been implicated in regulation of cell adhesion, cell polarity, and organization of the cytoskeleton. Like other members of the family, the protein encoded by this gene contains RapGAP and PDZ domains. In addition, this protein contains a C-terminal leucine zipper domain. This gene is proposed to function in epithelial …

**Accessions** — [HGNC:23801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23801) · Entrez [23094](https://www.ncbi.nlm.nih.gov/gene/23094) · UniProt [O60292](https://www.uniprot.org/uniprotkb/O60292) · Ensembl [ENSG00000105738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105738)

## Data

Gene col 2659: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2659); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2659, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2659]; `tensor/DDL_lfc|DDL_z.npy` [2659]; `embed/gene_vectors.npy` [2659]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2659 or target_col == 2659). Every well: [[SIPA1L3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SIPA1L3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
