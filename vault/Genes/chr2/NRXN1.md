---
symbol: "NRXN1"
type: "gene"
col: 11064
ensembl_id: "ENSG00000179915"
name: "neurexin 1"
location: "2p16.3"
module: 9
arm: "+"
pooled_cpm: 12.86
n_lines_expressing: 31
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 14
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NRXN1

*neurexin 1* — 2p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.96× (z +31.4, q 0e+00, up in 18 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.284×, NCI-H1792 0.270×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.236×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.130×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.146×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.374×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNBD1]] (+0.77, fdr 7e-06), [[RALYL]] (+0.77, fdr 7e-06), [[GRIK1]] (+0.72, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[DACH1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.96×** | +31.4 | 0e+00 | 18/23 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **3.86×** | +14.5 | 6e-45 | 20/26 (LOX-IMVI, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +12.8 | 4e-35 | 21/27 (NCI-H460, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.15×** | +11.6 | 4e-29 | 15/23 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.85×** | +11.2 | 3e-27 | 7/15 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +9.8 | 9e-21 | 1/7 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +7.4 | 9e-12 | 3/9 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +7.2 | 3e-11 | 16/26 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.59×** | +7.0 | 1e-10 | 9/28 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.4 | 8e-09 | 5/22 (KATO III, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.6 | 1e-06 | 6/19 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.9 | 0.004 | 3/17 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.40×** | +3.5 | 0.023 | 9/25 (A-427, SK-MEL-2, …) | top dose only | composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.023 | 1/26 (A-172) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.031 | 5/26 (A-172, C32, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.048 | 4/27 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.063 | 2/25 (SK-MEL-2, LOX-IMVI) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.064 | 3/26 (A-172, HCT15, …) | inconsistent across doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.075 | 1/24 (HCT15) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SHP-77 0.284×, NCI-H1792 0.270×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.236×); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.130×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.146×); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.374×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 379 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -16.4) |
| [[A-172 (line)]] | wt | 4.28 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 43.9× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 3.31 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 4.08 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 12.9× (z +10.4) | — |
| [[C32 (line)]] | wt | 3.57 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 20.4× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 30.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +10.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -11.3) |
| [[A-427 (line)]] | wt | 3.25 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 11.1× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 7.12 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.67× (z +10.9) | — |
| [[KATO III (line)]] | alt | 3.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.26× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 4.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 8.05 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 9.23× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 72.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.3× (z +13.2) | — |
| [[A498 (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.12 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.98 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.89 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNBD1]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[RALYL]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 | pathway: Neuronal System; STRING 403 |
| [[GLRA3]] | +0.72 | +0.66 / +0.68 | both halves | 7e-06 | pathway: Neuronal System |
| [[VENTXP1]] | +0.71 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[UNC80]] | +0.71 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ESRRG]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[GPM6A]] | +0.69 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[SNTG1]] | +0.68 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[MYT1L]] | +0.67 | +0.68 / +0.63 | both halves | 7e-06 | STRING 501 |
| [[XIRP2]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.67 | +0.66 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 13, C 6. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NRXN1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.5% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ASCL1]] | B | ASCL1 activity raises NRXN1's level | lines that do not express ASCL1 (41) vs lines expressing it (9) | 4.22× lower at baseline in the lines without ASCL1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000232252, ENSG00000275016, SYT4 |
| [[SRRM4]] | B | SRRM4 activity raises NRXN1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 4.29× lower at baseline in the lines without SRRM4 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |
| [[KCNH7]] | B | KCNH7 activity raises NRXN1's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 2.71× lower at baseline in the lines without KCNH7 | 0.031 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |
| [[LINC01287]] | B | LINC01287 activity raises NRXN1's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 3.15× lower at baseline in the lines without LINC01287 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[CDH12]] | B | CDH12 activity raises NRXN1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.77× lower at baseline in the lines without CDH12 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[TOX]] | B | TOX activity raises NRXN1's level | lines that do not express TOX (30) vs lines expressing it (20) | 1.80× lower at baseline in the lines without TOX | 0.065 | ⚠ within organs, on part of the lines; also absent: CDH6, DKK3, MXRA5 |
| [[SCG3]] | B | SCG3 activity raises NRXN1's level | lines that do not express SCG3 (39) vs lines expressing it (11) | 2.88× lower at baseline in the lines without SCG3 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, PCSK1, CALCA |
| [[SNTG1]] | B | SNTG1 activity raises NRXN1's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.74× lower at baseline in the lines without SNTG1 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent |
| [[FSTL5]] | B | FSTL5 activity raises NRXN1's level | lines that do not express FSTL5 (34) vs lines expressing it (16) | 2.43× lower at baseline in the lines without FSTL5 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC02438, ENSG00000248973, COX7B2 |
| [[LINC01320]] | B | LINC01320 activity raises NRXN1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.52× lower at baseline in the lines without LINC01320 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[F11-AS1]] | B | F11-AS1 activity raises NRXN1's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 2.38× lower at baseline in the lines without F11-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 10, C 4. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DACH1]] | B | NRXN1 activity raises DACH1's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 2.53× lower at baseline in the lines without NRXN1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[MIR325HG]] | B | NRXN1 activity raises MIR325HG's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.57× lower at baseline in the lines without NRXN1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[B3GALT1]] | B | NRXN1 activity raises B3GALT1's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without NRXN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[MIR4300HG]] | B | NRXN1 activity raises MIR4300HG's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.46× lower at baseline in the lines without NRXN1 | 0.074 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[LINC02315]] | B | NRXN1 activity raises LINC02315's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without NRXN1 | 0.075 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[DOK5]] | B | NRXN1 activity raises DOK5's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without NRXN1 | 0.076 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[PRUNE2]] | B | NRXN1 activity raises PRUNE2's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without NRXN1 | 0.085 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[GRIA4]] | B | NRXN1 activity raises GRIA4's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without NRXN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[SEMA6D]] | B | NRXN1 activity raises SEMA6D's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without NRXN1 | 0.098 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[LINC01320]] | B | NRXN1 activity raises LINC01320's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 2.27× lower at baseline in the lines without NRXN1 | 0.099 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[LINC01885]] | C | NRXN1 activity raises LINC01885's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 3.16× lower at baseline in the lines without NRXN1 | 0.049 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent; co-absent with the target |
| [[MIR2052HG]] | C | NRXN1 activity raises MIR2052HG's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 2.51× lower at baseline in the lines without NRXN1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, 34.9); signed map (42.8, 32.8). **Vector** length 53.5, 10.6% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +31.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.2 | +7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +7.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +0.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.4 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | neurexin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.3 — chr2:49,918,503-51,225,575 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0578, Hs.22998 |
| Gene groups (HGNC) | Neurexins; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: Neurexins and neuroligins; Non-integrin membrane-ECM interactions; Protein-protein interactions at synapses |
| Matched by | ensembl_id |

**Function**, from UniProt [P58400](https://www.uniprot.org/uniprotkb/P58400) (Neurexin-1-beta):

> Neuronal cell surface protein involved in cell recognition and cell adhesion by forming intracellular junctions through binding to neuroligins (By similarity). Plays a role in formation of synaptic junctions (By similarity). Functions as part of a trans-synaptic complex by binding to cerebellins and postsynaptic GRID1. This interaction helps regulate the activity of NMDA and AMPA receptors at hippocampal synapses without affecting synapse formation. NRXN1B-CBLN2-GRID1 complex transduce …

**Summary**, from NCBI Gene [9378](https://www.ncbi.nlm.nih.gov/gene/9378):

> This gene encodes a single-pass type I membrane protein that belongs to the neurexin family. Neurexins are cell-surface receptors that bind neuroligins to form Ca(2+)-dependent neurexin/neuroligin complexes at synapses in the central nervous system. This complex is required for efficient neurotransmission and is involved in the formation of synaptic contacts. Three members of this gene family have been studied in detail and are estimated to generate over 3,000 variants through the use of two …

**Accessions** — [HGNC:8008](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8008) · Entrez [9378](https://www.ncbi.nlm.nih.gov/gene/9378) · UniProt [P58400](https://www.uniprot.org/uniprotkb/P58400) · Ensembl [ENSG00000179915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179915)

## Data

Gene col 11064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11064); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11064]; `tensor/DDL_lfc|DDL_z.npy` [11064]; `embed/gene_vectors.npy` [11064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11064 or target_col == 11064). Every well: [[NRXN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRXN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
