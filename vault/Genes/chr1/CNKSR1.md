---
symbol: "CNKSR1"
type: "gene"
col: 6645
ensembl_id: "ENSG00000142675"
name: "connector enhancer of kinase suppressor of Ras 1"
location: "1p36.11"
module: 94
arm: "+"
pooled_cpm: 10.66
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 13
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# CNKSR1

*connector enhancer of kinase suppressor of Ras 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.27× (z +14.6, q 1e-45, up in 16 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.752× (z -5.1, q 2e-04, down in 18 of 23 measured lines) ⚠ cell-cycle shift, explains ~19% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.312×, KATO III 0.266×, HT-29 0.333×, SW480 0.394×; ⚠ cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.0359×, NCI-H1573 0.270×, SW1417 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.114×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX19B]] (+0.64, fdr 1e-05), [[LPAR5]] (+0.63, fdr 2e-05), [[ZNF579]] (+0.62, fdr 1e-05); moves opposite to [[PGM1]] (-0.57, fdr 3e-05), [[ZRANB3]] (-0.54, fdr 3e-05), [[SMG1P6]] (-0.54, fdr 3e-05).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[CCDC120]] → it (grade B ⚠); 13 go from it, the strongest it → [[FGD4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6645.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.27×** | +14.6 | 1e-45 | 16/24 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.11×** | +9.1 | 3e-17 | 17/24 (PANC-1, A-427, …) | top dose only | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.8 | 2e-09 | 1/14 (LS 180) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.4 | 3e-08 | 5/24 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.56×** | +5.2 | 2e-05 | 2/18 (SW480, HOP62) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.44×** | +4.6 | 4e-04 | 5/24 (COLO 205, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.43×** | +4.5 | 6e-04 | 12/24 (SW1417, LS 180, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 15/24 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.007 | 12/24 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +3.6 | 0.019 | 6/24 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.45×** | +3.4 | 0.038 | 4/23 (A-427, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.067 | 8/23 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Erythromycin (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.090 | 5/24 (LS 180, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6645.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (LoVo 0.312×, KATO III 0.266×, HT-29 0.333×, SW480 0.394×; ⚠ cell-cycle shift, explains ~19% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H2030 0.0359×, NCI-H1573 0.270×, SW1417 0.272×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.114×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.752×** | -5.1 | 2e-04 | 18/23 (LoVo, KATO III, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 0.789× | -3.0 | 0.50 | 4/24 (A-427, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6645. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 30.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -16.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +13.7) | — |
| [[SW1417 (line)]] | alt | 22.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 30.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -8.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HOP62 (line)]] | alt | 4.45 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +9.3) | — |
| [[HT-29 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -10.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[KATO III (line)]] | alt | 20.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -12.1) ⚠ cell-cycle shift, explains ~19% of this change |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0359× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.6) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-172 (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.876 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.47 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.860 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.824 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6645), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX19B]] | +0.64 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[LPAR5]] | +0.63 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[ZNF579]] | +0.62 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[ZNF44]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[NFKBIL1]] | +0.60 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZNF385C]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[MTMR10]] | +0.56 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SH3TC1]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[NGFR]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[DUSP15]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[ZNF316]] | +0.54 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ZNF45]] | +0.54 | +0.49 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGM1]] | -0.57 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ZRANB3]] | -0.54 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[SMG1P6]] | -0.54 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[PRPS2]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[UBE2G2]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[DPAGT1]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PRDM10]] | -0.50 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[IPO5]] | -0.50 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[HCFC1]] | -0.50 | -0.37 / -0.51 | both halves | 9e-05 |  |
| [[RBBP7]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[PTDSS1]] | -0.50 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[XRCC5]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC120]] | B | CCDC120 activity raises CNKSR1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.60× lower at baseline in the lines without CCDC120 | 0.002 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[GRAMD2B]] | B | GRAMD2B activity raises CNKSR1's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.86× lower at baseline in the lines without GRAMD2B | 0.020 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[FGD4]] | B | FGD4 activity raises CNKSR1's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 3.34× lower at baseline in the lines without FGD4 | 0.050 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[MPZL3]] | C | MPZL3 activity raises CNKSR1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 4.04× lower at baseline in the lines without MPZL3 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1; co-absent with the target |
| [[GRB7]] | C | GRB7 activity raises CNKSR1's level | lines that do not express GRB7 (25) vs lines expressing it (25) | 4.82× lower at baseline in the lines without GRB7 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH2D3A, CRB3, MISP; co-absent with the target |
| [[LPAR5]] | C | LPAR5 activity raises CNKSR1's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.94× lower at baseline in the lines without LPAR5 | 0.018 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent; co-absent with the target |
| [[IFNLR1]] | C | IFNLR1 activity raises CNKSR1's level | lines that do not express IFNLR1 (18) vs lines expressing it (32) | 3.67× lower at baseline in the lines without IFNLR1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KLF5, NCMAP, ENTPD2; co-absent with the target |
| [[MOGAT3]] | C | MOGAT3 activity raises CNKSR1's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.60× lower at baseline in the lines without MOGAT3 | 0.031 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD4]] | B | CNKSR1 activity raises FGD4's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 3.96× lower at baseline in the lines without CNKSR1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[CCDC120]] | B | CNKSR1 activity raises CCDC120's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 2.57× lower at baseline in the lines without CNKSR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[PICK1]] | B | CNKSR1 activity raises PICK1's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 1.72× lower at baseline in the lines without CNKSR1 | 0.009 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[CBX4]] | B | CNKSR1 activity raises CBX4's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 1.42× lower at baseline in the lines without CNKSR1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[GRAMD2B]] | B | CNKSR1 activity raises GRAMD2B's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 3.34× lower at baseline in the lines without CNKSR1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[KIAA1522]] | B | CNKSR1 activity raises KIAA1522's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 2.39× lower at baseline in the lines without CNKSR1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[DSTYK]] | B | CNKSR1 activity lowers DSTYK's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 1.32× higher at baseline in the lines without CNKSR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[FBLIM1]] | B | CNKSR1 activity raises FBLIM1's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 1.95× lower at baseline in the lines without CNKSR1 | 0.089 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| cells under [[Torkinib (drug)]] 5 µM | B | CNKSR1 activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express CNKSR1 (24) vs lines expressing it (24) | the lines without CNKSR1: 0.82× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[MPZL3]] | C | CNKSR1 activity raises MPZL3's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 5.68× lower at baseline in the lines without CNKSR1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2; co-absent with the target |
| [[GRB7]] | C | CNKSR1 activity raises GRB7's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 3.82× lower at baseline in the lines without CNKSR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2; co-absent with the target |
| [[LPAR5]] | C | CNKSR1 activity raises LPAR5's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without CNKSR1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2; co-absent with the target |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.504). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.7, 26.5); signed map (-1.5, 2.8). **Vector** length 55.5, 13.8% of its response variance represented; |z| ≥ 3 in 400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +14.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +9.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +2.8 | +3.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | -0.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -1.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | connector enhancer of kinase suppressor of Ras 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,177,484-26,189,884 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CNK1, KSR, CNK |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Sterile alpha motif domain containing; PDZ domain containing |
| Reactome | 13 pathways, smallest: Signaling by high-kinase activity BRAF mutants; MAP2K and MAPK activation; Signaling by RAF1 mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [Q969H4](https://www.uniprot.org/uniprotkb/Q969H4) (Connector enhancer of kinase suppressor of ras 1):

> May function as an adapter protein or regulator of Ras signaling pathways.

**Summary**, from NCBI Gene [10256](https://www.ncbi.nlm.nih.gov/gene/10256):

> This gene encodes a protein containing several motifs involved in protein-protein interaction, including PDZ, PH (Pleckstrin homology), and SAM (sterile alpha motif) domains. The encoded protein acts as a scaffold component for receptor tyrosine kinase signaling and may mediate crosstalk between different signaling pathways. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:19700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19700) · Entrez [10256](https://www.ncbi.nlm.nih.gov/gene/10256) · UniProt [Q969H4](https://www.uniprot.org/uniprotkb/Q969H4) · Ensembl [ENSG00000142675](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142675)

## Data

Gene col 6645: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6645); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6645, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6645]; `tensor/DDL_lfc|DDL_z.npy` [6645]; `embed/gene_vectors.npy` [6645]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6645 or target_col == 6645). Every well: [[CNKSR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNKSR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
