---
symbol: "MSR1"
type: "gene"
col: 457
ensembl_id: "ENSG00000038945"
name: "macrophage scavenger receptor 1"
location: "8p22"
module: 9
arm: "+"
pooled_cpm: 34.05
n_lines_expressing: 14
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 16
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MSR1

*macrophage scavenger receptor 1* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.65× (z +14.8, q 0e+00, up in 2 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Larotrectinib (drug)]] 5 µM: 0.779× (z -3.8, q 0.083, down in 9 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LOX-IMVI 0.195×, A498 0.235×, RPMI-7951 0.436×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.250×, RPMI-7951 0.259×, A498 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.108×, RPMI-7951 0.213×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.227×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02241]] (+0.77, fdr 7e-06), [[LINC02476]] (+0.73, fdr 7e-06), [[LINC01435]] (+0.69, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[NETO1]] → it (grade C ⚠); 13 go from it, the strongest it → [[LINC02438]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +14.8 | 0e+00 | 2/12 (SNU-423, NCI-H1792) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +11.6 | 1e-28 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.03×** | +10.8 | 9e-25 | 7/12 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.7 | 3e-20 | 1/9 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +8.8 | 1e-16 | 7/12 (A498, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +7.8 | 4e-13 | 4/11 (A-172, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +6.2 | 5e-08 | 1/9 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +6.0 | 2e-07 | 5/11 (SK-MEL-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +5.3 | 8e-06 | 1/12 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +4.5 | 5e-04 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +4.3 | 1e-03 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.003 | 6/12 (RPMI-7951, A-172, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.006 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.013 | 0/11 | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +3.5 | 0.015 | 1/11 (A-427) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.033 | 5/11 (A-172, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.040 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.041 | 0/11 | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.096 | 0/11 | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 457.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (LOX-IMVI 0.195×, A498 0.235×, RPMI-7951 0.436×); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.250×, RPMI-7951 0.259×, A498 0.308×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (A-427 0.108×, RPMI-7951 0.213×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.227×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | **0.779×** | -3.8 | 0.083 | 9/12 (RPMI-7951, LOX-IMVI, …) | top dose only | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.712× | -3.4 | 0.14 | 0/12 | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.916× | -3.3 | 0.14 | 0/12 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.739× | -3.2 | 0.14 | 2/11 (RPMI-7951, LOX-IMVI) | all doses, flat |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.742× | -3.2 | 0.14 | 0/12 | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.744× | -3.2 | 0.14 | 3/11 (SHP-77, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.747× | -3.1 | 0.14 | 3/11 (A498, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 347 | 2 | 4 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.51× (z +9.3) | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -9.1) |
| [[A-172 (line)]] | wt | 20.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +17.6) | — |
| [[LOX-IMVI (line)]] | wt | 504 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -17.5) |
| [[A-427 (line)]] | wt | 96.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -15.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 261 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -15.0) |
| [[C32 (line)]] | wt | 22.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0709× (z -11.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 15.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 9.10× (z +8.8) | — |
| [[A549 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.80 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.90 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.57 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.87 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.88 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.41 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02241]] | +0.77 | +0.67 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC02476]] | +0.73 | +0.66 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC01435]] | +0.69 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[PHACTR1]] | +0.68 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[MIR4307HG]] | +0.68 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[LINC01320]] | +0.68 | +0.50 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[CDH12]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PEX5L]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SOX5]] | +0.68 | +0.45 / +0.72 | both halves | 3e-05 |  |
| [[LINC00470]] | +0.67 | +0.64 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LINC01695]] | +0.67 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TOX]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NETO1]] | C | NETO1 activity raises MSR1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 5.42× lower at baseline in the lines without NETO1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises MSR1's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 3.23× lower at baseline in the lines without LINC02492 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[KC6]] | C | KC6 activity raises MSR1's level | lines that do not express KC6 (32) vs lines expressing it (18) | 3.64× lower at baseline in the lines without KC6 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises MSR1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 3.85× lower at baseline in the lines without CDH12 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[CPED1]] | C | CPED1 activity raises MSR1's level | lines that do not express CPED1 (24) vs lines expressing it (26) | 3.77× lower at baseline in the lines without CPED1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: CCNYL2, LINC01885, ENSG00000291032; maybe low, not absent; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises MSR1's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 3.71× lower at baseline in the lines without CDH18 | 0.025 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[MIR137HG]] | C | MIR137HG activity raises MSR1's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 2.43× lower at baseline in the lines without MIR137HG | 0.039 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises MSR1's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 3.77× lower at baseline in the lines without TRPC4 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |
| [[LINC01684]] | C | LINC01684 activity raises MSR1's level | lines that do not express LINC01684 (30) vs lines expressing it (20) | 2.23× lower at baseline in the lines without LINC01684 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IRAG2, COL3A1, LINC01592; maybe low, not absent; co-absent with the target |
| [[IGSF1]] | C | IGSF1 activity raises MSR1's level | lines that do not express IGSF1 (33) vs lines expressing it (17) | 3.06× lower at baseline in the lines without IGSF1 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01885, ZNF208, ENSG00000233358; co-absent with the target |
| [[LINC00383]] | C | LINC00383 activity raises MSR1's level | lines that do not express LINC00383 (39) vs lines expressing it (11) | 4.15× lower at baseline in the lines without LINC00383 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000259639, LINC01425, ENSG00000285751; co-absent with the target |
| [[LINC01687]] | C | LINC01687 activity raises MSR1's level | lines that do not express LINC01687 (31) vs lines expressing it (19) | 3.61× lower at baseline in the lines without LINC01687 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC02616, TPTE; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02438]] | C | MSR1 activity raises LINC02438's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 8.87× lower at baseline in the lines without MSR1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[CDH18]] | C | MSR1 activity raises CDH18's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.70× lower at baseline in the lines without MSR1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[LINC02377]] | C | MSR1 activity raises LINC02377's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 6.29× lower at baseline in the lines without MSR1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[LINC01687]] | C | MSR1 activity raises LINC01687's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 5.84× lower at baseline in the lines without MSR1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[NPFFR2]] | C | MSR1 activity raises NPFFR2's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.89× lower at baseline in the lines without MSR1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[NTNG1]] | C | MSR1 activity raises NTNG1's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 4.73× lower at baseline in the lines without MSR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[FSTL5]] | C | MSR1 activity raises FSTL5's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 5.06× lower at baseline in the lines without MSR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[TOX]] | C | MSR1 activity raises TOX's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.49× lower at baseline in the lines without MSR1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[LINC00383]] | C | MSR1 activity raises LINC00383's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 1.86× lower at baseline in the lines without MSR1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[NETO1]] | C | MSR1 activity raises NETO1's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.24× lower at baseline in the lines without MSR1 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[CSMD3]] | C | MSR1 activity raises CSMD3's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 2.92× lower at baseline in the lines without MSR1 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |
| [[LINC01695]] | C | MSR1 activity raises LINC01695's level | lines that do not express MSR1 (36) vs lines expressing it (14) | 3.09× lower at baseline in the lines without MSR1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC02438, SAMMSON, ENSG00000286523; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.701). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.1, 27.0); signed map (39.2, 27.7). **Vector** length 41.8, 13.6% of its response variance represented; |z| ≥ 3 in 307 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +14.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +8.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | macrophage scavenger receptor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:16,107,878-16,567,490 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SCARA1, CD204, SR-AI, SR-AII, SR-AIII, SR-A |
| Gene groups (HGNC) | CD molecules; Scavenger receptors; Scavenger receptor cysteine rich domain containing |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 3 pathways, smallest: Scavenging by Class A Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P21757](https://www.uniprot.org/uniprotkb/P21757) (Macrophage scavenger receptor types I and II):

> Membrane receptor that mediates the binding, endocytosis and phagocytosis of a broad range of ligands. Recognizes and internalizes modified forms of low-density lipoproteins including acetylated LDL (AcLDL) and oxidized LDL (OxLDL), thereby promoting cholesterol uptake and contributing to foam cell formation during atherogenesis. Binds various pathogen-associated and damage-associated molecules, including bacterial cell wall components, apoptotic cell debris and polyanionic ligands, supporting …

**Summary**, from NCBI Gene [4481](https://www.ncbi.nlm.nih.gov/gene/4481):

> This gene encodes the class A macrophage scavenger receptors, which include three different types (1, 2, 3) generated by alternative splicing of this gene. These receptors or isoforms are macrophage-specific trimeric integral membrane glycoproteins and have been implicated in many macrophage-associated physiological and pathological processes including atherosclerosis, Alzheimer's disease, and host defense. The isoforms type 1 and type 2 are functional receptors and are able to mediate the …

**Accessions** — [HGNC:7376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7376) · Entrez [4481](https://www.ncbi.nlm.nih.gov/gene/4481) · UniProt [P21757](https://www.uniprot.org/uniprotkb/P21757) · Ensembl [ENSG00000038945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000038945)

## Data

Gene col 457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 457); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 457]; `tensor/DDL_lfc|DDL_z.npy` [457]; `embed/gene_vectors.npy` [457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 457 or target_col == 457). Every well: [[MSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
