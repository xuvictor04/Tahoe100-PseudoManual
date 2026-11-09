---
symbol: "GASK1B-AS1"
type: "gene"
col: 14538
ensembl_id: "ENSG00000248429"
name: "GASK1B antisense RNA 1"
location: "4q32.1"
module: 19
arm: "+"
pooled_cpm: 4.98
n_lines_expressing: 13
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GASK1B-AS1

*GASK1B antisense RNA 1* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.94× (z +10.5, q 7e-23, up in 4 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.549× (z -4.1, q 0.022, down in 6 of 11 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.150×, NCI-H460 0.180×; ⚠ cell-cycle shift, explains ~31% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (NCI-H460 0.117×, HepG2/C3A 0.0479×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0546×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.103×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.105×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GASK1B]] (+0.80, fdr 7e-06, ⚠ same locus), [[PDE1A]] (+0.66, fdr 1e-05), [[KCNK2]] (+0.65, fdr 1e-04), [[CTNND2]] (+0.64, fdr 4e-05); moves opposite to [[CD99P1-1]] (-0.45, fdr 2e-04), [[CASP9]] (-0.44, fdr 0.004, ⚠ not reproduced).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[HOXA10-AS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14538.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +10.5 | 7e-23 | 4/10 (NCI-H460, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.77×** | +9.9 | 1e-20 | 1/5 (A-172) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.44×** | +9.8 | 1e-20 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.00×** | +9.5 | 3e-19 | 2/8 (HT-29, A-172) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.77×** | +5.5 | 4e-06 | 5/11 (NCI-H460, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +5.4 | 7e-06 | 6/11 (A-172, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.13×** | +5.2 | 2e-05 | 4/10 (A-172, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +5.0 | 4e-05 | 3/10 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.06×** | +4.8 | 1e-04 | 4/11 (NCI-H460, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.05×** | +4.0 | 0.004 | 1/3 (A-172) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.74×** | +3.8 | 0.007 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.70×** | +3.7 | 0.012 | 1/11 (HepG2/C3A) | top dose only | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.10×** | +3.6 | 0.012 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.6 | 0.012 | 2/5 (A-172, NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.97×** | +3.3 | 0.033 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Brimonidine (drug)]] 0.5 µM |  | **1.60×** | +3.2 | 0.043 | 3/11 (BT-474, C-33 A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.083 | 3/10 (A-427, BT-474, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Decitabine (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.083 | 0/11 | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.54×** | +3.0 | 0.083 | 3/11 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14538.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 2 lines (A-427 0.150×, NCI-H460 0.180×; ⚠ cell-cycle shift, explains ~31% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 2 lines (NCI-H460 0.117×, HepG2/C3A 0.0479×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0546×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.103×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.549×** | -4.1 | 0.022 | 6/11 (NCI-H460, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | 0.731× | -3.0 | 0.54 | 3/11 (A-427, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.4 | 2 | 10 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0546× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.05 µM 0.103× (z -11.5) |
| [[A-427 (line)]] | wt | 86.6 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.0) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HepG2_C3A (line)]] | wt | 10.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0479× (z -9.5) |
| [[NCI-H661 (line)]] | alt | 88.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -8.9) |
| [[A-172 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.429 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.943 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.463 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.660 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.543 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.909 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.415 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.482 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.659 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.950 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.616 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.445 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.800 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.458 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GASK1B]] | +0.80 | +0.82 / +0.70 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[PDE1A]] | +0.66 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.65 | +0.70 / +0.36 | both halves | 1e-04 |  |
| [[CTNND2]] | +0.64 | +0.71 / +0.42 | both halves | 4e-05 |  |
| [[MIR99AHG]] | +0.62 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[NLGN4Y]] | +0.62 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[NCKAP5-AS2]] | +0.62 | +0.62 / +0.48 | both halves | 2e-05 | same gene group |
| [[CHL1]] | +0.61 | +0.66 / +0.34 | both halves | 1e-04 |  |
| [[SPINK13]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.60 | +0.65 / +0.36 | both halves | 1e-04 |  |
| [[PAX7]] | +0.60 | +0.66 / +0.37 | both halves | 7e-05 |  |
| [[P3H2-AS1]] | +0.59 | +0.53 / +0.41 | both halves | 4e-05 | same gene group |
| [[COL4A5]] | +0.59 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD99P1-1]] | -0.45 | -0.37 / -0.29 | both halves | 2e-04 |  |
| [[CASP9]] | -0.44 | -0.44 / -0.06 | ⚠ not reproduced | 0.004 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GASK1B-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[GASK1B]] | C | GASK1B activity raises GASK1B-AS1's level | lines that do not express GASK1B (34) vs lines expressing it (16) | 4.72× lower at baseline in the lines without GASK1B | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B-AS1, HCN1, ENSG00000238054; co-absent with the target |
| [[MIR99AHG]] | C | MIR99AHG activity raises GASK1B-AS1's level | lines that do not express MIR99AHG (37) vs lines expressing it (13) | 3.70× lower at baseline in the lines without MIR99AHG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNH5, GCG, LINC02099; co-absent with the target |
| [[TTTY10]] | C | TTTY10 activity raises GASK1B-AS1's level | lines that do not express TTTY10 (31) vs lines expressing it (19) | 2.50× lower at baseline in the lines without TTTY10 | 0.047 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ANOS2P, KDM5D, UTY; co-absent with the target |
| [[LINC02643]] | C | LINC02643 activity raises GASK1B-AS1's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 2.97× lower at baseline in the lines without LINC02643 | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA10-AS]] | B | GASK1B-AS1 activity raises HOXA10-AS's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 1.23× lower at baseline in the lines without GASK1B-AS1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB |
| [[LINC02269]] | B | GASK1B-AS1 activity raises LINC02269's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 1.48× lower at baseline in the lines without GASK1B-AS1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB |
| [[GASK1B]] | C | GASK1B-AS1 activity raises GASK1B's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 10.35× lower at baseline in the lines without GASK1B-AS1 | 3e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |
| [[CADM2]] | C | GASK1B-AS1 activity raises CADM2's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 4.80× lower at baseline in the lines without GASK1B-AS1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |
| [[HERC2P3-1]] | C | GASK1B-AS1 activity raises HERC2P3-1's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 2.94× lower at baseline in the lines without GASK1B-AS1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |
| [[CDH19]] | C | GASK1B-AS1 activity raises CDH19's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without GASK1B-AS1 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |
| [[CHL1]] | C | GASK1B-AS1 activity raises CHL1's level | lines that do not express GASK1B-AS1 (37) vs lines expressing it (13) | 2.02× lower at baseline in the lines without GASK1B-AS1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GASK1B, GCG, NPPB; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.634). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.0, 37.1); signed map (43.9, 42.9). **Vector** length 38.4, 12.0% of its response variance represented; |z| ≥ 3 in 278 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.6 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -1.4 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -1.3 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.2 | -1.3 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | GASK1B antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q32.1 — chr4:158,170,752-158,202,877 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously FAM198B-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53132](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53132) · Entrez [285505](https://www.ncbi.nlm.nih.gov/gene/285505) · Ensembl [ENSG00000248429](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248429)

## Data

Gene col 14538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14538); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14538]; `tensor/DDL_lfc|DDL_z.npy` [14538]; `embed/gene_vectors.npy` [14538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14538 or target_col == 14538). Every well: [[GASK1B-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GASK1B-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
