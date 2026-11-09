---
symbol: "ADGRB2"
type: "gene"
col: 4293
ensembl_id: "ENSG00000121753"
name: "adhesion G protein-coupled receptor B2"
location: "1p35.2"
module: 100
arm: "+"
pooled_cpm: 3.49
n_lines_expressing: 43
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 15
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# ADGRB2

*adhesion G protein-coupled receptor B2* — 1p35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.66× (z +13.0, q 4e-36, up in 36 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.203×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (C-33 A 0.0642×); [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0617×; ⚠ cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0740×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMCC2]] (+0.75, fdr 7e-06), [[RPS6KA1]] (+0.66, fdr 1e-05), [[SEMA6B]] (+0.65, fdr 1e-05); moves opposite to [[DIMT1]] (-0.56, fdr 3e-05), [[PRR14L]] (-0.55, fdr 2e-05), [[CDK12]] (-0.54, fdr 1e-04).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[APLP1]] → it (grade B ⚠); 15 go from it, the strongest it → [[SMARCD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4293.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.66×** | +13.0 | 4e-36 | 36/38 (J82, HS-578T, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.86×** | +9.9 | 7e-21 | 35/39 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.86×** | +9.9 | 7e-21 | 29/39 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.78×** | +9.6 | 9e-20 | 29/34 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.73×** | +9.5 | 3e-19 | 28/39 (NCI-H1792, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.56×** | +8.9 | 7e-17 | 26/39 (NCI-H1792, HOP62, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.43×** | +8.4 | 5e-15 | 17/27 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.24×** | +7.3 | 2e-11 | 4/7 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **3.26×** | +5.8 | 3e-07 | 15/35 (NCI-H460, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.95×** | +5.8 | 3e-07 | 2/8 (PANC-1, NCI-H2347) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.41×** | +4.6 | 3e-04 | 8/35 (A-427, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.91×** | +4.3 | 6e-04 | 3/18 (J82, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.56×** | +4.2 | 0.001 | 4/15 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.002 | 3/23 (NCI-H460, SHP-77, …) | inconsistent across doses | position effect removed |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +4.1 | 0.002 | 9/24 (NCI-H2030, SW 900, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.008 | 5/21 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 0.5 µM |  | **1.68×** | +3.5 | 0.015 | 1/35 (SW480) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.40×** | +3.2 | 0.048 | 6/37 (HOP62, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.39×** | +3.1 | 0.052 | 2/30 (RPMI-7951, AN3 CA) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4293.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 0.203×); [[Valdecoxib (drug)]] 0.05 µM in 1 line (C-33 A 0.0642×); [[Bortezomib (drug)]] 0.05 µM in 1 line (NCI-H460 0.0617×; ⚠ cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0740×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cinacalcet (drug)]] 0.05 µM |  | 0.679× | -3.7 | 0.14 | 6/37 (NCI-H2030, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4293. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.82 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0617× (z -8.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0740× (z -8.7) |
| [[A498 (line)]] | wt | 6.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.9) |
| [[C-33 A (line)]] | alt | 8.90 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0642× (z -9.7) |
| [[SNU-423 (line)]] | alt | 3.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +9.1) | — |
| [[A-172 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.425 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.622 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.919 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4293), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMCC2]] | +0.75 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[RPS6KA1]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 | same gene group |
| [[SEMA6B]] | +0.65 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[ANO8]] | +0.64 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.64 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[FOXO6]] | +0.61 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[PIK3C2B]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.60 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[SNPH]] | +0.60 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[CDH24]] | +0.60 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[MAP4K2]] | +0.59 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[HMSD]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIMT1]] | -0.56 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PRR14L]] | -0.55 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[CDK12]] | -0.54 | -0.36 / -0.56 | both halves | 1e-04 |  |
| [[SPRY3]] | -0.52 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[COX10]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[DPH5-DT]] | -0.52 | -0.36 / -0.38 | both halves | 1e-04 |  |
| [[GATC]] | -0.52 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[EXOC4]] | -0.51 | -0.31 / -0.57 | both halves | 2e-04 | same gene group |
| [[GATB]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[SUMF1]] | -0.51 | -0.35 / -0.62 | both halves | 1e-04 |  |
| [[UTP20]] | -0.51 | -0.38 / -0.45 | both halves | 7e-05 |  |
| [[MCPH1]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLP1]] | B | APLP1 activity raises ADGRB2's level | lines that do not express APLP1 (12) vs lines expressing it (38) | 2.05× lower at baseline in the lines without APLP1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000291283, CTXN1, SUSD4; maybe low, not absent |
| [[SEMA6B]] | B | SEMA6B activity raises ADGRB2's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without SEMA6B | 0.006 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[PAX2]] | B | PAX2 activity raises ADGRB2's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 1.78× lower at baseline in the lines without PAX2 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2 |
| [[SYTL4]] | B | SYTL4 activity lowers ADGRB2's level | lines that do not express SYTL4 (10) vs lines expressing it (40) | 1.43× higher at baseline in the lines without SYTL4 | 0.044 | ⚠ within organs, on part of the lines; also absent: PTPRE, PLEKHA6 |
| [[REEP2]] | B | REEP2 activity raises ADGRB2's level | lines that do not express REEP2 (12) vs lines expressing it (38) | 1.65× lower at baseline in the lines without REEP2 | 0.051 | ⚠ within organs, on part of the lines; also absent: DLK2, ENSG00000234405, STARD9; maybe low, not absent |
| [[ATP1A3]] | B | ATP1A3 activity raises ADGRB2's level | lines that do not express ATP1A3 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without ATP1A3 | 0.083 | ⚠ within organs, on part of the lines; also absent: KIF26A; maybe low, not absent |
| [[SUSD4]] | B | SUSD4 activity raises ADGRB2's level | lines that do not express SUSD4 (11) vs lines expressing it (39) | 1.90× lower at baseline in the lines without SUSD4 | 0.083 | ⚠ within organs, on part of the lines; also absent: SLC17A7, LINC00595, EBF4; maybe low, not absent |
| [[BCAM]] | B | BCAM activity raises ADGRB2's level | lines that do not express BCAM (8) vs lines expressing it (42) | 1.88× lower at baseline in the lines without BCAM | 0.091 | ⚠ within organs, on part of the lines; also absent: DNMT3B; maybe low, not absent |
| [[DNMT3B]] | C | DNMT3B activity raises ADGRB2's level | lines that do not express DNMT3B (4) vs lines expressing it (46) | 2.33× lower at baseline in the lines without DNMT3B | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CCDC113, SLC29A4, MYBL2; maybe low, not absent |
| [[CD83]] | C | CD83 activity raises ADGRB2's level | lines that do not express CD83 (4) vs lines expressing it (46) | 2.57× lower at baseline in the lines without CD83 | 0.095 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1 |
| [[SMARCD3]] | C | SMARCD3 activity raises ADGRB2's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 2.45× lower at baseline in the lines without SMARCD3 | 0.097 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMARCD3]] | B | ADGRB2 activity raises SMARCD3's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.70× lower at baseline in the lines without ADGRB2 | 0.004 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[APLP1]] | B | ADGRB2 activity raises APLP1's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 3.50× lower at baseline in the lines without ADGRB2 | 0.008 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[PLA2G4B]] | B | ADGRB2 activity lowers PLA2G4B's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.25× higher at baseline in the lines without ADGRB2 | 0.025 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[EFCAB2]] | B | ADGRB2 activity raises EFCAB2's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without ADGRB2 | 0.027 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[EXOC4]] | B | ADGRB2 activity raises EXOC4's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without ADGRB2 | 0.044 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[ATP1A3]] | B | ADGRB2 activity raises ATP1A3's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without ADGRB2 | 0.048 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[MAST1]] | B | ADGRB2 activity raises MAST1's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.16× lower at baseline in the lines without ADGRB2 | 0.068 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[MAPK11]] | B | ADGRB2 activity raises MAPK11's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.55× lower at baseline in the lines without ADGRB2 | 0.074 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[FOXO6]] | B | ADGRB2 activity raises FOXO6's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without ADGRB2 | 0.074 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| cells under [[Sodium Salicylate (drug)]] 0.5 µM | B | ADGRB2 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express ADGRB2 (7) vs lines expressing it (41) | the lines without ADGRB2: 1.16× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[DIMT1]] | B | ADGRB2 activity raises DIMT1's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.40× lower at baseline in the lines without ADGRB2 | 0.083 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[KIAA1522]] | B | ADGRB2 activity lowers KIAA1522's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 2.60× higher at baseline in the lines without ADGRB2 | 0.085 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.719). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.1, -4.2); signed map (-26.2, 20.9). **Vector** length 59.3, 10.1% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +13.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +9.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +9.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +8.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.6 | +3.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.7 | -1.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 0.05 µM |  | -1.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | adhesion G protein-coupled receptor B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.2 — chr1:31,727,117-31,764,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously BAI2 |
| Gene groups (HGNC) | Adhesion G protein-coupled receptors, subfamily B; MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [O60241](https://www.uniprot.org/uniprotkb/O60241) (Adhesion G protein-coupled receptor B2):

> Orphan G protein-coupled receptor involved in cell adhesion and probably in cell-cell interactions. Activates NFAT-signaling pathway, a transcription factor, via the G protein GNAZ. Involved in angiogenesis inhibition (By similarity).

**Summary**, from NCBI Gene [576](https://www.ncbi.nlm.nih.gov/gene/576):

> This gene encodes a a seven-span transmembrane protein that is thought to be a member of the secretin receptor family. The encoded protein is a brain-specific inhibitor of angiogenesis. The mature peptide may be further cleaved into additional products (PMID:20367554). Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:944](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:944) · Entrez [576](https://www.ncbi.nlm.nih.gov/gene/576) · UniProt [O60241](https://www.uniprot.org/uniprotkb/O60241) · Ensembl [ENSG00000121753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121753)

## Data

Gene col 4293: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4293); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4293, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4293]; `tensor/DDL_lfc|DDL_z.npy` [4293]; `embed/gene_vectors.npy` [4293]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4293 or target_col == 4293). Every well: [[ADGRB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
