---
symbol: "NXPE3"
type: "gene"
col: 6931
ensembl_id: "ENSG00000144815"
name: "neurexophilin and PC-esterase domain family member 3"
location: "3q12.3"
module: 57
arm: "+"
pooled_cpm: 15.77
n_lines_expressing: 45
n_dd_up: 35
n_dd_down: 11
n_dd_up_clean: 30
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# NXPE3

*neurexophilin and PC-esterase domain family member 3* — 3q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.61× (z +17.4, q 0e+00, up in 39 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.463× (z -14.0, q 6e-42, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSD17B4]] (+0.73, fdr 7e-06), [[GNPDA2]] (+0.71, fdr 7e-06), [[RAD23B]] (+0.69, fdr 1e-05); moves opposite to [[PDCD7]] (-0.62, fdr 5e-05), [[EP300]] (-0.58, fdr 1e-05), [[HELQ]] (-0.57, fdr 6e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MAP1B]] → it (grade B ⚠); 2 go from it, the strongest it → [[GPX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.61×** | +17.4 | 0e+00 | 39/43 (NCI-H2347, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.58×** | +17.2 | 0e+00 | 41/43 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.57×** | +17.2 | 0e+00 | 32/42 (HOP62, NCI-H460, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.57×** | +17.2 | 0e+00 | 39/42 (NCI-H2347, LoVo, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +16.4 | 0e+00 | 39/42 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +15.9 | 0e+00 | 40/43 (HT-29, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.28×** | +14.2 | 1e-43 | 31/43 (NCI-H460, A498, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.15×** | +13.9 | 6e-42 | 29/42 (HOP62, A498, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.06×** | +13.1 | 1e-37 | 37/42 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.91×** | +11.7 | 5e-30 | 23/32 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +11.4 | 3e-28 | 38/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.80×** | +10.3 | 4e-23 | 17/24 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +9.9 | 3e-21 | 33/43 (NCI-H2347, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +7.3 | 8e-12 | 23/42 (HOP62, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +6.8 | 5e-10 | 23/43 (RKO, J82, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.43×** | +6.2 | 2e-08 | 19/42 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.34×** | +5.3 | 4e-06 | 9/43 (NCI-H2347, SK-MEL-2, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.463×** | -14.0 | 6e-42 | 35/43 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.496×** | -12.8 | 6e-35 | 30/40 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.606×** | -9.1 | 1e-17 | 30/42 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.616×** | -8.8 | 1e-16 | 27/42 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.693×** | -6.7 | 3e-09 | 17/42 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.768×** | -4.8 | 1e-04 | 13/42 (C-33 A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.805×** | -4.0 | 0.006 | 17/42 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.681×** | -3.7 | 0.016 | 9/41 (PANC-1, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.7 | 0.016 | 4/43 (CHP-212, HepG2/C3A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.828×** | -3.5 | 0.029 | 11/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.880× | -3.3 | 0.047 | 14/42 (A-427, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.830×** | -3.3 | 0.049 | 8/42 (A-172, NCI-H23, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.826×** | -3.2 | 0.052 | 12/42 (SW48, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | 0.841× | -3.2 | 0.060 | 8/40 (H4, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 31.3 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.265× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.277× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 19.7 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 4.45× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.293× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.310× (z -9.5) |
| [[A-172 (line)]] | wt | 25.2 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.05× (z +10.5) | — |
| [[A-427 (line)]] | wt | 34.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 38.9 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.89× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 14.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.69× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 30.0 | 1 | 2 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.10× (z +9.0) | [[Pimitespib (drug)]] 5 µM 0.0749× (z -9.2) |
| [[HOP62 (line)]] | alt | 14.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.32× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 32.1 | 1 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 2.94× (z +8.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.344× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 14.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.22× (z +9.2) | — |
| [[LoVo (line)]] | wt | 7.33 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.23× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 21.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.253× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -16.0) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 25.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.81× (z +9.4) | — |
| [[C-33 A (line)]] | alt | 15.0 | 0 | 1 | — | [[Decitabine (drug)]] 0.05 µM 0.112× (z -9.9) |
| [[C32 (line)]] | wt | 9.63 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 9.60× (z +9.7) | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0757× (z -12.5) |
| [[HT-29 (line)]] | alt | 6.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.58× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 3.98 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0894× (z -8.7) ⚠ toxic |
| [[RKO (line)]] | wt | 27.5 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.59× (z +9.0) ⚠ cell-cycle shift, explains ~60% of this change | — |
| [[A549 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.20 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.04 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSD17B4]] | +0.73 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[GNPDA2]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[RAD23B]] | +0.69 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[GSR]] | +0.69 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZNF483]] | +0.68 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[NDRG3]] | +0.68 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[BLMH]] | +0.67 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CAMK2G]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TALDO1]] | +0.66 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[STARD3NL]] | +0.65 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ASAP3]] | +0.64 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[PHKB]] | +0.64 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDCD7]] | -0.62 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[EP300]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[HELQ]] | -0.57 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[LINS1]] | -0.55 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[RSPRY1]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ANKRD17-DT]] | -0.54 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[WNK4]] | -0.53 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[TNRC6C]] | -0.53 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[IBA57]] | -0.53 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[UNK]] | -0.53 | -0.41 / -0.46 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP1B]] | B | MAP1B activity raises NXPE3's level | lines that do not express MAP1B (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without MAP1B | 0.021 | ⚠ within organs, on part of the lines; also absent: MPDZ, GNB4, EVL |
| [[TTLL7]] | B | TTLL7 activity raises NXPE3's level | lines that do not express TTLL7 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without TTLL7 | 0.051 | ⚠ within organs, on part of the lines; also absent: BEND6, CFAP54, LINC01725 |
| [[ASAP3]] | B | ASAP3 activity raises NXPE3's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 3.73× lower at baseline in the lines without ASAP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[ANXA6]] | B | ANXA6 activity raises NXPE3's level | lines that do not express ANXA6 (8) vs lines expressing it (42) | 2.17× lower at baseline in the lines without ANXA6 | 0.060 | ⚠ within organs, on part of the lines; also absent: KATNAL1, PHC1, FAM171A1 |
| [[KIF3C]] | B | KIF3C activity raises NXPE3's level | lines that do not express KIF3C (5) vs lines expressing it (45) | 2.59× lower at baseline in the lines without KIF3C | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00888, WNT3, TBKBP1; its own permutation p |
| [[SOGA3]] | B | SOGA3 activity raises NXPE3's level | lines that do not express SOGA3 (21) vs lines expressing it (29) | 2.18× lower at baseline in the lines without SOGA3 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: KIAA0408, ENSG00000255330, RFTN1 |
| [[FAM171B]] | C | FAM171B activity raises NXPE3's level | lines that do not express FAM171B (7) vs lines expressing it (43) | 3.59× lower at baseline in the lines without FAM171B | 0.033 | ⚠ within organs, on part of the lines; also absent: NXPE3, GXYLT2, TMOD2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPX3]] | B | NXPE3 activity raises GPX3's level | lines that do not express NXPE3 (5) vs lines expressing it (45) | 3.34× lower at baseline in the lines without NXPE3 | 0.096 | ⚠ within organs, on part of the lines; also absent: FAM171B, TTC23L, LCA5; maybe low, not absent |
| [[PFN2]] | C | NXPE3 activity raises PFN2's level | lines that do not express NXPE3 (5) vs lines expressing it (45) | 3.65× lower at baseline in the lines without NXPE3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FAM171B, TTC23L, LCA5; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.2, -7.7); signed map (-28.0, -21.7). **Vector** length 88.2, 18.9% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.0 | +13.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.9 | +14.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +17.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +15.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +13.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +9.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +7.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +3.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.8 | -3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -6.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.0 | -8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | +4.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.0 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | neurexophilin and PC-esterase domain family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.3 — chr3:101,779,177-101,843,743 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15606; previously FAM55C |
| Gene groups (HGNC) | Neurexophilin and PC-esterase domain containing |
| Matched by | ensembl_id |

UniProt [Q969Y0](https://www.uniprot.org/uniprotkb/Q969Y0) carries no function annotation.

**Summary**, from NCBI Gene [91775](https://www.ncbi.nlm.nih.gov/gene/91775):

> This gene encodes a member of the neurexophilin family of neuropeptide-like glycoproteins. The encoded protein contains a variable N-terminal domain, a highly conserved neurexophilin and PC-esterase (NXPE) central domain, a short linker region, and a cysteine-rich C-terminal domain. This protein binds alpha neurexins, a group of presynaptic transmembrane receptors that promote adhesion between dendrites and axons. Alternative splicing results in multiple transcript variants. [provided by …

**Accessions** — [HGNC:28238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28238) · Entrez [91775](https://www.ncbi.nlm.nih.gov/gene/91775) · UniProt [Q969Y0](https://www.uniprot.org/uniprotkb/Q969Y0) · Ensembl [ENSG00000144815](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144815)

## Data

Gene col 6931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6931); `tables/drug_effects.parquet` (66 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6931]; `tensor/DDL_lfc|DDL_z.npy` [6931]; `embed/gene_vectors.npy` [6931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6931 or target_col == 6931). Every well: [[NXPE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NXPE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
