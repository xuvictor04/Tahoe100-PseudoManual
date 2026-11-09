---
symbol: "RUNX2"
type: "gene"
col: 4577
ensembl_id: "ENSG00000124813"
name: "RUNX family transcription factor 2"
location: "6p21.1"
module: 167
arm: "+"
pooled_cpm: 85.36
n_lines_expressing: 42
n_dd_up: 0
n_dd_down: 30
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# RUNX2

*RUNX family transcription factor 2* — 6p21.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.314× (z -15.8, q 0e+00, down in 37 of 40 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02015]] (+0.51, fdr 4e-05), [[SPTSSB]] (+0.48, fdr 1e-04), [[PLD1]] (+0.47, fdr 5e-05); moves opposite to [[CTNND2]] (-0.40, fdr 9e-05), [[TRMT2B]] (-0.37, fdr 4e-04), [[PRLR]] (-0.35, fdr 8e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[BICC1]] → it (grade B ⚠); 2 go from it, the strongest it → [[RADIL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4577.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bimiralisib (drug)]] 5 µM |  | 1.56× | +3.2 | 0.48 | 17/42 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Rifaximin (drug)]] 5 µM |  | 1.27× | +3.1 | 0.48 | 12/40 (A-172, C32, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4577.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.314×** | -15.8 | 0e+00 | 37/40 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.338×** | -14.8 | 0e+00 | 38/40 (A498, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.555×** | -11.3 | 2e-27 | 30/40 (NCI-H1792, NCI-H1573, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.447×** | -11.0 | 5e-26 | 34/40 (A498, SW 900, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.517×** | -9.0 | 3e-17 | 31/40 (SW 900, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.523×** | -8.9 | 7e-17 | 30/40 (SW 900, SW48, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.631×** | -8.8 | 7e-17 | 27/41 (SW 900, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.519×** | -8.5 | 2e-15 | 33/40 (SW48, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.541×** | -8.1 | 5e-14 | 32/39 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.588×** | -7.2 | 3e-11 | 25/40 (SW48, BT-474, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.605×** | -6.6 | 2e-09 | 28/40 (SW 900, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.639×** | -5.9 | 2e-07 | 21/33 (SW48, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | **0.679×** | -5.0 | 2e-05 | 22/40 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.708×** | -4.7 | 1e-04 | 22/41 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -4.7 | 1e-04 | 22/40 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.822×** | -3.7 | 0.005 | 21/41 (LOX-IMVI, HCT15, …) | all doses, stronger at high dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.755×** | -3.6 | 0.006 | 19/40 (NCI-H1792, A-172, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.609×** | -3.5 | 0.009 | 17/40 (SW48, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.687×** | -3.5 | 0.011 | 16/40 (SW48, SW 900, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.790×** | -3.2 | 0.024 | 16/40 (J82, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.640×** | -3.2 | 0.026 | 21/40 (NCI-H661, HCT15, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4577. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 62.5 | 0 | 19 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.119× (z -11.9) |
| [[SW 900 (line)]] | alt | 427 | 0 | 15 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0779× (z -18.9) |
| [[SW48 (line)]] | wt | 578 | 0 | 15 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -17.0) |
| [[SW480 (line)]] | alt | 125 | 0 | 14 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 68.3 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -20.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.220× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 383 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -27.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -18.5) |
| [[A498 (line)]] | wt | 182 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0942× (z -20.1) |
| [[SW1417 (line)]] | alt | 193 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -17.2) |
| [[RKO (line)]] | wt | 56.7 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HS-578T (line)]] | alt | 167 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -10.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.255× (z -8.9) |
| [[J82 (line)]] | alt | 146 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -13.0) |
| [[A-172 (line)]] | wt | 72.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.192× (z -13.9) |
| [[Panc 03.27 (line)]] | alt | 122 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 42.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.310× (z -9.0) |
| [[C32 (line)]] | wt | 63.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -11.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[PANC-1 (line)]] | alt | 46.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -18.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[A549 (line)]] | wt | 26.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CHP-212 (line)]] | wt | 117 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -9.5) |
| [[HOP62 (line)]] | alt | 76.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.377× (z -8.6) |
| [[LoVo (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -10.6) ⚠ cell-cycle shift, explains ~85% of this change |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.271× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -9.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RPMI-7951 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SK-MEL-2 (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -8.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 158 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.282× (z -8.8) |
| [[SW 1088 (line)]] | alt | 124 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0602× (z -9.6) |
| [[SW 1271 (line)]] | alt | 89.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0787× (z -8.9) |
| [[A-427 (line)]] | wt | 15.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4577), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02015]] | +0.51 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SPTSSB]] | +0.48 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[PLD1]] | +0.47 | +0.42 / +0.39 | both halves | 5e-05 |  |
| [[BICC1]] | +0.46 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[LPAR1]] | +0.46 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[HSD11B1]] | +0.45 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[SOD2]] | +0.45 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[MMD]] | +0.43 | +0.26 / +0.36 | both halves | 3e-04 |  |
| [[MGP]] | +0.43 | +0.41 / +0.37 | both halves | 8e-05 | STRING 683 |
| [[MAP3K5]] | +0.43 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[SLC16A2]] | +0.42 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[RBMS1]] | +0.42 | +0.38 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNND2]] | -0.40 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[TRMT2B]] | -0.37 | -0.24 / -0.36 | both halves | 4e-04 |  |
| [[PRLR]] | -0.35 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[SLCO1B3]] | -0.35 | -0.26 / -0.23 | both halves | 5e-04 |  |
| [[ZNF761]] | -0.34 | -0.34 / -0.30 | both halves | 2e-04 |  |
| [[NRIP3]] | -0.34 | -0.33 / -0.33 | both halves | 1e-04 |  |
| [[SLCO1B3-SLCO1B7]] | -0.34 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[ZNF823]] | -0.34 | -0.21 / -0.30 | both halves | 7e-04 |  |
| [[ANKRD23]] | -0.33 | -0.30 / -0.33 | both halves | 2e-04 |  |
| [[BTBD9]] | -0.33 | -0.17 / -0.33 | ⚠ not reproduced | 0.001 |  |
| [[ESM1]] | -0.33 | -0.26 / -0.30 | both halves | 4e-04 |  |
| [[LINC02509]] | -0.33 | -0.19 / -0.38 | ⚠ not reproduced | 8e-04 |  |
| [[ZNF680]] | -0.33 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[RADIL]] | -0.33 | -0.23 / -0.38 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICC1]] | B | BICC1 activity raises RUNX2's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.56× lower at baseline in the lines without BICC1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[C1QTNF1]] | B | C1QTNF1 activity raises RUNX2's level | lines that do not express C1QTNF1 (20) vs lines expressing it (30) | 2.78× lower at baseline in the lines without C1QTNF1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ZNF521, ENSG00000287622, SLC43A3 |
| [[CCBE1]] | B | CCBE1 activity raises RUNX2's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.16× lower at baseline in the lines without CCBE1 | 0.042 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1 |
| [[DCN]] | B | DCN activity raises RUNX2's level | lines that do not express DCN (39) vs lines expressing it (11) | 2.37× lower at baseline in the lines without DCN | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ADGRG7, CARMN, THY1 |
| [[LINC02509]] | B | LINC02509 activity raises RUNX2's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 1.99× lower at baseline in the lines without LINC02509 | 0.089 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2 |
| [[PTGFR]] | B | PTGFR activity raises RUNX2's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.37× lower at baseline in the lines without PTGFR | 0.094 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RADIL]] | B | RUNX2 activity lowers RADIL's level | lines that do not express RUNX2 (8) vs lines expressing it (42) | 2.61× higher at baseline in the lines without RUNX2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SATB1, ITGA3, TCEAL3; maybe low, not absent; its own permutation p |
| [[SMAD3]] | B | RUNX2 activity raises SMAD3's level | lines that do not express RUNX2 (8) vs lines expressing it (42) | 2.24× lower at baseline in the lines without RUNX2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SATB1, ITGA3, TCEAL3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, 20.4); signed map (50.1, 24.1). **Vector** length 92.7, 24.5% of its response variance represented; |z| ≥ 3 in 1,400 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | +3.3 | -4.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | +3.0 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change | +2.8 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | -0.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.6 | -9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -7.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -8.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | RUNX family transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:45,328,157-45,664,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AML3, PEBP2A1, PEBP2aA1; previously CCD, CBFA1, CCD1 |
| Gene groups (HGNC) | Runt-related transcription factors |
| Reactome | 10 pathways, smallest: RUNX2 regulates chondrocyte maturation; RUNX2 regulates genes involved in differentiation of myeloid cells; RUNX1 regulates transcription of genes involved in differentiation of myeloid cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13950](https://www.uniprot.org/uniprotkb/Q13950) (Runt-related transcription factor 2):

> Transcription factor involved in osteoblastic differentiation and skeletal morphogenesis. Essential for the maturation of osteoblasts and both intramembranous and endochondral ossification. CBF binds to the core site, 5'-PYGPYGGT-3', of a number of enhancers and promoters, including murine leukemia virus, polyomavirus enhancer, T-cell receptor enhancers, osteocalcin, osteopontin, bone sialoprotein, alpha 1(I) collagen, LCK, IL-3 and GM-CSF promoters. In osteoblasts, supports transcription …

**Summary**, from NCBI Gene [860](https://www.ncbi.nlm.nih.gov/gene/860):

> This gene is a member of the RUNX family of transcription factors and encodes a nuclear protein with an Runt DNA-binding domain. This protein is essential for osteoblastic differentiation and skeletal morphogenesis and acts as a scaffold for nucleic acids and regulatory factors involved in skeletal gene expression. The protein can bind DNA both as a monomer or, with more affinity, as a subunit of a heterodimeric complex. Two regions of potential trinucleotide repeat expansions are present in …

**Accessions** — [HGNC:10472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10472) · Entrez [860](https://www.ncbi.nlm.nih.gov/gene/860) · UniProt [Q13950](https://www.uniprot.org/uniprotkb/Q13950) · Ensembl [ENSG00000124813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124813)

## Data

Gene col 4577: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4577); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4577, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4577]; `tensor/DDL_lfc|DDL_z.npy` [4577]; `embed/gene_vectors.npy` [4577]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4577 or target_col == 4577). Every well: [[RUNX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUNX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
