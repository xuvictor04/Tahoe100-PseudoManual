---
symbol: "PELP1"
type: "gene"
col: 6525
ensembl_id: "ENSG00000141456"
name: "proline, glutamate and leucine rich protein 1"
location: "17p13.2"
module: 129
arm: "+"
pooled_cpm: 54.47
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# PELP1

*proline, glutamate and leucine rich protein 1* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.60× (z +7.6, q 2e-11, up in 39 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.96× (z +5.7, q 1e-06, up in 29 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.0968×, A-427 0.387×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.327×; ⚠ cell-cycle shift, explains ~98% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0659×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX55]] (+0.75, fdr 7e-06), [[ZSWIM9]] (+0.70, fdr 1e-05), [[DHX57]] (+0.63, fdr 2e-05); moves opposite to [[SDCBP]] (-0.60, fdr 1e-05), [[LEPROT]] (-0.58, fdr 2e-05), [[PRDM2]] (-0.53, fdr 5e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[OSBPL7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6525.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.60×** | +7.6 | 2e-11 | 39/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.59×** | +7.5 | 2e-11 | 43/48 (BT-474, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.58×** | +7.4 | 2e-11 | 40/48 (SHP-77, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.57×** | +7.3 | 6e-11 | 42/48 (SHP-77, BT-474, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +6.1 | 1e-07 | 38/48 (AsPC-1, LoVo, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.43×** | +5.7 | 9e-07 | 34/47 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +5.7 | 1e-06 | 29/48 (RKO, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +5.5 | 3e-06 | 26/49 (SHP-77, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.38×** | +5.2 | 1e-05 | 31/48 (SW480, PANC-1, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change | **1.34×** | +4.7 | 2e-04 | 23/48 (NCI-H23, SNU-423, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | 1.19× | +4.0 | 0.003 | 20/48 (LS 180, A549, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.004 | 22/48 (KATO III, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.9 | 0.004 | 21/48 (LOX-IMVI, A549, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 23/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.27×** | +3.9 | 0.004 | 22/48 (PANC-1, SW48, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.006 | 19/48 (KATO III, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.019 | 18/48 (LoVo, MIA PaCa-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.020 | 18/48 (C32, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.042 | 13/48 (HT-29, SNU-423, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.057 | 10/48 (SNU-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.061 | 6/48 (SW48, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +3.0 | 0.061 | 10/48 (KATO III, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.35×** | +2.9 | 0.067 | 13/48 (PANC-1, NCI-H460, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.41×** | +2.9 | 0.078 | 11/45 (NCI-H460, HCT15, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6525.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.0968×, A-427 0.387×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.327×; ⚠ cell-cycle shift, explains ~98% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (H4 0.0659×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.802× | -3.6 | 0.12 | 20/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.804× | -3.5 | 0.12 | 13/48 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.811× | -3.1 | 0.33 | 13/48 (SW480, SW1417, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6525. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 86.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0968× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 72.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.387× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 82.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.256× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0659× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LS 180 (line)]] | wt | 35.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.7) ⚠ cell-cycle shift, explains ~98% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 74.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.8) ⚠ cell-cycle shift, explains ~98% of this change |
| [[PANC-1 (line)]] | alt | 48.4 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.19× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[A-172 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 86.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 75.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 76.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 86.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 76.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6525), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX55]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[ZSWIM9]] | +0.70 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[DHX57]] | +0.63 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[SNRNP70]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.63 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PHRF1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PRPF6]] | +0.61 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[WRAP73]] | +0.60 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[KRI1]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[E4F1]] | +0.59 | +0.56 / +0.43 | both halves | 4e-05 |  |
| [[CDK5RAP1]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[VPS37C]] | +0.58 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDCBP]] | -0.60 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[LEPROT]] | -0.58 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[PRDM2]] | -0.53 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[UBE2A]] | -0.53 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[NXT2]] | -0.53 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[FGD5-AS1]] | -0.52 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[TWF1]] | -0.52 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.51 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.50 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[CTNNA1]] | -0.50 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CD164]] | -0.50 | -0.32 / -0.58 | both halves | 2e-04 |  |
| [[ARMT1]] | -0.49 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL7]] | B | OSBPL7 activity lowers PELP1's level | lines that do not express OSBPL7 (7) vs lines expressing it (43) | 1.47× higher at baseline in the lines without OSBPL7 | 0.093 | ⚠ within organs, on part of the lines; also absent: TBXAS1, PYROXD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.567). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.8, -8.5); signed map (-17.0, -13.2). **Vector** length 92.3, 24.1% of its response variance represented; |z| ≥ 3 in 703 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +4.1 | +7.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.8 | +7.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +6.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.2 | +3.4 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +2.7 | +3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.6 | +2.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.8 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.3 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | +0.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.3 | -2.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | proline, glutamate and leucine rich protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:4,669,774-4,704,337 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MNAR |
| Gene groups (HGNC) | Large ribosomal subunit biogenesis complex; Armadillo like helical domain containing |
| Reactome | 7 pathways, smallest: PTK6 Expression; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZL8](https://www.uniprot.org/uniprotkb/Q8IZL8) (Proline-, glutamic acid- and leucine-rich protein 1):

> Coactivator of estrogen receptor-mediated transcription and a corepressor of other nuclear hormone receptors and sequence-specific transcription factors. Plays a role in estrogen receptor (ER) genomic activity when present in the nuclear compartment by activating the ER target genes in a hormonal stimulation dependent manner. Can facilitate ER non-genomic signaling via SRC and PI3K interaction in the cytosol. Plays a role in E2-mediated cell cycle progression by interacting with RB1. May have …

**Summary**, from NCBI Gene [27043](https://www.ncbi.nlm.nih.gov/gene/27043):

> This gene encodes a transcription factor which coactivates transcription of estrogen receptor responsive genes and corepresses genes activated by other hormone receptors or sequence-specific transcription factors. Expression of this gene is regulated by both members of the estrogen receptor family. This gene may be involved in the progression of several types of cancer. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:30134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30134) · Entrez [27043](https://www.ncbi.nlm.nih.gov/gene/27043) · UniProt [Q8IZL8](https://www.uniprot.org/uniprotkb/Q8IZL8) · Ensembl [ENSG00000141456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141456)

## Data

Gene col 6525: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6525); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6525, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6525]; `tensor/DDL_lfc|DDL_z.npy` [6525]; `embed/gene_vectors.npy` [6525]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6525 or target_col == 6525). Every well: [[PELP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PELP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
