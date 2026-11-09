---
symbol: "KHDC1-AS1"
type: "gene"
col: 13718
ensembl_id: "ENSG00000229852"
name: "KHDC1 antisense RNA 1"
location: "6q13"
module: 4
arm: "+"
pooled_cpm: 7.51
n_lines_expressing: 37
n_dd_up: 4
n_dd_down: 22
n_dd_up_clean: 2
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 9
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# KHDC1-AS1

*KHDC1 antisense RNA 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.48× (z +4.6, q 0.002, up in 11 of 27 measured lines) ⚠ toxic; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.23× (z +3.6, q 0.063, up in 8 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.407× (z -15.5, q 0e+00, down in 24 of 30 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.373× (z -12.0, q 1e-30, down in 30 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP6]] (+0.60, fdr 1e-05), [[CHST10]] (+0.59, fdr 1e-05), [[PSTK]] (+0.55, fdr 2e-05); moves opposite to [[RORC]] (-0.49, fdr 8e-05), [[ZNF703]] (-0.47, fdr 8e-05), [[SLC50A1]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[ADAMTS10]] → it (grade B ⚠); 9 go from it, the strongest it → [[RBM45]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.48×** | +4.6 | 0.002 | 11/27 (NCI-H2347, SK-MEL-2, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.39×** | +4.0 | 0.016 | 9/34 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.6 | 0.063 | 8/35 (SW480, PANC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.083 | 6/35 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.28× | +3.1 | 0.23 | 6/35 (SNU-1, NCI-H23, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.0 | 0.23 | 6/35 (PANC-1, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.407×** | -15.5 | 0e+00 | 24/30 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.373×** | -12.0 | 1e-30 | 30/35 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.572×** | -9.6 | 1e-19 | 26/32 (SNU-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.504×** | -8.3 | 1e-14 | 19/30 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -8.0 | 2e-13 | 21/33 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.533×** | -7.4 | 2e-11 | 15/30 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.559×** | -7.1 | 1e-10 | 18/34 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -6.6 | 3e-09 | 20/34 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -6.6 | 3e-09 | 19/34 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.570×** | -6.6 | 3e-09 | 16/33 (PANC-1, SNU-1, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.603×** | -6.2 | 4e-08 | 18/35 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.502×** | -4.4 | 6e-04 | 14/35 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.541×** | -3.9 | 0.004 | 11/30 (HS-578T, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.734×** | -3.8 | 0.007 | 10/34 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.751×** | -3.5 | 0.019 | 11/35 (PANC-1, A-172, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.023 | 10/34 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.763×** | -3.3 | 0.032 | 7/35 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.609×** | -3.2 | 0.044 | 7/29 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.788×** | -2.9 | 0.099 | 8/34 (SNU-423, LoVo, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.3 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -23.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.126× (z -17.5) |
| [[SNU-1 (line)]] | wt | 33.7 | 0 | 10 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0547× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 27.2 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.8) |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0978× (z -14.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -11.7) |
| [[HOP62 (line)]] | alt | 14.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 8.91 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0877× (z -12.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Loperamide (hydrochloride) (drug)]] 0.05 µM 0.0776× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -14.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-172 (line)]] | wt | 7.86 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.9) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 7.52 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -12.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 5.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -8.6) ⚠ cell-cycle shift, explains ~30% of this change |
| [[C32 (line)]] | wt | 4.31 | 0 | 1 | — | [[γ-Oryzanol (drug)]] 0.5 µM 0.0678× (z -8.6) |
| [[J82 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -9.7) ⚠ toxic |
| [[LoVo (line)]] | wt | 6.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0942× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 4.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0343× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SNU-423 (line)]] | alt | 4.01 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.976 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP6]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[CHST10]] | +0.59 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PSTK]] | +0.55 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[RAD51D]] | +0.54 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[VASH1]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[ZNF236]] | +0.52 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[EXO5]] | +0.51 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[TERT]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[CASP2]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[WIPF1]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[RPRD1A]] | +0.50 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZNF354C]] | +0.50 | +0.50 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RORC]] | -0.49 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[ZNF703]] | -0.47 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[SLC50A1]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[ERBB3]] | -0.46 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[PROX1-AS1]] | -0.45 | -0.48 / -0.37 | both halves | 8e-05 | same gene group |
| [[THBS4-AS1]] | -0.45 | -0.30 / -0.44 | both halves | 2e-04 | same gene group |
| [[LINC00299]] | -0.44 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[ADCY4]] | -0.42 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[SPATA6L]] | -0.42 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[FGD5]] | -0.42 | -0.46 / -0.34 | both halves | 1e-04 |  |
| [[LINC01814]] | -0.42 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[FOXO4]] | -0.42 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAMTS10]] | B | ADAMTS10 activity raises KHDC1-AS1's level | lines that do not express ADAMTS10 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without ADAMTS10 | 0.071 | ⚠ within organs, on part of the lines; also absent: TSHZ3, EPHA5-AS1, HECW2; maybe low, not absent |
| [[ERBB3]] | B | ERBB3 activity lowers KHDC1-AS1's level | lines that do not express ERBB3 (27) vs lines expressing it (23) | 2.48× higher at baseline in the lines without ERBB3 | 0.073 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[VASH1]] | C | VASH1 activity raises KHDC1-AS1's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 3.38× lower at baseline in the lines without VASH1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B; co-absent with the target |
| [[WIPF1]] | C | WIPF1 activity raises KHDC1-AS1's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 2.47× lower at baseline in the lines without WIPF1 | 0.057 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3; co-absent with the target |
| [[TTC7B]] | C | TTC7B activity raises KHDC1-AS1's level | lines that do not express TTC7B (9) vs lines expressing it (41) | 3.26× lower at baseline in the lines without TTC7B | 0.082 | ⚠ within organs, on part of the lines; also absent: SYNGR1, HDGFL3, HLTF; co-absent with the target |
| [[ARHGEF25]] | C | ARHGEF25 activity raises KHDC1-AS1's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 2.56× lower at baseline in the lines without ARHGEF25 | 0.090 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10; co-absent with the target |
| [[GBX2-AS1]] | C | GBX2-AS1 activity raises KHDC1-AS1's level | lines that do not express GBX2-AS1 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without GBX2-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ANTXR1, KCNK13, TTC7B; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RBM45]] | B | KHDC1-AS1 activity raises RBM45's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 1.29× lower at baseline in the lines without KHDC1-AS1 | 0.022 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7 |
| [[ZNF530]] | B | KHDC1-AS1 activity raises ZNF530's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 2.19× lower at baseline in the lines without KHDC1-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7 |
| [[ZFP69]] | B | KHDC1-AS1 activity raises ZFP69's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 1.56× lower at baseline in the lines without KHDC1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7 |
| [[VASH1]] | C | KHDC1-AS1 activity raises VASH1's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 2.61× lower at baseline in the lines without KHDC1-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |
| [[TTC7B]] | C | KHDC1-AS1 activity raises TTC7B's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 3.66× lower at baseline in the lines without KHDC1-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |
| [[WIPF1]] | C | KHDC1-AS1 activity raises WIPF1's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 6.38× lower at baseline in the lines without KHDC1-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |
| [[ANKRD6]] | C | KHDC1-AS1 activity raises ANKRD6's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 4.04× lower at baseline in the lines without KHDC1-AS1 | 0.047 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |
| [[GBX2-AS1]] | C | KHDC1-AS1 activity raises GBX2-AS1's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 2.37× lower at baseline in the lines without KHDC1-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |
| [[ZNF287]] | C | KHDC1-AS1 activity raises ZNF287's level | lines that do not express KHDC1-AS1 (13) vs lines expressing it (37) | 2.24× lower at baseline in the lines without KHDC1-AS1 | 0.080 | ⚠ within organs, on part of the lines; also absent: MSN, PYGO1, TIGD7; co-absent with the target |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-37.0, 23.7); signed map (-9.1, -54.0). **Vector** length 55.2, 9.29% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | +3.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | -0.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.0 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.9 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +0.8 | +0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.8 | +2.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.4 | -15.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.3 | +0.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | KHDC1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q13 — chr6:73,263,212-73,301,789 (+) |
| Ensembl biotype | lncRNA |
| Also known as | lnc-KHDC3L-2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55468](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55468) · Entrez [122539212](https://www.ncbi.nlm.nih.gov/gene/122539212) · Ensembl [ENSG00000229852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229852)

## Data

Gene col 13718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13718); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13718]; `tensor/DDL_lfc|DDL_z.npy` [13718]; `embed/gene_vectors.npy` [13718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13718 or target_col == 13718). Every well: [[KHDC1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KHDC1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
