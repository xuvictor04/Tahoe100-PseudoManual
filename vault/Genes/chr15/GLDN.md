---
symbol: "GLDN"
type: "gene"
col: 11813
ensembl_id: "ENSG00000186417"
name: "gliomedin"
location: "15q21.2"
module: 27
arm: "+"
pooled_cpm: 4.59
n_lines_expressing: 25
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 19
direction_downstream: 20
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# GLDN

*gliomedin* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.91× (z +9.3, q 8e-18, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 1.69× (z +4.6, q 6e-04, up in 8 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.267× (z -11.9, q 4e-30, down in 22 of 22 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.553× (z -5.4, q 8e-06, down in 14 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4713HG]] (+0.86, fdr 7e-06, ⚠ same locus), [[LINC00649]] (+0.73, fdr 7e-06), [[DLEU1]] (+0.64, fdr 1e-05), [[BANK1]] (+0.62, fdr 1e-05); moves opposite to [[ITGB1BP1]] (-0.59, fdr 3e-05), [[MPP3]] (-0.51, fdr 4e-05), [[PPP2R3A]] (-0.50, fdr 5e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[SOX6]] → it (grade B ⚠); 20 go from it, the strongest it → [[DLEU1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11813.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +9.3 | 8e-18 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.42×** | +7.4 | 4e-11 | 1/9 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.0 | 9e-05 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.69×** | +4.6 | 6e-04 | 8/21 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.43×** | +4.6 | 6e-04 | 7/22 (KATO III, LS 180, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 0.001 | 6/22 (SW480, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.59×** | +4.2 | 0.002 | 10/22 (HCT15, SW48, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.006 | 7/22 (SW480, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.006 | 5/22 (H4, SW 900, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +3.9 | 0.006 | 7/21 (SW480, Hs 766T, …) | rises with dose |  |
| [[Finasteride (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.039 | 3/22 (NCI-H460, NCI-H1792, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.3 | 0.043 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.2 | 0.060 | 1/21 (NCI-H1792) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.41×** | +3.1 | 0.084 | 3/22 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11813.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.267×** | -11.9 | 4e-30 | 22/22 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.288×** | -11.3 | 6e-27 | 20/22 (HT-29, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.345×** | -9.6 | 1e-19 | 19/22 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.358×** | -9.3 | 2e-18 | 20/22 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.545×** | -5.5 | 4e-06 | 17/22 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.553×** | -5.4 | 8e-06 | 14/22 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.325×** | -5.3 | 9e-06 | 16/22 (KATO III, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.544×** | -5.3 | 9e-06 | 15/22 (NCI-H1792, NCI-H460, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.568×** | -4.8 | 9e-05 | 15/21 (HT-29, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.592×** | -4.7 | 1e-04 | 13/22 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.635×** | -4.1 | 0.002 | 17/22 (HT-29, MIA PaCa-2, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.640×** | -4.0 | 0.002 | 9/22 (SW480, SW 900, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.648×** | -3.9 | 0.004 | 17/21 (NCI-H1792, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.758×** | -3.5 | 0.016 | 10/22 (SW 900, MIA PaCa-2, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.579×** | -3.5 | 0.016 | 8/22 (NCI-H460, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.476×** | -3.5 | 0.016 | 10/20 (NCI-H460, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **0.673×** | -3.5 | 0.019 | 1/22 (NCI-H460) | rises with dose | plate-row cell shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.703×** | -3.2 | 0.046 | 15/22 (HT-29, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.699×** | -3.1 | 0.054 | 6/22 (SW480, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.721×** | -3.0 | 0.086 | 4/22 (NCI-H460, J82, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.57 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11813. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 14.4 | 0 | 17 (15 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0463× (z -17.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.192× (z -9.2) |
| [[HT-29 (line)]] | alt | 16.5 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0389× (z -15.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0568× (z -13.8) |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 9 (8 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0295× (z -17.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -12.7) |
| [[SW480 (line)]] | alt | 5.77 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0777× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[LoVo (line)]] | wt | 5.87 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0891× (z -9.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.03 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 12.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0346× (z -10.5) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Decitabine (drug)]] 5 µM 0.0486× (z -9.1) |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.126× (z -11.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 17.5 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0225× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 6.17 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0449× (z -9.4) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 7.37 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0360× (z -9.9) ⚠ cell-cycle shift, explains ~35% of this change |
| [[SW 900 (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0454× (z -14.4) ⚠ cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 8.09 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -9.3) |
| [[KATO III (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0238× (z -12.3) ⚠ cell-cycle shift, explains ~35% of this change |
| [[RPMI-7951 (line)]] | alt | 4.09 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.639 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.497 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.547 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.699 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.632 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.544 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.653 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.727 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.672 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.550 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.479 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.531 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.575 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.838 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11813), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4713HG]] | +0.86 | +0.85 / +0.84 | both halves | 7e-06 | ⚠ same locus (47.7 kb, same strand: neighbours can correlate without regulation) |
| [[LINC00649]] | +0.73 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[DLEU1]] | +0.64 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[BANK1]] | +0.62 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CASC9]] | +0.62 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[LINC02466]] | +0.61 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[NDUFA4L2]] | +0.60 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[LINC02058]] | +0.59 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[STK31]] | +0.59 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[SLC44A5]] | +0.58 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[PKHD1]] | +0.57 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[WDR72]] | +0.57 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[UGT1A8]] | +0.57 | +0.61 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB1BP1]] | -0.59 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[MPP3]] | -0.51 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[PPP2R3A]] | -0.50 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[DNAAF9]] | -0.45 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[CDR2L]] | -0.45 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[TUBB6]] | -0.45 | -0.35 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 6, C 13. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOX6]] | B | SOX6 activity raises GLDN's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 2.24× lower at baseline in the lines without SOX6 | 0.009 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[PLCB1]] | B | PLCB1 activity raises GLDN's level | lines that do not express PLCB1 (19) vs lines expressing it (31) | 2.44× lower at baseline in the lines without PLCB1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000289384, SNTB1, SOX6 |
| [[LINC01980]] | B | LINC01980 activity raises GLDN's level | lines that do not express LINC01980 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without LINC01980 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNMB2, LINC00698, PAPPA2; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers GLDN's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[CRACR2A]] | B | CRACR2A activity raises GLDN's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 2.31× lower at baseline in the lines without CRACR2A | 0.061 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |
| [[HNMT]] | B | HNMT activity raises GLDN's level | lines that do not express HNMT (17) vs lines expressing it (33) | 1.77× lower at baseline in the lines without HNMT | 0.093 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TNFSF10, VSIR |
| [[MIR4713HG]] | C | MIR4713HG activity raises GLDN's level | lines that do not express MIR4713HG (30) vs lines expressing it (20) | 3.71× lower at baseline in the lines without MIR4713HG | 5e-04 | ⚠ within organs, on part of the lines; also absent: GLDN, C4BPB, IL20RA; co-absent with the target |
| [[PIP5K1B]] | C | PIP5K1B activity raises GLDN's level | lines that do not express PIP5K1B (33) vs lines expressing it (17) | 3.12× lower at baseline in the lines without PIP5K1B | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF3, LINC02964, TMEM45B; co-absent with the target |
| [[BBOX1-AS1]] | C | BBOX1-AS1 activity raises GLDN's level | lines that do not express BBOX1-AS1 (21) vs lines expressing it (29) | 2.66× lower at baseline in the lines without BBOX1-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: GLDN, CHN2, CPVL; maybe low, not absent; co-absent with the target |
| [[SORBS2]] | C | SORBS2 activity raises GLDN's level | lines that do not express SORBS2 (17) vs lines expressing it (33) | 2.84× lower at baseline in the lines without SORBS2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC00299, ENSG00000228033, HR; co-absent with the target |
| [[CHN2]] | C | CHN2 activity raises GLDN's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 2.86× lower at baseline in the lines without CHN2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15; co-absent with the target |
| [[GNGT1]] | C | GNGT1 activity raises GLDN's level | lines that do not express GNGT1 (30) vs lines expressing it (20) | 2.35× lower at baseline in the lines without GNGT1 | 0.027 | ⚠ within organs, on part of the lines; also absent: SLC25A24P1, REG4, CACNA2D3; co-absent with the target |

### Downstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 9, C 11. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLEU1]] | B | GLDN activity raises DLEU1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 3.00× lower at baseline in the lines without GLDN | 0.007 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[CRACR2A]] | B | GLDN activity raises CRACR2A's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.73× lower at baseline in the lines without GLDN | 0.019 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[BANK1]] | B | GLDN activity raises BANK1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without GLDN | 0.022 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[NDUFA4L2]] | B | GLDN activity raises NDUFA4L2's level | lines that do not express GLDN (25) vs lines expressing it (25) | 1.85× lower at baseline in the lines without GLDN | 0.022 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[PLCB1]] | B | GLDN activity raises PLCB1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without GLDN | 0.030 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[NRG4]] | B | GLDN activity raises NRG4's level | lines that do not express GLDN (25) vs lines expressing it (25) | 1.37× lower at baseline in the lines without GLDN | 0.067 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[LINC00649]] | B | GLDN activity raises LINC00649's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.06× lower at baseline in the lines without GLDN | 0.076 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[LINC01980]] | B | GLDN activity raises LINC01980's level | lines that do not express GLDN (25) vs lines expressing it (25) | 1.56× lower at baseline in the lines without GLDN | 0.082 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[HNMT]] | B | GLDN activity raises HNMT's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.15× lower at baseline in the lines without GLDN | 0.097 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595 |
| [[MIR4713HG]] | C | GLDN activity raises MIR4713HG's level | lines that do not express GLDN (25) vs lines expressing it (25) | 7.62× lower at baseline in the lines without GLDN | 1e-04 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595; co-absent with the target |
| [[BBOX1-AS1]] | C | GLDN activity raises BBOX1-AS1's level | lines that do not express GLDN (25) vs lines expressing it (25) | 2.70× lower at baseline in the lines without GLDN | 0.025 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595; co-absent with the target |
| [[LINC01748]] | C | GLDN activity raises LINC01748's level | lines that do not express GLDN (25) vs lines expressing it (25) | 3.23× lower at baseline in the lines without GLDN | 0.033 | ⚠ within organs, on part of the lines; also absent: MIR4713HG, MT1G, ENSG00000255595; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.4, 43.9); signed map (59.1, 17.1). **Vector** length 63.8, 16.3% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.1 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | -2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +4.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -1.8 | -11.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.5 | -4.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.4 | -0.2 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.3 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.3 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | gliomedin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,341,655-51,408,005 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CRG-L2, CLOM, colmedin, UNC-122; previously COLM |
| Gene groups (HGNC) | Olfactomedin domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMI3](https://www.uniprot.org/uniprotkb/Q6ZMI3) (Gliomedin):

> Ligand for NRCAM and NFASC/neurofascin that plays a role in the formation and maintenance of the nodes of Ranvier on myelinated axons. Mediates interaction between Schwann cell microvilli and axons via its interactions with NRCAM and NFASC. Nodes of Ranvier contain clustered sodium channels that are crucial for the saltatory propagation of action potentials along myelinated axons. During development, nodes of Ranvier are formed by the fusion of two heminodes. Required for normal clustering of …

**Summary**, from NCBI Gene [342035](https://www.ncbi.nlm.nih.gov/gene/342035):

> This gene encodes a protein that contains olfactomedin-like and collagen-like domains. The encoded protein, which exists in both transmembrane and secreted forms, promotes formation of the nodes of Ranvier in the peripheral nervous system. Mutations in this gene cause a form of lethal congenital contracture syndrome in human patients. Autoantibodies to the encoded protein have been identified in sera form patients with multifocal motor neuropathy. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:29514](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29514) · Entrez [342035](https://www.ncbi.nlm.nih.gov/gene/342035) · UniProt [Q6ZMI3](https://www.uniprot.org/uniprotkb/Q6ZMI3) · Ensembl [ENSG00000186417](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186417)

## Data

Gene col 11813: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11813); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11813, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11813]; `tensor/DDL_lfc|DDL_z.npy` [11813]; `embed/gene_vectors.npy` [11813]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11813 or target_col == 11813). Every well: [[GLDN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GLDN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
