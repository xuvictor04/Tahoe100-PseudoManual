---
symbol: "TIA1"
type: "gene"
col: 3749
ensembl_id: "ENSG00000116001"
name: "TIA1 cytotoxic granule associated RNA binding protein"
location: "2p13.3"
module: 77
arm: "-"
pooled_cpm: 32.72
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# TIA1

*TIA1 cytotoxic granule associated RNA binding protein* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.08× (z +21.0, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.464× (z -15.6, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAZ2B]] (+0.75, fdr 7e-06), [[OCIAD1]] (+0.74, fdr 1e-05), [[ST7L]] (+0.72, fdr 3e-05); moves opposite to [[TMEM120B]] (-0.75, fdr 7e-06), [[ANKRD27]] (-0.74, fdr 1e-05), [[SNRPD2]] (-0.72, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.08×** | +21.0 | 0e+00 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +16.3 | 0e+00 | 33/38 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +15.2 | 0e+00 | 40/44 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.07×** | +14.2 | 7e-44 | 41/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +12.0 | 3e-31 | 40/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +8.4 | 3e-15 | 36/48 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.36×** | +5.7 | 8e-07 | 25/42 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.29×** | +5.2 | 1e-05 | 20/47 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.29×** | +5.1 | 2e-05 | 22/48 (J82, BT-474, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.26×** | +4.5 | 5e-04 | 22/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.8 | 0.007 | 16/48 (A-172, HS-578T, …) | all doses, stronger at high dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.7 | 0.010 | 13/40 (NCI-H460, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.012 | 16/47 (NCI-H23, AsPC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.065 | 13/47 (A549, HOP62, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.04× | +3.1 | 0.065 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.065 | 4/48 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +3.0 | 0.079 | 6/48 (HOP62, NCI-H661, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.080 | 11/48 (AsPC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.23×** | +3.0 | 0.080 | 7/48 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.091 | 5/48 (A498, C32, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.464×** | -15.6 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.483×** | -14.8 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.487×** | -14.6 | 0e+00 | 46/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.410×** | -9.5 | 4e-19 | 38/48 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.665×** | -8.3 | 1e-14 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.560×** | -6.2 | 7e-08 | 29/48 (A-427, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.768×** | -5.4 | 7e-06 | 20/48 (hTERT-HPNE, SW480, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.774×** | -5.2 | 1e-05 | 25/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.798×** | -4.6 | 3e-04 | 19/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.658×** | -4.4 | 5e-04 | 18/48 (NCI-H460, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -4.1 | 0.002 | 14/48 (KATO III, NCI-H460, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.880× | -3.7 | 0.012 | 19/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.884× | -3.5 | 0.017 | 9/48 (A-172, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.842× | -3.5 | 0.019 | 12/48 (PANC-1, LoVo, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 45.1 | 4 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +16.8) | [[Panobinostat (drug)]] 5 µM 0.319× (z -15.6) |
| [[PANC-1 (line)]] | alt | 36.0 | 4 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +16.1) | [[Panobinostat (drug)]] 0.5 µM 0.427× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 36.6 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +14.2) | [[Panobinostat (drug)]] 5 µM 0.395× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 33.8 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.1) | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 38.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -12.9) |
| [[A-172 (line)]] | wt | 41.3 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.413× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 42.0 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -10.3) |
| [[HT-29 (line)]] | alt | 34.4 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.396× (z -8.6) |
| [[KATO III (line)]] | alt | 39.9 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.3) | [[Panobinostat (drug)]] 5 µM 0.371× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 25.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +11.4) | — |
| [[C-33 A (line)]] | alt | 68.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.353× (z -9.5) |
| [[HOP62 (line)]] | alt | 25.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +13.6) | — |
| [[HS-578T (line)]] | alt | 27.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.7) | [[Belinostat (drug)]] 5 µM 0.333× (z -8.7) |
| [[LS 180 (line)]] | wt | 34.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 31.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.285× (z -9.5) |
| [[A-427 (line)]] | wt | 52.8 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.188× (z -9.3) |
| [[A498 (line)]] | wt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 29.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.21× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 43.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.153× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 22.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 24.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 40.3 | 0 | 1 | — | [[Pimitespib (drug)]] 5 µM 0.0919× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 21.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.6) | — |
| [[LoVo (line)]] | wt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 49.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +11.0) | — |
| [[RKO (line)]] | wt | 30.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.294× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 33.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.77× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ2B]] | +0.75 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[OCIAD1]] | +0.74 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[ST7L]] | +0.72 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[LZIC]] | +0.72 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[DCAF8]] | +0.72 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[RIPK2-DT]] | +0.71 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[ZNF280D]] | +0.71 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.71 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[CGGBP1]] | +0.70 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[ARFGAP2]] | +0.70 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.69 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[FKRP]] | +0.69 | +0.71 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM120B]] | -0.75 | -0.73 / -0.59 | both halves | 7e-06 |  |
| [[ANKRD27]] | -0.74 | -0.77 / -0.55 | both halves | 1e-05 |  |
| [[SNRPD2]] | -0.72 | -0.70 / -0.54 | both halves | 1e-05 | STRING 520 |
| [[SPTLC2]] | -0.72 | -0.71 / -0.56 | both halves | 1e-05 |  |
| [[GFOD2]] | -0.72 | -0.69 / -0.61 | both halves | 7e-06 |  |
| [[LPCAT4]] | -0.71 | -0.75 / -0.56 | both halves | 1e-05 |  |
| [[UQCRH]] | -0.70 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[TAF5L]] | -0.70 | -0.76 / -0.50 | both halves | 1e-05 |  |
| [[MAP2K1]] | -0.69 | -0.74 / -0.48 | both halves | 2e-05 |  |
| [[IGSF8]] | -0.69 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[ZDHHC9]] | -0.69 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[TSEN54]] | -0.69 | -0.58 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises TIA1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises TIA1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.855). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-1.4, 0.6); signed map (17.0, -23.5). **Vector** length 111, 28.4% of its response variance represented; |z| ≥ 3 in 993 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.9 | +21.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.0 | +12.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.8 | +14.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +8.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.8 | +1.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +3.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -7.8 | -15.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.5 | -14.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -7.1 | -14.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.5 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.1 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | TIA1 cytotoxic granule associated RNA binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,209,444-70,248,660 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIA-1 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 4 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [P31483](https://www.uniprot.org/uniprotkb/P31483) (Cytotoxic granule associated RNA binding protein TIA1):

> RNA-binding protein involved in the regulation of alternative pre-RNA splicing and mRNA translation by binding to uridine-rich (U-rich) RNA sequences. Binds to U-rich sequences immediately downstream from a 5' splice sites in a uridine-rich small nuclear ribonucleoprotein (U snRNP)-dependent fashion, thereby modulating alternative pre-RNA splicing. Preferably binds to the U-rich IAS1 sequence in a U1 snRNP-dependent manner; this binding is optimal if a 5' splice site is adjacent to IAS1 (By …

**Summary**, from NCBI Gene [7072](https://www.ncbi.nlm.nih.gov/gene/7072):

> The product encoded by this gene is a member of a RNA-binding protein family and possesses nucleolytic activity against cytotoxic lymphocyte (CTL) target cells. It has been suggested that this protein may be involved in the induction of apoptosis as it preferentially recognizes poly(A) homopolymers and induces DNA fragmentation in CTL targets. The major granule-associated species is a 15-kDa protein that is thought to be derived from the carboxyl terminus of the 40-kDa product by proteolytic …

**Accessions** — [HGNC:11802](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11802) · Entrez [7072](https://www.ncbi.nlm.nih.gov/gene/7072) · UniProt [P31483](https://www.uniprot.org/uniprotkb/P31483) · Ensembl [ENSG00000116001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116001)

## Data

Gene col 3749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3749); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3749]; `tensor/DDL_lfc|DDL_z.npy` [3749]; `embed/gene_vectors.npy` [3749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3749 or target_col == 3749). Every well: [[TIA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
