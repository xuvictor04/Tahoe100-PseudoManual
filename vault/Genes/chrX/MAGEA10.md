---
symbol: "MAGEA10"
type: "gene"
col: 4513
ensembl_id: "ENSG00000124260"
name: "MAGE family member A10"
location: "Xq28"
module: 9
arm: "+"
pooled_cpm: 4.08
n_lines_expressing: 8
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 12
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MAGEA10

*MAGE family member A10* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.09× (z +11.4, q 2e-27, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Saquinavir (drug)]] 5 µM: 1.91× (z +5.5, q 5e-06, up in 3 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.230×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGEB2]] (+0.61, fdr 1e-05), [[MAGEA1]] (+0.61, fdr 6e-05), [[NRG3]] (+0.58, fdr 4e-05); moves opposite to [[GNRH1]] (-0.53, fdr 9e-05), [[GOT1-DT]] (-0.49, fdr 2e-04), [[ECT2L]] (-0.48, fdr 1e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[GTSF1]] → it (grade C ⚠); 12 go from it, the strongest it → [[ABCA13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4513.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.09×** | +11.4 | 2e-27 | 3/3 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.14×** | +11.0 | 1e-25 | 5/6 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.02×** | +7.8 | 1e-12 | 4/5 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Saquinavir (drug)]] 5 µM |  | **1.91×** | +5.5 | 5e-06 | 3/6 (SK-MEL-2, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.35×** | +5.2 | 3e-05 | 2/5 (SK-MEL-2, NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +4.8 | 1e-04 | 1/6 (NCI-H1792) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.7 | 2e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.16×** | +4.6 | 4e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +4.4 | 7e-04 | 2/6 (NCI-H1573, C-33 A) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.8 | 0.009 | 2/6 (SK-MEL-2, NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +3.6 | 0.017 | 0/6 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.44×** | +3.5 | 0.020 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.89×** | +3.4 | 0.034 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +3.3 | 0.044 | 1/6 (C-33 A) | rises with dose |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.71×** | +3.2 | 0.046 | 1/6 (C-33 A) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.70×** | +3.2 | 0.046 | 4/6 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.67×** | +3.1 | 0.061 | 0/6 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.64×** | +3.0 | 0.081 | 2/6 (SHP-77, SK-MEL-2) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4513.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.230×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.573× | -3.1 | 0.88 | 1/6 (C-33 A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4513. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.29× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 59.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.97× (z +10.0) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.230× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 28.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.07× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.933 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.483 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.358 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.419 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.999 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.487 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.352 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4513), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGEB2]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 | same gene group |
| [[MAGEA1]] | +0.61 | +0.38 / +0.60 | both halves | 6e-05 | same gene group; STRING 520 |
| [[NRG3]] | +0.58 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[AKAP6]] | +0.57 | +0.47 / +0.38 | both halves | 6e-05 |  |
| [[NRG1]] | +0.54 | +0.46 / +0.35 | both halves | 1e-04 |  |
| [[CGA]] | +0.54 | +0.44 / +0.36 | both halves | 9e-05 |  |
| [[DNAH14]] | +0.53 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[MAGEA4]] | +0.53 | +0.45 / +0.57 | both halves | 3e-05 | same gene group; STRING 863 |
| [[NYAP2]] | +0.52 | +0.42 / +0.25 | both halves | 4e-04 |  |
| [[SCN3A]] | +0.52 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[LINC01592]] | +0.51 | +0.27 / +0.49 | both halves | 3e-04 |  |
| [[BHMT2]] | +0.51 | +0.55 / +0.26 | both halves | 3e-04 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNRH1]] | -0.53 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[GOT1-DT]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[ECT2L]] | -0.48 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[SDHAP4-1]] | -0.47 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[TSNAX-DISC1]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[C12orf76]] | -0.47 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[ZNF487]] | -0.46 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[ZFYVE21]] | -0.46 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[VDAC1P8]] | -0.46 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[MFSD8]] | -0.45 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[APTR]] | -0.45 | -0.34 / -0.41 | both halves | 1e-04 |  |
| [[GET1-SH3BGR]] | -0.45 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTSF1]] | C | GTSF1 activity raises MAGEA10's level | lines that do not express GTSF1 (40) vs lines expressing it (10) | 4.94× lower at baseline in the lines without GTSF1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CGA, CALCA, LINC02566; co-absent with the target |
| [[MAGEB2]] | C | MAGEB2 activity raises MAGEA10's level | lines that do not express MAGEB2 (42) vs lines expressing it (8) | 6.92× lower at baseline in the lines without MAGEB2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, MAGEA10, TBXT; co-absent with the target |
| [[LINC01287]] | C | LINC01287 activity raises MAGEA10's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 3.74× lower at baseline in the lines without LINC01287 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2; co-absent with the target |
| [[CGA]] | C | CGA activity raises MAGEA10's level | lines that do not express CGA (44) vs lines expressing it (6) | 4.35× lower at baseline in the lines without CGA | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, SYT4, RIT2; co-absent with the target |
| [[LINC02438]] | C | LINC02438 activity raises MAGEA10's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 3.32× lower at baseline in the lines without LINC02438 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[BHMT2]] | C | BHMT2 activity raises MAGEA10's level | lines that do not express BHMT2 (40) vs lines expressing it (10) | 2.89× lower at baseline in the lines without BHMT2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: APOB, LINC01320, CP; co-absent with the target |
| [[LINC02492]] | C | LINC02492 activity raises MAGEA10's level | lines that do not express LINC02492 (32) vs lines expressing it (18) | 2.65× lower at baseline in the lines without LINC02492 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000260289, ENSG00000254337, RHOJ; maybe low, not absent; co-absent with the target |
| [[STXBP5L]] | C | STXBP5L activity raises MAGEA10's level | lines that do not express STXBP5L (35) vs lines expressing it (15) | 2.01× lower at baseline in the lines without STXBP5L | 0.061 | ⚠ within organs, on part of the lines; also absent: PCSK1, ENSG00000287211, GABRG2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA13]] | B | MAGEA10 activity raises ABCA13's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 2.53× lower at baseline in the lines without MAGEA10 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425 |
| [[GTSF1]] | C | MAGEA10 activity raises GTSF1's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 6.11× lower at baseline in the lines without MAGEA10 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[POU6F2]] | C | MAGEA10 activity raises POU6F2's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 5.27× lower at baseline in the lines without MAGEA10 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[LINC02492]] | C | MAGEA10 activity raises LINC02492's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 3.77× lower at baseline in the lines without MAGEA10 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[FRMPD4]] | C | MAGEA10 activity raises FRMPD4's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 2.68× lower at baseline in the lines without MAGEA10 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[LINC01287]] | C | MAGEA10 activity raises LINC01287's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 2.90× lower at baseline in the lines without MAGEA10 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[MAGEB2]] | C | MAGEA10 activity raises MAGEB2's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 4.62× lower at baseline in the lines without MAGEA10 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[STXBP5L]] | C | MAGEA10 activity raises STXBP5L's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 2.65× lower at baseline in the lines without MAGEA10 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[PCSK1]] | C | MAGEA10 activity raises PCSK1's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 4.21× lower at baseline in the lines without MAGEA10 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[COL22A1]] | C | MAGEA10 activity raises COL22A1's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 3.23× lower at baseline in the lines without MAGEA10 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[LINC02438]] | C | MAGEA10 activity raises LINC02438's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 7.98× lower at baseline in the lines without MAGEA10 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |
| [[SCG2]] | C | MAGEA10 activity raises SCG2's level | lines that do not express MAGEA10 (42) vs lines expressing it (8) | 4.66× lower at baseline in the lines without MAGEA10 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MAGEB2, SOX10, LINC01425; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.527). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.2, 33.4); signed map (30.8, 34.9). **Vector** length 14.8, 4.02% of its response variance represented; |z| ≥ 3 in 89 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.1 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.9 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.5 | +2.0 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +0.4 | +0.5 |
|  | [[Vitamin K4 (drug)]] 0.05 µM |  | +0.4 | +0.5 |
| fall | [[Radotinib (drug)]] 5 µM |  | -0.5 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.5 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.3 | -0.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.3 | +0.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.3 | -1.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.3 | -1.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | MAGE family member A10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:152,133,310-152,138,578 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10599, CT1.10; previously MAGE10 |
| Gene groups (HGNC) | MAGE family |
| Matched by | ensembl_id |

**Function**, from UniProt [P43363](https://www.uniprot.org/uniprotkb/P43363) (Melanoma-associated antigen 10):

> Not known, though may play a role in embryonal development and tumor transformation or aspects of tumor progression.

**Summary**, from NCBI Gene [4109](https://www.ncbi.nlm.nih.gov/gene/4109):

> This gene is a member of the MAGEA gene family. The members of this family encode proteins with 50 to 80% sequence identity to each other. The promoters and first exons of the MAGEA genes show considerable variability, suggesting that the existence of this gene family enables the same function to be expressed under different transcriptional controls. The MAGEA genes are clustered at chromosomal location Xq28. They have been implicated in some hereditary disorders, such as dyskeratosis …

**Accessions** — [HGNC:6797](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6797) · Entrez [4109](https://www.ncbi.nlm.nih.gov/gene/4109) · UniProt [P43363](https://www.uniprot.org/uniprotkb/P43363) · Ensembl [ENSG00000124260](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124260)

## Data

Gene col 4513: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4513); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4513, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4513]; `tensor/DDL_lfc|DDL_z.npy` [4513]; `embed/gene_vectors.npy` [4513]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4513 or target_col == 4513). Every well: [[MAGEA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGEA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
