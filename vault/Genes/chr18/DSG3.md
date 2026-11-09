---
symbol: "DSG3"
type: "gene"
col: 5598
ensembl_id: "ENSG00000134757"
name: "desmoglein 3"
location: "18q12.1"
module: 73
arm: "+"
pooled_cpm: 15.46
n_lines_expressing: 9
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 84
direction_downstream: 77
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# DSG3

*desmoglein 3* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.53× (z +9.0, q 9e-17, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.69× (z +3.8, q 0.015, up in 5 of 7 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.583× (z -3.9, q 0.065, down in 5 of 7 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0994×, KATO III 0.0465×, CFPAC-1 0.0898×, AsPC-1 0.270×); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.185×, AsPC-1 0.173×, KATO III 0.103×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.00825×, LoVo 0.201×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB5]] (+0.78, fdr 7e-06), [[PRSS3]] (+0.78, fdr 7e-06), [[KLK10]] (+0.76, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 84 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); 77 go from it, the strongest it → [[RDH13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.53×** | +9.0 | 9e-17 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.43×** | +8.5 | 5e-15 | 0/4 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +7.7 | 3e-12 | 1/5 (AsPC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +5.5 | 5e-06 | 3/6 (KATO III, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.30×** | +4.5 | 9e-04 | 1/3 (AsPC-1) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.69×** | +3.8 | 0.015 | 5/7 (KATO III, SW1417, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.47×** | +3.4 | 0.056 | 3/6 (CFPAC-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.59×** | +3.3 | 0.058 | 1/7 (COLO 205) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.058 | 4/7 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.62×** | +3.3 | 0.058 | 4/7 (AsPC-1, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Bendamustine (drug)]] 5 µM |  | 1.56× | +3.1 | 0.11 | 0/7 | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.35× | +3.0 | 0.12 | 4/7 (KATO III, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5598.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LoVo 0.0994×, KATO III 0.0465×, CFPAC-1 0.0898×, AsPC-1 0.270×); [[Belinostat (drug)]] 5 µM in 3 lines (LoVo 0.185×, AsPC-1 0.173×, KATO III 0.103×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (KATO III 0.00825×, LoVo 0.201×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.583×** | -3.9 | 0.065 | 5/7 (KATO III, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.589× | -3.5 | 0.13 | 2/7 (SW48, LoVo) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.625× | -3.4 | 0.15 | 6/7 (KATO III, LoVo, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Asciminib (drug)]] 0.05 µM |  | 0.645× | -3.1 | 0.24 | 0/7 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 324 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -19.3) |
| [[KATO III (line)]] | alt | 36.9 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.00825× (z -18.5) |
| [[AsPC-1 (line)]] | alt | 94.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0911× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -14.1) |
| [[A-172 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.896 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.53 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.842 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.990 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.03 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB5]] | +0.78 | +0.80 / +0.71 | both halves | 7e-06 | STRING 539 |
| [[PRSS3]] | +0.78 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[KLK10]] | +0.76 | +0.82 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[HS3ST1]] | +0.76 | +0.72 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[DSG4]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 | same gene group; pathway: Formation of the cornified envelope; STRING 711; ⚠ same locus (32.8 kb, same strand: neighbours can correlate without regulation) |
| [[TPRXL]] | +0.74 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.73 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[LINC02474]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[C1orf116]] | +0.72 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[CALB1]] | +0.72 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[NPSR1]] | +0.72 | +0.77 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*84 arrows, 84 of them with an alert ⚠; grade A 0, B 1, C 83. Shown: the 12 strongest; 72 more arrows (72 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers DSG3's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NPSR1]] | C | NPSR1 activity raises DSG3's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 8.84× lower at baseline in the lines without NPSR1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises DSG3's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 5.60× lower at baseline in the lines without GCNT3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises DSG3's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 3.89× lower at baseline in the lines without HNF4A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[TMPRSS4]] | C | TMPRSS4 activity raises DSG3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.11× lower at baseline in the lines without TMPRSS4 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |
| [[SERPINB5]] | C | SERPINB5 activity raises DSG3's level | lines that do not express SERPINB5 (34) vs lines expressing it (16) | 4.50× lower at baseline in the lines without SERPINB5 | 0.005 | ⚠ within organs, on part of the lines; also absent: COL17A1, FGFBP1, TSPAN8; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises DSG3's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 4.42× lower at baseline in the lines without EPS8L3 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[TMPRSS2]] | C | TMPRSS2 activity raises DSG3's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 4.37× lower at baseline in the lines without TMPRSS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6; co-absent with the target |
| [[CLIC5]] | C | CLIC5 activity raises DSG3's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 4.36× lower at baseline in the lines without CLIC5 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises DSG3's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 4.69× lower at baseline in the lines without CEACAM6 | 0.006 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises DSG3's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 4.73× lower at baseline in the lines without FGFBP1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[TFF2]] | C | TFF2 activity raises DSG3's level | lines that do not express TFF2 (39) vs lines expressing it (11) | 6.74× lower at baseline in the lines without TFF2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG3, ENSG00000250920, TRIM31; co-absent with the target |

### Downstream of this gene

*77 arrows, 77 of them with an alert ⚠; grade A 0, B 16, C 61. Shown: the 12 strongest; 65 more arrows (65 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RDH13]] | B | DSG3 activity raises RDH13's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 2.69× lower at baseline in the lines without DSG3 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[ARHGEF34P]] | B | DSG3 activity raises ARHGEF34P's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 4.13× lower at baseline in the lines without DSG3 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[EPS8L1]] | B | DSG3 activity raises EPS8L1's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 4.39× lower at baseline in the lines without DSG3 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[PRDM1]] | B | DSG3 activity raises PRDM1's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 3.94× lower at baseline in the lines without DSG3 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[JUP]] | B | DSG3 activity raises JUP's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 5.02× lower at baseline in the lines without DSG3 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[ARHGEF5]] | B | DSG3 activity raises ARHGEF5's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 3.47× lower at baseline in the lines without DSG3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[VILL]] | B | DSG3 activity raises VILL's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 2.71× lower at baseline in the lines without DSG3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[SEMA3B]] | B | DSG3 activity raises SEMA3B's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 4.01× lower at baseline in the lines without DSG3 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[TLDC2]] | B | DSG3 activity raises TLDC2's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 2.53× lower at baseline in the lines without DSG3 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[FAM83E]] | B | DSG3 activity raises FAM83E's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 3.67× lower at baseline in the lines without DSG3 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[PLEKHG1]] | B | DSG3 activity raises PLEKHG1's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 4.36× lower at baseline in the lines without DSG3 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[SDCBP2]] | B | DSG3 activity raises SDCBP2's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 4.67× lower at baseline in the lines without DSG3 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.2, 54.5); signed map (65.6, 8.4). **Vector** length 42.4, 21.6% of its response variance represented; |z| ≥ 3 in 187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +1.4 | +3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +1.3 | +3.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.8 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +0.7 | +2.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -0.9 | -3.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.8 | -0.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.8 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.8 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | desmoglein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:31,447,741-31,478,702 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDHF6 |
| Gene groups (HGNC) | Desmosomal cadherins |
| Reactome | 7 pathways, smallest: Apoptotic cleavage of cell adhesion  proteins; Apoptotic cleavage of cellular proteins; Formation of the cornified envelope |
| Matched by | ensembl_id |

**Function**, from UniProt [P32926](https://www.uniprot.org/uniprotkb/P32926) (Desmoglein-3):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion. Required for adherens and desmosome junction assembly in response to mechanical force in keratinocytes. Required for desmosome-mediated cell-cell adhesion of cells surrounding the telogen hair club and the basal layer of the outer root sheath epithelium, consequently is essential for the anchoring of telogen hairs in the hair follicle. Required for the maintenance of the epithelial …

**Summary**, from NCBI Gene [1830](https://www.ncbi.nlm.nih.gov/gene/1830):

> This gene encodes a member of the desmoglein family and cadherin cell adhesion molecule superfamily of proteins. Desmogleins are calcium-binding transmembrane glycoprotein components of desmosomes, cell-cell junctions between epithelial, myocardial, and other cell types. The encoded preproprotein is proteolytically processed to generate the mature glycoprotein. This gene is present in a gene cluster with other desmoglein gene family members on chromosome 18. The encoded protein has been …

**Accessions** — [HGNC:3050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3050) · Entrez [1830](https://www.ncbi.nlm.nih.gov/gene/1830) · UniProt [P32926](https://www.uniprot.org/uniprotkb/P32926) · Ensembl [ENSG00000134757](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134757)

## Data

Gene col 5598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5598); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5598]; `tensor/DDL_lfc|DDL_z.npy` [5598]; `embed/gene_vectors.npy` [5598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5598 or target_col == 5598). Every well: [[DSG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
