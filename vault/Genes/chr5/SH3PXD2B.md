---
symbol: "SH3PXD2B"
type: "gene"
col: 10516
ensembl_id: "ENSG00000174705"
name: "SH3 and PX domains 2B"
location: "5q35.1"
module: 95
arm: "-"
pooled_cpm: 73.39
n_lines_expressing: 48
n_dd_up: 12
n_dd_down: 26
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# SH3PXD2B

*SH3 and PX domains 2B* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.43× (z +10.5, q 3e-23, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.243× (z -41.6, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD27]] (+0.75, fdr 1e-05), [[SLC27A1]] (+0.70, fdr 3e-05), [[MAST1]] (+0.68, fdr 1e-05); moves opposite to [[OARD1]] (-0.71, fdr 1e-05), [[INO80D]] (-0.70, fdr 3e-05), [[PPP3CB-AS1]] (-0.70, fdr 7e-05).
> It sits in the **-** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +10.5 | 3e-23 | 33/46 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.64×** | +10.4 | 1e-22 | 31/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.56×** | +9.2 | 7e-18 | 33/46 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +8.9 | 6e-17 | 30/46 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +8.4 | 5e-15 | 35/47 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +8.2 | 2e-14 | 28/46 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.33×** | +5.9 | 2e-07 | 24/47 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.67×** | +5.6 | 1e-06 | 26/47 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +5.6 | 1e-06 | 23/45 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 1e-05 | 22/45 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.29×** | +4.8 | 8e-05 | 23/46 (NCI-H460, BT-474, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.20×** | +3.8 | 0.006 | 17/46 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.20× | +3.7 | 0.011 | 13/46 (CFPAC-1, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.18× | +3.5 | 0.017 | 12/46 (SW1417, hTERT-HPNE, …) | top dose only |  |
| [[Meloxicam (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.051 | 13/46 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.064 | 16/45 (HOP62, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.243×** | -41.6 | 0e+00 | 45/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.340×** | -31.8 | 0e+00 | 44/47 (HS-578T, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.223×** | -31.2 | 0e+00 | 46/46 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.219×** | -30.4 | 0e+00 | 42/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.341×** | -22.4 | 0e+00 | 42/46 (PANC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.409×** | -18.6 | 0e+00 | 43/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.403×** | -18.2 | 0e+00 | 39/46 (SNU-423, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.427×** | -17.7 | 0e+00 | 41/46 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.445×** | -15.6 | 0e+00 | 34/41 (SK-MEL-2, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.520×** | -13.6 | 3e-40 | 40/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.509×** | -13.5 | 7e-40 | 40/48 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.300×** | -13.1 | 1e-37 | 43/47 (SK-MEL-2, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.548×** | -12.5 | 2e-34 | 40/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.582×** | -11.3 | 8e-28 | 31/43 (A-172, H4, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.688×** | -11.0 | 2e-26 | 37/46 (A-172, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.637×** | -9.4 | 2e-19 | 35/46 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.452×** | -8.7 | 2e-16 | 31/46 (A-172, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.660×** | -8.6 | 2e-16 | 35/46 (NCI-H2347, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 183 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0989× (z -35.6) |
| [[H4 (line)]] | wt | 133 | 0 | 17 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -25.9) |
| [[HS-578T (line)]] | alt | 260 | 0 | 14 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.169× (z -29.9) |
| [[LoVo (line)]] | wt | 39.4 | 6 (3 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.18× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.74× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.183× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.187× (z -18.2) |
| [[PANC-1 (line)]] | alt | 85.8 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -41.0) |
| [[C32 (line)]] | wt | 108 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -24.2) |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -25.5) |
| [[SK-MEL-2 (line)]] | alt | 167 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -35.5) |
| [[HOP62 (line)]] | alt | 114 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -21.1) |
| [[RPMI-7951 (line)]] | alt | 195 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -25.3) |
| [[SNU-423 (line)]] | alt | 184 | 0 | 12 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -28.2) |
| [[NCI-H460 (line)]] | wt | 39.1 | 0 | 10 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.155× (z -20.6) |
| [[Panc 03.27 (line)]] | alt | 29.4 | 3 | 7 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.41× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -20.2) |
| [[SW 900 (line)]] | alt | 79.6 | 2 | 8 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -19.9) |
| [[SW480 (line)]] | alt | 26.8 | 5 | 5 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.52× (z +13.4) | [[Harringtonine (drug)]] 5 µM 0.220× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 38.1 | 3 | 6 | [[Tucidinostat (drug)]] 5 µM 1.93× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -23.9) |
| [[NCI-H23 (line)]] | alt | 62.1 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0897× (z -24.2) |
| [[hTERT-HPNE (line)]] | wt | 68.6 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -20.3) |
| [[NCI-H2347 (line)]] | alt | 86.2 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.3) |
| [[A-427 (line)]] | wt | 46.7 | 2 | 5 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 46.8 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0568× (z -25.6) |
| [[NCI-H1573 (line)]] | alt | 44.2 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.66× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -17.5) |
| [[RKO (line)]] | wt | 31.5 | 1 | 6 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.43× (z +8.6) | [[Harringtonine (drug)]] 5 µM 0.0223× (z -24.9) |
| [[A498 (line)]] | wt | 120 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -18.1) |
| [[AN3 CA (line)]] | alt | 136 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -17.7) |
| [[BT-474 (line)]] | alt | 36.5 | 1 | 5 | [[Tucidinostat (drug)]] 5 µM 2.87× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.0) |
| [[CHP-212 (line)]] | wt | 152 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0428× (z -17.9) |
| [[J82 (line)]] | alt | 58.8 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -13.8) |
| [[KATO III (line)]] | alt | 48.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -20.0) |
| [[LS 180 (line)]] | wt | 31.2 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 63.6 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -21.7) |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -28.0) |
| [[SW1417 (line)]] | alt | 32.9 | 1 | 5 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -16.5) |
| [[A549 (line)]] | wt | 53.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -29.2) |
| [[CFPAC-1 (line)]] | alt | 52.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -20.2) |
| [[HCT15 (line)]] | alt | 81.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -16.3) |
| [[C-33 A (line)]] | alt | 70.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -19.5) |
| [[HepG2_C3A (line)]] | wt | 44.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -17.4) |
| [[SW48 (line)]] | wt | 39.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0903× (z -15.1) |
| [[Hs 766T (line)]] | wt | 27.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.3) |
| [[COLO 205 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0786× (z -13.3) ⚠ toxic; transcription drop |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.188× (z -14.9) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 68.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.501× (z -8.7) |
| [[SW 1088 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -8.7) |
| [[SW 1271 (line)]] | alt | 43.7 | 0 | 1 | — | [[Clopidogrel (drug)]] 0.5 µM 0.0594× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD27]] | +0.75 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.70 | +0.67 / +0.46 | both halves | 3e-05 |  |
| [[MAST1]] | +0.68 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ST6GALNAC4]] | +0.67 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[PWWP3A]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[HACE1]] | +0.66 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.66 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[GARNL3]] | +0.65 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PIP4K2A]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MAST3]] | +0.64 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[FCHO1]] | +0.64 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[TSPAN33]] | +0.64 | +0.49 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OARD1]] | -0.71 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[INO80D]] | -0.70 | -0.62 / -0.46 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | -0.70 | -0.64 / -0.38 | both halves | 7e-05 |  |
| [[UFL1-AS1]] | -0.70 | -0.71 / -0.31 | both halves | 2e-04 |  |
| [[PBLD]] | -0.69 | -0.66 / -0.32 | both halves | 2e-04 |  |
| [[BDNF-AS]] | -0.69 | -0.68 / -0.33 | both halves | 1e-04 |  |
| [[ZNF337-AS1]] | -0.68 | -0.69 / -0.21 | both halves | 6e-04 |  |
| [[DECR1]] | -0.67 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[TTC32]] | -0.67 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.67 | -0.68 / -0.20 | both halves | 7e-04 |  |
| [[LINC00869-1]] | -0.67 | -0.61 / -0.31 | both halves | 2e-04 |  |
| [[LEKR1]] | -0.67 | -0.67 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises SH3PXD2B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EFCAB6]] | B | EFCAB6 activity raises SH3PXD2B's level | lines that do not express EFCAB6 (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without EFCAB6 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGA2B, THBS3-AS1, CYP46A1; maybe low, not absent |
| [[MPP2]] | B | MPP2 activity raises SH3PXD2B's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 2.74× lower at baseline in the lines without MPP2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[ACTA2]] | B | ACTA2 activity raises SH3PXD2B's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without ACTA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[TTLL7]] | B | TTLL7 activity raises SH3PXD2B's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.28× lower at baseline in the lines without TTLL7 | 0.089 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[OSBPL6]] | B | OSBPL6 activity raises SH3PXD2B's level | lines that do not express OSBPL6 (12) vs lines expressing it (38) | 2.17× lower at baseline in the lines without OSBPL6 | 0.090 | ⚠ within organs, on part of the lines; also absent: RECK, LHFPL6, GLIPR2; maybe low, not absent |
| [[PMP22]] | B | PMP22 activity raises SH3PXD2B's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 1.85× lower at baseline in the lines without PMP22 | 0.092 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SH3PXD2B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers SH3PXD2B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HACE1]] | C | HACE1 activity raises SH3PXD2B's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 4.12× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **-** arm (projection on the module's main direction -0.720). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (2.5, 7.5); signed map (-27.2, 21.5). **Vector** length 115, 37.0% of its response variance represented; |z| ≥ 3 in 1,679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +10.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +8.3 | +8.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.2 | +10.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +7.9 | +1.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.9 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.9 | +5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +1.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.7 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.2 | -31.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.4 | -31.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.8 | -11.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.1 | -9.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.6 | -4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and PX domains 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,325,000-172,454,525 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20831; previously KIAA1295 |
| Gene groups (HGNC) | SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A1X283](https://www.uniprot.org/uniprotkb/A1X283) (SH3 and PX domain-containing protein 2B):

> Adapter protein involved in invadopodia and podosome formation and extracellular matrix degradation. Binds matrix metalloproteinases (ADAMs), NADPH oxidases (NOXs) and phosphoinositides. Acts as an organizer protein that allows NOX1- or NOX3-dependent reactive oxygen species (ROS) generation and ROS localization. Plays a role in mitotic clonal expansion during the immediate early stage of adipocyte differentiation (By similarity).

**Summary**, from NCBI Gene [285590](https://www.ncbi.nlm.nih.gov/gene/285590):

> This gene encodes an adapter protein that is characterized by a PX domain and four Src homology 3 domains. The encoded protein is required for podosome formation and is involved in cell adhesion and migration of numerous cell types. Mutations in this gene are the cause of Frank-ter Haar syndrome (FTHS), and also Borrone Dermato-Cardio-Skeletal (BDCS) syndrome. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:29242](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29242) · Entrez [285590](https://www.ncbi.nlm.nih.gov/gene/285590) · UniProt [A1X283](https://www.uniprot.org/uniprotkb/A1X283) · Ensembl [ENSG00000174705](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174705)

## Data

Gene col 10516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10516); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10516]; `tensor/DDL_lfc|DDL_z.npy` [10516]; `embed/gene_vectors.npy` [10516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10516 or target_col == 10516). Every well: [[SH3PXD2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3PXD2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
