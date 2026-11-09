---
symbol: "ARID4B"
type: "gene"
col: 605
ensembl_id: "ENSG00000054267"
name: "AT-rich interaction domain 4B"
location: "1q42.3"
module: 231
arm: "+"
pooled_cpm: 455.66
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/231"]
generated_by: "tahoemap"
---

# ARID4B

*AT-rich interaction domain 4B* — 1q42.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.96× (z +35.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.446× (z -18.2, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.742× (z -7.0, q 4e-10, down in 38 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 12 lines (NCI-H1792 0.229×, SK-MEL-2 0.220×, NCI-H2347 0.241×, SW 900 0.264×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 11 lines (SW 900 0.530×, CFPAC-1 0.542×, AsPC-1 0.554×, NCI-H1792 0.569×, …); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.300×, SW 900 0.392×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf56]] (+0.73, fdr 1e-05), [[TERF2IP]] (+0.72, fdr 7e-06), [[NDUFC1]] (+0.71, fdr 1e-05); moves opposite to [[EFTUD2]] (-0.70, fdr 7e-06), [[CS]] (-0.67, fdr 1e-05), [[MAPKAPK3]] (-0.67, fdr 7e-06).
> It is in [[Module 231]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SYF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +35.9 | 0e+00 | 47/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +16.4 | 0e+00 | 43/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +16.1 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +15.4 | 0e+00 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +15.2 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +12.6 | 2e-34 | 47/49 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +11.5 | 9e-29 | 37/49 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.52×** | +9.8 | 6e-21 | 39/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +9.7 | 2e-20 | 41/50 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +9.6 | 3e-20 | 42/48 (SW48, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +7.8 | 3e-13 | 37/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +7.7 | 8e-13 | 41/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +7.1 | 4e-11 | 34/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +6.1 | 4e-08 | 35/48 (HT-29, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.26×** | +5.4 | 2e-06 | 29/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +5.3 | 5e-06 | 31/48 (LoVo, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.7 | 8e-05 | 25/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.20×** | +4.1 | 0.001 | 25/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 605.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 12 lines (NCI-H1792 0.229×, SK-MEL-2 0.220×, NCI-H2347 0.241×, SW 900 0.264×, …; ⚠ toxic; transcription drop); [[Panobinostat (drug)]] 0.5 µM in 11 lines (SW 900 0.530×, CFPAC-1 0.542×, AsPC-1 0.554×, NCI-H1792 0.569×, …); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2347 0.300×, SW 900 0.392×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.446×** | -18.2 | 0e+00 | 44/44 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.522×** | -10.4 | 9e-23 | 47/49 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.674×** | -8.5 | 3e-15 | 34/45 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.742×** | -7.0 | 4e-10 | 38/48 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.805×** | -5.1 | 5e-05 | 27/48 (CFPAC-1, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -4.9 | 9e-05 | 15/48 (NCI-H2347, BT-474, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.842× | -3.9 | 0.009 | 20/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.858× | -3.6 | 0.024 | 20/48 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.874× | -3.1 | 0.097 | 6/48 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.874× | -3.1 | 0.097 | 14/48 (SW 900, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.875× | -3.1 | 0.097 | 9/48 (LS 180, COLO 205, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~54% of this change | 0.872× | -3.1 | 0.098 | 21/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.879× | -3.0 | 0.12 | 11/49 (BT-474, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 534 | 16 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +40.9) | — |
| [[PANC-1 (line)]] | alt | 410 | 13 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +39.2) | [[Dinaciclib (drug)]] 5 µM 0.442× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.644× (z -8.5) |
| [[SW480 (line)]] | alt | 450 | 13 (4 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +37.6) | [[Dinaciclib (drug)]] 5 µM 0.490× (z -13.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 411 | 9 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +28.7) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.633× (z -8.8) |
| [[LS 180 (line)]] | wt | 374 | 10 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +25.2) | [[Dinaciclib (drug)]] 5 µM 0.421× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 347 | 10 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +23.8) | [[Dinaciclib (drug)]] 5 µM 0.552× (z -9.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 325 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +32.3) | — |
| [[NCI-H1792 (line)]] | alt | 475 | 8 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +27.1) | [[Dinaciclib (drug)]] 5 µM 0.229× (z -25.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.569× (z -10.4) |
| [[SW 900 (line)]] | alt | 879 | 6 (1 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +28.1) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -24.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.530× (z -12.1) |
| [[H4 (line)]] | wt | 401 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +30.0) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 713 | 4 (1 ⚠) | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +20.1) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -25.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.626× (z -8.7) |
| [[RKO (line)]] | wt | 419 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +23.1) | — |
| [[AsPC-1 (line)]] | alt | 529 | 7 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.54× (z +31.5) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.554× (z -10.4) |
| [[C-33 A (line)]] | alt | 436 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.24× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.276× (z -18.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 398 | 7 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +29.7) | [[Dinaciclib (drug)]] 5 µM 0.527× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 240 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +23.0) | — |
| [[LOX-IMVI (line)]] | wt | 459 | 7 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -14.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 562 | 6 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 493 | 7 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +32.8) | [[Dinaciclib (drug)]] 5 µM 0.365× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.508× (z -9.8) |
| [[SW48 (line)]] | wt | 396 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +22.3) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -20.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 493 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +32.8) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -15.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 488 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +30.3) | — |
| [[HepG2_C3A (line)]] | wt | 413 | 4 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.580× (z -8.5) |
| [[HOP62 (line)]] | alt | 468 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +20.4) | [[Dinaciclib (drug)]] 5 µM 0.460× (z -10.9) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 492 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +24.2) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -15.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 414 | 5 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +23.5) | [[Dinaciclib (drug)]] 0.05 µM 0.419× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 401 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +29.4) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -25.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 329 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +17.9) | — |
| [[CFPAC-1 (line)]] | alt | 586 | 1 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +26.2) | [[Dinaciclib (drug)]] 5 µM 0.399× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.542× (z -11.8) |
| [[HCT15 (line)]] | alt | 511 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.469× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 370 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.486× (z -8.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 517 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +28.7) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.595× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 427 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +37.0) | [[Dinaciclib (drug)]] 5 µM 0.404× (z -15.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 500 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +37.7) | [[Dinaciclib (drug)]] 5 µM 0.480× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 432 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +39.5) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -12.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 654 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -11.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 390 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +32.1) | — |
| [[HS-578T (line)]] | alt | 319 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +22.4) | — |
| [[SNU-1 (line)]] | wt | 440 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +12.8) | — |
| [[J82 (line)]] | alt | 327 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +27.9) | — |
| [[SHP-77 (line)]] | alt | 371 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 1.99× (z +11.7) | — |
| [[A549 (line)]] | wt | 434 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +36.7) | — |
| [[CHP-212 (line)]] | wt | 716 | 2 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.25× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.378× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 478 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -15.2) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 582 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.30× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.480× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 477 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -8.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 380 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.1) | — |
| [[SW 1271 (line)]] | alt | 334 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +10.2) | — |
| [[NCI-H2122 (line)]] | alt | 527 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 528 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf56]] | +0.73 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[TERF2IP]] | +0.72 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.71 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[YTHDC1]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[SYNRG]] | +0.71 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[DNASE1]] | +0.70 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[GPBP1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[ZMYM5]] | +0.69 | +0.65 / +0.65 | both halves | 7e-06 | STRING 410 |
| [[RSF1]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 | STRING 672 |
| [[SMIM27]] | +0.69 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[CD27-AS1]] | +0.68 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[C2]] | +0.67 | +0.58 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.70 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[CS]] | -0.67 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | -0.67 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[FARSB]] | -0.66 | -0.43 / -0.72 | both halves | 3e-05 |  |
| [[PRPS1]] | -0.65 | -0.59 / -0.62 | both halves | 7e-06 |  |
| [[PPP5C]] | -0.65 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[PRPF19]] | -0.65 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[MTG1]] | -0.64 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[CAD]] | -0.64 | -0.60 / -0.64 | both halves | 7e-06 |  |
| [[ADAMTSL5]] | -0.64 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[BOP1]] | -0.64 | -0.61 / -0.58 | both halves | 7e-06 | same gene group |
| [[TFDP1]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYF2]] | C | ARID4B's natural level weakens SYF2's drug response | ARID4B's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.33; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 231]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.875). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.2, -40.0); signed map (-7.5, 4.8). **Vector** length 124, 56.4% of its response variance represented; |z| ≥ 3 in 1,428 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +12.9 | +9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.0 | +11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | -0.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.6 | +0.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.5 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.1 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.5 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -6.2 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -5.8 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.5 | -8.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.1 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.7 | -2.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.7 | -1.3 |
|  | [[EX229 (drug)]] 5 µM |  | -3.5 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | AT-rich interaction domain 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.3 — chr1:235,131,634-235,328,219 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BCAA, BRCAA1, SAP180; previously RBP1L1 |
| Gene groups (HGNC) | AT-rich interaction domain containing; MicroRNA protein coding host genes |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 9 pathways, smallest: HDACs deacetylate histones; NoRC negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4LE39](https://www.uniprot.org/uniprotkb/Q4LE39) (AT-rich interactive domain-containing protein 4B):

> Acts as a transcriptional repressor. May function in the assembly and/or enzymatic activity of the Sin3A corepressor complex or in mediating interactions between the complex and other regulatory complexes. Plays a role in the regulation of epigenetic modifications at the PWS/AS imprinting center near the SNRPN promoter, where it might function as part of a complex with RB1 and ARID4A. Involved in spermatogenesis, together with ARID4A, where it functions as a transcriptional coactivator for AR …

**Summary**, from NCBI Gene [51742](https://www.ncbi.nlm.nih.gov/gene/51742):

> This gene encodes a protein with sequence similarity to retinoblastoma-binding protein-1. The encoded protein is a subunit of the histone deacetylase-dependant SIN3A transcriptional corepressor complex, which functions in diverse cellular processes including proliferation, differentiation, apoptosis, oncogenesis, and cell fate determination. The gene product is recognized by IgG antibody isolated from a breast cancer patient and appears to be a molecular marker associated with a broad range of …

**Accessions** — [HGNC:15550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15550) · Entrez [51742](https://www.ncbi.nlm.nih.gov/gene/51742) · UniProt [Q4LE39](https://www.uniprot.org/uniprotkb/Q4LE39) · Ensembl [ENSG00000054267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000054267)

## Data

Gene col 605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 605); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 605]; `tensor/DDL_lfc|DDL_z.npy` [605]; `embed/gene_vectors.npy` [605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 605 or target_col == 605). Every well: [[ARID4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARID4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
