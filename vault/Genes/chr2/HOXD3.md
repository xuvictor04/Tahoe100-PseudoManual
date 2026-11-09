---
symbol: "HOXD3"
type: "gene"
col: 4908
ensembl_id: "ENSG00000128652"
name: "homeobox D3"
location: "2q31.1"
module: 46
arm: "+"
pooled_cpm: 6.13
n_lines_expressing: 33
n_dd_up: 17
n_dd_down: 21
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOXD3

*homeobox D3* — 2q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +11.0, q 3e-25, up in 17 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.277× (z -16.7, q 0e+00, down in 27 of 30 measured lines).
> Its strongest partners by |cos| (72 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 29 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATF5]] (+0.68, fdr 3e-05), [[ZBED3]] (+0.65, fdr 3e-05), [[ZIC1]] (+0.61, fdr 4e-05); moves opposite to [[TGM2]] (-0.54, fdr 5e-05), [[SCART1]] (-0.54, fdr 1e-04), [[ABHD2]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[UNC5C]] → it (grade B ⚠); 3 go from it, the strongest it → [[UNC5C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +11.0 | 3e-25 | 17/26 (A498, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.55×** | +8.0 | 3e-13 | 16/31 (C32, A-172, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.54×** | +5.6 | 3e-06 | 13/30 (HCT15, H4, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.6 | 4e-04 | 8/22 (J82, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 4e-04 | 5/28 (C32, A498, …) | two highest doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +4.6 | 4e-04 | 9/30 (C32, A-172, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.27×** | +4.4 | 9e-04 | 11/31 (LoVo, HCT15, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.002 | 8/31 (SW48, HCT15, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.040 | 7/30 (LoVo, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.31×** | +3.4 | 0.044 | 7/30 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.31×** | +3.3 | 0.051 | 4/31 (C32, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.056 | 7/28 (C32, A-172, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.056 | 4/31 (A-427, SHP-77, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.056 | 3/30 (LoVo, C32, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.056 | 5/31 (C32, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.090 | 3/30 (C32, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.090 | 2/28 (LoVo, RPMI-7951) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.277×** | -16.7 | 0e+00 | 27/30 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.355×** | -13.1 | 8e-37 | 24/29 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.381×** | -12.5 | 1e-33 | 23/30 (PANC-1, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.580×** | -6.9 | 7e-10 | 12/29 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **0.599×** | -6.6 | 4e-09 | 13/25 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.648×** | -5.6 | 2e-06 | 14/30 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.667×** | -5.2 | 1e-05 | 12/16 (C32, A-172, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.680×** | -5.0 | 4e-05 | 11/30 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.692×** | -4.8 | 1e-04 | 13/30 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.706×** | -4.4 | 6e-04 | 10/29 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.555×** | -4.0 | 0.003 | 10/29 (LOX-IMVI, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.741×** | -3.7 | 0.009 | 6/30 (NCI-H1573, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.763×** | -3.5 | 0.020 | 8/31 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.764×** | -3.5 | 0.020 | 5/29 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.602×** | -3.4 | 0.022 | 11/24 (NCI-H23, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.773×** | -3.3 | 0.037 | 8/29 (HEC-1-A, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.847× | -3.0 | 0.079 | 6/30 (C32, HEC-1-A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.793×** | -3.0 | 0.079 | 4/29 (COLO 205, SK-MEL-2, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.794×** | -3.0 | 0.081 | 8/30 (HEC-1-A, RKO, …) | top dose only |  |
| [[Fluvoxamine (maleate) (drug)]] 0.05 µM |  | **0.799×** | -2.9 | 0.098 | 6/29 (SW1417, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 77.2 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0923× (z -11.4) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.133× (z -9.7) |
| [[PANC-1 (line)]] | alt | 9.53 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.137× (z -11.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.163× (z -10.8) |
| [[A-172 (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.110× (z -11.6) |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0627× (z -13.3) |
| [[HOP62 (line)]] | alt | 8.83 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0946× (z -13.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 21.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.168× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 8.16 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.135× (z -9.3) |
| [[A498 (line)]] | wt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.5) | — |
| [[C32 (line)]] | wt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0719× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 12.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RKO (line)]] | wt | 8.31 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0675× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0823× (z -8.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.596 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.492 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.515 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.915 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 27 of them with an alert (⚠; 26 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATF5]] | +0.68 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ZBED3]] | +0.65 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ZIC1]] | +0.61 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[TMEM268]] | +0.61 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[TSTD3]] | +0.61 | +0.36 / +0.39 | both halves | 1e-04 |  |
| [[HOXC6]] | +0.61 | +0.44 / +0.44 | both halves | 3e-05 | same gene group |
| [[SLC3A2]] | +0.61 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[TP53]] | +0.58 | +0.43 / +0.36 | both halves | 1e-04 |  |
| [[C7orf31]] | +0.58 | +0.41 / +0.41 | both halves | 4e-05 |  |
| [[ZFHX4-AS1]] | +0.58 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[SIAH1]] | +0.58 | +0.36 / +0.29 | both halves | 2e-04 |  |
| [[KLHL42]] | +0.55 | +0.39 / +0.24 | both halves | 4e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGM2]] | -0.54 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[SCART1]] | -0.54 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[ABHD2]] | -0.53 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[KANK2]] | -0.53 | -0.40 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[PCMT1]] | -0.52 | -0.25 / -0.30 | both halves | 4e-04 |  |
| [[AKAP13]] | -0.52 | -0.30 / -0.30 | both halves | 2e-04 |  |
| [[RALGAPA2]] | -0.51 | -0.32 / -0.19 | ⚠ not reproduced | 9e-04 |  |
| [[DIAPH1]] | -0.51 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[ADARB1]] | -0.50 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[NDFIP2]] | -0.49 | -0.34 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5C]] | B | UNC5C activity raises HOXD3's level | lines that do not express UNC5C (31) vs lines expressing it (19) | 2.27× lower at baseline in the lines without UNC5C | 0.027 | ⚠ within organs, on part of the lines; also absent: NTNG1, ZNF667, LAYN; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers HOXD3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UNC5C]] | B | HOXD3 activity raises UNC5C's level | lines that do not express HOXD3 (17) vs lines expressing it (33) | 2.86× lower at baseline in the lines without HOXD3 | 0.069 | ⚠ within organs, on part of the lines; also absent: PPFIA2, SCN8A, FGF14 |
| [[MAGI2-AS3]] | B | HOXD3 activity raises MAGI2-AS3's level | lines that do not express HOXD3 (17) vs lines expressing it (33) | 1.60× lower at baseline in the lines without HOXD3 | 0.088 | ⚠ within organs, on part of the lines; also absent: PPFIA2, SCN8A, FGF14 |
| [[KCNT2]] | C | HOXD3 activity raises KCNT2's level | lines that do not express HOXD3 (17) vs lines expressing it (33) | 3.04× lower at baseline in the lines without HOXD3 | 0.024 | ⚠ within organs, on part of the lines; also absent: PPFIA2, SCN8A, FGF14; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-14.2, 46.2); signed map (26.7, -16.1). **Vector** length 56.3, 10.3% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +11.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +4.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +2.9 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.5 | +0.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.2 | +1.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.2 | -12.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.1 | -16.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.0 | -13.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.8 | -4.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.5 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.0 | -0.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.9 | -3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | homeobox D3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.1 — chr2:176,136,612-176,173,102 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX4A, HOX4, HOX1D |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 2 pathways, smallest: Activation of HOX genes during differentiation; Activation of anterior HOX genes in hindbrain development during early embryogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P31249](https://www.uniprot.org/uniprotkb/P31249) (Homeobox protein Hox-D3):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3232](https://www.ncbi.nlm.nih.gov/gene/3232):

> This gene belongs to the homeobox family of genes. The homeobox genes encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, located on different chromosomes, consisting of 9 to 11 genes arranged in tandem. This gene is one of several homeobox HOXD genes located at 2q31-2q37 chromosome regions. Deletions that removed the entire HOXD gene …

**Accessions** — [HGNC:5137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5137) · Entrez [3232](https://www.ncbi.nlm.nih.gov/gene/3232) · UniProt [P31249](https://www.uniprot.org/uniprotkb/P31249) · Ensembl [ENSG00000128652](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128652)

## Data

Gene col 4908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4908); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4908]; `tensor/DDL_lfc|DDL_z.npy` [4908]; `embed/gene_vectors.npy` [4908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4908 or target_col == 4908). Every well: [[HOXD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
