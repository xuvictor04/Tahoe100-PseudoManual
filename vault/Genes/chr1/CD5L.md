---
symbol: "CD5L"
type: "gene"
col: 1059
ensembl_id: "ENSG00000073754"
name: "CD5 molecule like"
location: "1q23.1"
module: 70
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 27
n_dd_up: 26
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 82
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# CD5L

*CD5 molecule like* — 1q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.64× (z +11.7, q 5e-29, up in 19 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.0474×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.0212×; ⚠ cell-cycle shift, explains ~92% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0902×; ⚠ toxic; transcription drop); [[Dexamethasone (drug)]] 0.05 µM in 1 line (A498 0.106×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOL3]] (+0.74, fdr 7e-06), [[GBP4]] (+0.71, fdr 7e-06), [[IL15RA]] (+0.69, fdr 7e-06); moves opposite to [[ITGA10]] (-0.57, fdr 1e-05), [[AKAP12]] (-0.53, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC02384]] → it (grade B ⚠); 82 go from it, the strongest it → [[PML]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.64×** | +11.7 | 5e-29 | 19/21 (C32, NCI-H2347, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +8.3 | 3e-14 | 4/15 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +8.0 | 3e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.27×** | +7.6 | 4e-12 | 10/16 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.03×** | +6.6 | 5e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.40×** | +5.6 | 2e-06 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +4.6 | 3e-04 | 11/22 (A498, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.97×** | +4.3 | 1e-03 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.88×** | +3.9 | 0.005 | 5/16 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Saquinavir (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.005 | 0/15 | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.17×** | +3.9 | 0.005 | 2/2 (SK-MEL-2, A498) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.25×** | +3.7 | 0.010 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.49×** | +3.6 | 0.012 | 2/20 (SK-MEL-2, hTERT-HPNE) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +3.6 | 0.013 | 5/18 (NCI-H1792, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.024 | 2/16 (C32, NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.034 | 7/18 (MIA PaCa-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.73×** | +3.3 | 0.036 | 2/9 (HS-578T, RPMI-7951) | all doses, flat |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.66×** | +3.3 | 0.036 | 0/7 | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **1.65×** | +3.2 | 0.036 | 1/20 (C32) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.44×** | +3.2 | 0.036 | 9/19 (Hs 766T, A549, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.64×** | +3.0 | 0.060 | 5/17 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.066 | 6/23 (SK-MEL-2, AsPC-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1059.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.0474×); [[Harringtonine (drug)]] 5 µM in 1 line (A498 0.0212×; ⚠ cell-cycle shift, explains ~92% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0902×; ⚠ toxic; transcription drop); [[Dexamethasone (drug)]] 0.05 µM in 1 line (A498 0.106×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[crizotinib (drug)]] 5 µM |  | 0.594× | -3.2 | 0.43 | 3/20 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.706× | -3.2 | 0.43 | 13/19 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 6.00 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0474× (z -17.8) |
| [[C32 (line)]] | wt | 1.13 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 27.9× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 46.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0902× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.892 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.799 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.270 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.968 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.300 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.550 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.351 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.659 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.324 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOL3]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GBP4]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[IL15RA]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NLRC5]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PARP12]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[GBP3]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TAP2]] | +0.66 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SHFL]] | +0.64 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[IDO1]] | +0.63 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[SLC15A3]] | +0.63 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[CFB]] | +0.60 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[TNFSF10]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA10]] | -0.57 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[AKAP12]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02384]] | B | LINC02384 activity raises CD5L's level | lines that do not express LINC02384 (26) vs lines expressing it (24) | 1.67× lower at baseline in the lines without LINC02384 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, ENSG00000277693, FAM230C; maybe low, not absent |
| [[GPR158]] | B | GPR158 activity raises CD5L's level | lines that do not express GPR158 (20) vs lines expressing it (30) | 1.47× lower at baseline in the lines without GPR158 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, P2RX7, LINC02968 |
| [[TP63]] | C | TP63 activity raises CD5L's level | lines that do not express TP63 (39) vs lines expressing it (11) | 2.32× lower at baseline in the lines without TP63 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX10, ENSG00000241168, TYR; co-absent with the target |
| [[TRIM22]] | C | TRIM22 activity raises CD5L's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.95× lower at baseline in the lines without TRIM22 | 0.032 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1; co-absent with the target |
| [[IFI6]] | C | IFI6 activity raises CD5L's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without IFI6 | 0.032 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; co-absent with the target |
| [[FBXO39]] | C | FBXO39 activity raises CD5L's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without FBXO39 | 0.039 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3; co-absent with the target |
| [[SAMD9L]] | C | SAMD9L activity raises CD5L's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.87× lower at baseline in the lines without SAMD9L | 0.044 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22; co-absent with the target |
| [[GBP5]] | C | GBP5 activity raises CD5L's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without GBP5 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3; co-absent with the target |
| [[ITIH5]] | C | ITIH5 activity raises CD5L's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 2.16× lower at baseline in the lines without ITIH5 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[GBP4]] | C | GBP4 activity raises CD5L's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.97× lower at baseline in the lines without GBP4 | 0.066 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1; co-absent with the target |
| [[GBP1]] | C | GBP1 activity raises CD5L's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without GBP1 | 0.076 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9; co-absent with the target |

### Downstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 65, C 17. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PML]] | B | CD5L activity raises PML's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without CD5L | 4e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[OAS2]] | B | CD5L activity raises OAS2's level | lines that do not express CD5L (23) vs lines expressing it (27) | 4.23× lower at baseline in the lines without CD5L | 1e-03 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[UBA7]] | B | CD5L activity raises UBA7's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without CD5L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[NLRC5]] | B | CD5L activity raises NLRC5's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.12× lower at baseline in the lines without CD5L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[PARP14]] | B | CD5L activity raises PARP14's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without CD5L | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[SHFL]] | B | CD5L activity raises SHFL's level | lines that do not express CD5L (23) vs lines expressing it (27) | 1.77× lower at baseline in the lines without CD5L | 0.003 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[PARP9]] | B | CD5L activity raises PARP9's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.32× lower at baseline in the lines without CD5L | 0.004 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[IFI35]] | B | CD5L activity raises IFI35's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without CD5L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[SAMD9]] | B | CD5L activity raises SAMD9's level | lines that do not express CD5L (23) vs lines expressing it (27) | 3.82× lower at baseline in the lines without CD5L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[CTSS]] | B | CD5L activity raises CTSS's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.98× lower at baseline in the lines without CD5L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[SP100]] | B | CD5L activity raises SP100's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.30× lower at baseline in the lines without CD5L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[UBE2L6]] | B | CD5L activity strengthens UBE2L6's drug response | lines that do not express CD5L (18) vs lines expressing it (24) | the lines without CD5L respond 0.51× as strongly (z diff +2.13); strongest at Panobinostat 5 µM: 0.56x vs 0.34x (z diff +3.7) | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.662). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.2, 52.3); signed map (61.3, 30.4). **Vector** length 47.8, 11.2% of its response variance represented; |z| ≥ 3 in 549 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Non-canonical inflammasome activation* (reactome, mean cos +0.55 to 4); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.52 to 4); *CASP4 inflammasome assembly* (reactome, mean cos +0.60 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.5 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.4 | +3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +2.0 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.8 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.7 | +3.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | CD5 molecule like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.1 — chr1:157,830,911-157,898,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Spalpha; previously API6 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing |
| Reactome | 3 pathways, smallest: Scavenging by Class B Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O43866](https://www.uniprot.org/uniprotkb/O43866) (CD5 antigen-like):

> Secreted protein that acts as a key regulator of lipid synthesis: mainly expressed by macrophages in lymphoid and inflamed tissues and regulates mechanisms in inflammatory responses, such as infection or atherosclerosis. Able to inhibit lipid droplet size in adipocytes. Following incorporation into mature adipocytes via CD36-mediated endocytosis, associates with cytosolic FASN, inhibiting fatty acid synthase activity and leading to lipolysis, the degradation of triacylglycerols into glycerol …

**Summary**, from NCBI Gene [922](https://www.ncbi.nlm.nih.gov/gene/922):

> Predicted to be involved in regulation of complement activation. Predicted to act upstream of or within positive regulation of complement-dependent cytotoxicity. Located in cell surface. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:1690](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1690) · Entrez [922](https://www.ncbi.nlm.nih.gov/gene/922) · UniProt [O43866](https://www.uniprot.org/uniprotkb/O43866) · Ensembl [ENSG00000073754](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073754)

## Data

Gene col 1059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1059); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1059]; `tensor/DDL_lfc|DDL_z.npy` [1059]; `embed/gene_vectors.npy` [1059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1059 or target_col == 1059). Every well: [[CD5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CD5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
