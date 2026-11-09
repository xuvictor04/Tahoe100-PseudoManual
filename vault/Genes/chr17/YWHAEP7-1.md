---
symbol: "YWHAEP7-1"
type: "gene"
col: 16509
ensembl_id: "ENSG00000290810"
name: ""
location: ""
module: 27
arm: "+"
pooled_cpm: 2.07
n_lines_expressing: 37
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 2
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# YWHAEP7-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.34× (z +13.4, q 7e-38, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.45× (z +13.2, q 4e-37, up in 4 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.585× (z -4.0, q 0.029, down in 6 of 24 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0373×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.205×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SW480 0.109×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.335×); [[c-Kit-IN-1 (drug)]] 5 µM in 1 line (CFPAC-1 0.0544×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02254]] (+0.55, fdr 2e-04), [[PKHD1]] (+0.54, fdr 1e-04), [[ZNF630]] (+0.54, fdr 9e-05); moves opposite to [[EPIC1]] (-0.50, fdr 8e-05), [[RSU1]] (-0.44, fdr 3e-04), [[AGAP1]] (-0.43, fdr 3e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[LINC01967]] → it (grade B ⚠); 2 go from it, the strongest it → [[CYP27A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16509.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.34×** | +13.4 | 7e-38 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +13.2 | 4e-37 | 4/11 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.64×** | +13.0 | 2e-36 | 2/6 (NCI-H460, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.16×** | +9.9 | 6e-21 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +5.6 | 2e-06 | 1/12 (SW480) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.09×** | +5.5 | 3e-06 | 1/5 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.01×** | +5.2 | 1e-05 | 6/19 (NCI-H2030, A-427, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.48×** | +4.9 | 8e-05 | 1/5 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +4.8 | 9e-05 | 3/17 (C32, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +4.6 | 2e-04 | 0/6 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.54×** | +4.6 | 3e-04 | 1/27 (CFPAC-1) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.0 | 0.003 | 2/26 (HEC-1-A, A498) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +3.9 | 0.005 | 9/25 (CFPAC-1, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +3.9 | 0.005 | 1/12 (A549) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +3.7 | 0.007 | 10/25 (CFPAC-1, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.65×** | +3.5 | 0.016 | 2/6 (A498, SW480) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +3.4 | 0.023 | 8/13 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.81×** | +3.2 | 0.039 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.0 | 0.060 | 3/8 (A498, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.49×** | +3.0 | 0.062 | 0/8 | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.47×** | +2.9 | 0.080 | 2/11 (CFPAC-1, A498) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +2.9 | 0.086 | 4/12 (CFPAC-1, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16509.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0373×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.205×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SW480 0.109×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (CFPAC-1 0.335×); [[c-Kit-IN-1 (drug)]] 5 µM in 1 line (CFPAC-1 0.0544×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.585×** | -4.0 | 0.029 | 6/24 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.653× | -3.2 | 0.36 | 7/28 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~22% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16509. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -12.7) |
| [[SW480 (line)]] | alt | 4.61 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.109× (z -9.2) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0373× (z -14.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.425 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.713 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.555 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.718 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.674 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.601 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.990 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.535 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.570 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.991 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.627 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.612 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.656 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.558 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.493 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.579 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.617 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.578 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.667 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.627 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.827 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.654 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.554 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.629 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.619 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.611 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.477 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16509), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02254]] | +0.55 | +0.61 / +0.30 | both halves | 2e-04 |  |
| [[PKHD1]] | +0.54 | +0.56 / +0.36 | both halves | 1e-04 |  |
| [[ZNF630]] | +0.54 | +0.48 / +0.36 | both halves | 9e-05 |  |
| [[SLC15A1]] | +0.54 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[LINC00649]] | +0.53 | +0.56 / +0.30 | both halves | 2e-04 |  |
| [[CCR3]] | +0.53 | +0.54 / +0.30 | both halves | 2e-04 |  |
| [[ABCC6]] | +0.53 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[ARHGAP25]] | +0.52 | +0.52 / +0.32 | both halves | 2e-04 |  |
| [[NSUN7]] | +0.52 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[WDR72]] | +0.51 | +0.36 / +0.59 | both halves | 9e-05 |  |
| [[GUCY1B2]] | +0.51 | +0.50 / +0.25 | both halves | 4e-04 |  |
| [[CSAG1]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPIC1]] | -0.50 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[RSU1]] | -0.44 | -0.39 / -0.27 | both halves | 3e-04 |  |
| [[AGAP1]] | -0.43 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[MLXIP]] | -0.42 | -0.34 / -0.29 | both halves | 2e-04 |  |
| [[SLC25A39]] | -0.42 | -0.28 / -0.38 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01967]] | B | LINC01967 activity raises YWHAEP7-1's level | lines that do not express LINC01967 (38) vs lines expressing it (12) | 1.17× lower at baseline in the lines without LINC01967 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000234352, SLC15A5, PCSK1 |
| [[TMEM163]] | B | TMEM163 activity raises YWHAEP7-1's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 1.65× lower at baseline in the lines without TMEM163 | 0.030 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2 |
| [[SLC15A1]] | B | SLC15A1 activity raises YWHAEP7-1's level | lines that do not express SLC15A1 (40) vs lines expressing it (10) | 2.12× lower at baseline in the lines without SLC15A1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SLC15A5, GSDMC, TBXT |
| [[TOP2A]] | B | TOP2A activity lowers YWHAEP7-1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ST6GALNAC5]] | B | ST6GALNAC5 activity raises YWHAEP7-1's level | lines that do not express ST6GALNAC5 (31) vs lines expressing it (19) | 1.43× lower at baseline in the lines without ST6GALNAC5 | 0.045 | ⚠ within organs, on part of the lines; also absent: TRBC2, ENPP5, KCNH8 |
| [[CCR3]] | B | CCR3 activity raises YWHAEP7-1's level | lines that do not express CCR3 (35) vs lines expressing it (15) | 1.61× lower at baseline in the lines without CCR3 | 0.055 | ⚠ within organs, on part of the lines; also absent: HOPX, KRT23, SERPINB11 |
| [[WFDC2]] | B | WFDC2 activity raises YWHAEP7-1's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 1.74× lower at baseline in the lines without WFDC2 | 0.064 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1 |
| [[FXYD2]] | B | FXYD2 activity raises YWHAEP7-1's level | lines that do not express FXYD2 (38) vs lines expressing it (12) | 1.31× lower at baseline in the lines without FXYD2 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSCAML1, ITIH2, FGA |
| [[VAV1]] | B | VAV1 activity raises YWHAEP7-1's level | lines that do not express VAV1 (23) vs lines expressing it (27) | 1.40× lower at baseline in the lines without VAV1 | 0.080 | ⚠ within organs, on part of the lines; also absent: COL4A4, COL4A3, C3; maybe low, not absent |
| [[GABRP]] | B | GABRP activity raises YWHAEP7-1's level | lines that do not express GABRP (44) vs lines expressing it (6) | 2.41× lower at baseline in the lines without GABRP | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KRT20, FGFR2, SLC34A2 |
| [[HNMT]] | B | HNMT activity raises YWHAEP7-1's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.36× lower at baseline in the lines without HNMT | 0.090 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP27A1]] | B | YWHAEP7-1 activity raises CYP27A1's level | lines that do not express YWHAEP7-1 (13) vs lines expressing it (37) | 2.94× lower at baseline in the lines without YWHAEP7-1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OCA2, ALK, SPDYE10; maybe low, not absent |
| [[CCR3]] | B | YWHAEP7-1 activity raises CCR3's level | lines that do not express YWHAEP7-1 (13) vs lines expressing it (37) | 1.76× lower at baseline in the lines without YWHAEP7-1 | 0.064 | ⚠ within organs, on part of the lines; also absent: OCA2, ALK, SPDYE10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.480). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.7, 44.3); signed map (59.5, 18.4). **Vector** length 34.1, 6.37% of its response variance represented; |z| ≥ 3 in 547 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +13.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -1.6 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -4.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.1 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -1.1 |

## What is on record

> [!warning] No registry record
> YWHAEP7-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16509: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16509); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16509, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16509]; `tensor/DDL_lfc|DDL_z.npy` [16509]; `embed/gene_vectors.npy` [16509]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16509 or target_col == 16509). Every well: [[YWHAEP7-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YWHAEP7-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
