---
symbol: "SLC38A9"
type: "gene"
col: 10786
ensembl_id: "ENSG00000177058"
name: "solute carrier family 38 member 9"
location: "5q11.2"
module: 15
arm: "+"
pooled_cpm: 46.48
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 28
n_dd_up_clean: 15
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SLC38A9

*solute carrier family 38 member 9* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.49× (z +9.2, q 2e-17, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.362× (z -23.2, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.337× (z -17.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCT6P3-1]] (+0.62, fdr 2e-05), [[PGS1]] (+0.60, fdr 1e-05), [[WIPI2]] (+0.60, fdr 3e-05); moves opposite to [[RASEF]] (-0.60, fdr 1e-05), [[PER2]] (-0.55, fdr 1e-05), [[JUNB]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +9.2 | 2e-17 | 33/48 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +7.4 | 3e-11 | 32/48 (LS 180, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +6.4 | 3e-08 | 30/48 (CFPAC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +5.9 | 7e-07 | 33/48 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +5.5 | 4e-06 | 28/48 (SW 900, A-172, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.1 | 4e-05 | 26/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.8 | 1e-04 | 28/48 (LS 180, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.33×** | +4.6 | 3e-04 | 24/48 (NCI-H2347, MIA PaCa-2, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +4.6 | 3e-04 | 25/48 (NCI-H2347, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.4 | 6e-04 | 23/48 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 25/48 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.30×** | +4.1 | 0.002 | 20/47 (NCI-H1792, LS 180, …) | two highest doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.006 | 22/48 (LoVo, KATO III, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.010 | 15/49 (LoVo, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.16× | +3.5 | 0.017 | 11/48 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.24×** | +3.3 | 0.029 | 20/48 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.063 | 15/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 14 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.362×** | -23.2 | 0e+00 | 42/48 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.337×** | -17.6 | 0e+00 | 46/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.354×** | -16.1 | 0e+00 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.370×** | -16.1 | 0e+00 | 45/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.483×** | -11.3 | 9e-28 | 41/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.511×** | -10.9 | 2e-25 | 35/48 (Panc 03.27, NCI-H23, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.541×** | -9.6 | 8e-20 | 38/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.381×** | -8.2 | 2e-14 | 40/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.597×** | -8.0 | 7e-14 | 35/47 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.593×** | -7.8 | 3e-13 | 30/44 (NCI-H23, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.620×** | -7.4 | 6e-12 | 26/40 (A549, Panc 03.27, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.633×** | -7.4 | 7e-12 | 29/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.637×** | -7.3 | 1e-11 | 36/48 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.653×** | -6.9 | 2e-10 | 30/48 (NCI-H460, A-427, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.463×** | -6.5 | 3e-09 | 37/48 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.522×** | -5.5 | 1e-06 | 27/48 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.602×** | -4.3 | 5e-04 | 25/48 (SHP-77, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.604×** | -4.3 | 6e-04 | 25/48 (Hs 766T, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -4.0 | 0.001 | 22/48 (C32, A-427, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.622×** | -4.0 | 0.001 | 23/48 (PANC-1, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.722×** | -3.7 | 0.004 | 12/48 (LoVo, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.811×** | -3.4 | 0.017 | 14/48 (A-172, PANC-1, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.753×** | -3.3 | 0.025 | 11/48 (LOX-IMVI, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.812×** | -3.2 | 0.034 | 16/48 (CFPAC-1, SW480, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.703×** | -3.0 | 0.060 | 14/48 (NCI-H1792, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.837× | -2.9 | 0.082 | 10/48 (NCI-H460, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 61.0 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -31.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -22.9) |
| [[NCI-H460 (line)]] | wt | 42.2 | 0 | 13 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -22.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -17.8) |
| [[SW480 (line)]] | alt | 60.2 | 3 (1 ⚠) | 7 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -17.4) |
| [[A549 (line)]] | wt | 55.0 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -22.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LoVo (line)]] | wt | 64.1 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.153× (z -21.4) |
| [[NCI-H2030 (line)]] | alt | 61.0 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -17.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.8) |
| [[C32 (line)]] | wt | 45.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -18.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.231× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 38.5 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.238× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 93.4 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -12.6) |
| [[A-427 (line)]] | wt | 71.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -8.5) |
| [[A498 (line)]] | wt | 48.3 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.5) ⚠ cell-cycle shift, explains ~41% of this change |
| [[LOX-IMVI (line)]] | wt | 45.5 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 57.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -11.1) |
| [[SNU-1 (line)]] | wt | 39.7 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -12.5) |
| [[SNU-423 (line)]] | alt | 42.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -15.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.7) |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.177× (z -11.3) |
| [[HEC-1-A (line)]] | alt | 45.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -14.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HT-29 (line)]] | alt | 33.1 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.170× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -11.7) |
| [[J82 (line)]] | alt | 42.7 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -19.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -14.0) |
| [[KATO III (line)]] | alt | 33.6 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.230× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 27.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -10.2) |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -14.7) |
| [[A-172 (line)]] | wt | 41.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.9) ⚠ cell-cycle shift, explains ~41% of this change |
| [[AsPC-1 (line)]] | alt | 26.8 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -9.7) |
| [[RKO (line)]] | wt | 60.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -9.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -9.0) |
| [[SW 1271 (line)]] | alt | 112 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0649× (z -12.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 46.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.297× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.299× (z -8.6) |
| [[Hs 766T (line)]] | wt | 44.6 | 0 | 2 (1 ⚠) | — | [[TAK-733 (drug)]] 5 µM 0.0397× (z -12.8) |
| [[HS-578T (line)]] | alt | 41.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.4) ⚠ cell-cycle shift, explains ~41% of this change |
| [[hTERT-HPNE (line)]] | wt | 30.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.179× (z -10.1) ⚠ transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SK-MEL-2 (line)]] | alt | 50.5 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.162× (z -13.3) ⚠ cell-cycle shift, explains ~33% of this change |
| [[CFPAC-1 (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.3) ⚠ cell-cycle shift, explains ~41% of this change |
| [[COLO 205 (line)]] | alt | 49.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -14.0) ⚠ cell-cycle shift, explains ~41% of this change |
| [[HCT15 (line)]] | alt | 32.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -9.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -11.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -9.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[NCI-H1792 (line)]] | alt | 53.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -8.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 49.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.320× (z -8.9) |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW 900 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -9.7) ⚠ cell-cycle shift, explains ~41% of this change |
| [[SW48 (line)]] | wt | 42.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -11.5) |
| [[AN3 CA (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT6P3-1]] | +0.62 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[PGS1]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[WIPI2]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 | pathway: Autophagy |
| [[PIK3R4]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 | pathway: Autophagy |
| [[SAP30L]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[EIF4ENIF1]] | +0.58 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[NFATC2IP]] | +0.58 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[TRAPPC10]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ZNF277]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PTPN9]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[STARD3]] | +0.56 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[RNF13]] | +0.56 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASEF]] | -0.60 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[PER2]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[JUNB]] | -0.54 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[ATP7A]] | -0.54 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[CELSR3]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ENPP1]] | -0.52 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[NOTCH2NLC]] | -0.50 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[ZC3H11A]] | -0.50 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ABLIM1]] | -0.50 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[ARL5B]] | -0.49 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SRSF3]] | -0.49 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[TEF]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC38A9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FZD5]] | C | FZD5 activity raises SLC38A9's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without FZD5 | 0.034 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.5, 21.2); signed map (-44.8, 1.0). **Vector** length 89.6, 25.6% of its response variance represented; |z| ≥ 3 in 1,268 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.0 | -0.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | -0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | -0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -9.6 | -23.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.9 | -7.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -7.7 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.7 | -1.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -7.2 | -10.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -6.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.7 | -4.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:55,625,845-55,773,194 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90709, SNAT9 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Reactome | 15 pathways, smallest: mTORC1-mediated signalling; Energy dependent regulation of mTOR by LKB1-AMPK; MTOR signalling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBW4](https://www.uniprot.org/uniprotkb/Q8NBW4) (Neutral amino acid transporter 9):

> Lysosomal amino acid transporter involved in the activation of mTORC1 in response to amino acid levels. Probably acts as an amino acid sensor of the Rag GTPases and Ragulator complexes, 2 complexes involved in amino acid sensing and activation of mTORC1, a signaling complex promoting cell growth in response to growth factors, energy levels, and amino acids. Following activation by amino acids, the Ragulator and Rag GTPases function as a scaffold recruiting mTORC1 to lysosomes where it is in …

**Summary**, from NCBI Gene [153129](https://www.ncbi.nlm.nih.gov/gene/153129):

> Enables several functions, including L-amino acid transmembrane transporter activity; cholesterol binding activity; and guanyl-nucleotide exchange factor activity. Involved in carboxylic acid transport; cellular response to amino acid stimulus; and positive regulation of TORC1 signaling. Located in Ragulator complex; late endosome; and lysosomal membrane. Part of FNIP-folliculin RagC/D GAP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26907](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26907) · Entrez [153129](https://www.ncbi.nlm.nih.gov/gene/153129) · UniProt [Q8NBW4](https://www.uniprot.org/uniprotkb/Q8NBW4) · Ensembl [ENSG00000177058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177058)

## Data

Gene col 10786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10786); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10786]; `tensor/DDL_lfc|DDL_z.npy` [10786]; `embed/gene_vectors.npy` [10786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10786 or target_col == 10786). Every well: [[SLC38A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
