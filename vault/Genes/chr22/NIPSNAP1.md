---
symbol: "NIPSNAP1"
type: "gene"
col: 11492
ensembl_id: "ENSG00000184117"
name: "nipsnap homolog 1"
location: "22q12.2"
module: 45
arm: "+"
pooled_cpm: 39.62
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 25
n_dd_up_clean: 4
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# NIPSNAP1

*nipsnap homolog 1* — 22q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +12.1, q 4e-31, up in 44 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.65× (z +6.6, q 5e-09, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.425× (z -11.3, q 4e-27, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SKIC3]] (+0.72, fdr 7e-06), [[RAB3A]] (+0.70, fdr 1e-05), [[SLC25A23]] (+0.69, fdr 1e-05); moves opposite to [[TLNRD1]] (-0.64, fdr 9e-06), [[NUP50-DT]] (-0.64, fdr 1e-05), [[AVEN]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[BCAM]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11492.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +12.1 | 4e-31 | 44/46 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.54×** | +11.9 | 5e-30 | 37/42 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +6.8 | 2e-09 | 31/44 (HEC-1-A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +6.6 | 5e-09 | 39/48 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.31×** | +5.0 | 5e-05 | 32/48 (AsPC-1, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.45×** | +4.9 | 8e-05 | 30/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.0 | 0.005 | 3/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.33×** | +3.7 | 0.013 | 25/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.017 | 25/48 (COLO 205, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +3.4 | 0.033 | 24/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.4 | 0.036 | 22/48 (COLO 205, LOX-IMVI, …) | rises with dose | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.067 | 20/46 (A-427, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11492.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.425×** | -11.3 | 4e-27 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -11.3 | 4e-27 | 41/48 (HT-29, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -11.0 | 6e-26 | 43/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.443×** | -10.7 | 9e-25 | 47/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.455×** | -10.4 | 4e-23 | 41/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.492×** | -9.3 | 9e-19 | 46/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.654×** | -5.6 | 2e-06 | 33/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.672×** | -5.0 | 3e-05 | 29/48 (AN3 CA, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.694×** | -4.8 | 9e-05 | 30/48 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.725×** | -4.0 | 0.004 | 23/47 (C32, RKO, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.755×** | -3.7 | 0.012 | 21/48 (HCT15, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.823×** | -3.6 | 0.015 | 21/48 (CHP-212, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.750×** | -3.6 | 0.016 | 18/48 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.770×** | -3.4 | 0.024 | 20/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.774×** | -3.4 | 0.029 | 20/48 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.615×** | -3.3 | 0.029 | 20/48 (PANC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.619×** | -3.3 | 0.032 | 16/48 (Hs 766T, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.779×** | -3.3 | 0.033 | 21/47 (HT-29, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11492. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 43.2 | 2 (2 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.60× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.1) |
| [[NCI-H460 (line)]] | wt | 30.5 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.41× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.4) |
| [[PANC-1 (line)]] | alt | 36.1 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.1) |
| [[LoVo (line)]] | wt | 34.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +12.7) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 0.5 µM 0.228× (z -12.0) |
| [[SNU-1 (line)]] | wt | 46.5 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -14.7) |
| [[HCT15 (line)]] | alt | 58.9 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.51× (z +8.6) ⚠ toxic; transcription drop | [[Niclosamide (olamine) (drug)]] 5 µM 0.237× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 32.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.45× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -12.4) |
| [[SW480 (line)]] | alt | 42.8 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.245× (z -13.2) |
| [[A-172 (line)]] | wt | 28.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.6) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 71.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.5) |
| [[CFPAC-1 (line)]] | alt | 38.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +8.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 74.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +14.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 53.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +10.5) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.355× (z -8.6) |
| [[MIA PaCa-2 (line)]] | alt | 53.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -10.3) |
| [[SW1417 (line)]] | alt | 45.5 | 2 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -11.6) |
| [[A-427 (line)]] | wt | 51.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -14.3) |
| [[A549 (line)]] | wt | 35.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +11.1) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 23.4 | 0 | 2 (1 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.221× (z -8.7) |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.4) |
| [[HS-578T (line)]] | alt | 51.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -9.5) |
| [[J82 (line)]] | alt | 18.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 22.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.197× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 42.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.25× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 59.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -9.0) |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -8.8) |
| [[AN3 CA (line)]] | alt | 67.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.106× (z -11.1) |
| [[BT-474 (line)]] | alt | 35.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.261× (z -8.8) |
| [[C-33 A (line)]] | alt | 64.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 50.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.44× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 26.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.0) |
| [[SHP-77 (line)]] | alt | 59.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11492), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKIC3]] | +0.72 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[RAB3A]] | +0.70 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.69 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[PAPSS1]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[TMEM9]] | +0.64 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ORC4]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.64 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MPP1]] | +0.64 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[IFT172]] | +0.64 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[CAT]] | +0.64 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[SCRN2]] | +0.63 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[CDON]] | +0.61 | +0.57 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TLNRD1]] | -0.64 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[NUP50-DT]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[AVEN]] | -0.63 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.60 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[ENOX2]] | -0.59 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.59 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[SPRY3]] | -0.57 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[ANKRD17-DT]] | -0.57 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[ITPA]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[AP5B1]] | -0.56 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[NUTM2B-AS1]] | -0.55 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[RAB30-DT]] | -0.55 | -0.37 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAM]] | B | BCAM activity raises NIPSNAP1's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.72× lower at baseline in the lines without BCAM | 0.015 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[CYB5A]] | B | CYB5A activity raises NIPSNAP1's level | lines that do not express CYB5A (6) vs lines expressing it (44) | 1.21× lower at baseline in the lines without CYB5A | 0.048 | ⚠ within organs, on part of the lines; also absent: FGF11 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers NIPSNAP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers NIPSNAP1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HACE1]] | C | HACE1 activity raises NIPSNAP1's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 1.82× lower at baseline in the lines without HACE1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (5.8, -7.8); signed map (-29.7, -5.7). **Vector** length 84.0, 22.0% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +6.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +3.5 | +4.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.4 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.1 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +1.9 | +1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.8 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -11.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -0.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.5 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | nipsnap homolog 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.2 — chr22:29,554,808-29,581,327 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPW8](https://www.uniprot.org/uniprotkb/Q9BPW8) (Protein NipSnap homolog 1):

> Protein involved in mitophagy by facilitating recruitment of the autophagy machinery required for clearance of damaged mitochondria. Accumulates on the mitochondria surface in response to mitochondrial depolarization and acts as a 'eat me' signal by recruiting proteins involved in selective autophagy, such as autophagy receptors (CALCOCO2/NDP52, NBR1, SQSTM1/p62, TAX1BP1 and WDFY3/ALFY) and ATG8 family proteins (MAP1LC3A, MAP1LC3B, MAP1LC3C, GABARAP, GABARAPL1 and GABARAPL2).

**Summary**, from NCBI Gene [8508](https://www.ncbi.nlm.nih.gov/gene/8508):

> This gene encodes a member of the NipSnap family of proteins that may be involved in vesicular transport. A similar protein in mice inhibits the calcium channel TRPV6, and is also localized to the inner mitochondrial membrane where it may play a role in mitochondrial DNA maintenance. A pseudogene of this gene is located on the short arm of chromosome 17. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:7827](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7827) · Entrez [8508](https://www.ncbi.nlm.nih.gov/gene/8508) · UniProt [Q9BPW8](https://www.uniprot.org/uniprotkb/Q9BPW8) · Ensembl [ENSG00000184117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184117)

## Data

Gene col 11492: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11492); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11492, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11492]; `tensor/DDL_lfc|DDL_z.npy` [11492]; `embed/gene_vectors.npy` [11492]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11492 or target_col == 11492). Every well: [[NIPSNAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIPSNAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
