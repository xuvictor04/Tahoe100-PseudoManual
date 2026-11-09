---
symbol: "DHRS12"
type: "gene"
col: 2273
ensembl_id: "ENSG00000102796"
name: "dehydrogenase/reductase 12"
location: "13q14.3"
module: 68
arm: "+"
pooled_cpm: 6.29
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# DHRS12

*dehydrogenase/reductase 12* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM: 1.72× (z +6.8, q 5e-09, up in 24 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.626× (z -8.3, q 5e-14, down in 24 of 42 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC9A8]] (+0.66, fdr 7e-06), [[CHTOP]] (+0.61, fdr 1e-05), [[FKRP]] (+0.61, fdr 3e-05); moves opposite to [[GRB2]] (-0.61, fdr 2e-05), [[NFATC3]] (-0.60, fdr 1e-05), [[C1orf21]] (-0.58, fdr 4e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.72×** | +6.8 | 5e-09 | 24/46 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +6.5 | 2e-08 | 20/48 (SW48, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.62×** | +5.6 | 4e-06 | 4/16 (CFPAC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.8 | 3e-04 | 10/47 (HOP62, NCI-H2347, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +4.4 | 0.001 | 1/9 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.005 | 7/43 (SW480, HEC-1-A, …) | two highest doses |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.009 | 11/46 (BT-474, SNU-1, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.37×** | +3.8 | 0.009 | 12/44 (SW480, RKO, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.012 | 4/48 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.018 | 3/30 (LS 180, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.021 | 4/47 (SW480, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +3.5 | 0.026 | 5/46 (KATO III, SHP-77, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.030 | 5/47 (A-172, NCI-H1573, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.046 | 12/47 (SW480, hTERT-HPNE, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.29×** | +3.2 | 0.046 | 5/47 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.29×** | +3.2 | 0.046 | 4/47 (Hs 766T, COLO 205, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.046 | 7/47 (SW480, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.046 | 2/47 (SW 900, SW480) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +3.2 | 0.046 | 5/47 (Hs 766T, COLO 205, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.046 | 6/46 (SW480, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -8.3 | 5e-14 | 24/42 (Panc 03.27, COLO 205, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.524×** | -8.1 | 1e-13 | 27/47 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.564×** | -7.2 | 1e-10 | 26/46 (PANC-1, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.582×** | -6.8 | 2e-09 | 23/47 (PANC-1, SW480, …) | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.585×** | -6.7 | 2e-09 | 22/47 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.619×** | -6.0 | 2e-07 | 18/37 (SW480, SW1417, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.447×** | -5.3 | 1e-05 | 16/40 (NCI-H1573, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.645×** | -5.2 | 1e-05 | 18/44 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.672×** | -5.0 | 4e-05 | 18/47 (SNU-423, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.471×** | -4.9 | 4e-05 | 12/44 (NCI-H1573, SNU-423, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.675×** | -4.9 | 4e-05 | 21/43 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.694×** | -4.6 | 2e-04 | 17/47 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.720×** | -4.1 | 0.002 | 18/47 (SNU-423, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.564×** | -3.8 | 0.007 | 13/36 (LS 180, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.665×** | -3.6 | 0.010 | 8/47 (SNU-423, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.781×** | -3.0 | 0.078 | 6/47 (LOX-IMVI, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 12.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0628× (z -11.6) |
| [[SNU-423 (line)]] | alt | 4.80 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.0802× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 7.69 | 0 | 2 | — | [[Belinostat (drug)]] 0.5 µM 0.0660× (z -11.0) |
| [[LoVo (line)]] | wt | 4.51 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0867× (z -10.9) ⚠ transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 9.51 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -9.5) ⚠ cell-cycle shift, explains ~74% of this change |
| [[Panc 03.27 (line)]] | alt | 8.36 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -8.7) |
| [[SW480 (line)]] | alt | 5.36 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0331× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[A-172 (line)]] | wt | 6.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A8]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CHTOP]] | +0.61 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[FKRP]] | +0.61 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[CXCL2]] | +0.59 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[MYL5]] | +0.58 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SAYSD1]] | +0.58 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[PNRC2]] | +0.58 | +0.60 / +0.37 | both halves | 7e-05 |  |
| [[HHLA3]] | +0.57 | +0.60 / +0.24 | both halves | 5e-04 |  |
| [[VPS35L]] | +0.57 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[BPHL]] | +0.57 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[LIG4]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TCEANC]] | +0.57 | +0.61 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRB2]] | -0.61 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[NFATC3]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[C1orf21]] | -0.58 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.57 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[THOC3]] | -0.57 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[SAP130]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TNPO3]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[SPICE1]] | -0.56 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[ANKRD13D]] | -0.56 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[SNHG30]] | -0.55 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[QPCTL]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[GLG1]] | -0.55 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers DHRS12's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises DHRS12's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 1.66× lower at baseline in the lines without TMEM9B-AS1 | 0.081 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |
| [[P3H1]] | C | P3H1 activity lowers DHRS12's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.88× higher at baseline in the lines without P3H1 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-17.1, -2.7); signed map (19.1, -24.6). **Vector** length 57.8, 7.71% of its response variance represented; |z| ≥ 3 in 1,052 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +1.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +1.1 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.5 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -8.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.3 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -2.1 | -6.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.8 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -7.2 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:51,767,993-51,804,163 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13639, SDR40C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [A0PJE2](https://www.uniprot.org/uniprotkb/A0PJE2) (Dehydrogenase/reductase SDR family member 12):

> Putative oxidoreductase.

**Summary**, from NCBI Gene [79758](https://www.ncbi.nlm.nih.gov/gene/79758):

> This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family, which has over 46,000 members. Members in this family are enzymes that metabolize many different compounds, such as steroid hormones, prostaglandins, retinoids, lipids and xenobiotics. Alternative splicing results in multiple transcript variants and protein isoforms. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:25832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25832) · Entrez [79758](https://www.ncbi.nlm.nih.gov/gene/79758) · UniProt [A0PJE2](https://www.uniprot.org/uniprotkb/A0PJE2) · Ensembl [ENSG00000102796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102796)

## Data

Gene col 2273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2273); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2273]; `tensor/DDL_lfc|DDL_z.npy` [2273]; `embed/gene_vectors.npy` [2273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2273 or target_col == 2273). Every well: [[DHRS12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
