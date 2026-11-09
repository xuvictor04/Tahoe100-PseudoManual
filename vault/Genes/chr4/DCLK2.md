---
symbol: "DCLK2"
type: "gene"
col: 9946
ensembl_id: "ENSG00000170390"
name: "doublecortin like kinase 2"
location: "4q31.23-q31.3"
module: 8
arm: "+"
pooled_cpm: 61.91
n_lines_expressing: 33
n_dd_up: 5
n_dd_down: 24
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 29
direction_downstream: 43
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# DCLK2

*doublecortin like kinase 2* — 4q31.23-q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Binimetinib (drug)]] 5 µM: 1.44× (z +5.6, q 8e-06, up in 16 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.498× (z -11.2, q 2e-26, down in 22 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL5A2]] (+0.59, fdr 1e-05), [[RNF220]] (+0.51, fdr 5e-05), [[BASP1-AS1]] (+0.51, fdr 7e-05); moves opposite to [[PTPRE]] (-0.54, fdr 3e-05), [[TMEM51-AS1]] (-0.52, fdr 1e-05), [[TMEM51]] (-0.50, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[ERBB3]] → it (grade B ⚠); 43 go from it, the strongest it → [[B3GNT3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Binimetinib (drug)]] 5 µM |  | **1.44×** | +5.6 | 8e-06 | 16/31 (HOP62, H4, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +5.5 | 8e-06 | 16/31 (HOP62, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +5.4 | 1e-05 | 16/31 (HOP62, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.9 | 1e-04 | 16/31 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.028 | 13/31 (HOP62, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.25× | +3.2 | 0.11 | 13/31 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.23× | +3.2 | 0.11 | 13/30 (HOP62, HS-578T, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | 1.22× | +3.0 | 0.15 | 9/31 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.15 | 9/31 (HOP62, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.15 | 12/30 (HOP62, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -11.2 | 2e-26 | 22/31 (A549, C-33 A, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.539×** | -9.9 | 8e-21 | 22/31 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.574×** | -8.9 | 8e-17 | 23/30 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.595×** | -8.3 | 1e-14 | 21/31 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.611×** | -7.1 | 1e-10 | 20/31 (A-172, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -6.8 | 1e-09 | 19/31 (PANC-1, NCI-H23, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.659×** | -6.7 | 2e-09 | 20/31 (A549, MIA PaCa-2, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.672×** | -6.4 | 1e-08 | 19/31 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -5.9 | 2e-07 | 16/31 (AN3 CA, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.693×** | -5.9 | 2e-07 | 17/31 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.697×** | -5.8 | 3e-07 | 17/31 (NCI-H23, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.704×** | -5.6 | 8e-07 | 17/31 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **0.721×** | -5.3 | 6e-06 | 19/29 (PANC-1, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.803×** | -5.0 | 3e-05 | 17/31 (A-172, NCI-H2030, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.566×** | -4.8 | 6e-05 | 15/31 (RKO, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -4.7 | 9e-05 | 16/31 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.768×** | -4.1 | 0.001 | 13/31 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.807×** | -3.4 | 0.014 | 11/31 (A-172, MIA PaCa-2, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.824×** | -3.1 | 0.043 | 13/31 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.836× | -2.9 | 0.084 | 11/31 (A549, PANC-1, …) | top dose only |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.882× | -2.8 | 0.087 | 5/31 (NCI-H2030, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 405 | 0 | 13 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.145× (z -14.5) |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -14.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.381× (z -10.1) |
| [[A549 (line)]] | wt | 112 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.146× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.240× (z -14.5) |
| [[PANC-1 (line)]] | alt | 116 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 54.0 | 0 | 8 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.170× (z -15.6) |
| [[NCI-H460 (line)]] | wt | 172 | 0 | 8 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.232× (z -11.9) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.288× (z -10.5) |
| [[HOP62 (line)]] | alt | 53.7 | 7 (2 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +14.3) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 0.5 µM 3.01× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 31.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.8) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 173 | 1 (1 ⚠) | 4 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +11.0) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.254× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 63.6 | 1 (1 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +8.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.272× (z -11.3) |
| [[A-427 (line)]] | wt | 67.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.428× (z -8.6) |
| [[C-33 A (line)]] | alt | 189 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0664× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.275× (z -13.7) |
| [[A498 (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -11.7) |
| [[AN3 CA (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.112× (z -13.1) |
| [[J82 (line)]] | alt | 62.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.29× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 45.5 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.148× (z -14.9) |
| [[H4 (line)]] | wt | 128 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.170× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.21× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[AsPC-1 (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.19 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.93 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.05 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL5A2]] | +0.59 | +0.56 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[RNF220]] | +0.51 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[BASP1-AS1]] | +0.51 | +0.56 / +0.38 | both halves | 7e-05 |  |
| [[UNC5C]] | +0.50 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[HECW2]] | +0.48 | +0.52 / +0.33 | both halves | 1e-04 |  |
| [[JADE1]] | +0.48 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[NALCN]] | +0.47 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[SAMD11]] | +0.47 | +0.53 / +0.31 | both halves | 2e-04 |  |
| [[CHN1]] | +0.47 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[SLC39A8]] | +0.46 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[LINC00466]] | +0.46 | +0.49 / +0.30 | both halves | 2e-04 |  |
| [[SHTN1]] | +0.46 | +0.47 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRE]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TMEM51-AS1]] | -0.52 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[TMEM51]] | -0.50 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TNFRSF14-AS1]] | -0.49 | -0.50 / -0.39 | both halves | 5e-05 |  |
| [[ADCY4]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[LASTR]] | -0.47 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TMC4]] | -0.47 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ABHD17C]] | -0.47 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[BACE2]] | -0.47 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[RINL]] | -0.45 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[TMEM45B]] | -0.44 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[TMEM125]] | -0.44 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 24, C 5. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERBB3]] | B | ERBB3 activity lowers DCLK2's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 5.61× higher at baseline in the lines without ERBB3 | 0.001 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[TMEM125]] | B | TMEM125 activity lowers DCLK2's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 5.38× higher at baseline in the lines without TMEM125 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[INAVA]] | B | INAVA activity lowers DCLK2's level | lines that do not express INAVA (29) vs lines expressing it (21) | 4.90× higher at baseline in the lines without INAVA | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[MPZL2]] | B | MPZL2 activity lowers DCLK2's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 5.82× higher at baseline in the lines without MPZL2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[B3GNT3]] | B | B3GNT3 activity lowers DCLK2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 5.46× higher at baseline in the lines without B3GNT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[FUT3]] | B | FUT3 activity lowers DCLK2's level | lines that do not express FUT3 (29) vs lines expressing it (21) | 3.05× higher at baseline in the lines without FUT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ATP2C2, TMEM125, ENSG00000243004 |
| [[LINC03040]] | B | LINC03040 activity lowers DCLK2's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 4.20× higher at baseline in the lines without LINC03040 | 0.003 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[TGFA]] | B | TGFA activity lowers DCLK2's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.01× higher at baseline in the lines without TGFA | 0.003 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[ADCY4]] | B | ADCY4 activity lowers DCLK2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 4.46× higher at baseline in the lines without ADCY4 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[RORC]] | B | RORC activity lowers DCLK2's level | lines that do not express RORC (30) vs lines expressing it (20) | 3.15× higher at baseline in the lines without RORC | 0.008 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[TMEM45B]] | B | TMEM45B activity lowers DCLK2's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 5.03× higher at baseline in the lines without TMEM45B | 0.009 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881 |
| [[TMCC3]] | B | TMCC3 activity lowers DCLK2's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.91× higher at baseline in the lines without TMCC3 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 37, C 6. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B3GNT3]] | B | DCLK2 activity lowers B3GNT3's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 7.76× higher at baseline in the lines without DCLK2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[ERBB3]] | B | DCLK2 activity lowers ERBB3's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 5.97× higher at baseline in the lines without DCLK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[TMC4]] | B | DCLK2 activity lowers TMC4's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 5.74× higher at baseline in the lines without DCLK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[MPZL2]] | B | DCLK2 activity lowers MPZL2's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 7.57× higher at baseline in the lines without DCLK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[INAVA]] | B | DCLK2 activity lowers INAVA's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 6.84× higher at baseline in the lines without DCLK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[TMEM125]] | B | DCLK2 activity lowers TMEM125's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.38× higher at baseline in the lines without DCLK2 | 0.005 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[TMEM45B]] | B | DCLK2 activity lowers TMEM45B's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 7.82× higher at baseline in the lines without DCLK2 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[TNFRSF14-AS1]] | B | DCLK2 activity lowers TNFRSF14-AS1's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 2.79× higher at baseline in the lines without DCLK2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[ADCY4]] | B | DCLK2 activity lowers ADCY4's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.13× higher at baseline in the lines without DCLK2 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[LASTR]] | B | DCLK2 activity lowers LASTR's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.92× higher at baseline in the lines without DCLK2 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[TGFA]] | B | DCLK2 activity lowers TGFA's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.47× higher at baseline in the lines without DCLK2 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |
| [[FAM171A1]] | B | DCLK2 activity raises FAM171A1's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 1.66× lower at baseline in the lines without DCLK2 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction -0.329). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, 39.5); signed map (23.2, 29.3). **Vector** length 97.4, 26.7% of its response variance represented; |z| ≥ 3 in 976 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.4 | +5.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +2.8 | +4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.7 | +3.2 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -3.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.1 | -3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | -3.0 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -9.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.4 | -2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -6.8 |
|  | [[Belzutifan (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | doublecortin like kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.23-q31.3 — chr4:150,078,445-150,257,438 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45428, DCDC3, DCDC3B, DCK2; previously DCAMKL2 |
| Gene groups (HGNC) | Doublecortin superfamily; Doublecortin like kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N568](https://www.uniprot.org/uniprotkb/Q8N568) (Serine/threonine-protein kinase DCLK2):

> Protein kinase with a significantly reduced C(a2+)/CAM affinity and dependence compared to other members of the CaMK family. May play a role in the down-regulation of CRE-dependent gene activation probably by phosphorylation of the CREB coactivator CRTC2/TORC2 and the resulting retention of TORC2 in the cytoplasm (By similarity).

**Summary**, from NCBI Gene [166614](https://www.ncbi.nlm.nih.gov/gene/166614):

> This gene encodes a member of the protein kinase superfamily and the doublecortin family. The protein encoded by this gene contains two N-terminal doublecortin domains, which bind microtubules and regulate microtubule polymerization, a C-terminal serine/threonine protein kinase domain, which shows substantial homology to Ca2+/calmodulin-dependent protein kinase, and a serine/proline-rich domain in between the doublecortin and the protein kinase domains, which mediates multiple protein-protein …

**Accessions** — [HGNC:19002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19002) · Entrez [166614](https://www.ncbi.nlm.nih.gov/gene/166614) · UniProt [Q8N568](https://www.uniprot.org/uniprotkb/Q8N568) · Ensembl [ENSG00000170390](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170390)

## Data

Gene col 9946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9946); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9946]; `tensor/DDL_lfc|DDL_z.npy` [9946]; `embed/gene_vectors.npy` [9946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9946 or target_col == 9946). Every well: [[DCLK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCLK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
