---
symbol: "STXBP6"
type: "gene"
col: 9730
ensembl_id: "ENSG00000168952"
name: "syntaxin binding protein 6"
location: "14q12"
module: 55
arm: "+"
pooled_cpm: 24.8
n_lines_expressing: 28
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 10
direction_downstream: 12
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# STXBP6

*syntaxin binding protein 6* — 14q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.87× (z +14.4, q 3e-44, up in 17 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.510× (z -11.0, q 2e-25, down in 19 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC27A2]] (+0.60, fdr 2e-05), [[CADPS]] (+0.59, fdr 3e-05), [[LYPD6]] (+0.57, fdr 2e-05); moves opposite to [[SOS2]] (-0.55, fdr 1e-05), [[OSMR-DT]] (-0.49, fdr 9e-05), [[RSPH9]] (-0.47, fdr 1e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[EDAR]] → it (grade B ⚠); 12 go from it, the strongest it → [[ONECUT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +14.4 | 3e-44 | 17/26 (SW480, BT-474, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.78×** | +9.5 | 8e-19 | 15/25 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.78×** | +9.4 | 8e-19 | 13/26 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +8.3 | 1e-14 | 17/26 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +6.0 | 3e-07 | 13/26 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.40×** | +5.5 | 4e-06 | 10/26 (SK-MEL-2, NCI-H23, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.74×** | +4.7 | 2e-04 | 9/26 (LS 180, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.016 | 7/25 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.22×** | +3.6 | 0.017 | 6/25 (NCI-H460, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.23×** | +3.4 | 0.042 | 3/23 (J82, SHP-77, …) | inconsistent across doses | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | 1.21× | +3.1 | 0.10 | 5/26 (HepG2/C3A, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.510×** | -11.0 | 2e-25 | 19/26 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.572×** | -9.1 | 2e-17 | 19/25 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.609×** | -8.1 | 9e-14 | 17/25 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.610×** | -7.8 | 1e-12 | 20/25 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.672×** | -6.5 | 9e-09 | 18/25 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.681×** | -6.3 | 3e-08 | 20/25 (LoVo, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -4.9 | 7e-05 | 15/26 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.769×** | -4.3 | 0.001 | 9/25 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.781×** | -4.0 | 0.003 | 8/26 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.784×** | -4.0 | 0.004 | 9/25 (HT-29, LS 180, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.856× | -3.6 | 0.016 | 10/25 (KATO III, HT-29, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.865× | -3.4 | 0.037 | 9/26 (KATO III, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.823×** | -3.2 | 0.060 | 12/26 (LS 180, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.824×** | -3.2 | 0.060 | 7/26 (SW 1271, LS 180, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 64.6 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.214× (z -15.2) |
| [[C32 (line)]] | wt | 88.2 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0928× (z -24.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 47.8 | 1 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.5× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.279× (z -11.4) |
| [[SNU-1 (line)]] | wt | 111 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0788× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0877× (z -9.2) |
| [[SW1417 (line)]] | alt | 78.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 28.2 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.08× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.294× (z -11.9) |
| [[BT-474 (line)]] | alt | 13.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 5.04× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 52.1 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.149× (z -14.6) |
| [[A498 (line)]] | wt | 28.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0848× (z -25.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 69.6 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 93.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.331× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.381× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 21.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.31× (z +10.0) | — |
| [[SW48 (line)]] | wt | 86.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.154× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -9.7) |
| [[H4 (line)]] | wt | 38.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 34.0 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 43.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 41.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0768× (z -18.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -10.5) ⚠ toxic |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.223× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.88× (z +9.4) | — |
| [[A-172 (line)]] | wt | 6.54 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.93 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.98 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.86 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.69 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.75 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.16 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC27A2]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CADPS]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[LYPD6]] | +0.57 | +0.46 / +0.58 | both halves | 2e-05 |  |
| [[PIWIL1]] | +0.57 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SLC52A3]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[SKAP1]] | +0.56 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[LINC02331]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[LINC02832]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[EDAR]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LINC01819]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ILDR2]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[PIK3AP1]] | +0.52 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOS2]] | -0.55 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[OSMR-DT]] | -0.49 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[RSPH9]] | -0.47 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[FGF11]] | -0.46 | -0.44 / -0.35 | both halves | 1e-04 |  |
| [[L3MBTL1]] | -0.45 | -0.38 / -0.37 | both halves | 7e-05 |  |
| [[TNXB]] | -0.45 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[MAFG]] | -0.44 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[FKBP14-AS1]] | -0.44 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[ZNF418]] | -0.44 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[DUSP28]] | -0.44 | -0.17 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[C1orf54]] | -0.43 | -0.25 / -0.42 | both halves | 4e-04 |  |
| [[CYP27C1]] | -0.43 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[FAM229A]] | -0.43 | -0.41 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EDAR]] | B | EDAR activity raises STXBP6's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without EDAR | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[SLC27A2]] | B | SLC27A2 activity raises STXBP6's level | lines that do not express SLC27A2 (19) vs lines expressing it (31) | 1.61× lower at baseline in the lines without SLC27A2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ICA1, BTC, ENSG00000288656 |
| [[LYPD6]] | B | LYPD6 activity raises STXBP6's level | lines that do not express LYPD6 (15) vs lines expressing it (35) | 2.69× lower at baseline in the lines without LYPD6 | 0.092 | ⚠ within organs, on part of the lines; also absent: LYPD6B, JPH1, NRN1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers STXBP6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers STXBP6's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02331]] | C | LINC02331 activity raises STXBP6's level | lines that do not express LINC02331 (30) vs lines expressing it (20) | 2.70× lower at baseline in the lines without LINC02331 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPS8L3, LCN2; co-absent with the target |
| [[HEPH]] | C | HEPH activity raises STXBP6's level | lines that do not express HEPH (41) vs lines expressing it (9) | 4.86× lower at baseline in the lines without HEPH | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4; co-absent with the target |
| [[IGFL2]] | C | IGFL2 activity raises STXBP6's level | lines that do not express IGFL2 (38) vs lines expressing it (12) | 2.81× lower at baseline in the lines without IGFL2 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, REG4, GPA33; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises STXBP6's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without HNF4A | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[USH1C]] | C | USH1C activity raises STXBP6's level | lines that do not express USH1C (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without USH1C | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ONECUT2]] | B | STXBP6 activity raises ONECUT2's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.35× lower at baseline in the lines without STXBP6 | 0.015 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[MCF2L]] | B | STXBP6 activity raises MCF2L's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without STXBP6 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[RAPGEF5]] | B | STXBP6 activity raises RAPGEF5's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without STXBP6 | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[FGFR4]] | B | STXBP6 activity raises FGFR4's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without STXBP6 | 0.062 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[HADH]] | B | STXBP6 activity raises HADH's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.30× lower at baseline in the lines without STXBP6 | 0.070 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[ARHGAP8]] | B | STXBP6 activity raises ARHGAP8's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.99× lower at baseline in the lines without STXBP6 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[UNC5A]] | B | STXBP6 activity raises UNC5A's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without STXBP6 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[AXIN2]] | B | STXBP6 activity raises AXIN2's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.52× lower at baseline in the lines without STXBP6 | 0.093 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[MPP7]] | C | STXBP6 activity raises MPP7's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.50× lower at baseline in the lines without STXBP6 | 0.013 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748; co-absent with the target |
| [[TMEM139]] | C | STXBP6 activity raises TMEM139's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.84× lower at baseline in the lines without STXBP6 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748; co-absent with the target |
| [[PROM1]] | C | STXBP6 activity raises PROM1's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.17× lower at baseline in the lines without STXBP6 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748; co-absent with the target |
| [[LINC00923]] | C | STXBP6 activity raises LINC00923's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 2.57× lower at baseline in the lines without STXBP6 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.494). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.3, 47.4); signed map (65.0, 11.8). **Vector** length 77.3, 19.3% of its response variance represented; |z| ≥ 3 in 785 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +2.8 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.5 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | -2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.0 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -6.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | syntaxin binding protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,809,454-25,050,147 (-) |
| Ensembl biotype | protein_coding |
| Also known as | amisyn, HSPC156 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NFX7](https://www.uniprot.org/uniprotkb/Q8NFX7) (Syntaxin-binding protein 6):

> Forms non-fusogenic complexes with SNAP25 and STX1A and may thereby modulate the formation of functional SNARE complexes and exocytosis.

**Summary**, from NCBI Gene [29091](https://www.ncbi.nlm.nih.gov/gene/29091):

> Enables cadherin binding activity involved in cell-cell adhesion. Predicted to be involved in negative regulation of exocytosis. Located in adherens junction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19666) · Entrez [29091](https://www.ncbi.nlm.nih.gov/gene/29091) · UniProt [Q8NFX7](https://www.uniprot.org/uniprotkb/Q8NFX7) · Ensembl [ENSG00000168952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168952)

## Data

Gene col 9730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9730); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9730]; `tensor/DDL_lfc|DDL_z.npy` [9730]; `embed/gene_vectors.npy` [9730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9730 or target_col == 9730). Every well: [[STXBP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STXBP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
