---
symbol: "C4orf19"
type: "gene"
col: 7794
ensembl_id: "ENSG00000154274"
name: "PDCD10 and GCKIII kinases associated 1"
location: "4p14"
module: 8
arm: "+"
pooled_cpm: 19.01
n_lines_expressing: 37
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 21
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 60
direction_downstream: 18
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# C4orf19

*PDCD10 and GCKIII kinases associated 1* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.41× (z +18.6, q 0e+00, up in 31 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[OTS514 (drug)]] 0.05 µM: 0.704× (z -5.0, q 4e-04, down in 4 of 33 measured lines) ⚠ transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.0838×, KATO III 0.237×, HT-29 0.205×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (COLO 205 0.119×, HT-29 0.134×); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.189×; ⚠ cell-cycle shift, explains ~9% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.347×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC40A1]] (+0.69, fdr 7e-06), [[TRIM31]] (+0.67, fdr 7e-06), [[STEAP4]] (+0.66, fdr 7e-06); moves opposite to [[FOXL1]] (-0.47, fdr 3e-05).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[GRHL2]] → it (grade B ⚠); 18 go from it, the strongest it → [[PLEKHG6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.41×** | +18.6 | 0e+00 | 31/35 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.44×** | +13.4 | 3e-38 | 8/25 (CFPAC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.4 | 1e-27 | 17/31 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.10×** | +11.2 | 1e-26 | 23/34 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.10×** | +11.1 | 1e-26 | 24/34 (NCI-H1573, J82, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +10.9 | 1e-25 | 24/34 (NCI-H1573, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.91×** | +9.7 | 3e-20 | 22/33 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +9.3 | 9e-19 | 21/34 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +8.6 | 6e-16 | 7/20 (SW 900, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +8.2 | 2e-14 | 5/17 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.4 | 7e-09 | 15/28 (SW 900, J82, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.12×** | +5.9 | 2e-07 | 17/32 (LS 180, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.34×** | +5.3 | 5e-06 | 16/34 (LS 180, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.8 | 5e-05 | 4/31 (NCI-H23, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.36×** | +4.3 | 7e-04 | 13/35 (LS 180, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.44×** | +3.9 | 0.003 | 2/33 (CFPAC-1, NCI-H1792) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.012 | 15/33 (LS 180, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.012 | 13/34 (LS 180, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.027 | 5/34 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7794.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (COLO 205 0.0838×, KATO III 0.237×, HT-29 0.205×; ⚠ toxic; transcription drop); [[Auranofin (drug)]] 5 µM in 2 lines (COLO 205 0.119×, HT-29 0.134×); [[Bortezomib (drug)]] 0.05 µM in 1 line (HT-29 0.189×; ⚠ cell-cycle shift, explains ~9% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (HT-29 0.347×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.704×** | -5.0 | 4e-04 | 4/33 (PANC-1, SW 900, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.784× | -3.5 | 0.13 | 5/35 (A498, HepG2/C3A, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -3.2 | 0.27 | 4/35 (A-427, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 267 | 0 | 6 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.134× (z -13.6) |
| [[A498 (line)]] | wt | 20.5 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.82× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 92.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0838× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.119× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 10.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.08× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 8.29 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 5.45× (z +12.8) | — |
| [[A-427 (line)]] | wt | 6.89 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.10× (z +9.0) | — |
| [[CFPAC-1 (line)]] | alt | 7.23 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.45× (z +11.2) | — |
| [[KATO III (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.37× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 17.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.87× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A-172 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.74 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 41.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC40A1]] | +0.69 | +0.60 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[TRIM31]] | +0.67 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[STEAP4]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[BCL2L15]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RASSF6]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TMC5]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SAMD12]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[MUC4]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[ELF3-AS1]] | +0.59 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ATP10B]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ALOX5]] | +0.59 | +0.46 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXL1]] | -0.47 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 59, C 1. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRHL2]] | B | GRHL2 activity raises C4orf19's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 3.29× lower at baseline in the lines without GRHL2 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[ATP10B]] | B | ATP10B activity raises C4orf19's level | lines that do not express ATP10B (40) vs lines expressing it (10) | 4.68× lower at baseline in the lines without ATP10B | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17 |
| [[CDH17]] | B | CDH17 activity raises C4orf19's level | lines that do not express CDH17 (40) vs lines expressing it (10) | 4.10× lower at baseline in the lines without CDH17 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, MUC13, CLRN3 |
| [[ARHGEF38]] | B | ARHGEF38 activity raises C4orf19's level | lines that do not express ARHGEF38 (36) vs lines expressing it (14) | 3.49× lower at baseline in the lines without ARHGEF38 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, TMEM125, SLC5A1 |
| [[SIDT1]] | B | SIDT1 activity raises C4orf19's level | lines that do not express SIDT1 (32) vs lines expressing it (18) | 2.93× lower at baseline in the lines without SIDT1 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM30B, STEAP4, GRHL2 |
| [[STEAP4]] | B | STEAP4 activity raises C4orf19's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 3.23× lower at baseline in the lines without STEAP4 | 0.006 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1 |
| [[ANK3]] | B | ANK3 activity raises C4orf19's level | lines that do not express ANK3 (23) vs lines expressing it (27) | 2.29× lower at baseline in the lines without ANK3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ATP2C2, MACC1, GALNT3 |
| [[RASSF6]] | B | RASSF6 activity raises C4orf19's level | lines that do not express RASSF6 (28) vs lines expressing it (22) | 2.58× lower at baseline in the lines without RASSF6 | 0.008 | ⚠ within organs, on part of the lines; also absent: TOX3, ELF3, ITGB6 |
| [[NR3C2]] | B | NR3C2 activity raises C4orf19's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without NR3C2 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[TMPRSS2]] | B | TMPRSS2 activity raises C4orf19's level | lines that do not express TMPRSS2 (35) vs lines expressing it (15) | 2.88× lower at baseline in the lines without TMPRSS2 | 0.011 | ⚠ within organs, on part of the lines; also absent: SLC5A1, ARHGEF38, ITGB6 |
| [[MUC13]] | B | MUC13 activity raises C4orf19's level | lines that do not express MUC13 (40) vs lines expressing it (10) | 3.74× lower at baseline in the lines without MUC13 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, NPSR1, CDH17 |
| [[PRR15]] | B | PRR15 activity raises C4orf19's level | lines that do not express PRR15 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without PRR15 | 0.014 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, RNF223, FAM110C |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHG6]] | B | C4orf19 activity raises PLEKHG6's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without C4orf19 | 0.007 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[GRHL2]] | B | C4orf19 activity raises GRHL2's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 4.14× lower at baseline in the lines without C4orf19 | 0.013 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[ST14]] | B | C4orf19 activity raises ST14's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 4.01× lower at baseline in the lines without C4orf19 | 0.019 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[SMPDL3B]] | B | C4orf19 activity raises SMPDL3B's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without C4orf19 | 0.023 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[C6orf132]] | B | C4orf19 activity raises C6orf132's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 3.25× lower at baseline in the lines without C4orf19 | 0.028 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[TJP3]] | B | C4orf19 activity raises TJP3's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without C4orf19 | 0.028 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[TC2N]] | B | C4orf19 activity raises TC2N's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.92× lower at baseline in the lines without C4orf19 | 0.045 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[RAB17]] | B | C4orf19 activity raises RAB17's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.86× lower at baseline in the lines without C4orf19 | 0.048 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[NPNT]] | B | C4orf19 activity raises NPNT's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.56× lower at baseline in the lines without C4orf19 | 0.054 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[SLC44A3-AS1]] | B | C4orf19 activity raises SLC44A3-AS1's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without C4orf19 | 0.067 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[CATSPERB]] | B | C4orf19 activity raises CATSPERB's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.75× lower at baseline in the lines without C4orf19 | 0.071 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |
| [[TMPRSS2]] | B | C4orf19 activity raises TMPRSS2's level | lines that do not express C4orf19 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without C4orf19 | 0.072 | ⚠ within organs, on part of the lines; also absent: RASEF, ARHGEF35-AS1, LNX1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.640). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.1, 53.8); signed map (59.4, 2.4). **Vector** length 68.4, 13.6% of its response variance represented; |z| ≥ 3 in 827 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.3 | +18.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.7 | +9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +13.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +8.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.9 | +5.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.5 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.5 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | PDCD10 and GCKIII kinases associated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:37,453,925-37,623,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11017; previously C4orf19 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY42](https://www.uniprot.org/uniprotkb/Q8IY42) (PDCD10 and GCKIII kinases-associated protein 1):

> Acts as a tumor suppressor. Acts as a tumor suppressor for colorectal cancer cell proliferation by targeting KEAP1/USP17/ELK1/CDK6 axis.

**Summary**, from NCBI Gene [55286](https://www.ncbi.nlm.nih.gov/gene/55286):

> Involved in regulation of cell cycle. Located in cell periphery. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25618](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25618) · Entrez [55286](https://www.ncbi.nlm.nih.gov/gene/55286) · UniProt [Q8IY42](https://www.uniprot.org/uniprotkb/Q8IY42) · Ensembl [ENSG00000154274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154274)

## Data

Gene col 7794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7794); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7794]; `tensor/DDL_lfc|DDL_z.npy` [7794]; `embed/gene_vectors.npy` [7794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7794 or target_col == 7794). Every well: [[C4orf19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C4orf19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
