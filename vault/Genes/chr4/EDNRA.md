---
symbol: "EDNRA"
type: "gene"
col: 7541
ensembl_id: "ENSG00000151617"
name: "endothelin receptor type A"
location: "4q31.22-q31.23"
module: 13
arm: "+"
pooled_cpm: 4.7
n_lines_expressing: 18
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 36
direction_downstream: 58
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# EDNRA

*endothelin receptor type A* — 4q31.22-q31.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.64× (z +11.6, q 2e-28, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.65× (z +5.6, q 3e-06, up in 4 of 15 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.710× (z -3.8, q 0.073, down in 13 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.120×, hTERT-HPNE 0.139×, HOP62 0.145×); [[Belinostat (drug)]] 5 µM in 3 lines (A-172 0.0632×, hTERT-HPNE 0.0936×, CHP-212 0.0705×); [[Panobinostat (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.0737×, NCI-H1792 0.188×, CHP-212 0.0540×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA11]] (+0.68, fdr 7e-06), [[ADAMTS14]] (+0.67, fdr 8e-06), [[VSTM4]] (+0.66, fdr 1e-05); moves opposite to [[MYO16-AS1]] (-0.51, fdr 2e-04), [[MIR3936HG]] (-0.49, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 36 arrows point to it, the strongest [[PATJ]] → it (grade B ⚠); 58 go from it, the strongest it → [[TMEM132A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7541.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.64×** | +11.6 | 2e-28 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.96×** | +8.5 | 4e-15 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +8.4 | 7e-15 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +5.6 | 3e-06 | 4/15 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +5.4 | 8e-06 | 1/14 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.0 | 6e-05 | 2/9 (SNU-423, HOP62) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.9 | 0.006 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.69×** | +3.8 | 0.008 | 5/13 (RPMI-7951, Panc 03.27, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.98×** | +3.8 | 0.008 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +3.5 | 0.026 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.47× | +3.0 | 0.13 | 1/13 (SW 900) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7541.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H1792 0.120×, hTERT-HPNE 0.139×, HOP62 0.145×); [[Belinostat (drug)]] 5 µM in 3 lines (A-172 0.0632×, hTERT-HPNE 0.0936×, CHP-212 0.0705×); [[Panobinostat (drug)]] 5 µM in 3 lines (hTERT-HPNE 0.0737×, NCI-H1792 0.188×, CHP-212 0.0540×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.710×** | -3.8 | 0.073 | 13/14 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.630×** | -3.7 | 0.074 | 11/15 (CHP-212, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.651× | -3.4 | 0.11 | 6/15 (HOP62, CHP-212, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.631× | -3.4 | 0.11 | 0/15 | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.667× | -3.2 | 0.16 | 1/15 (SW 900) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.758× | -3.1 | 0.17 | 2/15 (NCI-H2347, CFPAC-1) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 0.762× | -3.0 | 0.17 | 3/15 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.660× | -3.0 | 0.17 | 1/15 (Panc 03.27) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7541. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 90.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.8) |
| [[CHP-212 (line)]] | wt | 75.9 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0906× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 41.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -18.3) |
| [[A-172 (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0632× (z -13.2) |
| [[HOP62 (line)]] | alt | 3.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.207× (z -11.0) |
| [[A-427 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.580 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.534 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.446 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.488 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.556 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.444 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7541), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA11]] | +0.68 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[ADAMTS14]] | +0.67 | +0.75 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[VSTM4]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[SYNDIG1]] | +0.65 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[APCDD1L]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PRRX1]] | +0.64 | +0.67 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SPOCD1]] | +0.64 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[LINC01705]] | +0.63 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[NAV1]] | +0.63 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[CARMN]] | +0.62 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[INSYN2B]] | +0.61 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[TSHZ3]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO16-AS1]] | -0.51 | -0.52 / -0.29 | both halves | 2e-04 |  |
| [[MIR3936HG]] | -0.49 | -0.61 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 3, C 33. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PATJ]] | B | PATJ activity lowers EDNRA's level | lines that do not express PATJ (9) vs lines expressing it (41) | 3.94× higher at baseline in the lines without PATJ | 0.060 | ⚠ within organs, on part of the lines; also absent: FGFR4, OPLAH, RPH3AL; maybe low, not absent; its own permutation p |
| [[MANCR]] | B | MANCR activity raises EDNRA's level | lines that do not express MANCR (20) vs lines expressing it (30) | 1.74× lower at baseline in the lines without MANCR | 0.064 | ⚠ within organs, on part of the lines; also absent: NLRP1, EVA1A, RAC2 |
| [[GPR68]] | B | GPR68 activity raises EDNRA's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without GPR68 | 0.079 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[LINC01705]] | C | LINC01705 activity raises EDNRA's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 3.54× lower at baseline in the lines without LINC01705 | 0.004 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises EDNRA's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.39× lower at baseline in the lines without ITGA11 | 0.007 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises EDNRA's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.21× lower at baseline in the lines without WNT5A | 0.008 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[EVA1A-AS]] | C | EVA1A-AS activity raises EDNRA's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.55× lower at baseline in the lines without EVA1A-AS | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises EDNRA's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 3.66× lower at baseline in the lines without PRRX1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises EDNRA's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 3.34× lower at baseline in the lines without COL5A1 | 0.017 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises EDNRA's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.68× lower at baseline in the lines without APCDD1L | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ADAMTS14]] | C | ADAMTS14 activity raises EDNRA's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 3.12× lower at baseline in the lines without ADAMTS14 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises EDNRA's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 3.39× lower at baseline in the lines without LINC01411 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |

### Downstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 12, C 46. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM132A]] | B | EDNRA activity raises TMEM132A's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.62× lower at baseline in the lines without EDNRA | 0.001 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[RAI14]] | B | EDNRA activity raises RAI14's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 3.79× lower at baseline in the lines without EDNRA | 0.003 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[GPR68]] | B | EDNRA activity raises GPR68's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without EDNRA | 0.004 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[SYTL3]] | B | EDNRA activity raises SYTL3's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.46× lower at baseline in the lines without EDNRA | 0.019 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[MRC2]] | B | EDNRA activity raises MRC2's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 4.07× lower at baseline in the lines without EDNRA | 0.021 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[MANCR]] | B | EDNRA activity raises MANCR's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.59× lower at baseline in the lines without EDNRA | 0.032 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[LINC02257]] | B | EDNRA activity raises LINC02257's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without EDNRA | 0.048 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[ABCA1]] | B | EDNRA activity weakens ABCA1's drug response | lines that do not express EDNRA (12) vs lines expressing it (17) | the lines without EDNRA respond 1.11× as strongly (z diff -0.77); rises at some drug-doses, falls at others (71% from rises): Retinoic acid 5 µM: 2.58x vs 1.64x (z diff -3.4); Retinoic acid 0.5 µM: 3.20x vs 1.95x (z diff -3.0); Clotrimazole 5 µM: 0.38x vs 0.51x (z diff -2.1) | 0.060 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; target measured in part of the lines; rises at some drug-doses, falls at others; line-wide correction only |
| [[LTBP1]] | B | EDNRA activity raises LTBP1's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 2.56× lower at baseline in the lines without EDNRA | 0.066 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[SARDH]] | B | EDNRA activity raises SARDH's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 1.99× lower at baseline in the lines without EDNRA | 0.075 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[BOC]] | B | EDNRA activity raises BOC's level | lines that do not express EDNRA (32) vs lines expressing it (18) | 1.85× lower at baseline in the lines without EDNRA | 0.083 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12 |
| [[RAI14]] | B | EDNRA activity strengthens RAI14's drug response | lines that do not express EDNRA (21) vs lines expressing it (17) | the lines without EDNRA respond 0.71× as strongly (z diff +2.27); strongest at Topotecan (hydrochloride) 5 µM: 0.62x vs 0.42x (z diff +4.4) | 0.099 | ⚠ within organs, on part of the lines; also absent: CCBE1, G0S2, ADAMTS12; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (52.2, 16.9); signed map (24.3, 47.7). **Vector** length 49.9, 14.7% of its response variance represented; |z| ≥ 3 in 430 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Collagen biosynthesis and modifying enzymes* (reactome, mean cos +0.51 to 9); *Integrin cell surface interactions* (reactome, mean cos +0.50 to 8); *Signaling by PDGF* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +11.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | -0.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.9 | +1.0 |
|  | [[Carbamazepine (drug)]] 5 µM |  | +0.9 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -1.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.2 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | endothelin receptor type A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.22-q31.23 — chr4:147,480,917-147,544,954 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ET-A, ETA-R, hET-AR |
| Gene groups (HGNC) | Endothelin receptors |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P25101](https://www.uniprot.org/uniprotkb/P25101) (Endothelin-1 receptor):

> Receptor for endothelin-1. Mediates its action by association with G proteins that activate a phosphatidylinositol-calcium second messenger system. The rank order of binding affinities for ET-A is: ET1 > ET2 >> ET3.

**Summary**, from NCBI Gene [1909](https://www.ncbi.nlm.nih.gov/gene/1909):

> This gene encodes the receptor for endothelin-1, a peptide that plays a role in potent and long-lasting vasoconstriction. This receptor associates with guanine-nucleotide-binding (G) proteins, and this coupling activates a phosphatidylinositol-calcium second messenger system. Polymorphisms in this gene have been linked to migraine headache resistance. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:3179](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3179) · Entrez [1909](https://www.ncbi.nlm.nih.gov/gene/1909) · UniProt [P25101](https://www.uniprot.org/uniprotkb/P25101) · Ensembl [ENSG00000151617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151617)

## Data

Gene col 7541: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7541); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7541, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7541]; `tensor/DDL_lfc|DDL_z.npy` [7541]; `embed/gene_vectors.npy` [7541]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7541 or target_col == 7541). Every well: [[EDNRA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDNRA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
