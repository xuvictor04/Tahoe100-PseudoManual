---
symbol: "CDS2"
type: "gene"
col: 2109
ensembl_id: "ENSG00000101290"
name: "CDP-diacylglycerol synthase 2"
location: "20p12.3"
module: 168
arm: "+"
pooled_cpm: 52.43
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/168"]
generated_by: "tahoemap"
---

# CDS2

*CDP-diacylglycerol synthase 2* — 20p12.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.404× (z -20.5, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SDHAP4]] (+0.75, fdr 7e-06), [[NTAN1]] (+0.75, fdr 7e-06), [[ADD1]] (+0.70, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.65, fdr 1e-05), [[R3HDM2]] (-0.62, fdr 3e-05), [[PPP1R10]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 168]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.27× | +3.7 | 0.13 | 22/47 (LoVo, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | 1.50× | +3.4 | 0.18 | 21/48 (NCI-H1573, A549, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.23× | +3.3 | 0.18 | 17/47 (RPMI-7951, RKO, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.404×** | -20.5 | 0e+00 | 44/48 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.489×** | -11.4 | 1e-27 | 40/48 (NCI-H1573, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.523×** | -9.9 | 5e-21 | 40/48 (A-172, SNU-423, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.607×** | -8.0 | 2e-13 | 40/48 (HOP62, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.735×** | -4.9 | 1e-04 | 31/49 (LOX-IMVI, SNU-423, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.739×** | -4.8 | 1e-04 | 29/48 (A-172, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.742×** | -4.6 | 4e-04 | 26/47 (CFPAC-1, A-172, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.747×** | -4.3 | 0.001 | 22/45 (A549, NCI-H23, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.790×** | -3.7 | 0.011 | 23/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -3.7 | 0.012 | 19/48 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | 0.818× | -3.1 | 0.11 | 19/39 (LS 180, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Thymol (drug)]] 5 µM |  | 0.874× | -3.0 | 0.11 | 11/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.695× | -3.0 | 0.11 | 16/48 (MIA PaCa-2, A549, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 85.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -25.5) |
| [[A-172 (line)]] | wt | 75.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -24.6) |
| [[CFPAC-1 (line)]] | alt | 67.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -20.4) |
| [[HEC-1-A (line)]] | alt | 72.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.407× (z -14.6) |
| [[HS-578T (line)]] | alt | 61.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -18.3) |
| [[J82 (line)]] | alt | 48.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 28.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.168× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 36.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -20.6) |
| [[NCI-H2347 (line)]] | alt | 60.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -15.5) |
| [[PANC-1 (line)]] | alt | 38.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.9) |
| [[A498 (line)]] | wt | 26.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.5) |
| [[A549 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.525× (z -9.9) |
| [[C32 (line)]] | wt | 52.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.3) |
| [[COLO 205 (line)]] | alt | 48.6 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.145× (z -13.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 64.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -17.4) |
| [[MIA PaCa-2 (line)]] | alt | 61.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -18.7) |
| [[NCI-H23 (line)]] | alt | 32.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 50.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 75.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -13.6) |
| [[SNU-423 (line)]] | alt | 80.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -24.2) |
| [[SW 900 (line)]] | alt | 50.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.9) |
| [[AsPC-1 (line)]] | alt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.4) |
| [[BT-474 (line)]] | alt | 45.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -10.9) |
| [[H4 (line)]] | wt | 47.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -11.5) |
| [[HCT15 (line)]] | alt | 58.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -8.9) |
| [[Hs 766T (line)]] | wt | 64.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.1) |
| [[HT-29 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 44.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -13.7) |
| [[LS 180 (line)]] | wt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.306× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H661 (line)]] | alt | 46.3 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0610× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 40.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.6) |
| [[A-427 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 57.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 65.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SDHAP4]] | +0.75 | +0.82 / +0.60 | both halves | 7e-06 |  |
| [[NTAN1]] | +0.75 | +0.80 / +0.64 | both halves | 7e-06 |  |
| [[ADD1]] | +0.70 | +0.81 / +0.67 | both halves | 7e-06 |  |
| [[GET1]] | +0.70 | +0.78 / +0.57 | both halves | 9e-06 |  |
| [[SEC11A]] | +0.69 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.69 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[DHRS1]] | +0.67 | +0.74 / +0.50 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.66 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[NAP1L4]] | +0.65 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.65 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[AKTIP]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.65 | -0.76 / -0.49 | both halves | 1e-05 |  |
| [[R3HDM2]] | -0.62 | -0.73 / -0.44 | both halves | 3e-05 |  |
| [[PPP1R10]] | -0.61 | -0.66 / -0.50 | both halves | 1e-05 |  |
| [[TRIP11]] | -0.60 | -0.69 / -0.45 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | -0.60 | -0.72 / -0.42 | both halves | 4e-05 |  |
| [[RBBP6]] | -0.60 | -0.72 / -0.45 | both halves | 3e-05 |  |
| [[ST7L]] | -0.59 | -0.73 / -0.38 | both halves | 6e-05 |  |
| [[RBM23]] | -0.59 | -0.65 / -0.42 | both halves | 4e-05 |  |
| [[ZBTB38]] | -0.58 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[RPL7L1]] | -0.58 | -0.72 / -0.44 | both halves | 3e-05 |  |
| [[ATXN7L1]] | -0.58 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[USP16]] | -0.58 | -0.63 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises CDS2's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without KATNAL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 168]]; 25 genes; this gene is in the **+** arm (projection on the module's main direction 0.760). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (1.3, -8.8); signed map (-38.0, -10.1). **Vector** length 96.6, 24.4% of its response variance represented; |z| ≥ 3 in 804 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +2.9 | -3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.9 | -20.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.6 | -11.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.9 | -9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -8.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.5 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.7 |
|  | [[Thymol (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.9 | -3.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CDP-diacylglycerol synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.3 — chr20:5,126,879-5,197,887 (+) |
| Ensembl biotype | protein_coding |
| Reactome | 4 pathways, smallest: Synthesis of PG; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O95674](https://www.uniprot.org/uniprotkb/O95674) (Phosphatidate cytidylyltransferase 2):

> Catalyzes the conversion of phosphatidic acid (PA) to CDP-diacylglycerol (CDP-DAG), an essential intermediate in the synthesis of phosphatidylglycerol, cardiolipin and phosphatidylinositol. Exhibits specificity for the nature of the acyl chains at the sn-1 and sn-2 positions in the substrate, PA and the preferred acyl chain composition is 1-stearoyl-2-arachidonoyl-sn-phosphatidic acid. Plays an important role in regulating the growth and maturation of lipid droplets which are storage organelles …

**Summary**, from NCBI Gene [8760](https://www.ncbi.nlm.nih.gov/gene/8760):

> Breakdown products of phosphoinositides are ubiquitous second messengers that function downstream of many G protein-coupled receptors and tyrosine kinases regulating cell growth, calcium metabolism, and protein kinase C activity. This gene encodes an enzyme which regulates the amount of phosphatidylinositol available for signaling by catalyzing the conversion of phosphatidic acid to CDP-diacylglycerol. This enzyme is an integral membrane protein localized to two subcellular domains, the matrix …

**Accessions** — [HGNC:1801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1801) · Entrez [8760](https://www.ncbi.nlm.nih.gov/gene/8760) · UniProt [O95674](https://www.uniprot.org/uniprotkb/O95674) · Ensembl [ENSG00000101290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101290)

## Data

Gene col 2109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2109); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2109]; `tensor/DDL_lfc|DDL_z.npy` [2109]; `embed/gene_vectors.npy` [2109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2109 or target_col == 2109). Every well: [[CDS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
