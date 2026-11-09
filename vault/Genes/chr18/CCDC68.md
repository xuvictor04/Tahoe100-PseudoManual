---
symbol: "CCDC68"
type: "gene"
col: 9324
ensembl_id: "ENSG00000166510"
name: "coiled-coil domain containing 68"
location: "18q21.2"
module: 34
arm: "+"
pooled_cpm: 38.75
n_lines_expressing: 25
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 3
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 24
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CCDC68

*coiled-coil domain containing 68* — 18q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.63× (z +13.7, q 5e-40, up in 12 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.62× (z +9.7, q 1e-19, up in 17 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.453× (z -15.8, q 0e+00, down in 22 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB27B]] (+0.62, fdr 1e-05, ⚠ same locus), [[UNC5D]] (+0.59, fdr 1e-05), [[GTF2IP7]] (+0.59, fdr 1e-05), [[GDA]] (+0.58, fdr 1e-05); moves opposite to [[ZNF785]] (-0.46, fdr 3e-04), [[MTO1]] (-0.43, fdr 5e-05), [[VLDLR-AS1]] (-0.43, fdr 3e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PAQR5]] → it (grade B ⚠); 24 go from it, the strongest it → [[PAQR5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +13.7 | 5e-40 | 12/21 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +9.7 | 1e-19 | 17/23 (KATO III, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +8.5 | 2e-15 | 8/18 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +6.9 | 7e-10 | 17/23 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +6.3 | 4e-08 | 7/20 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.8 | 0.013 | 2/23 (HCT15, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.19 | 4/23 (LoVo, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.453×** | -15.8 | 0e+00 | 22/23 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.515×** | -13.2 | 2e-37 | 22/23 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.472×** | -10.6 | 6e-24 | 17/23 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.594×** | -7.3 | 3e-11 | 18/23 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.374×** | -7.3 | 5e-11 | 20/24 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -5.8 | 5e-07 | 17/23 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.703×** | -5.0 | 5e-05 | 12/23 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -5.0 | 5e-05 | 17/23 (NCI-H460, MIA PaCa-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.689×** | -4.9 | 5e-05 | 9/23 (SNU-1, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -4.4 | 8e-04 | 19/23 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.722×** | -4.2 | 0.001 | 9/23 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.743×** | -4.2 | 0.001 | 9/23 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.734×** | -4.2 | 0.001 | 13/23 (AsPC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -4.1 | 0.002 | 17/23 (NCI-H460, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.748×** | -4.1 | 0.002 | 15/23 (SNU-1, NCI-H460, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.752×** | -4.0 | 0.002 | 14/23 (LoVo, COLO 205, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 235 | 0 | 27 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0866× (z -29.7) |
| [[SNU-1 (line)]] | wt | 215 | 0 | 8 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -23.0) |
| [[AsPC-1 (line)]] | alt | 150 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -26.7) |
| [[MIA PaCa-2 (line)]] | alt | 89.4 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0608× (z -29.4) |
| [[NCI-H1792 (line)]] | alt | 143 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0732× (z -25.6) |
| [[LS 180 (line)]] | wt | 60.5 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -21.4) |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 54.6 | 0 | 4 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -14.9) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.294× (z -11.7) |
| [[LoVo (line)]] | wt | 53.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -26.2) |
| [[NCI-H2030 (line)]] | alt | 88.9 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -17.7) |
| [[Panc 03.27 (line)]] | alt | 29.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.218× (z -15.6) |
| [[A498 (line)]] | wt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 36.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 56.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.8) |
| [[A549 (line)]] | wt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -13.5) |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0628× (z -11.6) |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.0) |
| [[KATO III (line)]] | alt | 25.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -10.1) |
| [[A-172 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.38 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.72 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.78 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.21 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.60 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.67 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.70 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 9.62 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.57 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB27B]] | +0.62 | +0.68 / +0.57 | both halves | 1e-05 | STRING 437; ⚠ same locus (6.0 kb: neighbours can correlate without regulation) |
| [[UNC5D]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[GTF2IP7]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[GDA]] | +0.58 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[DOCK4]] | +0.58 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LIPH]] | +0.57 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[PSD3]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[UNC13A]] | +0.55 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[SYT13]] | +0.54 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[SMOC1]] | +0.54 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CD55]] | +0.54 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SERPIND1]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[BMP6]] | +0.53 | +0.53 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF785]] | -0.46 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[MTO1]] | -0.43 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[VLDLR-AS1]] | -0.43 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[ZNF717]] | -0.42 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[ACAD11]] | -0.42 | -0.44 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR5]] | B | PAQR5 activity raises CCDC68's level | lines that do not express PAQR5 (11) vs lines expressing it (39) | 1.94× lower at baseline in the lines without PAQR5 | 0.054 | ⚠ within organs, on part of the lines; also absent: ADORA2B |
| [[RAB27B]] | C | RAB27B activity raises CCDC68's level | lines that do not express RAB27B (15) vs lines expressing it (35) | 3.33× lower at baseline in the lines without RAB27B | 0.009 | ⚠ within organs, on part of the lines; also absent: CXCL3, PLAAT4, F3; co-absent with the target |
| [[GABRE]] | C | GABRE activity raises CCDC68's level | lines that do not express GABRE (20) vs lines expressing it (30) | 2.40× lower at baseline in the lines without GABRE | 0.024 | ⚠ within organs, on part of the lines; also absent: IL2RG, ACSL5, PI3; co-absent with the target |
| [[GDA]] | C | GDA activity raises CCDC68's level | lines that do not express GDA (35) vs lines expressing it (15) | 3.43× lower at baseline in the lines without GDA | 0.038 | ⚠ within organs, on part of the lines; also absent: HHLA2, GPA33, LGALS4; co-absent with the target |
| [[IGFBP1]] | C | IGFBP1 activity raises CCDC68's level | lines that do not express IGFBP1 (39) vs lines expressing it (11) | 2.90× lower at baseline in the lines without IGFBP1 | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGB, ITIH2; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 15, C 9. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAQR5]] | B | CCDC68 activity raises PAQR5's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 2.36× lower at baseline in the lines without CCDC68 | 0.012 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[NOSTRIN]] | B | CCDC68 activity raises NOSTRIN's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without CCDC68 | 0.015 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[GPRC5A]] | B | CCDC68 activity raises GPRC5A's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 3.15× lower at baseline in the lines without CCDC68 | 0.018 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[FGD6]] | B | CCDC68 activity raises FGD6's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without CCDC68 | 0.025 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[FAM107B]] | B | CCDC68 activity raises FAM107B's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 1.99× lower at baseline in the lines without CCDC68 | 0.036 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[EIF5A2]] | B | CCDC68 activity lowers EIF5A2's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 1.67× higher at baseline in the lines without CCDC68 | 0.050 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[AKAP13]] | B | CCDC68 activity raises AKAP13's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 1.55× lower at baseline in the lines without CCDC68 | 0.066 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[JUP]] | B | CCDC68 activity raises JUP's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 3.03× lower at baseline in the lines without CCDC68 | 0.078 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| cells under [[Terfenadine (drug)]] 5 µM | B | CCDC68 activity raises the cells' numbers under Terfenadine 5 µM (protects the cells) | lines that do not express CCDC68 (25) vs lines expressing it (23) | the lines without CCDC68: 0.89× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| cells under [[Terfenadine (drug)]] 0.5 µM | B | CCDC68 activity raises the cells' numbers under Terfenadine 0.5 µM (protects the cells) | lines that do not express CCDC68 (25) vs lines expressing it (23) | the lines without CCDC68: 0.80× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| cells under [[Aliskiren (drug)]] 0.5 µM | B | CCDC68 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express CCDC68 (25) vs lines expressing it (23) | the lines without CCDC68: 0.79× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |
| [[TCF7L2]] | B | CCDC68 activity raises TCF7L2's level | lines that do not express CCDC68 (25) vs lines expressing it (25) | 1.93× lower at baseline in the lines without CCDC68 | 0.087 | ⚠ within organs, on part of the lines; also absent: GRB7, SH2D3A, GOLT1A |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.0, 16.4); signed map (17.2, 55.0). **Vector** length 90.2, 28.0% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +9.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.3 | +6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +0.1 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +1.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.3 | +2.5 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.3 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.3 | -3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.2 — chr18:54,901,509-54,959,461 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SE57-1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2F9](https://www.uniprot.org/uniprotkb/Q9H2F9) (Coiled-coil domain-containing protein 68):

> Centriolar protein required for centriole subdistal appendage assembly and microtubule anchoring in interphase cells. Together with CCDC120, cooperate with subdistal appendage components ODF2, NIN and CEP170 for hierarchical subdistal appendage assembly.

**Summary**, from NCBI Gene [80323](https://www.ncbi.nlm.nih.gov/gene/80323):

> Involved in intracellular protein localization and microtubule anchoring at centrosome. Located in centriole. Part of centriolar subdistal appendage. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24350) · Entrez [80323](https://www.ncbi.nlm.nih.gov/gene/80323) · UniProt [Q9H2F9](https://www.uniprot.org/uniprotkb/Q9H2F9) · Ensembl [ENSG00000166510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166510)

## Data

Gene col 9324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9324); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9324]; `tensor/DDL_lfc|DDL_z.npy` [9324]; `embed/gene_vectors.npy` [9324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9324 or target_col == 9324). Every well: [[CCDC68 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC68.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
