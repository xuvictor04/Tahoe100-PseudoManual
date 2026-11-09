---
symbol: "HTR7"
type: "gene"
col: 7305
ensembl_id: "ENSG00000148680"
name: "5-hydroxytryptamine receptor 7"
location: "10q23.31"
module: 84
arm: "+"
pooled_cpm: 7.81
n_lines_expressing: 27
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 27
direction_downstream: 33
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# HTR7

*5-hydroxytryptamine receptor 7* — 10q23.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.82× (z +19.2, q 0e+00, up in 15 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM: 0.537× (z -6.3, q 2e-07, down in 14 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02454]] (+0.71, fdr 7e-06), [[MIR100HG]] (+0.68, fdr 7e-06), [[PHC2]] (+0.66, fdr 7e-06); moves opposite to [[KIF13A]] (-0.48, fdr 3e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[NPAS2]] → it (grade B ⚠); 33 go from it, the strongest it → [[SLC25A51]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.82×** | +19.2 | 0e+00 | 15/23 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.52×** | +17.3 | 0e+00 | 15/24 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +12.6 | 6e-34 | 15/24 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.62×** | +9.8 | 2e-20 | 11/23 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.33×** | +8.6 | 9e-16 | 15/23 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +7.3 | 3e-11 | 8/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +6.5 | 6e-09 | 6/25 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +6.0 | 2e-07 | 13/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +5.9 | 2e-07 | 9/24 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.69×** | +5.3 | 5e-06 | 5/24 (LOX-IMVI, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.3 | 7e-06 | 4/24 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.59×** | +4.5 | 3e-04 | 0/12 | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +3.9 | 0.004 | 1/14 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +3.4 | 0.029 | 3/24 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.060 | 1/19 (BT-474) | rises with dose | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.537×** | -6.3 | 2e-07 | 14/23 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.611×** | -5.8 | 2e-06 | 11/24 (C32, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.663×** | -5.1 | 7e-05 | 13/24 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.735×** | -4.4 | 0.001 | 12/24 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.649×** | -4.0 | 0.006 | 9/23 (C32, SK-MEL-2, …) | all doses, flat |  |
| [[LJI308 (drug)]] 0.05 µM |  | **0.675×** | -3.7 | 0.017 | 6/24 (PANC-1, C-33 A, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.775×** | -3.6 | 0.022 | 8/24 (SK-MEL-2, C32, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.776×** | -3.6 | 0.022 | 10/24 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.711×** | -3.5 | 0.035 | 4/23 (SK-MEL-2, NCI-H2030, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.714×** | -3.4 | 0.037 | 11/25 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.788×** | -3.4 | 0.040 | 12/24 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.727×** | -3.2 | 0.056 | 14/24 (SK-MEL-2, A549, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.718×** | -3.2 | 0.056 | 12/22 (NCI-H1573, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.749×** | -3.1 | 0.078 | 11/24 (C32, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 19.6 | 0 | 7 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0135× (z -15.2) |
| [[LOX-IMVI (line)]] | wt | 41.3 | 0 | 5 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0756× (z -17.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 1 | 4 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.52× (z +9.2) | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.174× (z -9.0) |
| [[HOP62 (line)]] | alt | 50.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0533× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 53.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0405× (z -21.0) |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0463× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 3.72 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.40× (z +10.5) | — |
| [[PANC-1 (line)]] | alt | 6.70 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.19× (z +12.9) | — |
| [[H4 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0594× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 4.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 5.14 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0293× (z -11.9) |
| [[NCI-H2030 (line)]] | alt | 9.51 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0784× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 7.59 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.426× (z -11.0) ⚠ position not correctable |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0856× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.778 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.881 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.677 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.679 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.755 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.685 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.912 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02454]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MIR100HG]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[PHC2]] | +0.66 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[ITGB3]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SPRY4]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[COL13A1]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RGS17]] | +0.63 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[ZNF385D]] | +0.63 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[DUSP6]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[ZNF697]] | +0.60 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[LINC02813]] | +0.60 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SH2B3]] | +0.60 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF13A]] | -0.48 | -0.43 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 8, C 19. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPAS2]] | B | NPAS2 activity raises HTR7's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.56× lower at baseline in the lines without NPAS2 | 0.026 | ⚠ within organs, on part of the lines |
| [[RPSAP52]] | B | RPSAP52 activity raises HTR7's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.73× lower at baseline in the lines without RPSAP52 | 0.035 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[NLRP1]] | B | NLRP1 activity weakens HTR7's drug response | lines that do not express NLRP1 (10) vs lines expressing it (15) | the lines without NLRP1 respond 3.43× as strongly (z diff -2.23); strongest at Homoharringtonine 5 µM: 3.64x vs 1.13x (z diff -5.4) | 0.054 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12; target measured in part of the lines; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity raises HTR7's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; shared targets |
| [[ALK]] | B | ALK activity raises HTR7's level | lines that do not express ALK (7) vs lines expressing it (43) | 3.38× lower at baseline in the lines without ALK | 0.086 | ⚠ within organs, on part of the lines; also absent: GGT7, HLTF, BBS5; maybe low, not absent |
| [[LINC02454]] | B | LINC02454 activity raises HTR7's level | lines that do not express LINC02454 (12) vs lines expressing it (38) | 2.65× lower at baseline in the lines without LINC02454 | 0.092 | ⚠ within organs, on part of the lines; also absent: PAPLN, LGALS1, SCHIP1; maybe low, not absent |
| [[UBASH3B]] | B | UBASH3B activity raises HTR7's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 2.42× lower at baseline in the lines without UBASH3B | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[NLRP1]] | B | NLRP1 activity raises HTR7's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 2.15× lower at baseline in the lines without NLRP1 | 0.096 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[FRMD4A]] | C | FRMD4A activity raises HTR7's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 3.71× lower at baseline in the lines without FRMD4A | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises HTR7's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.31× lower at baseline in the lines without ITGB3 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[INSYN2B]] | C | INSYN2B activity raises HTR7's level | lines that do not express INSYN2B (31) vs lines expressing it (19) | 4.19× lower at baseline in the lines without INSYN2B | 0.008 | ⚠ within organs, on part of the lines; also absent: MMP2, ITGA11, FGF5; co-absent with the target |
| [[IL31RA]] | C | IL31RA activity raises HTR7's level | lines that do not express IL31RA (28) vs lines expressing it (22) | 3.05× lower at baseline in the lines without IL31RA | 0.008 | ⚠ within organs, on part of the lines; also absent: EFEMP1, EYA4, CCBE1; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 21, C 12. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC25A51]] | B | HTR7 activity raises SLC25A51's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without HTR7 | 0.006 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[BLZF2P]] | B | HTR7 activity raises BLZF2P's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without HTR7 | 0.006 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[REP15]] | B | HTR7 activity raises REP15's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.34× lower at baseline in the lines without HTR7 | 0.008 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[NPAS2]] | B | HTR7 activity raises NPAS2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.68× lower at baseline in the lines without HTR7 | 0.011 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[ACTN1]] | B | HTR7 activity raises ACTN1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.59× lower at baseline in the lines without HTR7 | 0.017 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[SPRED1]] | B | HTR7 activity raises SPRED1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.23× lower at baseline in the lines without HTR7 | 0.021 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[SMOX]] | B | HTR7 activity raises SMOX's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.44× lower at baseline in the lines without HTR7 | 0.025 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[PHC2]] | B | HTR7 activity raises PHC2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without HTR7 | 0.027 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[COL13A1]] | B | HTR7 activity raises COL13A1's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 2.94× lower at baseline in the lines without HTR7 | 0.033 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[A3GALT2]] | B | HTR7 activity raises A3GALT2's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without HTR7 | 0.036 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[UBASH3B]] | B | HTR7 activity raises UBASH3B's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.85× lower at baseline in the lines without HTR7 | 0.038 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |
| [[ARSJ]] | B | HTR7 activity raises ARSJ's level | lines that do not express HTR7 (23) vs lines expressing it (27) | 1.78× lower at baseline in the lines without HTR7 | 0.039 | ⚠ within organs, on part of the lines; also absent: STK32B, CNRIP1, MAGI2 |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.643). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (48.8, 7.6); signed map (10.6, 49.9). **Vector** length 73.8, 19.9% of its response variance represented; |z| ≥ 3 in 662 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +12.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +19.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.6 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.1 | +0.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.1 | -5.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.5 | -6.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.3 | -5.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | 5-hydroxytryptamine receptor 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.31 — chr10:90,740,823-90,858,039 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 5-HT7 |
| Gene groups (HGNC) | 5-hydroxytryptamine receptors, G protein-coupled |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 9 pathways, smallest: Serotonin receptors; RHOBTB3 ATPase cycle; Amine ligand-binding receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [P34969](https://www.uniprot.org/uniprotkb/P34969) (5-hydroxytryptamine receptor 7):

> G protein-coupled receptor for 5-hydroxytryptamine (serotonin), a biogenic hormone that functions as a neurotransmitter, a hormone and a mitogen. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors. HTR7 is coupled to G(s) G alpha proteins and mediates activation of adenylate cyclase activity.

**Summary**, from NCBI Gene [3363](https://www.ncbi.nlm.nih.gov/gene/3363):

> The neurotransmitter, serotonin, is thought to play a role in various cognitive and behavioral functions. The serotonin receptor encoded by this gene belongs to the superfamily of G protein-coupled receptors and the gene is a candidate locus for involvement in autistic disorder and other neuropsychiatric disorders. Three splice variants have been identified which encode proteins that differ in the length of their carboxy terminal ends. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5302) · Entrez [3363](https://www.ncbi.nlm.nih.gov/gene/3363) · UniProt [P34969](https://www.uniprot.org/uniprotkb/P34969) · Ensembl [ENSG00000148680](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148680)

## Data

Gene col 7305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7305); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7305]; `tensor/DDL_lfc|DDL_z.npy` [7305]; `embed/gene_vectors.npy` [7305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7305 or target_col == 7305). Every well: [[HTR7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTR7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
