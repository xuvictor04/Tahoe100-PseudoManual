---
symbol: "GNL2"
type: "gene"
col: 5590
ensembl_id: "ENSG00000134697"
name: "G protein nucleolar 2"
location: "1p34.3"
module: 52
arm: "+"
pooled_cpm: 106.34
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 7
n_dd_up_clean: 15
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# GNL2

*G protein nucleolar 2* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.91× (z +9.4, q 3e-18, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 0.732× (z -4.6, q 0.003, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL3]] (+0.73, fdr 7e-06), [[UTP6]] (+0.72, fdr 7e-06), [[NANS]] (+0.71, fdr 7e-06); moves opposite to [[SCYL3]] (-0.54, fdr 3e-05), [[MED21]] (-0.52, fdr 4e-05), [[SUMO2]] (-0.51, fdr 6e-05).
> It sits in the **+** arm of [[Module 052]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5590.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.91×** | +9.4 | 3e-18 | 43/48 (NCI-H1792, HT-29, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.47×** | +7.9 | 6e-13 | 32/48 (SNU-423, NCI-H460, …) | two highest doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.9 | 9e-07 | 39/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.52×** | +5.8 | 9e-07 | 36/48 (NCI-H1573, NCI-H1792, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.01×** | +5.3 | 1e-05 | 39/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +4.7 | 3e-04 | 29/48 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **1.23×** | +4.3 | 0.001 | 34/49 (MIA PaCa-2, SW 900, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.36×** | +4.2 | 0.002 | 30/47 (NCI-H23, LOX-IMVI, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.32×** | +4.0 | 0.004 | 30/48 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.32×** | +4.0 | 0.004 | 24/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.31×** | +3.9 | 0.005 | 27/48 (SNU-423, C32, …) | rises with dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.006 | 35/48 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.007 | 37/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.30×** | +3.8 | 0.007 | 27/48 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.30×** | +3.7 | 0.007 | 30/48 (C32, HEC-1-A, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.030 | 25/48 (AN3 CA, SNU-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.031 | 25/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.031 | 26/48 (Panc 03.27, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.031 | 29/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.033 | 26/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.041 | 20/48 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.041 | 21/48 (RKO, LoVo, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.054 | 23/49 (MIA PaCa-2, NCI-H460, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.054 | 20/48 (SW 900, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5590.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.732×** | -4.6 | 0.003 | 31/48 (RKO, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.733×** | -4.3 | 0.004 | 34/47 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.823×** | -4.0 | 0.014 | 23/48 (COLO 205, CHP-212, …) | all doses, flat |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.769×** | -3.8 | 0.018 | 35/48 (SW1417, J82, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.780×** | -3.6 | 0.033 | 24/47 (C-33 A, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | 0.846× | -3.5 | 0.052 | 25/48 (LoVo, SHP-77, …) | top dose only | low cells (technical?) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.795×** | -3.4 | 0.064 | 25/48 (SW 1088, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.785×** | -3.3 | 0.075 | 23/48 (LoVo, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5590. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 85.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.55× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 82.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 134 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.85× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 87.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.25× (z +11.7) | — |
| [[NCI-H460 (line)]] | wt | 61.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.6) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.86× (z +9.3) | — |
| [[NCI-H596 (line)]] | alt | 93.0 | 1 | 1 (1 ⚠) | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 2.92× (z +8.5) | [[Trametinib (drug)]] 5 µM 0.316× (z -9.4) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SNU-423 (line)]] | alt | 77.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.3) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +8.9) | — |
| [[A-172 (line)]] | wt | 49.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.6) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[AsPC-1 (line)]] | alt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 79.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.304× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 84.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.64× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 72.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.4) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[HOP62 (line)]] | alt | 91.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.91× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +10.2) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[LoVo (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +9.2) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 124 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 2.36× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 75.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.36× (z +12.0) | — |
| [[NCI-H23 (line)]] | alt | 146 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 139 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.73× (z +10.7) | — |
| [[SNU-1 (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 1088 (line)]] | alt | 134 | 0 | 1 | — | [[Finasteride (drug)]] 5 µM 0.0864× (z -9.5) |
| [[SW48 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 180 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 91.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 136 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 90.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 68.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 178 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 145 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 91.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5590), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL3]] | +0.73 | +0.73 / +0.70 | both halves | 7e-06 | STRING 997 |
| [[UTP6]] | +0.72 | +0.76 / +0.61 | both halves | 7e-06 | STRING 931 |
| [[NANS]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[PMM2]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[POLR3D]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[DIS3]] | +0.68 | +0.76 / +0.53 | both halves | 1e-05 | STRING 472 |
| [[SPTY2D1]] | +0.66 | +0.76 / +0.49 | both halves | 1e-05 |  |
| [[ARF4]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[SCFD1]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[DDX18]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 | STRING 975 |
| [[SCFD2]] | +0.64 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[RRP12]] | +0.63 | +0.66 / +0.66 | both halves | 7e-06 | STRING 917 |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCYL3]] | -0.54 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[MED21]] | -0.52 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[SUMO2]] | -0.51 | -0.53 / -0.38 | both halves | 6e-05 | STRING 562 |
| [[SPPL3]] | -0.51 | -0.52 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.574). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (8.6, -32.7); signed map (-52.9, 14.0). **Vector** length 107, 36.2% of its response variance represented; |z| ≥ 3 in 974 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +9.4 |
|  | [[EX229 (drug)]] 0.05 µM |  | +2.7 | +3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.6 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.7 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -5.5 | +4.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | -4.9 | -3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.2 | -4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -2.9 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein nucleolar 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,566,816-37,595,937 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Ngp-1, HUMAUANTIG, Nog2, Nug2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13823](https://www.uniprot.org/uniprotkb/Q13823) (Nucleolar GTP-binding protein 2):

> GTPase that associates with pre-60S ribosomal subunits in the nucleolus and is required for their nuclear export and maturation. May promote cell proliferation possibly by increasing p53/TP53 protein levels, and consequently those of its downstream product CDKN1A/p21, and decreasing RPL23A protein levels.

**Summary**, from NCBI Gene [29889](https://www.ncbi.nlm.nih.gov/gene/29889):

> Enables RNA binding activity. Predicted to be involved in ribosome biogenesis. Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29925) · Entrez [29889](https://www.ncbi.nlm.nih.gov/gene/29889) · UniProt [Q13823](https://www.uniprot.org/uniprotkb/Q13823) · Ensembl [ENSG00000134697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134697)

## Data

Gene col 5590: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5590); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5590, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5590]; `tensor/DDL_lfc|DDL_z.npy` [5590]; `embed/gene_vectors.npy` [5590]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5590 or target_col == 5590). Every well: [[GNL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
