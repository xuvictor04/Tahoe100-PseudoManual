---
symbol: "CNTLN"
type: "gene"
col: 500
ensembl_id: "ENSG00000044459"
name: "centlein"
location: "9p22.2"
module: 10
arm: "+"
pooled_cpm: 54.73
n_lines_expressing: 42
n_dd_up: 18
n_dd_down: 26
n_dd_up_clean: 16
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CNTLN

*centlein* — 9p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.53× (z +5.8, q 4e-06, up in 23 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +5.7, q 4e-06, up in 24 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.422× (z -11.7, q 5e-29, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FRG1-DT]] (+0.70, fdr 1e-05), [[CACNA2D1]] (+0.67, fdr 7e-06), [[TCF12]] (+0.66, fdr 1e-05); moves opposite to [[MPG]] (-0.64, fdr 3e-05), [[TMEM184B]] (-0.61, fdr 2e-05), [[GPR157]] (-0.59, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DZIP1L]] → it (grade B ⚠); 2 go from it, the strongest it → [[CCDC171]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.8 | 4e-06 | 23/38 (LoVo, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.7 | 4e-06 | 24/40 (HS-578T, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +4.4 | 0.002 | 21/40 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.010 | 24/39 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.012 | 21/39 (RKO, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +3.8 | 0.012 | 17/33 (LoVo, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.013 | 19/40 (RKO, LOX-IMVI, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.69×** | +3.7 | 0.013 | 19/40 (J82, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.014 | 18/40 (RKO, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.7 | 0.014 | 18/40 (SK-MEL-2, RKO, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.016 | 18/40 (hTERT-HPNE, SK-MEL-2, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.022 | 17/40 (RKO, HCT15, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.025 | 17/40 (HS-578T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.4 | 0.025 | 10/40 (RKO, MIA PaCa-2, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.034 | 13/40 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.048 | 16/40 (A498, HOP62, …) | inconsistent across doses |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.052 | 15/40 (A549, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 500.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.422×** | -11.7 | 5e-29 | 34/40 (SHP-77, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.457×** | -10.6 | 6e-24 | 37/40 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.487×** | -9.8 | 3e-20 | 33/40 (SHP-77, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.504×** | -9.3 | 2e-18 | 35/40 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.544×** | -8.3 | 2e-14 | 34/40 (SNU-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.338×** | -7.7 | 1e-12 | 31/40 (A-427, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -7.6 | 3e-12 | 34/41 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.613×** | -6.6 | 2e-09 | 29/40 (HEC-1-A, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.616×** | -6.6 | 3e-09 | 31/40 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.633×** | -6.2 | 3e-08 | 27/40 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -5.5 | 2e-06 | 24/40 (HEC-1-A, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.669×** | -5.5 | 2e-06 | 28/40 (A-172, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -5.4 | 3e-06 | 28/40 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.487×** | -5.1 | 1e-05 | 30/40 (SK-MEL-2, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.691×** | -5.0 | 2e-05 | 20/40 (NCI-H1792, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.774×** | -4.9 | 4e-05 | 27/40 (MIA PaCa-2, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.249× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.319× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 88.7 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.294× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.298× (z -10.0) |
| [[SNU-1 (line)]] | wt | 131 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 135 | 0 | 6 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.301× (z -12.3) |
| [[A-427 (line)]] | wt | 96.2 | 0 | 5 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0649× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 82.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.300× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 60.9 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.286× (z -10.9) |
| [[SHP-77 (line)]] | alt | 126 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.314× (z -12.1) |
| [[A549 (line)]] | wt | 95.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -10.4) |
| [[J82 (line)]] | alt | 114 | 1 (1 ⚠) | 1 | [[Selinexor (drug)]] 5 µM 2.02× (z +9.3) ⚠ cell-cycle shift, explains ~80% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.379× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 47.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.273× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 98.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.324× (z -10.0) |
| [[AN3 CA (line)]] | alt | 126 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0883× (z -8.6) |
| [[C-33 A (line)]] | alt | 114 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.250× (z -11.3) |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -8.7) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 60.2 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +8.8) | — |
| [[LoVo (line)]] | wt | 29.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.55× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.256× (z -11.3) ⚠ toxic |
| [[A-172 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 102 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.47 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 71.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 116 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1-DT]] | +0.70 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[CACNA2D1]] | +0.67 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[TCF12]] | +0.66 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CPLANE1]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.65 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[FAM111A]] | +0.65 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[USP13]] | +0.65 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[ZNF236]] | +0.64 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[EIF1B-AS1]] | +0.63 | +0.64 / +0.37 | both halves | 7e-05 |  |
| [[DPH6-DT]] | +0.63 | +0.67 / +0.26 | both halves | 4e-04 |  |
| [[RIF1]] | +0.63 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[ZNF532]] | +0.63 | +0.51 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPG]] | -0.64 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.61 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[GPR157]] | -0.59 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[EIF4EBP1]] | -0.59 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[DNAAF3]] | -0.59 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TMEM120B]] | -0.58 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[ATG4B]] | -0.58 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[MKNK2]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TNNI3]] | -0.57 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[GPR89B]] | -0.57 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[FBXL16]] | -0.56 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[MPST]] | -0.56 | -0.50 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DZIP1L]] | B | DZIP1L activity raises CNTLN's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 4.66× lower at baseline in the lines without DZIP1L | 0.076 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers CNTLN's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[FRG1-DT]] | C | FRG1-DT activity raises CNTLN's level | lines that do not express FRG1-DT (7) vs lines expressing it (43) | 4.50× lower at baseline in the lines without FRG1-DT | 0.078 | ⚠ within organs, on part of the lines; also absent: GALNT16, ENSG00000272438, PRKAR2B; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC171]] | B | CNTLN activity raises CCDC171's level | lines that do not express CNTLN (8) vs lines expressing it (42) | 2.16× lower at baseline in the lines without CNTLN | 0.036 | ⚠ within organs, on part of the lines; also absent: SRGAP2D, PRKAR2B, WDR54 |
| [[DZIP1L]] | B | CNTLN activity raises DZIP1L's level | lines that do not express CNTLN (8) vs lines expressing it (42) | 3.72× lower at baseline in the lines without CNTLN | 0.098 | ⚠ within organs, on part of the lines; also absent: SRGAP2D, PRKAR2B, WDR54 |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-4.7, 5.1); signed map (20.2, -33.4). **Vector** length 113, 34.6% of its response variance represented; |z| ≥ 3 in 1,063 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +7.0 | +2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.9 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | -0.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +1.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.3 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -10.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.9 | -11.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.6 | -9.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.5 | -5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -6.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | centlein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.2 — chr9:17,134,982-17,503,923 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20276, bA340N12.1, OTTHUMG00000019597; previously C9orf101, C9orf39 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXG0](https://www.uniprot.org/uniprotkb/Q9NXG0) (Centlein):

> Required for centrosome cohesion and recruitment of CEP68 to centrosomes.

**Summary**, from NCBI Gene [54875](https://www.ncbi.nlm.nih.gov/gene/54875):

> Enables protein domain specific binding activity; protein kinase binding activity; and protein-macromolecule adaptor activity. Involved in centriole-centriole cohesion. Located in centriole; centrosome; and cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23432) · Entrez [54875](https://www.ncbi.nlm.nih.gov/gene/54875) · UniProt [Q9NXG0](https://www.uniprot.org/uniprotkb/Q9NXG0) · Ensembl [ENSG00000044459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000044459)

## Data

Gene col 500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 500); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 500]; `tensor/DDL_lfc|DDL_z.npy` [500]; `embed/gene_vectors.npy` [500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 500 or target_col == 500). Every well: [[CNTLN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTLN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
