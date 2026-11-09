---
symbol: "UNC5A"
type: "gene"
col: 3502
ensembl_id: "ENSG00000113763"
name: "unc-5 netrin receptor A"
location: "5q35.2"
module: 31
arm: "+"
pooled_cpm: 3.37
n_lines_expressing: 29
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 16
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 6
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# UNC5A

*unc-5 netrin receptor A* — 5q35.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.57× (z +16.3, q 0e+00, up in 21 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.518× (z -6.0, q 1e-06, down in 18 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP8]] (+0.65, fdr 1e-05), [[SLC5A1]] (+0.64, fdr 3e-05), [[SEMA4D]] (+0.64, fdr 1e-05); moves opposite to [[PUS10]] (-0.57, fdr 4e-05), [[TBCK]] (-0.56, fdr 5e-05), [[DNAI4]] (-0.53, fdr 1e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[OLFM1]] → it (grade B ⚠); 6 go from it, the strongest it → [[SBK1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3502.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.57×** | +16.3 | 0e+00 | 21/26 (LOX-IMVI, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **5.49×** | +15.4 | 0e+00 | 17/26 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.44×** | +15.3 | 0e+00 | 16/25 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.70×** | +11.8 | 4e-30 | 16/26 (A-172, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.40×** | +11.1 | 2e-26 | 21/26 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +10.6 | 2e-24 | 5/18 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.25×** | +10.2 | 1e-22 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.76×** | +9.2 | 4e-18 | 13/22 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.72×** | +8.0 | 6e-14 | 3/8 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.18×** | +7.0 | 1e-10 | 0/9 | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **2.06×** | +6.3 | 2e-08 | 2/12 (LoVo, SW480) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.75×** | +5.1 | 2e-05 | 10/26 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **2.82×** | +4.9 | 4e-05 | 2/23 (HEC-1-A, LOX-IMVI) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +4.6 | 2e-04 | 7/23 (HEC-1-A, SW48, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.006 | 5/17 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.015 | 1/26 (SW480) | two highest doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.66×** | +3.2 | 0.034 | 6/17 (SW48, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.035 | 0/19 | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **1.95×** | +3.1 | 0.039 | 3/11 (LoVo, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.60×** | +3.0 | 0.052 | 0/16 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3502.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.518×** | -6.0 | 1e-06 | 18/26 (LoVo, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.562×** | -5.0 | 1e-04 | 10/23 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.622×** | -4.3 | 0.003 | 9/23 (LoVo, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.667×** | -3.7 | 0.031 | 11/21 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.467×** | -3.6 | 0.033 | 13/22 (SW48, C-33 A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Lenalidomide (hemihydrate) (drug)]] 5 µM |  | 0.779× | -3.2 | 0.10 | 3/24 (HCT15, CFPAC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.702× | -3.2 | 0.10 | 5/26 (Panc 03.27, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3502. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 10.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0559× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 26.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0820× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -8.9) |
| [[SW1417 (line)]] | alt | 20.5 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 11.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -10.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 7.87 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.533 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.866 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.988 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.507 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.729 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.528 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.257 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.606 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.308 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.729 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.958 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3502), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP8]] | +0.65 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[SLC5A1]] | +0.64 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[SEMA4D]] | +0.64 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[CRYBG2]] | +0.59 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[CBLC]] | +0.58 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[RAPGEF5]] | +0.57 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[IGSF9]] | +0.56 | +0.47 / +0.49 | both halves | 2e-05 | same gene group |
| [[ENTREP2]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[AIF1L]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[EPHA2-AS1]] | +0.56 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[TMC6]] | +0.55 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[C1orf116]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS10]] | -0.57 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[TBCK]] | -0.56 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[DNAI4]] | -0.53 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[LMLN]] | -0.51 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[GALK2]] | -0.50 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[PRR4]] | -0.49 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.49 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[ASH1L]] | -0.49 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[EFCAB6]] | -0.48 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[PPP4R3B]] | -0.48 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[ATRX]] | -0.47 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[CFAP418-AS1]] | -0.47 | -0.30 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OLFM1]] | B | OLFM1 activity raises UNC5A's level | lines that do not express OLFM1 (27) vs lines expressing it (23) | 1.29× lower at baseline in the lines without OLFM1 | 0.029 | ⚠ within organs, on part of the lines; also absent: JPH3, DPYSL5, CHST8 |
| [[PGBD5]] | B | PGBD5 activity raises UNC5A's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 1.43× lower at baseline in the lines without PGBD5 | 0.068 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[STXBP6]] | B | STXBP6 activity raises UNC5A's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.58× lower at baseline in the lines without STXBP6 | 0.082 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[PIK3AP1]] | C | PIK3AP1 activity raises UNC5A's level | lines that do not express PIK3AP1 (28) vs lines expressing it (22) | 2.74× lower at baseline in the lines without PIK3AP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: HNF4A, EPS8L3, TMEM139; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SBK1]] | B | UNC5A activity raises SBK1's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 2.97× lower at baseline in the lines without UNC5A | 0.009 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[TMEM40]] | B | UNC5A activity raises TMEM40's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 1.39× lower at baseline in the lines without UNC5A | 0.046 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[RAP1GAP2]] | B | UNC5A activity raises RAP1GAP2's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 1.86× lower at baseline in the lines without UNC5A | 0.056 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[RAPGEF5]] | B | UNC5A activity raises RAPGEF5's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 2.33× lower at baseline in the lines without UNC5A | 0.078 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[OLFM1]] | B | UNC5A activity raises OLFM1's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without UNC5A | 0.086 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN |
| [[PIK3AP1]] | C | UNC5A activity raises PIK3AP1's level | lines that do not express UNC5A (21) vs lines expressing it (29) | 2.67× lower at baseline in the lines without UNC5A | 0.053 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, KCNK5, CGN; co-absent with the target |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.2, 46.9); signed map (-3.7, 39.2). **Vector** length 45.6, 8.47% of its response variance represented; |z| ≥ 3 in 608 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +16.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.1 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.0 | +11.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[vincristine (drug)]] 5 µM |  | +1.1 | +3.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +3.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | +0.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | unc-5 netrin receptor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.2 — chr5:176,810,519-176,880,898 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1976, UNC5H1 |
| Gene groups (HGNC) | I-set domain containing; Ig-like cell adhesion molecule family; ZU5 domain containing |
| Reactome | 8 pathways, smallest: Netrin mediated repulsion signals; Caspase activation via Dependence Receptors in the absence of ligand; Caspase activation via extrinsic apoptotic signalling pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZN44](https://www.uniprot.org/uniprotkb/Q6ZN44) (Netrin receptor UNC5A):

> Receptor for netrin required for axon guidance. Functions in the netrin signaling pathway and promotes neurite outgrowth in response to NTN1. It also acts as a dependence receptor required for apoptosis induction when not associated with netrin ligand.

**Summary**, from NCBI Gene [90249](https://www.ncbi.nlm.nih.gov/gene/90249):

> UNC5A belongs to a family of netrin-1 (MIM 601614) receptors thought to mediate the chemorepulsive effect of netrin-1 on specific axons. For more information on UNC5 proteins, see UNC5C (MIM 603610).[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:12567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12567) · Entrez [90249](https://www.ncbi.nlm.nih.gov/gene/90249) · UniProt [Q6ZN44](https://www.uniprot.org/uniprotkb/Q6ZN44) · Ensembl [ENSG00000113763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113763)

## Data

Gene col 3502: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3502); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3502, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3502]; `tensor/DDL_lfc|DDL_z.npy` [3502]; `embed/gene_vectors.npy` [3502]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3502 or target_col == 3502). Every well: [[UNC5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UNC5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
