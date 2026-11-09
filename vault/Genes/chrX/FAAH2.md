---
symbol: "FAAH2"
type: "gene"
col: 9148
ensembl_id: "ENSG00000165591"
name: "fatty acid amide hydrolase 2"
location: "Xp11.21"
module: 8
arm: "+"
pooled_cpm: 55.86
n_lines_expressing: 24
n_dd_up: 23
n_dd_down: 26
n_dd_up_clean: 20
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 105
direction_downstream: 148
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FAAH2

*fatty acid amide hydrolase 2* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.71× (z +7.5, q 5e-11, up in 1 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.66× (z +6.8, q 4e-09, up in 19 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.464× (z -10.7, q 9e-24, down in 20 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATA6L]] (+0.75, fdr 7e-06), [[RORC]] (+0.73, fdr 7e-06), [[LINC02253]] (+0.72, fdr 7e-06); moves opposite to [[ITGB1BP1]] (-0.52, fdr 2e-05), [[TRIM65]] (-0.52, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 105 arrows point to it, the strongest [[SLC44A3]] → it (grade B ⚠); 148 go from it, the strongest it → [[PRRG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +7.5 | 5e-11 | 1/22 (AsPC-1) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +6.8 | 4e-09 | 19/22 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 4e-08 | 18/22 (SW480, BT-474, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 6e-07 | 17/22 (SW480, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +5.5 | 6e-06 | 16/22 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.44×** | +5.1 | 3e-05 | 17/22 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.42×** | +5.0 | 4e-05 | 19/24 (SW480, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +5.0 | 5e-05 | 15/23 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.41×** | +4.9 | 7e-05 | 14/23 (SW480, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.42×** | +4.9 | 7e-05 | 13/22 (KATO III, LoVo, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 6/22 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.003 | 15/23 (BT-474, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.014 | 12/22 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.021 | 13/22 (KATO III, SW480, …) | two highest doses |  |
| [[Afatinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.026 | 10/23 (BT-474, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.59×** | +3.4 | 0.028 | 18/24 (NCI-H2347, HEC-1-A, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.028 | 9/20 (SW480, SHP-77, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9148.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.464×** | -10.7 | 9e-24 | 20/22 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.483×** | -10.1 | 1e-21 | 20/22 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.539×** | -8.6 | 2e-15 | 21/22 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -8.0 | 1e-13 | 20/23 (COLO 205, KATO III, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.562×** | -7.7 | 2e-12 | 17/22 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.595×** | -7.2 | 5e-11 | 21/22 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.598×** | -7.1 | 8e-11 | 19/22 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.643×** | -6.1 | 7e-08 | 15/22 (COLO 205, SHP-77, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.665×** | -5.7 | 9e-07 | 19/22 (SW480, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.680×** | -5.3 | 5e-06 | 14/22 (CFPAC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.678×** | -5.2 | 1e-05 | 7/22 (SW480, CFPAC-1, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.690×** | -5.1 | 1e-05 | 14/21 (COLO 205, SW480, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.499×** | -5.0 | 2e-05 | 17/22 (CFPAC-1, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -4.8 | 8e-05 | 14/23 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.698×** | -4.7 | 1e-04 | 9/22 (SW480, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.731×** | -4.3 | 5e-04 | 13/21 (COLO 205, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.675×** | -3.9 | 0.003 | 9/22 (SHP-77, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.779×** | -3.5 | 0.014 | 14/22 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -3.3 | 0.027 | 13/22 (HCT15, CFPAC-1, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.801×** | -2.8 | 0.098 | 3/22 (AN3 CA, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 189 | 0 | 14 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -15.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -14.3) |
| [[COLO 205 (line)]] | alt | 176 | 0 | 12 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0948× (z -21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.183× (z -15.7) |
| [[SHP-77 (line)]] | alt | 267 | 0 | 12 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.290× (z -12.9) |
| [[HT-29 (line)]] | alt | 133 | 0 | 11 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.105× (z -19.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 222 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -12.1) |
| [[SW480 (line)]] | alt | 72.7 | 1 | 9 (6 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.14× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -17.1) |
| [[Panc 03.27 (line)]] | alt | 159 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.349× (z -9.0) |
| [[HCT15 (line)]] | alt | 144 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.164× (z -13.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.271× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 65.0 | 0 | 6 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0372× (z -20.4) ⚠ toxic; cell-cycle shift, explains ~53% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.145× (z -12.4) |
| [[KATO III (line)]] | alt | 186 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -11.8) |
| [[LoVo (line)]] | wt | 101 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.398× (z -9.1) |
| [[LS 180 (line)]] | wt | 187 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.345× (z -10.2) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.6) |
| [[SW1417 (line)]] | alt | 39.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 94.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.461× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 130 | 1 | 0 | [[Afatinib (drug)]] 0.5 µM 3.14× (z +10.1) | — |
| [[NCI-H2347 (line)]] | alt | 48.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.9) |
| [[SW48 (line)]] | wt | 111 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -9.1) |
| [[A-172 (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.83 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 12.1 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.32 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.52 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.9 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.66 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.78 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.88 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.34 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.08 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.99 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATA6L]] | +0.75 | +0.66 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[RORC]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC02253]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[TOX3]] | +0.71 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[BCAS1]] | +0.70 | +0.66 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[ARHGEF38]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[ERBB3]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[TMC4]] | +0.69 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[LINC01814]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[LINC00299]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ANK3]] | +0.68 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[NIHCOLE]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.52 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[TRIM65]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*105 arrows, 105 of them with an alert ⚠; grade A 0, B 18, C 87. Shown: the 12 strongest; 93 more arrows (93 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC44A3]] | B | SLC44A3 activity raises FAAH2's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.16× lower at baseline in the lines without SLC44A3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[LNX1]] | B | LNX1 activity raises FAAH2's level | lines that do not express LNX1 (20) vs lines expressing it (30) | 2.85× lower at baseline in the lines without LNX1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, EGF, KLF8 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises FAAH2's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 3.22× lower at baseline in the lines without SLC44A3-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[EFNA1]] | B | EFNA1 activity raises FAAH2's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 4.31× lower at baseline in the lines without EFNA1 | 0.013 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises FAAH2's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.35× lower at baseline in the lines without ATP8B1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[FRMD4B]] | B | FRMD4B activity raises FAAH2's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 2.89× lower at baseline in the lines without FRMD4B | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[PARVB]] | B | PARVB activity lowers FAAH2's level | lines that do not express PARVB (13) vs lines expressing it (37) | 4.65× higher at baseline in the lines without PARVB | 0.045 | ⚠ within organs, on part of the lines; also absent: PARVG, MSRB3, RASSF8 |
| [[PCAT1]] | B | PCAT1 activity raises FAAH2's level | lines that do not express PCAT1 (11) vs lines expressing it (39) | 3.47× lower at baseline in the lines without PCAT1 | 0.049 | ⚠ within organs, on part of the lines; also absent: POU5F1B, MCF2L, LRATD2; maybe low, not absent |
| [[MAP2K6]] | B | MAP2K6 activity raises FAAH2's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 2.22× lower at baseline in the lines without MAP2K6 | 0.056 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |
| [[KLF8]] | B | KLF8 activity raises FAAH2's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without KLF8 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692 |
| [[MAP2K1]] | B | MAP2K1 activity lowers FAAH2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[POU5F1B]] | B | POU5F1B activity raises FAAH2's level | lines that do not express POU5F1B (14) vs lines expressing it (36) | 3.13× lower at baseline in the lines without POU5F1B | 0.071 | ⚠ within organs, on part of the lines; also absent: PCAT1, LRATD2, MYB; maybe low, not absent |

### Downstream of this gene

*148 arrows, 148 of them with an alert ⚠; grade A 0, B 62, C 86. Shown: the 12 strongest; 136 more arrows (136 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRRG2]] | B | FAAH2 activity raises PRRG2's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.53× lower at baseline in the lines without FAAH2 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[LNX1]] | B | FAAH2 activity raises LNX1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 4.26× lower at baseline in the lines without FAAH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[SLC44A3]] | B | FAAH2 activity raises SLC44A3's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.75× lower at baseline in the lines without FAAH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[SLC44A3-AS1]] | B | FAAH2 activity raises SLC44A3-AS1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.55× lower at baseline in the lines without FAAH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[MUC20]] | B | FAAH2 activity raises MUC20's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.34× lower at baseline in the lines without FAAH2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[BCL2L15]] | B | FAAH2 activity raises BCL2L15's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.52× lower at baseline in the lines without FAAH2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[IL17RE]] | B | FAAH2 activity raises IL17RE's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.82× lower at baseline in the lines without FAAH2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[ICA1]] | B | FAAH2 activity raises ICA1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.51× lower at baseline in the lines without FAAH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[PCAT1]] | B | FAAH2 activity raises PCAT1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without FAAH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[SH3BGRL2]] | B | FAAH2 activity raises SH3BGRL2's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.17× lower at baseline in the lines without FAAH2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[ITGB1BP1]] | B | FAAH2 activity lowers ITGB1BP1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 1.39× higher at baseline in the lines without FAAH2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |
| [[CCSER1]] | B | FAAH2 activity raises CCSER1's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 3.14× lower at baseline in the lines without FAAH2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 49.5); signed map (57.8, 4.3). **Vector** length 116, 45.8% of its response variance represented; |z| ≥ 3 in 899 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | -0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.6 | +6.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.2 | -2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +4.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +5.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.8 | +5.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -7.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -1.9 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -1.8 | -4.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.8 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.7 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | fatty acid amide hydrolase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:57,286,706-57,489,193 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-479E16.1, FLJ31204, FAAH-2; previously AMDD |
| Gene groups (HGNC) | N-arachidonoylethanolamine hydrolases |
| Reactome | 3 pathways, smallest: Arachidonate metabolism; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6GMR7](https://www.uniprot.org/uniprotkb/Q6GMR7) (Fatty-acid amide hydrolase 2):

> Catalyzes the hydrolysis of endogenous amidated lipids like the sleep-inducing lipid oleamide ((9Z)-octadecenamide), the endocannabinoid anandamide (N-(5Z,8Z,11Z,14Z-eicosatetraenoyl)-ethanolamine), as well as other fatty amides, to their corresponding fatty acids, thereby regulating the signaling functions of these molecules. Hydrolyzes monounsaturated substrate anandamide preferentially as compared to polyunsaturated substrates.

**Summary**, from NCBI Gene [158584](https://www.ncbi.nlm.nih.gov/gene/158584):

> This gene encodes a fatty acid amide hydrolase that shares a conserved protein motif with the amidase signature family of enzymes. The encoded enzyme is able to catalyze the hydrolysis of a broad range of bioactive lipids, including those from the three main classes of fatty acid amides; N-acylethanolamines, fatty acid primary amides and N-acyl amino acids. This enzyme has a preference for monounsaturated acyl chains as a substrate. Alternate splicing results in multiple transcript variants …

**Accessions** — [HGNC:26440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26440) · Entrez [158584](https://www.ncbi.nlm.nih.gov/gene/158584) · UniProt [Q6GMR7](https://www.uniprot.org/uniprotkb/Q6GMR7) · Ensembl [ENSG00000165591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165591)

## Data

Gene col 9148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9148); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9148]; `tensor/DDL_lfc|DDL_z.npy` [9148]; `embed/gene_vectors.npy` [9148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9148 or target_col == 9148). Every well: [[FAAH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAAH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
