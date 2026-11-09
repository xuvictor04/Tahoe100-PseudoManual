---
symbol: "TRIM2"
type: "gene"
col: 3067
ensembl_id: "ENSG00000109654"
name: "tripartite motif containing 2"
location: "4q31.3"
module: 8
arm: "+"
pooled_cpm: 105.57
n_lines_expressing: 35
n_dd_up: 16
n_dd_down: 35
n_dd_up_clean: 13
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 33
direction_downstream: 11
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# TRIM2

*tripartite motif containing 2* — 4q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.53× (z +13.2, q 8e-37, up in 18 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.646× (z -13.4, q 2e-38, down in 26 of 33 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.610× (z -10.8, q 1e-24, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRK]] (+0.60, fdr 1e-05), [[PIP5K1B]] (+0.59, fdr 1e-05), [[ERBB3]] (+0.57, fdr 1e-05); moves opposite to [[TUBB6]] (-0.49, fdr 2e-05), [[ELL2]] (-0.49, fdr 4e-05), [[OSMR]] (-0.49, fdr 2e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[ADGRF1]] → it (grade B ⚠); 11 go from it, the strongest it → [[HSF2BP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3067.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.53×** | +13.2 | 8e-37 | 18/33 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +8.3 | 4e-14 | 15/34 (CFPAC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +8.2 | 4e-14 | 21/33 (SK-MEL-2, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.46×** | +7.8 | 1e-12 | 16/33 (H4, A-172, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +7.4 | 1e-11 | 12/34 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +7.2 | 7e-11 | 14/33 (NCI-H460, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.25×** | +7.0 | 3e-10 | 18/33 (SW480, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +5.4 | 6e-06 | 15/33 (SK-MEL-2, Hs 766T, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.25×** | +4.9 | 6e-05 | 12/33 (SW480, AsPC-1, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.24×** | +4.7 | 1e-04 | 17/33 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.25×** | +4.7 | 1e-04 | 16/33 (CFPAC-1, Panc 03.27, …) | top dose only | plate-row cell shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.24×** | +4.7 | 1e-04 | 17/33 (HT-29, KATO III, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.4 | 4e-04 | 10/34 (NCI-H460, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +4.4 | 4e-04 | 14/32 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.3 | 8e-04 | 12/32 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.15× | +4.2 | 9e-04 | 11/33 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | 1.14× | +4.1 | 0.001 | 15/34 (SW 900, HT-29, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.16× | +4.1 | 0.001 | 10/33 (C32, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3067.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.646×** | -13.4 | 2e-38 | 26/33 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.609×** | -10.8 | 1e-24 | 27/33 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.610×** | -10.8 | 1e-24 | 25/33 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.620×** | -10.4 | 3e-23 | 29/33 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.627×** | -10.2 | 3e-22 | 27/33 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -9.9 | 3e-21 | 27/34 (COLO 205, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -8.9 | 4e-17 | 22/32 (C32, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.680×** | -8.4 | 3e-15 | 22/33 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -7.7 | 1e-12 | 22/33 (RKO, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.710×** | -7.5 | 5e-12 | 21/33 (SW 900, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.705×** | -7.3 | 1e-11 | 22/33 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.741×** | -6.5 | 3e-09 | 23/33 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.744×** | -6.4 | 6e-09 | 19/32 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.812×** | -6.4 | 7e-09 | 23/34 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.741×** | -6.3 | 1e-08 | 18/32 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.583×** | -6.1 | 3e-08 | 18/33 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **0.588×** | -6.0 | 5e-08 | 22/32 (SNU-1, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.760×** | -6.0 | 7e-08 | 18/33 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.765×** | -5.6 | 6e-07 | 19/33 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.767×** | -5.3 | 3e-06 | 16/32 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.629×** | -5.3 | 3e-06 | 14/33 (NCI-H460, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -5.2 | 6e-06 | 22/33 (C32, SW480, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.718×** | -5.1 | 7e-06 | 11/33 (SNU-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3067. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 474 | 10 (1 ⚠) | 14 (10 ⚠) | [[Binimetinib (drug)]] 0.5 µM 2.81× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -14.7) |
| [[LoVo (line)]] | wt | 577 | 0 | 15 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -18.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -15.1) |
| [[LS 180 (line)]] | wt | 592 | 0 | 14 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.329× (z -13.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.167× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 91.9 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -20.4) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.212× (z -15.0) |
| [[SW480 (line)]] | alt | 78.7 | 1 (1 ⚠) | 12 (7 ⚠) | [[Selinexor (drug)]] 5 µM 1.96× (z +9.5) ⚠ cell-cycle shift, explains ~72% of this change | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -17.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -11.6) |
| [[COLO 205 (line)]] | alt | 525 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -26.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -16.7) |
| [[KATO III (line)]] | alt | 306 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -14.8) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -10.8) |
| [[SW1417 (line)]] | alt | 226 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -14.2) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.344× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 236 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -13.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.353× (z -9.1) |
| [[SW 900 (line)]] | alt | 70.0 | 0 | 6 (4 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.260× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.321× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 109 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.324× (z -10.5) |
| [[HT-29 (line)]] | alt | 65.4 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 41.7 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +11.8) | — |
| [[H4 (line)]] | wt | 45.5 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.25× (z +11.0) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.29× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 30.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.169× (z -10.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -11.3) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HepG2_C3A (line)]] | wt | 38.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.24× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 36.3 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.34× (z +8.5) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.2) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 8.58 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 23.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 25.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 13.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 55.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3067), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRK]] | +0.60 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PIP5K1B]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ERBB3]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ATP10B]] | +0.57 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CADPS]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[TMPRSS2]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TMPRSS3]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TANC1]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[QPRT]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[DNM3]] | +0.54 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[SLC44A4]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[USH1C]] | +0.54 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB6]] | -0.49 | -0.46 / -0.50 | both halves | 2e-05 | pathway: Interferon Signaling |
| [[ELL2]] | -0.49 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[OSMR]] | -0.49 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[AKAP12]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DUSP7]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[DLK2]] | -0.47 | -0.51 / -0.31 | both halves | 2e-04 |  |
| [[HSF2BP]] | -0.47 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[BCAR3]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CCM2]] | -0.46 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CLMP]] | -0.46 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ETS1]] | -0.45 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[STEAP3]] | -0.45 | -0.44 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 32, C 1. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADGRF1]] | B | ADGRF1 activity raises TRIM2's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.82× lower at baseline in the lines without ADGRF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[CLIC5]] | B | CLIC5 activity raises TRIM2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.71× lower at baseline in the lines without CLIC5 | 0.007 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[SLC44A4]] | B | SLC44A4 activity raises TRIM2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.41× lower at baseline in the lines without SLC44A4 | 0.007 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[ATP10B]] | B | ATP10B activity raises TRIM2's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 6.48× lower at baseline in the lines without ATP10B | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[LINC03040]] | B | LINC03040 activity raises TRIM2's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 3.48× lower at baseline in the lines without LINC03040 | 0.009 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[SLC40A1]] | B | SLC40A1 activity raises TRIM2's level | lines that do not express SLC40A1 (28) vs lines expressing it (22) | 1.89× lower at baseline in the lines without SLC40A1 | 0.016 | ⚠ within organs, on part of the lines; also absent: RASSF6, WFDC2, TOX3 |
| [[ERBB3]] | B | ERBB3 activity raises TRIM2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 3.43× lower at baseline in the lines without ERBB3 | 0.017 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[GCNT3]] | B | GCNT3 activity raises TRIM2's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.19× lower at baseline in the lines without GCNT3 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises TRIM2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 3.02× lower at baseline in the lines without TMPRSS2 | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[EPS8L3]] | B | EPS8L3 activity raises TRIM2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.81× lower at baseline in the lines without EPS8L3 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[SLC5A1]] | B | SLC5A1 activity raises TRIM2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.50× lower at baseline in the lines without SLC5A1 | 0.044 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises TRIM2's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.35× lower at baseline in the lines without ARHGEF38 | 0.044 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSF2BP]] | B | TRIM2 activity lowers HSF2BP's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 1.53× higher at baseline in the lines without TRIM2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[SNTB1]] | B | TRIM2 activity raises SNTB1's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 3.65× lower at baseline in the lines without TRIM2 | 0.019 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[SLC40A1]] | B | TRIM2 activity raises SLC40A1's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 2.16× lower at baseline in the lines without TRIM2 | 0.023 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[DNM3]] | B | TRIM2 activity raises DNM3's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 1.45× lower at baseline in the lines without TRIM2 | 0.025 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[DLG3]] | B | TRIM2 activity raises DLG3's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 2.43× lower at baseline in the lines without TRIM2 | 0.044 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[FRK]] | B | TRIM2 activity raises FRK's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 2.68× lower at baseline in the lines without TRIM2 | 0.055 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[HSF2BP]] | B | TRIM2 activity weakens HSF2BP's drug response | lines that do not express TRIM2 (15) vs lines expressing it (29) | the lines without TRIM2 respond 1.48× as strongly (z diff -0.81); strongest at Ouabain (Octahydrate) 5 µM: 0.26x vs 0.44x (z diff -2.4) | 0.058 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5; target measured in part of the lines; artifact flags |
| cells under [[Docetaxel (drug)]] 5 µM | B | TRIM2 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express TRIM2 (15) vs lines expressing it (33) | the lines without TRIM2: 0.92× the cells of the other lines | 0.060 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[STEAP3]] | B | TRIM2 activity lowers STEAP3's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 1.67× higher at baseline in the lines without TRIM2 | 0.062 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[ABO]] | B | TRIM2 activity raises ABO's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 3.25× lower at baseline in the lines without TRIM2 | 0.079 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |
| [[TUBB6]] | B | TRIM2 activity lowers TUBB6's level | lines that do not express TRIM2 (15) vs lines expressing it (35) | 2.51× higher at baseline in the lines without TRIM2 | 0.093 | ⚠ within organs, on part of the lines; also absent: MICE, TNFRSF14-AS1, ACSL5 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.545). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.7, 51.5); signed map (61.9, 3.5). **Vector** length 104, 26.5% of its response variance represented; |z| ≥ 3 in 1,296 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.2 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +5.5 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +13.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.7 | +0.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.4 | +4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.1 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +8.2 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -2.8 | -5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.7 | -4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.6 | -6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -6.4 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.3 — chr4:153,152,163-153,339,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0517, RNF86, CMT2R |
| Gene groups (HGNC) | Ring finger proteins; Tripartite motif family; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Interferon gamma signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C040](https://www.uniprot.org/uniprotkb/Q9C040) (Tripartite motif-containing protein 2):

> UBE2D1-dependent E3 ubiquitin-protein ligase that mediates the ubiquitination of NEFL and of phosphorylated BCL2L11. Plays a neuroprotective function. May play a role in neuronal rapid ischemic tolerance. Plays a role in antiviral immunity and limits New World arenavirus infection independently of its ubiquitin ligase activity.

**Summary**, from NCBI Gene [23321](https://www.ncbi.nlm.nih.gov/gene/23321):

> The protein encoded by this gene is a member of the tripartite motif (TRIM) family. The TRIM motif includes three zinc-binding domains, a RING, a B-box type 1 and a B-box type 2, and a coiled-coil region. The protein localizes to cytoplasmic filaments. It plays a neuroprotective role and functions as an E3-ubiquitin ligase in proteasome-mediated degradation of target proteins. Mutations in this gene can cause early-onset axonal neuropathy. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:15974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15974) · Entrez [23321](https://www.ncbi.nlm.nih.gov/gene/23321) · UniProt [Q9C040](https://www.uniprot.org/uniprotkb/Q9C040) · Ensembl [ENSG00000109654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109654)

## Data

Gene col 3067: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3067); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3067, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3067]; `tensor/DDL_lfc|DDL_z.npy` [3067]; `embed/gene_vectors.npy` [3067]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3067 or target_col == 3067). Every well: [[TRIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
