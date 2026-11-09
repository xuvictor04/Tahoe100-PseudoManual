---
symbol: "PAN3"
type: "gene"
col: 7639
ensembl_id: "ENSG00000152520"
name: "poly(A) specific ribonuclease subunit PAN3"
location: "13q12.2"
module: 225
arm: "+"
pooled_cpm: 296.58
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/225"]
generated_by: "tahoemap"
---

# PAN3

*poly(A) specific ribonuclease subunit PAN3* — 13q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.53× (z +9.1, q 4e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.297× (z -25.0, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.358× (z -22.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIAS1]] (+0.72, fdr 7e-06), [[FBXL20]] (+0.71, fdr 7e-06), [[GPBP1L1]] (+0.67, fdr 7e-06); moves opposite to [[CYCS]] (-0.51, fdr 1e-05), [[SLC35A4]] (-0.51, fdr 3e-04), [[LRRC59]] (-0.51, fdr 2e-04).
> It is in [[Module 225]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NOS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.53×** | +9.1 | 4e-17 | 40/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.7 | 4e-12 | 33/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.34×** | +6.3 | 6e-08 | 34/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +6.2 | 1e-07 | 37/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.81×** | +5.9 | 3e-07 | 36/49 (COLO 205, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +5.4 | 5e-06 | 40/48 (A-427, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.065 | 24/48 (BT-474, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.086 | 26/49 (AsPC-1, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.12 | 16/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | 1.36× | +3.0 | 0.14 | 21/49 (BT-474, J82, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.297×** | -25.0 | 0e+00 | 44/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.321×** | -24.4 | 0e+00 | 49/49 (J82, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.358×** | -22.0 | 0e+00 | 48/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.358×** | -22.0 | 0e+00 | 48/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.381×** | -19.1 | 0e+00 | 45/45 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.437×** | -17.8 | 0e+00 | 48/48 (AsPC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.499×** | -14.9 | 0e+00 | 44/48 (C32, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.650×** | -13.0 | 5e-37 | 35/48 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.538×** | -12.8 | 2e-35 | 46/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.613×** | -10.5 | 6e-24 | 46/48 (SW1417, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.668×** | -8.6 | 3e-16 | 41/48 (SW 900, HT-29, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.673×** | -8.5 | 1e-15 | 44/48 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.770×** | -7.9 | 1e-13 | 32/49 (A549, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.707×** | -7.4 | 5e-12 | 42/48 (SW48, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -7.4 | 7e-12 | 43/48 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.730×** | -6.7 | 5e-10 | 34/48 (SW480, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.803×** | -6.6 | 1e-09 | 40/48 (LOX-IMVI, SW 900, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.602×** | -5.1 | 1e-05 | 43/48 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.615×** | -4.8 | 4e-05 | 40/48 (MIA PaCa-2, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.627×** | -4.6 | 9e-05 | 36/48 (NCI-H23, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.628×** | -4.6 | 1e-04 | 39/49 (AsPC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.819×** | -4.3 | 5e-04 | 29/48 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.871× | -4.2 | 7e-04 | 17/48 (J82, NCI-H2347, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.672×** | -4.0 | 0.002 | 34/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 407 | 1 | 13 (8 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.19× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -23.0) |
| [[PANC-1 (line)]] | alt | 248 | 4 (1 ⚠) | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -13.4) |
| [[SW480 (line)]] | alt | 374 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.337× (z -19.9) |
| [[CFPAC-1 (line)]] | alt | 204 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.373× (z -16.0) |
| [[NCI-H1792 (line)]] | alt | 176 | 1 | 11 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -25.1) |
| [[Hs 766T (line)]] | wt | 358 | 2 (1 ⚠) | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -22.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.350× (z -15.5) |
| [[HT-29 (line)]] | alt | 716 | 0 | 11 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -16.2) |
| [[KATO III (line)]] | alt | 304 | 3 | 8 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -24.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.356× (z -15.3) |
| [[MIA PaCa-2 (line)]] | alt | 312 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -22.3) |
| [[NCI-H1573 (line)]] | alt | 265 | 2 (1 ⚠) | 9 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.211× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.418× (z -15.2) |
| [[SW 900 (line)]] | alt | 301 | 1 | 10 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.341× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 307 | 1 | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.218× (z -24.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.256× (z -22.0) |
| [[C32 (line)]] | wt | 487 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -20.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -19.7) |
| [[J82 (line)]] | alt | 333 | 1 | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.424× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 476 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -23.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.337× (z -18.8) |
| [[SNU-423 (line)]] | alt | 240 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.309× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -16.9) |
| [[SW1417 (line)]] | alt | 318 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.287× (z -19.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -18.8) |
| [[A-172 (line)]] | wt | 203 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -25.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.450× (z -11.9) |
| [[HOP62 (line)]] | alt | 235 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -21.2) |
| [[LoVo (line)]] | wt | 291 | 2 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -22.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 341 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0379× (z -49.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.320× (z -18.1) |
| [[NCI-H2347 (line)]] | alt | 246 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.278× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.370× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 236 | 2 (1 ⚠) | 7 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 1.68× (z +9.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 1.62× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.374× (z -17.7) |
| [[SK-MEL-2 (line)]] | alt | 183 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.457× (z -12.0) |
| [[COLO 205 (line)]] | alt | 914 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.05× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -23.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.337× (z -16.3) |
| [[HCT15 (line)]] | alt | 414 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.210× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.508× (z -11.3) |
| [[HepG2_C3A (line)]] | wt | 240 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 286 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.332× (z -19.1) |
| [[LS 180 (line)]] | wt | 337 | 1 | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +9.5) | [[Dinaciclib (drug)]] 0.05 µM 0.305× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -11.8) |
| [[RPMI-7951 (line)]] | alt | 239 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.359× (z -14.7) |
| [[SW48 (line)]] | wt | 361 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.345× (z -11.2) |
| [[A549 (line)]] | wt | 240 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -21.9) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.322× (z -18.0) |
| [[HEC-1-A (line)]] | alt | 247 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.300× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -14.1) |
| [[HS-578T (line)]] | alt | 150 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.519× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 198 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -11.9) |
| [[RKO (line)]] | wt | 291 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -12.5) |
| [[SNU-1 (line)]] | wt | 355 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -26.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.372× (z -13.1) |
| [[A498 (line)]] | wt | 233 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.384× (z -12.0) |
| [[BT-474 (line)]] | alt | 245 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -16.6) |
| [[C-33 A (line)]] | alt | 295 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.463× (z -8.9) |
| [[CHP-212 (line)]] | wt | 309 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.224× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.351× (z -10.0) |
| [[H4 (line)]] | wt | 228 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -13.8) |
| [[A-427 (line)]] | wt | 196 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.229× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.513× (z -9.2) |
| [[SHP-77 (line)]] | alt | 278 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -25.4) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 323 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.392× (z -8.5) |
| [[NCI-H661 (line)]] | alt | 290 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -11.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 239 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -8.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -8.7) |
| [[SW 1271 (line)]] | alt | 320 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.4) |
| [[NCI-H2122 (line)]] | alt | 361 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 343 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 9 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIAS1]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.71 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[GPBP1L1]] | +0.67 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[ZBTB44]] | +0.64 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TNRC6B]] | +0.63 | +0.45 / +0.58 | both halves | 3e-05 | STRING 464 |
| [[SPPL3]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TMEM59]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[AMBRA1]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[HIGD2A]] | +0.61 | +0.63 / +0.43 | both halves | 4e-05 |  |
| [[ELF2]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[CTSF]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CDK19]] | +0.59 | +0.46 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYCS]] | -0.51 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.51 | -0.75 / -0.27 | both halves | 3e-04 |  |
| [[LRRC59]] | -0.51 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[GZF1]] | -0.51 | -0.67 / -0.41 | both halves | 4e-05 |  |
| [[GTF2H3]] | -0.50 | -0.63 / -0.33 | both halves | 1e-04 |  |
| [[CSRP1]] | -0.50 | -0.52 / -0.28 | both halves | 3e-04 |  |
| [[ZSCAN22]] | -0.49 | -0.39 / -0.40 | both halves | 6e-05 |  |
| [[ZKSCAN2]] | -0.49 | -0.54 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOS3]] | B | NOS3 activity raises PAN3's level | lines that do not express NOS3 (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without NOS3 | 0.016 | ⚠ within organs, on part of the lines; also absent: ABO, GJB3, SYK |
| [[FAM217A]] | C | FAM217A's natural level strengthens PAN3's drug response | FAM217A's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.08; direction not clear | 0.030 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 225]]; 9 genes; every member is in the + arm (projection on the module's main direction 0.745). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.3, -42.0); signed map (-15.1, 12.2). **Vector** length 92.3, 40.7% of its response variance represented; |z| ≥ 3 in 1,569 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +5.0 | -7.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +5.0 | -3.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | -2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.1 | -0.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.0 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.9 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.8 | -14.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.7 | -13.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.2 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.1 | -6.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.0 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -4.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.5 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -4.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | poly(A) specific ribonuclease subunit PAN3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.2 — chr13:28,138,506-28,295,335 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers CCCH-type |
| Reactome | 3 pathways, smallest: Deadenylation of mRNA; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q58A45](https://www.uniprot.org/uniprotkb/Q58A45) (PAN2-PAN3 deadenylation complex subunit PAN3):

> Regulatory subunit of the poly(A)-nuclease (PAN) deadenylation complex, one of two cytoplasmic mRNA deadenylases involved in general and miRNA-mediated mRNA turnover. PAN specifically shortens poly(A) tails of RNA and the activity is stimulated by poly(A)-binding protein (PABP). PAN deadenylation is followed by rapid degradation of the shortened mRNA tails by the CCR4-NOT complex. Deadenylated mRNAs are then degraded by two alternative mechanisms, namely exosome-mediated 3'-5' exonucleolytic …

**Summary**, from NCBI Gene [255967](https://www.ncbi.nlm.nih.gov/gene/255967):

> Contributes to poly(A)-specific ribonuclease activity. Involved in nuclear-transcribed mRNA poly(A) tail shortening. Part of PAN complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29991) · Entrez [255967](https://www.ncbi.nlm.nih.gov/gene/255967) · UniProt [Q58A45](https://www.uniprot.org/uniprotkb/Q58A45) · Ensembl [ENSG00000152520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152520)

## Data

Gene col 7639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7639); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7639]; `tensor/DDL_lfc|DDL_z.npy` [7639]; `embed/gene_vectors.npy` [7639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7639 or target_col == 7639). Every well: [[PAN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
