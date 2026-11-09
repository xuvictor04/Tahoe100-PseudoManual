---
symbol: "TNS4"
type: "gene"
col: 5238
ensembl_id: "ENSG00000131746"
name: "tensin 4"
location: "17q21.2"
module: 31
arm: "+"
pooled_cpm: 50.02
n_lines_expressing: 18
n_dd_up: 9
n_dd_down: 33
n_dd_up_clean: 6
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 72
direction_downstream: 86
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TNS4

*tensin 4* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.51× (z +5.0, q 3e-04, up in 8 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.305× (z -10.1, q 4e-21, down in 16 of 16 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GNT3]] (+0.78, fdr 7e-06), [[ITGB4]] (+0.76, fdr 7e-06), [[MST1R]] (+0.74, fdr 7e-06).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 72 arrows point to it, the strongest [[TNIK]] → it (grade B ⚠); 86 go from it, the strongest it → [[BCL2L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.0 | 3e-04 | 8/16 (HCT15, HEC-1-A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.77×** | +4.9 | 3e-04 | 1/17 (NCI-H1573) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.65×** | +4.1 | 0.007 | 1/14 (HEC-1-A) | all doses, flat | composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.008 | 8/16 (CFPAC-1, NCI-H1573, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +4.0 | 0.008 | 7/16 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.87×** | +3.7 | 0.024 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.025 | 8/16 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.040 | 7/16 (CFPAC-1, AsPC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.52×** | +3.3 | 0.061 | 0/15 | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.305×** | -10.1 | 4e-21 | 16/16 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.477×** | -8.9 | 2e-16 | 16/16 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.361×** | -8.0 | 3e-13 | 14/16 (SW480, LS 180, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.445×** | -6.6 | 5e-09 | 15/16 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.497×** | -5.7 | 1e-06 | 14/16 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.457×** | -5.7 | 1e-06 | 14/17 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.542×** | -5.2 | 2e-05 | 11/16 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.541×** | -5.0 | 4e-05 | 14/16 (SW480, LS 180, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.620×** | -4.9 | 5e-05 | 12/16 (SW480, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.542×** | -4.9 | 5e-05 | 15/16 (LS 180, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.544×** | -4.6 | 2e-04 | 15/16 (LS 180, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.678×** | -4.6 | 2e-04 | 13/16 (SW480, LS 180, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.586×** | -4.5 | 3e-04 | 3/16 (HT-29, HCT15, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.638×** | -4.5 | 3e-04 | 14/16 (SW480, LS 180, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.606×** | -4.2 | 9e-04 | 12/16 (SW480, LoVo, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 588 | 0 | 28 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0494× (z -26.6) |
| [[SW480 (line)]] | alt | 200 | 0 | 26 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -23.6) |
| [[LoVo (line)]] | wt | 61.0 | 0 | 15 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0939× (z -13.6) |
| [[KATO III (line)]] | alt | 117 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0985× (z -17.9) |
| [[HCT15 (line)]] | alt | 43.7 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 4.30× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -13.2) |
| [[Hs 766T (line)]] | wt | 167 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -22.3) |
| [[HT-29 (line)]] | alt | 126 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0683× (z -17.7) |
| [[A549 (line)]] | wt | 41.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0965× (z -14.6) |
| [[NCI-H2030 (line)]] | alt | 54.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 25.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.195× (z -9.8) |
| [[COLO 205 (line)]] | alt | 121 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -12.2) |
| [[CFPAC-1 (line)]] | alt | 100 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -13.0) |
| [[Panc 03.27 (line)]] | alt | 72.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -11.8) |
| [[SW1417 (line)]] | alt | 83.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -13.9) |
| [[A-172 (line)]] | wt | 3.37 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.64 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.17 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.74 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.66 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 61.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 9.07 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.57 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.80 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.43 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GNT3]] | +0.78 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ITGB4]] | +0.76 | +0.78 / +0.72 | both halves | 7e-06 | STRING 558 |
| [[MST1R]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PDE9A]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC02320]] | +0.73 | +0.71 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[LINC00659]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[PKP2]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[ONECUT3]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[KIAA0040]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ACOT11]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[CAPN8]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[SLC52A3]] | +0.67 | +0.62 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*72 arrows, 72 of them with an alert ⚠; grade A 0, B 10, C 62. Shown: the 12 strongest; 60 more arrows (60 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TNIK]] | B | TNIK activity raises TNS4's level | lines that do not express TNIK (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without TNIK | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000285082, FUT2, PTPRE |
| [[BAIAP2L2]] | B | BAIAP2L2 activity raises TNS4's level | lines that do not express BAIAP2L2 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without BAIAP2L2 | 0.047 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SH3TC1]] | B | SH3TC1 activity raises TNS4's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 3.28× lower at baseline in the lines without SH3TC1 | 0.052 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[TBC1D8]] | B | TBC1D8 activity raises TNS4's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 3.26× lower at baseline in the lines without TBC1D8 | 0.055 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[IGSF9]] | B | IGSF9 activity raises TNS4's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 3.19× lower at baseline in the lines without IGSF9 | 0.055 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[PDE9A]] | B | PDE9A activity raises TNS4's level | lines that do not express PDE9A (16) vs lines expressing it (34) | 3.69× lower at baseline in the lines without PDE9A | 0.058 | ⚠ within organs, on part of the lines; also absent: NRARP, FBXO2, ENSG00000267748 |
| [[ITGA6]] | B | ITGA6 activity raises TNS4's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 3.74× lower at baseline in the lines without ITGA6 | 0.063 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NOSTRIN]] | B | NOSTRIN activity raises TNS4's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 3.44× lower at baseline in the lines without NOSTRIN | 0.070 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[SLC16A5]] | B | SLC16A5 activity raises TNS4's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 3.90× lower at baseline in the lines without SLC16A5 | 0.072 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[ZNF860]] | B | ZNF860 activity raises TNS4's level | lines that do not express ZNF860 (16) vs lines expressing it (34) | 2.98× lower at baseline in the lines without ZNF860 | 0.079 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[B3GNT3]] | C | B3GNT3 activity raises TNS4's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 8.03× lower at baseline in the lines without B3GNT3 | 3e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises TNS4's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 6.17× lower at baseline in the lines without P2RY2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |

### Downstream of this gene

*86 arrows, 86 of them with an alert ⚠; grade A 0, B 30, C 56. Shown: the 12 strongest; 74 more arrows (74 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2L1]] | B | TNS4 activity raises BCL2L1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.12× lower at baseline in the lines without TNS4 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[BAIAP2L2]] | B | TNS4 activity raises BAIAP2L2's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.06× lower at baseline in the lines without TNS4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[KRT8]] | B | TNS4 activity raises KRT8's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 4.12× lower at baseline in the lines without TNS4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[ITGA6]] | B | TNS4 activity raises ITGA6's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.84× lower at baseline in the lines without TNS4 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[KIF13B]] | B | TNS4 activity raises KIF13B's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.26× lower at baseline in the lines without TNS4 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[NOSTRIN]] | B | TNS4 activity raises NOSTRIN's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 3.28× lower at baseline in the lines without TNS4 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[BCL2L1-AS1]] | B | TNS4 activity raises BCL2L1-AS1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.44× lower at baseline in the lines without TNS4 | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[RAPGEF3]] | B | TNS4 activity raises RAPGEF3's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without TNS4 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[ARHGEF16]] | B | TNS4 activity raises ARHGEF16's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.96× lower at baseline in the lines without TNS4 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[SH3TC1]] | B | TNS4 activity raises SH3TC1's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.54× lower at baseline in the lines without TNS4 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[LAMA5]] | B | TNS4 activity raises LAMA5's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 2.58× lower at baseline in the lines without TNS4 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |
| [[KPNA2P3]] | B | TNS4 activity raises KPNA2P3's level | lines that do not express TNS4 (32) vs lines expressing it (18) | 1.86× lower at baseline in the lines without TNS4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000279806, KLK10, IRF6 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, 50.7); signed map (4.8, 37.6). **Vector** length 121, 54.2% of its response variance represented; |z| ≥ 3 in 799 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +3.8 | +4.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.7 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +4.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.6 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +3.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +2.4 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.4 | +2.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.1 | -8.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.1 | -5.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.6 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.3 | -3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.2 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.0 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | tensin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:40,475,828-40,501,623 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTEN |
| Gene groups (HGNC) | SH2 domain containing |
| Reactome | 4 pathways, smallest: MET interacts with TNS proteins; MET promotes cell motility; Signaling by MET |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZW8](https://www.uniprot.org/uniprotkb/Q8IZW8) (Tensin-4):

> Promotes EGF-induced cell migration by displacing tensin TNS3 from the cytoplasmic tail of integrin ITGB1 which results in dissociation of TNS3 from focal adhesions, disassembly of actin stress fibers and initiation of cell migration. Suppresses ligand-induced degradation of EGFR by reducing EGFR ubiquitination in the presence of EGF. Increases MET protein stability by inhibiting MET endocytosis and subsequent lysosomal degradation which leads to increased cell survival, proliferation and …

**Summary**, from NCBI Gene [84951](https://www.ncbi.nlm.nih.gov/gene/84951):

> Predicted to enable actin binding activity. Involved in intracellular protein localization. Located in cytosol and focal adhesion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24352) · Entrez [84951](https://www.ncbi.nlm.nih.gov/gene/84951) · UniProt [Q8IZW8](https://www.uniprot.org/uniprotkb/Q8IZW8) · Ensembl [ENSG00000131746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131746)

## Data

Gene col 5238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5238); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5238]; `tensor/DDL_lfc|DDL_z.npy` [5238]; `embed/gene_vectors.npy` [5238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5238 or target_col == 5238). Every well: [[TNS4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNS4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
