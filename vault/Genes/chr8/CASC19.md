---
symbol: "CASC19"
type: "gene"
col: 14858
ensembl_id: "ENSG00000254166"
name: "cancer susceptibility 19"
location: "8q24.21"
module: 1
arm: "+"
pooled_cpm: 78.05
n_lines_expressing: 22
n_dd_up: 19
n_dd_down: 36
n_dd_up_clean: 12
n_dd_down_clean: 32
in_vector_space: true
direction_upstream: 6
direction_downstream: 22
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# CASC19

*cancer susceptibility 19* — 8q24.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.46× (z +11.3, q 8e-27, up in 8 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +8.5, q 3e-15, up in 2 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.339× (z -14.7, q 0e+00, down in 20 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CASC8]] (+0.72, fdr 7e-06), [[ZNF121]] (+0.70, fdr 7e-06), [[PALD1]] (+0.68, fdr 7e-06); moves opposite to [[VPS37D]] (-0.55, fdr 2e-05), [[PRKAB2]] (-0.54, fdr 1e-05), [[USP30]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[SLCO1B3]] → it (grade C ⚠); 22 go from it, the strongest it → [[BCL2L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.46×** | +11.3 | 8e-27 | 8/19 (C-33 A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.19×** | +10.6 | 7e-24 | 4/20 (NCI-H2030, Panc 03.27, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +8.5 | 3e-15 | 2/20 (Panc 03.27, CFPAC-1) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.74×** | +7.2 | 7e-11 | 4/18 (LS 180, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.67×** | +7.0 | 4e-10 | 10/20 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.64×** | +6.7 | 2e-09 | 12/20 (KATO III, A549, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +4.9 | 7e-05 | 10/20 (CFPAC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.8 | 9e-05 | 4/20 (LoVo, LS 180, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 1e-04 | 10/20 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 8e-04 | 11/20 (LoVo, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.1 | 0.002 | 3/13 (A-427, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.018 | 0/20 | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +3.4 | 0.034 | 13/20 (KATO III, HepG2/C3A, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.051 | 12/20 (LS 180, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.063 | 5/20 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +3.1 | 0.071 | 0/20 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.071 | 5/20 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.071 | 5/20 (KATO III, AsPC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 5 with an alert ⚠; shown: the 15 strongest. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14858.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.339×** | -14.7 | 0e+00 | 20/20 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.393×** | -12.7 | 3e-34 | 20/20 (RKO, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.476×** | -10.1 | 2e-21 | 20/20 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.541×** | -7.7 | 2e-12 | 17/20 (COLO 205, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.546×** | -7.6 | 3e-12 | 18/21 (COLO 205, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.641×** | -7.4 | 1e-11 | 18/20 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.585×** | -7.3 | 3e-11 | 17/20 (RKO, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.697×** | -6.9 | 5e-10 | 14/20 (COLO 205, MIA PaCa-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.653×** | -6.4 | 1e-08 | 18/20 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.418×** | -6.2 | 4e-08 | 18/20 (HT-29, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.733×** | -6.0 | 1e-07 | 16/20 (KATO III, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.647×** | -5.9 | 2e-07 | 20/20 (KATO III, HT-29, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.645×** | -5.7 | 5e-07 | 17/20 (HepG2/C3A, COLO 205, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.664×** | -5.6 | 1e-06 | 19/21 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.659×** | -5.4 | 2e-06 | 18/20 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 121 | 2 (1 ⚠) | 20 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 4.73× (z +9.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.68× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.0594× (z -17.1) |
| [[MIA PaCa-2 (line)]] | alt | 411 | 0 | 19 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0302× (z -24.4) |
| [[COLO 205 (line)]] | alt | 180 | 1 | 14 | [[Homoharringtonine (drug)]] 0.5 µM 5.10× (z +8.9) | [[Trametinib (drug)]] 5 µM 0.0389× (z -18.3) |
| [[HEC-1-A (line)]] | alt | 79.0 | 0 | 13 | — | [[Panobinostat (drug)]] 0.5 µM 0.0868× (z -15.6) |
| [[Hs 766T (line)]] | wt | 155 | 0 | 13 | — | [[Panobinostat (drug)]] 0.5 µM 0.0662× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 387 | 0 | 12 | — | [[Trametinib (drug)]] 5 µM 0.0919× (z -16.8) |
| [[HT-29 (line)]] | alt | 300 | 0 | 12 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0575× (z -14.5) |
| [[RKO (line)]] | wt | 765 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0299× (z -30.4) |
| [[SW48 (line)]] | wt | 430 | 0 | 11 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0308× (z -26.9) |
| [[LoVo (line)]] | wt | 108 | 3 (2 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.49× (z +13.6) | [[Panobinostat (drug)]] 5 µM 0.0639× (z -21.9) |
| [[AsPC-1 (line)]] | alt | 129 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -12.9) |
| [[C-33 A (line)]] | alt | 85.1 | 0 | 6 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0712× (z -13.2) ⚠ cell-cycle shift, explains ~73% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.156× (z -9.7) |
| [[LS 180 (line)]] | wt | 55.4 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0867× (z -17.9) |
| [[SW1417 (line)]] | alt | 442 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.0622× (z -22.2) |
| [[Panc 03.27 (line)]] | alt | 40.6 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.0945× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 48.4 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 11.6× (z +12.9) | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -9.7) |
| [[HCT15 (line)]] | alt | 78.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -13.6) |
| [[A-427 (line)]] | wt | 120 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0675× (z -19.8) |
| [[A549 (line)]] | wt | 30.6 | 0 | 2 | — | [[Trametinib (drug)]] 5 µM 0.172× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.5) |
| [[A-172 (line)]] | wt | 6.58 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.08 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 7.84 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.52 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.91 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.50 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.03 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.49 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.02 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.51 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.48 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC8]] | +0.72 | +0.76 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZNF121]] | +0.70 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[PALD1]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ACSL5]] | +0.66 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[WDR4]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[BCL2L1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[SH3D19]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[NOP2]] | +0.62 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | +0.62 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[EPHA2]] | +0.62 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[KRT18]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS37D]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[PRKAB2]] | -0.54 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[USP30]] | -0.54 | -0.46 / -0.53 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO1B3]] | C | SLCO1B3 activity raises CASC19's level | lines that do not express SLCO1B3 (28) vs lines expressing it (22) | 4.77× lower at baseline in the lines without SLCO1B3 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000257062, SLCO1B3-SLCO1B7, SLCO1B1; co-absent with the target |
| [[CASC8]] | C | CASC8 activity raises CASC19's level | lines that do not express CASC8 (20) vs lines expressing it (30) | 6.05× lower at baseline in the lines without CASC8 | 0.006 | ⚠ within organs, on part of the lines; also absent: NOS3, CASC19, COBL; maybe low, not absent; co-absent with the target |
| [[FERMT1]] | C | FERMT1 activity raises CASC19's level | lines that do not express FERMT1 (22) vs lines expressing it (28) | 5.80× lower at baseline in the lines without FERMT1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FOXQ1, LINC01564, SFN; co-absent with the target |
| [[LINC00659]] | C | LINC00659 activity raises CASC19's level | lines that do not express LINC00659 (26) vs lines expressing it (24) | 4.49× lower at baseline in the lines without LINC00659 | 0.066 | ⚠ within organs, on part of the lines; also absent: KLK6, TRIM15, ENSG00000225680; co-absent with the target |
| [[ITGB4]] | C | ITGB4 activity raises CASC19's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 5.62× lower at baseline in the lines without ITGB4 | 0.067 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3; co-absent with the target |
| [[COL17A1]] | C | COL17A1 activity raises CASC19's level | lines that do not express COL17A1 (34) vs lines expressing it (16) | 6.11× lower at baseline in the lines without COL17A1 | 0.077 | ⚠ within organs, on part of the lines; also absent: SERPINB5, GJB3, FGFBP1; co-absent with the target |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 10, C 12. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL2L1]] | B | CASC19 activity raises BCL2L1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 3.12× lower at baseline in the lines without CASC19 | 0.007 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[EPHA2]] | B | CASC19 activity raises EPHA2's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 3.42× lower at baseline in the lines without CASC19 | 0.030 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[EHBP1]] | B | CASC19 activity raises EHBP1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without CASC19 | 0.032 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[NOSTRIN]] | B | CASC19 activity raises NOSTRIN's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 2.48× lower at baseline in the lines without CASC19 | 0.048 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[SLC20A2]] | B | CASC19 activity raises SLC20A2's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.60× lower at baseline in the lines without CASC19 | 0.060 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[ITGA6]] | B | CASC19 activity raises ITGA6's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without CASC19 | 0.064 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[BCL2L1-AS1]] | B | CASC19 activity raises BCL2L1-AS1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.35× lower at baseline in the lines without CASC19 | 0.077 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[GALNT14]] | B | CASC19 activity raises GALNT14's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.76× lower at baseline in the lines without CASC19 | 0.083 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[DLC1]] | B | CASC19 activity raises DLC1's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 1.69× lower at baseline in the lines without CASC19 | 0.083 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[SH3D19]] | B | CASC19 activity raises SH3D19's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 2.12× lower at baseline in the lines without CASC19 | 0.089 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4 |
| [[SLCO1B3]] | C | CASC19 activity raises SLCO1B3's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 6.09× lower at baseline in the lines without CASC19 | 0.001 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4; co-absent with the target |
| [[CASC8]] | C | CASC19 activity raises CASC8's level | lines that do not express CASC19 (28) vs lines expressing it (22) | 3.21× lower at baseline in the lines without CASC19 | 0.003 | ⚠ within organs, on part of the lines; also absent: KLK10, KLK6, TNS4; co-absent with the target |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (13.0, 46.4); signed map (8.3, 36.8). **Vector** length 110, 33.9% of its response variance represented; |z| ≥ 3 in 1,012 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +5.9 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.7 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.8 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +4.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +1.7 |
| fall | [[Trametinib (drug)]] 5 µM |  | -4.8 | -7.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.4 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -5.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -7.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.6 | -6.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | cancer susceptibility 19 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q24.21 — chr8:127,072,694-127,227,541 (-) |
| Ensembl biotype | lncRNA |
| Also known as | CARLo-6; previously LINC01245 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:49476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49476) · Entrez [103021165](https://www.ncbi.nlm.nih.gov/gene/103021165) · Ensembl [ENSG00000254166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254166)

## Data

Gene col 14858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14858); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14858]; `tensor/DDL_lfc|DDL_z.npy` [14858]; `embed/gene_vectors.npy` [14858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14858 or target_col == 14858). Every well: [[CASC19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASC19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
