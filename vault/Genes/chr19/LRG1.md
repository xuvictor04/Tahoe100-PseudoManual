---
symbol: "LRG1"
type: "gene"
col: 10079
ensembl_id: "ENSG00000171236"
name: "leucine rich alpha-2-glycoprotein 1"
location: "19p13.3"
module: 8
arm: "+"
pooled_cpm: 3.43
n_lines_expressing: 22
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 59
direction_downstream: 51
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# LRG1

*leucine rich alpha-2-glycoprotein 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.68× (z +13.0, q 4e-36, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.551× (z -4.0, q 0.037, down in 12 of 19 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (KATO III 0.0179×, HT-29 0.0333×); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (KATO III 0.0426×, COLO 205 0.0918×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (COLO 205 0.0914×, HCT15 0.0463×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0410×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF183]] (+0.70, fdr 7e-06), [[TRIM15]] (+0.64, fdr 1e-05), [[HLA-DRB1]] (+0.64, fdr 8e-05); moves opposite to [[DNAJA4]] (-0.47, fdr 6e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 59 arrows point to it, the strongest [[ATAD3C]] → it (grade B ⚠); 51 go from it, the strongest it → [[AQP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.68×** | +13.0 | 4e-36 | 16/19 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.12×** | +10.9 | 2e-25 | 16/19 (CFPAC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.47×** | +9.9 | 9e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.73×** | +9.7 | 3e-20 | 17/19 (HT-29, KATO III, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **3.80×** | +9.2 | 6e-18 | 15/19 (HepG2/C3A, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.58×** | +6.5 | 7e-09 | 0/10 | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +6.4 | 2e-08 | 5/17 (HEC-1-A, HT-29, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.47×** | +6.2 | 3e-08 | 16/19 (BT-474, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.47×** | +6.2 | 3e-08 | 14/17 (HT-29, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.29×** | +5.3 | 8e-06 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.88×** | +4.3 | 8e-04 | 2/12 (HEC-1-A, SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.017 | 2/15 (HepG2/C3A, CFPAC-1) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +3.4 | 0.032 | 7/18 (HEC-1-A, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.31×** | +3.3 | 0.040 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +3.3 | 0.040 | 3/12 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **1.55×** | +3.0 | 0.092 | 1/19 (COLO 205) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10079.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ixazomib citrate (drug)]] 5 µM in 2 lines (KATO III 0.0179×, HT-29 0.0333×); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (KATO III 0.0426×, COLO 205 0.0918×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Verteporfin (drug)]] 5 µM in 2 lines (COLO 205 0.0914×, HCT15 0.0463×); [[Digitoxin (drug)]] 0.5 µM in 1 line (SW480 0.0410×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.551×** | -4.0 | 0.037 | 12/19 (SW480, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.702× | -3.4 | 0.13 | 13/19 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.611× | -3.4 | 0.13 | 8/18 (BT-474, CFPAC-1, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.396× | -3.3 | 0.13 | 5/18 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.627× | -3.1 | 0.20 | 12/18 (BT-474, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.645× | -3.0 | 0.25 | 10/19 (COLO 205, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 31.4 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.86× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 23.8 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 10.8× (z +9.8) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0953× (z -9.6) |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 3 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.0914× (z -8.8) |
| [[KATO III (line)]] | alt | 10.1 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.48× (z +8.9) | [[Ixazomib citrate (drug)]] 5 µM 0.0179× (z -16.8) |
| [[HT-29 (line)]] | alt | 16.4 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 7.54× (z +12.9) | [[Ixazomib citrate (drug)]] 5 µM 0.0333× (z -15.4) |
| [[SW480 (line)]] | alt | 2.19 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0410× (z -10.4) |
| [[BT-474 (line)]] | alt | 6.68 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0486× (z -9.0) |
| [[HCT15 (line)]] | alt | 7.89 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0463× (z -8.8) |
| [[A-172 (line)]] | wt | 0.457 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.498 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.542 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.732 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.847 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.612 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.375 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.441 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.268 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.634 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.284 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.353 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF183]] | +0.70 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[TRIM15]] | +0.64 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[HLA-DRB1]] | +0.64 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[TJP3]] | +0.64 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[STEAP4]] | +0.62 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[ELF3-AS1]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[BCL2L15]] | +0.60 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MUC1]] | +0.60 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[CYP4F12]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TCN1]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SLC52A3]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[HLA-DRA]] | +0.58 | +0.46 / +0.50 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJA4]] | -0.47 | -0.46 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*59 arrows, 59 of them with an alert ⚠; grade A 0, B 5, C 54. Shown: the 12 strongest; 47 more arrows (47 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATAD3C]] | B | ATAD3C activity raises LRG1's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 2.42× lower at baseline in the lines without ATAD3C | 0.032 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[AQP3]] | B | AQP3 activity raises LRG1's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without AQP3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[CFB]] | B | CFB activity raises LRG1's level | lines that do not express CFB (20) vs lines expressing it (30) | 1.93× lower at baseline in the lines without CFB | 0.040 | ⚠ within organs, on part of the lines; also absent: SAA4, RHBDL2, IL2RG |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises LRG1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without ELF3-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[FLRT3]] | B | FLRT3 activity raises LRG1's level | lines that do not express FLRT3 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without FLRT3 | 0.064 | ⚠ within organs, on part of the lines; also absent: ARHGAP30, TMC5, ENSG00000259925 |
| [[TMEM139]] | C | TMEM139 activity raises LRG1's level | lines that do not express TMEM139 (33) vs lines expressing it (17) | 3.85× lower at baseline in the lines without TMEM139 | 8e-04 | ⚠ within organs, on part of the lines; also absent: EPS8L3, LINC02964, HNF4A; co-absent with the target |
| [[SERPINA5]] | C | SERPINA5 activity raises LRG1's level | lines that do not express SERPINA5 (37) vs lines expressing it (13) | 3.66× lower at baseline in the lines without SERPINA5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02899, SERPINA1, ENSG00000286546; co-absent with the target |
| [[LINC01814]] | C | LINC01814 activity raises LRG1's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 3.57× lower at baseline in the lines without LINC01814 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises LRG1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.23× lower at baseline in the lines without MUC5B | 0.002 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises LRG1's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 4.36× lower at baseline in the lines without SLC6A14 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[TMEM45B]] | C | TMEM45B activity raises LRG1's level | lines that do not express TMEM45B (32) vs lines expressing it (18) | 3.74× lower at baseline in the lines without TMEM45B | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TRIM15, CDH1, ENSG00000267881; co-absent with the target |
| [[TJP3]] | C | TJP3 activity raises LRG1's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 3.45× lower at baseline in the lines without TJP3 | 0.003 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1; co-absent with the target |

### Downstream of this gene

*51 arrows, 51 of them with an alert ⚠; grade A 0, B 16, C 35. Shown: the 12 strongest; 39 more arrows (39 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | LRG1 activity raises AQP3's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.49× lower at baseline in the lines without LRG1 | 0.003 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[SCIN]] | B | LRG1 activity raises SCIN's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without LRG1 | 0.011 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[PROM2]] | B | LRG1 activity raises PROM2's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.28× lower at baseline in the lines without LRG1 | 0.015 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[CARD14]] | B | LRG1 activity raises CARD14's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.86× lower at baseline in the lines without LRG1 | 0.016 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[ELF3-AS1]] | B | LRG1 activity raises ELF3-AS1's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 3.08× lower at baseline in the lines without LRG1 | 0.016 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[BCL2L15]] | B | LRG1 activity raises BCL2L15's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without LRG1 | 0.041 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[ATAD3C]] | B | LRG1 activity raises ATAD3C's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without LRG1 | 0.053 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[CYP2J2]] | B | LRG1 activity raises CYP2J2's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without LRG1 | 0.059 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[PPP1R3B-DT]] | B | LRG1 activity raises PPP1R3B-DT's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.83× lower at baseline in the lines without LRG1 | 0.065 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| cells under [[Afatinib (drug)]] 0.5 µM | B | LRG1 activity lowers the cells' numbers under Afatinib 0.5 µM (makes them more sensitive) | lines that do not express LRG1 (28) vs lines expressing it (20) | the lines without LRG1: 1.12× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| [[LYPD5]] | B | LRG1 activity raises LYPD5's level | lines that do not express LRG1 (28) vs lines expressing it (22) | 1.70× lower at baseline in the lines without LRG1 | 0.076 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |
| cells under [[Amsacrine (drug)]] 5 µM | B | LRG1 activity raises the cells' numbers under Amsacrine 5 µM (protects the cells) | lines that do not express LRG1 (28) vs lines expressing it (20) | the lines without LRG1: 0.85× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: RORC, LAD1, EPCAM |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.522). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.3, 54.8); signed map (61.3, -2.2). **Vector** length 58.4, 17.0% of its response variance represented; |z| ≥ 3 in 553 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +6.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +9.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.4 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +1.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -1.6 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich alpha-2-glycoprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,536,402-4,540,036 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LRG |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

UniProt [P02750](https://www.uniprot.org/uniprotkb/P02750) carries no function annotation.

**Summary**, from NCBI Gene [116844](https://www.ncbi.nlm.nih.gov/gene/116844):

> The leucine-rich repeat (LRR) family of proteins, including LRG1, have been shown to be involved in protein-protein interaction, signal transduction, and cell adhesion and development. LRG1 is expressed during granulocyte differentiation (O'Donnell et al., 2002 [PubMed 12223515]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29480) · Entrez [116844](https://www.ncbi.nlm.nih.gov/gene/116844) · UniProt [P02750](https://www.uniprot.org/uniprotkb/P02750) · Ensembl [ENSG00000171236](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171236)

## Data

Gene col 10079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10079); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10079]; `tensor/DDL_lfc|DDL_z.npy` [10079]; `embed/gene_vectors.npy` [10079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10079 or target_col == 10079). Every well: [[LRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
