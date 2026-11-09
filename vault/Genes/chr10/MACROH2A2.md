---
symbol: "MACROH2A2"
type: "gene"
col: 1790
ensembl_id: "ENSG00000099284"
name: "macroH2A.2 histone"
location: "10q22.1"
module: 18
arm: "+"
pooled_cpm: 15.08
n_lines_expressing: 31
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# MACROH2A2

*macroH2A.2 histone* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +8.1, q 4e-13, up in 8 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +5.7, q 4e-06, up in 16 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.273× (z -21.2, q 0e+00, down in 27 of 29 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF11]] (+0.69, fdr 7e-06), [[ATAD2B]] (+0.68, fdr 1e-05), [[USP46]] (+0.65, fdr 3e-05); moves opposite to [[RALY]] (-0.57, fdr 3e-05), [[TMEM92]] (-0.54, fdr 2e-04), [[RTN4]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FAM169A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[FAM169A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +8.1 | 4e-13 | 8/16 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.7 | 4e-06 | 16/29 (CFPAC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.3 | 3e-05 | 14/26 (HOP62, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.1 | 6e-05 | 15/29 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +4.4 | 0.001 | 10/29 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.9 | 0.009 | 11/22 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.084 | 7/29 (C-33 A, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +3.2 | 0.086 | 5/29 (CFPAC-1, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.273×** | -21.2 | 0e+00 | 27/29 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.278×** | -20.9 | 0e+00 | 25/29 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.380×** | -15.8 | 0e+00 | 23/29 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -7.6 | 4e-12 | 18/29 (NCI-H23, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.629×** | -7.6 | 4e-12 | 18/29 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.730×** | -7.3 | 3e-11 | 18/29 (SW480, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.707×** | -5.7 | 1e-06 | 16/29 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.747×** | -4.8 | 1e-04 | 15/29 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -4.6 | 3e-04 | 16/28 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.624×** | -4.0 | 0.003 | 11/29 (AN3 CA, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.792×** | -3.6 | 0.017 | 11/29 (HCT15, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.5 | 0.020 | 10/29 (C-33 A, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.806×** | -3.4 | 0.029 | 14/29 (AN3 CA, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **0.672×** | -3.4 | 0.029 | 8/28 (RKO, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.807×** | -3.4 | 0.030 | 11/25 (C-33 A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.696×** | -3.1 | 0.071 | 9/26 (LS 180, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.832×** | -3.0 | 0.083 | 12/29 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 50.4 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.211× (z -14.4) |
| [[AN3 CA (line)]] | alt | 76.2 | 0 | 7 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0594× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0879× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 24.7 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -15.3) |
| [[C-33 A (line)]] | alt | 55.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0620× (z -22.0) |
| [[SW480 (line)]] | alt | 39.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.0992× (z -26.6) |
| [[A-427 (line)]] | wt | 31.5 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.167× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.135× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 32.8 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -11.5) |
| [[A549 (line)]] | wt | 27.5 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 21.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.218× (z -10.6) |
| [[RKO (line)]] | wt | 39.8 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.259× (z -10.5) |
| [[BT-474 (line)]] | alt | 42.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -14.0) |
| [[LS 180 (line)]] | wt | 29.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.245× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.141× (z -10.8) |
| [[H4 (line)]] | wt | 11.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.107× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 47.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -9.6) |
| [[SNU-1 (line)]] | wt | 21.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -8.5) |
| [[A-172 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.50 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.06 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF11]] | +0.69 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ATAD2B]] | +0.68 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[USP46]] | +0.65 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[RAB11FIP2]] | +0.62 | +0.58 / +0.38 | both halves | 7e-05 |  |
| [[MVB12B]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SMAD1]] | +0.58 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[ZNF346]] | +0.58 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[PAXBP1]] | +0.58 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[NSMAF]] | +0.58 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[FAM169A]] | +0.57 | +0.62 / +0.22 | both halves | 6e-04 |  |
| [[SLC35G1]] | +0.57 | +0.56 / +0.28 | both halves | 3e-04 |  |
| [[GABPB1]] | +0.57 | +0.35 / +0.38 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALY]] | -0.57 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[TMEM92]] | -0.54 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[RTN4]] | -0.54 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[GNAI3]] | -0.54 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[CAST]] | -0.53 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[NBEAL1]] | -0.53 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[SPAG9]] | -0.52 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[GIPR]] | -0.52 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[ATOSB]] | -0.52 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[VGF]] | -0.52 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[SPTLC2]] | -0.51 | -0.43 / -0.21 | both halves | 6e-04 |  |
| [[DNAJB1]] | -0.51 | -0.36 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | FAM169A activity raises MACROH2A2's level | lines that do not express FAM169A (12) vs lines expressing it (38) | 4.53× lower at baseline in the lines without FAM169A | 0.041 | ⚠ within organs, on part of the lines; also absent: NUP210, HID1, AIF1L |
| [[MLPH]] | B | MLPH activity lowers MACROH2A2's level | lines that do not express MLPH (13) vs lines expressing it (37) | 3.25× higher at baseline in the lines without MLPH | 0.083 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[MARK1]] | B | MARK1 activity raises MACROH2A2's level | lines that do not express MARK1 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without MARK1 | 0.085 | ⚠ within organs, on part of the lines; also absent: FXYD6, COL4A4, ENSG00000283982 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM169A]] | B | MACROH2A2 activity raises FAM169A's level | lines that do not express MACROH2A2 (19) vs lines expressing it (31) | 3.06× lower at baseline in the lines without MACROH2A2 | 0.044 | ⚠ within organs, on part of the lines; also absent: MSI1, KCNQ2, GAS7 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.344). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.3, 14.0); signed map (25.8, -22.8). **Vector** length 71.4, 16.4% of its response variance represented; |z| ≥ 3 in 665 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.6 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.1 | +5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +1.8 | +3.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.2 | +2.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -20.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.3 | -21.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.9 | -15.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.2 | -7.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | macroH2A.2 histone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:70,052,544-70,112,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously H2AFY2 |
| Gene groups (HGNC) | Macro domain containing; H2A histones |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0M6](https://www.uniprot.org/uniprotkb/Q9P0M6) (Core histone macro-H2A.2):

> Variant histone H2A which replaces conventional H2A in a subset of nucleosomes where it represses transcription. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and …

**Summary**, from NCBI Gene [55506](https://www.ncbi.nlm.nih.gov/gene/55506):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Nucleosomes consist of approximately 146 bp of DNA wrapped around a histone octamer composed of pairs of each of the four core histones (H2A, H2B, H3, and H4). The chromatin fiber is further compacted through the interaction of a linker histone, H1, with the DNA between the nucleosomes to form higher order chromatin structures. This gene encodes a replication-independent …

**Accessions** — [HGNC:14453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14453) · Entrez [55506](https://www.ncbi.nlm.nih.gov/gene/55506) · UniProt [Q9P0M6](https://www.uniprot.org/uniprotkb/Q9P0M6) · Ensembl [ENSG00000099284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099284)

## Data

Gene col 1790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1790); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1790]; `tensor/DDL_lfc|DDL_z.npy` [1790]; `embed/gene_vectors.npy` [1790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1790 or target_col == 1790). Every well: [[MACROH2A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MACROH2A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
