---
symbol: "AKR1C2"
type: "gene"
col: 7543
ensembl_id: "ENSG00000151632"
name: "aldo-keto reductase family 1 member C2"
location: "10p15.1"
module: 117
arm: "+"
pooled_cpm: 25.23
n_lines_expressing: 16
n_dd_up: 30
n_dd_down: 1
n_dd_up_clean: 23
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 11
direction_downstream: 16
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# AKR1C2

*aldo-keto reductase family 1 member C2* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.02× (z +14.6, q 3e-45, up in 11 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.07× (z +5.9, q 5e-07, up in 6 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.715× (z -3.9, q 0.058, down in 11 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0760×, AN3 CA 0.0625×, COLO 205 0.235×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AN3 CA 0.199×, NCI-H460 0.273×, SHP-77 0.284×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.152×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.202×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1C1]] (+0.81, fdr 7e-06, ⚠ same locus), [[AKR1C3]] (+0.79, fdr 7e-06, ⚠ same locus), [[GSG1L2]] (+0.57, fdr 1e-05), [[LINC00824]] (+0.57, fdr 1e-05), [[PIR]] (+0.57, fdr 1e-05); moves opposite to [[RAPGEF3]] (-0.48, fdr 7e-05), [[ZNF275]] (-0.48, fdr 9e-05), [[DPY19L3]] (-0.46, fdr 8e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MGST1]] → it (grade B ⚠); 16 go from it, the strongest it → [[NMRAL2P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7543.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.02×** | +14.6 | 3e-45 | 11/15 (A498, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.36×** | +9.0 | 4e-17 | 9/12 (SW480, A498, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.12×** | +8.5 | 3e-15 | 8/13 (A549, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.07×** | +5.9 | 5e-07 | 6/14 (COLO 205, AsPC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.23×** | +4.6 | 4e-04 | 8/14 (A498, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.5 | 7e-04 | 9/14 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.72×** | +4.4 | 0.001 | 11/15 (A549, NCI-H2030, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.56×** | +4.1 | 0.002 | 11/14 (A549, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.59×** | +3.7 | 0.011 | 5/14 (COLO 205, HepG2/C3A, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.65×** | +3.7 | 0.011 | 10/14 (A549, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.6 | 0.015 | 1/15 (COLO 205) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.56×** | +3.6 | 0.017 | 8/14 (A498, A549, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.026 | 10/14 (A549, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +3.4 | 0.029 | 4/14 (AsPC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.029 | 6/14 (NCI-H1573, A498, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.78×** | +3.3 | 0.029 | 3/14 (SW480, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **2.25×** | +3.3 | 0.029 | 8/14 (A549, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.029 | 3/14 (SW480, HepG2/C3A, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.029 | 9/15 (A549, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7543.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (SHP-77 0.0760×, AN3 CA 0.0625×, COLO 205 0.235×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (AN3 CA 0.199×, NCI-H460 0.273×, SHP-77 0.284×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.152×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.202×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.715×** | -3.9 | 0.058 | 11/14 (SHP-77, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.661× | -3.1 | 0.33 | 1/14 (HepG2/C3A) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM |  | 0.586× | -3.1 | 0.33 | 5/14 (NCI-H1792, A498, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | 0.482× | -3.0 | 0.33 | 5/14 (NCI-H460, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7543. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 117 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 12.7× (z +12.6) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 10.5× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -10.3) |
| [[AN3 CA (line)]] | alt | 188 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0625× (z -20.9) |
| [[SHP-77 (line)]] | alt | 93.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0760× (z -21.4) |
| [[A498 (line)]] | wt | 57.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 7.26 | 1 | 0 | [[Auranofin (drug)]] 5 µM 12.8× (z +9.1) | — |
| [[NCI-H1573 (line)]] | alt | 63.4 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 9.09× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.273× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.96 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 341 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.61 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.89 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.17 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7543), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1C1]] | +0.81 | +0.83 / +0.81 | both halves | 7e-06 | same gene group; pathway: Bile acid and bile salt metabolism; STRING 998; ⚠ same locus (4.5 kb: neighbours can correlate without regulation) |
| [[AKR1C3]] | +0.79 | +0.77 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_XENOBIOTIC_METABOLISM; STRING 997; ⚠ same locus (17.3 kb: neighbours can correlate without regulation) |
| [[GSG1L2]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[LINC00824]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PIR]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[THSD7A]] | +0.56 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[HOPX]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[PDK4]] | +0.55 | +0.45 / +0.48 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[CYP4F3]] | +0.54 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[MID1]] | +0.53 | +0.55 / +0.43 | both halves | 4e-05 |  |
| [[CD24]] | +0.53 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[SEMA3E]] | +0.52 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[ALDH1A1]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[ZSCAN31]] | +0.51 | +0.49 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAPGEF3]] | -0.48 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[ZNF275]] | -0.48 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[DPY19L3]] | -0.46 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[BLZF1]] | -0.45 | -0.46 / -0.39 | both halves | 6e-05 |  |
| [[TMEM158]] | -0.45 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[ANTXR2]] | -0.45 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ITGB5]] | -0.44 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[ARID3B]] | -0.44 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[MYEOV]] | -0.43 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[COL13A1]] | -0.43 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[SLC1A1]] | -0.43 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ARPC2]] | -0.43 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGST1]] | B | MGST1 activity raises AKR1C2's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.67× lower at baseline in the lines without MGST1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[AKR1C1]] | C | AKR1C1 activity raises AKR1C2's level | lines that do not express AKR1C1 (25) vs lines expressing it (25) | 4.90× lower at baseline in the lines without AKR1C1 | 0.001 | ⚠ within organs, on part of the lines; also absent: AKR1C2, IGFBP1, KYNU; co-absent with the target |
| [[AKR1C3]] | C | AKR1C3 activity raises AKR1C2's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 4.28× lower at baseline in the lines without AKR1C3 | 0.001 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3; co-absent with the target |
| [[WDR72]] | C | WDR72 activity raises AKR1C2's level | lines that do not express WDR72 (32) vs lines expressing it (18) | 2.85× lower at baseline in the lines without WDR72 | 0.010 | ⚠ within organs, on part of the lines; also absent: KCNE3, GPX2, CPLX2; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises AKR1C2's level | lines that do not express KYNU (29) vs lines expressing it (21) | 3.16× lower at baseline in the lines without KYNU | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |
| [[FGA]] | C | FGA activity raises AKR1C2's level | lines that do not express FGA (43) vs lines expressing it (7) | 7.27× lower at baseline in the lines without FGA | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[CYP4F11]] | C | CYP4F11 activity raises AKR1C2's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.58× lower at baseline in the lines without CYP4F11 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[FGG]] | C | FGG activity raises AKR1C2's level | lines that do not express FGG (42) vs lines expressing it (8) | 4.95× lower at baseline in the lines without FGG | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[CD24]] | C | CD24 activity raises AKR1C2's level | lines that do not express CD24 (24) vs lines expressing it (26) | 2.31× lower at baseline in the lines without CD24 | 0.096 | ⚠ within organs, on part of the lines; also absent: FOXQ1, RNF223, SPNS2; co-absent with the target |
| [[ALDH1A1]] | C | ALDH1A1 activity raises AKR1C2's level | lines that do not express ALDH1A1 (36) vs lines expressing it (14) | 2.88× lower at baseline in the lines without ALDH1A1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, FGA, GCG; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises AKR1C2's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 4.32× lower at baseline in the lines without AKR1B10 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 6, C 10. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P]] | B | AKR1C2 activity raises NMRAL2P's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 3.55× lower at baseline in the lines without AKR1C2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[NMRAL2P-1]] | B | AKR1C2 activity raises NMRAL2P-1's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 2.22× lower at baseline in the lines without AKR1C2 | 0.002 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[GCLC]] | B | AKR1C2 activity raises GCLC's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 2.23× lower at baseline in the lines without AKR1C2 | 0.003 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[PGD]] | B | AKR1C2 activity raises PGD's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 1.96× lower at baseline in the lines without AKR1C2 | 0.005 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[ARHGAP17]] | B | AKR1C2 activity raises ARHGAP17's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 1.34× lower at baseline in the lines without AKR1C2 | 0.064 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[RAPGEF3]] | B | AKR1C2 activity raises RAPGEF3's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 1.62× lower at baseline in the lines without AKR1C2 | 0.080 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2 |
| [[AKR1C3]] | C | AKR1C2 activity raises AKR1C3's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 5.98× lower at baseline in the lines without AKR1C2 | 9e-05 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[AKR1C1]] | C | AKR1C2 activity raises AKR1C1's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 8.05× lower at baseline in the lines without AKR1C2 | 1e-04 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[ABCC2]] | C | AKR1C2 activity raises ABCC2's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 3.97× lower at baseline in the lines without AKR1C2 | 0.001 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[KYNU]] | C | AKR1C2 activity raises KYNU's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 4.99× lower at baseline in the lines without AKR1C2 | 0.004 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[WDR72]] | C | AKR1C2 activity raises WDR72's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 3.28× lower at baseline in the lines without AKR1C2 | 0.007 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |
| [[FGA]] | C | AKR1C2 activity raises FGA's level | lines that do not express AKR1C2 (34) vs lines expressing it (16) | 2.79× lower at baseline in the lines without AKR1C2 | 0.040 | ⚠ within organs, on part of the lines; also absent: F5, FGA, CPLX2; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.595). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-7.3, 49.1); signed map (52.2, -8.6). **Vector** length 50.2, 15.8% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +14.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.7 |
| fall | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -3.1 |
|  | [[4EGI-1 (drug)]] 0.5 µM |  | -1.0 | -3.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | aldo-keto reductase family 1 member C2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:4,987,775-5,018,031 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DD, BABP, DD2, HAKRD, MCDR2; previously DDH2, TDD |
| Gene groups (HGNC) | Aldo-keto reductases |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 7 pathways, smallest: Synthesis of bile acids and bile salts via 27-hydroxycholesterol; Synthesis of bile acids and bile salts via 24-hydroxycholesterol; Synthesis of bile acids and bile salts via 7alpha-hydroxycholesterol |
| Matched by | ensembl_id |

**Function**, from UniProt [P52895](https://www.uniprot.org/uniprotkb/P52895) (Aldo-keto reductase family 1 member C2):

> Cytosolic aldo-keto reductase that catalyzes NADPH-dependent reduction of ketosteroids to hydroxysteroids. Displays broad substrate specificity with distinct positional and stereochemistry, primarily generating 3alpha-hydroxysteroids, but also 3beta-, 17beta- and 20alpha-hydroxysteroids. Required for male sex determination as a component of the 'backdoor' androgen biosynthesis pathway that generates 5alpha-dihydrotestosterone (5alpha-DHT) via pregnanes. Acts together with AKR1C4 to convert …

**Summary**, from NCBI Gene [1646](https://www.ncbi.nlm.nih.gov/gene/1646):

> This gene encodes a member of the aldo/keto reductase superfamily, which consists of more than 40 known enzymes and proteins. These enzymes catalyze the conversion of aldehydes and ketones to their corresponding alcohols using NADH and/or NADPH as cofactors. The enzymes display overlapping but distinct substrate specificity. This enzyme binds bile acid with high affinity, and shows minimal 3-alpha-hydroxysteroid dehydrogenase activity. This gene shares high sequence identity with three other …

**Accessions** — [HGNC:385](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:385) · Entrez [1646](https://www.ncbi.nlm.nih.gov/gene/1646) · UniProt [P52895](https://www.uniprot.org/uniprotkb/P52895) · Ensembl [ENSG00000151632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151632)

## Data

Gene col 7543: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7543); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7543, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7543]; `tensor/DDL_lfc|DDL_z.npy` [7543]; `embed/gene_vectors.npy` [7543]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7543 or target_col == 7543). Every well: [[AKR1C2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKR1C2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
