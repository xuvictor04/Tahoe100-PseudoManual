---
symbol: "TFAP4"
type: "gene"
col: 1623
ensembl_id: "ENSG00000090447"
name: "transcription factor AP-4"
location: "16p13.3"
module: 1
arm: "+"
pooled_cpm: 9.91
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TFAP4

*transcription factor AP-4* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.64× (z +6.4, q 6e-08, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.548× (z -7.8, q 3e-12, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EMSLR]] (+0.61, fdr 7e-06), [[TSNARE1]] (+0.61, fdr 7e-06), [[NUDT19]] (+0.58, fdr 1e-05); moves opposite to [[MAGT1]] (-0.60, fdr 1e-05), [[CDKL5]] (-0.53, fdr 3e-05), [[NUMB]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LRP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +6.4 | 6e-08 | 24/47 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +6.3 | 6e-08 | 22/42 (PANC-1, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.39×** | +6.0 | 3e-07 | 21/46 (PANC-1, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.4 | 1e-05 | 6/15 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.3 | 1e-05 | 17/35 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +5.3 | 1e-05 | 16/37 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +5.0 | 4e-05 | 19/46 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.7 | 2e-04 | 15/37 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 20/46 (SW480, HEC-1-A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +4.4 | 5e-04 | 15/46 (NCI-H1792, LS 180, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.0 | 0.003 | 13/38 (HCT15, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.021 | 6/47 (A-172, RPMI-7951, …) | top dose only | position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.046 | 7/46 (SK-MEL-2, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1623.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.548×** | -7.8 | 3e-12 | 26/47 (SW48, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.555×** | -7.7 | 6e-12 | 27/46 (C-33 A, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.603×** | -6.3 | 5e-08 | 24/44 (SNU-1, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.617×** | -6.3 | 5e-08 | 24/45 (SW48, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.668×** | -5.0 | 5e-05 | 17/46 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -4.5 | 6e-04 | 17/44 (MIA PaCa-2, SNU-423, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.713×** | -4.4 | 9e-04 | 17/46 (NCI-H1792, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.726×** | -4.2 | 0.002 | 19/47 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.727×** | -4.1 | 0.002 | 17/47 (SW480, C-33 A, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.744×** | -3.8 | 0.007 | 12/47 (H4, C32, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.752×** | -3.7 | 0.012 | 18/47 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.675×** | -3.6 | 0.013 | 8/47 (PANC-1, MIA PaCa-2, …) | two highest doses | noisy plate (z scaled) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.031 | 4/48 (NCI-H23, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.767×** | -3.2 | 0.047 | 12/47 (NCI-H23, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Cilostazol (drug)]] 5 µM |  | **0.785×** | -3.0 | 0.096 | 4/46 (NCI-H1573, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 18.0 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0714× (z -23.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 14.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.149× (z -9.4) |
| [[A-172 (line)]] | wt | 5.30 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.119× (z -8.5) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 6.23 | 0 | 1 | — | [[Flutamide (drug)]] 0.5 µM 0.0857× (z -9.2) |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0628× (z -11.7) |
| [[C32 (line)]] | wt | 9.56 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0262× (z -15.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 19.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -9.9) |
| [[HOP62 (line)]] | alt | 4.46 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +11.6) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[Hs 766T (line)]] | wt | 8.38 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.22× (z +12.1) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[NCI-H460 (line)]] | wt | 8.17 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.9) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[SNU-1 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0681× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 18.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -8.8) |
| [[SW48 (line)]] | wt | 33.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -9.1) |
| [[SW480 (line)]] | alt | 16.3 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -8.5) |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMSLR]] | +0.61 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TSNARE1]] | +0.61 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[NUDT19]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[TTC39C]] | +0.57 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[PATZ1]] | +0.56 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[DDX31]] | +0.56 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[DNAAF2]] | +0.55 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TGFBRAP1]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[DIS3L]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[ACVR2B]] | +0.54 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[EXOSC5]] | +0.54 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[DDX54]] | +0.54 | +0.49 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGT1]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[CDKL5]] | -0.53 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[NUMB]] | -0.50 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[STX12]] | -0.49 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[MYL6]] | -0.48 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[PDLIM5]] | -0.47 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[SYNJ1]] | -0.46 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[TPMT]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRP3]] | B | LRP3 activity raises TFAP4's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.43× lower at baseline in the lines without LRP3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[LTBR]] | B | LTBR activity lowers TFAP4's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.33× higher at baseline in the lines without LTBR | 0.074 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[PPARGC1B]] | C | PPARGC1B activity raises TFAP4's level | lines that do not express PPARGC1B (3) vs lines expressing it (47) | 2.02× lower at baseline in the lines without PPARGC1B | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC4A7, SPDL1, ARHGAP10; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.1, -44.7); signed map (4.2, -39.8). **Vector** length 91.7, 18.5% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.5 | +6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.3 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +6.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.7 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.3 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -3.6 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor AP-4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:4,257,186-4,273,075 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AP-4, bHLHc41 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01664](https://www.uniprot.org/uniprotkb/Q01664) (Transcription factor AP-4):

> Transcription factor that activates both viral and cellular genes by binding to the symmetrical DNA sequence 5'-CAGCTG-3'.

**Summary**, from NCBI Gene [7023](https://www.ncbi.nlm.nih.gov/gene/7023):

> Transcription factors of the basic helix-loop-helix-zipper (bHLH-ZIP) family contain a basic domain, which is used for DNA binding, and HLH and ZIP domains, which are used for oligomerization. Transcription factor AP4 activates both viral and cellular genes by binding to the symmetrical DNA sequence CAGCTG (Mermod et al., 1988 [PubMed 2833704]; Hu et al., 1990 [PubMed 2123466]).[supplied by OMIM, Jul 2009]

**Accessions** — [HGNC:11745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11745) · Entrez [7023](https://www.ncbi.nlm.nih.gov/gene/7023) · UniProt [Q01664](https://www.uniprot.org/uniprotkb/Q01664) · Ensembl [ENSG00000090447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090447)

## Data

Gene col 1623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1623); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1623]; `tensor/DDL_lfc|DDL_z.npy` [1623]; `embed/gene_vectors.npy` [1623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1623 or target_col == 1623). Every well: [[TFAP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TFAP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
