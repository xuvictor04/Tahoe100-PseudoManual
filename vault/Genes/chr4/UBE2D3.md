---
symbol: "UBE2D3"
type: "gene"
col: 3045
ensembl_id: "ENSG00000109332"
name: "ubiquitin conjugating enzyme E2 D3"
location: "4q24"
module: 23
arm: "+"
pooled_cpm: 323.52
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# UBE2D3

*ubiquitin conjugating enzyme E2 D3* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.96× (z +14.1, q 1e-42, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.474× (z -18.5, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (64 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 37 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YTHDF3]] (+0.62, fdr 7e-06), [[ELOC]] (+0.60, fdr 1e-05), [[ZFAND2A-DT]] (+0.60, fdr 1e-04); moves opposite to [[ACTL6A]] (-0.49, fdr 3e-04), [[POLD2]] (-0.47, fdr 2e-04), [[IPO9]] (-0.46, fdr 6e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3045.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.96×** | +14.1 | 1e-42 | 48/49 (LoVo, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +13.2 | 2e-37 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +12.9 | 8e-36 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.35×** | +11.1 | 1e-26 | 45/48 (LoVo, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +9.0 | 4e-17 | 40/48 (BT-474, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +8.9 | 7e-17 | 38/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +7.7 | 1e-12 | 36/48 (HT-29, LS 180, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +7.4 | 1e-11 | 37/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +7.2 | 3e-11 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +6.2 | 4e-08 | 29/48 (HT-29, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.26×** | +5.7 | 5e-07 | 24/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.5 | 4e-04 | 25/38 (NCI-H1573, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 1.12× | +3.9 | 0.004 | 17/48 (A-172, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.17× | +3.9 | 0.004 | 22/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.004 | 21/48 (HT-29, C-33 A, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +3.6 | 0.010 | 7/49 (CFPAC-1, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.027 | 22/49 (HT-29, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.15× | +3.2 | 0.039 | 10/49 (NCI-H460, HOP62, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3045.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.474×** | -18.5 | 0e+00 | 48/48 (HT-29, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.533×** | -15.6 | 0e+00 | 47/48 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.543×** | -15.2 | 0e+00 | 48/48 (HT-29, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.687×** | -9.3 | 2e-18 | 45/48 (HT-29, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.697×** | -8.5 | 3e-15 | 32/44 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.791×** | -8.2 | 2e-14 | 33/49 (A549, A498, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.772×** | -6.1 | 1e-07 | 34/48 (H4, A498, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.809×** | -5.3 | 1e-05 | 31/48 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.801×** | -5.2 | 1e-05 | 29/50 (hTERT-HPNE, HT-29, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.670×** | -5.2 | 1e-05 | 35/49 (HT-29, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -5.2 | 1e-05 | 1/50 (NCI-H23) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.811×** | -5.2 | 1e-05 | 27/49 (NCI-H2347, BT-474, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.810×** | -5.0 | 3e-05 | 29/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.821×** | -4.9 | 4e-05 | 26/48 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.883× | -4.4 | 5e-04 | 12/48 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.864× | -3.6 | 0.009 | 9/48 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.871× | -3.4 | 0.019 | 18/48 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.865× | -3.4 | 0.020 | 14/48 (NCI-H2347, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.912× | -3.2 | 0.036 | 4/48 (A549, BT-474, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.884× | -3.0 | 0.065 | 4/48 (SW1417, C32, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.890× | -2.9 | 0.096 | 5/48 (HS-578T, AN3 CA, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 5 µM |  | 0.921× | -2.9 | 0.096 | 1/48 (C32) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3045. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 259 | 13 (7 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 3.90× (z +23.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.52× (z +21.4) | [[Panobinostat (drug)]] 5 µM 0.518× (z -11.1) |
| [[NCI-H1573 (line)]] | alt | 628 | 7 (3 ⚠) | 5 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.80× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.84× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.286× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -14.8) |
| [[HT-29 (line)]] | alt | 408 | 7 (2 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 2.97× (z +11.4) | [[Panobinostat (drug)]] 5 µM 0.380× (z -19.4) |
| [[A498 (line)]] | wt | 372 | 5 (4 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.59× (z +11.9) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.59× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -13.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.473× (z -13.7) |
| [[hTERT-HPNE (line)]] | wt | 343 | 4 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.5) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 3.60× (z +10.8) | [[Panobinostat (drug)]] 5 µM 0.395× (z -14.9) |
| [[KATO III (line)]] | alt | 262 | 6 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.529× (z -11.7) |
| [[LoVo (line)]] | wt | 333 | 5 (2 ⚠) | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +17.4) | [[Panobinostat (drug)]] 5 µM 0.517× (z -14.3) |
| [[PANC-1 (line)]] | alt | 247 | 6 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +21.9) | [[Panobinostat (drug)]] 5 µM 0.517× (z -14.0) |
| [[SW480 (line)]] | alt | 188 | 6 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 2.12× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.90× (z +12.0) | [[Panobinostat (drug)]] 5 µM 0.473× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 417 | 3 (1 ⚠) | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.65× (z +11.9) | [[Panobinostat (drug)]] 5 µM 0.291× (z -18.4) |
| [[BT-474 (line)]] | alt | 240 | 4 (1 ⚠) | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.48× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.495× (z -11.2) |
| [[SW 900 (line)]] | alt | 347 | 4 (1 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.06× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.438× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 347 | 3 | 4 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.18× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.483× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 299 | 4 (2 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.374× (z -14.2) |
| [[HOP62 (line)]] | alt | 324 | 2 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.87× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.361× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 304 | 3 (1 ⚠) | 4 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.42× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.552× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 307 | 3 (1 ⚠) | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.84× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.494× (z -11.8) |
| [[SW1417 (line)]] | alt | 306 | 2 (1 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.16× (z +12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.434× (z -13.1) |
| [[A-172 (line)]] | wt | 239 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +14.1) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.18× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.555× (z -9.7) |
| [[COLO 205 (line)]] | alt | 312 | 3 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.37× (z +11.3) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 4.08× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.326× (z -15.5) |
| [[H4 (line)]] | wt | 344 | 2 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.03× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.377× (z -13.7) |
| [[Hs 766T (line)]] | wt | 287 | 3 (2 ⚠) | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.476× (z -11.5) |
| [[LS 180 (line)]] | wt | 316 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 530 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.418× (z -14.2) |
| [[RPMI-7951 (line)]] | alt | 348 | 3 | 3 | [[TAK-901 (drug)]] 5 µM 4.56× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.394× (z -13.0) |
| [[A549 (line)]] | wt | 254 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 2.92× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.523× (z -15.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.533× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 494 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.306× (z -17.8) |
| [[J82 (line)]] | alt | 246 | 2 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.482× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 421 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.14× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.401× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 326 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 3.24× (z +10.1) | [[Panobinostat (drug)]] 5 µM 0.480× (z -12.0) |
| [[SNU-1 (line)]] | wt | 389 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.40× (z +10.8) | — |
| [[A-427 (line)]] | wt | 352 | 2 | 2 | [[Auranofin (drug)]] 5 µM 1.95× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.556× (z -10.4) |
| [[HCT15 (line)]] | alt | 390 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 3.88× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.461× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 363 | 1 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.388× (z -10.3) |
| [[RKO (line)]] | wt | 370 | 3 | 1 | [[Auranofin (drug)]] 5 µM 1.92× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.555× (z -9.4) |
| [[SW48 (line)]] | wt | 381 | 4 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.54× (z +13.3) | — |
| [[C-33 A (line)]] | alt | 332 | 1 | 2 | [[Auranofin (drug)]] 5 µM 2.10× (z +11.0) | [[Panobinostat (drug)]] 5 µM 0.520× (z -9.7) |
| [[HS-578T (line)]] | alt | 265 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 3.81× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.450× (z -11.0) |
| [[SNU-423 (line)]] | alt | 187 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.406× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 285 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.423× (z -12.0) |
| [[AN3 CA (line)]] | alt | 349 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.06× (z +11.3) | — |
| [[C32 (line)]] | wt | 391 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.62× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 351 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 263 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.48× (z +11.9) | — |
| [[NCI-H2122 (line)]] | alt | 392 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 299 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 396 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 255 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3045), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 37 of them with an alert (⚠; 36 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDF3]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ELOC]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 661 |
| [[ZFAND2A-DT]] | +0.60 | +0.57 / +0.36 | both halves | 1e-04 |  |
| [[ZNF207]] | +0.59 | +0.58 / +0.57 | both halves | 9e-06 | STRING 475 |
| [[DMXL1-DT]] | +0.59 | +0.16 / +0.42 | ⚠ not reproduced | 0.001 |  |
| [[TMEM44-AS1]] | +0.57 | +0.16 / +0.53 | ⚠ one half (not replicated) | 0.001 |  |
| [[GPBP1]] | +0.57 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[PPM1N]] | +0.56 | +0.29 / +0.48 | both halves | 2e-04 |  |
| [[SPSB2]] | +0.55 | +0.37 / +0.36 | both halves | 1e-04 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[C11orf1]] | +0.54 | +0.28 / +0.41 | both halves | 3e-04 |  |
| [[BCAS2]] | +0.54 | +0.54 / +0.33 | both halves | 1e-04 |  |
| [[ABCC11]] | +0.54 | +0.44 / +0.32 | both halves | 2e-04 |  |
| [[TRA2A]] | +0.53 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[OSER1]] | +0.53 | +0.62 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | -0.49 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[POLD2]] | -0.47 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[IPO9]] | -0.46 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[TEX2]] | -0.46 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[QSOX2]] | -0.45 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[SMC1A]] | -0.45 | -0.46 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UBE2D3's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.304). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (6.3, 23.3); signed map (32.8, -13.9). **Vector** length 75.7, 28.1% of its response variance represented; |z| ≥ 3 in 1,414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.9 | -0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +5.1 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +4.1 | -8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.8 | +0.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.6 | +1.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.7 | +8.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.7 | +13.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.7 | +7.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.1 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | +0.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -0.6 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.6 | -2.3 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin conjugating enzyme E2 D3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:102,794,383-102,868,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UbcH5C |
| Gene groups (HGNC) | Ubiquitin conjugating enzymes E2 |
| Hallmark sets | TGF_BETA_SIGNALING, PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 41 pathways, smallest: TICAM1, RIP1-mediated IKK complex recruitment; IKK complex recruitment mediated by RIP1; Inactivation of CSF3 (G-CSF) signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P61077](https://www.uniprot.org/uniprotkb/P61077) (Ubiquitin-conjugating enzyme E2 D3):

> Accepts ubiquitin from the E1 complex and catalyzes its covalent attachment to other proteins. In vitro catalyzes 'Lys-11'-, as well as 'Lys-48'-linked polyubiquitination. Cooperates with the E2 CDC34 and the SCF(FBXW11) E3 ligase complex for the polyubiquitination of NFKBIA leading to its subsequent proteasomal degradation. Acts as an initiator E2, priming the phosphorylated NFKBIA target at positions 'Lys-21' and/or 'Lys-22' with a monoubiquitin. Ubiquitin chain elongation is then performed …

**Summary**, from NCBI Gene [7323](https://www.ncbi.nlm.nih.gov/gene/7323):

> The modification of proteins with ubiquitin is an important cellular mechanism for targeting abnormal or short-lived proteins for degradation. Ubiquitination involves at least three classes of enzymes: ubiquitin-activating enzymes, or E1s, ubiquitin-conjugating enzymes, or E2s, and ubiquitin-protein ligases, or E3s. This gene encodes a member of the E2 ubiquitin-conjugating enzyme family. This enzyme functions in the ubiquitination of the tumor-suppressor protein p53, which is induced by an E3 …

**Accessions** — [HGNC:12476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12476) · Entrez [7323](https://www.ncbi.nlm.nih.gov/gene/7323) · UniProt [P61077](https://www.uniprot.org/uniprotkb/P61077) · Ensembl [ENSG00000109332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109332)

## Data

Gene col 3045: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3045); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3045, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3045]; `tensor/DDL_lfc|DDL_z.npy` [3045]; `embed/gene_vectors.npy` [3045]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3045 or target_col == 3045). Every well: [[UBE2D3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2D3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
