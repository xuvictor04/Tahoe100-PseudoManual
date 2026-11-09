---
symbol: "HAS2"
type: "gene"
col: 10035
ensembl_id: "ENSG00000170961"
name: "hyaluronan synthase 2"
location: "8q24.13"
module: 13
arm: "+"
pooled_cpm: 27.85
n_lines_expressing: 23
n_dd_up: 3
n_dd_down: 32
n_dd_up_clean: 1
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 15
direction_downstream: 23
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# HAS2

*hyaluronan synthase 2* — 8q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.61× (z +4.5, q 0.004, up in 0 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.16× (z +3.8, q 0.041, up in 12 of 20 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 10.1×, CFPAC-1 9.31×; ⚠ cell-cycle shift, explains ~41% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (CFPAC-1 6.39×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.239× (z -13.4, q 2e-38, down in 19 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRX1]] (+0.55, fdr 1e-05), [[HTR7]] (+0.53, fdr 1e-05), [[SGIP1]] (+0.51, fdr 3e-05); moves opposite to [[NAPB]] (-0.47, fdr 8e-05), [[FAM168B]] (-0.46, fdr 2e-04), [[IQSEC2]] (-0.46, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[NOXA1]] → it (grade B ⚠); 23 go from it, the strongest it → [[HMGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10035.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H1573 10.1×, CFPAC-1 9.31×; ⚠ cell-cycle shift, explains ~41% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (CFPAC-1 6.39×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +4.5 | 0.004 | 0/18 | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +3.8 | 0.041 | 12/20 (NCI-H1573, Hs 766T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.6 | 0.053 | 2/17 (HOP62, RPMI-7951) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.41× | +3.3 | 0.12 | 2/20 (NCI-H1573, HOP62) | top dose only |  |
| [[Flutamide (drug)]] 5 µM |  | 1.41× | +3.3 | 0.12 | 7/20 (NCI-H1573, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, none with an alert; shown: the 15 strongest. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10035.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.239×** | -13.4 | 2e-38 | 19/20 (Hs 766T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.392×** | -8.8 | 5e-16 | 20/20 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.412×** | -8.3 | 2e-14 | 19/20 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.458×** | -7.3 | 4e-11 | 19/20 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.619×** | -6.3 | 3e-08 | 17/21 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -5.1 | 3e-05 | 16/20 (NCI-H1792, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.589×** | -4.9 | 6e-05 | 17/20 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.577×** | -4.9 | 6e-05 | 11/21 (NCI-H1792, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.580×** | -4.9 | 6e-05 | 12/20 (NCI-H1792, AsPC-1, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.577×** | -4.8 | 1e-04 | 11/20 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.614×** | -4.6 | 3e-04 | 15/20 (NCI-H1792, SW480, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.606×** | -4.5 | 3e-04 | 15/20 (Hs 766T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.405×** | -4.4 | 4e-04 | 19/21 (NCI-H1792, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.639×** | -4.2 | 0.001 | 14/20 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.681×** | -3.6 | 0.013 | 9/20 (Hs 766T, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10035. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 227 | 0 | 18 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0486× (z -27.2) |
| [[Hs 766T (line)]] | wt | 96.4 | 0 | 11 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0371× (z -21.5) |
| [[LOX-IMVI (line)]] | wt | 220 | 0 | 10 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0514× (z -17.2) |
| [[RKO (line)]] | wt | 34.9 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0239× (z -17.2) |
| [[HS-578T (line)]] | alt | 171 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0295× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 123 | 0 | 8 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0195× (z -16.6) |
| [[AsPC-1 (line)]] | alt | 45.1 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0761× (z -12.0) |
| [[SW1417 (line)]] | alt | 24.3 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.180× (z -9.3) |
| [[SW480 (line)]] | alt | 17.8 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.110× (z -15.3) |
| [[CFPAC-1 (line)]] | alt | 18.0 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 9.31× (z +9.8) ⚠ cell-cycle shift, explains ~41% of this change | [[Belinostat (drug)]] 5 µM 0.150× (z -8.6) |
| [[CHP-212 (line)]] | wt | 114 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0325× (z -14.5) |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 53.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.185× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -14.0) |
| [[SW48 (line)]] | wt | 18.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 10.1× (z +10.5) ⚠ cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.96 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.20 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.78 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 22.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10035), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRX1]] | +0.55 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[HTR7]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[SGIP1]] | +0.51 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MIR100HG]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ARL10]] | +0.49 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[ZNF385D]] | +0.49 | +0.44 / +0.31 | both halves | 2e-04 |  |
| [[FRMD4A]] | +0.48 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[CACNA1A]] | +0.47 | +0.35 / +0.39 | both halves | 1e-04 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[AMOTL1]] | +0.47 | +0.36 / +0.49 | both halves | 9e-05 |  |
| [[HTR1F]] | +0.47 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[SETBP1]] | +0.46 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[PTGS2]] | +0.46 | +0.56 / +0.40 | both halves | 5e-05 | STRING 597 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAPB]] | -0.47 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[FAM168B]] | -0.46 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[IQSEC2]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[PHKB]] | -0.44 | -0.38 / -0.43 | both halves | 6e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[EIF4E3]] | -0.44 | -0.23 / -0.41 | both halves | 5e-04 |  |
| [[NT5C2]] | -0.44 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[RTN3]] | -0.43 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[MIR3936HG]] | -0.43 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[CLCC1]] | -0.43 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[NOXA1]] | -0.42 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[FN3K]] | -0.40 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[ARHGEF10L]] | -0.40 | -0.32 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 5, C 10. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | NOXA1 activity lowers HAS2's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 5.77× higher at baseline in the lines without NOXA1 | 0.024 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[LINC02454]] | B | LINC02454 activity raises HAS2's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 4.26× lower at baseline in the lines without LINC02454 | 0.043 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[HMGA2]] | B | HMGA2 activity raises HAS2's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 4.13× lower at baseline in the lines without HMGA2 | 0.047 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[NPAS2]] | B | NPAS2 activity raises HAS2's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 3.51× lower at baseline in the lines without NPAS2 | 0.069 | ⚠ within organs, on part of the lines |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises HAS2's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 4.02× lower at baseline in the lines without CDK6-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[STC1]] | C | STC1 activity raises HAS2's level | lines that do not express STC1 (24) vs lines expressing it (26) | 3.92× lower at baseline in the lines without STC1 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP; co-absent with the target |
| [[FRMD4A]] | C | FRMD4A activity raises HAS2's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.60× lower at baseline in the lines without FRMD4A | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[PTHLH]] | C | PTHLH activity raises HAS2's level | lines that do not express PTHLH (20) vs lines expressing it (30) | 3.10× lower at baseline in the lines without PTHLH | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, KMT2D; also absent: TGFBI, LINC02057, COL7A1; co-absent with the target |
| [[RFX8]] | C | RFX8 activity raises HAS2's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 4.31× lower at baseline in the lines without RFX8 | 0.023 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN; co-absent with the target |
| [[PTGS2]] | C | PTGS2 activity raises HAS2's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 3.72× lower at baseline in the lines without PTGS2 | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises HAS2's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 4.15× lower at baseline in the lines without PRRX1 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[HTR7]] | C | HTR7 activity raises HAS2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 3.11× lower at baseline in the lines without HTR7 | 0.051 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 13, C 10. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2]] | B | HAS2 activity raises HMGA2's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 3.40× lower at baseline in the lines without HAS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[FN3K]] | B | HAS2 activity lowers FN3K's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.71× higher at baseline in the lines without HAS2 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[ARL10]] | B | HAS2 activity raises ARL10's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without HAS2 | 0.018 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[EGR3]] | B | HAS2 activity raises EGR3's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 2.38× lower at baseline in the lines without HAS2 | 0.022 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[NOXA1]] | B | HAS2 activity lowers NOXA1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.81× higher at baseline in the lines without HAS2 | 0.024 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[LINC02454]] | B | HAS2 activity raises LINC02454's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.92× lower at baseline in the lines without HAS2 | 0.025 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[MIR3936HG]] | B | HAS2 activity lowers MIR3936HG's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.68× higher at baseline in the lines without HAS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[MIR100HG]] | B | HAS2 activity raises MIR100HG's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 3.60× lower at baseline in the lines without HAS2 | 0.039 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[SPOCD1]] | B | HAS2 activity raises SPOCD1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 2.48× lower at baseline in the lines without HAS2 | 0.052 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[TIMP1]] | B | HAS2 activity raises TIMP1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.75× lower at baseline in the lines without HAS2 | 0.061 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[HRH1]] | B | HAS2 activity raises HRH1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without HAS2 | 0.074 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |
| [[PHLDA1]] | B | HAS2 activity raises PHLDA1's level | lines that do not express HAS2 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without HAS2 | 0.080 | ⚠ within organs, on part of the lines; also absent: RFX8, IRAG2, PRRX1 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.440). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 8.0); signed map (10.9, 49.9). **Vector** length 78.8, 22.3% of its response variance represented; |z| ≥ 3 in 775 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +1.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.0 | +0.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +3.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.1 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +1.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +0.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.9 | +2.5 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.9 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | hyaluronan synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.13 — chr8:121,612,116-121,641,440 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycosyltransferase family 2 |
| Hallmark sets | INFLAMMATORY_RESPONSE, UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: Hyaluronan metabolism; Glycosaminoglycan metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92819](https://www.uniprot.org/uniprotkb/Q92819) (Hyaluronan synthase 2):

> Catalyzes the addition of GlcNAc or GlcUA monosaccharides to the nascent hyaluronan polymer (Probable). Therefore, it is essential to hyaluronan synthesis a major component of most extracellular matrices that has a structural role in tissues architectures and regulates cell adhesion, migration and differentiation. This is one of three isoenzymes responsible for cellular hyaluronan synthesis and it is particularly responsible for the synthesis of high molecular mass hyaluronan (By similarity).

**Summary**, from NCBI Gene [3037](https://www.ncbi.nlm.nih.gov/gene/3037):

> Hyaluronan or hyaluronic acid (HA) is a high molecular weight unbranched polysaccharide synthesized by a wide variety of organisms from bacteria to mammals, and is a constituent of the extracellular matrix. It consists of alternating glucuronic acid and N-acetylglucosamine residues that are linked by beta-1-3 and beta-1-4 glycosidic bonds. HA is synthesized by membrane-bound synthase at the inner surface of the plasma membrane, and the chains are extruded through pore-like structures into the …

**Accessions** — [HGNC:4819](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4819) · Entrez [3037](https://www.ncbi.nlm.nih.gov/gene/3037) · UniProt [Q92819](https://www.uniprot.org/uniprotkb/Q92819) · Ensembl [ENSG00000170961](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170961)

## Data

Gene col 10035: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10035); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10035, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10035]; `tensor/DDL_lfc|DDL_z.npy` [10035]; `embed/gene_vectors.npy` [10035]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10035 or target_col == 10035). Every well: [[HAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
