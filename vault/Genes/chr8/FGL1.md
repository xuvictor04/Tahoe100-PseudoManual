---
symbol: "FGL1"
type: "gene"
col: 2493
ensembl_id: "ENSG00000104760"
name: "fibrinogen like 1"
location: "8p22"
module: 8
arm: "+"
pooled_cpm: 3.64
n_lines_expressing: 11
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 17
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FGL1

*fibrinogen like 1* — 8p22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.25× (z +11.4, q 2e-27, up in 4 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.0953×, HepG2/C3A 0.0932×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.108×, AN3 CA 0.0533×; ⚠ cell-cycle shift, explains ~81% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HepG2/C3A 0.175×, AN3 CA 0.0544×; ⚠ cell-cycle shift, explains ~60% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.166×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.323×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOB]] (+0.69, fdr 1e-05), [[MTUS1]] (+0.62, fdr 1e-05), [[HGD]] (+0.55, fdr 5e-05); moves opposite to [[PLEK2]] (-0.49, fdr 3e-04), [[ARID3B]] (-0.48, fdr 1e-04), [[STK10]] (-0.47, fdr 4e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MGC32805]] → it (grade C ⚠); 17 go from it, the strongest it → [[MTUS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2493.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.25×** | +11.4 | 2e-27 | 4/6 (KATO III, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.71×** | +8.6 | 2e-15 | 2/4 (SHP-77, AsPC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.88×** | +8.5 | 4e-15 | 2/2 (SHP-77, HepG2/C3A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.41×** | +7.6 | 3e-12 | 1/3 (SHP-77) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.26×** | +4.5 | 6e-04 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.52×** | +3.7 | 0.022 | 1/4 (AsPC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.93×** | +3.6 | 0.022 | 4/6 (SHP-77, A549, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.48×** | +3.6 | 0.023 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.042 | 1/7 (AsPC-1) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 1.74× | +3.1 | 0.12 | 0/7 | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.72× | +3.0 | 0.13 | 1/6 (SHP-77) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2493.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.0953×, HepG2/C3A 0.0932×); [[Panobinostat (drug)]] 0.5 µM in 2 lines (HepG2/C3A 0.108×, AN3 CA 0.0533×; ⚠ cell-cycle shift, explains ~81% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (HepG2/C3A 0.175×, AN3 CA 0.0544×; ⚠ cell-cycle shift, explains ~60% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.166×); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.323×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ivermectin (drug)]] 5 µM |  | 0.552× | -3.3 | 0.47 | 0/8 | top dose only | position effect removed |
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.570× | -3.1 | 0.47 | 3/7 (AsPC-1, KATO III, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2493. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0932× (z -17.8) |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0533× (z -9.3) ⚠ cell-cycle shift, explains ~81% of this change |
| [[SHP-77 (line)]] | alt | 85.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -19.2) |
| [[A-172 (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.455 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.642 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.565 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.592 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.452 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.481 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.648 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.744 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.516 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.559 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.596 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.733 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.456 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2493), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOB]] | +0.69 | +0.80 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[MTUS1]] | +0.62 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[HGD]] | +0.55 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[PEG3]] | +0.54 | +0.70 / +0.29 | both halves | 2e-04 |  |
| [[AGT]] | +0.53 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[AFP]] | +0.53 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[UGT2B7]] | +0.53 | +0.46 / +0.34 | both halves | 1e-04 |  |
| [[FGG]] | +0.52 | +0.55 / +0.49 | both halves | 1e-05 | same gene group; STRING 943 |
| [[PLA2G2A]] | +0.52 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PDK4]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[SHROOM3]] | +0.51 | +0.43 / +0.40 | both halves | 5e-05 |  |
| [[PHYHIPL]] | +0.50 | +0.56 / +0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[CFI]] | +0.50 | +0.51 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEK2]] | -0.49 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[ARID3B]] | -0.48 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[STK10]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[GDPD5]] | -0.46 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[CDCP1]] | -0.46 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[AGPAT4]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[LYPD3]] | -0.45 | -0.31 / -0.38 | both halves | 2e-04 |  |
| [[PLEKHG5]] | -0.45 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[WNT7B]] | -0.44 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[ARHGEF4]] | -0.43 | -0.23 / -0.37 | both halves | 5e-04 |  |
| [[C6orf141]] | -0.43 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[LAMC2]] | -0.42 | -0.32 / -0.48 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGC32805]] | C | MGC32805 activity raises FGL1's level | lines that do not express MGC32805 (32) vs lines expressing it (18) | 1.65× lower at baseline in the lines without MGC32805 | 0.016 | ⚠ within organs, on part of the lines; also absent: CEACAM5, ST18, PRR15L; maybe low, not absent; co-absent with the target |
| [[PHYHIPL]] | C | PHYHIPL activity raises FGL1's level | lines that do not express PHYHIPL (39) vs lines expressing it (11) | 3.93× lower at baseline in the lines without PHYHIPL | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[FGG]] | C | FGG activity raises FGL1's level | lines that do not express FGG (42) vs lines expressing it (8) | 4.14× lower at baseline in the lines without FGG | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[LGR5]] | C | LGR5 activity raises FGL1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.70× lower at baseline in the lines without LGR5 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[TOX3]] | C | TOX3 activity raises FGL1's level | lines that do not express TOX3 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without TOX3 | 0.080 | ⚠ within organs, on part of the lines; also absent: GPX2, ENSG00000287426, TMEM45B; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 6, C 11. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1]] | B | FGL1 activity raises MTUS1's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 4.59× lower at baseline in the lines without FGL1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[DIP2C-AS1]] | B | FGL1 activity raises DIP2C-AS1's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 1.52× lower at baseline in the lines without FGL1 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[CDX2]] | B | FGL1 activity lowers CDX2's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 1.04× higher at baseline in the lines without FGL1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[MTUS1-DT]] | B | FGL1 activity raises MTUS1-DT's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.19× lower at baseline in the lines without FGL1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[CNKSR3]] | B | FGL1 activity raises CNKSR3's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.02× lower at baseline in the lines without FGL1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[PLEKHA7]] | B | FGL1 activity raises PLEKHA7's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 1.56× lower at baseline in the lines without FGL1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA |
| [[TOX3]] | C | FGL1 activity raises TOX3's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 4.96× lower at baseline in the lines without FGL1 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[CPLX2]] | C | FGL1 activity raises CPLX2's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without FGL1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[PPARGC1A]] | C | FGL1 activity raises PPARGC1A's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 3.24× lower at baseline in the lines without FGL1 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[NPNT]] | C | FGL1 activity raises NPNT's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.09× lower at baseline in the lines without FGL1 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[RMST]] | C | FGL1 activity raises RMST's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.66× lower at baseline in the lines without FGL1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |
| [[LGR5]] | C | FGL1 activity raises LGR5's level | lines that do not express FGL1 (39) vs lines expressing it (11) | 2.73× lower at baseline in the lines without FGL1 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, AFP, CALCA; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, 53.7); signed map (57.5, 1.0). **Vector** length 24.4, 7.50% of its response variance represented; |z| ≥ 3 in 212 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.8 | +8.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +8.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.8 | +2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.7 | +1.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.6 | +2.1 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | +0.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -0.7 | -1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.6 | +0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.5 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -0.5 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.5 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | fibrinogen like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p22 — chr8:17,864,380-17,910,365 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HFREP-1, HPS |
| Gene groups (HGNC) | Fibrinogen C domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q08830](https://www.uniprot.org/uniprotkb/Q08830) (Fibrinogen-like protein 1):

> Immune suppressive molecule that inhibits antigen-specific T-cell activation by acting as a ligand of LAG3. LAG3-binding initiates a signaling that inhibits the T-cell receptor (TCR) in the immunological synapse, preventing T-cell activation. Binds LAG3 independently from MHC class II (MHC-II). Secreted by, and promotes growth of, hepatocytes.

**Summary**, from NCBI Gene [2267](https://www.ncbi.nlm.nih.gov/gene/2267):

> Fibrinogen-like 1 is a member of the fibrinogen family. This protein is homologous to the carboxy terminus of the fibrinogen beta- and gamma- subunits which contains the four conserved cysteines of fibrinogens and fibrinogen related proteins. However, this protein lacks the platelet-binding site, cross-linking region and a thrombin-sensitive site which are necessary for fibrin clot formation. This protein may play a role in the development of hepatocellular carcinomas. Four alternatively …

**Accessions** — [HGNC:3695](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3695) · Entrez [2267](https://www.ncbi.nlm.nih.gov/gene/2267) · UniProt [Q08830](https://www.uniprot.org/uniprotkb/Q08830) · Ensembl [ENSG00000104760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104760)

## Data

Gene col 2493: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2493); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2493, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2493]; `tensor/DDL_lfc|DDL_z.npy` [2493]; `embed/gene_vectors.npy` [2493]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2493 or target_col == 2493). Every well: [[FGL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
