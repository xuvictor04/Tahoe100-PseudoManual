---
symbol: "CASC9"
type: "gene"
col: 14609
ensembl_id: "ENSG00000249395"
name: "cancer susceptibility 9"
location: "8q21.13"
module: 77
arm: "-"
pooled_cpm: 46.36
n_lines_expressing: 28
n_dd_up: 22
n_dd_down: 44
n_dd_up_clean: 19
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# CASC9

*cancer susceptibility 9* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.51× (z +8.1, q 3e-13, up in 15 of 26 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +7.0, q 9e-10, up in 15 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 44 drug-doses (14 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.204× (z -22.1, q 0e+00, down in 26 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIPK2-DT]] (+0.69, fdr 1e-05), [[TIA1]] (+0.67, fdr 1e-05), [[TAPBPL]] (+0.66, fdr 1e-05); moves opposite to [[EIF4EBP1]] (-0.67, fdr 1e-05), [[ANKRD27]] (-0.67, fdr 7e-06), [[LPCAT4]] (-0.66, fdr 1e-05).
> It sits in the **-** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[ENG]] → it (grade B ⚠); 4 go from it, the strongest it → [[KMO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14609.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.51×** | +8.1 | 3e-13 | 15/26 (J82, A498, …) | rises with dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +7.0 | 9e-10 | 15/26 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.58×** | +6.2 | 1e-07 | 17/26 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.57×** | +6.0 | 2e-07 | 21/26 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 4e-07 | 16/26 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.51×** | +5.7 | 1e-06 | 21/26 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.47×** | +5.3 | 1e-05 | 14/27 (NCI-H460, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 2e-05 | 17/26 (NCI-H460, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.42×** | +4.8 | 1e-04 | 18/27 (NCI-H460, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +4.7 | 1e-04 | 14/26 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 2e-04 | 14/27 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.4 | 5e-04 | 13/26 (J82, NCI-H23, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +3.8 | 0.006 | 8/26 (J82, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 14/26 (RKO, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.29×** | +3.6 | 0.014 | 10/26 (J82, A498, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.31×** | +3.5 | 0.015 | 15/26 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.021 | 12/26 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.4 | 0.023 | 8/26 (A498, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 44 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14609.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.204×** | -22.1 | 0e+00 | 26/26 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.227×** | -20.6 | 0e+00 | 26/26 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.278×** | -17.8 | 0e+00 | 25/26 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.362×** | -14.1 | 4e-43 | 26/26 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.437×** | -11.5 | 2e-28 | 26/26 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.458×** | -10.8 | 2e-25 | 25/26 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.521×** | -9.0 | 1e-17 | 20/26 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.517×** | -8.6 | 4e-16 | 20/26 (NCI-H1573, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.554×** | -8.2 | 2e-14 | 19/26 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.605×** | -7.0 | 2e-10 | 21/26 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.402×** | -6.6 | 2e-09 | 19/27 (HEC-1-A, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -6.5 | 4e-09 | 21/26 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.631×** | -6.4 | 7e-09 | 19/26 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.415×** | -6.4 | 7e-09 | 21/27 (NCI-H1573, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.738×** | -6.0 | 1e-07 | 21/27 (NCI-H1573, HT-29, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.478×** | -5.4 | 3e-06 | 16/26 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.679×** | -5.2 | 8e-06 | 19/26 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.690×** | -5.1 | 9e-06 | 17/26 (NCI-H1573, SW48, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14609. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 109 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0939× (z -24.2) |
| [[NCI-H460 (line)]] | wt | 225 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -20.3) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.114× (z -18.9) |
| [[NCI-H1792 (line)]] | alt | 90.8 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0620× (z -23.3) |
| [[COLO 205 (line)]] | alt | 65.8 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0497× (z -21.2) |
| [[HT-29 (line)]] | alt | 70.1 | 0 | 9 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.112× (z -18.3) |
| [[RKO (line)]] | wt | 31.6 | 3 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.0992× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.108× (z -14.7) |
| [[A549 (line)]] | wt | 56.2 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.100× (z -16.0) |
| [[Hs 766T (line)]] | wt | 60.5 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -13.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.139× (z -13.0) |
| [[SW480 (line)]] | alt | 63.2 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -16.9) |
| [[A498 (line)]] | wt | 74.2 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 180 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 27.0 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.215× (z -12.8) |
| [[SW 900 (line)]] | alt | 140 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.0892× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 25.2 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.133× (z -11.0) |
| [[J82 (line)]] | alt | 31.1 | 2 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.223× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 41.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.118× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.152× (z -10.3) |
| [[SHP-77 (line)]] | alt | 101 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.153× (z -14.5) |
| [[A-172 (line)]] | wt | 47.4 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.273× (z -9.1) |
| [[LoVo (line)]] | wt | 27.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.175× (z -13.4) |
| [[SW48 (line)]] | wt | 25.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +8.6) | [[Ixazomib citrate (drug)]] 0.5 µM 0.0992× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 19.5 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.226× (z -8.5) |
| [[HS-578T (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +9.1) | — |
| [[A-427 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.39 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.31 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.81 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.16 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.83 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.30 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.06 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14609), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIPK2-DT]] | +0.69 | +0.67 / +0.49 | both halves | 1e-05 | same gene group |
| [[TIA1]] | +0.67 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TAPBPL]] | +0.66 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[BAZ2B]] | +0.66 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PATL2]] | +0.65 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.65 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ZNF747]] | +0.65 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[GUCY1B2]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[TIGD6]] | +0.64 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[ZNF764]] | +0.64 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.64 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[REPIN1]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4EBP1]] | -0.67 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[ANKRD27]] | -0.67 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[LPCAT4]] | -0.66 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[IMPDH1]] | -0.66 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[LPCAT1]] | -0.65 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[BICD2]] | -0.65 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[RGS10]] | -0.65 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[TPST2]] | -0.65 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TCF3]] | -0.64 | -0.63 / -0.51 | both halves | 1e-05 |  |
| [[TMEM120B]] | -0.63 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[MAP2K1]] | -0.63 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ST6GALNAC6]] | -0.63 | -0.59 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENG]] | B | ENG activity raises CASC9's level | lines that do not express ENG (17) vs lines expressing it (33) | 2.03× lower at baseline in the lines without ENG | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000286076, CSPG4, EGF; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CASC9's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[STAT5A]] | B | STAT5A activity raises CASC9's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without STAT5A | 0.071 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[GNGT1]] | B | GNGT1 activity raises CASC9's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 2.16× lower at baseline in the lines without GNGT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3 |
| [[FRMD4B]] | B | FRMD4B activity raises CASC9's level | lines that do not express FRMD4B (20) vs lines expressing it (30) | 1.96× lower at baseline in the lines without FRMD4B | 0.081 | ⚠ within organs, on part of the lines; also absent: LINC01589, ENSG00000290729, FRK; maybe low, not absent |
| [[BBOX1-AS1]] | C | BBOX1-AS1 activity raises CASC9's level | lines that do not express BBOX1-AS1 (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without BBOX1-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: GLDN, CHN2, CPVL; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KMO]] | B | CASC9 activity lowers KMO's level | lines that do not express CASC9 (22) vs lines expressing it (28) | 1.37× higher at baseline in the lines without CASC9 | 0.054 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5 |
| [[TPRG1]] | B | CASC9 activity raises TPRG1's level | lines that do not express CASC9 (22) vs lines expressing it (28) | 2.07× lower at baseline in the lines without CASC9 | 0.075 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5 |
| [[TPRG1]] | B | CASC9 activity strengthens TPRG1's drug response | lines that do not express CASC9 (16) vs lines expressing it (23) | the lines without CASC9 respond 0.50× as strongly (z diff +2.08); strongest at Digitoxin 5 µM: 0.56x vs 0.29x (z diff +3.6) | 0.086 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5; target measured in part of the lines; artifact flags |
| [[BBOX1-AS1]] | C | CASC9 activity raises BBOX1-AS1's level | lines that do not express CASC9 (22) vs lines expressing it (28) | 3.25× lower at baseline in the lines without CASC9 | 0.006 | ⚠ within organs, on part of the lines; also absent: MSLN, LINC00857, SLC38A5; co-absent with the target |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **-** arm (projection on the module's main direction -0.730). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.5, 0.9); signed map (22.7, -16.5). **Vector** length 96.6, 28.4% of its response variance represented; |z| ≥ 3 in 961 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +7.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.3 | +2.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.0 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +5.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -3.7 | -22.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -17.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -10.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.0 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.4 | -5.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -6.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.9 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | cancer susceptibility 9 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q21.13 — chr8:75,120,409-75,352,327 (-) |
| Ensembl biotype | lncRNA |
| Also known as | LINC00981, ESCCAL-1, linc-JPH1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48906) · Entrez [101805492](https://www.ncbi.nlm.nih.gov/gene/101805492) · Ensembl [ENSG00000249395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249395)

## Data

Gene col 14609: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14609); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14609, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14609]; `tensor/DDL_lfc|DDL_z.npy` [14609]; `embed/gene_vectors.npy` [14609]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14609 or target_col == 14609). Every well: [[CASC9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
