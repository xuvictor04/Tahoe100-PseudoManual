---
symbol: "GRHL3"
type: "gene"
col: 8127
ensembl_id: "ENSG00000158055"
name: "grainyhead like transcription factor 3"
location: "1p36.11"
module: 8
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 34
n_dd_up: 32
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 30
direction_downstream: 35
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# GRHL3

*grainyhead like transcription factor 3* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.68× (z +18.6, q 0e+00, up in 17 of 20 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0405×, LS 180 0.143×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.104×, LS 180 0.161×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.0333×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0495×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (LoVo 0.0819×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF39]] (+0.62, fdr 3e-05), [[EPS8L1]] (+0.59, fdr 3e-05), [[PAX5]] (+0.57, fdr 1e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 30 arrows point to it, the strongest [[TMPRSS4]] → it (grade B ⚠); 35 go from it, the strongest it → [[IL22RA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.68×** | +18.6 | 0e+00 | 17/20 (LS 180, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.35×** | +14.9 | 0e+00 | 2/8 (PANC-1, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.25×** | +14.1 | 1e-42 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +9.8 | 1e-20 | 9/21 (SW1417, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +9.5 | 3e-19 | 1/7 (LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +7.5 | 9e-12 | 8/28 (SW480, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.06×** | +7.3 | 3e-11 | 11/26 (LS 180, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.01×** | +7.0 | 1e-10 | 0/7 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +5.6 | 1e-06 | 6/27 (A549, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +5.6 | 1e-06 | 10/26 (HCT15, SW480, …) | two highest doses | cell-cycle shift (explains ~22% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.14×** | +5.5 | 2e-06 | 1/6 (NCI-H2347) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.46×** | +5.4 | 3e-06 | 3/30 (SW48, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.64×** | +5.0 | 3e-05 | 10/29 (HCT15, SW480, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.9 | 3e-05 | 2/14 (NCI-H460, NCI-H1573) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +4.9 | 3e-05 | 7/23 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +4.7 | 1e-04 | 4/22 (C32, SW480, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +4.1 | 0.001 | 7/27 (A549, C32, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +4.1 | 0.001 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.0 | 0.002 | 5/18 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.012 | 4/24 (SW1417, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.013 | 1/16 (HOP62) | inconsistent across doses |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.41×** | +3.3 | 0.023 | 2/18 (LoVo, BT-474) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8127.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW48 0.0405×, LS 180 0.143×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW48 0.104×, LS 180 0.161×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 1 line (SW48 0.0333×); [[Clobetasol propionate (drug)]] 0.5 µM in 1 line (CFPAC-1 0.0495×); [[XRK3F2 (drug)]] 0.5 µM in 1 line (LoVo 0.0819×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Megestrol (drug)]] 5 µM |  | 0.787× | -3.5 | 0.22 | 6/29 (Hs 766T, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.720× | -3.4 | 0.22 | 6/24 (PANC-1, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.734× | -3.2 | 0.29 | 4/23 (NCI-H23, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.731× | -3.1 | 0.29 | 4/27 (Panc 03.27, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 64.1 | 0 | 5 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0333× (z -17.0) |
| [[LS 180 (line)]] | wt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -9.4) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 3.35 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.5 µM 0.0495× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 1.91 | 0 | 1 | — | [[Pentagastrin (drug)]] 0.05 µM 0.0499× (z -8.5) |
| [[LoVo (line)]] | wt | 9.55 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0819× (z -9.3) |
| [[A-172 (line)]] | wt | 0.935 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.830 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.776 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.943 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.815 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.770 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.873 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.985 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.732 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.643 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.766 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.880 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF39]] | +0.62 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[EPS8L1]] | +0.59 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[PAX5]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ADGRF1]] | +0.55 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[ZNF423]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NECTIN4]] | +0.54 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ST14]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[INAVA]] | +0.53 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[TMPRSS2]] | +0.52 | +0.48 / +0.46 | both halves | 2e-05 |  |
| [[JUP]] | +0.52 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[EHF]] | +0.52 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[DSG3]] | +0.51 | +0.50 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 25, C 5. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMPRSS4]] | B | TMPRSS4 activity raises GRHL3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 3.07× lower at baseline in the lines without TMPRSS4 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[CLIC5]] | B | CLIC5 activity raises GRHL3's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.61× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[CDH1]] | B | CDH1 activity raises GRHL3's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.70× lower at baseline in the lines without CDH1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[GPR87]] | B | GPR87 activity raises GRHL3's level | lines that do not express GPR87 (36) vs lines expressing it (14) | 2.93× lower at baseline in the lines without GPR87 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, MUC16, HEPHL1 |
| [[RNF39]] | B | RNF39 activity raises GRHL3's level | lines that do not express RNF39 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without RNF39 | 0.008 | ⚠ within organs, on part of the lines; also absent: CDH1, TNNT2, TRIM15; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers GRHL3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.6% of all compounds | 0.011 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[INAVA]] | B | INAVA activity raises GRHL3's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.36× lower at baseline in the lines without INAVA | 0.013 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[KLK11]] | B | KLK11 activity raises GRHL3's level | lines that do not express KLK11 (40) vs lines expressing it (10) | 3.39× lower at baseline in the lines without KLK11 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GABRP, MUC17, LYZ |
| [[PKP1]] | B | PKP1 activity raises GRHL3's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.47× lower at baseline in the lines without PKP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[IGFL2]] | B | IGFL2 activity raises GRHL3's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 3.11× lower at baseline in the lines without IGFL2 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33 |
| [[CLDN4]] | B | CLDN4 activity raises GRHL3's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.22× lower at baseline in the lines without CLDN4 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[HS3ST1]] | B | HS3ST1 activity raises GRHL3's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 2.64× lower at baseline in the lines without HS3ST1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 27, C 8. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL22RA1]] | B | GRHL3 activity raises IL22RA1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without GRHL3 | 0.015 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[PLEKHG1]] | B | GRHL3 activity raises PLEKHG1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.04× lower at baseline in the lines without GRHL3 | 0.018 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[CDH1]] | B | GRHL3 activity raises CDH1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 5.27× lower at baseline in the lines without GRHL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[KCNK1]] | B | GRHL3 activity raises KCNK1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.28× lower at baseline in the lines without GRHL3 | 0.030 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[CLDN4]] | B | GRHL3 activity raises CLDN4's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.74× lower at baseline in the lines without GRHL3 | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[INAVA]] | B | GRHL3 activity raises INAVA's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.99× lower at baseline in the lines without GRHL3 | 0.037 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[KPNA7]] | B | GRHL3 activity raises KPNA7's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without GRHL3 | 0.042 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[TMPRSS2]] | B | GRHL3 activity raises TMPRSS2's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.24× lower at baseline in the lines without GRHL3 | 0.046 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[HS3ST1]] | B | GRHL3 activity raises HS3ST1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.51× lower at baseline in the lines without GRHL3 | 0.048 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[SULF2]] | B | GRHL3 activity raises SULF2's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.77× lower at baseline in the lines without GRHL3 | 0.049 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[EPS8L1]] | B | GRHL3 activity raises EPS8L1's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.64× lower at baseline in the lines without GRHL3 | 0.052 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[EHF]] | B | GRHL3 activity raises EHF's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 3.67× lower at baseline in the lines without GRHL3 | 0.053 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.459). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.3, 55.8); signed map (56.6, 8.7). **Vector** length 42.0, 6.82% of its response variance represented; |z| ≥ 3 in 691 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +18.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +4.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.7 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | grainyhead like transcription factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:24,199,558-24,364,482 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SOM; previously TFCP2L4 |
| Gene groups (HGNC) | Grainyhead like transcription factor family |
| Reactome | 4 pathways, smallest: Assembly of the 9+2 motile cilia; Transcriptional regulation of multiciliogenesis; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE85](https://www.uniprot.org/uniprotkb/Q8TE85) (Grainyhead-like protein 3 homolog):

> Transcription factor playing important roles in primary neurulation and in the differentiation of stratified epithelia of both ectodermal and endodermal origin (By similarity). Binds directly to the consensus DNA sequence 5'-AACCGGTT-3' acting as an activator and repressor on distinct target genes. xhibits functional redundancy with GRHL2 in epidermal morphogenetic events and epidermal wound repair (By similarity). Exhibits functional redundancy with GRHL2 in epidermal morphogenetic events and …

**Summary**, from NCBI Gene [57822](https://www.ncbi.nlm.nih.gov/gene/57822):

> This gene encodes a member of the grainyhead family of transcription factors. The encoded protein may function as a transcription factor during development, and has been shown to stimulate migration of endothelial cells. Multiple transcript variants encoding distinct isoforms have been identified for this gene.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:25839](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25839) · Entrez [57822](https://www.ncbi.nlm.nih.gov/gene/57822) · UniProt [Q8TE85](https://www.uniprot.org/uniprotkb/Q8TE85) · Ensembl [ENSG00000158055](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158055)

## Data

Gene col 8127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8127); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8127]; `tensor/DDL_lfc|DDL_z.npy` [8127]; `embed/gene_vectors.npy` [8127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8127 or target_col == 8127). Every well: [[GRHL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRHL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
