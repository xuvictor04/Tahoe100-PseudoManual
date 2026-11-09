---
symbol: "TNK1"
type: "gene"
col: 10481
ensembl_id: "ENSG00000174292"
name: "tyrosine kinase non receptor 1"
location: "17p13.1"
module: 11
arm: "+"
pooled_cpm: 2.52
n_lines_expressing: 37
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TNK1

*tyrosine kinase non receptor 1* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.36× (z +12.7, q 3e-34, up in 21 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pioglitazone (drug)]] 0.5 µM in 1 line (AsPC-1 0.0617×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.106×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OVOL1]] (+0.64, fdr 1e-05), [[MAD2L1BP]] (+0.61, fdr 4e-05), [[ZNF701]] (+0.60, fdr 2e-05); moves opposite to [[GGCT]] (-0.60, fdr 2e-05), [[NHP2]] (-0.58, fdr 2e-04), [[ERI1]] (-0.52, fdr 1e-04).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[OVOL1]] → it (grade B ⚠); 7 go from it, the strongest it → [[KPNB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10481.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.36×** | +12.7 | 3e-34 | 21/27 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.2 | 1e-07 | 4/23 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.51×** | +6.0 | 3e-07 | 11/33 (LoVo, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +4.8 | 3e-04 | 13/28 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.7 | 3e-04 | 1/7 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.3 | 0.001 | 1/18 (COLO 205) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.0 | 0.005 | 0/14 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.6 | 0.023 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **1.84×** | +3.3 | 0.053 | 2/19 (CFPAC-1, SW480) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.053 | 1/19 (LS 180) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.079 | 3/21 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.083 | 1/20 (CFPAC-1) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.1 | 0.083 | 5/14 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Silodosin (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.083 | 3/22 (NCI-H2030, HCT15, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Pioglitazone (drug)]] 0.5 µM in 1 line (AsPC-1 0.0617×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 0.106×; ⚠ toxic; transcription drop).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10481. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.62 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -8.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 4.89 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0617× (z -10.6) |
| [[A-172 (line)]] | wt | 0.615 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.704 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.388 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.484 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.802 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.812 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.24 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10481), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OVOL1]] | +0.64 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[MAD2L1BP]] | +0.61 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[ZNF701]] | +0.60 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[MEPCE]] | +0.59 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[ZNF525]] | +0.59 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ZCCHC3]] | +0.58 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[MAP3K2-DT]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[BRD2]] | +0.57 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[ZSWIM1]] | +0.57 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ZFTA]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[RNF103]] | +0.56 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[FAM200A]] | +0.56 | +0.56 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGCT]] | -0.60 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[NHP2]] | -0.58 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[ERI1]] | -0.52 | -0.55 / -0.33 | both halves | 1e-04 |  |
| [[TREX2]] | -0.52 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[KIAA1328]] | -0.52 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[NUP93]] | -0.51 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[LSM4]] | -0.51 | -0.53 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[POLA1]] | -0.51 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[EIF3K]] | -0.51 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[NUDT21]] | -0.50 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[CBX3]] | -0.50 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[SNRPA]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[GOLM2]] | -0.49 | -0.48 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OVOL1]] | B | OVOL1 activity raises TNK1's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.59× lower at baseline in the lines without OVOL1 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[HCP5]] | B | HCP5 activity raises TNK1's level | lines that do not express HCP5 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without HCP5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TINAGL1, LINC02832, ENSG00000236451 |
| [[HLA-V-1]] | B | HLA-V-1 activity raises TNK1's level | lines that do not express HLA-V-1 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without HLA-V-1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MST1R, KIAA0040 |
| [[KMO]] | B | KMO activity lowers TNK1's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.07× higher at baseline in the lines without KMO | 0.091 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KPNB1]] | B | TNK1 activity lowers KPNB1's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.18× higher at baseline in the lines without TNK1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[TBKBP1]] | B | TNK1 activity lowers TBKBP1's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.55× higher at baseline in the lines without TNK1 | 0.066 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[AP5S1]] | B | TNK1 activity raises AP5S1's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.20× lower at baseline in the lines without TNK1 | 0.067 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[DLX2]] | B | TNK1 activity lowers DLX2's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 1.76× higher at baseline in the lines without TNK1 | 0.083 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[STAP2]] | B | TNK1 activity raises STAP2's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 2.12× lower at baseline in the lines without TNK1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[RNF103-CHMP3]] | B | TNK1 activity raises RNF103-CHMP3's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 2.29× lower at baseline in the lines without TNK1 | 0.089 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |
| [[PLEKHG3]] | B | TNK1 activity raises PLEKHG3's level | lines that do not express TNK1 (13) vs lines expressing it (37) | 2.20× lower at baseline in the lines without TNK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: TUBA4A, CDCP1, CHMP4C; maybe low, not absent |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.5, 7.3); signed map (4.2, -18.1). **Vector** length 34.7, 4.07% of its response variance represented; |z| ≥ 3 in 725 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +12.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.8 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.0 | +3.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.1 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -0.8 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -1.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | tyrosine kinase non receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,380,534-7,389,774 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOS1 |
| Gene groups (HGNC) | TNK family tyrosine kinases; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13470](https://www.uniprot.org/uniprotkb/Q13470) (Non-receptor tyrosine-protein kinase TNK1):

> Involved in negative regulation of cell growth. Has tumor suppressor properties. Plays a negative regulatory role in the Ras-MAPK pathway. May function in signaling pathways utilized broadly during fetal development and more selectively in adult tissues and in cells of the lymphohematopoietic system. Could specifically be involved in phospholipid signal transduction.

**Summary**, from NCBI Gene [8711](https://www.ncbi.nlm.nih.gov/gene/8711):

> The protein encoded by this gene belongs to the tyrosine protein kinase family. Tyrosine protein kinases are important regulators of intracellular signal transduction pathways, mediating cellular proliferation, survival, and development. This gene is highly expressed in fetal tissues and at lower levels in few adult tissues, thus may function in signaling pathways utilized broadly during fetal development, and more selectively in adult tissues. It plays a negative regulatory role in the …

**Accessions** — [HGNC:11940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11940) · Entrez [8711](https://www.ncbi.nlm.nih.gov/gene/8711) · UniProt [Q13470](https://www.uniprot.org/uniprotkb/Q13470) · Ensembl [ENSG00000174292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174292)

## Data

Gene col 10481: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10481); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10481, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10481]; `tensor/DDL_lfc|DDL_z.npy` [10481]; `embed/gene_vectors.npy` [10481]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10481 or target_col == 10481). Every well: [[TNK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
