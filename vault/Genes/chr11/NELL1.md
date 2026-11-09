---
symbol: "NELL1"
type: "gene"
col: 9217
ensembl_id: "ENSG00000165973"
name: "neural EGFL like 1"
location: "11p15.1"
module: 9
arm: "+"
pooled_cpm: 7.42
n_lines_expressing: 31
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 14
direction_downstream: 9
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# NELL1

*neural EGFL like 1* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.45× (z +17.6, q 0e+00, up in 13 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.160×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.325×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.389×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DGKB]] (+0.79, fdr 7e-06), [[LRFN2]] (+0.79, fdr 7e-06), [[MYT1L]] (+0.76, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[CALCA]] → it (grade B ⚠); 9 go from it, the strongest it → [[CHGB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9217.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.45×** | +17.6 | 0e+00 | 13/18 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.36×** | +10.1 | 2e-21 | 4/7 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +8.4 | 1e-14 | 8/19 (A549, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +7.8 | 7e-13 | 1/2 (C32) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +7.5 | 6e-12 | 1/2 (C32) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.88×** | +7.4 | 1e-11 | 10/25 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.39×** | +7.2 | 3e-11 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +5.6 | 2e-06 | 4/16 (SW480, SNU-423, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +5.5 | 2e-06 | 10/22 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +3.8 | 0.009 | 7/20 (NCI-H23, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.47× | +3.1 | 0.10 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9217.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.139×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.160×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.325×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.389×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -3.1 | 0.50 | 6/28 (SNU-1, NCI-H23, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.689× | -3.1 | 0.50 | 5/22 (SHP-77, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.697× | -3.0 | 0.50 | 1/26 (C-33 A) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9217. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 233 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 4.86 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 11.8× (z +11.1) | — |
| [[A549 (line)]] | wt | 4.82 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0510× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 1.92 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 13.2× (z +9.7) | — |
| [[SW480 (line)]] | alt | 3.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 80.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9217), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKB]] | +0.79 | +0.72 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LRFN2]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[MYT1L]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GRIA2]] | +0.75 | +0.64 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[GLRA3]] | +0.74 | +0.76 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[GRIK1]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[SRRM4]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[RIT2]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.72 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[LINC02197]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[UNC80]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[SYT4]] | +0.69 | +0.71 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCA]] | B | CALCA activity raises NELL1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 5.04× lower at baseline in the lines without CALCA | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[RIT2]] | B | RIT2 activity raises NELL1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.83× lower at baseline in the lines without RIT2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[SYT4]] | B | SYT4 activity raises NELL1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 3.82× lower at baseline in the lines without SYT4 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[KCNB2]] | B | KCNB2 activity raises NELL1's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 3.14× lower at baseline in the lines without KCNB2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent |
| [[FKBP9P1-1]] | B | FKBP9P1-1 activity raises NELL1's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 1.78× lower at baseline in the lines without FKBP9P1-1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent |
| [[CGA]] | B | CGA activity raises NELL1's level | lines that do not express CGA (44) vs lines expressing it (6) | 3.86× lower at baseline in the lines without CGA | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2 |
| [[CFI]] | B | CFI activity raises NELL1's level | lines that do not express CFI (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without CFI | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000285330, ENSG00000239268, RUNX1T1 |
| [[RUNX1T1]] | B | RUNX1T1 activity raises NELL1's level | lines that do not express RUNX1T1 (38) vs lines expressing it (12) | 1.91× lower at baseline in the lines without RUNX1T1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, ENSG00000232252, SYT4 |
| [[C2CD4A]] | B | C2CD4A activity raises NELL1's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 1.71× lower at baseline in the lines without C2CD4A | 0.086 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L |
| [[LRFN2]] | B | LRFN2 activity raises NELL1's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 2.33× lower at baseline in the lines without LRFN2 | 0.089 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent |
| [[LEF1]] | B | LEF1 activity raises NELL1's level | lines that do not express LEF1 (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without LEF1 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF521, LEF1-AS1, LAMA1 |
| [[LOXL4]] | B | LOXL4 activity raises NELL1's level | lines that do not express LOXL4 (30) vs lines expressing it (20) | 1.71× lower at baseline in the lines without LOXL4 | 0.097 | ⚠ within organs, on part of the lines; also absent: HSD17B2, BATF, TFF3 |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHGB]] | B | NELL1 activity raises CHGB's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 2.25× lower at baseline in the lines without NELL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent |
| [[DIRC3]] | B | NELL1 activity raises DIRC3's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 2.61× lower at baseline in the lines without NELL1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent |
| [[SEMA6D]] | B | NELL1 activity raises SEMA6D's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without NELL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent |
| [[NRG3]] | B | NELL1 activity raises NRG3's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without NELL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent |
| [[TMEM178B]] | C | NELL1 activity raises TMEM178B's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without NELL1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent; co-absent with the target |
| [[NELL2]] | C | NELL1 activity raises NELL2's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without NELL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent; co-absent with the target |
| [[CHRM3]] | C | NELL1 activity raises CHRM3's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 3.86× lower at baseline in the lines without NELL1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent; co-absent with the target |
| [[SNAP25]] | C | NELL1 activity raises SNAP25's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 3.25× lower at baseline in the lines without NELL1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent; co-absent with the target |
| [[KCNJ6]] | C | NELL1 activity raises KCNJ6's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without NELL1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.7, 36.7); signed map (44.2, 34.3). **Vector** length 42.3, 7.75% of its response variance represented; |z| ≥ 3 in 562 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.53 to 15).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +17.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +7.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +2.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -3.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.5 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | neural EGFL like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:20,669,551-21,575,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IDH3GL, FLJ45906 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92832](https://www.uniprot.org/uniprotkb/Q92832) (Protein kinase C-binding protein NELL1):

> Plays a role in the control of cell growth and differentiation. Promotes osteoblast cell differentiation and terminal mineralization.

**Summary**, from NCBI Gene [4745](https://www.ncbi.nlm.nih.gov/gene/4745):

> This gene encodes a cytoplasmic protein that contains epidermal growth factor (EGF)-like repeats. The encoded heterotrimeric protein may be involved in cell growth regulation and differentiation. A similar protein in rodents is involved in craniosynostosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2013]

**Accessions** — [HGNC:7750](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7750) · Entrez [4745](https://www.ncbi.nlm.nih.gov/gene/4745) · UniProt [Q92832](https://www.uniprot.org/uniprotkb/Q92832) · Ensembl [ENSG00000165973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165973)

## Data

Gene col 9217: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9217); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9217, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9217]; `tensor/DDL_lfc|DDL_z.npy` [9217]; `embed/gene_vectors.npy` [9217]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9217 or target_col == 9217). Every well: [[NELL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NELL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
