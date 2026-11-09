---
symbol: "APOH"
type: "gene"
col: 1670
ensembl_id: "ENSG00000091583"
name: "apolipoprotein H"
location: "17q24.2"
module: 44
arm: "+"
pooled_cpm: 3.52
n_lines_expressing: 9
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 15
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# APOH

*apolipoprotein H* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 13.9× (z +16.4, q 0e+00, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.39× (z +14.8, q 0e+00, up in 2 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.269×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.183×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (66 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 34 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSG]] (+0.57, fdr 7e-06), [[TM4SF4]] (+0.56, fdr 1e-04), [[KRT20]] (+0.54, fdr 5e-04); moves opposite to [[RAI14]] (-0.42, fdr 4e-04), [[PNPT1]] (-0.39, fdr 2e-04), [[DCBLD2]] (-0.38, fdr 0.002, ⚠ not reproduced), [[CHROMR]] (-0.37, fdr 4e-04).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[C4orf19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1670.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **13.9×** | +16.4 | 0e+00 | 1/2 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.39×** | +14.8 | 0e+00 | 2/3 (HepG2/C3A, A549) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.5×** | +14.5 | 1e-45 | 1/2 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **7.12×** | +11.3 | 3e-27 | 1/2 (HepG2/C3A) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +6.4 | 2e-08 | 1/2 (HT-29) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.04×** | +6.2 | 4e-08 | 1/3 (HT-29) | top dose only | cell-cycle shift (explains ~21% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.36×** | +5.1 | 3e-05 | 1/2 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.49×** | +4.9 | 8e-05 | 1/2 (HepG2/C3A) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +4.6 | 3e-04 | 2/4 (HepG2/C3A, A549) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.68×** | +4.5 | 3e-04 | 1/4 (HepG2/C3A) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +4.5 | 3e-04 | 2/4 (HepG2/C3A, A549) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.34×** | +3.8 | 0.008 | 0/2 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.7 | 0.009 | 1/2 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~12% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.13×** | +3.3 | 0.034 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +3.3 | 0.034 | 0/3 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +3.1 | 0.060 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.66×** | +3.1 | 0.060 | 1/4 (A549) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1670.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (HepG2/C3A 0.269×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.183×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 0.05 µM |  | 0.577× | -3.3 | 0.41 | 1/4 (A549) | inconsistent across doses | position effect removed |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.602× | -3.2 | 0.41 | 1/4 (A549) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1670. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 144 | 3 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +11.9) | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.5) |
| [[A-172 (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.820 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.819 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.827 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.631 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.523 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.677 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.551 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.474 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.568 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1670), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 32 of them with an alert (⚠; 32 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSG]] | +0.57 | +0.66 / +0.74 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 957 |
| [[TM4SF4]] | +0.56 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[KRT20]] | +0.54 | +0.23 / +0.57 | both halves | 5e-04 |  |
| [[ALB]] | +0.54 | +0.60 / +0.70 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation; STRING 933 |
| [[AGR2]] | +0.53 | +0.27 / +0.49 | both halves | 3e-04 |  |
| [[PIP5K1B]] | +0.51 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[FXYD3]] | +0.50 | +0.25 / +0.49 | both halves | 4e-04 |  |
| [[APOA1]] | +0.50 | +0.59 / +0.68 | both halves | 7e-06 | same gene group; pathway: Platelet activation, signaling and aggregation; STRING 985 |
| [[CLDN3]] | +0.49 | +0.24 / +0.47 | both halves | 4e-04 |  |
| [[TSPAN1]] | +0.49 | +0.27 / +0.39 | both halves | 3e-04 |  |
| [[SLC44A4]] | +0.47 | +0.28 / +0.54 | both halves | 3e-04 |  |
| [[LGALS4]] | +0.47 | +0.29 / +0.48 | both halves | 2e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAI14]] | -0.42 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[PNPT1]] | -0.39 | -0.29 / -0.30 | both halves | 2e-04 |  |
| [[DCBLD2]] | -0.38 | -0.14 / -0.30 | ⚠ not reproduced | 0.002 |  |
| [[CHROMR]] | -0.37 | -0.24 / -0.28 | both halves | 4e-04 |  |
| [[INO80E]] | -0.37 | -0.27 / -0.23 | both halves | 5e-04 |  |
| [[NUDCD1]] | -0.36 | -0.20 / -0.29 | ⚠ not reproduced | 8e-04 |  |
| [[SLC25A28]] | -0.36 | -0.31 / -0.24 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers APOH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KRT20]] | C | KRT20 activity raises APOH's level | lines that do not express KRT20 (46) vs lines expressing it (4) | 4.13× lower at baseline in the lines without KRT20 | 0.005 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: HEPHL1, APOB, BMP10; co-absent with the target |
| [[FGFR2]] | C | FGFR2 activity raises APOH's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 2.48× lower at baseline in the lines without FGFR2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[AMBP]] | C | AMBP activity raises APOH's level | lines that do not express AMBP (41) vs lines expressing it (9) | 3.39× lower at baseline in the lines without AMBP | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, CALCA, APOA2; co-absent with the target |
| [[AGR3]] | C | AGR3 activity raises APOH's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 1.98× lower at baseline in the lines without AGR3 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises APOH's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 1.79× lower at baseline in the lines without AKR1B10 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[MUC17]] | C | MUC17 activity raises APOH's level | lines that do not express MUC17 (44) vs lines expressing it (6) | 2.36× lower at baseline in the lines without MUC17 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, FGFR2, NPSR1; co-absent with the target |
| [[TM4SF4]] | C | TM4SF4 activity raises APOH's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 1.97× lower at baseline in the lines without TM4SF4 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 1, C 14. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C4orf19]] | B | APOH activity weakens C4orf19's drug response | lines that do not express APOH (29) vs lines expressing it (6) | (z diff -2.26); strongest at Dinaciclib 5 µM: 1.15x vs 0.25x (z diff -9.6) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; target measured in part of the lines; the reference differs; artifact flags |
| [[BCAS1]] | C | APOH activity raises BCAS1's level | lines that do not express APOH (41) vs lines expressing it (9) | 3.37× lower at baseline in the lines without APOH | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[GCNT3]] | C | APOH activity raises GCNT3's level | lines that do not express APOH (41) vs lines expressing it (9) | 3.61× lower at baseline in the lines without APOH | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[TRIM31]] | C | APOH activity raises TRIM31's level | lines that do not express APOH (41) vs lines expressing it (9) | 2.05× lower at baseline in the lines without APOH | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[UGT1A9]] | C | APOH activity raises UGT1A9's level | lines that do not express APOH (41) vs lines expressing it (9) | 1.73× lower at baseline in the lines without APOH | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[SULF2]] | C | APOH activity raises SULF2's level | lines that do not express APOH (41) vs lines expressing it (9) | 1.53× lower at baseline in the lines without APOH | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[AGR3]] | C | APOH activity raises AGR3's level | lines that do not express APOH (41) vs lines expressing it (9) | 1.60× lower at baseline in the lines without APOH | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[TM4SF4]] | C | APOH activity raises TM4SF4's level | lines that do not express APOH (41) vs lines expressing it (9) | 2.36× lower at baseline in the lines without APOH | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[ATP10B]] | C | APOH activity raises ATP10B's level | lines that do not express APOH (41) vs lines expressing it (9) | 2.68× lower at baseline in the lines without APOH | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[SLC44A4]] | C | APOH activity raises SLC44A4's level | lines that do not express APOH (41) vs lines expressing it (9) | 2.54× lower at baseline in the lines without APOH | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[IGFL2-AS1]] | C | APOH activity raises IGFL2-AS1's level | lines that do not express APOH (41) vs lines expressing it (9) | 2.53× lower at baseline in the lines without APOH | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |
| [[PIP5K1B]] | C | APOH activity raises PIP5K1B's level | lines that do not express APOH (41) vs lines expressing it (9) | 2.54× lower at baseline in the lines without APOH | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITIH2, AFP, APOA2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.487). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.7, 59.0); signed map (62.4, 3.2). **Vector** length 9.21, 2.30% of its response variance represented; |z| ≥ 3 in 93 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.7 | +14.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.5 | +1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.5 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.4 | +11.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.3 | +2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.3 | +1.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.3 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.2 | +0.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.4 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.3 | -0.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.2 | -1.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.2 | -0.0 |
|  | [[EX229 (drug)]] 5 µM |  | -0.2 | +1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.2 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.2 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q24.2 — chr17:66,212,033-66,256,525 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BG; previously B2G1 |
| Gene groups (HGNC) | Apolipoproteins; Sushi domain containing |
| Hallmark sets | ANGIOGENESIS |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [P02749](https://www.uniprot.org/uniprotkb/P02749) (Beta-2-glycoprotein 1):

> Binds to various kinds of negatively charged substances such as heparin, phospholipids, and dextran sulfate. May prevent activation of the intrinsic blood coagulation cascade by binding to phospholipids on the surface of damaged cells.

**Summary**, from NCBI Gene [350](https://www.ncbi.nlm.nih.gov/gene/350):

> Apolipoprotein H, also known as beta-2-glycoprotein I, is a component of circulating plasma lipoproteins. It has been implicated in a variety of physiologic pathways including lipoprotein metabolism, coagulation, hemostasis, and the production of antiphospholipid autoantibodies. APOH may be a required cofactor for anionic phospholipid binding by the antiphospholipid autoantibodies found in sera of many patients with lupus and primary antiphospholipid syndrome (APS). The anti-beta (2) …

**Accessions** — [HGNC:616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:616) · Entrez [350](https://www.ncbi.nlm.nih.gov/gene/350) · UniProt [P02749](https://www.uniprot.org/uniprotkb/P02749) · Ensembl [ENSG00000091583](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091583)

## Data

Gene col 1670: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1670); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1670, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1670]; `tensor/DDL_lfc|DDL_z.npy` [1670]; `embed/gene_vectors.npy` [1670]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1670 or target_col == 1670). Every well: [[APOH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
