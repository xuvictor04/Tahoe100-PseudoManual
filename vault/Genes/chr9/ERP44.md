---
symbol: "ERP44"
type: "gene"
col: 343
ensembl_id: "ENSG00000023318"
name: "endoplasmic reticulum protein 44"
location: "9q31.1"
module: 42
arm: "+"
pooled_cpm: 107.68
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 4
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# ERP44

*endoplasmic reticulum protein 44* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.42× (z +21.9, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.752× (z -6.8, q 7e-09, down in 33 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.821× (z -4.9, q 3e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEL1L]] (+0.76, fdr 7e-06), [[HSPA5]] (+0.69, fdr 7e-06), [[CLINT1]] (+0.67, fdr 7e-06); moves opposite to [[ANKRD18A]] (-0.58, fdr 5e-05), [[NOP56]] (-0.56, fdr 1e-05), [[PNRC2]] (-0.54, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 343.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +21.9 | 0e+00 | 48/48 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +18.7 | 0e+00 | 47/48 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.02×** | +17.5 | 0e+00 | 46/48 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +13.8 | 6e-41 | 47/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +11.3 | 2e-27 | 40/48 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.48×** | +9.7 | 2e-20 | 39/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.45×** | +8.8 | 2e-16 | 40/48 (LOX-IMVI, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.31×** | +6.7 | 2e-09 | 34/48 (LOX-IMVI, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +6.4 | 1e-08 | 33/48 (HOP62, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +5.0 | 3e-05 | 24/48 (HOP62, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 26/49 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.3 | 7e-04 | 20/48 (NCI-H23, SW480, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.030 | 14/49 (A-427, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.3 | 0.037 | 13/48 (NCI-H1792, SW480, …) | inconsistent across doses | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.15× | +3.2 | 0.047 | 16/48 (AsPC-1, Hs 766T, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | 1.14× | +3.2 | 0.055 | 16/48 (SHP-77, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 343.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.752×** | -6.8 | 7e-09 | 33/47 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.821×** | -4.9 | 3e-04 | 24/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.849× | -4.1 | 0.009 | 18/48 (A-172, KATO III, …) | all doses, flat |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.800×** | -3.8 | 0.019 | 18/48 (A-427, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.862× | -3.7 | 0.028 | 16/48 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.859× | -3.5 | 0.047 | 15/47 (A-172, AsPC-1, …) | all doses, flat | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | 0.870× | -3.4 | 0.047 | 12/48 (LoVo, COLO 205, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.823×** | -3.3 | 0.061 | 19/48 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | 0.878× | -3.2 | 0.080 | 16/48 (A-172, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | 0.881× | -3.1 | 0.10 | 13/48 (RPMI-7951, SW 1088, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | 0.879× | -3.1 | 0.11 | 17/44 (C-33 A, SW48, …) | all doses, flat | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 343. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 94.6 | 7 | 0 | [[Panobinostat (drug)]] 5 µM 3.43× (z +17.5) | — |
| [[RKO (line)]] | wt | 212 | 5 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.30× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.0565× (z -37.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[MIA PaCa-2 (line)]] | alt | 106 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.59× (z +15.5) | — |
| [[PANC-1 (line)]] | alt | 65.9 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.53× (z +14.5) | — |
| [[HOP62 (line)]] | alt | 75.6 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +16.5) | — |
| [[SW480 (line)]] | alt | 131 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +15.1) | — |
| [[A-172 (line)]] | wt | 157 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.46× (z +13.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.3) ⚠ cell-cycle shift, explains ~93% of this change |
| [[C-33 A (line)]] | alt | 63.6 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.10× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.220× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H23 (line)]] | alt | 78.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +12.5) | — |
| [[NCI-H460 (line)]] | wt | 125 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.66× (z +14.0) | — |
| [[SK-MEL-2 (line)]] | alt | 94.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[A498 (line)]] | wt | 116 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +12.5) | — |
| [[A549 (line)]] | wt | 90.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +13.0) | — |
| [[AsPC-1 (line)]] | alt | 92.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +11.6) | — |
| [[BT-474 (line)]] | alt | 75.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.45× (z +10.1) | — |
| [[C32 (line)]] | wt | 96.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.18× (z +8.9) | — |
| [[HEC-1-A (line)]] | alt | 109 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 143 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 95.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.70× (z +10.2) | — |
| [[KATO III (line)]] | alt | 222 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.446× (z -10.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 58.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 106 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +16.7) | — |
| [[A-427 (line)]] | wt | 50.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.14× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 84.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +11.0) | — |
| [[LoVo (line)]] | wt | 105 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 1.99× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 81.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.36× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 119 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.55× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 153 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.05× (z +9.5) | — |
| [[SW48 (line)]] | wt | 98.3 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[AN3 CA (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0911× (z -11.3) ⚠ toxic |
| [[H4 (line)]] | wt | 118 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +8.7) | — |
| [[J82 (line)]] | alt | 163 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.78× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 77.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.89× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 103 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +9.7) | — |
| [[SNU-1 (line)]] | wt | 81.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +10.8) | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 1 | — | [[Tetracycline (hydrochloride) (drug)]] 0.05 µM 0.0872× (z -9.5) |
| [[SW1417 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.477× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[CFPAC-1 (line)]] | alt | 63.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 90.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 84.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 93.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 343), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEL1L]] | +0.76 | +0.69 / +0.73 | both halves | 7e-06 | STRING 402 |
| [[HSPA5]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 | STRING 682 |
| [[CLINT1]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TM9SF2]] | +0.66 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[DNAJC3]] | +0.65 | +0.67 / +0.66 | both halves | 7e-06 | STRING 628 |
| [[RAB2A]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CALR]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 | STRING 744 |
| [[PDIA4]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 | same gene group; STRING 474 |
| [[SEC63]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 | STRING 454 |
| [[SLC35A3]] | +0.63 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[DNAJB11]] | +0.63 | +0.68 / +0.62 | both halves | 7e-06 | STRING 855 |
| [[HSP90B1]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 | STRING 556 |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.58 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[NOP56]] | -0.56 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ZCCHC3]] | -0.54 | -0.40 / -0.44 | both halves | 5e-05 |  |
| [[ST7L]] | -0.53 | -0.46 / -0.26 | both halves | 4e-04 |  |
| [[ZBTB2]] | -0.52 | -0.36 / -0.28 | both halves | 3e-04 |  |
| [[UNK]] | -0.51 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[PTGR3]] | -0.51 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[ZC3H7B]] | -0.51 | -0.55 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers ERP44's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers ERP44's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SEL1L]] | C | SEL1L's natural level weakens ERP44's drug response | SEL1L's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.08; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.8, -30.9); signed map (-54.2, 7.5). **Vector** length 111, 32.0% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.61 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.55 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.54 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.9 | +13.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.9 | +17.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.7 | +18.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.7 | +21.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +11.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +6.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +4.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.6 | -6.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -5.9 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -5.6 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.2 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | endoplasmic reticulum protein 44 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:99,979,185-100,099,052 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0573, PDIA10; previously TXNDC4 |
| Gene groups (HGNC) | Protein disulfide isomerases; Thioredoxin domain containing |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BS26](https://www.uniprot.org/uniprotkb/Q9BS26) (Endoplasmic reticulum resident protein 44):

> Mediates thiol-dependent retention in the early secretory pathway, forming mixed disulfides with substrate proteins through its conserved CRFS motif. Inhibits the calcium channel activity of ITPR1. May have a role in the control of oxidative protein folding in the endoplasmic reticulum. Required to retain ERO1A and ERO1B in the endoplasmic reticulum.

**Summary**, from NCBI Gene [23071](https://www.ncbi.nlm.nih.gov/gene/23071):

> This gene encodes a member of the protein disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins. It has an inferred N-terminal signal peptide, a catalytically active thioredoxin (TRX) domain, two TRX-like domains and a C-terminal ER-retention sequence. This protein functions as a pH-regulated chaperone of the secretory pathway and likely plays a role in protein quality control at the endoplasmic reticulum - Golgi interface. [provided by RefSeq, Dec 2016]

**Accessions** — [HGNC:18311](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18311) · Entrez [23071](https://www.ncbi.nlm.nih.gov/gene/23071) · UniProt [Q9BS26](https://www.uniprot.org/uniprotkb/Q9BS26) · Ensembl [ENSG00000023318](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023318)

## Data

Gene col 343: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 343); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 343, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 343]; `tensor/DDL_lfc|DDL_z.npy` [343]; `embed/gene_vectors.npy` [343]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 343 or target_col == 343). Every well: [[ERP44 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ERP44.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
