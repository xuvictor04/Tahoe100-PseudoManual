---
symbol: "GUCY1B2"
type: "gene"
col: 4416
ensembl_id: "ENSG00000123201"
name: "guanylate cyclase 1 soluble subunit beta 2 (pseudogene)"
location: "13q14.3"
module: 10
arm: "+"
pooled_cpm: 4.39
n_lines_expressing: 32
n_dd_up: 13
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# GUCY1B2

*guanylate cyclase 1 soluble subunit beta 2 (pseudogene)* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.81× (z +7.7, q 1e-11, up in 3 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.48× (z +4.3, q 0.002, up in 8 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.335× (z -8.4, q 2e-14, down in 25 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AGA-DT]] (+0.65, fdr 3e-05), [[TPRG1]] (+0.65, fdr 1e-05), [[CASC9]] (+0.64, fdr 1e-05); moves opposite to [[TMEM184B]] (-0.58, fdr 3e-05), [[RGS10]] (-0.58, fdr 3e-05), [[MPG]] (-0.56, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02026]] → it (grade B ⚠); 6 go from it, the strongest it → cells under [[Verteporfin (drug)]] 5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4416.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +7.7 | 1e-11 | 3/8 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +5.6 | 6e-06 | 6/11 (MIA PaCa-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.93×** | +5.1 | 8e-05 | 5/17 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.48×** | +4.3 | 0.002 | 8/27 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +4.2 | 0.003 | 15/28 (NCI-H23, HCT15, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.72×** | +4.2 | 0.003 | 15/29 (COLO 205, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.004 | 9/29 (LoVo, NCI-H460, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.66×** | +3.9 | 0.007 | 9/29 (COLO 205, PANC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.44×** | +3.8 | 0.008 | 14/29 (SW480, HCT15, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.021 | 7/29 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.024 | 10/29 (SW480, NCI-H23, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.37×** | +3.4 | 0.030 | 9/29 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.069 | 8/29 (SW480, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4416.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.335×** | -8.4 | 2e-14 | 25/29 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.463×** | -5.9 | 9e-07 | 16/29 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.472×** | -5.8 | 1e-06 | 20/29 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.478×** | -5.7 | 2e-06 | 21/29 (COLO 205, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.472×** | -5.5 | 5e-06 | 20/27 (PANC-1, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.499×** | -5.4 | 8e-06 | 14/29 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.505×** | -5.3 | 1e-05 | 19/29 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.508×** | -5.2 | 1e-05 | 17/29 (COLO 205, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.538×** | -4.8 | 1e-04 | 14/26 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.538×** | -4.8 | 1e-04 | 17/29 (NCI-H1792, SHP-77, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.563×** | -4.3 | 7e-04 | 14/29 (SW 1271, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.609×** | -3.8 | 0.006 | 18/25 (A549, SHP-77, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.604×** | -3.7 | 0.008 | 13/29 (SW 900, COLO 205, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -3.7 | 0.010 | 13/29 (NCI-H460, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.619×** | -3.6 | 0.011 | 11/29 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -3.3 | 0.034 | 10/27 (A549, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.750×** | -3.1 | 0.054 | 8/29 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.469×** | -3.0 | 0.068 | 12/28 (NCI-H23, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.663×** | -3.0 | 0.068 | 8/29 (SW 1271, NCI-H2030, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.668×** | -3.0 | 0.076 | 7/29 (AsPC-1, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.481×** | -2.9 | 0.082 | 12/29 (SHP-77, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4416. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 14.9 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0306× (z -14.2) |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 3 (2 ⚠) | — | [[Artesunate (drug)]] 5 µM 0.131× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0964× (z -8.7) |
| [[A549 (line)]] | wt | 11.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0426× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.131× (z -11.7) |
| [[PANC-1 (line)]] | alt | 4.85 | 0 | 2 | — | [[Bortezomib (drug)]] 0.05 µM 0.0823× (z -9.7) |
| [[LoVo (line)]] | wt | 2.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.53 | 0 | 1 | — | [[vincristine (drug)]] 0.05 µM 0.0435× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 4.64 | 0 | 1 | — | [[Tazarotene (drug)]] 0.5 µM 0.0544× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 8.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0832× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H460 (line)]] | wt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0836× (z -8.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 0.613 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.902 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.708 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.665 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.814 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.835 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.651 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.816 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.751 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.657 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4416), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGA-DT]] | +0.65 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[TPRG1]] | +0.65 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[CASC9]] | +0.64 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[BANK1]] | +0.63 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[IQCH-AS1]] | +0.63 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[KRBA2]] | +0.63 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[ANXA2R-AS1]] | +0.62 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[STPG2]] | +0.62 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[BCLAF1]] | +0.62 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[ZNF747]] | +0.62 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[NXPH1]] | +0.61 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[DRAIC]] | +0.60 | +0.60 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | -0.58 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[RGS10]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MPG]] | -0.56 | -0.63 / -0.30 | both halves | 2e-04 |  |
| [[FLNB]] | -0.55 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[HMOX2]] | -0.55 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[GUK1]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[BET1L]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[PDIA5]] | -0.54 | -0.55 / -0.34 | both halves | 1e-04 |  |
| [[ZCCHC17]] | -0.53 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[TPST2]] | -0.53 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SLC37A3]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[EIF4EBP1]] | -0.52 | -0.54 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02026]] | B | LINC02026 activity raises GUCY1B2's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without LINC02026 | 0.022 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[MAP2K1]] | B | MAP2K1 activity lowers GUCY1B2's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[RDM1P5]] | B | RDM1P5 activity raises GUCY1B2's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without RDM1P5 | 0.080 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[TESMIN]] | C | TESMIN activity raises GUCY1B2's level | lines that do not express TESMIN (11) vs lines expressing it (39) | 2.94× lower at baseline in the lines without TESMIN | 0.017 | ⚠ within organs, on part of the lines; also absent: GPRC5A, GUCY1B2, CDKN1C; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Verteporfin (drug)]] 5 µM | B | GUCY1B2 activity raises the cells' numbers under Verteporfin 5 µM (protects the cells) | lines that do not express GUCY1B2 (18) vs lines expressing it (30) | the lines without GUCY1B2: 0.82× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |
| [[LINC02889]] | B | GUCY1B2 activity raises LINC02889's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without GUCY1B2 | 0.049 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |
| [[RBM23]] | B | GUCY1B2 activity raises RBM23's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without GUCY1B2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |
| [[ZNF630]] | B | GUCY1B2 activity raises ZNF630's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 2.03× lower at baseline in the lines without GUCY1B2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |
| [[MPG]] | B | GUCY1B2 activity lowers MPG's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 1.24× higher at baseline in the lines without GUCY1B2 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent |
| [[TESMIN]] | C | GUCY1B2 activity raises TESMIN's level | lines that do not express GUCY1B2 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without GUCY1B2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, TNFRSF1B, MAP7; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (18.0, 20.7); signed map (33.1, -11.8). **Vector** length 64.4, 14.4% of its response variance represented; |z| ≥ 3 in 768 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.9 | -8.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.3 | -5.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.1 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.0 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -0.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | guanylate cyclase 1 soluble subunit beta 2 (pseudogene) |
| Locus type | pseudogene |
| Location | 13q14.3 — chr13:51,006,991-51,062,894 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | GUCY1B2P, GC-SB2 |
| Gene groups (HGNC) | Soluble guanylate cyclases; Unitary pseudogenes |
| Reactome | 5 pathways, smallest: Nitric oxide stimulates guanylate cyclase; Smooth Muscle Contraction; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75343](https://www.uniprot.org/uniprotkb/O75343) (Putative guanylate cyclase soluble subunit beta-2):

> Probably a non-functional pseudogene. In mouse, the functional ortholog acts as a soluble guanylate cyclase that senses low environmental oxygen in sensory neurons of the main olfactory epithelium.

**Summary**, from NCBI Gene [2974](https://www.ncbi.nlm.nih.gov/gene/2974):

> Predicted to enable guanylate cyclase activity. Predicted to be involved in response to oxygen levels. Predicted to be located in cytosol. Predicted to be part of guanylate cyclase complex, soluble. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4686) · Entrez [2974](https://www.ncbi.nlm.nih.gov/gene/2974) · UniProt [O75343](https://www.uniprot.org/uniprotkb/O75343) · Ensembl [ENSG00000123201](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123201)

## Data

Gene col 4416: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4416); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4416, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4416]; `tensor/DDL_lfc|DDL_z.npy` [4416]; `embed/gene_vectors.npy` [4416]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4416 or target_col == 4416). Every well: [[GUCY1B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUCY1B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
