---
symbol: "DAPK1"
type: "gene"
col: 12275
ensembl_id: "ENSG00000196730"
name: "death associated protein kinase 1"
location: "9q21.33"
module: 8
arm: "+"
pooled_cpm: 53.45
n_lines_expressing: 27
n_dd_up: 8
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DAPK1

*death associated protein kinase 1* — 9q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.49× (z +5.6, q 9e-06, up in 15 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.539× (z -12.9, q 2e-35, down in 18 of 25 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.620× (z -7.1, q 2e-10, down in 20 of 25 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRIN2]] (+0.65, fdr 1e-05), [[MUC16]] (+0.60, fdr 1e-05), [[SIDT1]] (+0.57, fdr 2e-05); moves opposite to [[LINC02985]] (-0.44, fdr 1e-04), [[SLC25A24P1]] (-0.41, fdr 1e-04), [[CCDC102B]] (-0.41, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SIDT1]] → it (grade B ⚠); 9 go from it, the strongest it → [[ARHGEF28]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12275.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +5.6 | 9e-06 | 15/25 (HEC-1-A, A549, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 2e-04 | 12/25 (HEC-1-A, A549, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.8 | 0.021 | 11/25 (CFPAC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.8 | 0.021 | 9/25 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +3.6 | 0.041 | 13/25 (HEC-1-A, A549, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.25×** | +3.4 | 0.063 | 12/26 (HEC-1-A, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.068 | 11/25 (RKO, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.3 | 0.072 | 4/25 (C32, NCI-H1792, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.087 | 7/25 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.25×** | +3.1 | 0.095 | 13/25 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.13 | 7/25 (CFPAC-1, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12275.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.539×** | -12.9 | 2e-35 | 18/25 (A549, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.437×** | -11.8 | 1e-29 | 21/25 (A549, CFPAC-1, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.519×** | -9.7 | 6e-20 | 20/25 (LoVo, A549, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.620×** | -7.1 | 2e-10 | 20/25 (A549, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.625×** | -6.9 | 4e-10 | 18/25 (LoVo, HT-29, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.625×** | -6.9 | 4e-10 | 19/25 (A549, LoVo, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **0.628×** | -6.9 | 5e-10 | 19/24 (A549, SK-MEL-2, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.647×** | -6.4 | 8e-09 | 18/25 (A549, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.637×** | -6.4 | 8e-09 | 17/23 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.663×** | -6.1 | 7e-08 | 15/25 (SNU-1, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.677×** | -5.8 | 4e-07 | 18/25 (LoVo, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.697×** | -5.3 | 4e-06 | 18/24 (NCI-H2030, LoVo, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **0.704×** | -5.2 | 9e-06 | 18/24 (CFPAC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **0.515×** | -5.1 | 1e-05 | 13/25 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.538×** | -4.8 | 6e-05 | 17/26 (SNU-1, A-427, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.597×** | -4.0 | 0.002 | 9/24 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.611×** | -3.8 | 0.004 | 12/25 (A498, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.614×** | -3.8 | 0.005 | 13/25 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.783×** | -3.6 | 0.008 | 13/25 (CFPAC-1, A549, …) | two highest doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.647×** | -3.4 | 0.019 | 13/25 (A498, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.800×** | -3.2 | 0.036 | 6/25 (A498, A549, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.816×** | -3.0 | 0.060 | 10/25 (CFPAC-1, RKO, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.823×** | -2.9 | 0.083 | 6/25 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.825×** | -2.8 | 0.089 | 12/25 (A549, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.41 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12275. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 295 | 0 | 16 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0766× (z -32.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.128× (z -18.1) |
| [[LoVo (line)]] | wt | 133 | 0 | 16 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -23.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.299× (z -12.6) |
| [[A498 (line)]] | wt | 255 | 0 | 14 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -17.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 244 | 0 | 14 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0972× (z -31.2) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -14.6) |
| [[Hs 766T (line)]] | wt | 74.9 | 0 | 10 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -14.3) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 106 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -15.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -9.8) |
| [[HT-29 (line)]] | alt | 132 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -15.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 160 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -15.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 47.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -15.0) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -10.6) |
| [[J82 (line)]] | alt | 87.3 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -17.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2030 (line)]] | alt | 32.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[SNU-1 (line)]] | wt | 83.5 | 0 | 4 (3 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0359× (z -12.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.257× (z -9.5) |
| [[COLO 205 (line)]] | alt | 35.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0753× (z -16.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SNU-423 (line)]] | alt | 49.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.2) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 30.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[AN3 CA (line)]] | alt | 58.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0711× (z -12.3) |
| [[NCI-H2347 (line)]] | alt | 19.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.225× (z -9.3) ⚠ cell-cycle shift, explains ~30% of this change |
| [[RKO (line)]] | wt | 90.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -9.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -18.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[C-33 A (line)]] | alt | 44.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.191× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 16.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.13 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.13 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.81 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.76 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.10 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12275), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN2]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 | **novel candidate** |
| [[MUC16]] | +0.60 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SIDT1]] | +0.57 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PLA2R1]] | +0.56 | +0.55 / +0.45 | both halves | 3e-05 | **novel candidate** |
| [[TIMD4]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[GABRP]] | +0.54 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[MUC4]] | +0.53 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[CRACDL]] | +0.50 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[POU5F1]] | +0.49 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[THRB]] | +0.49 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[HNF1B]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ADGRF1]] | +0.48 | +0.42 / +0.44 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02985]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[SLC25A24P1]] | -0.41 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[CCDC102B]] | -0.41 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[PRRX1]] | -0.40 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[WNT5A]] | -0.39 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[F10]] | -0.39 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[LOXL3]] | -0.39 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[TET1]] | -0.39 | -0.23 / -0.46 | both halves | 5e-04 |  |
| [[LINC01905]] | -0.39 | -0.46 / -0.24 | both halves | 4e-04 |  |
| [[LINC00460]] | -0.38 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[NHSL1-AS1]] | -0.38 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ADAMTS18]] | -0.38 | -0.37 / -0.26 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 3, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIDT1]] | B | SIDT1 activity raises DAPK1's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.96× lower at baseline in the lines without SIDT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[APOL1]] | B | APOL1 activity raises DAPK1's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.59× lower at baseline in the lines without APOL1 | 0.074 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[TMC5]] | B | TMC5 activity raises DAPK1's level | lines that do not express TMC5 (29) vs lines expressing it (21) | 1.99× lower at baseline in the lines without TMC5 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TNFSF15, ENSG00000259925, TMPRSS4 |
| [[MUC16]] | C | MUC16 activity raises DAPK1's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.32× lower at baseline in the lines without MUC16 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; co-absent with the target |
| [[MMP7]] | C | MMP7 activity raises DAPK1's level | lines that do not express MMP7 (39) vs lines expressing it (11) | 3.71× lower at baseline in the lines without MMP7 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC5B, SFTPA2, GABRP; co-absent with the target |
| [[HAVCR1]] | C | HAVCR1 activity raises DAPK1's level | lines that do not express HAVCR1 (39) vs lines expressing it (11) | 3.96× lower at baseline in the lines without HAVCR1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TIMD4, RHEX, FGA; co-absent with the target |
| [[TIMD4]] | C | TIMD4 activity raises DAPK1's level | lines that do not express TIMD4 (40) vs lines expressing it (10) | 4.37× lower at baseline in the lines without TIMD4 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HAVCR1, RHEX, FGA; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGEF28]] | B | DAPK1 activity raises ARHGEF28's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without DAPK1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[PLAAT3]] | B | DAPK1 activity raises PLAAT3's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.70× lower at baseline in the lines without DAPK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[SLC37A1]] | B | DAPK1 activity raises SLC37A1's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.46× lower at baseline in the lines without DAPK1 | 0.035 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[CCDC102B]] | B | DAPK1 activity lowers CCDC102B's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.85× higher at baseline in the lines without DAPK1 | 0.036 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[PLSCR4]] | B | DAPK1 activity raises PLSCR4's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without DAPK1 | 0.046 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[TSPAN3]] | B | DAPK1 activity raises TSPAN3's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.41× lower at baseline in the lines without DAPK1 | 0.064 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[APOL1]] | B | DAPK1 activity raises APOL1's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without DAPK1 | 0.074 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[ST8SIA6]] | B | DAPK1 activity raises ST8SIA6's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.47× lower at baseline in the lines without DAPK1 | 0.084 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |
| [[CDK15]] | B | DAPK1 activity lowers CDK15's level | lines that do not express DAPK1 (23) vs lines expressing it (27) | 1.51× higher at baseline in the lines without DAPK1 | 0.097 | ⚠ within organs, on part of the lines; also absent: HAVCR1, DCDC2, ENSG00000275649 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.505). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.9, 56.4); signed map (62.4, 0.9). **Vector** length 77.4, 19.3% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +1.8 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.6 | +3.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.5 | +1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.5 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.5 | -4.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.3 | -11.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.1 | -9.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -3.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | death associated protein kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.33 — chr9:87,497,228-87,708,634 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAPK |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Death associated protein kinases; ROCO family |
| Reactome | 4 pathways, smallest: Caspase activation via Dependence Receptors in the absence of ligand; Caspase activation via extrinsic apoptotic signalling pathway; Apoptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [P53355](https://www.uniprot.org/uniprotkb/P53355) (Death-associated protein kinase 1):

> Calcium/calmodulin-dependent serine/threonine kinase involved in multiple cellular signaling pathways that trigger cell survival, apoptosis, and autophagy. Regulates both type I apoptotic and type II autophagic cell deaths signal, depending on the cellular setting. The former is caspase-dependent, while the latter is caspase-independent and is characterized by the accumulation of autophagic vesicles. Phosphorylates PIN1 resulting in inhibition of its catalytic activity, nuclear localization, …

**Summary**, from NCBI Gene [1612](https://www.ncbi.nlm.nih.gov/gene/1612):

> Death-associated protein kinase 1 is a positive mediator of gamma-interferon induced programmed cell death. DAPK1 encodes a structurally unique 160-kD calmodulin dependent serine-threonine kinase that carries 8 ankyrin repeats and 2 putative P-loop consensus sites. It is a tumor suppressor candidate. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:2674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2674) · Entrez [1612](https://www.ncbi.nlm.nih.gov/gene/1612) · UniProt [P53355](https://www.uniprot.org/uniprotkb/P53355) · Ensembl [ENSG00000196730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196730)

## Data

Gene col 12275: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12275); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12275, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12275]; `tensor/DDL_lfc|DDL_z.npy` [12275]; `embed/gene_vectors.npy` [12275]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12275 or target_col == 12275). Every well: [[DAPK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAPK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
