---
symbol: "DPP10"
type: "gene"
col: 10616
ensembl_id: "ENSG00000175497"
name: "dipeptidyl peptidase like 10"
location: "2q14.1"
module: 19
arm: "+"
pooled_cpm: 48.07
n_lines_expressing: 10
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 19
direction_downstream: 43
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# DPP10

*dipeptidyl peptidase like 10* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.97× (z +11.3, q 1e-26, up in 2 of 7 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0986×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.0835×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0952×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.196×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01035]] (+0.89, fdr 7e-06), [[LINC03000]] (+0.89, fdr 7e-06), [[SCARA5]] (+0.88, fdr 7e-06); moves opposite to [[ADRA2C]] (-0.47, fdr 5e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 43 go from it, the strongest it → [[KCNMB2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10616.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.97×** | +11.3 | 1e-26 | 2/7 (SW 900, BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.50×** | +8.8 | 4e-16 | 2/4 (SW 900, BT-474) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +8.5 | 5e-15 | 2/6 (SW 900, H4) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +4.3 | 0.002 | 2/9 (BT-474, SW 900) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +4.0 | 0.009 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.047 | 5/8 (SHP-77, BT-474, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.056 | 2/7 (H4, SW 900) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +3.4 | 0.056 | 1/7 (BT-474) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10616.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0986×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H460 0.0835×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0952×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.591× | -3.6 | 0.21 | 1/7 (SW 900) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.734× | -3.1 | 0.50 | 2/8 (AN3 CA, SW 900) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10616. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 809 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0986× (z -16.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0952× (z -12.1) |
| [[SHP-77 (line)]] | alt | 68.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.45× (z +8.6) | — |
| [[A-172 (line)]] | wt | 7.61 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.88 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 6.29 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.52 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.19 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.51 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.85 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.45 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.24 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.82 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.27 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.60 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.69 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.61 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 85.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.12 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.41 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.89 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.59 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.31 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 9.41 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10616), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01035]] | +0.89 | +0.78 / +0.93 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.89 | +0.82 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB11]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.85 | +0.75 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[GREM2]] | +0.83 | +0.76 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.83 | +0.72 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[PAX7]] | +0.82 | +0.76 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.80 | +0.74 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.80 | +0.72 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[SLC15A5]] | +0.79 | +0.80 / +0.71 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADRA2C]] | -0.47 | -0.45 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 1, C 18. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPP10's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GSG1L2]] | C | GSG1L2 activity raises DPP10's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 6.43× lower at baseline in the lines without GSG1L2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises DPP10's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.31× lower at baseline in the lines without LINC01508 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises DPP10's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 4.49× lower at baseline in the lines without GTF2I-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises DPP10's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 4.97× lower at baseline in the lines without SLC15A5 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises DPP10's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.57× lower at baseline in the lines without SCARA5 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises DPP10's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 5.05× lower at baseline in the lines without LINC03000 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[SPINK13]] | C | SPINK13 activity raises DPP10's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 4.63× lower at baseline in the lines without SPINK13 | 0.030 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises DPP10's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 3.02× lower at baseline in the lines without CTNND2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[LINC01035]] | C | LINC01035 activity raises DPP10's level | lines that do not express LINC01035 (43) vs lines expressing it (7) | 4.93× lower at baseline in the lines without LINC01035 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, CALCA, GSG1L2; co-absent with the target |
| [[CHL1]] | C | CHL1 activity raises DPP10's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 3.22× lower at baseline in the lines without CHL1 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168; co-absent with the target |
| [[PDE1A]] | C | PDE1A activity raises DPP10's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.73× lower at baseline in the lines without PDE1A | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 8, C 35. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNMB2]] | B | DPP10 activity raises KCNMB2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.38× lower at baseline in the lines without DPP10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[LSAMP]] | B | DPP10 activity raises LSAMP's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.96× lower at baseline in the lines without DPP10 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[RGS2]] | B | DPP10 activity raises RGS2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.41× lower at baseline in the lines without DPP10 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[RIMS1]] | B | DPP10 activity raises RIMS1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.36× lower at baseline in the lines without DPP10 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[PLAC4]] | B | DPP10 activity raises PLAC4's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.29× lower at baseline in the lines without DPP10 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[PART1]] | B | DPP10 activity raises PART1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 1.75× lower at baseline in the lines without DPP10 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[LINC00922]] | B | DPP10 activity raises LINC00922's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 1.53× lower at baseline in the lines without DPP10 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | B | DPP10 activity raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | lines that do not express DPP10 (40) vs lines expressing it (8) | the lines without DPP10: 0.87× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent |
| [[PAK3]] | C | DPP10 activity raises PAK3's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.05× lower at baseline in the lines without DPP10 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[CLDN10-AS1]] | C | DPP10 activity raises CLDN10-AS1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 3.51× lower at baseline in the lines without DPP10 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[SCUBE1]] | C | DPP10 activity raises SCUBE1's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.54× lower at baseline in the lines without DPP10 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[CTNND2]] | C | DPP10 activity raises CTNND2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.07× lower at baseline in the lines without DPP10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.2, 36.2); signed map (42.9, 44.2). **Vector** length 38.9, 20.1% of its response variance represented; |z| ≥ 3 in 143 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.51 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.3 | +4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +2.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.5 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.7 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | dipeptidyl peptidase like 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:114,442,299-115,845,780 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DPRP3, DPL2, DPPY |
| Gene groups (HGNC) | Potassium voltage-gated channel regulatory subunits; DASH family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N608](https://www.uniprot.org/uniprotkb/Q8N608) (Inactive dipeptidyl peptidase 10):

> Promotes cell surface expression of the potassium channel KCND2. Modulates the activity and gating characteristics of the potassium channel KCND2. Has no dipeptidyl aminopeptidase activity.

**Summary**, from NCBI Gene [57628](https://www.ncbi.nlm.nih.gov/gene/57628):

> This gene encodes a single-pass type II membrane protein that is a member of the S9B family in clan SC of the serine proteases. This protein has no detectable protease activity, most likely due to the absence of the conserved serine residue normally present in the catalytic domain of serine proteases. However, it does bind specific voltage-gated potassium channels and alters their expression and biophysical properties. Mutations in this gene have been associated with asthma. Alternate …

**Accessions** — [HGNC:20823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20823) · Entrez [57628](https://www.ncbi.nlm.nih.gov/gene/57628) · UniProt [Q8N608](https://www.uniprot.org/uniprotkb/Q8N608) · Ensembl [ENSG00000175497](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175497)

## Data

Gene col 10616: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10616); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10616, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10616]; `tensor/DDL_lfc|DDL_z.npy` [10616]; `embed/gene_vectors.npy` [10616]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10616 or target_col == 10616). Every well: [[DPP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
