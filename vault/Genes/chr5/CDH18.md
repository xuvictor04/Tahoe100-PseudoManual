---
symbol: "CDH18"
type: "gene"
col: 7001
ensembl_id: "ENSG00000145526"
name: "cadherin 18"
location: "5p14.3"
module: 9
arm: "+"
pooled_cpm: 16.88
n_lines_expressing: 19
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 17
direction_downstream: 20
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CDH18

*cadherin 18* — 5p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.14× (z +27.1, q 0e+00, up in 7 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.163×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0969×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMN2]] (+0.75, fdr 7e-06), [[CDH12]] (+0.72, fdr 7e-06), [[ERBB4]] (+0.67, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 20 go from it, the strongest it → [[NREP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.14×** | +27.1 | 0e+00 | 7/14 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.49×** | +15.1 | 0e+00 | 12/15 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.48×** | +15.0 | 0e+00 | 17/17 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.91×** | +12.5 | 1e-33 | 7/15 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.41×** | +9.9 | 5e-21 | 1/9 (RPMI-7951) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +8.9 | 8e-17 | 4/13 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +8.1 | 3e-14 | 2/14 (NCI-H460, A-172) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +7.6 | 2e-12 | 12/15 (NCI-H460, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +6.7 | 2e-09 | 13/16 (SHP-77, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~6% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.5 | 5e-09 | 5/17 (A-172, NCI-H460, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.3 | 1e-08 | 6/14 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.9 | 2e-07 | 7/14 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +5.7 | 5e-07 | 11/16 (NCI-H460, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.66×** | +5.7 | 5e-07 | 8/15 (A-427, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +5.2 | 6e-06 | 9/14 (NCI-H23, C-33 A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +5.0 | 2e-05 | 7/17 (NCI-H23, C-33 A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +4.7 | 8e-05 | 10/16 (NCI-H23, C-33 A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7001.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (C-33 A 0.163×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0969×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (C-33 A 0.167×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.2 | 0.47 | 1/17 (SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 759 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -17.5) |
| [[NCI-H460 (line)]] | wt | 5.16 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.28× (z +13.3) | — |
| [[A-172 (line)]] | wt | 5.20 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.75× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.171× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-427 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.58 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.92 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.59 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.92 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMN2]] | +0.75 | +0.75 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CDH12]] | +0.72 | +0.75 / +0.66 | both halves | 7e-06 | same gene group; pathway: Adherens junctions interactions; STRING 752 |
| [[ERBB4]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[HMCN1]] | +0.65 | +0.65 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ATRNL1]] | +0.65 | +0.55 / +0.64 | both halves | 1e-05 | **novel candidate** |
| [[DMD]] | +0.65 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CDH10]] | +0.65 | +0.50 / +0.65 | both halves | 1e-05 | same gene group; pathway: Adherens junctions interactions; STRING 767 |
| [[NEGR1]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[BRINP3]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 | STRING 410 |
| [[NCAM2]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[EPHA5]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[EGFEM1P]] | +0.63 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 1, C 16. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CDH18's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDH12]] | C | CDH12 activity raises CDH18's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.98× lower at baseline in the lines without CDH12 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises CDH18's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without ANGPT1 | 0.018 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[MSR1]] | C | MSR1 activity raises CDH18's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.70× lower at baseline in the lines without MSR1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[GRIA2]] | C | GRIA2 activity raises CDH18's level | lines that do not express GRIA2 (33) vs lines expressing it (17) | 3.62× lower at baseline in the lines without GRIA2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000286099, ASCL1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[NTNG1]] | C | NTNG1 activity raises CDH18's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 2.31× lower at baseline in the lines without NTNG1 | 0.030 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[LINC01885]] | C | LINC01885 activity raises CDH18's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.81× lower at baseline in the lines without LINC01885 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[MMRN1]] | C | MMRN1 activity raises CDH18's level | lines that do not express MMRN1 (43) vs lines expressing it (7) | 4.96× lower at baseline in the lines without MMRN1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, KRT5; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises CDH18's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 1.97× lower at baseline in the lines without CSMD3 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[FAM133A]] | C | FAM133A activity raises CDH18's level | lines that do not express FAM133A (29) vs lines expressing it (21) | 3.45× lower at baseline in the lines without FAM133A | 0.058 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CDH18, LINC01885, TRPC4; co-absent with the target |
| [[BRINP3]] | C | BRINP3 activity raises CDH18's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.88× lower at baseline in the lines without BRINP3 | 0.059 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent; co-absent with the target |
| [[LINC02241]] | C | LINC02241 activity raises CDH18's level | lines that do not express LINC02241 (34) vs lines expressing it (16) | 1.98× lower at baseline in the lines without LINC02241 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259560, LINC02616, LINC02476; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 2, C 18. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NREP]] | B | CDH18 activity raises NREP's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 4.05× lower at baseline in the lines without CDH18 | 0.070 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent |
| [[SYT1]] | B | CDH18 activity raises SYT1's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 2.85× lower at baseline in the lines without CDH18 | 0.074 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent |
| [[LINC01885]] | C | CDH18 activity raises LINC01885's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 5.38× lower at baseline in the lines without CDH18 | 0.009 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[MSR1]] | C | CDH18 activity raises MSR1's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without CDH18 | 0.025 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[ANGPT1]] | C | CDH18 activity raises ANGPT1's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 5.01× lower at baseline in the lines without CDH18 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[CDH12]] | C | CDH18 activity raises CDH12's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 4.32× lower at baseline in the lines without CDH18 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[RBM20]] | C | CDH18 activity raises RBM20's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 6.22× lower at baseline in the lines without CDH18 | 0.033 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[LINC02241]] | C | CDH18 activity raises LINC02241's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 3.10× lower at baseline in the lines without CDH18 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[ADGRL3]] | C | CDH18 activity raises ADGRL3's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 3.42× lower at baseline in the lines without CDH18 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[SLC6A15]] | C | CDH18 activity raises SLC6A15's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 5.00× lower at baseline in the lines without CDH18 | 0.038 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[NCAM2]] | C | CDH18 activity raises NCAM2's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 4.97× lower at baseline in the lines without CDH18 | 0.054 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[CDH10]] | C | CDH18 activity raises CDH10's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 4.74× lower at baseline in the lines without CDH18 | 0.055 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.724). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.5, 32.3); signed map (40.3, 33.9). **Vector** length 44.2, 11.4% of its response variance represented; |z| ≥ 3 in 409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +3.6 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +15.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +5.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.3 | +4.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | +0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | cadherin 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p14.3 — chr5:19,471,296-20,575,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDH14, EY-CADHERIN |
| Gene groups (HGNC) | Type II classical cadherins |
| Reactome | 4 pathways, smallest: Adherens junctions interactions; Cell-cell junction organization; Cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13634](https://www.uniprot.org/uniprotkb/Q13634) (Cadherin-18):

> Cadherins are calcium-dependent cell adhesion proteins. They preferentially interact with themselves in a homophilic manner in connecting cells; cadherins may thus contribute to the sorting of heterogeneous cell types.

**Summary**, from NCBI Gene [1016](https://www.ncbi.nlm.nih.gov/gene/1016):

> This gene encodes a type II classical cadherin from the cadherin superfamily of integral membrane proteins that mediate calcium-dependent cell-cell adhesion. Mature cadherin proteins are composed of a large N-terminal extracellular domain, a single membrane-spanning domain, and a small, highly conserved C-terminal cytoplasmic domain. Type II (atypical) cadherins are defined based on their lack of a HAV cell adhesion recognition sequence specific to type I cadherins. This particular cadherin is …

**Accessions** — [HGNC:1757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1757) · Entrez [1016](https://www.ncbi.nlm.nih.gov/gene/1016) · UniProt [Q13634](https://www.uniprot.org/uniprotkb/Q13634) · Ensembl [ENSG00000145526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145526)

## Data

Gene col 7001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7001); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7001]; `tensor/DDL_lfc|DDL_z.npy` [7001]; `embed/gene_vectors.npy` [7001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7001 or target_col == 7001). Every well: [[CDH18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDH18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
