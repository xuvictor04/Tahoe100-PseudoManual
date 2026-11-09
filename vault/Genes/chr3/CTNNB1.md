---
symbol: "CTNNB1"
type: "gene"
col: 9585
ensembl_id: "ENSG00000168036"
name: "catenin beta 1"
location: "3p22.1"
module: 106
arm: "+"
pooled_cpm: 405.06
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# CTNNB1

*catenin beta 1* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.73× (z +13.4, q 2e-38, up in 44 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.64× (z +12.2, q 5e-32, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.747× (z -7.0, q 1e-09, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNL1]] (+0.56, fdr 1e-05), [[TIPARP]] (+0.56, fdr 3e-05), [[TCF7L2]] (+0.55, fdr 4e-05); moves opposite to [[XPNPEP3]] (-0.52, fdr 3e-05), [[DPP9]] (-0.51, fdr 1e-04), [[ZNF142]] (-0.51, fdr 2e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +13.4 | 2e-38 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.44×** | +12.8 | 6e-35 | 30/48 (LoVo, HS-578T, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +12.2 | 5e-32 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +9.0 | 3e-17 | 39/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +7.8 | 5e-13 | 34/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.34×** | +7.0 | 2e-10 | 30/48 (A549, HS-578T, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~21% of this change | **1.31×** | +6.5 | 8e-09 | 33/47 (LoVo, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +6.4 | 9e-09 | 34/49 (AsPC-1, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +6.0 | 1e-07 | 22/48 (LoVo, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +5.4 | 3e-06 | 32/49 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.21×** | +4.8 | 9e-05 | 25/49 (PANC-1, SW480, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.20×** | +4.5 | 3e-04 | 24/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.012 | 24/48 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.029 | 22/48 (SW48, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 0.5 µM |  | 1.15× | +3.4 | 0.029 | 9/48 (Hs 766T, PANC-1, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.14× | +3.3 | 0.030 | 10/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.031 | 15/48 (HT-29, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.747×** | -7.0 | 1e-09 | 35/48 (RPMI-7951, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.763×** | -6.6 | 1e-08 | 29/48 (A-172, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.769×** | -6.4 | 3e-08 | 31/48 (RPMI-7951, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -5.3 | 1e-05 | 0/50 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.809×** | -5.2 | 3e-05 | 29/48 (COLO 205, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.817×** | -4.9 | 1e-04 | 26/48 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.820×** | -4.6 | 3e-04 | 24/47 (SW1417, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.819×** | -4.6 | 4e-04 | 28/50 (RPMI-7951, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.878× | -4.5 | 5e-04 | 18/49 (SW 900, SW1417, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.828×** | -4.4 | 6e-04 | 24/47 (SW1417, A-172, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.824×** | -4.3 | 7e-04 | 24/48 (NCI-H1573, HCT15, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.713×** | -4.3 | 8e-04 | 26/49 (HT-29, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.842× | -4.2 | 0.001 | 21/48 (SW 900, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.843× | -4.2 | 0.001 | 23/48 (SW1417, SW 1088, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.892× | -3.8 | 0.005 | 10/48 (SHP-77, NCI-H1573, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.859× | -3.7 | 0.008 | 18/47 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.871× | -3.3 | 0.029 | 16/48 (BT-474, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.875× | -3.2 | 0.038 | 15/48 (RPMI-7951, SW 900, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.782×** | -3.1 | 0.051 | 19/48 (NCI-H2347, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.879× | -3.0 | 0.074 | 12/49 (HEC-1-A, CFPAC-1, …) | top dose only | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 209 | 12 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.82× (z +26.4) | — |
| [[SW 900 (line)]] | alt | 553 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -18.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.510× (z -9.0) |
| [[BT-474 (line)]] | alt | 267 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.52× (z +12.0) | — |
| [[LoVo (line)]] | wt | 279 | 7 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.36× (z +23.4) | — |
| [[NCI-H1792 (line)]] | alt | 276 | 5 (3 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.83× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.660× (z -8.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW480 (line)]] | alt | 527 | 2 (2 ⚠) | 4 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.497× (z -15.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HOP62 (line)]] | alt | 314 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 910 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.471× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 159 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +15.0) | — |
| [[SW1417 (line)]] | alt | 1,126 | 1 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -16.0) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SW48 (line)]] | wt | 270 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.33× (z +12.7) | — |
| [[A498 (line)]] | wt | 185 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +18.7) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A549 (line)]] | wt | 238 | 3 (3 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.26× (z +12.5) ⚠ cell-cycle shift, explains ~50% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.666× (z -9.1) ⚠ cell-cycle shift, explains ~20% of this change |
| [[AsPC-1 (line)]] | alt | 391 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +14.1) | — |
| [[KATO III (line)]] | alt | 2,830 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.93× (z +25.7) | — |
| [[LS 180 (line)]] | wt | 452 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -9.9) ⚠ cell-cycle shift, explains ~20% of this change |
| [[NCI-H1573 (line)]] | alt | 248 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.59× (z +15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.46× (z +14.3) | — |
| [[RPMI-7951 (line)]] | alt | 615 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -13.0) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.525× (z -10.0) |
| [[A-427 (line)]] | wt | 246 | 3 (3 ⚠) | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HS-578T (line)]] | alt | 281 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +20.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[LOX-IMVI (line)]] | wt | 327 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +13.5) | — |
| [[COLO 205 (line)]] | alt | 496 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.6) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.420× (z -8.7) |
| [[H4 (line)]] | wt | 180 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.56× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 481 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.7) ⚠ cell-cycle shift, explains ~50% of this change | [[Dinaciclib (drug)]] 5 µM 0.466× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 240 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.92× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 1.87× (z +9.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 190 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.8) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[Panc 03.27 (line)]] | alt | 427 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -10.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[SK-MEL-2 (line)]] | alt | 515 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.5) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SNU-423 (line)]] | alt | 420 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -10.2) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.522× (z -8.5) |
| [[A-172 (line)]] | wt | 201 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.513× (z -10.1) |
| [[AN3 CA (line)]] | alt | 308 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +12.9) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[C-33 A (line)]] | alt | 281 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.99× (z +9.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 345 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +14.8) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[CHP-212 (line)]] | wt | 464 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -8.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[HT-29 (line)]] | alt | 222 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.545× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 252 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +20.3) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[J82 (line)]] | alt | 289 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 326 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 237 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 1.86× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H596 (line)]] | alt | 399 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.252× (z -13.7) |
| [[RKO (line)]] | wt | 250 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[SW 1088 (line)]] | alt | 288 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.211× (z -9.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 335 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 376 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 380 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 340 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 200 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 241 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 386 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNL1]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[TIPARP]] | +0.56 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[TCF7L2]] | +0.55 | +0.40 / +0.61 | both halves | 4e-05 | same gene group; pathway: Beta-catenin independent WNT signaling; STRING 999 |
| [[MYLIP]] | +0.55 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CAPZA2]] | +0.53 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PELI1]] | +0.52 | +0.48 / +0.55 | both halves | 2e-05 | pathway: Programmed Cell Death |
| [[PPM1N]] | +0.52 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[PUM1]] | +0.52 | +0.43 / +0.53 | both halves | 4e-05 |  |
| [[IQCD]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LINC00511]] | +0.51 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[EPS8]] | +0.50 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[VASN]] | +0.50 | +0.48 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPNPEP3]] | -0.52 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DPP9]] | -0.51 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ZNF142]] | -0.51 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[ATP6V0A2]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[BAG5]] | -0.50 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[MTOR]] | -0.49 | -0.46 / -0.45 | both halves | 3e-05 | pathway: Cellular responses to mechanical stimuli; STRING 694 |
| [[CHFR]] | -0.48 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[L3MBTL2]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[CAMKK2]] | -0.47 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[EP400]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 | STRING 578 |
| [[TRIM27]] | -0.47 | -0.40 / -0.48 | both halves | 5e-05 | pathway: Bacterial Infection Pathways |
| [[ZBTB49]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CTNNB1's level | compounds that target MAP2K1: 3 of 4 lower it (Cobimetinib, TAK-733, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NFKBIZ]] | C | NFKBIZ activity lowers CTNNB1's level | lines that do not express NFKBIZ (3) vs lines expressing it (47) | 2.34× higher at baseline in the lines without NFKBIZ | 0.067 | ⚠ few lines (3 vs 47); across organs; also absent: CPEB2, PKIA-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.456). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.1, 46.2); signed map (11.1, 29.9). **Vector** length 110, 35.7% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.8 | +6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.2 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +7.4 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.9 | +0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | +0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.1 | -0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.9 | -0.1 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.2 | -0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.1 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.1 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.9 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.2 | +1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.4 | -3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | +3.3 |

## What is on record

|  |  |
|---|---|
| Name | catenin beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:41,194,741-41,260,096 (+) |
| Ensembl biotype | protein_coding |
| Also known as | beta-catenin, armadillo; previously CTNNB |
| Gene groups (HGNC) | Armadillo repeat containing; Beta catenins; Wnt enhanceosome complex |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING, TGF_BETA_SIGNALING, CHOLESTEROL_HOMEOSTASIS, APOPTOSIS |
| Reactome | 92 pathways, smallest: LRR FLII-interacting protein 1 (LRRFIP1) activates type I IFN production; CDH11 homotypic and heterotypic interactions; Regulation of CDH19 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [P35222](https://www.uniprot.org/uniprotkb/P35222) (Catenin beta-1):

> Key downstream component of the canonical Wnt signaling pathway. In the absence of Wnt, forms a complex with AXIN1, AXIN2, APC, CSNK1A1 and GSK3B that promotes phosphorylation on N-terminal Ser and Thr residues and ubiquitination of CTNNB1 via BTRC and its subsequent degradation by the proteasome. In the presence of Wnt ligand, CTNNB1 is not ubiquitinated and accumulates in the nucleus, where it acts as a coactivator for transcription factors of the TCF/LEF family, leading to activate Wnt …

**Summary**, from NCBI Gene [1499](https://www.ncbi.nlm.nih.gov/gene/1499):

> The protein encoded by this gene is part of a complex of proteins that constitute adherens junctions (AJs). AJs are necessary for the creation and maintenance of epithelial cell layers by regulating cell growth and adhesion between cells. The encoded protein also anchors the actin cytoskeleton and may be responsible for transmitting the contact inhibition signal that causes cells to stop dividing once the epithelial sheet is complete. Finally, this protein binds to the product of the APC gene, …

**Accessions** — [HGNC:2514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2514) · Entrez [1499](https://www.ncbi.nlm.nih.gov/gene/1499) · UniProt [P35222](https://www.uniprot.org/uniprotkb/P35222) · Ensembl [ENSG00000168036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168036)

## Data

Gene col 9585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9585); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9585]; `tensor/DDL_lfc|DDL_z.npy` [9585]; `embed/gene_vectors.npy` [9585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9585 or target_col == 9585). Every well: [[CTNNB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTNNB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
