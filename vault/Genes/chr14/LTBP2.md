---
symbol: "LTBP2"
type: "gene"
col: 4095
ensembl_id: "ENSG00000119681"
name: "latent transforming growth factor beta binding protein 2"
location: "14q24.3"
module: 116
arm: "+"
pooled_cpm: 21.58
n_lines_expressing: 34
n_dd_up: 11
n_dd_down: 25
n_dd_up_clean: 8
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 14
direction_downstream: 20
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# LTBP2

*latent transforming growth factor beta binding protein 2* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.33× (z +14.4, q 2e-44, up in 20 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.681× (z -5.7, q 9e-06, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01204]] (+0.69, fdr 7e-06), [[FGF1]] (+0.69, fdr 7e-06), [[ABR]] (+0.66, fdr 7e-06); moves opposite to [[PPP1R12B]] (-0.57, fdr 2e-05), [[PRKRA]] (-0.56, fdr 1e-05), [[ARNT]] (-0.55, fdr 3e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[LINC01629]] → it (grade B ⚠); 20 go from it, the strongest it → [[ACTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +14.4 | 2e-44 | 20/31 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +11.0 | 2e-25 | 14/24 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +10.8 | 5e-25 | 10/19 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +9.0 | 3e-17 | 15/23 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +6.8 | 1e-09 | 11/30 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.2 | 7e-08 | 18/32 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +5.5 | 4e-06 | 16/30 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.016 | 7/29 (HOP62, SW48, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.018 | 7/29 (A498, SNU-423, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.029 | 10/31 (NCI-H2347, RPMI-7951, …) | all doses, flat | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.048 | 5/32 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.20× | +3.1 | 0.097 | 6/32 (Hs 766T, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.681×** | -5.7 | 9e-06 | 19/31 (RKO, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.641×** | -5.3 | 2e-05 | 21/31 (RKO, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.676×** | -5.3 | 2e-05 | 19/32 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.651×** | -5.2 | 3e-05 | 19/31 (PANC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.665×** | -4.9 | 1e-04 | 21/31 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.657×** | -4.8 | 2e-04 | 19/28 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.692×** | -4.4 | 8e-04 | 15/31 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.698×** | -4.3 | 0.001 | 14/30 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Terfenadine (drug)]] 5 µM |  | **0.777×** | -4.3 | 0.001 | 13/31 (NCI-H2347, NCI-H661, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.514×** | -4.2 | 0.002 | 13/26 (RKO, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.523×** | -4.1 | 0.002 | 15/28 (RKO, Hs 766T, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.717×** | -4.0 | 0.003 | 16/29 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.008 | 18/31 (HEC-1-A, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.742×** | -3.6 | 0.014 | 10/31 (SW480, A498, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | **0.811×** | -3.5 | 0.015 | 9/32 (HS-578T, SW 1088, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.594×** | -3.3 | 0.035 | 14/28 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.599×** | -3.2 | 0.040 | 11/27 (RKO, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 220 | 0 | 18 (4 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.102× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 69.6 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -12.2) |
| [[PANC-1 (line)]] | alt | 51.8 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +13.0) | [[Ixazomib citrate (drug)]] 5 µM 0.323× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 43.2 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0832× (z -10.7) |
| [[MIA PaCa-2 (line)]] | alt | 70.7 | 0 | 4 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.273× (z -21.7) ⚠ position not correctable · without an alert: [[Binimetinib (drug)]] 0.5 µM 0.180× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 8.95 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +9.0) | [[Binimetinib (drug)]] 0.5 µM 0.199× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 5.98 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +11.5) | [[Harringtonine (drug)]] 0.05 µM 0.0544× (z -13.3) |
| [[A-172 (line)]] | wt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 26.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +10.9) | — |
| [[NCI-H1792 (line)]] | alt | 7.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 27.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.168× (z -11.3) |
| [[SW480 (line)]] | alt | 13.5 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -9.1) |
| [[A-427 (line)]] | wt | 4.20 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01204]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[FGF1]] | +0.69 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[ABR]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[TOMM34]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CCND1]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[AGO2]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 | pathway: Signaling by TGFB family members |
| [[AXL]] | +0.65 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ARHGAP31]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[MSRA]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[ITGB1-DT]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ROBO4]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12B]] | -0.57 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[PRKRA]] | -0.56 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ARNT]] | -0.55 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[NCK1]] | -0.54 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[CRYZL1]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 7, C 7. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01629]] | B | LINC01629 activity raises LTBP2's level | lines that do not express LINC01629 (30) vs lines expressing it (20) | 2.64× lower at baseline in the lines without LINC01629 | 0.034 | ⚠ within organs, on part of the lines; also absent: XIST, ENSG00000262198, RHEX |
| [[SFTA1P]] | B | SFTA1P activity raises LTBP2's level | lines that do not express SFTA1P (32) vs lines expressing it (18) | 2.16× lower at baseline in the lines without SFTA1P | 0.059 | ⚠ within organs, on part of the lines; also absent: SUN3, SIM1, MMRN1 |
| [[TOP2A]] | B | TOP2A activity lowers LTBP2's level | compounds that target TOP2A: 3 of 5 raise it (Epirubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CFAP299]] | B | CFAP299 activity raises LTBP2's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.96× lower at baseline in the lines without CFAP299 | 0.063 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[LINC01844]] | B | LINC01844 activity raises LTBP2's level | lines that do not express LINC01844 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without LINC01844 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000287712, ADGRG2, ENSG00000291283; maybe low, not absent |
| [[FJX1]] | B | FJX1 activity raises LTBP2's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 2.64× lower at baseline in the lines without FJX1 | 0.091 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[CHST15]] | B | CHST15 activity raises LTBP2's level | lines that do not express CHST15 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without CHST15 | 0.098 | ⚠ within organs, on part of the lines; also absent: SH2D4A |
| [[TMEM156]] | C | TMEM156 activity raises LTBP2's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 2.20× lower at baseline in the lines without TMEM156 | 0.007 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4; co-absent with the target |
| [[ITGB1-DT]] | C | ITGB1-DT activity raises LTBP2's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 3.40× lower at baseline in the lines without ITGB1-DT | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent; co-absent with the target |
| [[ROBO4]] | C | ROBO4 activity raises LTBP2's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.36× lower at baseline in the lines without ROBO4 | 0.020 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1; co-absent with the target |
| [[AXL]] | C | AXL activity raises LTBP2's level | lines that do not express AXL (14) vs lines expressing it (36) | 3.91× lower at baseline in the lines without AXL | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: LGALS1, ENSG00000289526, LTBP2; co-absent with the target |
| [[ADTRP]] | C | ADTRP activity raises LTBP2's level | lines that do not express ADTRP (25) vs lines expressing it (25) | 2.72× lower at baseline in the lines without ADTRP | 0.066 | ⚠ within organs, on part of the lines; also absent: LINC02725, ROBO4, AIM2; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 15, C 5. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTN1]] | B | LTBP2 activity raises ACTN1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.81× lower at baseline in the lines without LTBP2 | 0.009 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[NEPRO-AS1]] | B | LTBP2 activity raises NEPRO-AS1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without LTBP2 | 0.011 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[ELK3]] | B | LTBP2 activity raises ELK3's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 2.65× lower at baseline in the lines without LTBP2 | 0.014 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[SMCO2]] | B | LTBP2 activity raises SMCO2's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.65× lower at baseline in the lines without LTBP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[MIR4435-2HG]] | B | LTBP2 activity raises MIR4435-2HG's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without LTBP2 | 0.024 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[LCP1]] | B | LTBP2 activity raises LCP1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 2.87× lower at baseline in the lines without LTBP2 | 0.037 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[CYTOR]] | B | LTBP2 activity raises CYTOR's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.82× lower at baseline in the lines without LTBP2 | 0.037 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[ASB1]] | B | LTBP2 activity raises ASB1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.48× lower at baseline in the lines without LTBP2 | 0.044 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[ANAPC1P4]] | B | LTBP2 activity raises ANAPC1P4's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.62× lower at baseline in the lines without LTBP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[SCHIP1]] | B | LTBP2 activity raises SCHIP1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without LTBP2 | 0.053 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[ARHGAP31]] | B | LTBP2 activity raises ARHGAP31's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 3.22× lower at baseline in the lines without LTBP2 | 0.057 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |
| [[ATP2C2-AS1]] | B | LTBP2 activity raises ATP2C2-AS1's level | lines that do not express LTBP2 (16) vs lines expressing it (34) | 1.52× lower at baseline in the lines without LTBP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: AXL, MATN3, ENSG00000289526 |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.6, 10.1); signed map (13.4, 45.0). **Vector** length 101, 27.9% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +14.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.5 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.6 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.6 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.9 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.3 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +2.0 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.6 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.9 | -5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.3 | -2.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.2 | -2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | latent transforming growth factor beta binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:74,498,183-74,612,378 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously LTBP3, C14orf141 |
| Gene groups (HGNC) | Latent transforming growth factor beta binding proteins |
| Hallmark sets | TGF_BETA_SIGNALING |
| Reactome | 6 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14767](https://www.uniprot.org/uniprotkb/Q14767) (Latent-transforming growth factor beta-binding protein 2):

> May play an integral structural role in elastic-fiber architectural organization and/or assembly.

**Summary**, from NCBI Gene [4053](https://www.ncbi.nlm.nih.gov/gene/4053):

> The protein encoded by this gene belongs to the family of latent transforming growth factor (TGF)-beta binding proteins (LTBP), which are extracellular matrix proteins with multi-domain structure. This protein is the largest member of the LTBP family possessing unique regions and with most similarity to the fibrillins. It has thus been suggested that it may have multiple functions: as a member of the TGF-beta latent complex, as a structural component of microfibrils, and a role in cell …

**Accessions** — [HGNC:6715](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6715) · Entrez [4053](https://www.ncbi.nlm.nih.gov/gene/4053) · UniProt [Q14767](https://www.uniprot.org/uniprotkb/Q14767) · Ensembl [ENSG00000119681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119681)

## Data

Gene col 4095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4095); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4095]; `tensor/DDL_lfc|DDL_z.npy` [4095]; `embed/gene_vectors.npy` [4095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4095 or target_col == 4095). Every well: [[LTBP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTBP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
