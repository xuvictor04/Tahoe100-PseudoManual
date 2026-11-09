---
symbol: "TRIOBP"
type: "gene"
col: 1870
ensembl_id: "ENSG00000100106"
name: "TRIO and F-actin binding protein"
location: "22q13.1"
module: 136
arm: "+"
pooled_cpm: 63.06
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 48
n_dd_up_clean: 0
n_dd_down_clean: 37
in_vector_space: true
direction_upstream: 10
direction_downstream: 0
tags: ["gene", "module/136"]
generated_by: "tahoemap"
---

# TRIOBP

*TRIO and F-actin binding protein* — 22q13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.53×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.374× (z -22.6, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCL2L12]] (+0.64, fdr 1e-05), [[PPP1R13L]] (+0.61, fdr 7e-06), [[ADGRL1-AS1]] (+0.61, fdr 1e-05); moves opposite to [[PAIP1]] (-0.62, fdr 1e-05), [[LARP1]] (-0.54, fdr 2e-05), [[FUBP1]] (-0.53, fdr 2e-05).
> It is in [[Module 136]], a single-armed module (heme metabolism).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[RAC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1870.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 2.53×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Thymol (drug)]] 0.5 µM |  | 1.25× | +3.7 | 0.11 | 18/47 (HT-29, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1870.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.374×** | -22.6 | 0e+00 | 42/48 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.401×** | -14.9 | 0e+00 | 43/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -12.6 | 5e-34 | 44/48 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.229×** | -12.6 | 5e-34 | 48/49 (NCI-H1573, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.460×** | -12.1 | 7e-32 | 42/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.463×** | -12.0 | 2e-31 | 42/47 (SNU-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -11.8 | 3e-30 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.252×** | -11.7 | 5e-30 | 45/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.612×** | -11.3 | 1e-27 | 38/48 (SNU-423, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -11.0 | 3e-26 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.520×** | -10.6 | 1e-24 | 44/48 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.548×** | -9.8 | 7e-21 | 37/48 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.549×** | -9.7 | 9e-21 | 39/48 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -9.6 | 2e-20 | 38/48 (NCI-H1792, HCT15, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -9.3 | 7e-19 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.531×** | -8.9 | 3e-17 | 39/48 (HS-578T, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -8.1 | 2e-14 | 28/48 (SNU-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1870. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.0 | 0 | 20 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -24.6) |
| [[NCI-H1792 (line)]] | alt | 102 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 90.5 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -24.4) |
| [[HOP62 (line)]] | alt | 75.8 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -18.6) |
| [[SNU-1 (line)]] | wt | 105 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -25.1) |
| [[SW480 (line)]] | alt | 66.6 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -22.7) |
| [[HS-578T (line)]] | alt | 132 | 0 | 11 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.277× (z -13.2) |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -16.4) |
| [[Hs 766T (line)]] | wt | 169 | 0 | 10 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.135× (z -21.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.373× (z -15.6) |
| [[NCI-H1573 (line)]] | alt | 95.6 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -24.0) |
| [[HCT15 (line)]] | alt | 116 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -16.4) |
| [[LS 180 (line)]] | wt | 84.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.5) |
| [[BT-474 (line)]] | alt | 79.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -17.3) |
| [[hTERT-HPNE (line)]] | wt | 96.0 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.212× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.253× (z -10.2) |
| [[COLO 205 (line)]] | alt | 86.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -19.4) |
| [[PANC-1 (line)]] | alt | 47.4 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -11.8) |
| [[H4 (line)]] | wt | 54.1 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -9.5) |
| [[A-172 (line)]] | wt | 54.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -22.2) |
| [[J82 (line)]] | alt | 58.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -12.6) |
| [[NCI-H23 (line)]] | alt | 52.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.6) |
| [[A549 (line)]] | wt | 42.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -18.7) |
| [[LoVo (line)]] | wt | 37.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 4 | — | [[Ixazomib citrate (drug)]] 5 µM 0.284× (z -12.2) |
| [[SNU-423 (line)]] | alt | 55.2 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.340× (z -13.2) |
| [[SW 900 (line)]] | alt | 61.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 42.0 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.237× (z -11.7) |
| [[KATO III (line)]] | alt | 68.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.285× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.468× (z -8.7) |
| [[A498 (line)]] | wt | 45.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.345× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 41.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -17.3) |
| [[Panc 03.27 (line)]] | alt | 45.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.9) |
| [[SW 1088 (line)]] | alt | 154 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -10.2) |
| [[A-427 (line)]] | wt | 27.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.6) |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.194× (z -9.1) ⚠ toxic |
| [[HT-29 (line)]] | alt | 43.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 26.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.256× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 40.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.276× (z -8.9) |
| [[AN3 CA (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 83.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1870), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCL2L12]] | +0.64 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R13L]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ADGRL1-AS1]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.60 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[CCNYL1]] | +0.60 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[PDLIM7]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[ITGB5]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[SLC25A51]] | +0.58 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[EHBP1L1]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PTGS1]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SMOX]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP1]] | -0.62 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LARP1]] | -0.54 | -0.46 / -0.50 | both halves | 2e-05 |  |
| [[FUBP1]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[HINT3]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PYURF]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[USP46]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[GAS2]] | -0.51 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SMG7]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[CUL5]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[OSBPL1A]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[ZNF618]] | -0.50 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[PDCL3]] | -0.50 | -0.37 / -0.42 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAC2]] | B | RAC2 activity raises TRIOBP's level | lines that do not express RAC2 (19) vs lines expressing it (31) | 1.44× lower at baseline in the lines without RAC2 | 0.018 | ⚠ within organs, on part of the lines; also absent: BHLHE41, ADTRP, MANCR |
| [[COL13A1]] | B | COL13A1 activity raises TRIOBP's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without COL13A1 | 0.019 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[ITGA3]] | B | ITGA3 activity raises TRIOBP's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without ITGA3 | 0.024 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[ADAM8]] | B | ADAM8 activity raises TRIOBP's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 1.49× lower at baseline in the lines without ADAM8 | 0.039 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[NIBAN2]] | B | NIBAN2 activity raises TRIOBP's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 1.75× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SMOX]] | B | SMOX activity raises TRIOBP's level | lines that do not express SMOX (6) vs lines expressing it (44) | 1.65× lower at baseline in the lines without SMOX | 0.071 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[PLAT]] | B | PLAT activity raises TRIOBP's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.44× lower at baseline in the lines without PLAT | 0.089 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[PTGS1]] | B | PTGS1 activity raises TRIOBP's level | lines that do not express PTGS1 (26) vs lines expressing it (24) | 1.45× lower at baseline in the lines without PTGS1 | 0.095 | ⚠ within organs, on part of the lines; also absent: C2CD4A, ARHGEF38, ILDR1 |
| [[MTSS1]] | B | MTSS1 activity raises TRIOBP's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 1.40× lower at baseline in the lines without MTSS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1 |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises TRIOBP's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 1.98× lower at baseline in the lines without SPRY4-AS1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 136]] — heme metabolism; 35 genes; every member is in the + arm (projection on the module's main direction 0.629). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (42.0, -5.2); signed map (-0.5, 29.3). **Vector** length 84.9, 25.6% of its response variance represented; |z| ≥ 3 in 1,496 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | -22.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | -9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | -10.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | -9.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +0.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.9 | -11.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.1 | -4.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.9 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.7 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.2 | -2.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.1 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | TRIO and F-actin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:37,697,048-37,776,556 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HRIHFB2122, KIAA1662, Tara, TAP68; previously DFNB28 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2D6](https://www.uniprot.org/uniprotkb/Q9H2D6) (TRIO and F-actin-binding protein):

> [Isoform 1]: Regulates actin cytoskeletal organization, cell spreading and cell contraction by directly binding and stabilizing filamentous F-actin and prevents its depolymerization. May also serve as a linker protein to recruit proteins required for F-actin formation and turnover. Essential for correct mitotic progression.; [Isoform 5]: Plays a pivotal role in the formation of stereocilia rootlets.; [Isoform 4]: Plays a pivotal role in the formation of stereocilia rootlets.

**Summary**, from NCBI Gene [11078](https://www.ncbi.nlm.nih.gov/gene/11078):

> This gene encodes a protein with an N-terminal pleckstrin homology domain and a C-terminal coiled-coil region. The protein interacts with trio, which is involved with neural tissue development and controlling actin cytoskeleton organization, cell motility and cell growth. The protein also associates with F-actin and stabilizes F-actin structures. Mutations in this gene have been associated with a form of autosomal recessive nonsyndromic deafness. Multiple alternatively spliced transcript …

**Accessions** — [HGNC:17009](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17009) · Entrez [11078](https://www.ncbi.nlm.nih.gov/gene/11078) · UniProt [Q9H2D6](https://www.uniprot.org/uniprotkb/Q9H2D6) · Ensembl [ENSG00000100106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100106)

## Data

Gene col 1870: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1870); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1870, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1870]; `tensor/DDL_lfc|DDL_z.npy` [1870]; `embed/gene_vectors.npy` [1870]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1870 or target_col == 1870). Every well: [[TRIOBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIOBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
