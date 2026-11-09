---
symbol: "ADAMTSL5"
type: "gene"
col: 11729
ensembl_id: "ENSG00000185761"
name: "ADAMTS like 5"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 3.32
n_lines_expressing: 45
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ADAMTSL5

*ADAMTS like 5* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.18× (z +6.7, q 1e-08, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.58× (z +5.8, q 1e-06, up in 15 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.404× (z -11.5, q 5e-28, down in 29 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[R3HDM4]] (+0.72, fdr 7e-06), [[MAPKAPK3]] (+0.65, fdr 1e-05), [[GPRIN1]] (+0.65, fdr 1e-05); moves opposite to [[NDUFC1]] (-0.71, fdr 7e-06), [[PUS10]] (-0.65, fdr 7e-06), [[ARID4B]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11729.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.18×** | +6.7 | 1e-08 | 4/4 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.2 | 2e-07 | 11/17 (NCI-H2030, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +5.8 | 1e-06 | 4/7 (A498, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +5.8 | 1e-06 | 15/41 (SW480, LS 180, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +5.0 | 7e-05 | 10/40 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +4.8 | 2e-04 | 14/42 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.55×** | +3.9 | 0.008 | 14/41 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | 1.42× | +3.1 | 0.14 | 5/37 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.1 | 0.14 | 4/42 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11729.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.404×** | -11.5 | 5e-28 | 29/33 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.397×** | -8.0 | 3e-13 | 19/32 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.592×** | -6.7 | 4e-09 | 19/36 (LoVo, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.574×** | -5.0 | 7e-05 | 17/38 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.579×** | -4.8 | 2e-04 | 11/40 (Panc 03.27, LoVo, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.614×** | -4.4 | 9e-04 | 14/42 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.619×** | -4.3 | 0.001 | 13/41 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.627×** | -4.2 | 0.002 | 13/33 (LoVo, A-172, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -4.1 | 0.003 | 14/30 (LS 180, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.649×** | -3.9 | 0.005 | 15/28 (LoVo, A498, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 9.29 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.126× (z -14.8) |
| [[SW480 (line)]] | alt | 3.85 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.134× (z -9.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -8.5) |
| [[A-172 (line)]] | wt | 7.52 | 0 | 1 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0742× (z -10.3) |
| [[HEC-1-A (line)]] | alt | 3.40 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.162× (z -9.2) |
| [[HS-578T (line)]] | alt | 5.61 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -8.8) |
| [[LS 180 (line)]] | wt | 3.62 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0795× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 7.73 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -10.3) |
| [[A-427 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.555 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.217 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.935 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM4]] | +0.72 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[MAPKAPK3]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[GPRIN1]] | +0.65 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[STK25]] | +0.64 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[EPPK1]] | +0.62 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[LRFN3]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[TMCO6]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ATP13A2]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[MICAL1]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[MAPK11]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[ARHGDIA]] | +0.59 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[CDK9]] | +0.59 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFC1]] | -0.71 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[PUS10]] | -0.65 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[ARID4B]] | -0.64 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[HOXA5]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ASH1L]] | -0.59 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[ZNF248]] | -0.59 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[PDHX]] | -0.59 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GTF2IRD2B]] | -0.58 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[FBXL15]] | -0.58 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PMS2P4-1]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PDSS2]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[NIFK-AS1]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ADAMTSL5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[DHRS3]] | B | DHRS3 activity lowers ADAMTSL5's level | lines that do not express DHRS3 (13) vs lines expressing it (37) | 1.51× higher at baseline in the lines without DHRS3 | 0.055 | ⚠ within organs, on part of the lines; also absent: CCDC9B, ENSG00000290729, STON2 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ADAMTSL5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ADAMTSL5's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SLC4A3]] | B | SLC4A3 activity raises ADAMTSL5's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without SLC4A3 | 0.097 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (15.9, -1.9); signed map (-8.4, 29.2). **Vector** length 56.8, 8.31% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.6 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.4 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -11.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -4.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -8.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.2 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.2 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | ADAMTS like 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:1,505,022-1,513,604 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously THSD6 |
| Gene groups (HGNC) | ADAMTS like |
| Reactome | 6 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMM2](https://www.uniprot.org/uniprotkb/Q6ZMM2) (ADAMTS-like protein 5):

> May play a role in modulation of fibrillin microfibrils in the extracellular matrix (ECM).

**Summary**, from NCBI Gene [339366](https://www.ncbi.nlm.nih.gov/gene/339366):

> Enables heparin binding activity and microfibril binding activity. Predicted to be involved in extracellular matrix organization. Located in microfibril. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27912](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27912) · Entrez [339366](https://www.ncbi.nlm.nih.gov/gene/339366) · UniProt [Q6ZMM2](https://www.uniprot.org/uniprotkb/Q6ZMM2) · Ensembl [ENSG00000185761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185761)

## Data

Gene col 11729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11729); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11729]; `tensor/DDL_lfc|DDL_z.npy` [11729]; `embed/gene_vectors.npy` [11729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11729 or target_col == 11729). Every well: [[ADAMTSL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADAMTSL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
