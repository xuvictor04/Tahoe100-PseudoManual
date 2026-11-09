---
symbol: "UBOX5"
type: "gene"
col: 11610
ensembl_id: "ENSG00000185019"
name: "U-box domain containing 5"
location: "20p13"
module: 142
arm: "+"
pooled_cpm: 21.38
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/142"]
generated_by: "tahoemap"
---

# UBOX5

*U-box domain containing 5* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.18× (z +14.5, q 7e-45, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.527× (z -9.4, q 4e-18, down in 22 of 32 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (HS-578T 0.0385×, J82 0.0643×, BT-474 0.0872×, LOX-IMVI 0.119×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.163×, SHP-77 0.199×, HepG2/C3A 0.142×, NCI-H2347 0.263×; ⚠ toxic; transcription drop); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0552×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0919×); [[Ixazomib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.195×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CWF19L1]] (+0.75, fdr 7e-06), [[C1orf52]] (+0.73, fdr 7e-06), [[RNF121]] (+0.70, fdr 7e-06); moves opposite to [[RFK]] (-0.63, fdr 1e-05), [[ROCK2]] (-0.58, fdr 1e-05), [[ISOC1]] (-0.56, fdr 1e-05).
> It is in [[Module 142]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF568]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11610.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.18×** | +14.5 | 7e-45 | 48/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.58×** | +10.2 | 9e-22 | 39/46 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.63×** | +7.5 | 2e-11 | 38/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +5.8 | 7e-07 | 30/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.8 | 7e-07 | 20/36 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +5.2 | 2e-05 | 21/29 (NCI-H1573, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.9 | 1e-04 | 21/48 (SW480, SNU-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.24×** | +4.5 | 6e-04 | 18/47 (PANC-1, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +3.9 | 0.005 | 21/47 (NCI-H23, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.005 | 17/48 (MIA PaCa-2, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +3.8 | 0.008 | 17/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | 1.17× | +3.4 | 0.038 | 16/48 (SNU-1, NCI-H2347, …) | top dose only | low cells (technical?) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.050 | 12/48 (PANC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.059 | 11/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.093 | 16/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11610.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (HS-578T 0.0385×, J82 0.0643×, BT-474 0.0872×, LOX-IMVI 0.119×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (A-172 0.163×, SHP-77 0.199×, HepG2/C3A 0.142×, NCI-H2347 0.263×; ⚠ toxic; transcription drop); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0552×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.0919×); [[Ixazomib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.195×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.527×** | -9.4 | 4e-18 | 22/32 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.605×** | -7.7 | 5e-12 | 27/41 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.692×** | -5.4 | 1e-05 | 23/47 (HOP62, NCI-H2347, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **0.750×** | -4.4 | 0.002 | 20/45 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -3.7 | 0.023 | 16/48 (SHP-77, C32, …) | rises with dose |  |
| [[Busulfan (drug)]] 5 µM |  | 0.845× | -3.6 | 0.035 | 12/48 (SW480, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.816× | -3.1 | 0.15 | 9/48 (A-172, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11610. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 27.3 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 11.0× (z +12.9) | — |
| [[A-172 (line)]] | wt | 22.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.163× (z -13.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 43.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.199× (z -13.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 28.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.291× (z -9.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0872× (z -15.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0552× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 33.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -12.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0385× (z -23.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0643× (z -18.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.73× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -13.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -9.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 19.1 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.195× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.108× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 19.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.45× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 26.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 22.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0919× (z -12.5) |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11610), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CWF19L1]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[C1orf52]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[RNF121]] | +0.70 | +0.75 / +0.65 | both halves | 7e-06 | same gene group |
| [[USPL1]] | +0.68 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZBTB49]] | +0.67 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[TIMM23]] | +0.67 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PGS1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[ZNF251]] | +0.66 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[GLUD1P3]] | +0.66 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MED17]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[ZNF500]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MED9]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFK]] | -0.63 | -0.66 / -0.52 | both halves | 1e-05 |  |
| [[ROCK2]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ISOC1]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[RASEF]] | -0.55 | -0.57 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF568]] | B | ZNF568 activity raises UBOX5's level | lines that do not express ZNF568 (18) vs lines expressing it (32) | 1.25× lower at baseline in the lines without ZNF568 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF829, ACTN2, ZNF880 |
| [[ARHGAP10]] | C | ARHGAP10 activity lowers UBOX5's level | lines that do not express ARHGAP10 (3) vs lines expressing it (47) | 1.63× higher at baseline in the lines without ARHGAP10 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: SPDL1, HOMER3, RBMS2; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | C | UBOX5's natural level lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | UBOX5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.015 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 142]]; 33 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.0, -16.8); signed map (-46.1, 5.5). **Vector** length 85.9, 17.5% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.8 | +14.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -6.3 | -5.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.2 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | U-box domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:3,107,573-3,160,196 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UIP5, KIAA0860, Ubce7ip5, RNF37 |
| Gene groups (HGNC) | Ring finger proteins; U-box domain containing; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O94941](https://www.uniprot.org/uniprotkb/O94941) (RING finger protein 37):

> May have a ubiquitin-protein ligase activity acting as an E3 ubiquitin-protein ligase or as a ubiquitin-ubiquitin ligase promoting elongation of ubiquitin chains on substrates.

**Summary**, from NCBI Gene [22888](https://www.ncbi.nlm.nih.gov/gene/22888):

> This gene encodes a U-box domain containing protein. The encoded protein interacts with E2 enzymes and may play a role in the ubiquitination pathway. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jun 2012]

**Accessions** — [HGNC:17777](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17777) · Entrez [22888](https://www.ncbi.nlm.nih.gov/gene/22888) · UniProt [O94941](https://www.uniprot.org/uniprotkb/O94941) · Ensembl [ENSG00000185019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185019)

## Data

Gene col 11610: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11610); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11610, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11610]; `tensor/DDL_lfc|DDL_z.npy` [11610]; `embed/gene_vectors.npy` [11610]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11610 or target_col == 11610). Every well: [[UBOX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBOX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
