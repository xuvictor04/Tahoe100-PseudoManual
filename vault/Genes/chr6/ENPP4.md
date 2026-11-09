---
symbol: "ENPP4"
type: "gene"
col: 11
ensembl_id: "ENSG00000001561"
name: "ectonucleotide pyrophosphatase/phosphodiesterase 4"
location: "6p21.1"
module: 27
arm: "+"
pooled_cpm: 13.82
n_lines_expressing: 33
n_dd_up: 12
n_dd_down: 26
n_dd_up_clean: 9
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 10
direction_downstream: 17
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# ENPP4

*ectonucleotide pyrophosphatase/phosphodiesterase 4* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.40× (z +7.9, q 2e-12, up in 19 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.493× (z -16.4, q 0e+00, down in 26 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf115]] (+0.64, fdr 1e-05), [[COMMD8]] (+0.63, fdr 3e-05), [[ENPP5]] (+0.62, fdr 2e-05, ⚠ same locus), [[GCOM1]] (+0.61, fdr 3e-05); moves opposite to [[FAM156A]] (-0.54, fdr 3e-05), [[HDAC7]] (-0.54, fdr 4e-05), [[C1S]] (-0.53, fdr 3e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 17 go from it, the strongest it → [[SYNJ2BP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +7.9 | 2e-12 | 19/31 (J82, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +6.7 | 7e-09 | 21/31 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.43×** | +5.9 | 6e-07 | 17/30 (LS 180, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 1e-05 | 15/30 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.8 | 2e-04 | 8/17 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.28×** | +3.8 | 0.016 | 9/20 (NCI-H2030, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.20×** | +3.6 | 0.026 | 6/31 (SW480, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.51×** | +3.6 | 0.026 | 7/29 (HEC-1-A, SW48, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.060 | 7/31 (SW480, LoVo, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.075 | 6/31 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +3.2 | 0.075 | 5/31 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.091 | 8/29 (LoVo, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.493×** | -16.4 | 0e+00 | 26/30 (RKO, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.516×** | -15.3 | 0e+00 | 24/30 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.518×** | -10.8 | 1e-24 | 20/30 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.537×** | -10.2 | 4e-22 | 24/31 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.586×** | -8.7 | 3e-16 | 19/30 (SNU-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.620×** | -7.8 | 5e-13 | 22/31 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.627×** | -7.6 | 2e-12 | 20/31 (SNU-1, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.619×** | -7.4 | 9e-12 | 21/29 (SW 900, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.453×** | -6.8 | 8e-10 | 19/30 (RKO, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -6.6 | 3e-09 | 18/30 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -6.5 | 4e-09 | 22/30 (A-427, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.667×** | -6.4 | 9e-09 | 21/30 (CFPAC-1, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.682×** | -6.3 | 2e-08 | 20/31 (NCI-H2347, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -5.5 | 1e-06 | 17/31 (CFPAC-1, NCI-H2347, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -5.5 | 2e-06 | 20/31 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.731×** | -5.1 | 1e-05 | 17/30 (SW480, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 14.7 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -12.8) |
| [[LoVo (line)]] | wt | 21.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -11.5) |
| [[LS 180 (line)]] | wt | 28.8 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.147× (z -9.6) |
| [[PANC-1 (line)]] | alt | 7.55 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.5) |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -12.1) |
| [[SW480 (line)]] | alt | 20.0 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -14.0) |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.7) |
| [[KATO III (line)]] | alt | 10.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.279× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.0) |
| [[NCI-H23 (line)]] | alt | 9.80 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.8) |
| [[RKO (line)]] | wt | 19.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -17.5) |
| [[SW1417 (line)]] | alt | 30.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -13.2) |
| [[A-427 (line)]] | wt | 27.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -15.5) |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 28.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.0) |
| [[J82 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.118× (z -9.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -11.2) |
| [[SNU-423 (line)]] | alt | 5.38 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0677× (z -8.9) |
| [[SW 900 (line)]] | alt | 19.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0556× (z -9.0) |
| [[SW48 (line)]] | wt | 15.0 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0876× (z -9.8) |
| [[A-172 (line)]] | wt | 0.970 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.947 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.10 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.36 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 34.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf115]] | +0.64 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[COMMD8]] | +0.63 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[ENPP5]] | +0.62 | +0.47 / +0.67 | both halves | 2e-05 | same gene group; ⚠ same locus (12.5 kb: neighbours can correlate without regulation) |
| [[GCOM1]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[PRSS16]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[PPP1CC]] | +0.58 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[GDE1]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[MPP7]] | +0.57 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[AMOT]] | +0.56 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[STEAP2]] | +0.56 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[SRI]] | +0.55 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[SCOC]] | +0.55 | +0.38 / +0.56 | both halves | 6e-05 |  |
| [[MGAT4A]] | +0.54 | +0.51 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM156A]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[HDAC7]] | -0.54 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[C1S]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[MEF2B]] | -0.53 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[SPG7]] | -0.52 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[ANKMY1]] | -0.51 | -0.36 / -0.53 | both halves | 1e-04 |  |
| [[UBAP1L]] | -0.51 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[IPO9-AS1]] | -0.50 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[C2orf92]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[PEX6]] | -0.50 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[CDR2]] | -0.50 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[WDR81]] | -0.50 | -0.26 / -0.49 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers ENPP4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.0% of all compounds | 0.029 | ⚠ off-target possible; 3 compounds |
| [[MPP7]] | B | MPP7 activity raises ENPP4's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without MPP7 | 0.048 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity raises ENPP4's level | compounds that target TOP1: 3 of 3 lower it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAP2K2]] | B | MAP2K2 activity lowers ENPP4's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |
| [[SAMD12]] | C | SAMD12 activity raises ENPP4's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 4.41× lower at baseline in the lines without SAMD12 | 0.002 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325; co-absent with the target |
| [[SMPDL3B]] | C | SMPDL3B activity raises ENPP4's level | lines that do not express SMPDL3B (23) vs lines expressing it (27) | 3.89× lower at baseline in the lines without SMPDL3B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HOOK1, BSPRY, SPINT1-AS1; co-absent with the target |
| [[ENPP5]] | C | ENPP5 activity raises ENPP4's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 3.58× lower at baseline in the lines without ENPP5 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004; co-absent with the target |
| [[PRR36]] | C | PRR36 activity raises ENPP4's level | lines that do not express PRR36 (19) vs lines expressing it (31) | 3.24× lower at baseline in the lines without PRR36 | 0.044 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN; co-absent with the target |
| [[BSPRY]] | C | BSPRY activity raises ENPP4's level | lines that do not express BSPRY (29) vs lines expressing it (21) | 2.92× lower at baseline in the lines without BSPRY | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25; co-absent with the target |
| [[ICA1]] | C | ICA1 activity raises ENPP4's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 3.21× lower at baseline in the lines without ICA1 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 12, C 5. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNJ2BP]] | B | ENPP4 activity raises SYNJ2BP's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.61× lower at baseline in the lines without ENPP4 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[GTPBP8]] | B | ENPP4 activity raises GTPBP8's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without ENPP4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[RAB3IP]] | B | ENPP4 activity raises RAB3IP's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 2.91× lower at baseline in the lines without ENPP4 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[MPP7]] | B | ENPP4 activity raises MPP7's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 2.95× lower at baseline in the lines without ENPP4 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[UGT8]] | B | ENPP4 activity raises UGT8's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 3.28× lower at baseline in the lines without ENPP4 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[DNAJC19]] | B | ENPP4 activity raises DNAJC19's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.30× lower at baseline in the lines without ENPP4 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[DENND11]] | B | ENPP4 activity raises DENND11's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.67× lower at baseline in the lines without ENPP4 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[FIG4]] | B | ENPP4 activity raises FIG4's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.36× lower at baseline in the lines without ENPP4 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[SC5D]] | B | ENPP4 activity raises SC5D's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.80× lower at baseline in the lines without ENPP4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[ILDR1]] | B | ENPP4 activity raises ILDR1's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without ENPP4 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[FYCO1]] | B | ENPP4 activity raises FYCO1's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.47× lower at baseline in the lines without ENPP4 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |
| [[RADX]] | B | ENPP4 activity raises RADX's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.46× lower at baseline in the lines without ENPP4 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.279). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.1, 36.4); signed map (-3.4, 17.5). **Vector** length 69.1, 15.0% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.8 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.8 | +5.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +3.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +3.2 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.1 | +1.1 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.1 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.4 | -16.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.9 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -7.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -6.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.4 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleotide pyrophosphatase/phosphodiesterase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:46,129,989-46,146,688 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NPP4, KIAA0879, AP3Aase |
| Gene groups (HGNC) | Ectonucleotide pyrophosphatase/phosphodiesterase family |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6X5](https://www.uniprot.org/uniprotkb/Q9Y6X5) (Bis(5'-adenosyl)-triphosphatase ENPP4):

> Hydrolyzes extracellular Ap3A into AMP and ADP, and Ap4A into AMP and ATP. Ap3A and Ap4A are diadenosine polyphosphates thought to induce proliferation of vascular smooth muscle cells. Acts as a procoagulant, mediating platelet aggregation at the site of nascent thrombus via release of ADP from Ap3A and activation of ADP receptors.

**Summary**, from NCBI Gene [22875](https://www.ncbi.nlm.nih.gov/gene/22875):

> Enables bis(5'-adenosyl)-triphosphatase activity. Involved in positive regulation of blood coagulation and purine ribonucleoside catabolic process. Located in extracellular exosome and membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3359) · Entrez [22875](https://www.ncbi.nlm.nih.gov/gene/22875) · UniProt [Q9Y6X5](https://www.uniprot.org/uniprotkb/Q9Y6X5) · Ensembl [ENSG00000001561](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000001561)

## Data

Gene col 11: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11]; `tensor/DDL_lfc|DDL_z.npy` [11]; `embed/gene_vectors.npy` [11]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11 or target_col == 11). Every well: [[ENPP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENPP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
