---
symbol: "CCDC152"
type: "gene"
col: 12715
ensembl_id: "ENSG00000198865"
name: "coiled-coil domain containing 152"
location: "5p12"
module: 196
arm: "+"
pooled_cpm: 3.01
n_lines_expressing: 20
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 13
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# CCDC152

*coiled-coil domain containing 152* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.31× (z +10.8, q 3e-24, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.54× (z +8.8, q 2e-16, up in 1 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.266×; ⚠ cell-cycle shift, explains ~40% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.338×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF17]] (+0.69, fdr 2e-05), [[F11-AS1]] (+0.56, fdr 1e-05), [[MILR1]] (+0.55, fdr 2e-04); moves opposite to [[MSL1]] (-0.43, fdr 1e-04), [[BIVM]] (-0.40, fdr 3e-04), [[CERS2]] (-0.40, fdr 3e-04).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CHST9]] → it (grade B ⚠); 13 go from it, the strongest it → [[NYAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12715.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.31×** | +10.8 | 3e-24 | 2/3 (CFPAC-1, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.65×** | +10.3 | 2e-22 | 5/5 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +8.8 | 2e-16 | 1/9 (HEC-1-A) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.99×** | +8.6 | 1e-15 | 2/3 (CFPAC-1, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.01×** | +4.7 | 4e-04 | 6/12 (C32, LOX-IMVI, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.60×** | +4.4 | 8e-04 | 3/12 (LOX-IMVI, C32, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +4.4 | 8e-04 | 4/14 (AsPC-1, hTERT-HPNE, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.89×** | +4.3 | 0.001 | 6/15 (AsPC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.86×** | +4.1 | 0.002 | 1/4 (Panc 03.27) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.6 | 0.020 | 0/5 | rises with dose | cell-cycle shift (explains ~20% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.48×** | +3.5 | 0.026 | 1/5 (Panc 03.27) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.5 | 0.026 | 1/5 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.038 | 1/6 (SHP-77) | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.088 | 3/7 (Panc 03.27, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12715.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.266×; ⚠ cell-cycle shift, explains ~40% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.338×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.865× | -3.6 | 0.18 | 3/16 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Ivermectin (drug)]] 5 µM |  | 0.616× | -3.3 | 0.29 | 1/15 (CFPAC-1) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12715. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 41.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 53.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.451 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.768 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.764 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.478 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.407 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.476 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.610 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.546 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.463 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12715), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF17]] | +0.69 | +0.47 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[F11-AS1]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[MILR1]] | +0.55 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[LINC01239]] | +0.54 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[NRG3]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[MAGEB2]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[CHST9]] | +0.51 | +0.29 / +0.39 | both halves | 2e-04 |  |
| [[SHROOM4]] | +0.50 | +0.42 / +0.29 | both halves | 3e-04 |  |
| [[DHRS2]] | +0.50 | +0.36 / +0.42 | both halves | 1e-04 |  |
| [[LAPTM5]] | +0.47 | +0.31 / +0.42 | both halves | 2e-04 |  |
| [[MAGEA10]] | +0.46 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[ATP6V0A4]] | +0.46 | +0.50 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSL1]] | -0.43 | -0.37 / -0.32 | both halves | 1e-04 |  |
| [[BIVM]] | -0.40 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[CERS2]] | -0.40 | -0.27 / -0.44 | both halves | 3e-04 |  |
| [[CHFR]] | -0.40 | -0.30 / -0.39 | both halves | 2e-04 |  |
| [[ZFYVE21]] | -0.39 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ZDHHC24]] | -0.38 | -0.25 / -0.29 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHST9]] | B | CHST9 activity raises CCDC152's level | lines that do not express CHST9 (18) vs lines expressing it (32) | 1.62× lower at baseline in the lines without CHST9 | 0.041 | ⚠ within organs, on part of the lines; also absent: LINC02015, PRKD1, MYO18B; maybe low, not absent |
| [[RNF17]] | C | RNF17 activity raises CCDC152's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 3.14× lower at baseline in the lines without RNF17 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[PAEP]] | C | PAEP activity raises CCDC152's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without PAEP | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D; co-absent with the target |
| [[F11-AS1]] | C | F11-AS1 activity raises CCDC152's level | lines that do not express F11-AS1 (34) vs lines expressing it (16) | 1.84× lower at baseline in the lines without F11-AS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, SRRM4, LINC02566; maybe low, not absent; co-absent with the target |
| [[FKBP9P1-1]] | C | FKBP9P1-1 activity raises CCDC152's level | lines that do not express FKBP9P1-1 (30) vs lines expressing it (20) | 2.39× lower at baseline in the lines without FKBP9P1-1 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000231317, ENSG00000253642, ENSG00000287622; maybe low, not absent; co-absent with the target |
| [[PEX5L]] | C | PEX5L activity raises CCDC152's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.09× lower at baseline in the lines without PEX5L | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[NRG3]] | C | NRG3 activity raises CCDC152's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 2.00× lower at baseline in the lines without NRG3 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[ZNF334]] | C | ZNF334 activity raises CCDC152's level | lines that do not express ZNF334 (32) vs lines expressing it (18) | 1.92× lower at baseline in the lines without ZNF334 | 0.050 | ⚠ within organs, on part of the lines; also absent: COL4A6, LINC02742, IGF2; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises CCDC152's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.15× lower at baseline in the lines without SNTG1 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 4, C 9. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NYAP2]] | B | CCDC152 activity raises NYAP2's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.06× lower at baseline in the lines without CCDC152 | 0.048 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent |
| [[MILR1]] | B | CCDC152 activity raises MILR1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.32× lower at baseline in the lines without CCDC152 | 0.059 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent |
| cells under [[Docetaxel (drug)]] 5 µM | B | CCDC152 activity raises the cells' numbers under Docetaxel 5 µM (protects the cells) | lines that do not express CCDC152 (30) vs lines expressing it (18) | the lines without CCDC152: 0.90× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent |
| [[MSL1]] | B | CCDC152 activity lowers MSL1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 1.07× higher at baseline in the lines without CCDC152 | 0.0997 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent |
| [[COL22A1]] | C | CCDC152 activity raises COL22A1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.86× lower at baseline in the lines without CCDC152 | 0.018 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[PEX5L]] | C | CCDC152 activity raises PEX5L's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.65× lower at baseline in the lines without CCDC152 | 0.021 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[CLDN10-AS1]] | C | CCDC152 activity raises CLDN10-AS1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without CCDC152 | 0.024 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[FKBP9P1-1]] | C | CCDC152 activity raises FKBP9P1-1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without CCDC152 | 0.033 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[IL19]] | C | CCDC152 activity raises IL19's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 1.50× lower at baseline in the lines without CCDC152 | 0.046 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[SNTG1]] | C | CCDC152 activity raises SNTG1's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 1.91× lower at baseline in the lines without CCDC152 | 0.050 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[PAEP]] | C | CCDC152 activity raises PAEP's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.25× lower at baseline in the lines without CCDC152 | 0.055 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |
| [[SAMMSON]] | C | CCDC152 activity raises SAMMSON's level | lines that do not express CCDC152 (30) vs lines expressing it (20) | 2.62× lower at baseline in the lines without CCDC152 | 0.065 | ⚠ within organs, on part of the lines; also absent: PLAT, SNTG1, COL19A1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.615). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.3, 28.8); signed map (31.7, 36.7). **Vector** length 18.1, 2.74% of its response variance represented; |z| ≥ 3 in 300 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.1 | +2.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +1.1 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.9 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.6 | +4.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.6 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.4 | +1.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.4 | +0.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.6 | -3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -0.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.5 | -1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.5 | -0.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -1.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.4 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 152 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p12 — chr5:42,756,818-42,802,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LOC100129792 |
| Matched by | ensembl_id |

UniProt [Q4G0S7](https://www.uniprot.org/uniprotkb/Q4G0S7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:34438](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34438) · Entrez [100129792](https://www.ncbi.nlm.nih.gov/gene/100129792) · UniProt [Q4G0S7](https://www.uniprot.org/uniprotkb/Q4G0S7) · Ensembl [ENSG00000198865](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198865)

## Data

Gene col 12715: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12715); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12715, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12715]; `tensor/DDL_lfc|DDL_z.npy` [12715]; `embed/gene_vectors.npy` [12715]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12715 or target_col == 12715). Every well: [[CCDC152 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC152.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
