---
symbol: "RIMS2"
type: "gene"
col: 10714
ensembl_id: "ENSG00000176406"
name: "regulating synaptic membrane exocytosis 2"
location: "8q22.3"
module: 10
arm: "+"
pooled_cpm: 84.29
n_lines_expressing: 27
n_dd_up: 20
n_dd_down: 12
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# RIMS2

*regulating synaptic membrane exocytosis 2* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.09× (z +20.0, q 0e+00, up in 18 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.526× (z -8.1, q 4e-13, down in 23 of 25 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR2F1-AS1]] (+0.62, fdr 1e-05), [[LNC-LBCS]] (+0.59, fdr 1e-05), [[FGF14]] (+0.58, fdr 1e-05); moves opposite to [[ANAPC4]] (-0.52, fdr 2e-05), [[NBPF3]] (-0.52, fdr 2e-05), [[ANAPC5]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FAM184A]] → it (grade B ⚠); 13 go from it, the strongest it → [[PCDHA6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10714.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +20.0 | 0e+00 | 18/26 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.7 | 2e-24 | 17/25 (HOP62, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +9.3 | 3e-18 | 9/25 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +9.2 | 6e-18 | 10/25 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +8.2 | 2e-14 | 9/27 (SK-MEL-2, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.86×** | +7.8 | 7e-13 | 8/26 (SK-MEL-2, SW48, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +6.8 | 1e-09 | 9/25 (SHP-77, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +5.7 | 9e-07 | 9/25 (C32, PANC-1, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.11×** | +4.9 | 6e-05 | 8/25 (SK-MEL-2, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.10×** | +4.9 | 6e-05 | 8/26 (SK-MEL-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.7 | 1e-04 | 3/24 (RPMI-7951, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.0 | 0.003 | 8/26 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.4 | 0.025 | 0/23 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.042 | 12/25 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.042 | 10/26 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.044 | 8/26 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.28×** | +3.1 | 0.070 | 15/26 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +3.0 | 0.073 | 13/25 (SW 900, RPMI-7951, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10714.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.526×** | -8.1 | 4e-13 | 23/25 (BT-474, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.659×** | -5.2 | 5e-05 | 22/25 (BT-474, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.622×** | -5.1 | 8e-05 | 19/25 (BT-474, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.672×** | -5.0 | 9e-05 | 21/25 (BT-474, NCI-H23, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.714×** | -4.2 | 0.003 | 15/25 (A-172, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.731×** | -3.9 | 0.008 | 16/25 (SHP-77, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.703×** | -3.8 | 0.013 | 17/25 (BT-474, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.750×** | -3.6 | 0.021 | 22/25 (BT-474, J82, …) | all doses, flat | composition shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.754×** | -3.6 | 0.024 | 5/25 (NCI-H1792, LOX-IMVI, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.762×** | -3.4 | 0.035 | 17/25 (BT-474, SHP-77, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.764×** | -3.4 | 0.036 | 14/25 (BT-474, A-427, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.761×** | -3.3 | 0.044 | 4/25 (HOP62, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Dexamethasone (drug)]] 5 µM |  | 0.787× | -3.0 | 0.11 | 5/25 (NCI-H1792, RPMI-7951, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.844× | -3.0 | 0.11 | 13/25 (C32, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10714. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 460 | 0 | 14 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -18.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.134× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 452 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.211× (z -12.0) |
| [[J82 (line)]] | alt | 139 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.218× (z -9.9) |
| [[A-427 (line)]] | wt | 399 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -13.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -11.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -11.4) |
| [[SHP-77 (line)]] | alt | 970 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.171× (z -17.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +11.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0625× (z -13.8) ⚠ toxic; cell-cycle shift, explains ~91% of this change |
| [[SW480 (line)]] | alt | 122 | 0 | 4 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 53.3 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.40× (z +9.7) | — |
| [[LOX-IMVI (line)]] | wt | 178 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[C32 (line)]] | wt | 29.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +8.8) | — |
| [[H4 (line)]] | wt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -8.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0495× (z -11.9) |
| [[PANC-1 (line)]] | alt | 49.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.291× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RPMI-7951 (line)]] | alt | 30.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 34.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.6) | — |
| [[A-172 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.2 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 119 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.67 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.33 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 18.5 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.62 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.94 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.47 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 9.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 92.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.99 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.40 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.9 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10714), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR2F1-AS1]] | +0.62 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[LNC-LBCS]] | +0.59 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[FGF14]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[NOVA1]] | +0.57 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[ST8SIA6-AS1]] | +0.57 | +0.56 / +0.32 | both halves | 2e-04 |  |
| [[DLGAP4-AS1]] | +0.56 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[FLG-AS1]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[MIR2052HG]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[OR3A2]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[LGSN]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[CYP1B1-AS1]] | +0.54 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[NKAIN3]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANAPC4]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[NBPF3]] | -0.52 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[ANAPC5]] | -0.52 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[SLC35A1]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[IFT172]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[TSC2]] | -0.50 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[PRUNE1]] | -0.50 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[METTL17]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[KLHL8]] | -0.49 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[C12orf76]] | -0.47 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[RSAD1]] | -0.46 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[DPY30]] | -0.46 | -0.48 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM184A]] | B | FAM184A activity raises RIMS2's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 3.84× lower at baseline in the lines without FAM184A | 0.006 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers RIMS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NPAS3]] | B | NPAS3 activity raises RIMS2's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without NPAS3 | 0.084 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[ERC2]] | B | ERC2 activity raises RIMS2's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 3.74× lower at baseline in the lines without ERC2 | 0.089 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| [[MIR2052HG]] | C | MIR2052HG activity raises RIMS2's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 3.95× lower at baseline in the lines without MIR2052HG | 0.002 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent; co-absent with the target |
| [[MGAT4C]] | C | MGAT4C activity raises RIMS2's level | lines that do not express MGAT4C (35) vs lines expressing it (15) | 4.29× lower at baseline in the lines without MGAT4C | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000281566, LINC01205, ENSG00000286385; co-absent with the target |
| [[GARIN1B]] | C | GARIN1B activity lowers RIMS2's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.57× higher at baseline in the lines without GARIN1B | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |
| [[JPH3]] | C | JPH3 activity raises RIMS2's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 4.81× lower at baseline in the lines without JPH3 | 0.069 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 8, C 5. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDHA6]] | B | RIMS2 activity raises PCDHA6's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.00× lower at baseline in the lines without RIMS2 | 0.012 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[DRAIC]] | B | RIMS2 activity raises DRAIC's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without RIMS2 | 0.013 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[FNBP1P1]] | B | RIMS2 activity raises FNBP1P1's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.30× lower at baseline in the lines without RIMS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[ERC2]] | B | RIMS2 activity raises ERC2's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.33× lower at baseline in the lines without RIMS2 | 0.042 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[GRK4]] | B | RIMS2 activity raises GRK4's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.26× lower at baseline in the lines without RIMS2 | 0.048 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[FAM184A]] | B | RIMS2 activity raises FAM184A's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without RIMS2 | 0.056 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[HIVEP2-DT]] | B | RIMS2 activity raises HIVEP2-DT's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without RIMS2 | 0.057 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[CTBP1-DT]] | B | RIMS2 activity raises CTBP1-DT's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.20× lower at baseline in the lines without RIMS2 | 0.073 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[FLG-AS1]] | C | RIMS2 activity raises FLG-AS1's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 3.67× lower at baseline in the lines without RIMS2 | 0.015 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3; co-absent with the target |
| [[DOCK3]] | C | RIMS2 activity raises DOCK3's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.38× lower at baseline in the lines without RIMS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3; co-absent with the target |
| [[MIR2052HG]] | C | RIMS2 activity raises MIR2052HG's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 3.10× lower at baseline in the lines without RIMS2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3; co-absent with the target |
| [[JPH3]] | C | RIMS2 activity raises JPH3's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 2.69× lower at baseline in the lines without RIMS2 | 0.040 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.494). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (30.4, 24.8); signed map (53.2, 20.0). **Vector** length 89.8, 28.7% of its response variance represented; |z| ≥ 3 in 717 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +20.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.1 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +10.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.7 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.9 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -5.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -8.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.7 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -2.5 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.0 | -3.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | regulating synaptic membrane exocytosis 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:103,500,610-104,254,430 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0751, RIM2, OBOE; previously RAB3IP3 |
| Gene groups (HGNC) | Regulating synaptic membrane exocytosis family; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ26](https://www.uniprot.org/uniprotkb/Q9UQ26) (Regulating synaptic membrane exocytosis protein 2):

> Rab effector involved in exocytosis. May act as scaffold protein. Plays a role in dendrite formation by melanocytes.

**Summary**, from NCBI Gene [9699](https://www.ncbi.nlm.nih.gov/gene/9699):

> The protein encoded by this gene is a presynaptic protein that interacts with RAB3, a protein important for normal neurotransmitter release. The encoded protein can also bind several other synaptic proteins, including UNC-13 homolog B, ELKS/Rab6-interacting/CAST family member 1, and synaptotagmin 1. This protein is involved in synaptic membrane exocytosis. Polymorphisms in this gene have been associated with degenerative lumbar scoliosis. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:17283](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17283) · Entrez [9699](https://www.ncbi.nlm.nih.gov/gene/9699) · UniProt [Q9UQ26](https://www.uniprot.org/uniprotkb/Q9UQ26) · Ensembl [ENSG00000176406](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176406)

## Data

Gene col 10714: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10714); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10714, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10714]; `tensor/DDL_lfc|DDL_z.npy` [10714]; `embed/gene_vectors.npy` [10714]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10714 or target_col == 10714). Every well: [[RIMS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RIMS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
