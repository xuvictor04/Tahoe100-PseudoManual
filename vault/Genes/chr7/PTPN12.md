---
symbol: "PTPN12"
type: "gene"
col: 4845
ensembl_id: "ENSG00000127947"
name: "protein tyrosine phosphatase non-receptor type 12"
location: "7q11.23"
module: 174
arm: "+"
pooled_cpm: 451.43
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 48
n_dd_up_clean: 5
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 11
direction_downstream: 0
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# PTPN12

*protein tyrosine phosphatase non-receptor type 12* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.33× (z +6.2, q 3e-07, up in 33 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.29× (z +5.6, q 6e-06, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.530× (z -19.2, q 0e+00, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHC2]] (+0.79, fdr 7e-06), [[NIBAN2]] (+0.73, fdr 7e-06), [[ITGB5]] (+0.71, fdr 7e-06); moves opposite to [[ZSCAN31]] (-0.55, fdr 3e-05), [[EPB41]] (-0.53, fdr 1e-05).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC02320]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4845.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.2 | 3e-07 | 33/48 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 6e-06 | 31/48 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.4 | 1e-05 | 27/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.64×** | +5.0 | 9e-05 | 31/48 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.6 | 6e-04 | 32/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.51×** | +4.2 | 0.002 | 28/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.13 | 16/48 (SW480, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 16 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4845.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.530×** | -19.2 | 0e+00 | 43/48 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.544×** | -18.4 | 0e+00 | 44/49 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.526×** | -13.7 | 1e-40 | 41/48 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.599×** | -11.0 | 8e-26 | 39/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.604×** | -10.8 | 5e-25 | 44/48 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.679×** | -10.2 | 3e-22 | 41/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -9.9 | 5e-21 | 41/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.607×** | -9.7 | 3e-20 | 38/48 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.628×** | -9.6 | 6e-20 | 37/47 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.639×** | -9.6 | 6e-20 | 37/49 (C32, AsPC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.629×** | -9.2 | 2e-18 | 29/45 (C32, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.643×** | -9.1 | 5e-18 | 38/48 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.649×** | -8.9 | 3e-17 | 32/44 (AsPC-1, C32, …) | all doses, flat | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.664×** | -8.7 | 9e-17 | 38/49 (NCI-H23, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.676×** | -8.4 | 2e-15 | 36/48 (H4, HS-578T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.717×** | -8.1 | 2e-14 | 38/50 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.723×** | -7.9 | 1e-13 | 34/49 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.738×** | -7.8 | 3e-13 | 39/48 (C32, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.723×** | -6.9 | 1e-10 | 37/47 (C32, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.802×** | -6.6 | 8e-10 | 28/48 (NCI-H2347, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4845. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 750 | 0 | 28 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -26.3) |
| [[C32 (line)]] | wt | 1,007 | 0 | 26 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -27.4) |
| [[CFPAC-1 (line)]] | alt | 692 | 0 | 19 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -23.1) |
| [[NCI-H1573 (line)]] | alt | 656 | 0 | 18 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -25.7) |
| [[SK-MEL-2 (line)]] | alt | 492 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -16.7) |
| [[HOP62 (line)]] | alt | 469 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -18.2) |
| [[HS-578T (line)]] | alt | 424 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -23.2) |
| [[MIA PaCa-2 (line)]] | alt | 717 | 0 | 11 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.553× (z -27.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.349× (z -20.1) |
| [[LoVo (line)]] | wt | 345 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -29.9) |
| [[NCI-H2347 (line)]] | alt | 533 | 0 | 10 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -18.5) |
| [[A549 (line)]] | wt | 551 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -24.8) |
| [[J82 (line)]] | alt | 349 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -19.0) |
| [[NCI-H1792 (line)]] | alt | 876 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -24.4) |
| [[A-172 (line)]] | wt | 338 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -17.8) |
| [[BT-474 (line)]] | alt | 343 | 4 (1 ⚠) | 4 | [[Digitoxin (drug)]] 0.5 µM 1.96× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -15.2) |
| [[NCI-H23 (line)]] | alt | 525 | 0 | 8 | — | [[Trametinib (drug)]] 5 µM 0.309× (z -15.9) |
| [[PANC-1 (line)]] | alt | 372 | 3 (2 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 1.88× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -13.7) |
| [[SW 900 (line)]] | alt | 379 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -13.2) |
| [[AsPC-1 (line)]] | alt | 897 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.407× (z -11.7) |
| [[COLO 205 (line)]] | alt | 329 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -21.7) |
| [[HepG2_C3A (line)]] | wt | 464 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.545× (z -13.1) |
| [[LOX-IMVI (line)]] | wt | 281 | 1 | 6 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.13× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -17.5) |
| [[SNU-423 (line)]] | alt | 483 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -19.3) |
| [[KATO III (line)]] | alt | 539 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -20.5) |
| [[SW480 (line)]] | alt | 323 | 3 (2 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 1.81× (z +10.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -12.7) |
| [[A498 (line)]] | wt | 415 | 2 (1 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.75× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.525× (z -15.9) |
| [[HT-29 (line)]] | alt | 486 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 369 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.473× (z -10.9) |
| [[Panc 03.27 (line)]] | alt | 422 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.494× (z -15.4) |
| [[HEC-1-A (line)]] | alt | 348 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.490× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.628× (z -11.2) |
| [[LS 180 (line)]] | wt | 279 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -19.2) |
| [[SW1417 (line)]] | alt | 378 | 1 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.69× (z +8.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.481× (z -10.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 321 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.309× (z -13.1) |
| [[Hs 766T (line)]] | wt | 367 | 1 | 1 | [[Clobetasol propionate (drug)]] 5 µM 1.90× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.535× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 367 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -16.1) |
| [[SW48 (line)]] | wt | 372 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -12.0) |
| [[A-427 (line)]] | wt | 224 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -11.5) |
| [[AN3 CA (line)]] | alt | 269 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -9.0) |
| [[HCT15 (line)]] | alt | 207 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -13.4) |
| [[SHP-77 (line)]] | alt | 225 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.528× (z -9.7) |
| [[SW 1088 (line)]] | alt | 597 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -14.2) |
| [[C-33 A (line)]] | alt | 199 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 222 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 675 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 464 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 236 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 272 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 182 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 374 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4845), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2]] | +0.79 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[NIBAN2]] | +0.73 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[ITGB5]] | +0.71 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[TBC1D8]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[TOP1]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[HPCAL1]] | +0.67 | +0.76 / +0.56 | both halves | 1e-05 |  |
| [[SLC20A1]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[PITPNC1]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[RGS17]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN31]] | -0.55 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[EPB41]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 7, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02320]] | B | LINC02320 activity raises PTPN12's level | lines that do not express LINC02320 (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without LINC02320 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000258919, TSPAN1, ENSG00000266088 |
| [[MAP2K1]] | B | MAP2K1 activity raises PTPN12's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.8% of all compounds | 0.038 | ⚠ off-target possible; 4 compounds |
| [[ST3GAL1]] | B | ST3GAL1 activity raises PTPN12's level | lines that do not express ST3GAL1 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without ST3GAL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: IL1RAP, FBXO32, PLSCR2 |
| [[NIBAN2]] | B | NIBAN2 activity raises PTPN12's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.89× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SMOX]] | B | SMOX activity raises PTPN12's level | lines that do not express SMOX (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without SMOX | 0.072 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[TGFBR2]] | B | TGFBR2 activity raises PTPN12's level | lines that do not express TGFBR2 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without TGFBR2 | 0.086 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[ITGA3]] | B | ITGA3 activity raises PTPN12's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without ITGA3 | 0.089 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[STX1A]] | C | STX1A activity strengthens PTPN12's drug response | lines that do not express STX1A (3) vs lines expressing it (46) | the lines without STX1A respond 0.22× as strongly (z diff +3.81); strongest at Dinaciclib 0.5 µM: 1.25x vs 0.62x (z diff +7.7) | 0.030 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TIMP1]] | C | TIMP1 activity raises PTPN12's level | lines that do not express TIMP1 (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without TIMP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: COTL1, OSBPL3, IGF2BP2; maybe low, not absent; its own permutation p |
| [[STX1A]] | C | STX1A activity raises PTPN12's level | lines that do not express STX1A (3) vs lines expressing it (47) | 1.99× lower at baseline in the lines without STX1A | 0.071 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[ERRFI1]] | C | ERRFI1 activity strengthens PTPN12's drug response | lines that do not express ERRFI1 (4) vs lines expressing it (45) | the lines without ERRFI1 respond 0.45× as strongly (z diff +2.98); strongest at Idarubicin (hydrochloride) 5 µM: 0.86x vs 0.51x (z diff +5.3) | 0.081 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000256029; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.4, 5.5); signed map (7.3, 48.1). **Vector** length 127, 54.5% of its response variance represented; |z| ≥ 3 in 2,219 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +6.8 | -10.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | -13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +1.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.6 | -11.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.6 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.9 | +1.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +3.4 | +1.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.3 | -0.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -10.2 | -8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.8 | -9.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.7 | -10.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.5 | -7.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.4 | -8.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -8.3 | -7.8 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:77,537,295-77,640,069 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTPG1, PTP-PEST |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type |
| Reactome | 14 pathways, smallest: Constitutive Signaling by Overexpressed ERBB2; Interleukin-37 signaling; SHC1 events in ERBB2 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05209](https://www.uniprot.org/uniprotkb/Q05209) (Tyrosine-protein phosphatase non-receptor type 12):

> Dephosphorylates a range of proteins, and thereby regulates cellular signaling cascades. Dephosphorylates cellular tyrosine kinases, such as ERBB2 and PTK2B/PYK2, and thereby regulates signaling via ERBB2 and PTK2B/PYK2. Selectively dephosphorylates ERBB2 phosphorylated at 'Tyr-1112', 'Tyr-1196', and/or 'Tyr-1248'.

**Summary**, from NCBI Gene [5782](https://www.ncbi.nlm.nih.gov/gene/5782):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains a C-terminal PEST motif, which serves as a protein-protein interaction domain, and may regulate protein intracellular half-life. This PTP was found to bind and dephosphorylate the product of the oncogene c-ABL and thus may …

**Accessions** — [HGNC:9645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9645) · Entrez [5782](https://www.ncbi.nlm.nih.gov/gene/5782) · UniProt [Q05209](https://www.uniprot.org/uniprotkb/Q05209) · Ensembl [ENSG00000127947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127947)

## Data

Gene col 4845: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4845); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4845, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4845]; `tensor/DDL_lfc|DDL_z.npy` [4845]; `embed/gene_vectors.npy` [4845]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4845 or target_col == 4845). Every well: [[PTPN12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
