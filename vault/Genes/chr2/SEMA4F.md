---
symbol: "SEMA4F"
type: "gene"
col: 5731
ensembl_id: "ENSG00000135622"
name: "ssemaphorin 4F"
location: "2p13.1"
module: 159
arm: "+"
pooled_cpm: 6.72
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# SEMA4F

*ssemaphorin 4F* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.58× (z +14.3, q 7e-44, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.458× (z -11.8, q 4e-29, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAZ]] (+0.73, fdr 7e-06), [[RIMS3]] (+0.73, fdr 7e-06), [[LRFN3]] (+0.72, fdr 1e-05); moves opposite to [[MCPH1]] (-0.68, fdr 3e-05), [[GTF2H1]] (-0.67, fdr 1e-05), [[AEBP2]] (-0.65, fdr 3e-05).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[KATNAL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5731.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.58×** | +14.3 | 7e-44 | 40/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +14.1 | 2e-42 | 41/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +11.7 | 2e-29 | 35/46 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +8.0 | 2e-13 | 21/47 (SW480, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +7.9 | 4e-13 | 25/46 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +5.7 | 1e-06 | 18/43 (Hs 766T, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +5.2 | 2e-05 | 16/40 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +4.0 | 0.004 | 7/45 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.011 | 2/46 (A498, C32) | inconsistent across doses | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.54×** | +3.4 | 0.038 | 4/35 (HOP62, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.24×** | +3.2 | 0.066 | 2/46 (SW480, NCI-H2347) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.077 | 4/46 (RPMI-7951, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.24× | +3.0 | 0.12 | 4/19 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5731.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.458×** | -11.8 | 4e-29 | 32/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.453×** | -11.1 | 5e-26 | 30/44 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.613×** | -10.4 | 5e-23 | 25/41 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.530×** | -9.5 | 2e-19 | 27/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.579×** | -7.6 | 2e-12 | 19/34 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -7.5 | 5e-12 | 21/46 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.611×** | -7.4 | 1e-11 | 23/40 (NCI-H1573, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.633×** | -6.9 | 5e-10 | 23/40 (A-172, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.645×** | -6.6 | 3e-09 | 21/45 (A-172, A549, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.445×** | -6.4 | 1e-08 | 23/44 (RKO, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.656×** | -6.3 | 1e-08 | 22/45 (HCT15, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -5.0 | 2e-05 | 16/46 (HEC-1-A, PANC-1, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.718×** | -5.0 | 3e-05 | 16/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.547×** | -4.7 | 8e-05 | 13/39 (HOP62, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.740×** | -4.5 | 2e-04 | 12/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -4.2 | 0.001 | 17/46 (C32, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | **0.742×** | -4.2 | 0.001 | 12/40 (LoVo, HOP62, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.762×** | -3.8 | 0.004 | 11/42 (A498, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.650×** | -3.4 | 0.022 | 5/42 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.746×** | -3.1 | 0.049 | 3/46 (SK-MEL-2, A-172, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5731. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -15.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0668× (z -14.2) |
| [[A-427 (line)]] | wt | 16.6 | 0 | 3 | — | [[Omeprazole (drug)]] 0.5 µM 0.239× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 6.74 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.129× (z -11.6) |
| [[PANC-1 (line)]] | alt | 6.44 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.134× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.182× (z -9.9) |
| [[C32 (line)]] | wt | 10.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -9.6) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.108× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 7.15 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0590× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 9.59 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0844× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SW480 (line)]] | alt | 6.49 | 1 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.17× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -8.9) |
| [[A549 (line)]] | wt | 9.00 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.153× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.89 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.179× (z -9.2) ⚠ toxic |
| [[J82 (line)]] | alt | 4.32 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -11.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[LOX-IMVI (line)]] | wt | 8.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 4.90 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0803× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -11.7) ⚠ cell-cycle shift, explains ~48% of this change |
| [[SW1417 (line)]] | alt | 8.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5731), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAZ]] | +0.73 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[RIMS3]] | +0.73 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LRFN3]] | +0.72 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[CROCCP3]] | +0.71 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[POMGNT2]] | +0.70 | +0.58 / +0.69 | both halves | 8e-06 |  |
| [[WASF3]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[STIMATE]] | +0.65 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[ACTR5]] | +0.64 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[USP35]] | +0.63 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.62 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[FCHSD1]] | +0.62 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[DNMT3B]] | +0.62 | +0.52 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCPH1]] | -0.68 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[GTF2H1]] | -0.67 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[AEBP2]] | -0.65 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ASH1L]] | -0.65 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[LINC00571]] | -0.62 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[WARS2-AS1]] | -0.61 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[CCDC90B-AS1]] | -0.61 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[ANGPT2]] | -0.61 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[INO80D]] | -0.61 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[MZF1-AS1]] | -0.61 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[RBM23]] | -0.61 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[ST8SIA5]] | -0.60 | -0.43 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KATNAL1]] | B | KATNAL1 activity raises SEMA4F's level | lines that do not express KATNAL1 (7) vs lines expressing it (43) | 1.89× lower at baseline in the lines without KATNAL1 | 0.021 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, STARD9, SPAG17 |
| [[GNAZ]] | B | GNAZ activity raises SEMA4F's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without GNAZ | 0.054 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |
| [[TMOD2]] | B | TMOD2 activity raises SEMA4F's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without TMOD2 | 0.065 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[RAB3B]] | B | RAB3B activity raises SEMA4F's level | lines that do not express RAB3B (17) vs lines expressing it (33) | 1.37× lower at baseline in the lines without RAB3B | 0.075 | ⚠ within organs, on part of the lines; also absent: C1QL1, CYS1, ACTN2 |
| [[BVES]] | B | BVES activity raises SEMA4F's level | lines that do not express BVES (19) vs lines expressing it (31) | 1.49× lower at baseline in the lines without BVES | 0.079 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2 |
| [[SDC3]] | C | SDC3 activity raises SEMA4F's level | lines that do not express SDC3 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without SDC3 | 0.089 | ⚠ few lines (4 vs 46); across organs |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.0, -0.6); signed map (-39.4, -7.4). **Vector** length 58.2, 8.12% of its response variance represented; |z| ≥ 3 in 1,136 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.2 | +14.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +11.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +14.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.9 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +8.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +1.6 |
|  | [[vincristine (drug)]] 5 µM |  | +1.3 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -11.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.6 | -10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.3 | -6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.7 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -0.8 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.3 | -1.2 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ssemaphorin 4F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,654,228-74,683,853 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SEMAW; previously SEMAM |
| Gene groups (HGNC) | Semaphorins |
| Reactome | 4 pathways, smallest: RND3 GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [O95754](https://www.uniprot.org/uniprotkb/O95754) (Semaphorin-4F):

> Probable cell surface receptor that regulates oligodendroglial precursor cell migration (By similarity). Might also regulate differentiation of oligodendroglial precursor cells (By similarity). Has growth cone collapse activity against retinal ganglion-cell axons (By similarity).

**Summary**, from NCBI Gene [10505](https://www.ncbi.nlm.nih.gov/gene/10505):

> This gene encodes a transmembrane class IV semaphorin family protein, which plays a role in neural development. This gene may be involved in neurogenesis in prostate cancer, the development of neurofibromas, and breast cancer tumorigenesis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Nov 2012]

**Accessions** — [HGNC:10734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10734) · Entrez [10505](https://www.ncbi.nlm.nih.gov/gene/10505) · UniProt [O95754](https://www.uniprot.org/uniprotkb/O95754) · Ensembl [ENSG00000135622](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135622)

## Data

Gene col 5731: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5731); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5731, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5731]; `tensor/DDL_lfc|DDL_z.npy` [5731]; `embed/gene_vectors.npy` [5731]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5731 or target_col == 5731). Every well: [[SEMA4F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEMA4F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
