---
symbol: "FUT2"
type: "gene"
col: 10767
ensembl_id: "ENSG00000176920"
name: "fucosyltransferase 2 (H blood group)"
location: "19q13.33"
module: 55
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 38
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 81
direction_downstream: 25
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# FUT2

*fucosyltransferase 2 (H blood group)* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.36× (z +15.2, q 0e+00, up in 6 of 11 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.94× (z +7.1, q 2e-10, up in 17 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.0682×, LS 180 0.129×, COLO 205 0.0913×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CFPAC-1 0.0749×, KATO III 0.246×, COLO 205 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (COLO 205 0.0679×, AsPC-1 0.0463×); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 0.0275×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01559]] (+0.73, fdr 7e-06), [[ABO]] (+0.72, fdr 7e-06), [[TPRXL]] (+0.70, fdr 1e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 81 arrows point to it, the strongest [[LINC03040]] → it (grade B ⚠); 25 go from it, the strongest it → [[KCNK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10767.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.36×** | +15.2 | 0e+00 | 6/11 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.59×** | +13.6 | 2e-39 | 5/6 (HOP62, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.23×** | +12.5 | 2e-33 | 4/9 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.94×** | +7.1 | 2e-10 | 17/31 (CFPAC-1, SK-MEL-2, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +6.2 | 5e-08 | 5/14 (SW480, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.26×** | +6.2 | 7e-08 | 18/31 (CFPAC-1, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.77×** | +5.5 | 3e-06 | 15/30 (SW480, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.91×** | +5.4 | 4e-06 | 3/12 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +5.2 | 1e-05 | 8/26 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.95×** | +5.1 | 2e-05 | 3/10 (SW1417, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.80×** | +4.2 | 0.001 | 12/25 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +3.8 | 0.008 | 6/26 (SK-MEL-2, HOP62, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.55×** | +3.7 | 0.009 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.5 | 0.018 | 4/24 (J82, SW1417, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.5 | 0.018 | 1/27 (HEC-1-A) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.080 | 7/31 (SW1417, LS 180, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10767.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (KATO III 0.0682×, LS 180 0.129×, COLO 205 0.0913×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CFPAC-1 0.0749×, KATO III 0.246×, COLO 205 0.178×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (COLO 205 0.0679×, AsPC-1 0.0463×); [[PH-797804 (drug)]] 5 µM in 1 line (LS 180 0.0275×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.614× | -3.3 | 0.47 | 3/33 (SW1417, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10767. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 16.2 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -18.5) |
| [[COLO 205 (line)]] | alt | 15.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -11.9) |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 3.28 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0463× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 3.30 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0749× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 2.40 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 61.3× (z +9.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 5.56 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0512× (z -8.5) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -10.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.989 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.820 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.857 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.776 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.965 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.600 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.490 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.462 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.768 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.740 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10767), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01559]] | +0.73 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[ABO]] | +0.72 | +0.72 / +0.62 | both halves | 7e-06 | same gene group; pathway: Blood group systems biosynthesis; STRING 927 |
| [[TPRXL]] | +0.70 | +0.73 / +0.57 | both halves | 1e-05 |  |
| [[MUC3A]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[LGALS4]] | +0.68 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[GCNT3]] | +0.68 | +0.75 / +0.52 | both halves | 1e-05 | STRING 483 |
| [[USH1C]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[MYH14]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.65 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[PRR15]] | +0.65 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[PRR15L]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[MUC12]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*81 arrows, 81 of them with an alert ⚠; grade A 0, B 81, C 0. Shown: the 12 strongest; 69 more arrows (69 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC03040]] | B | LINC03040 activity raises FUT2's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.56× lower at baseline in the lines without LINC03040 | 5e-04 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[SLC44A4]] | B | SLC44A4 activity raises FUT2's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 3.09× lower at baseline in the lines without SLC44A4 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1 |
| [[GPA33]] | B | GPA33 activity raises FUT2's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 3.62× lower at baseline in the lines without GPA33 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[ALOX5]] | B | ALOX5 activity raises FUT2's level | lines that do not express ALOX5 (28) vs lines expressing it (22) | 2.22× lower at baseline in the lines without ALOX5 | 0.001 | ⚠ within organs, on part of the lines; also absent: PDZK1IP1, ADGRF1, RASSF6 |
| [[INAVA]] | B | INAVA activity raises FUT2's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.49× lower at baseline in the lines without INAVA | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[TMPRSS2]] | B | TMPRSS2 activity raises FUT2's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.87× lower at baseline in the lines without TMPRSS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[SLC5A1]] | B | SLC5A1 activity raises FUT2's level | lines that do not express SLC5A1 (36) vs lines expressing it (14) | 3.23× lower at baseline in the lines without SLC5A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM30B, TMPRSS2, TMEM125 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises FUT2's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.74× lower at baseline in the lines without TMPRSS4 | 0.002 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[LINC01559]] | B | LINC01559 activity raises FUT2's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 3.23× lower at baseline in the lines without LINC01559 | 0.003 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17 |
| [[MUC13]] | B | MUC13 activity raises FUT2's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.35× lower at baseline in the lines without MUC13 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[CLIC5]] | B | CLIC5 activity raises FUT2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.64× lower at baseline in the lines without CLIC5 | 0.004 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[LINC02967]] | B | LINC02967 activity raises FUT2's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 2.74× lower at baseline in the lines without LINC02967 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 25, C 0. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNK1]] | B | FUT2 activity raises KCNK1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 4.45× lower at baseline in the lines without FUT2 | 0.006 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[CDA]] | B | FUT2 activity raises CDA's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 3.72× lower at baseline in the lines without FUT2 | 0.007 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[FXYD3]] | B | FUT2 activity raises FXYD3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.68× lower at baseline in the lines without FUT2 | 0.023 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[TNFRSF14-AS1]] | B | FUT2 activity raises TNFRSF14-AS1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without FUT2 | 0.034 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[C6orf132]] | B | FUT2 activity raises C6orf132's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 3.47× lower at baseline in the lines without FUT2 | 0.035 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[LPAR5]] | B | FUT2 activity raises LPAR5's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.94× lower at baseline in the lines without FUT2 | 0.036 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[ELF3]] | B | FUT2 activity raises ELF3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 3.26× lower at baseline in the lines without FUT2 | 0.037 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[KLKP1-1]] | B | FUT2 activity raises KLKP1-1's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without FUT2 | 0.041 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[ADCY4]] | B | FUT2 activity raises ADCY4's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.95× lower at baseline in the lines without FUT2 | 0.042 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[MAP3K8]] | B | FUT2 activity raises MAP3K8's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 1.82× lower at baseline in the lines without FUT2 | 0.042 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[SULT1C2]] | B | FUT2 activity raises SULT1C2's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.37× lower at baseline in the lines without FUT2 | 0.044 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |
| [[TMPRSS3]] | B | FUT2 activity raises TMPRSS3's level | lines that do not express FUT2 (12) vs lines expressing it (38) | 2.46× lower at baseline in the lines without FUT2 | 0.045 | ⚠ within organs, on part of the lines; also absent: EFNB2, SH3TC1, PTPRE; maybe low, not absent |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.4, 53.3); signed map (61.5, 6.5). **Vector** length 60.8, 14.1% of its response variance represented; |z| ≥ 3 in 583 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +13.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.7 | +4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +5.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | fucosyltransferase 2 (H blood group) |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,695,971-48,705,951 (+) |
| Ensembl biotype | protein_coding |
| Also known as | sej, Se2, SEC2; previously SE |
| Gene groups (HGNC) | Fucosyltransferases; Blood group antigens |
| Reactome | 7 pathways, smallest: Lewis blood group biosynthesis; Blood group systems biosynthesis; Glycosphingolipid biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q10981](https://www.uniprot.org/uniprotkb/Q10981) (Galactoside alpha-(1,2)-fucosyltransferase 2):

> Catalyzes the transfer of L-fucose, from a guanosine diphosphate-beta-L-fucose, to the terminal galactose on both O- and N-linked glycans chains of cell surface glycoproteins and glycolipids and the resulting epitope regulates several processes such as cell-cell interaction including host-microbe interaction, cell surface expression and cell proliferation. Preferentially fucosylates gangliosides GA1 and GM1 in the antrum, cecum and colon and in the female reproductive organs (By similarity). …

**Summary**, from NCBI Gene [2524](https://www.ncbi.nlm.nih.gov/gene/2524):

> This gene is one of two encoding the galactoside 2-L-fucosyltransferase enzyme. The encoded protein is important for the final step in the soluble ABO blood group antigen synthesis pathway. It is also involved in cell-cell interaction, cell surface expression, and cell proliferation. Mutations in this gene are a cause of the H-Bombay blood group where red blood cells lack the H antigen. [provided by RefSeq, May 2022]

**Accessions** — [HGNC:4013](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4013) · Entrez [2524](https://www.ncbi.nlm.nih.gov/gene/2524) · UniProt [Q10981](https://www.uniprot.org/uniprotkb/Q10981) · Ensembl [ENSG00000176920](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176920)

## Data

Gene col 10767: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10767); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10767, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10767]; `tensor/DDL_lfc|DDL_z.npy` [10767]; `embed/gene_vectors.npy` [10767]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10767 or target_col == 10767). Every well: [[FUT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
