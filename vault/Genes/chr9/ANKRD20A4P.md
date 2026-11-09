---
symbol: "ANKRD20A4P"
type: "gene"
col: 10199
ensembl_id: "ENSG00000172014"
name: "ankyrin repeat domain 20 family member A4, pseudogene"
location: "9q13"
module: 196
arm: "+"
pooled_cpm: 3.8
n_lines_expressing: 26
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 8
direction_downstream: 9
tags: ["gene", "module/196"]
generated_by: "tahoemap"
---

# ANKRD20A4P

*ankyrin repeat domain 20 family member A4, pseudogene* — 9q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.96× (z +10.2, q 1e-21, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.59× (z +6.4, q 4e-08, up in 10 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.588× (z -5.2, q 1e-04, down in 10 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.0700×, PANC-1 0.189×, Hs 766T 0.0900×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.198×, SW480 0.181×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 1 line (PANC-1 0.199×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.275×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.109×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD20A1]] (+0.79, fdr 7e-06), [[CNTNAP3B]] (+0.54, fdr 2e-05), [[SYT9]] (+0.51, fdr 3e-05); moves opposite to [[SPAG16]] (-0.49, fdr 3e-04), [[SDHD]] (-0.47, fdr 1e-04), [[EXOC7]] (-0.45, fdr 7e-05).
> It is in [[Module 196]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CNTNAP3P2]] → it (grade B ⚠); 9 go from it, the strongest it → [[KIF20B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +10.2 | 1e-21 | 1/5 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +6.4 | 4e-08 | 10/23 (SW480, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.66×** | +4.9 | 1e-04 | 0/11 | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +4.8 | 2e-04 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.98×** | +4.8 | 2e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +4.0 | 0.007 | 10/22 (SW480, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.008 | 1/19 (SW48) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.008 | 6/20 (Panc 03.27, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.008 | 7/24 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.026 | 3/16 (CFPAC-1, A549, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +3.5 | 0.026 | 0/8 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.037 | 1/21 (A-427) | inconsistent across doses | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.057 | 2/18 (Hs 766T, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.2 | 0.058 | 1/8 (A549) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.86×** | +3.2 | 0.058 | 0/6 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10199.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.0700×, PANC-1 0.189×, Hs 766T 0.0900×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SK-MEL-2 0.198×, SW480 0.181×; ⚠ toxic; transcription drop); [[Ixazomib citrate (drug)]] 5 µM in 1 line (PANC-1 0.199×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (PANC-1 0.275×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (Hs 766T 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.588×** | -5.2 | 1e-04 | 10/22 (PANC-1, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -4.1 | 0.011 | 6/24 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.723× | -3.2 | 0.27 | 7/23 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.715× | -3.1 | 0.30 | 1/22 (NCI-H2347) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.737× | -3.0 | 0.30 | 9/22 (PANC-1, SW48, …) | top dose only | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.199× (z -11.6) |
| [[SK-MEL-2 (line)]] | alt | 69.1 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.7) ⚠ cell-cycle shift, explains ~48% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.0700× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[Hs 766T (line)]] | wt | 8.09 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0900× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.109× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 4.99 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.508× (z -8.8) ⚠ position not correctable |
| [[SW480 (line)]] | alt | 6.96 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.617 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.377 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.567 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.98 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.689 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.674 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.743 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.464 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.568 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.80 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD20A1]] | +0.79 | +0.71 / +0.75 | both halves | 7e-06 | same gene group; STRING 646 |
| [[CNTNAP3B]] | +0.54 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SYT9]] | +0.51 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[ANKRD20A7P]] | +0.51 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[GLDC]] | +0.50 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[CNTNAP3P2]] | +0.49 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[ADAMTS15]] | +0.49 | +0.36 / +0.35 | both halves | 1e-04 |  |
| [[GNAO1]] | +0.49 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[CNTNAP3C]] | +0.48 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[DPY19L2P1]] | +0.48 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[DBF4]] | +0.47 | +0.44 / +0.39 | both halves | 5e-05 |  |
| [[EEPD1]] | +0.45 | +0.46 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG16]] | -0.49 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[SDHD]] | -0.47 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[EXOC7]] | -0.45 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[MAGED2]] | -0.44 | -0.30 / -0.53 | both halves | 2e-04 |  |
| [[LMAN2]] | -0.44 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[ATXN7L3-AS1]] | -0.41 | -0.33 / -0.24 | both halves | 5e-04 |  |
| [[EFCAB6]] | -0.41 | -0.20 / -0.36 | both halves | 7e-04 |  |
| [[ERVK13-1]] | -0.41 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[PXDNL]] | -0.41 | -0.26 / -0.31 | both halves | 4e-04 |  |
| [[ATXN1L]] | -0.41 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[PEX19]] | -0.40 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[C1D]] | -0.40 | -0.23 / -0.39 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNTNAP3P2]] | B | CNTNAP3P2 activity raises ANKRD20A4P's level | lines that do not express CNTNAP3P2 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without CNTNAP3P2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CNTNAP3B, CNTNAP3, CNTNAP3C |
| [[SEMA6B]] | B | SEMA6B activity raises ANKRD20A4P's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.99× lower at baseline in the lines without SEMA6B | 0.029 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[TERT]] | B | TERT activity raises ANKRD20A4P's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without TERT | 0.057 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[SYT9]] | B | SYT9 activity raises ANKRD20A4P's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 1.83× lower at baseline in the lines without SYT9 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8 |
| [[SOBP]] | B | SOBP activity raises ANKRD20A4P's level | lines that do not express SOBP (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without SOBP | 0.089 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[ANKRD20A1]] | C | ANKRD20A1 activity raises ANKRD20A4P's level | lines that do not express ANKRD20A1 (20) vs lines expressing it (30) | 2.34× lower at baseline in the lines without ANKRD20A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ANKRD20A4P, CTNNA2, SCN8A; co-absent with the target |
| [[CNTNAP3B]] | C | CNTNAP3B activity raises ANKRD20A4P's level | lines that do not express CNTNAP3B (22) vs lines expressing it (28) | 2.27× lower at baseline in the lines without CNTNAP3B | 0.027 | ⚠ within organs, on part of the lines; also absent: CNTNAP3P2, CNTNAP3, CNTNAP3C; co-absent with the target |
| [[ANKRD20A7P]] | C | ANKRD20A7P activity raises ANKRD20A4P's level | lines that do not express ANKRD20A7P (30) vs lines expressing it (20) | 2.18× lower at baseline in the lines without ANKRD20A7P | 0.094 | ⚠ within organs, on part of the lines; also absent: BNC1, MAGEA1, ENSG00000275649; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF20B]] | B | ANKRD20A4P activity raises KIF20B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.32× lower at baseline in the lines without ANKRD20A4P | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[DEPDC1B]] | B | ANKRD20A4P activity raises DEPDC1B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.56× lower at baseline in the lines without ANKRD20A4P | 0.044 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[DEPDC1B]] | B | ANKRD20A4P activity strengthens DEPDC1B's drug response | lines that do not express ANKRD20A4P (24) vs lines expressing it (24) | the lines without ANKRD20A4P respond 0.95× as strongly (z diff +0.17); strongest at Selinexor 5 µM: 0.73x vs 0.58x (z diff +2.5) | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5; target measured in part of the lines; both ways; artifact flags |
| [[G2E3]] | B | ANKRD20A4P activity raises G2E3's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.35× lower at baseline in the lines without ANKRD20A4P | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[KIF18B]] | B | ANKRD20A4P activity raises KIF18B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.35× lower at baseline in the lines without ANKRD20A4P | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[NT5M]] | B | ANKRD20A4P activity raises NT5M's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.53× lower at baseline in the lines without ANKRD20A4P | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[SOBP]] | B | ANKRD20A4P activity raises SOBP's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 2.87× lower at baseline in the lines without ANKRD20A4P | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5 |
| [[ANKRD20A1]] | C | ANKRD20A4P activity raises ANKRD20A1's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 1.98× lower at baseline in the lines without ANKRD20A4P | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5; co-absent with the target |
| [[CNTNAP3B]] | C | ANKRD20A4P activity raises CNTNAP3B's level | lines that do not express ANKRD20A4P (24) vs lines expressing it (26) | 2.93× lower at baseline in the lines without ANKRD20A4P | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000253503, ENSG00000253500, ADGRF5; co-absent with the target |

## Where it sits

- **Module**: [[Module 196]]; 17 genes; every member is in the + arm (projection on the module's main direction 0.532). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, 28.8); signed map (19.8, 58.6). **Vector** length 35.2, 5.69% of its response variance represented; |z| ≥ 3 in 502 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +6.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.5 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.2 | +3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +1.2 | +2.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +2.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +0.6 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.6 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +0.6 | -0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +0.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -1.4 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.8 | +0.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.7 | +0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -0.6 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 20 family member A4, pseudogene |
| Locus type | pseudogene |
| Location | 9q13 — chr9:64,369,675-64,438,574 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | OTTHUMG00000066855; previously ANKRD20A4 |
| Gene groups (HGNC) | N-Ank proteins |
| Matched by | ensembl_id |

UniProt [Q4UJ75](https://www.uniprot.org/uniprotkb/Q4UJ75) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31982](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31982) · Entrez [728747](https://www.ncbi.nlm.nih.gov/gene/728747) · UniProt [Q4UJ75](https://www.uniprot.org/uniprotkb/Q4UJ75) · Ensembl [ENSG00000172014](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172014)

## Data

Gene col 10199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10199); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10199]; `tensor/DDL_lfc|DDL_z.npy` [10199]; `embed/gene_vectors.npy` [10199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10199 or target_col == 10199). Every well: [[ANKRD20A4P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD20A4P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
