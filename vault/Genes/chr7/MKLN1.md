---
symbol: "MKLN1"
type: "gene"
col: 4897
ensembl_id: "ENSG00000128585"
name: "muskelin 1"
location: "7q32.3"
module: 26
arm: "+"
pooled_cpm: 461.3
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MKLN1

*muskelin 1* — 7q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.28× (z +20.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.498× (z -17.2, q 0e+00, down in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.583× (z -13.3, q 4e-38, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (69 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 31 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02615]] (+0.67, fdr 6e-05), [[CDNF]] (+0.66, fdr 1e-04), [[TLK2]] (+0.62, fdr 3e-05); moves opposite to [[MIER2]] (-0.58, fdr 4e-05), [[TAF1A]] (-0.54, fdr 3e-05), [[AP1M1]] (-0.52, fdr 2e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4897.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.28×** | +20.2 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +15.8 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.74×** | +13.7 | 3e-40 | 47/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.74×** | +13.6 | 9e-40 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.21×** | +10.0 | 2e-21 | 47/49 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +9.7 | 4e-20 | 46/48 (SW480, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.33×** | +7.0 | 2e-10 | 32/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +6.9 | 3e-10 | 27/48 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.28×** | +6.1 | 6e-08 | 28/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +5.9 | 2e-07 | 32/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.9 | 2e-07 | 36/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +5.2 | 1e-05 | 26/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.21×** | +4.4 | 6e-04 | 24/47 (SW48, BT-474, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.21×** | +4.3 | 6e-04 | 24/48 (PANC-1, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +4.3 | 6e-04 | 21/48 (PANC-1, LS 180, …) | rises with dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.17× | +3.6 | 0.013 | 7/48 (A498, LS 180, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.037 | 12/48 (A498, A-172, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.0 | 0.060 | 13/49 (C-33 A, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4897.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.498×** | -17.2 | 0e+00 | 49/49 (NCI-H23, HCT15, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.488×** | -17.0 | 0e+00 | 42/44 (NCI-H23, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.583×** | -13.3 | 4e-38 | 47/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.621×** | -11.8 | 8e-30 | 46/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -10.4 | 2e-23 | 45/47 (CFPAC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.705×** | -8.6 | 6e-16 | 43/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.741×** | -7.4 | 1e-11 | 43/48 (RPMI-7951, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.792×** | -5.8 | 6e-07 | 33/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.849× | -4.1 | 0.003 | 17/48 (HOP62, SW480, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.874× | -3.4 | 0.045 | 12/48 (NCI-H1573, H4, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.876× | -3.3 | 0.050 | 5/48 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.879× | -3.2 | 0.063 | 9/47 (SW 1271, HepG2/C3A, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4897. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 540 | 11 (3 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.32× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -13.6) |
| [[PANC-1 (line)]] | alt | 359 | 11 (3 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +30.7) | [[Dinaciclib (drug)]] 0.5 µM 0.520× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.630× (z -10.3) |
| [[SW480 (line)]] | alt | 362 | 8 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +24.3) | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -16.0) |
| [[BT-474 (line)]] | alt | 335 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.44× (z +20.9) | — |
| [[HOP62 (line)]] | alt | 423 | 6 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.48× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.443× (z -14.3) |
| [[KATO III (line)]] | alt | 375 | 6 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.13× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.598× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 545 | 4 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +15.4) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.542× (z -13.8) |
| [[SW 900 (line)]] | alt | 569 | 4 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.482× (z -11.2) |
| [[HT-29 (line)]] | alt | 392 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.540× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.552× (z -10.6) |
| [[LoVo (line)]] | wt | 422 | 7 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +25.1) | [[Dinaciclib (drug)]] 5 µM 0.585× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 440 | 5 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.415× (z -13.6) |
| [[NCI-H23 (line)]] | alt | 602 | 6 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.592× (z -10.4) |
| [[COLO 205 (line)]] | alt | 316 | 7 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.17× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.498× (z -11.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 494 | 5 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -9.3) |
| [[LS 180 (line)]] | wt | 352 | 6 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.50× (z +20.5) | [[Dinaciclib (drug)]] 0.5 µM 0.500× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.531× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 436 | 5 (1 ⚠) | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.01× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -12.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 693 | 4 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +16.4) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.509× (z -10.3) |
| [[A-427 (line)]] | wt | 279 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.556× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 1,216 | 2 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.83× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -10.9) |
| [[HS-578T (line)]] | alt | 395 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.472× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 266 | 4 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.93× (z +19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.86× (z +19.3) | [[Panobinostat (drug)]] 0.5 µM 0.478× (z -13.5) |
| [[NCI-H2347 (line)]] | alt | 456 | 2 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -17.9) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 460 | 5 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.23× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -12.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 669 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.69× (z +9.2) ⚠ cell-cycle shift, explains ~11% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.71× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.536× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 419 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.62× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.390× (z -16.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.509× (z -12.0) |
| [[NCI-H2030 (line)]] | alt | 751 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.448× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 473 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -10.9) |
| [[A-172 (line)]] | wt | 208 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -19.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 513 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -10.2) |
| [[H4 (line)]] | wt | 476 | 2 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.438× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 552 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.397× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.496× (z -12.2) |
| [[Panc 03.27 (line)]] | alt | 371 | 2 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.488× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.607× (z -9.2) |
| [[SNU-423 (line)]] | alt | 343 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.509× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 598 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -18.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.480× (z -10.8) |
| [[C-33 A (line)]] | alt | 369 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -10.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 476 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.572× (z -8.8) |
| [[J82 (line)]] | alt | 299 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -13.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 436 | 1 (1 ⚠) | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.529× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.574× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 387 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -14.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 630 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 394 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.577× (z -9.0) |
| [[AN3 CA (line)]] | alt | 730 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.385× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 348 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.0) | — |
| [[CHP-212 (line)]] | wt | 412 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.43× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 498 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +8.6) | — |
| [[NCI-H2122 (line)]] | alt | 458 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 511 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 552 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 465 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 602 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4897), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 31 of them with an alert (⚠; 31 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02615]] | +0.67 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[CDNF]] | +0.66 | +0.36 / +0.35 | both halves | 1e-04 |  |
| [[TLK2]] | +0.62 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[WDFY3]] | +0.62 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[DPH6-DT]] | +0.62 | +0.21 / +0.45 | both halves | 6e-04 |  |
| [[CCDC90B-AS1]] | +0.61 | +0.13 / +0.52 | ⚠ one half (not replicated) | 0.002 |  |
| [[LINC01762]] | +0.61 | +0.26 / +0.37 | both halves | 3e-04 |  |
| [[CCDC30]] | +0.60 | +0.20 / +0.40 | ⚠ not reproduced | 7e-04 |  |
| [[KDM6A]] | +0.60 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[TAFA2]] | +0.60 | +0.21 / +0.42 | both halves | 6e-04 |  |
| [[APPBP2-DT]] | +0.60 | +0.37 / +0.24 | both halves | 4e-04 |  |
| [[PDC-AS1]] | +0.59 | +0.36 / +0.41 | both halves | 9e-05 |  |
| [[AHI1-DT]] | +0.59 | +0.28 / +0.38 | both halves | 3e-04 |  |
| [[MAMDC2-AS1]] | +0.59 | +0.30 / +0.41 | both halves | 2e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER2]] | -0.58 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[TAF1A]] | -0.54 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[AP1M1]] | -0.52 | -0.30 / -0.35 | both halves | 2e-04 |  |
| [[NANS]] | -0.52 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[KLHL26]] | -0.51 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[GPSM1]] | -0.51 | -0.36 / -0.38 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises MKLN1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.3, 17.6); signed map (31.9, -8.5). **Vector** length 101, 40.9% of its response variance represented; |z| ≥ 3 in 1,474 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.6 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +8.8 | +3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.2 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.5 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.0 | -1.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +3.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.8 | -13.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.7 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.6 | -11.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -4.7 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.5 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.7 | +0.2 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -2.9 | -1.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.8 | +0.9 |
|  | [[Daidzin (drug)]] 5 µM |  | -2.7 | -0.5 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -2.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | muskelin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.3 — chr7:131,110,096-131,496,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TWA2 |
| Gene groups (HGNC) | CTLH complex subunits |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL63](https://www.uniprot.org/uniprotkb/Q9UL63) (Muskelin):

> Component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. Required for internalization of the GABA receptor GABRA1 from the cell membrane via endosomes and subsequent GABRA1 degradation (By similarity). Acts as a mediator of cell spreading and cytoskeletal responses to the extracellular matrix component THBS1.

**Summary**, from NCBI Gene [4289](https://www.ncbi.nlm.nih.gov/gene/4289):

> Muskelin is an intracellular protein that acts as a mediator of cell spreading and cytoskeletal responses to the extracellular matrix component thrombospondin I (MIM 188060) (Adams et al., 1998 [PubMed 9724633]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:7109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7109) · Entrez [4289](https://www.ncbi.nlm.nih.gov/gene/4289) · UniProt [Q9UL63](https://www.uniprot.org/uniprotkb/Q9UL63) · Ensembl [ENSG00000128585](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128585)

## Data

Gene col 4897: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4897); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4897, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4897]; `tensor/DDL_lfc|DDL_z.npy` [4897]; `embed/gene_vectors.npy` [4897]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4897 or target_col == 4897). Every well: [[MKLN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKLN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
