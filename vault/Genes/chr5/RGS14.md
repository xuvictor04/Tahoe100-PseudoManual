---
symbol: "RGS14"
type: "gene"
col: 9774
ensembl_id: "ENSG00000169220"
name: "regulator of G protein signaling 14"
location: "5q35.3"
module: 85
arm: "+"
pooled_cpm: 3.8
n_lines_expressing: 46
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 2
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# RGS14

*regulator of G protein signaling 14* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.67× (z +4.5, q 0.003, up in 1 of 6 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.37× (z +4.1, q 0.011, up in 11 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.390× (z -12.2, q 1e-31, down in 30 of 32 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A1]] (+0.69, fdr 3e-05), [[OSBPL7]] (+0.68, fdr 1e-05), [[MAST3]] (+0.68, fdr 4e-05); moves opposite to [[MMADHC-DT]] (-0.66, fdr 8e-04, ⚠ one half only (not replicated)), [[SDCBP2-AS1]] (-0.64, fdr 1e-05), [[HEXIM2-AS1]] (-0.64, fdr 2e-04), [[TUG1]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AZGP1]] → it (grade B ⚠); 5 go from it, the strongest it → [[RAB30-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **1.67×** | +4.5 | 0.003 | 1/6 (A498) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.011 | 11/39 (PANC-1, COLO 205, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +3.7 | 0.038 | 5/22 (A-172, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.49×** | +3.6 | 0.038 | 13/40 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +3.5 | 0.045 | 5/26 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.46×** | +3.5 | 0.045 | 10/42 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.4 | 0.055 | 2/10 (LS 180, CFPAC-1) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | 1.40× | +3.1 | 0.12 | 2/18 (HEC-1-A, A498) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.42× | +3.1 | 0.13 | 4/19 (SNU-423, A498, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.39× | +3.0 | 0.15 | 6/40 (KATO III, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.390×** | -12.2 | 1e-31 | 30/32 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.385×** | -8.8 | 5e-16 | 23/31 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.404×** | -8.0 | 2e-13 | 28/38 (NCI-H2347, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -7.8 | 9e-13 | 26/43 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.442×** | -7.5 | 7e-12 | 22/38 (C32, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.536×** | -5.7 | 1e-06 | 20/37 (LoVo, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -5.6 | 2e-06 | 17/27 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.324×** | -5.4 | 4e-06 | 16/37 (NCI-H2347, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -5.2 | 1e-05 | 17/32 (C32, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.633×** | -4.0 | 0.004 | 8/38 (A-427, SW480, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.658×** | -3.8 | 0.006 | 12/26 (C32, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.689×** | -3.4 | 0.030 | 11/37 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.496×** | -3.4 | 0.033 | 11/38 (SW480, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.699×** | -3.3 | 0.040 | 8/40 (SW 900, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -3.2 | 0.058 | 15/31 (CFPAC-1, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | **0.531×** | -3.0 | 0.084 | 5/40 (MIA PaCa-2, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 6.28 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0520× (z -14.7) |
| [[PANC-1 (line)]] | alt | 2.40 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 3.02 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0397× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 6.62 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0286× (z -20.3) |
| [[NCI-H2347 (line)]] | alt | 12.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -19.2) |
| [[SW480 (line)]] | alt | 5.59 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -12.0) |
| [[HOP62 (line)]] | alt | 3.96 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -14.6) |
| [[Hs 766T (line)]] | wt | 4.06 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.149× (z -9.0) |
| [[KATO III (line)]] | alt | 3.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 8.29 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.2) |
| [[Panc 03.27 (line)]] | alt | 6.71 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 6.88 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.5) |
| [[SW 900 (line)]] | alt | 8.48 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -9.2) |
| [[SW1417 (line)]] | alt | 5.11 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0678× (z -9.2) |
| [[A-172 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.978 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.283 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.524 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.51 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A1]] | +0.69 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[OSBPL7]] | +0.68 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[MAST3]] | +0.68 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[ZNF511]] | +0.67 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[TNNI3]] | +0.67 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.67 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[PLCD1]] | +0.66 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[NFRKB]] | +0.66 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ABCB9]] | +0.65 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.65 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CARHSP1]] | +0.65 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[YIF1B]] | +0.64 | +0.53 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMADHC-DT]] | -0.66 | -0.63 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SDCBP2-AS1]] | -0.64 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[HEXIM2-AS1]] | -0.64 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[TUG1]] | -0.63 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZMYND11]] | -0.63 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[DGKH]] | -0.62 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[PSME3IP1]] | -0.62 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.62 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[PBLD]] | -0.62 | -0.56 / -0.23 | both halves | 5e-04 |  |
| [[ST7L]] | -0.61 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[PSMD6-AS1]] | -0.61 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.61 | -0.58 / -0.23 | both halves | 5e-04 |  |
| [[PKN2-AS1]] | -0.61 | -0.51 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AZGP1]] | B | AZGP1 activity raises RGS14's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 1.57× lower at baseline in the lines without AZGP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |
| [[TOP2A]] | B | TOP2A activity raises RGS14's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[INPP5F]] | C | INPP5F's natural level strengthens RGS14's drug response | INPP5F's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.39; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB30-DT]] | C | RGS14 activity lowers RAB30-DT's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.61× higher at baseline in the lines without RGS14 | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[FAM104A]] | C | RGS14's natural level strengthens FAM104A's drug response | RGS14's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.20; direction not clear | 0.078 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[KLHL26]] | C | RGS14 activity lowers KLHL26's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without RGS14 | 0.080 | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[KCTD17]] | C | RGS14 activity lowers KCTD17's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without RGS14 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines |
| [[MAD2L1-DT]] | C | RGS14 activity lowers MAD2L1-DT's level | lines that do not express RGS14 (4) vs lines expressing it (46) | 1.33× higher at baseline in the lines without RGS14 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.740). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (5.4, -5.7); signed map (-30.7, 19.9). **Vector** length 60.5, 10.7% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.5 | +3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.5 | +3.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.2 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +4.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.1 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.4 | -12.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.1 | -8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.6 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:177,357,924-177,372,596 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulators of G-protein signaling |
| Reactome | 3 pathways, smallest: G alpha (i) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [O43566](https://www.uniprot.org/uniprotkb/O43566) (Regulator of G protein signaling 14):

> Regulates G protein-coupled receptor signaling cascades. Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound form. Besides, modulates signal transduction via G protein alpha subunits by functioning as a GDP-dissociation inhibitor (GDI). Has GDI activity on G(i) alpha subunits GNAI1 and GNAI3, but not on GNAI2 and G(o)-alpha subunit GNAO1. Has GAP activity on GNAI0, GNAI2 and GNAI3. May act as a scaffold …

**Summary**, from NCBI Gene [10636](https://www.ncbi.nlm.nih.gov/gene/10636):

> This gene encodes a member of the regulator of G-protein signaling family. This protein contains one RGS domain, two Raf-like Ras-binding domains (RBDs), and one GoLoco domain. The protein attenuates the signaling activity of G-proteins by binding, through its GoLoco domain, to specific types of activated, GTP-bound G alpha subunits. Acting as a GTPase activating protein (GAP), the protein increases the rate of conversion of the GTP to GDP. This hydrolysis allows the G alpha subunits to bind G …

**Accessions** — [HGNC:9996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9996) · Entrez [10636](https://www.ncbi.nlm.nih.gov/gene/10636) · UniProt [O43566](https://www.uniprot.org/uniprotkb/O43566) · Ensembl [ENSG00000169220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169220)

## Data

Gene col 9774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9774); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9774]; `tensor/DDL_lfc|DDL_z.npy` [9774]; `embed/gene_vectors.npy` [9774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9774 or target_col == 9774). Every well: [[RGS14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
