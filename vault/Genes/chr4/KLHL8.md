---
symbol: "KLHL8"
type: "gene"
col: 6975
ensembl_id: "ENSG00000145332"
name: "kelch like family member 8"
location: "4q22.1"
module: 10
arm: "-"
pooled_cpm: 40.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# KLHL8

*kelch like family member 8* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.72× (z +12.1, q 4e-31, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.386× (z -11.2, q 1e-26, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GLMN]] (+0.69, fdr 7e-06), [[NCK1]] (+0.64, fdr 3e-05), [[ASB13]] (+0.64, fdr 1e-05); moves opposite to [[PDCL3P4]] (-0.67, fdr 1e-05), [[PRECSIT]] (-0.65, fdr 1e-05), [[RAP2C-AS1]] (-0.64, fdr 3e-05).
> It sits in the **-** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FGD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +12.1 | 4e-31 | 43/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +11.9 | 3e-30 | 40/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +11.7 | 2e-29 | 37/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +10.8 | 6e-25 | 38/48 (A498, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +9.1 | 1e-17 | 40/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +7.4 | 1e-11 | 34/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +7.1 | 1e-10 | 29/48 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +7.0 | 2e-10 | 31/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.31×** | +6.0 | 2e-07 | 26/46 (LOX-IMVI, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.26×** | +5.3 | 8e-06 | 22/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.010 | 17/48 (CFPAC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.7 | 0.011 | 13/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.015 | 16/48 (A498, H4, …) | inconsistent across doses |  |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.17× | +3.5 | 0.021 | 8/48 (RKO, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.035 | 6/48 (SW480, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.15× | +3.2 | 0.057 | 9/48 (H4, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -11.2 | 1e-26 | 40/49 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.708×** | -11.0 | 8e-26 | 32/48 (LoVo, A498, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.633×** | -9.6 | 2e-19 | 29/45 (A-427, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.716×** | -7.2 | 6e-11 | 26/47 (PANC-1, SHP-77, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.742×** | -6.5 | 1e-08 | 25/48 (A498, AN3 CA, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.639×** | -5.3 | 1e-05 | 21/48 (A-172, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.818×** | -4.4 | 7e-04 | 24/48 (AN3 CA, A498, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.883× | -4.0 | 0.006 | 15/48 (SNU-1, A498, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.849× | -3.5 | 0.026 | 14/48 (PANC-1, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.857× | -3.5 | 0.029 | 16/48 (RKO, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.858× | -3.5 | 0.029 | 23/47 (C-33 A, SHP-77, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.862× | -3.3 | 0.039 | 19/48 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Gefitinib (drug)]] 5 µM |  | 0.863× | -3.3 | 0.041 | 8/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.862× | -3.2 | 0.056 | 8/48 (C32, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 0.869× | -3.1 | 0.063 | 14/47 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | 0.908× | -3.0 | 0.084 | 9/48 (SW 1088, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.8 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.362× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.201× (z -9.9) |
| [[A498 (line)]] | wt | 51.4 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -16.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.223× (z -8.7) |
| [[LoVo (line)]] | wt | 58.8 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.95× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -17.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.276× (z -8.8) |
| [[PANC-1 (line)]] | alt | 40.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -17.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 83.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.366× (z -10.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 69.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -22.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 26.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.24× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -16.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 58.3 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.342× (z -10.4) |
| [[SW48 (line)]] | wt | 44.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -12.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.142× (z -9.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[C-33 A (line)]] | alt | 80.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 16.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.20× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 58.7 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.0579× (z -13.6) |
| [[A-172 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 59.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GLMN]] | +0.69 | +0.62 / +0.65 | both halves | 7e-06 | STRING 720 |
| [[NCK1]] | +0.64 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[ASB13]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[L2HGDH]] | +0.63 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[SFXN4]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[FAM118A]] | +0.62 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[FBXL4]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[FAM24B]] | +0.61 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[SLC35A1]] | +0.60 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[GPR89A]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[MCOLN2]] | +0.59 | +0.42 / +0.60 | both halves | 4e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCL3P4]] | -0.67 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PRECSIT]] | -0.65 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[RAP2C-AS1]] | -0.64 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[RNF32]] | -0.62 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[EFCAB6]] | -0.62 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[FAM120AOS]] | -0.62 | -0.53 / -0.37 | both halves | 9e-05 |  |
| [[HIVEP2-DT]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[CTBP1-DT]] | -0.60 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CAPN3]] | -0.60 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[GPR137]] | -0.60 | -0.52 / -0.40 | both halves | 5e-05 |  |
| [[TMEM232]] | -0.60 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[AK8]] | -0.59 | -0.46 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD1]] | B | FGD1 activity raises KLHL8's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.18× lower at baseline in the lines without FGD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[MCOLN2]] | B | MCOLN2 activity raises KLHL8's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.26× lower at baseline in the lines without MCOLN2 | 0.050 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers KLHL8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers KLHL8's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ARHGEF26]] | C | ARHGEF26 activity raises KLHL8's level | lines that do not express ARHGEF26 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without ARHGEF26 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ERO1B, RHOQ, DPF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.622). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (15.9, 13.6); signed map (-38.9, -19.0). **Vector** length 95.7, 22.0% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.3 | +5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +9.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +7.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +2.2 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.3 | -11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.7 | -9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.3 | -4.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -4.5 | -3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.0 | -2.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:87,160,103-87,240,314 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1378 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2G9](https://www.uniprot.org/uniprotkb/Q9P2G9) (Kelch-like protein 8):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex required for The BCR(KLHL8) ubiquitin ligase complex mediates ubiquitination and degradation of RAPSN.

**Summary**, from NCBI Gene [57563](https://www.ncbi.nlm.nih.gov/gene/57563):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Involved in protein ubiquitination and ubiquitin-dependent protein catabolic process. Located in nucleoplasm. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18644](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18644) · Entrez [57563](https://www.ncbi.nlm.nih.gov/gene/57563) · UniProt [Q9P2G9](https://www.uniprot.org/uniprotkb/Q9P2G9) · Ensembl [ENSG00000145332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145332)

## Data

Gene col 6975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6975); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6975]; `tensor/DDL_lfc|DDL_z.npy` [6975]; `embed/gene_vectors.npy` [6975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6975 or target_col == 6975). Every well: [[KLHL8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
