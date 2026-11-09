---
symbol: "DENND2D"
type: "gene"
col: 8578
ensembl_id: "ENSG00000162777"
name: "DENN domain containing 2D"
location: "1p13.3-p13.2"
module: 55
arm: "+"
pooled_cpm: 4.22
n_lines_expressing: 29
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 22
direction_downstream: 37
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# DENND2D

*DENN domain containing 2D* — 1p13.3-p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.87× (z +10.7, q 9e-24, up in 1 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 1.69× (z +3.9, q 0.013, up in 0 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.411× (z -9.3, q 5e-18, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFTR]] (+0.73, fdr 7e-06), [[TMEM30B]] (+0.70, fdr 8e-06), [[SYK]] (+0.70, fdr 7e-06); moves opposite to [[DNAAF9]] (-0.65, fdr 1e-05), [[ZNF8-DT]] (-0.55, fdr 4e-05), [[FAM228B]] (-0.53, fdr 1e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[TJP2]] → it (grade B ⚠); 37 go from it, the strongest it → [[ADAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.87×** | +10.7 | 9e-24 | 1/5 (CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.94×** | +7.0 | 9e-10 | 4/14 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +6.8 | 2e-09 | 6/11 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +3.9 | 0.013 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.6 | 0.030 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.037 | 3/22 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.049 | 6/25 (KATO III, CFPAC-1, …) | rises with dose |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.049 | 2/24 (J82, HCT15) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.11 | 2/26 (LoVo, A498) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 1.27× | +3.1 | 0.12 | 0/25 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.411×** | -9.3 | 5e-18 | 18/26 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.483×** | -7.7 | 5e-12 | 16/26 (SNU-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -7.3 | 5e-11 | 18/26 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.628×** | -4.9 | 1e-04 | 11/26 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -3.9 | 0.008 | 9/26 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.689×** | -3.9 | 0.008 | 15/26 (LoVo, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.770×** | -3.9 | 0.008 | 17/22 (HT-29, SNU-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.058 | 1/26 (CFPAC-1) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.548×** | -3.3 | 0.059 | 8/24 (LS 180, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.742×** | -3.1 | 0.094 | 9/26 (SNU-1, HT-29, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.752× | -3.0 | 0.14 | 8/24 (NCI-H23, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 72.0 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0751× (z -15.0) |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0549× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.121× (z -11.3) |
| [[LoVo (line)]] | wt | 9.83 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0541× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0980× (z -12.2) |
| [[SW480 (line)]] | alt | 4.60 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.142× (z -10.8) |
| [[BT-474 (line)]] | alt | 9.86 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0228× (z -15.8) |
| [[HCT15 (line)]] | alt | 8.64 | 0 | 2 | — | [[Ferulic acid (drug)]] 0.05 µM 0.0644× (z -9.1) |
| [[HT-29 (line)]] | alt | 25.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0923× (z -12.0) |
| [[KATO III (line)]] | alt | 8.44 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0898× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~14% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.142× (z -9.6) |
| [[A-427 (line)]] | wt | 6.76 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0307× (z -15.3) |
| [[COLO 205 (line)]] | alt | 5.17 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 2.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0811× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 0.601 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.381 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.826 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.723 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFTR]] | +0.73 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[TMEM30B]] | +0.70 | +0.72 / +0.58 | both halves | 8e-06 |  |
| [[SYK]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[PLCH1]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[TNFRSF14-AS1]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[LINC02331]] | +0.68 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[KCNE3]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[GPX2]] | +0.67 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[SH2D4A]] | +0.66 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[PROM1]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[LINC01819]] | +0.65 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[ABO]] | +0.64 | +0.64 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF9]] | -0.65 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[ZNF8-DT]] | -0.55 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[FAM228B]] | -0.53 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[EPOR]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 5, C 17. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP2]] | B | TJP2 activity raises DENND2D's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without TJP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[ANK3]] | B | ANK3 activity raises DENND2D's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.01× lower at baseline in the lines without ANK3 | 0.055 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[SHROOM3]] | B | SHROOM3 activity raises DENND2D's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without SHROOM3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[PPP1R9A]] | B | PPP1R9A activity raises DENND2D's level | lines that do not express PPP1R9A (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without PPP1R9A | 0.068 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[INPP4B]] | B | INPP4B activity raises DENND2D's level | lines that do not express INPP4B (10) vs lines expressing it (40) | 1.40× lower at baseline in the lines without INPP4B | 0.091 | ⚠ within organs, on part of the lines; also absent: RAB32, CD82, IFIT2 |
| [[LINC02331]] | C | LINC02331 activity raises DENND2D's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 3.25× lower at baseline in the lines without LINC02331 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[ACTR3C]] | C | ACTR3C activity raises DENND2D's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 2.67× lower at baseline in the lines without ACTR3C | 0.009 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325; co-absent with the target |
| [[SLC52A3]] | C | SLC52A3 activity raises DENND2D's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.95× lower at baseline in the lines without SLC52A3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises DENND2D's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.86× lower at baseline in the lines without CLIC5 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[BMP4]] | C | BMP4 activity raises DENND2D's level | lines that do not express BMP4 (31) vs lines expressing it (19) | 3.31× lower at baseline in the lines without BMP4 | 0.016 | ⚠ within organs, on part of the lines; also absent: TRIM15, ENSG00000287426, TMEM45B; co-absent with the target |
| [[PRKCH-AS1]] | C | PRKCH-AS1 activity raises DENND2D's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 2.91× lower at baseline in the lines without PRKCH-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises DENND2D's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 3.55× lower at baseline in the lines without TMEM30B | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 16, C 21. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAP1]] | B | DENND2D activity raises ADAP1's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.23× lower at baseline in the lines without DENND2D | 0.016 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[TMEM184A]] | B | DENND2D activity raises TMEM184A's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.06× lower at baseline in the lines without DENND2D | 0.033 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[ANO9]] | B | DENND2D activity raises ANO9's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.52× lower at baseline in the lines without DENND2D | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[BCL2L15]] | B | DENND2D activity raises BCL2L15's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without DENND2D | 0.038 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[ABHD11]] | B | DENND2D activity raises ABHD11's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.02× lower at baseline in the lines without DENND2D | 0.039 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[TNFRSF14-AS1]] | B | DENND2D activity raises TNFRSF14-AS1's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 1.72× lower at baseline in the lines without DENND2D | 0.046 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[LRP5]] | B | DENND2D activity raises LRP5's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.25× lower at baseline in the lines without DENND2D | 0.048 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[PPP1R9A]] | B | DENND2D activity raises PPP1R9A's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.38× lower at baseline in the lines without DENND2D | 0.050 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[STEAP2]] | B | DENND2D activity raises STEAP2's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 2.11× lower at baseline in the lines without DENND2D | 0.052 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[IQCH-AS1]] | B | DENND2D activity raises IQCH-AS1's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without DENND2D | 0.054 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[BAIAP2L2]] | B | DENND2D activity raises BAIAP2L2's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 1.75× lower at baseline in the lines without DENND2D | 0.063 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |
| [[INPP4B]] | B | DENND2D activity raises INPP4B's level | lines that do not express DENND2D (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without DENND2D | 0.065 | ⚠ within organs, on part of the lines; also absent: SAMD12, SLC52A3, AREG |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.0, 49.1); signed map (62.8, 7.7). **Vector** length 56.5, 11.9% of its response variance represented; |z| ≥ 3 in 606 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +1.3 |
| fall | [[TAK-733 (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -0.9 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -0.9 | -3.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.9 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DENN domain containing 2D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3-p13.2 — chr1:111,185,969-111,204,535 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22457, RP5-1180E21.2 |
| Gene groups (HGNC) | DENN domain containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6A0](https://www.uniprot.org/uniprotkb/Q9H6A0) (DENN domain-containing protein 2D):

> Guanine nucleotide exchange factor (GEF) which may activate RAB9A and RAB9B. Promotes the exchange of GDP to GTP, converting inactive GDP-bound Rab proteins into their active GTP-bound form.

**Summary**, from NCBI Gene [79961](https://www.ncbi.nlm.nih.gov/gene/79961):

> Enables guanyl-nucleotide exchange factor activity. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26192](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26192) · Entrez [79961](https://www.ncbi.nlm.nih.gov/gene/79961) · UniProt [Q9H6A0](https://www.uniprot.org/uniprotkb/Q9H6A0) · Ensembl [ENSG00000162777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162777)

## Data

Gene col 8578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8578); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8578]; `tensor/DDL_lfc|DDL_z.npy` [8578]; `embed/gene_vectors.npy` [8578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8578 or target_col == 8578). Every well: [[DENND2D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DENND2D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
