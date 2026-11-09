---
symbol: "MR1"
type: "gene"
col: 7680
ensembl_id: "ENSG00000153029"
name: "major histocompatibility complex, class I-related"
location: "1q25.3"
module: 23
arm: "+"
pooled_cpm: 7.44
n_lines_expressing: 45
n_dd_up: 38
n_dd_down: 13
n_dd_up_clean: 29
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MR1

*major histocompatibility complex, class I-related* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.96× (z +15.9, q 0e+00, up in 31 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.645× (z -4.5, q 0.003, down in 17 of 38 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.657× (z -4.3, q 0.004, down in 14 of 39 measured lines).
> Its strongest partners by |cos| (78 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 22 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB5]] (+0.75, fdr 3e-05), [[TTC32]] (+0.72, fdr 4e-05), [[N4BP2L1]] (+0.72, fdr 4e-05); moves opposite to [[NPHP4]] (-0.71, fdr 1e-05), [[KIAA1328]] (-0.68, fdr 6e-05), [[SMYD3]] (-0.68, fdr 3e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[FLT3LG]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7680.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.96×** | +15.9 | 0e+00 | 31/36 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.88×** | +9.2 | 8e-18 | 28/42 (RKO, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.82×** | +8.8 | 4e-16 | 21/35 (A-172, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +7.6 | 4e-12 | 25/41 (A-172, A498, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.99×** | +7.1 | 1e-10 | 25/38 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.03×** | +7.0 | 2e-10 | 20/28 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +6.1 | 1e-07 | 21/34 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.58×** | +5.7 | 6e-07 | 22/40 (NCI-H2347, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.78×** | +5.7 | 6e-07 | 21/37 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +5.6 | 2e-06 | 13/18 (C32, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.67×** | +5.3 | 6e-06 | 19/39 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-05 | 18/40 (A-172, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.1 | 2e-05 | 8/14 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +5.1 | 2e-05 | 17/41 (A498, MIA PaCa-2, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +4.9 | 3e-05 | 18/40 (A-172, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +4.9 | 3e-05 | 15/41 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.7 | 9e-05 | 16/41 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.59×** | +4.6 | 1e-04 | 15/39 (A498, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.52×** | +4.3 | 5e-04 | 15/40 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.2 | 7e-04 | 15/34 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7680.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.645×** | -4.5 | 0.003 | 17/38 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.657×** | -4.3 | 0.004 | 14/39 (H4, NCI-H460, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.681×** | -4.0 | 0.012 | 15/41 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.484×** | -3.9 | 0.012 | 13/33 (RKO, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.698×** | -3.7 | 0.022 | 9/38 (SNU-423, HT-29, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.706×** | -3.6 | 0.030 | 11/41 (MIA PaCa-2, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.724×** | -3.3 | 0.068 | 12/36 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.730×** | -3.3 | 0.073 | 11/42 (SW480, A549, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.733×** | -3.2 | 0.073 | 12/43 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.803×** | -3.2 | 0.073 | 13/40 (MIA PaCa-2, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.736×** | -3.2 | 0.073 | 9/39 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.736×** | -3.2 | 0.073 | 10/41 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.733×** | -3.1 | 0.089 | 14/31 (A-172, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7680. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 15.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.88× (z +12.5) | — |
| [[A498 (line)]] | wt | 20.9 | 3 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 5.54 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0761× (z -9.5) |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HOP62 (line)]] | alt | 3.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.55× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 3.00 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.2× (z +9.8) | — |
| [[NCI-H460 (line)]] | wt | 9.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.58× (z +12.6) | — |
| [[SNU-423 (line)]] | alt | 7.90 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[A-427 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.918 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.797 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 7.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7680), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB5]] | +0.75 | +0.71 / +0.43 | both halves | 3e-05 |  |
| [[TTC32]] | +0.72 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[N4BP2L1]] | +0.72 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[C3orf38]] | +0.71 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[BTN2A1]] | +0.71 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[AHI1-DT]] | +0.70 | +0.69 / +0.27 | both halves | 3e-04 |  |
| [[TAPBPL]] | +0.70 | +0.72 / +0.36 | both halves | 9e-05 | same gene group; STRING 909 |
| [[PATL2]] | +0.69 | +0.72 / +0.33 | both halves | 1e-04 |  |
| [[DRAM1]] | +0.69 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[PBLD]] | +0.69 | +0.70 / +0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[PNISR-AS1]] | +0.68 | +0.61 / +0.20 | both halves | 7e-04 |  |
| [[ATE1OSP]] | +0.66 | +0.65 / +0.22 | both halves | 6e-04 |  |
| [[PPP1R42]] | +0.66 | +0.64 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP4]] | -0.71 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[KIAA1328]] | -0.68 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[SMYD3]] | -0.68 | -0.54 / -0.29 | both halves | 3e-04 |  |
| [[STUB1]] | -0.66 | -0.49 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[INPP5F]] | -0.63 | -0.58 / -0.29 | both halves | 2e-04 |  |
| [[WASF3]] | -0.63 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[GNB1L]] | -0.63 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[RSU1]] | -0.63 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[WRN]] | -0.62 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[FANCE]] | -0.62 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[TBCD]] | -0.62 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[ANKRD27]] | -0.61 | -0.56 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[SPTLC2]] | -0.61 | -0.60 / -0.23 | both halves | 5e-04 |  |
| [[CEP131]] | -0.61 | -0.45 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MR1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TLR1]] | B | TLR1 activity raises MR1's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 1.89× lower at baseline in the lines without TLR1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |
| [[PSTPIP2]] | B | PSTPIP2 activity raises MR1's level | lines that do not express PSTPIP2 (20) vs lines expressing it (30) | 1.51× lower at baseline in the lines without PSTPIP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: NEDD9, CARD11, BCAT1 |
| [[HECTD2]] | B | HECTD2 activity raises MR1's level | lines that do not express HECTD2 (5) vs lines expressing it (45) | 3.45× lower at baseline in the lines without HECTD2 | 0.035 | ⚠ within organs, on part of the lines; also absent: IMPG2, PHC1, TPST1; maybe low, not absent |
| [[LY96]] | B | LY96 activity raises MR1's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.87× lower at baseline in the lines without LY96 | 0.043 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |
| [[ERAP2]] | B | ERAP2 activity raises MR1's level | lines that do not express ERAP2 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without ERAP2 | 0.047 | ⚠ within organs, on part of the lines; also absent: COL13A1, SMOX, TRIM38; maybe low, not absent |
| [[MGST2]] | B | MGST2 activity raises MR1's level | lines that do not express MGST2 (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without MGST2 | 0.062 | ⚠ within organs, on part of the lines; also absent: LGALS3BP, TUBA4A, TNK1 |
| [[TRIP6]] | B | TRIP6 activity raises MR1's level | lines that do not express TRIP6 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without TRIP6 | 0.063 | ⚠ within organs, on part of the lines; also absent: EFNB2, PLAC4 |
| [[OGFRL1]] | B | OGFRL1 activity raises MR1's level | lines that do not express OGFRL1 (10) vs lines expressing it (40) | 2.02× lower at baseline in the lines without OGFRL1 | 0.096 | ⚠ within organs, on part of the lines; also absent: AFAP1L1, HDGFL3, CYP46A1 |
| [[FLNB]] | C | FLNB activity raises MR1's level | lines that do not express FLNB (3) vs lines expressing it (47) | 1.77× lower at baseline in the lines without FLNB | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens MR1's drug response | recorded loss-of-function mutation of TP53 in 28 lines vs 15 not recorded | the TP53-altered lines respond 0.68× as strongly (z diff +0.93); strongest at Topotecan (hydrochloride) 5 µM: 1.65x vs 2.39x (z diff +2.1) | 0.907 over the table, 0.090 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLT3LG]] | B | MR1 activity raises FLT3LG's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without MR1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[PAQR4]] | B | MR1 activity lowers PAQR4's level | lines that do not express MR1 (5) vs lines expressing it (45) | 2.05× higher at baseline in the lines without MR1 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[BTN3A3]] | B | MR1 activity raises BTN3A3's level | lines that do not express MR1 (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without MR1 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[RC3H2]] | B | MR1 activity raises RC3H2's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.29× lower at baseline in the lines without MR1 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[BTN2A3P]] | B | MR1 activity raises BTN2A3P's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without MR1 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |
| [[C1RL]] | B | MR1 activity raises C1RL's level | lines that do not express MR1 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without MR1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with CTNNB1; also absent: GGT7, AGK, TCTN1 |

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (1.4, 16.3); signed map (24.2, -13.6). **Vector** length 83.7, 18.3% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +15.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +8.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.1 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.2 | +4.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.0 | +5.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | -1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.6 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.2 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.7 | -2.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class I-related |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:181,033,374-181,061,938 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HLALS |
| Gene groups (HGNC) | C1-set domain containing; Minor histocompatibility antigens |
| Matched by | ensembl_id |

**Function**, from UniProt [Q95460](https://www.uniprot.org/uniprotkb/Q95460) (Major histocompatibility complex class I-related protein 1):

> Antigen-presenting molecule specialized in displaying microbial pyrimidine-based metabolites to alpha-beta T cell receptors (TCR) on innate-type mucosal-associated invariant T (MAIT) cells. In complex with B2M preferentially presents riboflavin-derived metabolites to semi-invariant TRAV1.2 TCRs on MAIT cells, guiding immune surveillance of the microbial metabolome at mucosal epithelial barriers. Signature pyrimidine-based microbial antigens are generated via non-enzymatic condensation of …

**Summary**, from NCBI Gene [3140](https://www.ncbi.nlm.nih.gov/gene/3140):

> MAIT (mucosal-associated invariant T-cells) lymphocytes represent a small population of T-cells primarily found in the gut. The protein encoded by this gene is an antigen-presenting molecule that presents metabolites of microbial vitamin B to MAITs. This presentation may activate the MAITs to regulate the amounts of specific types of bacteria in the gut. Several transcript variants encoding different isoforms have been found for this gene, and a pseudogene of it has been detected about 36 kbp …

**Accessions** — [HGNC:4975](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4975) · Entrez [3140](https://www.ncbi.nlm.nih.gov/gene/3140) · UniProt [Q95460](https://www.uniprot.org/uniprotkb/Q95460) · Ensembl [ENSG00000153029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153029)

## Data

Gene col 7680: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7680); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7680, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7680]; `tensor/DDL_lfc|DDL_z.npy` [7680]; `embed/gene_vectors.npy` [7680]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7680 or target_col == 7680). Every well: [[MR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
