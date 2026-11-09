---
symbol: "TBL1XR1"
type: "gene"
col: 10834
ensembl_id: "ENSG00000177565"
name: "TBL1X/Y related 1"
location: "3q26.32"
module: 142
arm: "+"
pooled_cpm: 422.41
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 23
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# TBL1XR1

*TBL1X/Y related 1* — 3q26.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.43× (z +6.0, q 8e-07, up in 38 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 1.41× (z +5.9, q 8e-07, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.354× (z -18.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AMOT]] (+0.60, fdr 4e-05), [[SMG7]] (+0.59, fdr 1e-05), [[PLCB4]] (+0.58, fdr 6e-05); moves opposite to [[SLC30A6]] (-0.66, fdr 1e-05), [[GPR89A]] (-0.63, fdr 9e-05), [[C19orf25]] (-0.63, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +6.0 | 8e-07 | 38/47 (J82, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 8e-07 | 36/49 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +5.7 | 3e-06 | 40/48 (C32, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +5.3 | 1e-05 | 28/48 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +5.1 | 5e-05 | 30/48 (HS-578T, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.25×** | +3.9 | 0.010 | 28/48 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.025 | 26/48 (PANC-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.15× | +3.5 | 0.035 | 21/48 (A-172, J82, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.073 | 25/49 (HepG2/C3A, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.079 | 24/48 (A-427, SW480, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.2 | 0.080 | 23/48 (NCI-H460, SW480, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.354×** | -18.0 | 0e+00 | 48/48 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.359×** | -17.8 | 0e+00 | 48/48 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -15.7 | 0e+00 | 46/49 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.414×** | -15.3 | 0e+00 | 48/48 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -12.1 | 1e-31 | 47/47 (HepG2/C3A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.614×** | -8.1 | 4e-14 | 41/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.638×** | -7.8 | 5e-13 | 47/48 (BT-474, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.644×** | -7.3 | 1e-11 | 45/50 (LS 180, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **0.659×** | -7.2 | 3e-11 | 32/49 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **0.687×** | -6.3 | 2e-08 | 28/44 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.739×** | -5.2 | 9e-06 | 42/48 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.745×** | -5.1 | 2e-05 | 35/48 (LoVo, SW 900, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.748×** | -5.0 | 2e-05 | 29/48 (NCI-H1573, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.815×** | -5.0 | 2e-05 | 28/48 (PANC-1, NCI-H2347, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.773×** | -4.5 | 3e-04 | 35/48 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.845× | -4.1 | 0.001 | 22/48 (NCI-H2347, MIA PaCa-2, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.793×** | -4.0 | 0.002 | 31/49 (LoVo, HT-29, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.756×** | -4.0 | 0.002 | 31/48 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.696×** | -3.3 | 0.026 | 27/48 (KATO III, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.703×** | -3.2 | 0.034 | 28/48 (LoVo, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.726×** | -2.9 | 0.082 | 27/48 (SW480, SNU-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.50 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 491 | 2 | 11 (8 ⚠) | [[Ponatinib (drug)]] 5 µM 2.41× (z +10.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -20.9) |
| [[LoVo (line)]] | wt | 622 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -18.2) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.260× (z -15.6) |
| [[PANC-1 (line)]] | alt | 381 | 4 (2 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +11.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 233 | 2 | 8 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.61× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -19.8) |
| [[NCI-H460 (line)]] | wt | 246 | 3 (3 ⚠) | 7 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.97× (z +11.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -19.2) |
| [[HT-29 (line)]] | alt | 619 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -15.9) |
| [[LS 180 (line)]] | wt | 426 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -17.8) |
| [[SK-MEL-2 (line)]] | alt | 606 | 1 | 8 (6 ⚠) | [[PH-797804 (drug)]] 5 µM 3.15× (z +8.5) | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -21.7) |
| [[COLO 205 (line)]] | alt | 504 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -15.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -12.9) |
| [[HepG2_C3A (line)]] | wt | 433 | 1 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -21.7) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -17.5) |
| [[KATO III (line)]] | alt | 709 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.299× (z -15.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -15.5) |
| [[SW 900 (line)]] | alt | 356 | 0 | 8 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -18.0) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.311× (z -15.4) |
| [[A498 (line)]] | wt | 407 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -21.3) |
| [[A549 (line)]] | wt | 202 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 805 | 1 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +10.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -20.4) |
| [[NCI-H1792 (line)]] | alt | 380 | 1 (1 ⚠) | 6 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.00× (z +8.5) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -15.8) |
| [[SW480 (line)]] | alt | 452 | 1 (1 ⚠) | 6 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.93× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -20.5) |
| [[A-427 (line)]] | wt | 565 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.16× (z +9.5) | [[Panobinostat (drug)]] 5 µM 0.271× (z -16.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -15.5) |
| [[AsPC-1 (line)]] | alt | 239 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.305× (z -15.6) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.308× (z -15.5) |
| [[CHP-212 (line)]] | wt | 388 | 1 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +8.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -10.9) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 592 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 2.05× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.433× (z -10.6) |
| [[RKO (line)]] | wt | 510 | 1 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.44× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -12.6) |
| [[A-172 (line)]] | wt | 214 | 2 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.92× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 612 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -15.5) |
| [[H4 (line)]] | wt | 292 | 3 (2 ⚠) | 2 (1 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.29× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.14× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -9.9) |
| [[HOP62 (line)]] | alt | 413 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -16.1) |
| [[LOX-IMVI (line)]] | wt | 414 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -18.4) |
| [[MIA PaCa-2 (line)]] | alt | 393 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.273× (z -15.0) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 443 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -14.3) |
| [[NCI-H23 (line)]] | alt | 303 | 1 (1 ⚠) | 4 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.97× (z +9.0) ⚠ toxic | [[Panobinostat (drug)]] 5 µM 0.226× (z -20.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.262× (z -18.5) |
| [[SNU-423 (line)]] | alt | 305 | 1 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +11.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Panobinostat (drug)]] 5 µM 0.396× (z -12.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.447× (z -11.2) |
| [[SW48 (line)]] | wt | 455 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 0.05 µM 4.04× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -14.9) |
| [[RPMI-7951 (line)]] | alt | 362 | 2 | 2 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.11× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -11.1) |
| [[SW1417 (line)]] | alt | 408 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +13.8) ⚠ cell-cycle shift, explains ~26% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -13.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.461× (z -9.8) |
| [[C-33 A (line)]] | alt | 309 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.279× (z -16.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.280× (z -16.3) |
| [[Hs 766T (line)]] | wt | 268 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -12.3) |
| [[HS-578T (line)]] | alt | 272 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.72× (z +10.0) | — |
| [[J82 (line)]] | alt | 358 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +16.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.92× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 529 | 2 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.463× (z -9.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 519 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -15.1) |
| [[hTERT-HPNE (line)]] | wt | 207 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.389× (z -11.9) |
| [[SHP-77 (line)]] | alt | 267 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.47× (z +9.5) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -11.5) |
| [[SNU-1 (line)]] | wt | 563 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.323× (z -11.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 527 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -11.0) |
| [[HCT15 (line)]] | alt | 294 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 354 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 391 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 322 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 226 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 396 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMOT]] | +0.60 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[SMG7]] | +0.59 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.58 | +0.38 / +0.59 | both halves | 6e-05 |  |
| [[ATF7IP]] | +0.57 | +0.28 / +0.66 | both halves | 3e-04 | pathway: Chromatin modifying enzymes |
| [[DHX9]] | +0.57 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[H2AZ2]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 | pathway: Chromatin modifying enzymes |
| [[MACROD2]] | +0.56 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[CHN1]] | +0.56 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[TMEM123]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[VAPA]] | +0.56 | +0.41 / +0.64 | both halves | 4e-05 |  |
| [[AHR]] | +0.55 | +0.36 / +0.61 | both halves | 1e-04 | pathway: PPARA activates gene expression |
| [[NFIB]] | +0.55 | +0.38 / +0.58 | both halves | 6e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A6]] | -0.66 | -0.51 / -0.69 | both halves | 1e-05 |  |
| [[GPR89A]] | -0.63 | -0.36 / -0.68 | both halves | 9e-05 |  |
| [[C19orf25]] | -0.63 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TAF12]] | -0.60 | -0.60 / -0.63 | both halves | 7e-06 | pathway: Chromatin modifying enzymes |
| [[FBXO28]] | -0.60 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[ZBTB49]] | -0.60 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[ZNF778]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[GPR89B]] | -0.59 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[IL17RA]] | -0.59 | -0.39 / -0.64 | both halves | 5e-05 |  |
| [[PCYT1A]] | -0.58 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[FBH1]] | -0.58 | -0.37 / -0.62 | both halves | 7e-05 |  |
| [[GON4L]] | -0.58 | -0.51 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TBL1XR1's level | compounds that target TOP2A: 4 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MPP7]] | B | MPP7 activity raises TBL1XR1's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 1.17× lower at baseline in the lines without MPP7 | 0.075 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction -0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.7, -4.5); signed map (48.3, 1.5). **Vector** length 120, 49.2% of its response variance represented; |z| ≥ 3 in 1,537 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.5 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +11.4 | -2.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +10.4 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +10.4 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +10.1 | -6.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.5 | +0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.1 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +1.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.5 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.4 | -1.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.2 | -7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.9 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.3 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -3.2 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | TBL1X/Y related 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.32 — chr3:177,019,340-177,228,000 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IRA1, FLJ12894, TBLR1, C21, DC42 |
| Gene groups (HGNC) | WD repeat domain containing; NCoR/SMRT transcriptional repression complex subunits |
| Reactome | 55 pathways, smallest: Loss of MECP2 binding ability to the NCoR/SMRT complex; Disorders of Nervous System Development; Loss of function of MECP2 in Rett syndrome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZK7](https://www.uniprot.org/uniprotkb/Q9BZK7) (F-box-like/WD repeat-containing protein TBL1XR1):

> F-box-like protein involved in the recruitment of the ubiquitin/19S proteasome complex to nuclear receptor-regulated transcription units. Plays an essential role in transcription activation mediated by nuclear receptors. Probably acts as integral component of the N-Cor corepressor complex that mediates the recruitment of the 19S proteasome complex, leading to the subsequent proteasomal degradation of N-Cor complex, thereby allowing cofactor exchange, and transcription activation.

**Summary**, from NCBI Gene [79718](https://www.ncbi.nlm.nih.gov/gene/79718):

> This gene is a member of the WD40 repeat-containing gene family and shares sequence similarity with transducin (beta)-like 1X-linked (TBL1X). The protein encoded by this gene is thought to be a component of both nuclear receptor corepressor (N-CoR) and histone deacetylase 3 (HDAC 3) complexes, and is required for transcriptional activation by a variety of transcription factors. Mutations in these gene have been associated with some autism spectrum disorders, and one finding suggests that …

**Accessions** — [HGNC:29529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29529) · Entrez [79718](https://www.ncbi.nlm.nih.gov/gene/79718) · UniProt [Q9BZK7](https://www.uniprot.org/uniprotkb/Q9BZK7) · Ensembl [ENSG00000177565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177565)

## Data

Gene col 10834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10834); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10834]; `tensor/DDL_lfc|DDL_z.npy` [10834]; `embed/gene_vectors.npy` [10834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10834 or target_col == 10834). Every well: [[TBL1XR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBL1XR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
