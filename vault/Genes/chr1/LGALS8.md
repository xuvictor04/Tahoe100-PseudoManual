---
symbol: "LGALS8"
type: "gene"
col: 3860
ensembl_id: "ENSG00000116977"
name: "galectin 8"
location: "1q43"
module: 77
arm: "-"
pooled_cpm: 80.02
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# LGALS8

*galectin 8* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.65× (z +34.4, q 0e+00, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.576× (z -13.7, q 4e-40, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKT1S1]] (+0.63, fdr 1e-05), [[ZBTB1]] (+0.62, fdr 1e-05), [[SMCR8]] (+0.60, fdr 1e-05); moves opposite to [[VKORC1L1]] (-0.61, fdr 1e-05), [[FAR1]] (-0.61, fdr 1e-05), [[TMEM120B]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.65×** | +34.4 | 0e+00 | 43/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +19.5 | 0e+00 | 40/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +17.2 | 0e+00 | 40/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +15.8 | 0e+00 | 35/46 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +11.7 | 1e-29 | 41/46 (LS 180, COLO 205, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +11.4 | 7e-28 | 36/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +10.1 | 7e-22 | 38/46 (LS 180, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +8.8 | 1e-16 | 36/46 (LS 180, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +8.3 | 5e-15 | 24/47 (NCI-H2347, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +7.4 | 7e-12 | 27/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +5.6 | 1e-06 | 24/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.4 | 5e-04 | 20/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +4.3 | 8e-04 | 21/47 (AsPC-1, SW1417, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | 1.17× | +3.9 | 0.004 | 19/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.004 | 16/40 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.004 | 14/45 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.16× | +3.5 | 0.014 | 12/47 (A-172, PANC-1, …) | top dose only | plate-row cell shift |
| [[Roxadustat (drug)]] 5 µM |  | 1.14× | +3.2 | 0.045 | 9/46 (NCI-H1573, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3860.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.576×** | -13.7 | 4e-40 | 37/46 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -12.9 | 1e-35 | 38/46 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.621×** | -11.8 | 4e-30 | 35/46 (SW 900, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.687×** | -9.3 | 2e-18 | 32/46 (SW 900, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.742×** | -7.4 | 1e-11 | 29/46 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -6.2 | 7e-08 | 25/45 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.640×** | -5.8 | 6e-07 | 22/47 (RKO, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -5.2 | 1e-05 | 16/46 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.835× | -4.5 | 5e-04 | 20/46 (PANC-1, SW480, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.727×** | -4.1 | 0.002 | 17/46 (NCI-H460, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.899× | -3.7 | 0.011 | 9/47 (C32, CFPAC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.773×** | -3.3 | 0.038 | 16/46 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.774×** | -3.3 | 0.038 | 18/46 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.914× | -3.2 | 0.065 | 9/46 (NCI-H1573, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 143 | 12 (5 ⚠) | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +39.8) | [[Belinostat (drug)]] 5 µM 0.425× (z -14.1) |
| [[SW480 (line)]] | alt | 98.0 | 8 (3 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +36.8) | [[Belinostat (drug)]] 5 µM 0.364× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 67.3 | 9 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +23.5) | — |
| [[NCI-H2347 (line)]] | alt | 99.8 | 4 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +16.2) | [[Panobinostat (drug)]] 0.5 µM 0.448× (z -11.8) |
| [[SW 900 (line)]] | alt | 150 | 2 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +24.5) | [[Panobinostat (drug)]] 5 µM 0.284× (z -16.3) |
| [[A-172 (line)]] | wt | 124 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +29.1) | [[Panobinostat (drug)]] 5 µM 0.464× (z -8.8) |
| [[COLO 205 (line)]] | alt | 105 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +13.8) | [[Panobinostat (drug)]] 0.5 µM 0.367× (z -10.5) |
| [[LS 180 (line)]] | wt | 60.8 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +20.4) | — |
| [[NCI-H1573 (line)]] | alt | 106 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +37.2) | — |
| [[PANC-1 (line)]] | alt | 92.9 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +21.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.418× (z -10.8) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 75.9 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -15.0) |
| [[SW1417 (line)]] | alt | 69.8 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +25.3) | — |
| [[AsPC-1 (line)]] | alt | 53.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +26.2) | — |
| [[CFPAC-1 (line)]] | alt | 124 | 1 | 4 | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -16.9) |
| [[HOP62 (line)]] | alt | 68.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.8) | — |
| [[HT-29 (line)]] | alt | 71.7 | 2 | 3 | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.390× (z -10.3) |
| [[J82 (line)]] | alt | 79.1 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +22.3) | [[Panobinostat (drug)]] 0.5 µM 0.398× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 109 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.401× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 118 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.349× (z -12.5) |
| [[A549 (line)]] | wt | 57.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +28.4) | [[Dinaciclib (drug)]] 5 µM 0.443× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 157 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.412× (z -9.9) |
| [[RKO (line)]] | wt | 102 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.261× (z -14.3) |
| [[SW48 (line)]] | wt | 149 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.16× (z +23.4) | [[Panobinostat (drug)]] 5 µM 0.420× (z -8.8) |
| [[A-427 (line)]] | wt | 95.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +12.2) | — |
| [[LoVo (line)]] | wt | 30.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.37× (z +10.9) | — |
| [[NCI-H2030 (line)]] | alt | 49.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +18.4) | — |
| [[Panc 03.27 (line)]] | alt | 58.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +13.2) | — |
| [[AN3 CA (line)]] | alt | 70.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 106 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +9.9) | — |
| [[C32 (line)]] | wt | 137 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.442× (z -8.6) |
| [[H4 (line)]] | wt | 63.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 84.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 68.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +18.4) | — |
| [[hTERT-HPNE (line)]] | wt | 79.4 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +8.5) | — |
| [[KATO III (line)]] | alt | 32.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 27.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 47.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 72.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +16.5) | — |
| [[SHP-77 (line)]] | alt | 72.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.65× (z +9.0) | — |
| [[A498 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 62.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1S1]] | +0.63 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ZBTB1]] | +0.62 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[SMCR8]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[C11orf58]] | +0.59 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[SUPT7L]] | +0.58 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[AK9]] | +0.58 | +0.51 / +0.32 | both halves | 2e-04 |  |
| [[ZNF436]] | +0.58 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ARMT1]] | +0.57 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[MRPL45]] | +0.57 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[GGPS1]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TAPBPL]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[UBXN4]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[FAR1]] | -0.61 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.60 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TSEN54]] | -0.59 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[GFOD2]] | -0.59 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[SOCS7]] | -0.58 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[TOMM5]] | -0.58 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[CYTH3]] | -0.57 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[RAP1A]] | -0.57 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[NUP93]] | -0.56 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[TAF5L]] | -0.56 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[SMARCD2]] | -0.56 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises LGALS8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-3.0, 1.7); signed map (19.3, -21.2). **Vector** length 123, 35.2% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.5 | +34.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.5 | +17.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.4 | +19.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.2 | +15.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.9 | +11.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +11.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +1.1 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.3 | -6.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -4.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -13.7 |
|  | [[EX229 (drug)]] 5 µM |  | -4.1 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -9.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.2 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.0 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | galectin 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:236,518,000-236,552,981 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PCTA-1 |
| Gene groups (HGNC) | Galectins |
| Matched by | ensembl_id |

**Function**, from UniProt [O00214](https://www.uniprot.org/uniprotkb/O00214) (Galectin-8):

> Beta-galactoside-binding lectin that acts as a sensor of membrane damage caused by infection and restricts the proliferation of infecting pathogens by targeting them for autophagy. Detects membrane rupture by binding beta-galactoside ligands located on the lumenal side of the endosome membrane; these ligands becoming exposed to the cytoplasm following rupture. Restricts infection by initiating autophagy via interaction with CALCOCO2/NDP52. Required to restrict infection of bacterial invasion …

**Summary**, from NCBI Gene [3964](https://www.ncbi.nlm.nih.gov/gene/3964):

> This gene encodes a member of the galectin family. Galectins are beta-galactoside-binding animal lectins with conserved carbohydrate recognition domains. The galectins have been implicated in many essential functions including development, differentiation, cell-cell adhesion, cell-matrix interaction, growth regulation, apoptosis, and RNA splicing. This gene is widely expressed in tumoral tissues and seems to be involved in integrin-like cell interactions. Alternatively spliced transcript …

**Accessions** — [HGNC:6569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6569) · Entrez [3964](https://www.ncbi.nlm.nih.gov/gene/3964) · UniProt [O00214](https://www.uniprot.org/uniprotkb/O00214) · Ensembl [ENSG00000116977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116977)

## Data

Gene col 3860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3860); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3860]; `tensor/DDL_lfc|DDL_z.npy` [3860]; `embed/gene_vectors.npy` [3860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3860 or target_col == 3860). Every well: [[LGALS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGALS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
