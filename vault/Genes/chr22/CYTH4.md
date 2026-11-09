---
symbol: "CYTH4"
type: "gene"
col: 1853
ensembl_id: "ENSG00000100055"
name: "cytohesin 4"
location: "22q13.1"
module: 206
arm: "+"
pooled_cpm: 2.08
n_lines_expressing: 25
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# CYTH4

*cytohesin 4* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.31× (z +10.9, q 9e-25, up in 15 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.0536×, HOP62 0.102×; ⚠ cell-cycle shift, explains ~38% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.155×, HOP62 0.189×); [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0449×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0594×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0732×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N4BP3]] (+0.69, fdr 7e-06), [[RIN1]] (+0.66, fdr 1e-05), [[NFKBIE]] (+0.65, fdr 1e-05); moves opposite to [[ADPGK]] (-0.54, fdr 1e-05), [[SDHD]] (-0.48, fdr 9e-05), [[SETD7]] (-0.47, fdr 8e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02970]] → it (grade B ⚠); 3 go from it, the strongest it → [[SHB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1853.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.31×** | +10.9 | 9e-25 | 15/19 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.02×** | +10.0 | 3e-21 | 12/16 (SNU-423, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +8.2 | 5e-14 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.87×** | +6.8 | 2e-09 | 10/16 (NCI-H2347, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +6.7 | 3e-09 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.81×** | +6.6 | 3e-09 | 9/15 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.75×** | +6.5 | 7e-09 | 9/18 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.62×** | +6.2 | 5e-08 | 9/20 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +5.6 | 1e-06 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.39×** | +5.4 | 4e-06 | 13/17 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +4.4 | 5e-04 | 8/19 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.98×** | +4.4 | 6e-04 | 9/19 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.78×** | +3.7 | 0.010 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.22×** | +3.6 | 0.011 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +3.6 | 0.012 | 0/11 | top dose only | cell-cycle shift (explains ~24% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.13×** | +3.5 | 0.017 | 0/7 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.026 | 1/16 (NCI-H2347) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.57×** | +2.9 | 0.100 | 0/12 | rises with dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1853.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.0536×, HOP62 0.102×; ⚠ cell-cycle shift, explains ~38% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 0.155×, HOP62 0.189×); [[Digitoxin (drug)]] 5 µM in 1 line (LOX-IMVI 0.0449×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0594×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LOX-IMVI 0.0732×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.568× | -3.6 | 0.16 | 8/21 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.563× | -3.4 | 0.18 | 6/21 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.599× | -3.3 | 0.19 | 14/21 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | 0.598× | -3.2 | 0.20 | 7/22 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1853. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 11.0 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0590× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.189× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0449× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0594× (z -10.1) |
| [[PANC-1 (line)]] | alt | 4.87 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0536× (z -12.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -11.3) |
| [[A-172 (line)]] | wt | 1.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.6× (z +11.1) | — |
| [[CFPAC-1 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0998× (z -8.8) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 0.901 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.5× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 2.98 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 5.94 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0795× (z -8.5) |
| [[SNU-423 (line)]] | alt | 5.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.4× (z +14.0) | — |
| [[A-427 (line)]] | wt | 0.136 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.199 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.947 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.194 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.346 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.599 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.192 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.851 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.491 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.247 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.198 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.434 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1853), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP3]] | +0.69 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RIN1]] | +0.66 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CD82]] | +0.65 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[RAC2]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 | STRING 469; ⚠ same locus (22.4 kb: neighbours can correlate without regulation) |
| [[KCNN4]] | +0.63 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CD22]] | +0.62 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[FAM167A]] | +0.61 | +0.49 / +0.63 | both halves | 1e-05 |  |
| [[HIVEP3]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PLCH2]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[CSF1R]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 | STRING 408 |
| [[COL5A3]] | +0.59 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[FAM43A]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPGK]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SDHD]] | -0.48 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[SETD7]] | -0.47 | -0.38 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02970]] | B | LINC02970 activity raises CYTH4's level | lines that do not express LINC02970 (24) vs lines expressing it (26) | 1.79× lower at baseline in the lines without LINC02970 | 0.014 | ⚠ within organs, on part of the lines; also absent: TOX, MXRA5, ENSG00000255595 |
| [[GOLGA7B]] | B | GOLGA7B activity raises CYTH4's level | lines that do not express GOLGA7B (14) vs lines expressing it (36) | 1.79× lower at baseline in the lines without GOLGA7B | 0.060 | ⚠ within organs, on part of the lines; also absent: GOLGA7B-DT, KCNS3, ENSG00000232386; maybe low, not absent |
| [[PLCH2]] | B | PLCH2 activity raises CYTH4's level | lines that do not express PLCH2 (26) vs lines expressing it (24) | 1.60× lower at baseline in the lines without PLCH2 | 0.069 | ⚠ within organs, on part of the lines; also absent: SERPINA5, LINC01814, ACOXL; maybe low, not absent |
| [[HES6]] | B | HES6 activity lowers CYTH4's level | lines that do not express HES6 (8) vs lines expressing it (42) | 2.17× higher at baseline in the lines without HES6 | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TRIM9]] | B | TRIM9 activity raises CYTH4's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 1.57× lower at baseline in the lines without TRIM9 | 0.093 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |
| [[IL1A]] | C | IL1A activity raises CYTH4's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.93× lower at baseline in the lines without IL1A | 0.054 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT; co-absent with the target |
| [[RAC2]] | C | RAC2 activity raises CYTH4's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without RAC2 | 0.059 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHB]] | B | CYTH4 activity raises SHB's level | lines that do not express CYTH4 (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without CYTH4 | 0.063 | ⚠ within organs, on part of the lines; also absent: CSF3, ADTRP, ADAMTS16; maybe low, not absent |
| [[ARL4C]] | B | CYTH4 activity raises ARL4C's level | lines that do not express CYTH4 (25) vs lines expressing it (25) | 2.19× lower at baseline in the lines without CYTH4 | 0.067 | ⚠ within organs, on part of the lines; also absent: CSF3, ADTRP, ADAMTS16; maybe low, not absent |
| [[SEMA4B]] | B | CYTH4 activity raises SEMA4B's level | lines that do not express CYTH4 (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without CYTH4 | 0.073 | ⚠ within organs, on part of the lines; also absent: CSF3, ADTRP, ADAMTS16; maybe low, not absent |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.741). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.9, -1.5); signed map (-0.3, 43.5). **Vector** length 52.9, 13.6% of its response variance represented; |z| ≥ 3 in 591 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +10.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.6 | +6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +1.8 | +6.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +0.8 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -1.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -2.0 | +1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -2.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -3.4 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | cytohesin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,282,027-37,315,341 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CYT4, cytohesin-4; previously PSCD4 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Cytohesins |
| Reactome | 4 pathways, smallest: Intra-Golgi traffic; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIA0](https://www.uniprot.org/uniprotkb/Q9UIA0) (Cytohesin-4):

> Promotes guanine-nucleotide exchange on ARF1 and ARF5. Promotes the activation of ARF factors through replacement of GDP with GTP.

**Summary**, from NCBI Gene [27128](https://www.ncbi.nlm.nih.gov/gene/27128):

> This gene encodes a member of the PSCD family of proteins, which have an N-terminal coiled-coil motif, a central Sec7 domain, and a C-terminal pleckstrin homology (PH) domain. The coiled-coil motif is involved in homodimerization, the Sec7 domain contains guanine-nucleotide exchange protein (GEP) activity, and the PH domain interacts with phospholipids and is responsible for association of PSCDs with membranes. Members of this family function as GEPs for ADP-ribosylation factors (ARFs), which …

**Accessions** — [HGNC:9505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9505) · Entrez [27128](https://www.ncbi.nlm.nih.gov/gene/27128) · UniProt [Q9UIA0](https://www.uniprot.org/uniprotkb/Q9UIA0) · Ensembl [ENSG00000100055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100055)

## Data

Gene col 1853: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1853); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1853, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1853]; `tensor/DDL_lfc|DDL_z.npy` [1853]; `embed/gene_vectors.npy` [1853]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1853 or target_col == 1853). Every well: [[CYTH4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYTH4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
