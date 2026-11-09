---
symbol: "MUC3A"
type: "gene"
col: 9867
ensembl_id: "ENSG00000169894"
name: "mucin 3A, cell surface associated"
location: "7q22.1"
module: 44
arm: "+"
pooled_cpm: 6.31
n_lines_expressing: 25
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 101
direction_downstream: 107
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MUC3A

*mucin 3A, cell surface associated* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.84× (z +12.6, q 1e-33, up in 16 of 22 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HT-29 0.0922×, COLO 205 0.0363×, LoVo 0.285×, KATO III 0.128×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.275×, HT-29 0.255×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.0767×; ⚠ toxic); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.253×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHG6]] (+0.81, fdr 7e-06), [[CLDN3]] (+0.78, fdr 7e-06), [[TJP3]] (+0.75, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 101 arrows point to it, the strongest [[UGT1A6]] → it (grade B ⚠); 107 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9867.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.84×** | +12.6 | 1e-33 | 16/22 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.80×** | +8.8 | 4e-16 | 13/22 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.52×** | +7.6 | 6e-12 | 2/9 (LS 180, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.09×** | +6.3 | 4e-08 | 2/11 (LS 180, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.97×** | +5.8 | 8e-07 | 5/22 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +5.6 | 2e-06 | 6/22 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +5.5 | 3e-06 | 4/22 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +5.4 | 5e-06 | 2/9 (LS 180, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +5.2 | 1e-05 | 4/13 (PANC-1, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +4.9 | 4e-05 | 1/17 (A498) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +4.9 | 5e-05 | 6/22 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.17×** | +4.7 | 1e-04 | 3/10 (SW1417, A549, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.5 | 3e-04 | 1/16 (NCI-H1573) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.06×** | +4.4 | 4e-04 | 1/17 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.32×** | +3.7 | 0.008 | 0/9 | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.80×** | +3.6 | 0.013 | 4/19 (HT-29, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.76×** | +3.4 | 0.020 | 3/17 (LoVo, PANC-1, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.021 | 1/19 (A498) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.48×** | +3.3 | 0.029 | 2/19 (NCI-H1573, NCI-H23) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +2.9 | 0.089 | 1/16 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.42×** | +2.9 | 0.089 | 4/17 (LS 180, NCI-H2347, …) | inconsistent across doses |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.41×** | +2.9 | 0.095 | 3/21 (A498, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9867.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 5 lines (HT-29 0.0922×, COLO 205 0.0363×, LoVo 0.285×, KATO III 0.128×, …); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (LS 180 0.275×, HT-29 0.255×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A498 0.0767×; ⚠ toxic); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.253×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.654× | -3.4 | 0.35 | 2/22 (Panc 03.27, SHP-77) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | 0.503× | -3.1 | 0.38 | 7/16 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9867. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 17.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -15.7) |
| [[LoVo (line)]] | wt | 22.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -11.5) |
| [[LS 180 (line)]] | wt | 58.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -9.9) |
| [[A498 (line)]] | wt | 5.99 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0767× (z -11.7) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0363× (z -15.1) |
| [[KATO III (line)]] | alt | 55.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -9.8) |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.130× (z -9.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 0.444 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.861 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.572 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.429 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.554 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.516 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.37 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9867), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHG6]] | +0.81 | +0.70 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CLDN3]] | +0.78 | +0.74 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TJP3]] | +0.75 | +0.64 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SLC44A4]] | +0.75 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[PRR15L]] | +0.75 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[LINC01559]] | +0.74 | +0.74 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[FXYD3]] | +0.74 | +0.78 / +0.67 | both halves | 7e-06 |  |
| [[MUC13]] | +0.73 | +0.79 / +0.65 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 920 |
| [[ATP10B]] | +0.72 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[USH1C]] | +0.72 | +0.62 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[LGALS4]] | +0.72 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[MYH14]] | +0.72 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*101 arrows, 101 of them with an alert ⚠; grade A 0, B 8, C 93. Shown: the 12 strongest; 89 more arrows (89 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UGT1A6]] | B | UGT1A6 activity raises MUC3A's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 2.60× lower at baseline in the lines without UGT1A6 | 0.031 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1 |
| [[MYO7B]] | B | MYO7B activity raises MUC3A's level | lines that do not express MYO7B (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without MYO7B | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CLRN3, LINC01559, PHGR1 |
| [[UGT1A1]] | B | UGT1A1 activity raises MUC3A's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 2.95× lower at baseline in the lines without UGT1A1 | 0.040 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1 |
| [[MMP28]] | B | MMP28 activity raises MUC3A's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without MMP28 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[SLC28A3]] | B | SLC28A3 activity raises MUC3A's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.65× lower at baseline in the lines without SLC28A3 | 0.075 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[JUP]] | B | JUP activity raises MUC3A's level | lines that do not express JUP (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without JUP | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: ELF3, SHROOM3, ENSG00000253671 |
| [[PLS1]] | B | PLS1 activity raises MUC3A's level | lines that do not express PLS1 (14) vs lines expressing it (36) | 2.40× lower at baseline in the lines without PLS1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: NRARP, MYO5C, MLXIPL |
| [[ZDHHC11B]] | B | ZDHHC11B activity raises MUC3A's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 2.60× lower at baseline in the lines without ZDHHC11B | 0.097 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[MUC13]] | C | MUC13 activity raises MUC3A's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 7.06× lower at baseline in the lines without MUC13 | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises MUC3A's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 5.24× lower at baseline in the lines without GCNT3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[CDH17]] | C | CDH17 activity raises MUC3A's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 6.51× lower at baseline in the lines without CDH17 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3; co-absent with the target |
| [[TRIM31]] | C | TRIM31 activity raises MUC3A's level | lines that do not express TRIM31 (39) vs lines expressing it (11) | 6.15× lower at baseline in the lines without TRIM31 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, GCNT3, NPSR1; co-absent with the target |

### Downstream of this gene

*107 arrows, 107 of them with an alert ⚠; grade A 0, B 29, C 78. Shown: the 12 strongest; 95 more arrows (95 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | MUC3A activity raises EPS8L1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without MUC3A | 0.003 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[PLS1]] | B | MUC3A activity raises PLS1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 3.36× lower at baseline in the lines without MUC3A | 0.005 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[CYSTM1]] | B | MUC3A activity raises CYSTM1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.10× lower at baseline in the lines without MUC3A | 0.008 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[FZD5]] | B | MUC3A activity raises FZD5's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.05× lower at baseline in the lines without MUC3A | 0.009 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[FAM83E]] | B | MUC3A activity raises FAM83E's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without MUC3A | 0.012 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[BICDL2]] | B | MUC3A activity raises BICDL2's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.51× lower at baseline in the lines without MUC3A | 0.013 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[SYNGR2]] | B | MUC3A activity raises SYNGR2's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without MUC3A | 0.020 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[CAMK2N1]] | B | MUC3A activity raises CAMK2N1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without MUC3A | 0.022 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[MANSC1]] | B | MUC3A activity raises MANSC1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without MUC3A | 0.029 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[HDHD3]] | B | MUC3A activity raises HDHD3's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.71× lower at baseline in the lines without MUC3A | 0.029 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[PROM2]] | B | MUC3A activity raises PROM2's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 1.88× lower at baseline in the lines without MUC3A | 0.034 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |
| [[ELF3-AS1]] | B | MUC3A activity raises ELF3-AS1's level | lines that do not express MUC3A (25) vs lines expressing it (25) | 2.32× lower at baseline in the lines without MUC3A | 0.035 | ⚠ within organs, on part of the lines; also absent: HSH2D, ADGRF1, CKMT1B |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.7, 52.9); signed map (61.9, 6.0). **Vector** length 45.7, 9.92% of its response variance represented; |z| ≥ 3 in 443 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.54 to 4); *Aspirin ADME* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +12.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +5.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.3 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.4 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | mucin 3A, cell surface associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,949,534-100,968,347 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MUC3 |
| Gene groups (HGNC) | Mucins; SEA domain containing |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02505](https://www.uniprot.org/uniprotkb/Q02505) (Mucin-3A):

> Major glycoprotein component of a variety of mucus gels. Thought to provide a protective, lubricating barrier against particles and infectious agents at mucosal surfaces. May be involved in ligand binding and intracellular signaling.

**Summary**, from NCBI Gene [4584](https://www.ncbi.nlm.nih.gov/gene/4584):

> The mucin genes encode epithelial glycoproteins, some of which are secreted and some membrane bound. Each of the genes contains at least one large domain of tandemly repeated sequence that encodes the peptide sequence rich in serine and/or threonine residues, which carries most of the O-linked glycosylation (Gendler and Spicer, 1995 [PubMed 7778880]).[supplied by OMIM, Aug 2008]

**Accessions** — [HGNC:7513](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7513) · Entrez [4584](https://www.ncbi.nlm.nih.gov/gene/4584) · UniProt [Q02505](https://www.uniprot.org/uniprotkb/Q02505) · Ensembl [ENSG00000169894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169894)

## Data

Gene col 9867: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9867); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9867, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9867]; `tensor/DDL_lfc|DDL_z.npy` [9867]; `embed/gene_vectors.npy` [9867]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9867 or target_col == 9867). Every well: [[MUC3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
