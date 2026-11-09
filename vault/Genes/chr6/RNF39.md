---
symbol: "RNF39"
type: "gene"
col: 12903
ensembl_id: "ENSG00000204618"
name: "ring finger protein 39"
location: "6p22.1"
module: 8
arm: "+"
pooled_cpm: 2.61
n_lines_expressing: 20
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 76
direction_downstream: 119
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RNF39

*ring finger protein 39* — 6p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.96× (z +10.2, q 2e-21, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +6.7, q 2e-09, up in 6 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0680×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.209×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.126×; ⚠ toxic; transcription drop); [[EX229 (drug)]] 5 µM in 1 line (NCI-H2347 0.0663×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRF1]] (+0.71, fdr 7e-06), [[NECTIN4]] (+0.69, fdr 7e-06), [[JUP]] (+0.66, fdr 1e-05); moves opposite to [[TAS2R14]] (-0.51, fdr 2e-05), [[PMS1]] (-0.46, fdr 5e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 76 arrows point to it, the strongest [[SEMA3B]] → it (grade B ⚠); 119 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.96×** | +10.2 | 2e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.65×** | +7.5 | 2e-11 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +7.0 | 6e-10 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.46×** | +6.9 | 7e-10 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +6.7 | 2e-09 | 6/15 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.51×** | +5.0 | 5e-05 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.47×** | +4.9 | 6e-05 | 1/9 (SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.9 | 8e-05 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +4.6 | 2e-04 | 10/16 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.77×** | +4.4 | 7e-04 | 11/14 (LS 180, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +4.3 | 7e-04 | 2/10 (BT-474, AsPC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.01×** | +3.8 | 0.007 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.5 | 0.016 | 1/8 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.5 | 0.016 | 1/12 (BT-474) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Entrectinib (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.017 | 2/14 (CFPAC-1, Panc 03.27) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.024 | 1/15 (Panc 03.27) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.84×** | +3.3 | 0.028 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.51×** | +3.1 | 0.050 | 0/10 | inconsistent across doses | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.064 | 1/13 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12903.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2347 0.0680×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 0.209×); [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H2347 0.126×; ⚠ toxic; transcription drop); [[EX229 (drug)]] 5 µM in 1 line (NCI-H2347 0.0663×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.619× | -3.7 | 0.13 | 13/17 (NCI-H2347, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0680× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.209× (z -13.5) |
| [[A-172 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.293 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.345 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.522 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.413 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.490 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.413 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.427 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.340 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.365 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.353 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.827 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRF1]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[NECTIN4]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[JUP]] | +0.66 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DAPP1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TACSTD2]] | +0.64 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SPINT1]] | +0.63 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[LIPH]] | +0.63 | +0.58 / +0.68 | both halves | 8e-06 |  |
| [[ST14]] | +0.62 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CLDN4]] | +0.62 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[GRHL3]] | +0.62 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[HHLA2]] | +0.61 | +0.57 / +0.62 | both halves | 9e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAS2R14]] | -0.51 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[PMS1]] | -0.46 | -0.40 / -0.44 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*76 arrows, 76 of them with an alert ⚠; grade A 0, B 4, C 72. Shown: the 12 strongest; 64 more arrows (64 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA3B]] | B | SEMA3B activity raises RNF39's level | lines that do not express SEMA3B (19) vs lines expressing it (31) | 1.86× lower at baseline in the lines without SEMA3B | 0.022 | ⚠ within organs, on part of the lines; also absent: SERPINA1, CSF1R, TNNT2; maybe low, not absent |
| [[MUC20]] | B | MUC20 activity raises RNF39's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without MUC20 | 0.079 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[EPS8L1]] | B | EPS8L1 activity raises RNF39's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without EPS8L1 | 0.091 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises RNF39's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 1.93× lower at baseline in the lines without GRHL3 | 0.092 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[TMPRSS2]] | C | TMPRSS2 activity raises RNF39's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.06× lower at baseline in the lines without TMPRSS2 | 8e-05 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises RNF39's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.63× lower at baseline in the lines without SLC44A4 | 1e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[CDH1]] | C | CDH1 activity raises RNF39's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 3.41× lower at baseline in the lines without CDH1 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1; co-absent with the target |
| [[DAPP1]] | C | DAPP1 activity raises RNF39's level | lines that do not express DAPP1 (39) vs lines expressing it (11) | 4.67× lower at baseline in the lines without DAPP1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A14, CEACAM6, MUC5B; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises RNF39's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.31× lower at baseline in the lines without CLIC5 | 2e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises RNF39's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.66× lower at baseline in the lines without TMPRSS4 | 2e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises RNF39's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 3.85× lower at baseline in the lines without WFDC2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises RNF39's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 3.33× lower at baseline in the lines without ADGRF1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*119 arrows, 119 of them with an alert ⚠; grade A 0, B 42, C 77. Shown: the 12 strongest; 107 more arrows (107 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | RNF39 activity raises EPS8L1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 4.31× lower at baseline in the lines without RNF39 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[KPNA7]] | B | RNF39 activity raises KPNA7's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.41× lower at baseline in the lines without RNF39 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[SEMA3B]] | B | RNF39 activity raises SEMA3B's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 4.08× lower at baseline in the lines without RNF39 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[MXD1]] | B | RNF39 activity raises MXD1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.01× lower at baseline in the lines without RNF39 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[FAM83E]] | B | RNF39 activity raises FAM83E's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 4.15× lower at baseline in the lines without RNF39 | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[PARD6B]] | B | RNF39 activity raises PARD6B's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.07× lower at baseline in the lines without RNF39 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[MUC20]] | B | RNF39 activity raises MUC20's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without RNF39 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[GPRC5C]] | B | RNF39 activity raises GPRC5C's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 3.23× lower at baseline in the lines without RNF39 | 0.003 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[RDH13]] | B | RNF39 activity raises RDH13's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without RNF39 | 0.004 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[GRHL3]] | B | RNF39 activity raises GRHL3's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without RNF39 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[RAB11FIP1]] | B | RNF39 activity raises RAB11FIP1's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without RNF39 | 0.009 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[ABHD11]] | B | RNF39 activity raises ABHD11's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without RNF39 | 0.010 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.9, 57.8); signed map (56.2, 7.9). **Vector** length 40.1, 10.8% of its response variance represented; |z| ≥ 3 in 361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +6.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +2.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +3.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +4.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.1 — chr6:30,070,266-30,075,849 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HZFw1, LIRF, FAP216 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2S5](https://www.uniprot.org/uniprotkb/Q9H2S5) (RING finger protein 39):

> Plays an inhibitory role in anti-RNA viral innate immunity by targeting the adapter DDX3X and promoting its 'Lys-48'-linked polyubiquitination. Alternatively, enhances the cGAS-STING pathway activation by promoting 'Lys-63'-linked ubiquitination of STING1, facilitating the STING1-TBK1 complex formation and STING1 activation.; (Microbial infection) Plays a positive role in human immunodeficiency virus (HIV-1) replication.

**Summary**, from NCBI Gene [80352](https://www.ncbi.nlm.nih.gov/gene/80352):

> This gene lies within the major histocompatibility complex class I region on chromosome 6. Studies of a similar rat protein suggest that this gene encodes a protein that plays a role in an early phase of synaptic plasticity. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18064) · Entrez [80352](https://www.ncbi.nlm.nih.gov/gene/80352) · UniProt [Q9H2S5](https://www.uniprot.org/uniprotkb/Q9H2S5) · Ensembl [ENSG00000204618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204618)

## Data

Gene col 12903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12903); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12903]; `tensor/DDL_lfc|DDL_z.npy` [12903]; `embed/gene_vectors.npy` [12903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12903 or target_col == 12903). Every well: [[RNF39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
