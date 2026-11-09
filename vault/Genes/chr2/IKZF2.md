---
symbol: "IKZF2"
type: "gene"
col: 397
ensembl_id: "ENSG00000030419"
name: "IKAROS family zinc finger 2"
location: "2q34"
module: 8
arm: "+"
pooled_cpm: 23.51
n_lines_expressing: 37
n_dd_up: 13
n_dd_down: 43
n_dd_up_clean: 13
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 14
direction_downstream: 18
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# IKZF2

*IKAROS family zinc finger 2* — 2q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.54× (z +5.5, q 2e-05, up in 16 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.431× (z -15.1, q 0e+00, down in 29 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRR]] (+0.64, fdr 7e-06), [[ATP8B1]] (+0.62, fdr 7e-06), [[MECOM]] (+0.60, fdr 1e-05); moves opposite to [[PTPDC1]] (-0.48, fdr 4e-05), [[ULK2]] (-0.46, fdr 3e-05), [[GLRX3]] (-0.44, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[STYK1]] → it (grade B ⚠); 18 go from it, the strongest it → [[STYK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 397.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +5.5 | 2e-05 | 16/35 (A498, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.46×** | +4.7 | 7e-04 | 15/35 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.003 | 15/35 (Panc 03.27, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.003 | 18/34 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.003 | 13/35 (A-427, HT-29, …) | all doses, flat | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +3.9 | 0.007 | 14/35 (NCI-H1573, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.9 | 0.007 | 13/35 (NCI-H1573, HT-29, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.9 | 0.008 | 13/35 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.008 | 13/35 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.76×** | +3.8 | 0.008 | 13/35 (LOX-IMVI, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.017 | 13/35 (NCI-H1573, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.33×** | +3.5 | 0.020 | 14/35 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.4 | 0.030 | 9/35 (HEC-1-A, C32, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.3 | 0.045 | 13/35 (A498, HEC-1-A, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 397.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.431×** | -15.1 | 0e+00 | 29/35 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.409×** | -11.4 | 1e-27 | 27/35 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.418×** | -11.1 | 3e-26 | 30/35 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.437×** | -10.5 | 9e-24 | 28/35 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.428×** | -10.4 | 4e-23 | 26/33 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.479×** | -9.4 | 8e-19 | 30/35 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -9.1 | 8e-18 | 28/34 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.511×** | -8.5 | 1e-15 | 22/34 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.496×** | -8.4 | 3e-15 | 30/34 (A-427, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.520×** | -8.3 | 5e-15 | 26/35 (LS 180, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.527×** | -8.1 | 2e-14 | 26/35 (BT-474, HT-29, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.571×** | -7.1 | 6e-11 | 22/35 (A-427, CFPAC-1, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.676×** | -7.0 | 1e-10 | 21/35 (BT-474, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.579×** | -6.9 | 2e-10 | 20/31 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.416×** | -5.8 | 2e-07 | 20/35 (Panc 03.27, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.465×** | -5.1 | 1e-05 | 20/34 (LS 180, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.665×** | -5.0 | 2e-05 | 18/34 (A-427, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.729×** | -4.0 | 0.002 | 14/35 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 397. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 98.9 | 0 | 18 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0573× (z -18.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.159× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 64.8 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0470× (z -18.7) |
| [[LS 180 (line)]] | wt | 37.1 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0970× (z -16.4) |
| [[NCI-H1792 (line)]] | alt | 67.9 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -20.7) |
| [[A-427 (line)]] | wt | 109 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.194× (z -13.1) |
| [[CFPAC-1 (line)]] | alt | 78.7 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0622× (z -18.8) |
| [[COLO 205 (line)]] | alt | 52.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0689× (z -18.5) |
| [[Hs 766T (line)]] | wt | 38.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.2) |
| [[HT-29 (line)]] | alt | 25.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.232× (z -9.3) |
| [[LoVo (line)]] | wt | 10.2 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0359× (z -16.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 28.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -14.7) |
| [[SNU-423 (line)]] | alt | 50.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -14.7) |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.118× (z -11.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 39.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0937× (z -14.2) |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -11.8) |
| [[J82 (line)]] | alt | 26.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 12.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.177× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0998× (z -10.5) |
| [[SHP-77 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.142× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.73 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0754× (z -10.2) |
| [[CHP-212 (line)]] | wt | 50.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0610× (z -11.2) |
| [[HEC-1-A (line)]] | alt | 7.66 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -8.9) |
| [[SW48 (line)]] | wt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0481× (z -13.4) |
| [[A-172 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.69 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.68 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.09 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 397), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRR]] | +0.64 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[ATP8B1]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MECOM]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 | same gene group |
| [[RBM47]] | +0.57 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[SIDT1]] | +0.56 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[CGN]] | +0.55 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[ADGRF1]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HHLA2]] | +0.54 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[DUOX2]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PRSS51]] | +0.53 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[SLC44A4]] | +0.52 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TC2N]] | +0.52 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPDC1]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ULK2]] | -0.46 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[GLRX3]] | -0.44 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[SLC4A3]] | -0.44 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[CROCCP3-1]] | -0.44 | -0.37 / -0.47 | both halves | 7e-05 |  |
| [[CARS2]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[KLC1]] | -0.43 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[CUL4A]] | -0.42 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[TATDN1]] | -0.42 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STYK1]] | B | STYK1 activity raises IKZF2's level | lines that do not express STYK1 (20) vs lines expressing it (30) | 2.00× lower at baseline in the lines without STYK1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, TSTD1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers IKZF2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[BMP2]] | B | BMP2 activity raises IKZF2's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.32× lower at baseline in the lines without BMP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[PTPRB]] | B | PTPRB activity raises IKZF2's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without PTPRB | 0.036 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[INPP4B]] | B | INPP4B activity raises IKZF2's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without INPP4B | 0.044 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[ADGRF1]] | B | ADGRF1 activity raises IKZF2's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 1.69× lower at baseline in the lines without ADGRF1 | 0.075 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |
| [[UGT1A1]] | B | UGT1A1 activity raises IKZF2's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.14× lower at baseline in the lines without UGT1A1 | 0.079 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[CLDN3]] | B | CLDN3 activity raises IKZF2's level | lines that do not express CLDN3 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without CLDN3 | 0.079 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[UGT1A6]] | B | UGT1A6 activity raises IKZF2's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.19× lower at baseline in the lines without UGT1A6 | 0.083 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers IKZF2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MAP2K2]] | B | MAP2K2 activity lowers IKZF2's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[EPHA6]] | B | EPHA6 activity raises IKZF2's level | lines that do not express EPHA6 (29) vs lines expressing it (21) | 2.42× lower at baseline in the lines without EPHA6 | 0.095 | ⚠ within organs, on part of the lines; also absent: SLITRK4, NOVA1, KCTD8 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 17, C 1. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STYK1]] | B | IKZF2 activity raises STYK1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without IKZF2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[GLRX3]] | B | IKZF2 activity lowers GLRX3's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.42× higher at baseline in the lines without IKZF2 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[PTPRB]] | B | IKZF2 activity raises PTPRB's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 3.02× lower at baseline in the lines without IKZF2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[SAMD12]] | B | IKZF2 activity raises SAMD12's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without IKZF2 | 0.029 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[KCNK1]] | B | IKZF2 activity raises KCNK1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.66× lower at baseline in the lines without IKZF2 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[BMP2]] | B | IKZF2 activity raises BMP2's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 3.21× lower at baseline in the lines without IKZF2 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[ATP8B1]] | B | IKZF2 activity raises ATP8B1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without IKZF2 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[ST14]] | B | IKZF2 activity raises ST14's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without IKZF2 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[ADGRF1]] | B | IKZF2 activity raises ADGRF1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.60× lower at baseline in the lines without IKZF2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[SAMD12-AS1]] | B | IKZF2 activity raises SAMD12-AS1's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.99× lower at baseline in the lines without IKZF2 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[ULK2]] | B | IKZF2 activity lowers ULK2's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 1.43× higher at baseline in the lines without IKZF2 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |
| [[PTPRR]] | B | IKZF2 activity raises PTPRR's level | lines that do not express IKZF2 (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without IKZF2 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000273118, MECOM, SEMA3C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.1, 54.5); signed map (64.1, 1.7). **Vector** length 95.2, 22.9% of its response variance represented; |z| ≥ 3 in 1,278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | -0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +3.8 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.9 | -7.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.3 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | +0.9 |
|  | [[Artesunate (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -2.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | IKAROS family zinc finger 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q34 — chr2:212,999,691-213,152,427 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Helios; previously ZNFN1A2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 6 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UKS7](https://www.uniprot.org/uniprotkb/Q9UKS7) (Zinc finger protein Helios):

> Transcription factor, which stabilizes the noninflammatory phenotype of regulatory T cells (Tregs) (By similarity). May possibly act via STAT5-mediated signaling (By similarity). Binds IL2 promoter and represses its transcription, possibly by epigenetic silencing, inducing deacetylation of core histones in the IL2 promoter. In Tregs, required for FOXP3 recruitment to the IL2 promoter (By similarity). Required for outer hair cells maturation and, consequently, for hearing (By similarity).

**Summary**, from NCBI Gene [22807](https://www.ncbi.nlm.nih.gov/gene/22807):

> This gene encodes a member of the Ikaros family of zinc-finger proteins. Three members of this protein family (Ikaros, Aiolos and Helios) are hematopoietic-specific transcription factors involved in the regulation of lymphocyte development. This protein forms homo- or hetero-dimers with other Ikaros family members, and is thought to function predominantly in early hematopoietic development. Multiple transcript variants encoding different isoforms have been found for this gene, but the …

**Accessions** — [HGNC:13177](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13177) · Entrez [22807](https://www.ncbi.nlm.nih.gov/gene/22807) · UniProt [Q9UKS7](https://www.uniprot.org/uniprotkb/Q9UKS7) · Ensembl [ENSG00000030419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000030419)

## Data

Gene col 397: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 397); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 397, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 397]; `tensor/DDL_lfc|DDL_z.npy` [397]; `embed/gene_vectors.npy` [397]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 397 or target_col == 397). Every well: [[IKZF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKZF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
