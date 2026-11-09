---
symbol: "EPHA10"
type: "gene"
col: 11392
ensembl_id: "ENSG00000183317"
name: "EPH receptor A10"
location: "1p34.3"
module: 128
arm: "+"
pooled_cpm: 2.93
n_lines_expressing: 31
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 10
direction_downstream: 18
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# EPHA10

*EPH receptor A10* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +8.4, q 3e-14, up in 16 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.599× (z -4.7, q 0.002, down in 14 of 29 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 0.5 µM: 0.700× (z -3.2, q 0.096, down in 8 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H2030 0.104×, SW480 0.131×, NCI-H23 0.0959×, LoVo 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.0647×, NCI-H2030 0.106×, PANC-1 0.0790×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0921×; ⚠ toxic; cell-cycle shift, explains ~84% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SHP-77 0.0649×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF385C]] (+0.62, fdr 1e-05), [[MAP4K5]] (+0.55, fdr 3e-05), [[MYT1]] (+0.55, fdr 1e-05); moves opposite to [[CFAP44]] (-0.49, fdr 9e-05), [[KIAA0753]] (-0.44, fdr 3e-04), [[MYCBP]] (-0.44, fdr 6e-05).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 18 go from it, the strongest it → [[NOXA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11392.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +8.4 | 3e-14 | 16/26 (PANC-1, BT-474, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +7.0 | 5e-10 | 1/4 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +6.1 | 2e-07 | 11/23 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +5.7 | 2e-06 | 1/6 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +5.2 | 2e-05 | 1/9 (LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +5.0 | 6e-05 | 11/28 (LoVo, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +4.8 | 1e-04 | 9/28 (LoVo, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.002 | 5/24 (LS 180, BT-474, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.004 | 4/22 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.51×** | +3.8 | 0.008 | 3/19 (PANC-1, LS 180, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.48×** | +3.6 | 0.014 | 6/23 (LS 180, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.019 | 7/24 (PANC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.037 | 4/24 (LoVo, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.43×** | +3.3 | 0.037 | 7/28 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.3 | 0.037 | 2/22 (LoVo, C-33 A) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.41×** | +3.2 | 0.051 | 4/23 (LS 180, NCI-H2030, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11392.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 4 lines (NCI-H2030 0.104×, SW480 0.131×, NCI-H23 0.0959×, LoVo 0.137×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (MIA PaCa-2 0.0647×, NCI-H2030 0.106×, PANC-1 0.0790×; ⚠ toxic; cell-cycle shift, would explain all of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0921×; ⚠ toxic; cell-cycle shift, explains ~84% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (SHP-77 0.0649×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.599×** | -4.7 | 0.002 | 14/29 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.637×** | -4.1 | 0.011 | 9/23 (NCI-H1573, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.675×** | -3.4 | 0.096 | 13/21 (MIA PaCa-2, A-427, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.768×** | -3.4 | 0.096 | 12/22 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.690×** | -3.2 | 0.096 | 12/21 (A-427, C-33 A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.700×** | -3.2 | 0.096 | 8/25 (SW48, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.700×** | -3.2 | 0.096 | 12/24 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Allopurinol (drug)]] 0.05 µM |  | 0.711× | -3.1 | 0.13 | 4/28 (NCI-H661, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11392. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 8.09 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 13.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0921× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~84% of this change |
| [[NCI-H2030 (line)]] | alt | 6.14 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 4.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.137× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 6.46 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0959× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 2.08 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0790× (z -9.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 4.96 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0649× (z -8.7) |
| [[SW480 (line)]] | alt | 5.25 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.668 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.335 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.746 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.323 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.324 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.400 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.797 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.760 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.523 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11392), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF385C]] | +0.62 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[MAP4K5]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[MYT1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[BCAS4]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RASGEF1A]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[ENTREP1]] | +0.52 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[RETREG1]] | +0.52 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[AQP11]] | +0.51 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ACBD4]] | +0.51 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[COPG2IT1]] | +0.51 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[CYS1]] | +0.50 | +0.37 / +0.46 | both halves | 8e-05 |  |
| [[SEC14L4]] | +0.50 | +0.35 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP44]] | -0.49 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[KIAA0753]] | -0.44 | -0.27 / -0.49 | both halves | 3e-04 |  |
| [[MYCBP]] | -0.44 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[LYPLA2]] | -0.43 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ZBTB11]] | -0.43 | -0.19 / -0.44 | ⚠ not reproduced | 8e-04 |  |
| [[C2CD3]] | -0.43 | -0.26 / -0.33 | both halves | 4e-04 |  |
| [[FBXW7]] | -0.42 | -0.36 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 8, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EPHA10's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MYT1]] | B | MYT1 activity raises EPHA10's level | lines that do not express MYT1 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without MYT1 | 0.043 | ⚠ within organs, on part of the lines; also absent: CHGB, ENSG00000249776, PAX2 |
| [[NFASC]] | B | NFASC activity raises EPHA10's level | lines that do not express NFASC (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without NFASC | 0.056 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A |
| [[ETNK2]] | B | ETNK2 activity raises EPHA10's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without ETNK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[FXYD6]] | B | FXYD6 activity raises EPHA10's level | lines that do not express FXYD6 (25) vs lines expressing it (25) | 1.66× lower at baseline in the lines without FXYD6 | 0.084 | ⚠ within organs, on part of the lines; also absent: MARK1, KIF1A, MAP6 |
| [[ENTREP1]] | B | ENTREP1 activity raises EPHA10's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.53× lower at baseline in the lines without ENTREP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[PRSS16]] | B | PRSS16 activity raises EPHA10's level | lines that do not express PRSS16 (13) vs lines expressing it (37) | 2.30× lower at baseline in the lines without PRSS16 | 0.088 | ⚠ within organs, on part of the lines; also absent: STXBP2, MAP3K21, LINC00857 |
| [[NOXA1]] | B | NOXA1 activity raises EPHA10's level | lines that do not express NOXA1 (8) vs lines expressing it (42) | 2.45× lower at baseline in the lines without NOXA1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CCDC88C, NRARP, MMP15; maybe low, not absent |
| [[CAMSAP3]] | C | CAMSAP3 activity raises EPHA10's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without CAMSAP3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent; co-absent with the target |
| [[RASGEF1A]] | C | RASGEF1A activity raises EPHA10's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.80× lower at baseline in the lines without RASGEF1A | 0.013 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 15, C 3. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOXA1]] | B | EPHA10 activity raises NOXA1's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.45× lower at baseline in the lines without EPHA10 | 0.005 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[PRSS16]] | B | EPHA10 activity raises PRSS16's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.18× lower at baseline in the lines without EPHA10 | 0.022 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[HID1]] | B | EPHA10 activity raises HID1's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.99× lower at baseline in the lines without EPHA10 | 0.030 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[C1orf115]] | B | EPHA10 activity raises C1orf115's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.88× lower at baseline in the lines without EPHA10 | 0.039 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[BCAS4]] | B | EPHA10 activity strengthens BCAS4's drug response | lines that do not express EPHA10 (18) vs lines expressing it (28) | the lines without EPHA10 respond 0.58× as strongly (z diff +1.21); rises at some drug-doses, falls at others (41% from rises): Ouabain (Octahydrate) 0.5 µM: 0.94x vs 0.54x (z diff +2.8); Ouabain (Octahydrate) 5 µM: 0.87x vs 0.50x (z diff +2.8); Belinostat 5 µM: 1.41x vs 1.80x (z diff +1.2) | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[TESMIN]] | B | EPHA10 activity raises TESMIN's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without EPHA10 | 0.060 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[SLC6A17]] | B | EPHA10 activity raises SLC6A17's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.56× lower at baseline in the lines without EPHA10 | 0.062 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[MYT1]] | B | EPHA10 activity raises MYT1's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.06× lower at baseline in the lines without EPHA10 | 0.066 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[ZNF385C]] | B | EPHA10 activity raises ZNF385C's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without EPHA10 | 0.068 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[CCDC88B]] | B | EPHA10 activity raises CCDC88B's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.74× lower at baseline in the lines without EPHA10 | 0.070 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[SHC2]] | B | EPHA10 activity raises SHC2's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.93× lower at baseline in the lines without EPHA10 | 0.076 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |
| [[LINC01012]] | B | EPHA10 activity raises LINC01012's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 2.31× lower at baseline in the lines without EPHA10 | 0.086 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.6, 39.3); signed map (22.8, 24.6). **Vector** length 47.8, 9.13% of its response variance represented; |z| ≥ 3 in 582 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -1.9 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -1.9 | -3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.6 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.6 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -1.9 |
|  | [[Busulfan (drug)]] 5 µM |  | -0.9 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | EPH receptor A10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:37,713,880-37,765,133 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ16103, FLJ33655 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; EPH receptors |
| Reactome | 5 pathways, smallest: EPHA-mediated growth cone collapse; EPH-ephrin mediated repulsion of cells; EPH-Ephrin signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5JZY3](https://www.uniprot.org/uniprotkb/Q5JZY3) (Ephrin type-A receptor 10):

> Receptor for members of the ephrin-A family. Binds to EFNA3, EFNA4 and EFNA5.

**Summary**, from NCBI Gene [284656](https://www.ncbi.nlm.nih.gov/gene/284656):

> Ephrin receptors, the largest subfamily of receptor tyrosine kinases (RTKs), and their ephrin ligands are important mediators of cell-cell communication regulating cell attachment, shape, and mobility in neuronal and epithelial cells (Aasheim et al., 2005 [PubMed 15777695]). See MIM 179610 for additional background on Eph receptors and ephrins.[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19987](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19987) · Entrez [284656](https://www.ncbi.nlm.nih.gov/gene/284656) · UniProt [Q5JZY3](https://www.uniprot.org/uniprotkb/Q5JZY3) · Ensembl [ENSG00000183317](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183317)

## Data

Gene col 11392: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11392); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11392, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11392]; `tensor/DDL_lfc|DDL_z.npy` [11392]; `embed/gene_vectors.npy` [11392]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11392 or target_col == 11392). Every well: [[EPHA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EPHA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
