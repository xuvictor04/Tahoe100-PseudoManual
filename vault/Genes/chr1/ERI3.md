---
symbol: "ERI3"
type: "gene"
col: 3906
ensembl_id: "ENSG00000117419"
name: "ERI1 exoribonuclease family member 3"
location: "1p34.1"
module: 36
arm: "+"
pooled_cpm: 66.51
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ERI3

*ERI1 exoribonuclease family member 3* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.76× (z +10.4, q 1e-22, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -22.1, q 0e+00, down in 47 of 48 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.557× (z -15.2, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WRN]] (+0.74, fdr 7e-06), [[CHCHD6]] (+0.73, fdr 7e-06), [[HERC2]] (+0.73, fdr 7e-06); moves opposite to [[SGO1-AS1]] (-0.64, fdr 2e-05), [[FAM200B]] (-0.61, fdr 5e-05), [[GPR137C]] (-0.61, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LHFPL6]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Adagrasib (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.76×** | +10.4 | 1e-22 | 38/48 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +10.4 | 1e-22 | 40/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.80×** | +10.2 | 5e-22 | 41/48 (NCI-H1573, PANC-1, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **1.48×** | +7.3 | 5e-11 | 33/48 (SW480, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +7.1 | 1e-10 | 33/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +6.3 | 2e-08 | 29/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +3.6 | 0.025 | 0/49 | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.15 | 12/48 (MIA PaCa-2, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.12× | +3.0 | 0.16 | 7/48 (CHP-212, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.428×** | -22.1 | 0e+00 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.557×** | -15.2 | 0e+00 | 40/48 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.451×** | -14.1 | 8e-43 | 43/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.622×** | -8.7 | 3e-16 | 35/48 (SW480, HOP62, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.631×** | -8.5 | 2e-15 | 35/48 (SW480, SW48, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.654×** | -7.8 | 4e-13 | 36/48 (SNU-423, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.659×** | -7.7 | 1e-12 | 34/48 (A-427, HS-578T, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.725×** | -5.9 | 2e-07 | 30/48 (NCI-H460, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **0.742×** | -5.5 | 2e-06 | 29/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.623×** | -4.6 | 3e-04 | 27/48 (MIA PaCa-2, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.772×** | -4.4 | 5e-04 | 22/45 (C-33 A, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~82% of this change | **0.788×** | -4.4 | 5e-04 | 24/47 (RPMI-7951, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.784×** | -4.3 | 7e-04 | 21/44 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.800×** | -4.1 | 0.002 | 22/48 (SW480, LS 180, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.816×** | -3.7 | 0.007 | 22/48 (SW48, Hs 766T, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.693×** | -3.5 | 0.014 | 21/48 (COLO 205, A498, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.781×** | -3.1 | 0.060 | 15/48 (MIA PaCa-2, RKO, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.090 | 15/48 (A-172, RKO, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.738×** | -2.9 | 0.097 | 16/48 (SHP-77, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 59.5 | 3 | 7 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +14.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -13.1) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.438× (z -11.0) |
| [[HOP62 (line)]] | alt | 75.8 | 4 (1 ⚠) | 5 (4 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +10.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.39× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -18.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 104 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -25.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.427× (z -9.4) |
| [[PANC-1 (line)]] | alt | 102 | 2 (2 ⚠) | 6 (5 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.18× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -25.1) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 50.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -23.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -11.3) |
| [[A-172 (line)]] | wt | 48.1 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.323× (z -11.4) |
| [[A498 (line)]] | wt | 95.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -23.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -12.7) |
| [[C32 (line)]] | wt | 60.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -16.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -9.4) |
| [[HS-578T (line)]] | alt | 96.0 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -18.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 82.9 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -19.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -13.8) |
| [[AN3 CA (line)]] | alt | 94.5 | 0 | 4 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0710× (z -15.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[OTS514 (drug)]] 5 µM 0.0719× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 60.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.7) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 48.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.27× (z +12.3) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.88× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[NCI-H2030 (line)]] | alt | 101 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.529× (z -9.7) |
| [[RKO (line)]] | wt | 77.5 | 0 | 4 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.238× (z -13.5) |
| [[RPMI-7951 (line)]] | alt | 65.5 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -15.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -13.1) |
| [[SNU-423 (line)]] | alt | 65.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -22.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.259× (z -14.2) |
| [[SW48 (line)]] | wt | 70.6 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -10.2) |
| [[A-427 (line)]] | wt | 91.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -20.8) ⚠ cell-cycle shift, explains ~37% of this change |
| [[HCT15 (line)]] | alt | 77.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.467× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 68.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -14.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[Hs 766T (line)]] | wt | 62.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -13.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[hTERT-HPNE (line)]] | wt | 54.0 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.7) |
| [[J82 (line)]] | alt | 70.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -18.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LS 180 (line)]] | wt | 38.9 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.445× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 154 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0927× (z -27.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SNU-1 (line)]] | wt | 80.7 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.7) |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -12.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -8.7) |
| [[C-33 A (line)]] | alt | 104 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[H4 (line)]] | wt | 116 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -14.6) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -11.8) |
| [[LoVo (line)]] | wt | 55.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -10.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 43.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 26.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[CHP-212 (line)]] | wt | 44.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -9.8) |
| [[KATO III (line)]] | alt | 50.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 30.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.65× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 65.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW1417 (line)]] | alt | 45.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRN]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | same gene group |
| [[CHCHD6]] | +0.73 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[HERC2]] | +0.73 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[HERC2P9]] | +0.72 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[HERC2P2]] | +0.72 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[IPO11]] | +0.70 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[UBAC2]] | +0.67 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[MRPS27]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.66 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[SPATA5]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[EXOC2]] | +0.66 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[DFFB]] | +0.65 | +0.63 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1-AS1]] | -0.64 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[FAM200B]] | -0.61 | -0.67 / -0.40 | both halves | 5e-05 |  |
| [[GPR137C]] | -0.61 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[MAP3K2-DT]] | -0.61 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[MALINC1]] | -0.59 | -0.59 / -0.36 | both halves | 9e-05 |  |
| [[NPHS1]] | -0.59 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[DPY19L2P2]] | -0.58 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[CPEB2]] | -0.58 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[TRIM69]] | -0.58 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[FBXO48]] | -0.58 | -0.64 / -0.43 | both halves | 3e-05 |  |
| [[EMSY-DT]] | -0.57 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[WAC-AS1]] | -0.57 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHFPL6]] | B | LHFPL6 activity raises ERI3's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.55× lower at baseline in the lines without LHFPL6 | 0.007 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |
| [[OVOL1]] | B | OVOL1 activity lowers ERI3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.49× higher at baseline in the lines without OVOL1 | 0.012 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[DUXAP9]] | B | DUXAP9 activity raises ERI3's level | lines that do not express DUXAP9 (8) vs lines expressing it (42) | 1.51× lower at baseline in the lines without DUXAP9 | 0.053 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, TTYH2; maybe low, not absent |
| [[DUXAP10]] | B | DUXAP10 activity raises ERI3's level | lines that do not express DUXAP10 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without DUXAP10 | 0.055 | ⚠ within organs, on part of the lines; also absent: DUXAP8, KLRG1, DUXAP9 |
| [[HDAC6]] | B | HDAC6 activity lowers ERI3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers ERI3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TSEN2]] | C | TSEN2 activity raises ERI3's level | lines that do not express TSEN2 (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without TSEN2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TMEM9B-AS1, NDC80, CSPG5; maybe low, not absent; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Adagrasib (drug)]] 0.5 µM | C | ERI3's natural level lowers the cells' numbers under Adagrasib 0.5 µM (makes them more sensitive) | ERI3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.409 over the table, 0.072 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | ERI3's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | ERI3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.491 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.711). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-7.9, -31.5); signed map (-15.6, -51.4). **Vector** length 125, 39.3% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +9.8 | +7.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | +9.6 | +10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.7 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +10.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +10.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -11.6 | -22.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.6 | -15.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -7.4 | -14.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -7.2 | -7.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.5 | -7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.0 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ERI1 exoribonuclease family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:44,221,070-44,355,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22943, PINT1; previously PRNPIP |
| Gene groups (HGNC) | Exonucleases |
| Matched by | ensembl_id |

UniProt [O43414](https://www.uniprot.org/uniprotkb/O43414) carries no function annotation.

**Summary**, from NCBI Gene [79033](https://www.ncbi.nlm.nih.gov/gene/79033):

> Enables RNA binding activity. Predicted to be involved in exonucleolytic trimming to generate mature 3'-end of 5.8S rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA) and negative regulation of regulatory ncRNA-mediated heterochromatin formation. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17276) · Entrez [79033](https://www.ncbi.nlm.nih.gov/gene/79033) · UniProt [O43414](https://www.uniprot.org/uniprotkb/O43414) · Ensembl [ENSG00000117419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117419)

## Data

Gene col 3906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3906); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3906]; `tensor/DDL_lfc|DDL_z.npy` [3906]; `embed/gene_vectors.npy` [3906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3906 or target_col == 3906). Every well: [[ERI3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERI3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
