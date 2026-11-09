---
symbol: "KRT20"
type: "gene"
col: 10105
ensembl_id: "ENSG00000171431"
name: "keratin 20"
location: "17q21.2"
module: 44
arm: "+"
pooled_cpm: 26.23
n_lines_expressing: 4
n_dd_up: 3
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 31
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# KRT20

*keratin 20* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.09× (z +8.8, q 1e-15, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.173×, SW1417 0.314×); [[Digitoxin (drug)]] 5 µM in 2 lines (HT-29 0.128×, SW1417 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.220×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST14]] (+0.73, fdr 7e-06), [[TM4SF4]] (+0.73, fdr 7e-06), [[CLIC5]] (+0.72, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[GABRP]] → it (grade C ⚠); 31 go from it, the strongest it → [[GABRP]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10105.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +8.8 | 1e-15 | 1/2 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.09×** | +8.4 | 9e-15 | 1/2 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.90×** | +6.1 | 2e-07 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.78× | +3.3 | 0.11 | 0/2 | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.72× | +3.3 | 0.11 | 0/2 | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.44× | +3.2 | 0.11 | 1/2 (SW1417) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.43× | +3.2 | 0.11 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10105.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HT-29 0.173×, SW1417 0.314×); [[Digitoxin (drug)]] 5 µM in 2 lines (HT-29 0.128×, SW1417 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (HT-29 0.220×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.588× | -3.3 | 0.41 | 0/2 | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.572× | -3.2 | 0.41 | 0/2 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10105. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 784 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -11.3) |
| [[SW1417 (line)]] | alt | 293 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.2) |
| [[A-172 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.55 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.22 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.51 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.02 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10105), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST14]] | +0.73 | +0.62 / +0.69 | both halves | 7e-06 | pathway: Formation of the cornified envelope |
| [[TM4SF4]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.72 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[TMEM30B]] | +0.70 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[HEPH]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[MUC13]] | +0.69 | +0.58 / +0.71 | both halves | 7e-06 | STRING 473 |
| [[LINC01559]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[CLDN3]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 | STRING 466 |
| [[BCAS1]] | +0.65 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 0, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRP]] | C | GABRP activity raises KRT20's level | lines that do not express GABRP (44) vs lines expressing it (6) | 4.39× lower at baseline in the lines without GABRP | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises KRT20's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.87× lower at baseline in the lines without TNFRSF14-AS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[BCAS1]] | C | BCAS1 activity raises KRT20's level | lines that do not express BCAS1 (32) vs lines expressing it (18) | 2.43× lower at baseline in the lines without BCAS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: SLC6A14, AGR3, LYZ; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises KRT20's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 3.34× lower at baseline in the lines without GCNT3 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises KRT20's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.29× lower at baseline in the lines without STEAP4 | 0.079 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[UCA1]] | C | UCA1 activity raises KRT20's level | lines that do not express UCA1 (37) vs lines expressing it (13) | 2.84× lower at baseline in the lines without UCA1 | 0.080 | ⚠ within organs, on part of the lines; also absent: TM4SF4, AGR3, LYZ; co-absent with the target |
| [[MUC16]] | C | MUC16 activity raises KRT20's level | lines that do not express MUC16 (38) vs lines expressing it (12) | 3.02× lower at baseline in the lines without MUC16 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSDMC, S100A9, STEAP4; co-absent with the target |
| [[MUC13]] | C | MUC13 activity raises KRT20's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.97× lower at baseline in the lines without MUC13 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[LGALS4]] | C | LGALS4 activity raises KRT20's level | lines that do not express LGALS4 (39) vs lines expressing it (11) | 3.48× lower at baseline in the lines without LGALS4 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; maybe low, not absent; co-absent with the target |
| [[APOH]] | C | APOH activity raises KRT20's level | lines that do not express APOH (41) vs lines expressing it (9) | 2.85× lower at baseline in the lines without APOH | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GABRP]] | C | KRT20 activity raises GABRP's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 1.43× lower at baseline in the lines without KRT20 | 0.001 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[APOH]] | C | KRT20 activity raises APOH's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.13× lower at baseline in the lines without KRT20 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[MGAM2]] | C | KRT20 activity raises MGAM2's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.86× lower at baseline in the lines without KRT20 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[EPS8L1]] | C | KRT20 activity raises EPS8L1's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 5.77× lower at baseline in the lines without KRT20 | 0.009 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10 |
| [[SYNPR-AS1]] | C | KRT20 activity raises SYNPR-AS1's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.43× lower at baseline in the lines without KRT20 | 0.011 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[MUC16]] | C | KRT20 activity raises MUC16's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 11.58× lower at baseline in the lines without KRT20 | 0.012 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[TM4SF4]] | C | KRT20 activity raises TM4SF4's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.84× lower at baseline in the lines without KRT20 | 0.020 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[MUC4]] | C | KRT20 activity raises MUC4's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 2.28× lower at baseline in the lines without KRT20 | 0.032 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[BCAS1]] | C | KRT20 activity raises BCAS1's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 6.05× lower at baseline in the lines without KRT20 | 0.032 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[TSPAN1]] | C | KRT20 activity raises TSPAN1's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.87× lower at baseline in the lines without KRT20 | 0.032 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[STEAP4]] | C | KRT20 activity raises STEAP4's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 10.00× lower at baseline in the lines without KRT20 | 0.035 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[MYH14]] | C | KRT20 activity raises MYH14's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 7.59× lower at baseline in the lines without KRT20 | 0.041 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.620). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.6, 53.4); signed map (61.5, 5.6). **Vector** length 16.8, 12.7% of its response variance represented; |z| ≥ 3 in 39 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.52 to 4); *Aspirin ADME* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.9 | +6.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.8 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.8 | +8.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.5 | +8.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +0.5 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.4 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.3 | +1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +0.3 | +2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.3 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.4 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.3 | -1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | +0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.3 | -2.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.3 | +0.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.3 | -1.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.3 | -2.7 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -0.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | keratin 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,875,889-40,885,242 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CK20, K20, MGC35423 |
| Gene groups (HGNC) | Keratins, type I |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [P35900](https://www.uniprot.org/uniprotkb/P35900) (Keratin, type I cytoskeletal 20):

> Plays a significant role in maintaining keratin filament organization in intestinal epithelia. When phosphorylated, plays a role in the secretion of mucin in the small intestine (By similarity).

**Summary**, from NCBI Gene [54474](https://www.ncbi.nlm.nih.gov/gene/54474):

> The protein encoded by this gene is a member of the keratin family. The keratins are intermediate filament proteins responsible for the structural integrity of epithelial cells and are subdivided into cytokeratins and hair keratins. The type I cytokeratins consist of acidic proteins which are arranged in pairs of heterotypic keratin chains. This cytokeratin is a major cellular protein of mature enterocytes and goblet cells and is specifically expressed in the gastric and intestinal mucosa. The …

**Accessions** — [HGNC:20412](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20412) · Entrez [54474](https://www.ncbi.nlm.nih.gov/gene/54474) · UniProt [P35900](https://www.uniprot.org/uniprotkb/P35900) · Ensembl [ENSG00000171431](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171431)

## Data

Gene col 10105: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10105); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10105, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10105]; `tensor/DDL_lfc|DDL_z.npy` [10105]; `embed/gene_vectors.npy` [10105]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10105 or target_col == 10105). Every well: [[KRT20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRT20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
