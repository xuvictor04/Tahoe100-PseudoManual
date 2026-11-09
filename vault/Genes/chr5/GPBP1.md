---
symbol: "GPBP1"
type: "gene"
col: 708
ensembl_id: "ENSG00000062194"
name: "GC-rich promoter binding protein 1"
location: "5q11.2"
module: 231
arm: "+"
pooled_cpm: 294.31
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/231"]
generated_by: "tahoemap"
---

# GPBP1

*GC-rich promoter binding protein 1* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.19× (z +26.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.484× (z -17.0, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (CFPAC-1 0.324×, A-427 0.325×, Panc 03.27 0.345×, NCI-H2347 0.364×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.401×, CFPAC-1 0.394×, A-427 0.428×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.498×; ⚠ cell-cycle shift, explains ~37% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID4B]] (+0.70, fdr 7e-06), [[RSRC2]] (+0.69, fdr 7e-06), [[DCP1A]] (+0.66, fdr 1e-05); moves opposite to [[DCTD]] (-0.64, fdr 7e-06), [[ARHGAP4]] (-0.61, fdr 4e-05), [[ITPR3]] (-0.60, fdr 1e-05).
> It is in [[Module 231]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +26.9 | 0e+00 | 47/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.85×** | +20.1 | 0e+00 | 48/49 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.04×** | +17.3 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +17.1 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +16.1 | 0e+00 | 44/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +15.3 | 0e+00 | 46/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.59×** | +12.1 | 1e-31 | 46/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.62×** | +11.8 | 4e-30 | 44/48 (SW1417, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +10.9 | 4e-26 | 45/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +9.6 | 4e-20 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +9.5 | 8e-20 | 30/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +9.5 | 9e-20 | 37/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +7.8 | 3e-13 | 33/48 (A-427, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.28×** | +5.7 | 4e-07 | 30/48 (CFPAC-1, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.26×** | +5.6 | 8e-07 | 32/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 2e-04 | 33/49 (RKO, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.17× | +3.6 | 0.009 | 17/49 (A-172, SNU-423, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.4 | 0.019 | 18/49 (A-427, C-33 A, …) | top dose only |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.15× | +3.3 | 0.024 | 13/49 (A-172, HepG2/C3A, …) | rises with dose | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 708.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (CFPAC-1 0.324×, A-427 0.325×, Panc 03.27 0.345×, NCI-H2347 0.364×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (NCI-H2347 0.401×, CFPAC-1 0.394×, A-427 0.428×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A549 0.498×; ⚠ cell-cycle shift, explains ~37% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -17.0 | 0e+00 | 42/44 (CFPAC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.585×** | -12.1 | 4e-31 | 41/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.536×** | -10.1 | 7e-22 | 47/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.695×** | -8.9 | 9e-17 | 39/48 (CFPAC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.755×** | -6.9 | 7e-10 | 32/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.859× | -5.3 | 1e-05 | 20/49 (A549, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.831×** | -4.5 | 4e-04 | 24/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **0.828×** | -4.4 | 6e-04 | 25/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.874× | -3.3 | 0.058 | 14/48 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.060 | 8/48 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.882× | -3.1 | 0.10 | 5/48 (NCI-H1792, LoVo, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.879× | -3.0 | 0.10 | 9/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | 0.879× | -3.0 | 0.10 | 11/49 (SW48, NCI-H2122, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 283 | 14 (4 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.29× (z +20.2) | [[Dinaciclib (drug)]] 5 µM 0.520× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 271 | 14 (6 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +30.6) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -14.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 431 | 12 (2 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.75× (z +25.4) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.27× (z +23.1) | [[Dinaciclib (drug)]] 5 µM 0.501× (z -13.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 321 | 9 (2 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +17.7) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -13.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 249 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +37.2) | — |
| [[A-427 (line)]] | wt | 368 | 8 (1 ⚠) | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.62× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -19.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 264 | 9 (2 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.42× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.479× (z -11.3) ⚠ cell-cycle shift, explains ~67% of this change |
| [[SW 900 (line)]] | alt | 399 | 9 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +19.8) | [[Dinaciclib (drug)]] 5 µM 0.447× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 303 | 8 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +21.8) | [[Dinaciclib (drug)]] 5 µM 0.322× (z -18.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 437 | 3 | 7 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +19.6) | [[Dinaciclib (drug)]] 5 µM 0.324× (z -19.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 268 | 7 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +18.1) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -13.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 273 | 10 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.5) | — |
| [[A498 (line)]] | wt | 264 | 6 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +31.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -11.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A549 (line)]] | wt | 259 | 6 (3 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.14× (z +31.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -15.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[C-33 A (line)]] | alt | 269 | 8 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -13.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 364 | 8 (4 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.77× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.58× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 290 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.580× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 231 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +18.8) | [[Dinaciclib (drug)]] 5 µM 0.400× (z -13.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 308 | 7 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +22.6) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -11.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 350 | 8 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.468× (z -9.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 207 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +16.5) | — |
| [[HEC-1-A (line)]] | alt | 190 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +20.0) | [[Panobinostat (drug)]] 0.5 µM 0.506× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 231 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +25.6) | — |
| [[KATO III (line)]] | alt | 241 | 7 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.569× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 258 | 6 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -13.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 387 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +22.7) | [[Dinaciclib (drug)]] 5 µM 0.339× (z -15.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 313 | 4 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.02× (z +16.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.413× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~56% of this change |
| [[NCI-H2030 (line)]] | alt | 301 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +19.4) | [[Dinaciclib (drug)]] 5 µM 0.514× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 702 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -19.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 311 | 6 (2 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.59× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.407× (z -10.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 326 | 6 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.50× (z +28.9) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 10.0× (z +19.4) | — |
| [[HOP62 (line)]] | alt | 123 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 281 | 4 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -12.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 228 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 396 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -19.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 240 | 5 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.86× (z +14.7) | [[Dinaciclib (drug)]] 0.05 µM 0.434× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 253 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +19.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.582× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~56% of this change |
| [[H4 (line)]] | wt | 216 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 191 | 4 (2 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.84× (z +20.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.482× (z -9.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 219 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +19.1) | — |
| [[HCT15 (line)]] | alt | 344 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.89× (z +13.7) | [[Dinaciclib (drug)]] 5 µM 0.437× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 219 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +14.8) | — |
| [[AN3 CA (line)]] | alt | 391 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.48× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -8.6) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HepG2_C3A (line)]] | wt | 256 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +14.5) | — |
| [[Hs 766T (line)]] | wt | 202 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.4) | — |
| [[SW 1088 (line)]] | alt | 368 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.7) | — |
| [[SW 1271 (line)]] | alt | 404 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.78× (z +8.7) | — |
| [[NCI-H2122 (line)]] | alt | 429 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 317 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 327 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[RSRC2]] | +0.69 | +0.60 / +0.68 | both halves | 7e-06 | STRING 465 |
| [[DCP1A]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[CHMP2B]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.63 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[C1orf56]] | +0.62 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[C11orf1]] | +0.62 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[PRRC2C]] | +0.61 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[WAC]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[YTHDC1]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTD]] | -0.64 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[ARHGAP4]] | -0.61 | -0.40 / -0.58 | both halves | 4e-05 |  |
| [[ITPR3]] | -0.60 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[MTG1]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NUP188]] | -0.59 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[TEX2]] | -0.59 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[UBE2G2]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CHID1]] | -0.57 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[TXNDC5]] | -0.57 | -0.36 / -0.58 | both halves | 9e-05 |  |
| [[E2F4]] | -0.57 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[TREX2]] | -0.56 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[QSOX2]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises GPBP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 231]]; 6 genes; every member is in the + arm (projection on the module's main direction 0.637). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.5, -30.0); signed map (-8.7, 2.4). **Vector** length 106, 42.4% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +6.8 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.6 | +7.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +26.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.7 | +15.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.6 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +5.5 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.9 | +0.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.9 | +9.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | +2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | +17.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | +9.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -2.9 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.8 | -1.3 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | GC-rich promoter binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:57,173,948-57,264,679 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp761C169 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86WP2](https://www.uniprot.org/uniprotkb/Q86WP2) (Vasculin):

> Functions as a GC-rich promoter-specific transactivating transcription factor.

**Summary**, from NCBI Gene [65056](https://www.ncbi.nlm.nih.gov/gene/65056):

> This gene was originally isolated by subtractive hybridization of cDNAs expressed in atherosclerotic plaques with a thrombus, and was found to be expressed only in vascular smooth muscle cells. However, a shorter splice variant was found to be more ubiquitously expressed. This protein is suggested to play a role in the development of atherosclerosis. Studies in mice suggest that it may also function as a GC-rich promoter-specific trans-activating transcription factor. Several alternatively …

**Accessions** — [HGNC:29520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29520) · Entrez [65056](https://www.ncbi.nlm.nih.gov/gene/65056) · UniProt [Q86WP2](https://www.uniprot.org/uniprotkb/Q86WP2) · Ensembl [ENSG00000062194](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062194)

## Data

Gene col 708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 708); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 708]; `tensor/DDL_lfc|DDL_z.npy` [708]; `embed/gene_vectors.npy` [708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 708 or target_col == 708). Every well: [[GPBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
