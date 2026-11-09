---
symbol: "GRIN2B"
type: "gene"
col: 15761
ensembl_id: "ENSG00000273079"
name: "glutamate ionotropic receptor NMDA type subunit 2B"
location: "12p13.1"
module: 55
arm: "+"
pooled_cpm: 42.09
n_lines_expressing: 10
n_dd_up: 12
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 27
direction_downstream: 24
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# GRIN2B

*glutamate ionotropic receptor NMDA type subunit 2B* — 12p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.36× (z +12.7, q 3e-34, up in 1 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.644× (z -4.6, q 0.002, down in 6 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0452×, LS 180 0.216×, LoVo 0.226×, A549 0.262×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.136×, COLO 205 0.156×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.167×, COLO 205 0.170×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.123×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF4A]] (+0.78, fdr 7e-06), [[GPA33]] (+0.68, fdr 1e-05), [[PIK3AP1]] (+0.65, fdr 2e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[PCK1]] → it (grade C ⚠); 24 go from it, the strongest it → [[ABHD12B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15761.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +12.7 | 3e-34 | 1/8 (C-33 A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.14×** | +12.0 | 2e-30 | 2/7 (LoVo, HCT15) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.5 | 3e-19 | 1/5 (LoVo) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.62×** | +9.3 | 1e-18 | 0/6 | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.61×** | +7.1 | 2e-10 | 1/8 (C-33 A) | top dose only | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.9 | 3e-07 | 2/8 (HCT15, C-33 A) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.5 | 4e-04 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.5 | 4e-04 | 1/8 (C-33 A) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.1 | 0.003 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.6 | 0.017 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.35×** | +3.2 | 0.078 | 1/8 (C-33 A) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.093 | 0/8 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15761.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (COLO 205 0.0452×, LS 180 0.216×, LoVo 0.226×, A549 0.262×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.136×, COLO 205 0.156×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LS 180 0.167×, COLO 205 0.170×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (LS 180 0.123×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.644×** | -4.6 | 0.002 | 6/8 (LS 180, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.747× | -3.1 | 0.64 | 2/8 (A549, A498) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15761. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 672 | 0 | 10 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -18.9) |
| [[COLO 205 (line)]] | alt | 244 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0452× (z -27.6) |
| [[A549 (line)]] | wt | 72.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -10.1) |
| [[LoVo (line)]] | wt | 54.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.2) |
| [[A-172 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.49 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.68 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.34 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.51 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.07 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.04 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.76 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.14 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.17 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.13 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.40 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 210 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15761), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4A]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GPA33]] | +0.68 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[PIK3AP1]] | +0.65 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[NPSR1]] | +0.63 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TPRXL]] | +0.62 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[CALB1]] | +0.62 | +0.59 / +0.57 | both halves | 9e-06 | STRING 418 |
| [[ILDR2]] | +0.62 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[IQGAP2]] | +0.61 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[CDH17]] | +0.60 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[PCK1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GPX2]] | +0.59 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[ACSL5]] | +0.59 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 0, C 27. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCK1]] | C | PCK1 activity raises GRIN2B's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 4.88× lower at baseline in the lines without PCK1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[A1CF]] | C | A1CF activity raises GRIN2B's level | lines that do not express A1CF (35) vs lines expressing it (15) | 5.28× lower at baseline in the lines without A1CF | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VIL1, NPSR1-AS1, MUC13; co-absent with the target |
| [[CALB1]] | C | CALB1 activity raises GRIN2B's level | lines that do not express CALB1 (42) vs lines expressing it (8) | 7.92× lower at baseline in the lines without CALB1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT5, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises GRIN2B's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.72× lower at baseline in the lines without ITIH2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises GRIN2B's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 5.06× lower at baseline in the lines without HNF4A | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises GRIN2B's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 3.34× lower at baseline in the lines without LINC02582 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises GRIN2B's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 4.13× lower at baseline in the lines without GPX2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[TNS4]] | C | TNS4 activity raises GRIN2B's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.14× lower at baseline in the lines without TNS4 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6; co-absent with the target |
| [[B3GNT3]] | C | B3GNT3 activity raises GRIN2B's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.98× lower at baseline in the lines without B3GNT3 | 0.034 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[C9orf152]] | C | C9orf152 activity raises GRIN2B's level | lines that do not express C9orf152 (32) vs lines expressing it (18) | 2.08× lower at baseline in the lines without C9orf152 | 0.039 | ⚠ within organs, on part of the lines; also absent: AGR3, MYO7B, KRT17; maybe low, not absent; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises GRIN2B's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 4.26× lower at baseline in the lines without LINC01559 | 0.040 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[DSCAML1]] | C | DSCAML1 activity raises GRIN2B's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.83× lower at baseline in the lines without DSCAML1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 1, C 23. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD12B]] | B | GRIN2B activity raises ABHD12B's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 2.82× lower at baseline in the lines without GRIN2B | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588 |
| [[HNF4A]] | C | GRIN2B activity raises HNF4A's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 6.69× lower at baseline in the lines without GRIN2B | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[FXYD2]] | C | GRIN2B activity raises FXYD2's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 1.97× lower at baseline in the lines without GRIN2B | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[ILDR2]] | C | GRIN2B activity raises ILDR2's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 3.56× lower at baseline in the lines without GRIN2B | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[TFF1]] | C | GRIN2B activity raises TFF1's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 2.31× lower at baseline in the lines without GRIN2B | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[IGFBP1]] | C | GRIN2B activity raises IGFBP1's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 1.63× lower at baseline in the lines without GRIN2B | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[TNS4]] | C | GRIN2B activity raises TNS4's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 5.01× lower at baseline in the lines without GRIN2B | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[A1CF]] | C | GRIN2B activity raises A1CF's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 2.88× lower at baseline in the lines without GRIN2B | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[IL20RA]] | C | GRIN2B activity raises IL20RA's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 4.73× lower at baseline in the lines without GRIN2B | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[SLC22A3]] | C | GRIN2B activity raises SLC22A3's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 4.31× lower at baseline in the lines without GRIN2B | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[NPSR1-AS1]] | C | GRIN2B activity raises NPSR1-AS1's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 3.62× lower at baseline in the lines without GRIN2B | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |
| [[LINC02582]] | C | GRIN2B activity raises LINC02582's level | lines that do not express GRIN2B (40) vs lines expressing it (10) | 3.45× lower at baseline in the lines without GRIN2B | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000237031, ENSG00000248588; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.3, 49.3); signed map (65.1, 9.2). **Vector** length 46.8, 22.2% of its response variance represented; |z| ≥ 3 in 242 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +12.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.9 | +2.7 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.1 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | glutamate ionotropic receptor NMDA type subunit 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.1 — chr12:13,437,942-13,982,002 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GluN2B, NR2B; previously NMDAR2B |
| Gene groups (HGNC) | Glutamate ionotropic receptor NMDA type subunits |
| Reactome | 27 pathways, smallest: Activated NTRK2 signals through FYN; MECP2 regulates neuronal receptors and channels; Ras activation upon Ca2+ influx through NMDA receptor |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13224](https://www.uniprot.org/uniprotkb/Q13224) (Glutamate receptor ionotropic, NMDA 2B):

> Component of N-methyl-D-aspartate (NMDA) receptors (NMDARs) that function as heterotetrameric, ligand-gated cation channels with high calcium permeability and voltage-dependent block by Mg(2+). Participates in synaptic plasticity for learning and memory formation by contributing to the long-term depression (LTD) of hippocampus membrane currents (By similarity). Channel activation requires binding of the neurotransmitter L-glutamate to the GluN2 subunit, glycine or D-serine binding to the GluN1 …

**Summary**, from NCBI Gene [2904](https://www.ncbi.nlm.nih.gov/gene/2904):

> This gene encodes a member of the N-methyl-D-aspartate (NMDA) receptor family within the ionotropic glutamate receptor superfamily. The encoded protein is a subunit of the NMDA receptor ion channel which acts as an agonist binding site for glutamate. The NMDA receptors mediate a slow calcium-permeable component of excitatory synaptic transmission in the central nervous system. The NMDA receptors are heterotetramers of seven genetically encoded, differentially expressed subunits including NR1 …

**Accessions** — [HGNC:4586](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4586) · Entrez [2904](https://www.ncbi.nlm.nih.gov/gene/2904) · UniProt [Q13224](https://www.uniprot.org/uniprotkb/Q13224) · Ensembl [ENSG00000273079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273079)

## Data

Gene col 15761: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15761); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15761, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15761]; `tensor/DDL_lfc|DDL_z.npy` [15761]; `embed/gene_vectors.npy` [15761]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15761 or target_col == 15761). Every well: [[GRIN2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRIN2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
