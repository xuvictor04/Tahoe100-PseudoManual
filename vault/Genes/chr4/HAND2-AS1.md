---
symbol: "HAND2-AS1"
type: "gene"
col: 14116
ensembl_id: "ENSG00000237125"
name: "HAND2 antisense RNA 1"
location: "4q34.1"
module: 90
arm: "+"
pooled_cpm: 4.09
n_lines_expressing: 30
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# HAND2-AS1

*HAND2 antisense RNA 1* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.80× (z +18.3, q 0e+00, up in 12 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.160×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.119×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.137×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.302×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALYL]] (+0.69, fdr 7e-06), [[LINC02268]] (+0.67, fdr 7e-06), [[CNTNAP4]] (+0.61, fdr 1e-05); moves opposite to [[ABCC10]] (-0.53, fdr 6e-05), [[AAGAB]] (-0.50, fdr 5e-05), [[HERC2]] (-0.49, fdr 5e-05).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LINC01320]] → it (grade B ⚠); 7 go from it, the strongest it → [[SNX31]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.80×** | +18.3 | 0e+00 | 12/15 (hTERT-HPNE, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.66×** | +10.7 | 3e-24 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.15×** | +9.1 | 2e-17 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +7.1 | 2e-10 | 6/15 (hTERT-HPNE, C32, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.50×** | +7.0 | 3e-10 | 2/3 (hTERT-HPNE, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +6.5 | 8e-09 | 7/19 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +6.1 | 1e-07 | 4/17 (hTERT-HPNE, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.2 | 0.002 | 4/11 (hTERT-HPNE, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.90×** | +3.8 | 0.010 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +3.7 | 0.010 | 2/6 (HEC-1-A, NCI-H1573) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.014 | 4/24 (C32, NCI-H1573, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.30×** | +3.6 | 0.015 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.4 | 0.034 | 0/10 | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.039 | 1/25 (RPMI-7951) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.75×** | +3.3 | 0.039 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.047 | 1/20 (H4) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.07×** | +3.1 | 0.058 | 4/19 (C32, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.45×** | +3.0 | 0.077 | 0/23 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +3.0 | 0.086 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14116.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.160×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (CHP-212 0.119×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.137×); [[Homoharringtonine (drug)]] 5 µM in 1 line (CHP-212 0.302×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hexylresorcinol (drug)]] 0.5 µM |  | 0.673× | -3.3 | 0.21 | 4/22 (hTERT-HPNE, CHP-212, …) | rises with dose | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM |  | 0.679× | -3.2 | 0.21 | 4/21 (RPMI-7951, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Quinestrol (drug)]] 0.5 µM |  | 0.679× | -3.2 | 0.21 | 1/22 (A-172) | inconsistent across doses |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.666× | -3.1 | 0.21 | 1/22 (H4) | inconsistent across doses | position effect removed |
| [[Delamanid (drug)]] 0.05 µM |  | 0.691× | -3.1 | 0.21 | 5/22 (NCI-H2030, HEC-1-A, …) | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 0.771× | -3.1 | 0.21 | 3/25 (CHP-212, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 622 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -17.6) |
| [[hTERT-HPNE (line)]] | wt | 48.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +12.6) | — |
| [[A498 (line)]] | wt | 1.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.34× (z +8.7) | — |
| [[A-172 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.764 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.766 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.731 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.718 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.664 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.725 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.619 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.789 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.685 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.16 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14116), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALYL]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[LINC02268]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[CNTNAP4]] | +0.61 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LINC02932]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[LRRN3]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[LINC02398]] | +0.59 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[CNTNAP5]] | +0.59 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.59 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.58 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SYNM-AS1]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 | same gene group |
| [[CD36]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[LRRC4C]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCC10]] | -0.53 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[AAGAB]] | -0.50 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[HERC2]] | -0.49 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01320]] | B | LINC01320 activity raises HAND2-AS1's level | lines that do not express LINC01320 (41) vs lines expressing it (9) | 2.05× lower at baseline in the lines without LINC01320 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DCT, SOX10, ENSG00000241168 |
| [[DCT]] | B | DCT activity raises HAND2-AS1's level | lines that do not express DCT (42) vs lines expressing it (8) | 2.37× lower at baseline in the lines without DCT | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1 |
| [[TWIST1]] | B | TWIST1 activity raises HAND2-AS1's level | lines that do not express TWIST1 (26) vs lines expressing it (24) | 1.88× lower at baseline in the lines without TWIST1 | 0.028 | ⚠ within organs, on part of the lines; also absent: PCDH10, MDGA2, FAP |
| [[DDX3Y]] | B | DDX3Y activity raises HAND2-AS1's level | lines that do not express DDX3Y (30) vs lines expressing it (20) | 1.93× lower at baseline in the lines without DDX3Y | 0.059 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: UTY, EIF1AY, ANOS2P |
| [[RALYL]] | B | RALYL activity raises HAND2-AS1's level | lines that do not express RALYL (17) vs lines expressing it (33) | 1.81× lower at baseline in the lines without RALYL | 0.064 | ⚠ within organs, on part of the lines; also absent: ENSG00000251294, TMTC1, LINC00882; maybe low, not absent |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNX31]] | B | HAND2-AS1 activity raises SNX31's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without HAND2-AS1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| [[PPP1R42]] | B | HAND2-AS1 activity raises PPP1R42's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.40× lower at baseline in the lines without HAND2-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| [[HSPA2-AS1]] | B | HAND2-AS1 activity raises HSPA2-AS1's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.12× lower at baseline in the lines without HAND2-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| [[RFTN2]] | B | HAND2-AS1 activity raises RFTN2's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.49× lower at baseline in the lines without HAND2-AS1 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| cells under [[Trifluridine (drug)]] 5 µM | B | HAND2-AS1 activity lowers the cells' numbers under Trifluridine 5 µM (makes them more sensitive) | lines that do not express HAND2-AS1 (20) vs lines expressing it (28) | the lines without HAND2-AS1: 1.11× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| [[LANCL1-AS1]] | B | HAND2-AS1 activity raises LANCL1-AS1's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.18× lower at baseline in the lines without HAND2-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |
| [[STX17-DT]] | B | HAND2-AS1 activity raises STX17-DT's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without HAND2-AS1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.551). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.3, 24.0); signed map (29.5, 11.9). **Vector** length 29.8, 4.20% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +1.8 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -0.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -2.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -2.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | HAND2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4q34.1 — chr4:173,527,270-173,659,696 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DEIN, NBLA00301, FLJ11539 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48872) · Entrez [79804](https://www.ncbi.nlm.nih.gov/gene/79804) · Ensembl [ENSG00000237125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237125)

## Data

Gene col 14116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14116); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14116, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14116]; `tensor/DDL_lfc|DDL_z.npy` [14116]; `embed/gene_vectors.npy` [14116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14116 or target_col == 14116). Every well: [[HAND2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAND2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
