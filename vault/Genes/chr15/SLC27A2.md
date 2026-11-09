---
symbol: "SLC27A2"
type: "gene"
col: 6385
ensembl_id: "ENSG00000140284"
name: "solute carrier family 27 member 2"
location: "15q21.2"
module: 55
arm: "+"
pooled_cpm: 5.92
n_lines_expressing: 31
n_dd_up: 21
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 8
direction_downstream: 14
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# SLC27A2

*solute carrier family 27 member 2* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.44× (z +9.7, q 1e-19, up in 5 of 7 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.83× (z +9.6, q 1e-19, up in 20 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.539× (z -7.0, q 1e-09, down in 21 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTPA]] (+0.68, fdr 7e-06), [[LARGE2]] (+0.65, fdr 7e-06), [[PPARGC1B]] (+0.63, fdr 7e-06); moves opposite to [[ATXN1L]] (-0.61, fdr 4e-05), [[CCNT2-AS1]] (-0.57, fdr 5e-05), [[STXBP2]] (-0.57, fdr 3e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[XK]] → it (grade B ⚠); 14 go from it, the strongest it → [[CYP2J2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.44×** | +9.7 | 1e-19 | 5/7 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.83×** | +9.6 | 1e-19 | 20/27 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.16×** | +8.7 | 7e-16 | 20/28 (NCI-H1792, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +7.2 | 6e-11 | 17/27 (J82, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.89×** | +7.2 | 6e-11 | 17/28 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.86×** | +7.0 | 2e-10 | 6/18 (CFPAC-1, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.79×** | +6.6 | 4e-09 | 15/29 (NCI-H1573, NCI-H2030, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.82×** | +6.5 | 6e-09 | 8/18 (LoVo, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.76×** | +6.4 | 1e-08 | 15/28 (NCI-H1573, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.63×** | +5.5 | 2e-06 | 16/27 (COLO 205, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.63×** | +5.1 | 1e-05 | 2/13 (A549, LS 180) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +5.0 | 3e-05 | 12/25 (NCI-H2347, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.32×** | +4.4 | 4e-04 | 13/27 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.40×** | +3.8 | 0.007 | 6/27 (J82, SHP-77, …) | all doses, stronger at high dose |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +3.7 | 0.007 | 4/27 (LS 180, HT-29, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.83×** | +3.6 | 0.012 | 6/26 (HT-29, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.026 | 7/27 (J82, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.029 | 5/27 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.65×** | +2.9 | 0.087 | 4/20 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -7.0 | 1e-09 | 21/28 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.570×** | -6.4 | 5e-08 | 15/27 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.682×** | -4.3 | 0.003 | 16/24 (SW48, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.705×** | -4.0 | 0.010 | 12/27 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.725×** | -3.7 | 0.029 | 14/25 (RKO, LoVo, …) | two highest doses |  |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.728×** | -3.4 | 0.061 | 4/27 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.568×** | -3.4 | 0.065 | 5/25 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.574×** | -3.3 | 0.066 | 4/29 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.749×** | -3.3 | 0.066 | 10/26 (SHP-77, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 21.1 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0980× (z -12.3) |
| [[SW48 (line)]] | wt | 24.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -14.5) ⚠ cell-cycle shift, explains ~7% of this change |
| [[NCI-H2030 (line)]] | alt | 4.60 | 0 | 3 (1 ⚠) | — | [[Ferulic acid (drug)]] 0.05 µM 0.0586× (z -11.2) |
| [[LoVo (line)]] | wt | 25.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -11.4) ⚠ cell-cycle shift, explains ~7% of this change |
| [[SW480 (line)]] | alt | 11.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.175× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.249× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.688 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.690 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.814 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.828 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.786 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.760 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTPA]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[LARGE2]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PPARGC1B]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[LYPD6]] | +0.63 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[FAM221A]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[FXN]] | +0.63 | +0.43 / +0.67 | both halves | 4e-05 | pathway: Protein localization |
| [[ASB13]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[CKMT1A]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[THEM6]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[TRAK1]] | +0.61 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[CKMT1B]] | +0.61 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[UCK2]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN1L]] | -0.61 | -0.40 / -0.66 | both halves | 4e-05 |  |
| [[CCNT2-AS1]] | -0.57 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[STXBP2]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[UBE3B]] | -0.54 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[LINC01004]] | -0.54 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[ZNF490]] | -0.54 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[CPEB2-DT]] | -0.53 | -0.29 / -0.47 | both halves | 3e-04 |  |
| [[WDR45]] | -0.53 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[EFCAB6]] | -0.52 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[BCL10-AS1]] | -0.52 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[CYTH2]] | -0.51 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[GTF2IRD2]] | -0.51 | -0.44 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XK]] | B | XK activity raises SLC27A2's level | lines that do not express XK (18) vs lines expressing it (32) | 2.00× lower at baseline in the lines without XK | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD12, MARVELD2, BTC; maybe low, not absent |
| [[PPM1H]] | B | PPM1H activity raises SLC27A2's level | lines that do not express PPM1H (11) vs lines expressing it (39) | 2.55× lower at baseline in the lines without PPM1H | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, MGST2, CXCL16; maybe low, not absent |
| [[TMEM98]] | B | TMEM98 activity raises SLC27A2's level | lines that do not express TMEM98 (18) vs lines expressing it (32) | 1.67× lower at baseline in the lines without TMEM98 | 0.072 | ⚠ within organs, on part of the lines; also absent: PGAP4, EDARADD, RPS6KA6; maybe low, not absent |
| [[PIK3AP1]] | C | PIK3AP1 activity raises SLC27A2's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 3.19× lower at baseline in the lines without PIK3AP1 | 0.009 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |
| [[NMNAT3]] | C | NMNAT3 activity raises SLC27A2's level | lines that do not express NMNAT3 (17) vs lines expressing it (33) | 2.79× lower at baseline in the lines without NMNAT3 | 0.021 | ⚠ within organs, on part of the lines; also absent: HOOK1, RASAL1, CHMP4C; co-absent with the target |
| [[RAPGEF5]] | C | RAPGEF5 activity raises SLC27A2's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.65× lower at baseline in the lines without RAPGEF5 | 0.040 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent; co-absent with the target |
| [[GPX2]] | C | GPX2 activity raises SLC27A2's level | lines that do not express GPX2 (36) vs lines expressing it (14) | 3.08× lower at baseline in the lines without GPX2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCNT3, F5, TRIM31; co-absent with the target |
| [[SMPDL3B]] | C | SMPDL3B activity raises SLC27A2's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 2.86× lower at baseline in the lines without SMPDL3B | 0.099 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 9, C 5. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP2J2]] | B | SLC27A2 activity raises CYP2J2's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 1.73× lower at baseline in the lines without SLC27A2 | 0.011 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[PPM1H]] | B | SLC27A2 activity raises PPM1H's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.50× lower at baseline in the lines without SLC27A2 | 0.014 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[SULT1A1]] | B | SLC27A2 activity raises SULT1A1's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 1.97× lower at baseline in the lines without SLC27A2 | 0.044 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | SLC27A2 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express SLC27A2 (19) vs lines expressing it (29) | the lines without SLC27A2: 0.95× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[PRKCQ]] | B | SLC27A2 activity raises PRKCQ's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without SLC27A2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| cells under [[Ritonavir (drug)]] 0.5 µM | B | SLC27A2 activity raises the cells' numbers under Ritonavir 0.5 µM (protects the cells) | lines that do not express SLC27A2 (19) vs lines expressing it (29) | the lines without SLC27A2: 0.87× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[STXBP6]] | B | SLC27A2 activity raises STXBP6's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 1.61× lower at baseline in the lines without SLC27A2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | SLC27A2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express SLC27A2 (19) vs lines expressing it (29) | the lines without SLC27A2: 0.81× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[SLAIN1]] | B | SLC27A2 activity raises SLAIN1's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without SLC27A2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[RAPGEF5]] | C | SLC27A2 activity raises RAPGEF5's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 3.71× lower at baseline in the lines without SLC27A2 | 0.009 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656; co-absent with the target |
| [[SMPDL3B]] | C | SLC27A2 activity raises SMPDL3B's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 2.94× lower at baseline in the lines without SLC27A2 | 0.019 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656; co-absent with the target |
| [[PLS1]] | C | SLC27A2 activity raises PLS1's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 3.57× lower at baseline in the lines without SLC27A2 | 0.031 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.512). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.1, 44.2); signed map (60.0, 13.9). **Vector** length 58.5, 12.8% of its response variance represented; |z| ≥ 3 in 590 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.5 | +7.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.2 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +2.9 | +9.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.5 | +5.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.7 | +3.8 |
|  | [[Brivudine (drug)]] 0.5 µM |  | +1.4 | +1.9 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -7.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 27 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:50,182,196-50,236,385 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FATP2, hFACVL1, VLACS, VLCS, HsT17226, ACSVL1; previously FACVL1 |
| Gene groups (HGNC) | Acyl-CoA synthetase family; Solute carrier family 27 |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 15 pathways, smallest: Alpha-oxidation of phytanate; Beta-oxidation of very long chain fatty acids; Synthesis of bile acids and bile salts via 24-hydroxycholesterol |
| Matched by | ensembl_id |

**Function**, from UniProt [O14975](https://www.uniprot.org/uniprotkb/O14975) (Long-chain fatty acid transport protein 2):

> Mediates the import of long-chain fatty acids (LCFA) into the cell by facilitating their transport across cell membranes, playing an important role in hepatic fatty acid uptake. Also functions as an acyl-CoA ligase catalyzing the ATP-dependent formation of fatty acyl-CoA using LCFA and very-long-chain fatty acids (VLCFA) as substrates, which prevents fatty acid efflux from cells and might drive more fatty acid uptake. Plays a pivotal role in regulating available LCFA substrates from exogenous …

**Summary**, from NCBI Gene [11001](https://www.ncbi.nlm.nih.gov/gene/11001):

> The protein encoded by this gene is an isozyme of long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. This isozyme activates long-chain, branched-chain and very-long-chain fatty acids containing 22 or more carbons to their CoA …

**Accessions** — [HGNC:10996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10996) · Entrez [11001](https://www.ncbi.nlm.nih.gov/gene/11001) · UniProt [O14975](https://www.uniprot.org/uniprotkb/O14975) · Ensembl [ENSG00000140284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140284)

## Data

Gene col 6385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6385); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6385]; `tensor/DDL_lfc|DDL_z.npy` [6385]; `embed/gene_vectors.npy` [6385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6385 or target_col == 6385). Every well: [[SLC27A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC27A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
