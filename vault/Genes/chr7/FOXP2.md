---
symbol: "FOXP2"
type: "gene"
col: 4894
ensembl_id: "ENSG00000128573"
name: "forkhead box P2"
location: "7q31.1"
module: 8
arm: "+"
pooled_cpm: 30.87
n_lines_expressing: 24
n_dd_up: 43
n_dd_down: 12
n_dd_up_clean: 40
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 13
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# FOXP2

*forkhead box P2* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.73× (z +17.0, q 0e+00, up in 18 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.589× (z -6.3, q 1e-07, down in 21 of 22 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Mebendazole (drug)]] 5 µM: 0.680× (z -4.4, q 9e-04, down in 9 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAAH2]] (+0.61, fdr 8e-06), [[TOX3]] (+0.60, fdr 1e-05), [[SAMD12]] (+0.59, fdr 1e-05); moves opposite to [[SERPINB6]] (-0.45, fdr 2e-05), [[LOXL2]] (-0.45, fdr 4e-05), [[FIBCD1]] (-0.44, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[SELENOP]] → it (grade B ⚠); 13 go from it, the strongest it → [[SELENOP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4894.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.73×** | +17.0 | 0e+00 | 18/22 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.49×** | +10.9 | 3e-25 | 20/22 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.37×** | +9.6 | 1e-19 | 17/22 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +9.1 | 9e-18 | 2/22 (NCI-H1573, SW480) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +8.8 | 2e-16 | 5/22 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.61×** | +6.7 | 2e-09 | 15/22 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.71×** | +6.2 | 5e-08 | 17/22 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.63×** | +5.9 | 3e-07 | 18/22 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 6e-06 | 7/22 (NCI-H1573, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +5.1 | 2e-05 | 13/22 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +5.0 | 2e-05 | 16/22 (SW480, SHP-77, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.52×** | +5.0 | 3e-05 | 14/22 (SW480, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.9 | 4e-05 | 4/23 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.49×** | +4.4 | 4e-04 | 13/22 (J82, A498, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +4.4 | 4e-04 | 12/23 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.49×** | +4.4 | 4e-04 | 16/23 (SW480, BT-474, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 10 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4894.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.589×** | -6.3 | 1e-07 | 21/22 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.597×** | -6.2 | 2e-07 | 14/22 (HT-29, LoVo, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.618×** | -5.8 | 2e-06 | 18/22 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.632×** | -5.5 | 6e-06 | 20/22 (NCI-H1792, LS 180, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.689×** | -4.5 | 9e-04 | 15/22 (NCI-H1792, SHP-77, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.680×** | -4.4 | 9e-04 | 9/22 (SHP-77, HCT15, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.715×** | -3.7 | 0.016 | 12/22 (BT-474, SW48, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.749×** | -3.5 | 0.037 | 12/22 (HEC-1-A, LOX-IMVI, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.748×** | -3.3 | 0.051 | 16/22 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.758×** | -3.3 | 0.051 | 13/22 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.687×** | -3.2 | 0.068 | 10/22 (LoVo, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.754×** | -3.1 | 0.081 | 13/22 (NCI-H1792, BT-474, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.776× | -3.0 | 0.10 | 10/22 (A498, HEC-1-A, …) | rises with dose | position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | 0.765× | -3.0 | 0.10 | 9/22 (LoVo, SW48, …) | all doses, flat |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.547× | -3.0 | 0.10 | 8/22 (LoVo, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4894. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 119 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -18.4) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 212 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.285× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 131 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -13.9) |
| [[HT-29 (line)]] | alt | 75.4 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.115× (z -13.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.260× (z -8.5) |
| [[LoVo (line)]] | wt | 113 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.193× (z -12.4) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 486 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -10.3) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -8.9) |
| [[C32 (line)]] | wt | 21.6 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 7.16× (z +12.9) | — |
| [[LOX-IMVI (line)]] | wt | 55.4 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 57.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -12.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.456× (z -9.0) |
| [[SW480 (line)]] | alt | 9.42 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 6.53× (z +8.9) | — |
| [[A498 (line)]] | wt | 28.4 | 1 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 5.53× (z +8.9) ⚠ cell-cycle shift, explains ~58% of this change | — |
| [[BT-474 (line)]] | alt | 76.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.222× (z -8.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0707× (z -9.9) ⚠ cell-cycle shift, explains ~70% of this change |
| [[J82 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 24.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 5.70× (z +11.6) | — |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 23.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0770× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW 900 (line)]] | alt | 41.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 4.52 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.49 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.74 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.79 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.00 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.14 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 48.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4894), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAAH2]] | +0.61 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[TOX3]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SAMD12]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[SYNPR-AS1]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[BCAS1]] | +0.57 | +0.33 / +0.61 | both halves | 1e-04 | same gene group |
| [[MECOM]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[LINC00992]] | +0.55 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[FUT9]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PRKG1]] | +0.55 | +0.55 / +0.61 | both halves | 1e-05 | same gene group |
| [[ANK3]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 | pathway: Adherens junctions interactions |
| [[PLCH1]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[LINC02967]] | +0.54 | +0.37 / +0.54 | both halves | 8e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB6]] | -0.45 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[LOXL2]] | -0.45 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[FIBCD1]] | -0.44 | -0.48 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SELENOP]] | B | SELENOP activity raises FOXP2's level | lines that do not express SELENOP (18) vs lines expressing it (32) | 3.45× lower at baseline in the lines without SELENOP | 0.017 | ⚠ within organs, on part of the lines; also absent: SORL1, GPR35, GOLT1A; maybe low, not absent |
| [[CCSER1]] | B | CCSER1 activity raises FOXP2's level | lines that do not express CCSER1 (20) vs lines expressing it (30) | 2.63× lower at baseline in the lines without CCSER1 | 0.061 | ⚠ within organs, on part of the lines; also absent: TSTD1, UGT8, HOOK1 |
| [[SCIN]] | B | SCIN activity raises FOXP2's level | lines that do not express SCIN (22) vs lines expressing it (28) | 3.04× lower at baseline in the lines without SCIN | 0.065 | ⚠ within organs, on part of the lines; also absent: SCEL, RASAL1, CLDN3 |
| [[PLXDC2]] | B | PLXDC2 activity raises FOXP2's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 2.33× lower at baseline in the lines without PLXDC2 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[PIP5K1B]] | C | PIP5K1B activity raises FOXP2's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 3.19× lower at baseline in the lines without PIP5K1B | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises FOXP2's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 2.58× lower at baseline in the lines without PTPRR | 0.038 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[LINC00992]] | C | LINC00992 activity raises FOXP2's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without LINC00992 | 0.053 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5; co-absent with the target |
| [[FAAH2]] | C | FAAH2 activity raises FOXP2's level | lines that do not express FAAH2 (26) vs lines expressing it (24) | 2.62× lower at baseline in the lines without FAAH2 | 0.059 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, TNNT2, ST14; maybe low, not absent; co-absent with the target |
| [[SAMD12-AS1]] | C | SAMD12-AS1 activity raises FOXP2's level | lines that do not express SAMD12-AS1 (23) vs lines expressing it (27) | 3.17× lower at baseline in the lines without SAMD12-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ENSG00000263325, TMPRSS4; co-absent with the target |
| [[CXXC4]] | C | CXXC4 activity raises FOXP2's level | lines that do not express CXXC4 (25) vs lines expressing it (25) | 2.74× lower at baseline in the lines without CXXC4 | 0.073 | ⚠ within organs, on part of the lines; also absent: VIPR2, DOK6, CCSER1; co-absent with the target |
| [[LINC02999]] | C | LINC02999 activity raises FOXP2's level | lines that do not express LINC02999 (43) vs lines expressing it (7) | 4.71× lower at baseline in the lines without LINC02999 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, GCG, SFTPA2; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SELENOP]] | B | FOXP2 activity raises SELENOP's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.53× lower at baseline in the lines without FOXP2 | 0.011 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[CCSER1]] | B | FOXP2 activity raises CCSER1's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 3.04× lower at baseline in the lines without FOXP2 | 0.033 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[SEMA3E]] | B | FOXP2 activity raises SEMA3E's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without FOXP2 | 0.045 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[SATB1]] | B | FOXP2 activity raises SATB1's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.94× lower at baseline in the lines without FOXP2 | 0.070 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[PBX1]] | B | FOXP2 activity raises PBX1's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.87× lower at baseline in the lines without FOXP2 | 0.076 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[PLXDC2]] | B | FOXP2 activity raises PLXDC2's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 1.43× lower at baseline in the lines without FOXP2 | 0.086 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| cells under [[Menadione (drug)]] 0.5 µM | B | FOXP2 activity raises the cells' numbers under Menadione 0.5 µM (protects the cells) | lines that do not express FOXP2 (26) vs lines expressing it (22) | the lines without FOXP2: 0.93× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6 |
| [[ESRRG]] | C | FOXP2 activity raises ESRRG's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without FOXP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6; co-absent with the target |
| [[FAAH2]] | C | FOXP2 activity raises FAAH2's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 2.93× lower at baseline in the lines without FOXP2 | 0.016 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6; co-absent with the target |
| [[LINC01456]] | C | FOXP2 activity raises LINC01456's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 2.09× lower at baseline in the lines without FOXP2 | 0.050 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6; co-absent with the target |
| [[ANK3]] | C | FOXP2 activity raises ANK3's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without FOXP2 | 0.051 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6; co-absent with the target |
| [[CLIC5]] | C | FOXP2 activity raises CLIC5's level | lines that do not express FOXP2 (26) vs lines expressing it (24) | 2.34× lower at baseline in the lines without FOXP2 | 0.081 | ⚠ within organs, on part of the lines; also absent: BMP4, SPON1, ITGB6; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.3, 50.9); signed map (58.0, 2.3). **Vector** length 77.3, 23.3% of its response variance represented; |z| ≥ 3 in 750 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +17.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.4 | +1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | +4.1 | -1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -0.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +5.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -6.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.5 | +5.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box P2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:114,086,327-114,693,772 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAGH44; previously TNRC10, SPCH1 |
| Gene groups (HGNC) | Forkhead boxes; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: Positive Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [O15409](https://www.uniprot.org/uniprotkb/O15409) (Forkhead box protein P2):

> Transcriptional repressor that may play a role in the specification and differentiation of lung epithelium. May also play a role in developing neural, gastrointestinal and cardiovascular tissues. Can act with CTBP1 to synergistically repress transcription but CTPBP1 is not essential. Plays a role in synapse formation by regulating SRPX2 levels. Involved in neural mechanisms mediating the development of speech and language.

**Summary**, from NCBI Gene [93986](https://www.ncbi.nlm.nih.gov/gene/93986):

> This gene encodes a member of the forkhead/winged-helix (FOX) family of transcription factors. It is expressed in fetal and adult brain as well as in several other organs such as the lung and gut. The protein product contains a FOX DNA-binding domain and a large polyglutamine tract and is an evolutionarily conserved transcription factor, which may bind directly to approximately 300 to 400 gene promoters in the human genome to regulate the expression of a variety of genes. This gene is required …

**Accessions** — [HGNC:13875](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13875) · Entrez [93986](https://www.ncbi.nlm.nih.gov/gene/93986) · UniProt [O15409](https://www.uniprot.org/uniprotkb/O15409) · Ensembl [ENSG00000128573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128573)

## Data

Gene col 4894: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4894); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4894, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4894]; `tensor/DDL_lfc|DDL_z.npy` [4894]; `embed/gene_vectors.npy` [4894]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4894 or target_col == 4894). Every well: [[FOXP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
