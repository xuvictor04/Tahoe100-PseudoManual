---
symbol: "SEPTIN6"
type: "gene"
col: 4605
ensembl_id: "ENSG00000125354"
name: "septin 6"
location: "Xq24"
module: 85
arm: "+"
pooled_cpm: 33.63
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 28
n_dd_up_clean: 14
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# SEPTIN6

*septin 6* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +13.2, q 6e-37, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.569× (z -14.4, q 6e-44, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB3A]] (+0.71, fdr 8e-06), [[ABCB9]] (+0.69, fdr 1e-05), [[ANKMY2]] (+0.67, fdr 1e-05); moves opposite to [[RNF146]] (-0.64, fdr 4e-05), [[ENOX2]] (-0.64, fdr 5e-05), [[ITPA]] (-0.63, fdr 3e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SEMA6B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4605.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +13.2 | 6e-37 | 37/47 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +10.4 | 9e-23 | 34/47 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +9.1 | 1e-17 | 36/47 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.66×** | +8.8 | 1e-16 | 24/36 (HEC-1-A, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +8.1 | 6e-14 | 32/47 (HOP62, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +7.9 | 4e-13 | 30/47 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.49×** | +7.2 | 4e-11 | 25/42 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +5.6 | 2e-06 | 29/47 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.8 | 1e-04 | 23/47 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +4.7 | 1e-04 | 20/47 (NCI-H460, AsPC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 4e-04 | 20/47 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +4.2 | 0.001 | 16/47 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.05 µM |  | **1.25×** | +3.7 | 0.008 | 14/47 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.012 | 11/47 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.018 | 16/47 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.094 | 7/47 (HOP62, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4605.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.569×** | -14.4 | 6e-44 | 34/47 (Hs 766T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.467×** | -13.7 | 2e-40 | 37/47 (PANC-1, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -13.2 | 2e-37 | 40/47 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.480×** | -12.7 | 7e-35 | 40/47 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.516×** | -11.9 | 1e-30 | 40/47 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.517×** | -11.9 | 1e-30 | 38/45 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.544×** | -11.0 | 5e-26 | 37/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.395×** | -8.7 | 2e-16 | 36/47 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.423×** | -8.1 | 3e-14 | 35/47 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.660×** | -7.5 | 4e-12 | 30/47 (AN3 CA, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.723×** | -5.8 | 3e-07 | 24/46 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.721×** | -5.7 | 7e-07 | 26/46 (MIA PaCa-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.807×** | -5.5 | 2e-06 | 22/47 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.741×** | -5.4 | 3e-06 | 26/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.742×** | -5.4 | 3e-06 | 23/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.732×** | -5.3 | 4e-06 | 22/46 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.813×** | -5.3 | 4e-06 | 21/47 (Hs 766T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4605. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.8 | 3 | 10 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -22.0) |
| [[Hs 766T (line)]] | wt | 72.8 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.2) |
| [[MIA PaCa-2 (line)]] | alt | 39.2 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.264× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 31.1 | 1 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.82× (z +9.8) | [[Homoharringtonine (drug)]] 0.05 µM 0.184× (z -15.9) |
| [[SNU-423 (line)]] | alt | 56.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -18.8) |
| [[A549 (line)]] | wt | 24.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.368× (z -10.5) |
| [[AN3 CA (line)]] | alt | 149 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -19.7) |
| [[SW 900 (line)]] | alt | 32.6 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -10.9) |
| [[SW1417 (line)]] | alt | 17.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.40× (z +10.9) | — |
| [[A-172 (line)]] | wt | 29.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -13.2) |
| [[A-427 (line)]] | wt | 34.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -14.8) |
| [[HOP62 (line)]] | alt | 22.2 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.63× (z +10.1) | — |
| [[J82 (line)]] | alt | 44.7 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.524× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 37.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.297× (z -9.8) |
| [[NCI-H661 (line)]] | alt | 95.4 | 0 | 3 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.175× (z -9.6) |
| [[SW480 (line)]] | alt | 68.1 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.268× (z -8.9) |
| [[C32 (line)]] | wt | 20.9 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.164× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 52.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +13.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 9.74 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | [[Digitoxin (drug)]] 0.5 µM 0.155× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 20.8 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.56× (z +9.0) ⚠ position not correctable | [[Harringtonine (drug)]] 5 µM 0.149× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 41.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.5) |
| [[RKO (line)]] | wt | 25.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -10.7) |
| [[A498 (line)]] | wt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.513× (z -8.6) |
| [[C-33 A (line)]] | alt | 68.6 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.319× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 33.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.5) |
| [[HCT15 (line)]] | alt | 45.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -9.5) |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.233× (z -8.7) |
| [[SHP-77 (line)]] | alt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +9.4) | — |
| [[AsPC-1 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4605), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3A]] | +0.71 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[ABCB9]] | +0.69 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ANKMY2]] | +0.67 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[MAST1]] | +0.67 | +0.53 / +0.60 | both halves | 1e-05 | same gene group |
| [[CCDC134]] | +0.66 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[TSPAN13]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[PLCD1]] | +0.64 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[AHDC1]] | +0.64 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SLC27A1]] | +0.63 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[HACE1]] | +0.63 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[MAPT]] | +0.63 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[GNAI2]] | +0.62 | +0.52 / +0.32 | both halves | 2e-04 | same gene group |

## Genes that move opposite

*25 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF146]] | -0.64 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ENOX2]] | -0.64 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[ITPA]] | -0.63 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PPP3CB-AS1]] | -0.62 | -0.39 / -0.48 | both halves | 5e-05 |  |
| [[BDNF-AS]] | -0.62 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[CFLAR]] | -0.61 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CHD1-DT]] | -0.61 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[DPH5-DT]] | -0.60 | -0.53 / -0.29 | both halves | 3e-04 |  |
| [[NIPAL2]] | -0.60 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[ANKRD17-DT]] | -0.59 | -0.48 / -0.22 | both halves | 6e-04 |  |
| [[WARS2-AS1]] | -0.58 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[HEXIM2-AS1]] | -0.58 | -0.45 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA6B]] | B | SEMA6B activity raises SEPTIN6's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.67× lower at baseline in the lines without SEMA6B | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[NOVA2]] | B | NOVA2 activity raises SEPTIN6's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 1.67× lower at baseline in the lines without NOVA2 | 0.009 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1 |
| [[TTYH2]] | B | TTYH2 activity raises SEPTIN6's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without TTYH2 | 0.015 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |
| [[HLTF]] | B | HLTF activity raises SEPTIN6's level | lines that do not express HLTF (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without HLTF | 0.024 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[LMX1B]] | B | LMX1B activity raises SEPTIN6's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 1.54× lower at baseline in the lines without LMX1B | 0.054 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2 |
| [[FHL1]] | B | FHL1 activity raises SEPTIN6's level | lines that do not express FHL1 (19) vs lines expressing it (31) | 1.81× lower at baseline in the lines without FHL1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAMTS7, ANTXR1, MSRB3 |
| [[TCF7L1]] | B | TCF7L1 activity strengthens SEPTIN6's drug response | lines that do not express TCF7L1 (11) vs lines expressing it (36) | the lines without TCF7L1 respond 0.80× as strongly (z diff +0.98); strongest at Digitoxin 5 µM: 0.72x vs 0.45x (z diff +3.6) | 0.090 | ⚠ within organs, on part of the lines; also absent: EML1, PYGO1, FAM124A; target measured in part of the lines; artifact flags |
| [[HACE1]] | C | HACE1 activity raises SEPTIN6's level | lines that do not express HACE1 (3) vs lines expressing it (47) | 3.32× lower at baseline in the lines without HACE1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: AXDND1, CFL2, ATP6V1E2; maybe low, not absent; its own permutation p |
| [[DNMT3B]] | C | DNMT3B activity raises SEPTIN6's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without DNMT3B | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (7.0, -6.0); signed map (-31.8, 20.6). **Vector** length 96.5, 24.7% of its response variance represented; |z| ≥ 3 in 1,318 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +8.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +5.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.9 | +7.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.7 | +10.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +4.7 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +2.3 | +3.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.3 | -7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.1 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.9 | -13.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | septin 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,615,724-119,693,370 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0128, SEP2, SEPT2, MGC16619, MGC20339, Septin-6; previously SEPT6 |
| Gene groups (HGNC) | Septins; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14141](https://www.uniprot.org/uniprotkb/Q14141) (Septin-6):

> Filament-forming cytoskeletal GTPase. Required for normal organization of the actin cytoskeleton. Involved in cytokinesis. May play a role in HCV RNA replication. Forms a filamentous structure with SEPTIN12, SEPTIN6, SEPTIN2 and probably SEPTIN4 at the sperm annulus which is required for the structural integrity and motility of the sperm tail during postmeiotic differentiation.

**Summary**, from NCBI Gene [23157](https://www.ncbi.nlm.nih.gov/gene/23157):

> This gene is a member of the septin family of GTPases. Members of this family are required for cytokinesis. One version of pediatric acute myeloid leukemia is the result of a reciprocal translocation between chromosomes 11 and X, with the breakpoint associated with the genes encoding the mixed-lineage leukemia and septin 2 proteins. This gene encodes four transcript variants encoding three distinct isoforms. An additional transcript variant has been identified, but its biological validity has …

**Accessions** — [HGNC:15848](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15848) · Entrez [23157](https://www.ncbi.nlm.nih.gov/gene/23157) · UniProt [Q14141](https://www.uniprot.org/uniprotkb/Q14141) · Ensembl [ENSG00000125354](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125354)

## Data

Gene col 4605: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4605); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4605, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4605]; `tensor/DDL_lfc|DDL_z.npy` [4605]; `embed/gene_vectors.npy` [4605]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4605 or target_col == 4605). Every well: [[SEPTIN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
