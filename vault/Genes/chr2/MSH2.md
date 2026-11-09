---
symbol: "MSH2"
type: "gene"
col: 1732
ensembl_id: "ENSG00000095002"
name: "mutS homolog 2"
location: "2p21-p16.3"
module: 6
arm: "+"
pooled_cpm: 72.8
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MSH2

*mutS homolog 2* — 2p21-p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.90× (z +15.9, q 0e+00, up in 39 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.22× (z +5.0, q 5e-05, up in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 2.37×, NCI-H2347 2.63×, NCI-H1792 3.55×, RPMI-7951 3.87×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 3.14×, KATO III 3.11×, SNU-423 2.92×, CFPAC-1 2.69×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 2.47×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.315× (z -40.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMS22L]] (+0.81, fdr 7e-06), [[DSCC1]] (+0.80, fdr 7e-06), [[RAD51]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1732.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (PANC-1 2.37×, NCI-H2347 2.63×, NCI-H1792 3.55×, RPMI-7951 3.87×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change); [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 3.14×, KATO III 3.11×, SNU-423 2.92×, CFPAC-1 2.69×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2347 2.47×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.90×** | +15.9 | 0e+00 | 39/49 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.87×** | +15.0 | 0e+00 | 36/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.43×** | +9.0 | 6e-17 | 34/48 (A549, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.43×** | +8.9 | 7e-17 | 31/48 (A549, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.38×** | +8.0 | 2e-13 | 30/48 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +5.9 | 4e-07 | 26/48 (A549, Panc 03.27, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.23×** | +5.2 | 2e-05 | 20/48 (SW480, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.22×** | +5.0 | 3e-05 | 24/48 (AsPC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +5.0 | 5e-05 | 22/48 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.21×** | +4.5 | 5e-04 | 22/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +4.2 | 0.001 | 14/48 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 13/49 (AsPC-1, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.11× | +3.8 | 0.007 | 6/48 (SK-MEL-2, PANC-1, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.13× | +3.1 | 0.068 | 6/48 (A498, SW480, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | 1.09× | +3.1 | 0.084 | 7/49 (SW480, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1732.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.315×** | -40.5 | 0e+00 | 44/48 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.365×** | -25.0 | 0e+00 | 43/48 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.434×** | -19.9 | 0e+00 | 42/48 (COLO 205, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.483×** | -18.1 | 0e+00 | 43/48 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.531×** | -15.7 | 0e+00 | 37/47 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.624×** | -11.7 | 1e-29 | 32/48 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -11.2 | 2e-27 | 33/48 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.658×** | -10.4 | 3e-23 | 31/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -10.3 | 4e-23 | 34/49 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.732×** | -7.7 | 7e-13 | 29/48 (A498, SW1417, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.578×** | -7.1 | 6e-11 | 29/48 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.746×** | -6.8 | 4e-10 | 28/48 (A-427, A498, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.761×** | -6.7 | 7e-10 | 28/48 (Panc 03.27, COLO 205, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 0.846× | -5.8 | 2e-07 | 18/48 (SHP-77, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.855× | -5.5 | 2e-06 | 17/48 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.855× | -5.5 | 2e-06 | 15/49 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.665×** | -5.3 | 4e-06 | 18/48 (A498, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.821×** | -4.9 | 4e-05 | 21/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1732. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 237 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -45.5) |
| [[MIA PaCa-2 (line)]] | alt | 99.7 | 1 (1 ⚠) | 7 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -28.7) |
| [[NCI-H460 (line)]] | wt | 49.3 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -29.2) |
| [[A-427 (line)]] | wt | 189 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -28.7) |
| [[A498 (line)]] | wt | 97.5 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -25.2) |
| [[HOP62 (line)]] | alt | 66.9 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -24.8) |
| [[NCI-H1573 (line)]] | alt | 36.2 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.93× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -11.6) |
| [[PANC-1 (line)]] | alt | 66.2 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -28.2) |
| [[A549 (line)]] | wt | 42.6 | 4 (4 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -13.6) |
| [[COLO 205 (line)]] | alt | 71.5 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.169× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 55.9 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0664× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.8) |
| [[LOX-IMVI (line)]] | wt | 98.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -34.7) |
| [[NCI-H2030 (line)]] | alt | 87.3 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -31.7) |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.8) |
| [[A-172 (line)]] | wt | 75.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 127 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -23.3) |
| [[Hs 766T (line)]] | wt | 37.9 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.09× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -18.0) |
| [[Panc 03.27 (line)]] | alt | 77.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -26.3) |
| [[CFPAC-1 (line)]] | alt | 48.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.9) |
| [[KATO III (line)]] | alt | 78.6 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -18.2) |
| [[HS-578T (line)]] | alt | 36.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.6) |
| [[NCI-H1792 (line)]] | alt | 35.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -10.8) |
| [[NCI-H2347 (line)]] | alt | 39.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -12.3) |
| [[RKO (line)]] | wt | 72.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -27.5) |
| [[RPMI-7951 (line)]] | alt | 43.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.5) |
| [[SNU-423 (line)]] | alt | 52.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -18.3) |
| [[SW1417 (line)]] | alt | 72.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -14.5) |
| [[SW480 (line)]] | alt | 106 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -25.2) |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -12.3) |
| [[BT-474 (line)]] | alt | 45.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.8) |
| [[HT-29 (line)]] | alt | 46.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -14.1) |
| [[LS 180 (line)]] | wt | 50.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.6) |
| [[SHP-77 (line)]] | alt | 189 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.89× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | [[Artesunate (drug)]] 5 µM 0.641× (z -8.8) ⚠ cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -20.5) |
| [[SNU-1 (line)]] | wt | 78.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.7) |
| [[SW48 (line)]] | wt | 88.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -14.2) |
| [[CHP-212 (line)]] | wt | 43.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0904× (z -10.9) |
| [[H4 (line)]] | wt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.4) |
| [[J82 (line)]] | alt | 67.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[LoVo (line)]] | wt | 31.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW 1271 (line)]] | alt | 71.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0969× (z -8.6) |
| [[AN3 CA (line)]] | alt | 81.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 94.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1732), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMS22L]] | +0.81 | +0.80 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[DSCC1]] | +0.80 | +0.79 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 405 |
| [[RAD51]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 | pathway: Diseases of DNA repair; STRING 944 |
| [[CDC45]] | +0.78 | +0.78 / +0.77 | both halves | 7e-06 | STRING 635 |
| [[BLM]] | +0.78 | +0.79 / +0.72 | both halves | 7e-06 | same gene group; pathway: Diseases of DNA repair; STRING 907 |
| [[NCAPD3]] | +0.78 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[POLE2]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | STRING 579 |
| [[RFC4]] | +0.77 | +0.78 / +0.72 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 935 |
| [[EXO1]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins; STRING 999 |
| [[FANCI]] | +0.77 | +0.78 / +0.73 | both halves | 7e-06 | pathway: TP53 Regulates Transcription of DNA Repair Genes; STRING 784 |
| [[DDX12P]] | +0.76 | +0.74 / +0.70 | both halves | 7e-06 |  |
| [[HAUS1]] | +0.76 | +0.78 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises MSH2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without CDC25A | 0.069 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises MSH2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.67× lower at baseline in the lines without E2F2 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers MSH2's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SHMT1]] | C | SHMT1 activity raises MSH2's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 2.25× lower at baseline in the lines without SHMT1 | 0.094 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.801). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-32.4, -44.6); signed map (-36.4, -42.5). **Vector** length 113, 35.0% of its response variance represented; |z| ≥ 3 in 1,407 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.64 to 28); *DNA Replication* (reactome, mean cos +0.64 to 40); *E2F G1/S* (control, mean cos +0.65 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +5.7 | +9.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.0 | +5.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +4.1 | +8.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.4 | +5.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +3.3 | +8.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +4.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.6 | +1.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +2.5 | +0.5 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +2.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.2 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -40.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.2 | -25.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -19.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -10.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.0 | -1.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | mutS homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21-p16.3 — chr2:47,403,067-47,663,146 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNPCC, HNPCC1, MSH-2; previously COCA1 |
| Gene groups (HGNC) | MutS homologs; BRCA1-associated genome surveillance complex |
| Hallmark sets | PEROXISOME, E2F_TARGETS |
| Reactome | 14 pathways, smallest: Defective Mismatch Repair Associated With MSH2; Diseases of Mismatch Repair (MMR); Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta) |
| Matched by | ensembl_id |

**Function**, from UniProt [P43246](https://www.uniprot.org/uniprotkb/P43246) (DNA mismatch repair protein Msh2):

> Component of the post-replicative DNA mismatch repair system (MMR). Forms two different heterodimers: MutS alpha (MSH2-MSH6 heterodimer) and MutS beta (MSH2-MSH3 heterodimer) which binds to DNA mismatches thereby initiating DNA repair. When bound, heterodimers bend the DNA helix and shields approximately 20 base pairs. MutS alpha recognizes single base mismatches and dinucleotide insertion-deletion loops (IDL) in the DNA. MutS beta recognizes larger insertion-deletion loops up to 13 nucleotides …

**Summary**, from NCBI Gene [4436](https://www.ncbi.nlm.nih.gov/gene/4436):

> This locus is frequently mutated in hereditary nonpolyposis colon cancer (HNPCC). When cloned, it was discovered to be a human homolog of the E. coli mismatch repair gene mutS, consistent with the characteristic alterations in microsatellite sequences (RER+ phenotype) found in HNPCC. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:7325](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7325) · Entrez [4436](https://www.ncbi.nlm.nih.gov/gene/4436) · UniProt [P43246](https://www.uniprot.org/uniprotkb/P43246) · Ensembl [ENSG00000095002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095002)

## Data

Gene col 1732: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1732); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1732, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1732]; `tensor/DDL_lfc|DDL_z.npy` [1732]; `embed/gene_vectors.npy` [1732]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1732 or target_col == 1732). Every well: [[MSH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
