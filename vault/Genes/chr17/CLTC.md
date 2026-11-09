---
symbol: "CLTC"
type: "gene"
col: 6505
ensembl_id: "ENSG00000141367"
name: "clathrin heavy chain"
location: "17q23.1"
module: 20
arm: "+"
pooled_cpm: 424.76
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 11
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CLTC

*clathrin heavy chain* — 17q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.69× (z +13.5, q 9e-39, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.710× (z -12.4, q 9e-33, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDLBP]] (+0.66, fdr 7e-06), [[HUWE1]] (+0.63, fdr 1e-05), [[NORAD]] (+0.59, fdr 1e-05); moves opposite to [[BCL7A]] (-0.58, fdr 4e-05), [[CHKB]] (-0.56, fdr 3e-05), [[ZNF330]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +13.5 | 9e-39 | 46/48 (C32, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +12.7 | 1e-34 | 44/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +11.2 | 1e-26 | 43/49 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +9.0 | 3e-17 | 42/48 (HEC-1-A, PANC-1, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +8.9 | 7e-17 | 42/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +8.5 | 1e-15 | 43/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.39×** | +7.9 | 2e-13 | 41/48 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +7.6 | 2e-12 | 39/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +6.9 | 3e-10 | 25/48 (NCI-H460, Hs 766T, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +6.7 | 9e-10 | 38/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +6.6 | 2e-09 | 31/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +6.6 | 3e-09 | 36/48 (HEC-1-A, HepG2/C3A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | 1.19× | +4.3 | 6e-04 | 22/48 (NCI-H1573, NCI-H460, …) | top dose only | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +4.2 | 9e-04 | 35/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 28/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.006 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.095 | 13/48 (HEC-1-A, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.12× | +2.9 | 0.095 | 3/48 (A-427, C-33 A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -12.4 | 9e-33 | 39/49 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -10.8 | 1e-24 | 45/47 (SW 900, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.747×** | -7.5 | 2e-11 | 45/48 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.844× | -4.4 | 0.002 | 17/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.953× | -4.2 | 0.003 | 0/50 | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.894× | -4.0 | 0.005 | 7/48 (AsPC-1, HT-29, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.859× | -3.9 | 0.007 | 17/48 (HepG2/C3A, SNU-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.810×** | -3.9 | 0.007 | 31/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.860× | -3.9 | 0.007 | 20/48 (BT-474, A549, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.872× | -3.5 | 0.025 | 3/48 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.829×** | -3.4 | 0.031 | 23/49 (SW 900, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.876× | -3.4 | 0.032 | 9/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.838× | -3.2 | 0.052 | 21/48 (HCT15, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | 0.839× | -3.2 | 0.056 | 18/48 (BT-474, HT-29, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.879× | -3.2 | 0.059 | 17/48 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.842× | -3.1 | 0.059 | 20/48 (CFPAC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.847× | -3.0 | 0.079 | 17/47 (SHP-77, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.920× | -3.0 | 0.080 | 6/48 (NCI-H2030, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 345 | 13 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +29.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.59× (z +23.3) | — |
| [[PANC-1 (line)]] | alt | 303 | 9 (4 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +15.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +15.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.635× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 266 | 9 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +19.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +13.0) | — |
| [[HOP62 (line)]] | alt | 489 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +16.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.543× (z -11.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 343 | 7 (5 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +20.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.92× (z +17.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.559× (z -9.2) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 470 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +15.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.22× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.537× (z -10.6) ⚠ toxic |
| [[SW480 (line)]] | alt | 354 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.502× (z -12.5) ⚠ toxic |
| [[LS 180 (line)]] | wt | 450 | 4 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +13.1) | [[Homoharringtonine (drug)]] 0.05 µM 0.582× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 395 | 6 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +17.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.40× (z +9.9) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.586× (z -8.5) |
| [[RKO (line)]] | wt | 457 | 4 | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.634× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 482 | 5 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.96× (z +14.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.646× (z -8.7) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 342 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +16.8) | — |
| [[SNU-423 (line)]] | alt | 424 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +14.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.87× (z +10.9) | — |
| [[BT-474 (line)]] | alt | 1,574 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -13.3) |
| [[COLO 205 (line)]] | alt | 423 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.518× (z -8.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 294 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +21.4) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.12× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 448 | 3 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.81× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 386 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.92× (z +10.7) | — |
| [[A-427 (line)]] | wt | 525 | 3 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 1.73× (z +8.9) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.66× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -8.9) |
| [[A498 (line)]] | wt | 539 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 1.83× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 1.53× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.621× (z -13.5) |
| [[LoVo (line)]] | wt | 356 | 2 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.51× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.519× (z -15.0) |
| [[H4 (line)]] | wt | 579 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 335 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 3.71× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.664× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 385 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -14.6) |
| [[Panc 03.27 (line)]] | alt | 440 | 3 | 0 | [[Auranofin (drug)]] 5 µM 1.96× (z +11.5) | — |
| [[SW 900 (line)]] | alt | 483 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.437× (z -13.9) ⚠ toxic |
| [[A549 (line)]] | wt | 503 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.9) ⚠ cell-cycle shift, explains ~25% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -23.5) |
| [[AsPC-1 (line)]] | alt | 345 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +10.1) | — |
| [[C32 (line)]] | wt | 228 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.12× (z +17.6) | — |
| [[HS-578T (line)]] | alt | 422 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.66× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.42× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 589 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -11.9) |
| [[SHP-77 (line)]] | alt | 275 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.90× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.600× (z -8.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 354 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 1.81× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.557× (z -10.2) ⚠ toxic |
| [[SW48 (line)]] | wt | 584 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -11.4) |
| [[A-172 (line)]] | wt | 392 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.59× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 336 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.18× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 464 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.99× (z +12.6) | — |
| [[CHP-212 (line)]] | wt | 606 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -11.3) |
| [[J82 (line)]] | alt | 384 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.526× (z -10.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 574 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.410× (z -12.5) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 446 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.614× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 367 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.78× (z +10.3) | — |
| [[SW 1088 (line)]] | alt | 395 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.211× (z -11.1) |
| [[C-33 A (line)]] | alt | 275 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 470 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 346 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 368 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 437 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 401 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDLBP]] | +0.66 | +0.58 / +0.71 | both halves | 7e-06 | pathway: Plasma lipoprotein assembly, remodeling, and clearance |
| [[HUWE1]] | +0.63 | +0.51 / +0.71 | both halves | 1e-05 | STRING 622 |
| [[NORAD]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[YIPF6]] | +0.56 | +0.50 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 554 |
| [[ARF1]] | +0.56 | +0.62 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_PI3K_AKT_MTOR_SIGNALING; STRING 903 |
| [[TMED7]] | +0.55 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[TTN-AS1]] | +0.55 | +0.37 / +0.58 | both halves | 9e-05 |  |
| [[ENO1]] | +0.55 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[UGGT1]] | +0.54 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[G6PD]] | +0.54 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[UBR4]] | +0.54 | +0.46 / +0.59 | both halves | 3e-05 | STRING 632 |
| [[USO1]] | +0.54 | +0.38 / +0.69 | both halves | 6e-05 | pathway: HALLMARK_PROTEIN_SECRETION; STRING 423 |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL7A]] | -0.58 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[CHKB]] | -0.56 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[ZNF330]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[MRPL32]] | -0.54 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[POMZP3]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[ZNRF2P2]] | -0.53 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ARRDC2]] | -0.53 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[WHAMMP2]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NDUFAF6]] | -0.52 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[RNF135]] | -0.52 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[RNF138]] | -0.51 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[SNHG9]] | -0.51 | -0.41 / -0.58 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.388). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-33.7, -20.7); signed map (-16.2, -35.6). **Vector** length 125, 46.6% of its response variance represented; |z| ≥ 3 in 1,363 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.9 | +13.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.1 | +1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.0 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.4 | +7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +9.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.4 | +4.2 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +3.3 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.5 | -10.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.0 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -12.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.3 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.0 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | clathrin heavy chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.1 — chr17:59,619,680-59,696,956 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Hc; previously CLTCL2 |
| Gene groups (HGNC) | Clathrin subunits |
| Hallmark sets | PROTEIN_SECRETION, PI3K_AKT_MTOR_SIGNALING |
| Reactome | 45 pathways, smallest: Entry of Influenza Virion into Host Cell via Endocytosis; Formation of annular gap junctions; ALK mutants bind TKIs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00610](https://www.uniprot.org/uniprotkb/Q00610) (Clathrin heavy chain 1):

> Clathrin is the major protein of the polyhedral coat of coated pits and vesicles. Two different adapter protein complexes link the clathrin lattice either to the plasma membrane or to the trans-Golgi network. Acts as a component of the TACC3/ch-TOG/clathrin complex proposed to contribute to stabilization of kinetochore fibers of the mitotic spindle by acting as inter-microtubule bridge. The TACC3/ch-TOG/clathrin complex is required for the maintenance of kinetochore fiber tension. Plays a role …

**Summary**, from NCBI Gene [1213](https://www.ncbi.nlm.nih.gov/gene/1213):

> Clathrin is a major protein component of the cytoplasmic face of intracellular organelles, called coated vesicles and coated pits. These specialized organelles are involved in the intracellular trafficking of receptors and endocytosis of a variety of macromolecules. The basic subunit of the clathrin coat is composed of three heavy chains and three light chains. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2092) · Entrez [1213](https://www.ncbi.nlm.nih.gov/gene/1213) · UniProt [Q00610](https://www.uniprot.org/uniprotkb/Q00610) · Ensembl [ENSG00000141367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141367)

## Data

Gene col 6505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6505); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6505]; `tensor/DDL_lfc|DDL_z.npy` [6505]; `embed/gene_vectors.npy` [6505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6505 or target_col == 6505). Every well: [[CLTC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLTC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
