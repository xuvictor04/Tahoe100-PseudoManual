---
symbol: "EMC2"
type: "gene"
col: 2456
ensembl_id: "ENSG00000104412"
name: "ER membrane protein complex subunit 2"
location: "8q23.1"
module: 24
arm: "+"
pooled_cpm: 68.04
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# EMC2

*ER membrane protein complex subunit 2* — 8q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.24× (z +4.2, q 0.013, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.391× (z -9.3, q 5e-18, down in 44 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP36]] (+0.72, fdr 7e-06), [[GOLPH3L]] (+0.63, fdr 1e-05), [[RBIS]] (+0.62, fdr 2e-05); moves opposite to [[MAPRE1]] (-0.67, fdr 7e-06), [[CCND1]] (-0.62, fdr 1e-05), [[KPNA4]] (-0.60, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLXNA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.24×** | +4.2 | 0.013 | 23/48 (NCI-H2030, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.032 | 19/48 (C32, SW480, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.032 | 18/49 (C32, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.096 | 13/48 (AsPC-1, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +3.3 | 0.096 | 17/48 (HOP62, J82, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.3 | 0.096 | 14/48 (NCI-H23, BT-474, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.13 | 20/47 (LoVo, HEC-1-A, …) | rises with dose |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | 1.12× | +3.1 | 0.13 | 8/48 (SW 900, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.391×** | -9.3 | 5e-18 | 44/49 (Panc 03.27, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.513×** | -6.6 | 9e-09 | 37/48 (Panc 03.27, C32, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.723×** | -6.2 | 1e-07 | 32/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **0.774×** | -4.9 | 2e-04 | 27/48 (SW480, SHP-77, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.836× | -4.8 | 2e-04 | 23/48 (Panc 03.27, HS-578T, …) | top dose only | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.795×** | -4.3 | 0.001 | 26/48 (SW480, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.859× | -4.0 | 0.004 | 20/48 (HS-578T, A498, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.814×** | -3.9 | 0.007 | 25/48 (SW 1271, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.833×** | -3.4 | 0.036 | 20/48 (SW480, AsPC-1, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.842× | -3.2 | 0.067 | 16/48 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.727×** | -3.2 | 0.081 | 15/49 (CHP-212, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | 0.848× | -3.1 | 0.089 | 20/48 (SW480, KATO III, …) | rises with dose | composition shift |
| [[Edoxaban (tosylate monohydrate) (drug)]] 5 µM | ⚠ unreliable plate only | 0.850× | -3.1 | 0.091 | 15/49 (A498, AsPC-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.954× | -3.1 | 0.091 | 1/49 (SW 1088) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Panc 03.27 (line)]] | alt | 80.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -13.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.156× (z -10.8) |
| [[SHP-77 (line)]] | alt | 82.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.386× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.442× (z -8.9) |
| [[SW480 (line)]] | alt | 44.4 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.321× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.402× (z -10.7) |
| [[KATO III (line)]] | alt | 87.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.359× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change |
| [[A-427 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 56.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 82.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -8.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 69.0 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.176× (z -9.1) ⚠ toxic |
| [[C32 (line)]] | wt | 73.1 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.188× (z -9.1) |
| [[HOP62 (line)]] | alt | 68.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.596× (z -8.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 114 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.566× (z -9.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[hTERT-HPNE (line)]] | wt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.316× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[NCI-H460 (line)]] | wt | 55.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -12.2) ⚠ cell-cycle shift, explains ~6% of this change |
| [[PANC-1 (line)]] | alt | 66.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[RKO (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RPMI-7951 (line)]] | alt | 73.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.360× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW 900 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A-172 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 73.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 64.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP36]] | +0.72 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[GOLPH3L]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[RBIS]] | +0.62 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ATP5MC2]] | +0.62 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[MED10]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CCS]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[TMEM126A]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TULP3]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[LAMTOR5]] | +0.60 | +0.46 / +0.63 | both halves | 3e-05 |  |
| [[RPAIN]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[EPB41L4A-AS1]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[MTIF3]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.67 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[CCND1]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.60 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[DDAH1]] | -0.59 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[FGD5-AS1]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[HNRNPAB]] | -0.56 | -0.47 / -0.55 | both halves | 2e-05 |  |
| [[SLFNL1-AS1]] | -0.56 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.54 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[PURB]] | -0.54 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[CTPS1]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[THOC6]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[MAP4K4]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | B | PLXNA2 activity raises EMC2's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.34× lower at baseline in the lines without PLXNA2 | 0.022 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-37.0, -20.6); signed map (-50.9, 18.1). **Vector** length 117, 30.8% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +1.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +1.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.6 | +3.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.6 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.5 | +2.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.6 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.3 | -4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -6.0 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.1 — chr8:108,443,601-108,489,196 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0103, TTC35 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; ER membrane protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15006](https://www.uniprot.org/uniprotkb/Q15006) (ER membrane protein complex subunit 2):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [9694](https://www.ncbi.nlm.nih.gov/gene/9694):

> Contributes to membrane insertase activity. Involved in protein insertion into ER membrane by stop-transfer membrane-anchor sequence and tail-anchored membrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane. Is extrinsic component of endoplasmic reticulum membrane. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28963](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28963) · Entrez [9694](https://www.ncbi.nlm.nih.gov/gene/9694) · UniProt [Q15006](https://www.uniprot.org/uniprotkb/Q15006) · Ensembl [ENSG00000104412](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104412)

## Data

Gene col 2456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2456); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2456]; `tensor/DDL_lfc|DDL_z.npy` [2456]; `embed/gene_vectors.npy` [2456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2456 or target_col == 2456). Every well: [[EMC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
