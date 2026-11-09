---
symbol: "GPRC5C"
type: "gene"
col: 9948
ensembl_id: "ENSG00000170412"
name: "G protein-coupled receptor class C group 5 member C"
location: "17q25.1"
module: 4
arm: "-"
pooled_cpm: 18.32
n_lines_expressing: 37
n_dd_up: 6
n_dd_down: 40
n_dd_up_clean: 6
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# GPRC5C

*G protein-coupled receptor class C group 5 member C* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +7.9, q 1e-12, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.241× (z -20.3, q 0e+00, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D4]] (+0.67, fdr 1e-05), [[IST1]] (+0.66, fdr 1e-05), [[ARID4B]] (+0.65, fdr 5e-05); moves opposite to [[EFTUD2]] (-0.63, fdr 9e-05), [[MTG1]] (-0.61, fdr 2e-04), [[AGK]] (-0.60, fdr 1e-04).
> It sits in the **-** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[DHRS3]] → it (grade B ⚠); 11 go from it, the strongest it → [[BCAP29]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9948.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +7.9 | 1e-12 | 19/32 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +4.5 | 0.002 | 15/34 (SW1417, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.016 | 12/35 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.057 | 4/30 (COLO 205, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.058 | 9/31 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.076 | 9/33 (A498, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.14 | 9/30 (SW1417, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.23× | +3.0 | 0.16 | 10/33 (HEC-1-A, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9948.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.241×** | -20.3 | 0e+00 | 32/34 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.267×** | -18.8 | 0e+00 | 32/34 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.334×** | -15.6 | 0e+00 | 31/34 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change; position correction uncertain | **0.394×** | -13.2 | 1e-37 | 26/27 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.477×** | -10.5 | 9e-24 | 27/34 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.518×** | -9.3 | 1e-18 | 25/34 (SW 900, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -7.8 | 4e-13 | 21/30 (Panc 03.27, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain | **0.565×** | -7.8 | 6e-13 | 19/23 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change; position correction uncertain | **0.598×** | -6.7 | 1e-09 | 18/26 (SW480, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.643×** | -6.2 | 3e-08 | 20/32 (SW 900, HT-29, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.670×** | -5.7 | 8e-07 | 18/34 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.671×** | -5.6 | 8e-07 | 18/34 (KATO III, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.756×** | -5.6 | 1e-06 | 20/34 (SW 900, HEC-1-A, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | **0.476×** | -5.5 | 2e-06 | 21/32 (SW 900, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.681×** | -5.4 | 2e-06 | 23/34 (SW 900, LS 180, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.488×** | -5.3 | 4e-06 | 20/34 (SW 900, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.679×** | -5.2 | 8e-06 | 19/31 (SW 900, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.703×** | -5.0 | 2e-05 | 18/34 (SW480, HEC-1-A, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.513×** | -4.9 | 2e-05 | 16/32 (SW 900, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.534×** | -4.7 | 9e-05 | 15/31 (RPMI-7951, SW1417, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.539×** | -4.6 | 1e-04 | 16/32 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.48 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9948. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 66.7 | 0 | 12 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0868× (z -17.0) |
| [[SW480 (line)]] | alt | 31.8 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0866× (z -22.2) |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -11.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.241× (z -9.6) |
| [[LoVo (line)]] | wt | 33.0 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.119× (z -18.5) |
| [[A498 (line)]] | wt | 27.4 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.212× (z -11.4) |
| [[LS 180 (line)]] | wt | 23.7 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.235× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 23.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change; position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.256× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.140× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 24.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.263× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 84.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -13.6) |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.152× (z -12.5) |
| [[COLO 205 (line)]] | alt | 37.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 22.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -11.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.194× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -11.4) |
| [[SW1417 (line)]] | alt | 35.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change; position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -10.1) |
| [[A549 (line)]] | wt | 11.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change; position correction uncertain |
| [[H4 (line)]] | wt | 16.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0826× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 6.45 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.128× (z -8.7) |
| [[SNU-423 (line)]] | alt | 43.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -13.8) |
| [[HCT15 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.279× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change; position correction uncertain |
| [[NCI-H23 (line)]] | alt | 7.80 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0913× (z -10.1) |
| [[PANC-1 (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +10.6) | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.156× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.151× (z -8.9) |
| [[A-172 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.67 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9948), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D4]] | +0.67 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[IST1]] | +0.66 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ARID4B]] | +0.65 | +0.39 / +0.66 | both halves | 5e-05 |  |
| [[EFNA1]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[TESK2]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[CCNG2]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[STARD10]] | +0.59 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[CXXC5]] | +0.58 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[GATA2]] | +0.58 | +0.32 / +0.57 | both halves | 1e-04 |  |
| [[CDC42EP4]] | +0.58 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[DHRS3]] | +0.58 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[ATOSA]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.63 | -0.37 / -0.65 | both halves | 9e-05 |  |
| [[MTG1]] | -0.61 | -0.32 / -0.64 | both halves | 2e-04 |  |
| [[AGK]] | -0.60 | -0.36 / -0.66 | both halves | 1e-04 |  |
| [[DROSHA]] | -0.60 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[CLPB]] | -0.59 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[GFM1]] | -0.59 | -0.42 / -0.62 | both halves | 4e-05 |  |
| [[FARSB]] | -0.59 | -0.34 / -0.65 | both halves | 1e-04 |  |
| [[BCAP29]] | -0.58 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[ELAC2]] | -0.57 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[POFUT1]] | -0.57 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[SLC25A24]] | -0.56 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[IPO9]] | -0.56 | -0.35 / -0.63 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DHRS3]] | B | DHRS3 activity raises GPRC5C's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 2.99× lower at baseline in the lines without DHRS3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[RNF39]] | B | RNF39 activity raises GPRC5C's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.23× lower at baseline in the lines without RNF39 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[ELF3]] | B | ELF3 activity raises GPRC5C's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 3.30× lower at baseline in the lines without ELF3 | 0.005 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[SPINT1]] | B | SPINT1 activity raises GPRC5C's level | lines that do not express SPINT1 (25) vs lines expressing it (25) | 2.89× lower at baseline in the lines without SPINT1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MARVELD3, CRB3, SPINT1-AS1 |
| [[HNF1B]] | B | HNF1B activity raises GPRC5C's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without HNF1B | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[GRB7]] | B | GRB7 activity raises GPRC5C's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 2.76× lower at baseline in the lines without GRB7 | 0.077 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP |
| [[CXXC5]] | B | CXXC5 activity raises GPRC5C's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 2.47× lower at baseline in the lines without CXXC5 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[FBXO32]] | B | FBXO32 activity raises GPRC5C's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without FBXO32 | 0.094 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[VAMP8]] | C | VAMP8 activity raises GPRC5C's level | lines that do not express VAMP8 (14) vs lines expressing it (36) | 4.49× lower at baseline in the lines without VAMP8 | 8e-04 | ⚠ within organs, on part of the lines; also absent: CDCP1, CHMP4C, EVPL; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCAP29]] | B | GPRC5C activity lowers BCAP29's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.64× higher at baseline in the lines without GPRC5C | 0.010 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[DHRS3]] | B | GPRC5C activity raises DHRS3's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 3.02× lower at baseline in the lines without GPRC5C | 0.013 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[BCL2L14]] | B | GPRC5C activity raises BCL2L14's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without GPRC5C | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[VPS4A]] | B | GPRC5C activity lowers VPS4A's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.20× higher at baseline in the lines without GPRC5C | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[SELENOM]] | B | GPRC5C activity lowers SELENOM's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.62× higher at baseline in the lines without GPRC5C | 0.051 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[CBX4]] | B | GPRC5C activity raises CBX4's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.47× lower at baseline in the lines without GPRC5C | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[EFNA1]] | B | GPRC5C activity raises EFNA1's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 2.41× lower at baseline in the lines without GPRC5C | 0.080 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[ELF3]] | B | GPRC5C activity raises ELF3's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 4.73× lower at baseline in the lines without GPRC5C | 0.082 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[SEC22C]] | B | GPRC5C activity lowers SEC22C's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.48× higher at baseline in the lines without GPRC5C | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[TERF2IP]] | B | GPRC5C activity lowers TERF2IP's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 1.17× higher at baseline in the lines without GPRC5C | 0.088 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1 |
| [[VAMP8]] | C | GPRC5C activity raises VAMP8's level | lines that do not express GPRC5C (13) vs lines expressing it (37) | 2.74× lower at baseline in the lines without GPRC5C | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM184A, VAMP8, ASS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **-** arm (projection on the module's main direction -0.603). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-4.2, -39.7); signed map (-8.1, 4.8). **Vector** length 92.3, 23.7% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +1.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.2 | -9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change; position correction uncertain | -4.1 | -13.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change; position correction uncertain | -4.1 | -7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change; position correction uncertain | -3.4 | -6.7 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM | ⚠ position correction uncertain | -2.8 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | G protein-coupled receptor class C group 5 member C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,424,851-74,451,653 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAIG-3 |
| Gene groups (HGNC) | G protein-coupled receptors, Class C orphans |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ84](https://www.uniprot.org/uniprotkb/Q9NQ84) (G protein-coupled receptor family C group 5 member C):

> This retinoic acid-inducible G protein-coupled receptor provide evidence for a possible interaction between retinoid and G-protein signaling pathways.

**Summary**, from NCBI Gene [55890](https://www.ncbi.nlm.nih.gov/gene/55890):

> The protein encoded by this gene is a member of the type 3 G protein-coupled receptor family. Members of this superfamily are characterized by a signature 7-transmembrane domain motif. The specific function of this protein is unknown; however, this protein may mediate the cellular effects of retinoic acid on the G protein signal transduction cascade. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13309) · Entrez [55890](https://www.ncbi.nlm.nih.gov/gene/55890) · UniProt [Q9NQ84](https://www.uniprot.org/uniprotkb/Q9NQ84) · Ensembl [ENSG00000170412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170412)

## Data

Gene col 9948: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9948); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9948, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9948]; `tensor/DDL_lfc|DDL_z.npy` [9948]; `embed/gene_vectors.npy` [9948]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9948 or target_col == 9948). Every well: [[GPRC5C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPRC5C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
