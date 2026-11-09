---
symbol: "ACTR3C"
type: "gene"
col: 2770
ensembl_id: "ENSG00000106526"
name: "actin related protein 3C"
location: "7q36.1"
module: 8
arm: "+"
pooled_cpm: 13.04
n_lines_expressing: 35
n_dd_up: 20
n_dd_down: 19
n_dd_up_clean: 18
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 20
direction_downstream: 27
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# ACTR3C

*actin related protein 3C* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.82× (z +6.5, q 4e-08, up in 20 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.270× (z -14.2, q 3e-43, down in 30 of 33 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF4G]] (+0.69, fdr 2e-05), [[HGD]] (+0.66, fdr 1e-05), [[ARMCX4]] (+0.63, fdr 1e-05); moves opposite to [[RRAS]] (-0.58, fdr 3e-04), [[GNAI2]] (-0.56, fdr 0.002, ⚠ not reproduced), [[ETHE1]] (-0.56, fdr 6e-05), [[LIX1L]] (-0.56, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[PROM1]] → it (grade B ⚠); 27 go from it, the strongest it → [[SLC44A3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2770.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +6.5 | 4e-08 | 20/33 (RKO, LoVo, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.67×** | +5.3 | 2e-05 | 18/33 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.43×** | +5.3 | 2e-05 | 19/33 (CFPAC-1, HEC-1-A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.61×** | +5.2 | 3e-05 | 17/33 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 2e-04 | 17/33 (CFPAC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.48×** | +4.3 | 0.002 | 16/33 (CFPAC-1, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.002 | 11/30 (RKO, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +4.0 | 0.004 | 14/33 (CFPAC-1, Panc 03.27, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.004 | 13/33 (CFPAC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.007 | 13/33 (CFPAC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.014 | 14/33 (CFPAC-1, LoVo, …) | all doses, flat |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.39×** | +3.6 | 0.015 | 13/33 (COLO 205, CFPAC-1, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.82×** | +3.4 | 0.031 | 9/32 (J82, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.047 | 6/33 (CFPAC-1, A498, …) | all doses, flat |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.35×** | +3.2 | 0.047 | 4/33 (NCI-H1792, J82, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.047 | 8/33 (CFPAC-1, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2770.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.270×** | -14.2 | 3e-43 | 30/33 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.388×** | -10.3 | 2e-22 | 27/33 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.413×** | -9.6 | 2e-19 | 27/33 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.455×** | -8.6 | 2e-15 | 26/33 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.464×** | -8.3 | 8e-15 | 26/32 (NCI-H23, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.479×** | -8.0 | 1e-13 | 26/33 (SW480, COLO 205, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.514×** | -7.0 | 3e-10 | 22/33 (NCI-H1792, COLO 205, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **0.675×** | -6.0 | 1e-07 | 18/30 (NCI-H1573, COLO 205, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.355×** | -5.9 | 3e-07 | 21/32 (LS 180, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.613×** | -5.3 | 6e-06 | 23/32 (SW480, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.434×** | -4.7 | 1e-04 | 17/33 (HT-29, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.671×** | -4.3 | 7e-04 | 16/33 (SW480, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **0.671×** | -4.2 | 0.001 | 19/30 (LoVo, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -3.9 | 0.004 | 15/31 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.704×** | -3.8 | 0.005 | 15/33 (HT-29, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.696×** | -3.8 | 0.006 | 10/33 (Panc 03.27, NCI-H23, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.727×** | -3.5 | 0.017 | 9/33 (CFPAC-1, SNU-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2770. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 44.0 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0628× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.105× (z -17.4) |
| [[HT-29 (line)]] | alt | 49.4 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0459× (z -21.0) |
| [[LS 180 (line)]] | wt | 22.1 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0482× (z -19.2) |
| [[CFPAC-1 (line)]] | alt | 35.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -12.1) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.129× (z -9.6) |
| [[COLO 205 (line)]] | alt | 34.1 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.00811× (z -27.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.103× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0976× (z -14.9) |
| [[SW1417 (line)]] | alt | 40.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -13.6) ⚠ cell-cycle shift, explains ~99% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.167× (z -11.3) |
| [[LoVo (line)]] | wt | 19.5 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.127× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.170× (z -11.6) |
| [[HCT15 (line)]] | alt | 41.2 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.127× (z -11.9) |
| [[KATO III (line)]] | alt | 18.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.05 µM 0.182× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0443× (z -15.8) |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.112× (z -10.2) |
| [[SNU-423 (line)]] | alt | 9.60 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0753× (z -10.6) |
| [[A498 (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -12.3) ⚠ cell-cycle shift, explains ~99% of this change |
| [[J82 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.201× (z -9.0) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 6.24 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -14.1) ⚠ cell-cycle shift, explains ~99% of this change |
| [[NCI-H1792 (line)]] | alt | 6.69 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0670× (z -9.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H2030 (line)]] | alt | 3.48 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.0854× (z -8.5) |
| [[PANC-1 (line)]] | alt | 5.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[RKO (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.130× (z -8.9) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 17.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0376× (z -13.0) |
| [[A-172 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2770), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 10 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4G]] | +0.69 | +0.71 / +0.47 | both halves | 2e-05 |  |
| [[HGD]] | +0.66 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ARMCX4]] | +0.63 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[PLCH1]] | +0.62 | +0.64 / +0.44 | both halves | 3e-05 |  |
| [[SPATA6L]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[STEAP2-AS1]] | +0.62 | +0.62 / +0.32 | both halves | 2e-04 |  |
| [[FBXL19-AS1]] | +0.62 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[LRRC61]] | +0.61 | +0.58 / +0.51 | both halves | 1e-05 | STRING 607; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TMCO4]] | +0.61 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[MAMDC2-AS1]] | +0.60 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[SAMD12-AS1]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HMGA1P4]] | +0.59 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[IQCH-AS1]] | +0.59 | +0.53 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAS]] | -0.58 | -0.51 / -0.29 | both halves | 3e-04 |  |
| [[GNAI2]] | -0.56 | -0.50 / -0.14 | ⚠ not reproduced | 0.002 |  |
| [[ETHE1]] | -0.56 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[LIX1L]] | -0.56 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[FSCN1]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[PSD3]] | -0.55 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[RTN2]] | -0.54 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[CDKN2D]] | -0.54 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[SH3BGRL3]] | -0.53 | -0.49 / -0.26 | both halves | 3e-04 |  |
| [[DNAAF9]] | -0.53 | -0.54 / -0.24 | both halves | 5e-04 |  |
| [[RAC2]] | -0.52 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[LTBP4]] | -0.52 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[ARL3]] | -0.52 | -0.39 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PROM1]] | B | PROM1 activity raises ACTR3C's level | lines that do not express PROM1 (37) vs lines expressing it (13) | 3.59× lower at baseline in the lines without PROM1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: AZGP1, KRT23, GJB1 |
| [[C11orf52]] | B | C11orf52 activity raises ACTR3C's level | lines that do not express C11orf52 (23) vs lines expressing it (27) | 2.72× lower at baseline in the lines without C11orf52 | 0.012 | ⚠ within organs, on part of the lines; also absent: TNNT2, MPZL3, RNF39 |
| [[DPP4]] | B | DPP4 activity raises ACTR3C's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 2.72× lower at baseline in the lines without DPP4 | 0.012 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[EPCAM-DT]] | B | EPCAM-DT activity raises ACTR3C's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without EPCAM-DT | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises ACTR3C's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.35× lower at baseline in the lines without SLC44A3-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[POU5F1B]] | B | POU5F1B activity raises ACTR3C's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 2.72× lower at baseline in the lines without POU5F1B | 0.051 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers ACTR3C's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[CYP4F3]] | B | CYP4F3 activity raises ACTR3C's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without CYP4F3 | 0.059 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6 |
| [[FAM149A]] | B | FAM149A activity raises ACTR3C's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without FAM149A | 0.069 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |
| [[HNF4G]] | B | HNF4G activity raises ACTR3C's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 2.77× lower at baseline in the lines without HNF4G | 0.083 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[PCAT1]] | B | PCAT1 activity raises ACTR3C's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 2.65× lower at baseline in the lines without PCAT1 | 0.087 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[GOLGA2P5-1]] | B | GOLGA2P5-1 activity raises ACTR3C's level | lines that do not express GOLGA2P5-1 (8) vs lines expressing it (42) | 2.68× lower at baseline in the lines without GOLGA2P5-1 | 0.089 | ⚠ within organs, on part of the lines; also absent: GOLGA2P5, ENSG00000257489, KCNIP3; maybe low, not absent |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 22, C 5. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3-AS1]] | B | ACTR3C activity raises SLC44A3-AS1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without ACTR3C | 0.007 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[PRRG2]] | B | ACTR3C activity raises PRRG2's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.05× lower at baseline in the lines without ACTR3C | 0.015 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[PRSS23-AS1]] | B | ACTR3C activity lowers PRSS23-AS1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.47× higher at baseline in the lines without ACTR3C | 0.016 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[CEP170]] | B | ACTR3C activity lowers CEP170's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.97× higher at baseline in the lines without ACTR3C | 0.017 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[C11orf52]] | B | ACTR3C activity raises C11orf52's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without ACTR3C | 0.021 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[ABCC6]] | B | ACTR3C activity raises ABCC6's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.86× lower at baseline in the lines without ACTR3C | 0.022 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[GOLGA2P5-1]] | B | ACTR3C activity raises GOLGA2P5-1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without ACTR3C | 0.031 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[IQCH-AS1]] | B | ACTR3C activity raises IQCH-AS1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.78× lower at baseline in the lines without ACTR3C | 0.033 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[GOLGA2P5]] | B | ACTR3C activity raises GOLGA2P5's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without ACTR3C | 0.033 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[PCAT1]] | B | ACTR3C activity raises PCAT1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.35× lower at baseline in the lines without ACTR3C | 0.035 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[ATXN7L3-AS1]] | B | ACTR3C activity raises ATXN7L3-AS1's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.38× lower at baseline in the lines without ACTR3C | 0.035 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[LIX1L]] | B | ACTR3C activity lowers LIX1L's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.67× higher at baseline in the lines without ACTR3C | 0.039 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.491). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.3, 51.3); signed map (57.4, -0.2). **Vector** length 84.2, 20.6% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.4 | +6.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.2 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -0.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -5.0 | -8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.8 | -8.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.0 | -14.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.7 | -3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 3C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:150,243,916-150,323,725 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARP11 |
| Gene groups (HGNC) | Actin related proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0K3](https://www.uniprot.org/uniprotkb/Q9C0K3) (Actin-related protein 3C):

> May play a role in the suppression of metastatic potential in lung adenoma carcinoma cells.

**Summary**, from NCBI Gene [653857](https://www.ncbi.nlm.nih.gov/gene/653857):

> Predicted to enable ATP binding activity and actin binding activity. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:37282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37282) · Entrez [653857](https://www.ncbi.nlm.nih.gov/gene/653857) · UniProt [Q9C0K3](https://www.uniprot.org/uniprotkb/Q9C0K3) · Ensembl [ENSG00000106526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106526)

## Data

Gene col 2770: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2770); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2770, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2770]; `tensor/DDL_lfc|DDL_z.npy` [2770]; `embed/gene_vectors.npy` [2770]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2770 or target_col == 2770). Every well: [[ACTR3C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACTR3C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
