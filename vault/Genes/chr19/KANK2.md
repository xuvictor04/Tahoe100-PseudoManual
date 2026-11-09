---
symbol: "KANK2"
type: "gene"
col: 12369
ensembl_id: "ENSG00000197256"
name: "KN motif and ankyrin repeat domains 2"
location: "19p13.2"
module: 85
arm: "+"
pooled_cpm: 29.76
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# KANK2

*KN motif and ankyrin repeat domains 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.96× (z +18.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.464× (z -14.7, q 0e+00, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (77 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.65, fdr 5e-05), [[CYTH1]] (+0.64, fdr 1e-05), [[CABLES2]] (+0.64, fdr 4e-05); moves opposite to [[YARS2]] (-0.65, fdr 7e-05), [[THAP2]] (-0.64, fdr 3e-04), [[RWDD2B]] (-0.62, fdr 0.001, ⚠ one half only (not replicated)), [[MFF-DT]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SORT1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12369.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.96×** | +18.7 | 0e+00 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.87×** | +18.4 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.11×** | +15.4 | 0e+00 | 46/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +8.0 | 2e-13 | 41/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.74×** | +7.5 | 8e-12 | 29/43 (HS-578T, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.64×** | +6.5 | 1e-08 | 23/34 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.6 | 2e-06 | 30/48 (A-172, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 3e-05 | 27/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.91×** | +4.6 | 3e-04 | 26/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +4.5 | 4e-04 | 25/48 (PANC-1, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.39×** | +4.5 | 4e-04 | 24/48 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.005 | 15/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.055 | 16/48 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.082 | 17/47 (HS-578T, A498, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12369.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.464×** | -14.7 | 0e+00 | 38/47 (A-427, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.412×** | -12.0 | 9e-31 | 38/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.465×** | -9.9 | 5e-21 | 39/48 (NCI-H23, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.286×** | -8.9 | 1e-16 | 42/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -8.1 | 8e-14 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.678×** | -7.4 | 1e-11 | 34/47 (NCI-H2030, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.352×** | -7.4 | 1e-11 | 36/46 (NCI-H460, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -6.3 | 2e-08 | 30/47 (BT-474, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.615×** | -6.2 | 4e-08 | 32/48 (AN3 CA, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -5.9 | 2e-07 | 27/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -5.6 | 1e-06 | 27/48 (NCI-H460, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.681×** | -5.2 | 1e-05 | 26/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.693×** | -5.0 | 3e-05 | 26/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.718×** | -4.5 | 3e-04 | 25/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -3.8 | 0.005 | 20/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pentagastrin (drug)]] 5 µM |  | 0.842× | -3.3 | 0.034 | 10/48 (SHP-77, A498, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12369. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.4 | 3 | 8 | [[Panobinostat (drug)]] 0.5 µM 4.64× (z +12.6) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -14.0) |
| [[SW480 (line)]] | alt | 37.5 | 3 | 6 | [[Panobinostat (drug)]] 5 µM 3.70× (z +12.7) | [[Harringtonine (drug)]] 5 µM 0.228× (z -14.0) |
| [[A-427 (line)]] | wt | 38.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -25.5) |
| [[MIA PaCa-2 (line)]] | alt | 27.1 | 3 | 3 | [[Belinostat (drug)]] 5 µM 4.39× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.3) |
| [[A-172 (line)]] | wt | 77.1 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.13× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -9.2) |
| [[HOP62 (line)]] | alt | 26.1 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 4.06× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.0) |
| [[Hs 766T (line)]] | wt | 31.7 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 5.08× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.4) |
| [[HT-29 (line)]] | alt | 24.6 | 2 | 3 | [[Panobinostat (drug)]] 0.5 µM 3.39× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -16.1) |
| [[PANC-1 (line)]] | alt | 29.5 | 3 | 2 | [[Panobinostat (drug)]] 0.5 µM 3.85× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -17.6) |
| [[J82 (line)]] | alt | 63.6 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.51× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 30.3 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 5.05× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.4) |
| [[A549 (line)]] | wt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 11.5× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 51.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.3) |
| [[HS-578T (line)]] | alt | 31.4 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.71× (z +10.0) | — |
| [[LoVo (line)]] | wt | 17.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.49× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 14.2 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 6.24× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.44× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 24.9 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 3.45× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.109× (z -14.7) |
| [[RKO (line)]] | wt | 16.5 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 9.99× (z +11.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.0689× (z -13.2) |
| [[SNU-423 (line)]] | alt | 34.9 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.4) |
| [[A498 (line)]] | wt | 37.6 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.67× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.1) |
| [[H4 (line)]] | wt | 20.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 8.71× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 70.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -18.6) |
| [[HEC-1-A (line)]] | alt | 36.4 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.78× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.0) |
| [[hTERT-HPNE (line)]] | wt | 20.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.18× (z +9.9) | — |
| [[KATO III (line)]] | alt | 21.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.92× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 45.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -17.3) |
| [[NCI-H2347 (line)]] | alt | 17.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.15× (z +9.2) | — |
| [[SW1417 (line)]] | alt | 30.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +10.4) | — |
| [[AsPC-1 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.7) |
| [[C-33 A (line)]] | alt | 42.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -9.4) |
| [[C32 (line)]] | wt | 23.7 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.22× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 9.31 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.67× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0498× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 47.2 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.12× (z +9.5) | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0552× (z -11.7) |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12369), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*33 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.65 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[CYTH1]] | +0.64 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[CABLES2]] | +0.64 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[TNK2]] | +0.64 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[GNAI2]] | +0.63 | +0.36 / +0.34 | both halves | 1e-04 |  |
| [[FN3KRP]] | +0.63 | +0.43 / +0.31 | both halves | 2e-04 |  |
| [[PCMT1]] | +0.61 | +0.41 / +0.29 | both halves | 2e-04 |  |
| [[FANCE]] | +0.61 | +0.53 / +0.34 | both halves | 1e-04 |  |
| [[PBX4]] | +0.61 | +0.48 / +0.40 | both halves | 5e-05 |  |
| [[CEP131]] | +0.59 | +0.39 / +0.27 | both halves | 3e-04 |  |
| [[CYB5R3]] | +0.59 | +0.55 / +0.28 | both halves | 3e-04 |  |
| [[PEDS1]] | +0.58 | +0.39 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*67 of its nearest partners move opposite, 22 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YARS2]] | -0.65 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[THAP2]] | -0.64 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[RWDD2B]] | -0.62 | -0.54 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[MFF-DT]] | -0.62 | -0.37 / -0.27 | both halves | 3e-04 |  |
| [[ACAD11]] | -0.62 | -0.62 / -0.29 | both halves | 2e-04 |  |
| [[PCNX4-DT]] | -0.60 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.60 | -0.43 / -0.12 | ⚠ not reproduced | 0.002 |  |
| [[GALNT7-DT]] | -0.60 | -0.35 / -0.25 | both halves | 4e-04 |  |
| [[CFAP418-AS1]] | -0.60 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[PLBD1-AS1]] | -0.60 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[PPP1R12A-AS2]] | -0.60 | -0.43 / -0.07 | ⚠ not reproduced | 0.004 |  |
| [[ATE1OSP]] | -0.59 | -0.46 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[ZXDA]] | -0.59 | -0.48 / -0.29 | both halves | 3e-04 |  |
| [[MAD2L1-DT]] | -0.59 | -0.38 / -0.26 | both halves | 4e-04 |  |
| [[LINC02100]] | -0.59 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[TSTD3]] | -0.59 | -0.42 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORT1]] | B | SORT1 activity raises KANK2's level | lines that do not express SORT1 (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without SORT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000269755, ZNF20, ENSG00000289985; maybe low, not absent |
| [[SCGB2B2]] | C | SCGB2B2 activity lowers KANK2's level | lines that do not express SCGB2B2 (4) vs lines expressing it (46) | 1.99× higher at baseline in the lines without SCGB2B2 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.692). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.7, -0.7); signed map (-39.7, -3.2). **Vector** length 97.7, 26.9% of its response variance represented; |z| ≥ 3 in 1,194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.3 | +18.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.2 | +18.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.9 | +15.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.8 | +5.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +3.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.7 | -7.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.4 | -12.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -14.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -9.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -5.0 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | KN motif and ankyrin repeat domains 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:11,164,270-11,197,791 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1518, SIP; previously MXRA3, ANKRD25 |
| Gene groups (HGNC) | KN motif and ankyrin repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q63ZY3](https://www.uniprot.org/uniprotkb/Q63ZY3) (KN motif and ankyrin repeat domain-containing protein 2):

> Involved in transcription regulation by sequestering in the cytoplasm nuclear receptor coactivators such as NCOA1, NCOA2 and NCOA3. Involved in regulation of caspase-independent apoptosis by sequestering the pro-apoptotic factor AIFM1 in mitochondria. Pro-apoptotic stimuli can induce its proteasomal degradation allowing the translocation of AIFM1 to the nucleus to induce apoptosis. Involved in the negative control of vitamin D receptor signaling pathway. Involved in actin stress fibers …

**Summary**, from NCBI Gene [25959](https://www.ncbi.nlm.nih.gov/gene/25959):

> This gene encodes a member of the KN motif and ankyrin repeat domains (KANK) family of proteins, which play a role in cytoskeletal formation by regulating actin polymerization. The encoded protein functions in the sequestration of steroid receptor coactivators and possibly other proteins. Mutations in this gene are associated with impaired kidney podocyte function and nephrotic syndrome, and keratoderma and woolly hair. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:29300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29300) · Entrez [25959](https://www.ncbi.nlm.nih.gov/gene/25959) · UniProt [Q63ZY3](https://www.uniprot.org/uniprotkb/Q63ZY3) · Ensembl [ENSG00000197256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197256)

## Data

Gene col 12369: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12369); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12369, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12369]; `tensor/DDL_lfc|DDL_z.npy` [12369]; `embed/gene_vectors.npy` [12369]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12369 or target_col == 12369). Every well: [[KANK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KANK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
