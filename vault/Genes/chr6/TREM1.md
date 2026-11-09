---
symbol: "TREM1"
type: "gene"
col: 4560
ensembl_id: "ENSG00000124731"
name: "triggering receptor expressed on myeloid cells 1"
location: "6p21.1"
module: 113
arm: "+"
pooled_cpm: 2.5
n_lines_expressing: 25
n_dd_up: 10
n_dd_down: 20
n_dd_up_clean: 6
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 16
direction_downstream: 31
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# TREM1

*triggering receptor expressed on myeloid cells 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.30× (z +9.3, q 1e-17, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.16× (z +7.2, q 1e-10, up in 11 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.324× (z -7.5, q 5e-11, down in 16 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADGRE2]] (+0.62, fdr 7e-06), [[ADAM28]] (+0.61, fdr 1e-05), [[EPAS1]] (+0.58, fdr 1e-05); moves opposite to [[AJUBA]] (-0.49, fdr 2e-05), [[PTPRK]] (-0.47, fdr 4e-05), [[TMCO4]] (-0.46, fdr 3e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CCDC33]] → it (grade B ⚠); 31 go from it, the strongest it → [[GPCPD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.30×** | +9.3 | 1e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.16×** | +7.2 | 1e-10 | 11/20 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.70×** | +6.1 | 2e-07 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +5.9 | 6e-07 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.31×** | +5.5 | 4e-06 | 8/15 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.17×** | +5.4 | 5e-06 | 1/6 (HS-578T) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.87×** | +4.1 | 0.003 | 4/18 (SHP-77, Hs 766T, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **2.15×** | +3.6 | 0.021 | 3/13 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.09×** | +3.5 | 0.031 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | **1.69×** | +3.4 | 0.045 | 1/14 (NCI-H2347) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.58× | +3.0 | 0.12 | 0/13 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, none with an alert; shown: the 15 strongest. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4560.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.324×** | -7.5 | 5e-11 | 16/21 (SHP-77, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.482×** | -6.8 | 2e-09 | 16/16 (SHP-77, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.445×** | -5.4 | 2e-05 | 16/21 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.449×** | -5.3 | 2e-05 | 14/17 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.442×** | -5.2 | 2e-05 | 14/18 (HS-578T, SHP-77, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.464×** | -4.7 | 2e-04 | 10/19 (C32, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.508×** | -4.5 | 6e-04 | 15/19 (SHP-77, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.560×** | -3.8 | 0.008 | 9/19 (HS-578T, C32, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.665×** | -3.8 | 0.008 | 8/18 (SHP-77, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM |  | **0.550×** | -3.8 | 0.009 | 9/20 (CFPAC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -3.6 | 0.014 | 11/19 (SHP-77, A549, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -3.6 | 0.017 | 14/19 (SHP-77, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.585×** | -3.6 | 0.017 | 9/19 (HS-578T, SHP-77, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.591×** | -3.5 | 0.020 | 10/16 (HS-578T, SW 900, …) | two highest doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.592×** | -3.3 | 0.032 | 4/19 (HS-578T, SHP-77, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 13 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00465× (z -38.6) |
| [[HS-578T (line)]] | alt | 11.6 | 0 | 7 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0177× (z -15.0) |
| [[SW 900 (line)]] | alt | 8.61 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0633× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0805× (z -11.8) |
| [[A549 (line)]] | wt | 4.85 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0467× (z -12.4) |
| [[CFPAC-1 (line)]] | alt | 2.45 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0546× (z -10.8) |
| [[HOP62 (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0130× (z -24.4) |
| [[NCI-H460 (line)]] | wt | 3.01 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0734× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.145× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 6.58 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0781× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0785× (z -10.2) |
| [[BT-474 (line)]] | alt | 3.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0415× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 2.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0977× (z -8.9) |
| [[A-172 (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.195 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.328 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.234 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.295 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.309 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.341 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.643 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.262 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.247 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADGRE2]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | same gene group |
| [[ADAM28]] | +0.61 | +0.56 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[EPAS1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[AGTR1]] | +0.57 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[EFNA5]] | +0.56 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MTSS1]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ANGPTL4]] | +0.56 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[ELL2]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GLRX]] | +0.54 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[CLDN10]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[FRY]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[PCBP3]] | +0.52 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AJUBA]] | -0.49 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PTPRK]] | -0.47 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TMCO4]] | -0.46 | -0.50 / -0.26 | both halves | 3e-04 |  |
| [[SH2D4A]] | -0.45 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[LINC02595]] | -0.45 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[LRRK1]] | -0.44 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[ANKRD18B]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[TENM3]] | -0.43 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[OXTR]] | -0.43 | -0.51 / -0.30 | both halves | 2e-04 |  |
| [[QSER1]] | -0.43 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[SFT2D2]] | -0.41 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[RGS20]] | -0.41 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 6, C 10. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCDC33]] | B | CCDC33 activity raises TREM1's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 2.22× lower at baseline in the lines without CCDC33 | 0.028 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[GLRX]] | B | GLRX activity raises TREM1's level | lines that do not express GLRX (10) vs lines expressing it (40) | 1.92× lower at baseline in the lines without GLRX | 0.056 | ⚠ within organs, on part of the lines; also absent: DUSP10, FES, DGKG; maybe low, not absent |
| [[THEMIS2]] | B | THEMIS2 activity raises TREM1's level | lines that do not express THEMIS2 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without THEMIS2 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF9, PLAU, IGDCC4 |
| [[MAP2K1]] | B | MAP2K1 activity raises TREM1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[TMEM255B]] | B | TMEM255B activity raises TREM1's level | lines that do not express TMEM255B (19) vs lines expressing it (31) | 1.92× lower at baseline in the lines without TMEM255B | 0.086 | ⚠ within organs, on part of the lines; also absent: DOCK10, ENSG00000289600, OR4F15; maybe low, not absent |
| [[LPAR1]] | B | LPAR1 activity raises TREM1's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 2.17× lower at baseline in the lines without LPAR1 | 0.094 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2 |
| [[TRPA1]] | C | TRPA1 activity raises TREM1's level | lines that do not express TRPA1 (31) vs lines expressing it (19) | 2.92× lower at baseline in the lines without TRPA1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITGA4, DOCK10, INSYN2B; co-absent with the target |
| [[CD38]] | C | CD38 activity raises TREM1's level | lines that do not express CD38 (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without CD38 | 0.009 | ⚠ within organs, on part of the lines; also absent: MAGEA10, RNF17, GRIA2; maybe low, not absent; co-absent with the target |
| [[LINC02015]] | C | LINC02015 activity raises TREM1's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 2.69× lower at baseline in the lines without LINC02015 | 0.014 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN; co-absent with the target |
| [[MTSS1]] | C | MTSS1 activity raises TREM1's level | lines that do not express MTSS1 (20) vs lines expressing it (30) | 2.15× lower at baseline in the lines without MTSS1 | 0.023 | ⚠ within organs, on part of the lines; also absent: RASD1, GATA3, TREM1; co-absent with the target |
| [[ADAM28]] | C | ADAM28 activity raises TREM1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.59× lower at baseline in the lines without ADAM28 | 0.025 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; co-absent with the target |
| [[SHC4]] | C | SHC4 activity raises TREM1's level | lines that do not express SHC4 (23) vs lines expressing it (27) | 2.54× lower at baseline in the lines without SHC4 | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000250137, AR, GNG2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 21, C 10. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPCPD1]] | B | TREM1 activity raises GPCPD1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 1.92× lower at baseline in the lines without TREM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[NAMPT]] | B | TREM1 activity raises NAMPT's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.20× lower at baseline in the lines without TREM1 | 0.005 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[GLRX]] | B | TREM1 activity raises GLRX's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.67× lower at baseline in the lines without TREM1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[SMOX]] | B | TREM1 activity raises SMOX's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.88× lower at baseline in the lines without TREM1 | 0.006 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[NIBAN2]] | B | TREM1 activity raises NIBAN2's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without TREM1 | 0.019 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[TMEM92-AS1]] | B | TREM1 activity raises TMEM92-AS1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.45× lower at baseline in the lines without TREM1 | 0.021 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[RGS20]] | B | TREM1 activity raises RGS20's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 1.10× lower at baseline in the lines without TREM1 | 0.031 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[GPCPD1]] | B | TREM1 activity weakens GPCPD1's drug response | lines that do not express TREM1 (25) vs lines expressing it (24) | the lines without TREM1 respond 1.22× as strongly (z diff -0.46); strongest at Homoharringtonine 5 µM: 3.02x vs 1.42x (z diff -4.8) | 0.032 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF; target measured in part of the lines; both ways; artifact flags |
| [[LPAR1]] | B | TREM1 activity raises LPAR1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 3.77× lower at baseline in the lines without TREM1 | 0.033 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| cells under [[LY-2584702 (tosylate salt) (drug)]] 5 µM | B | TREM1 activity lowers the cells' numbers under LY-2584702 (tosylate salt) 5 µM (makes them more sensitive) | lines that do not express TREM1 (25) vs lines expressing it (23) | the lines without TREM1: 1.30× the cells of the other lines | 0.035 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[ST3GAL1]] | B | TREM1 activity raises ST3GAL1's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.26× lower at baseline in the lines without TREM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[THEMIS2]] | B | TREM1 activity raises THEMIS2's level | lines that do not express TREM1 (25) vs lines expressing it (25) | 2.96× lower at baseline in the lines without TREM1 | 0.040 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.502). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (35.2, 10.4); signed map (19.6, 38.2). **Vector** length 66.5, 20.3% of its response variance represented; |z| ≥ 3 in 659 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +9.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.5 | +2.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | triggering receptor expressed on myeloid cells 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:41,267,926-41,286,682 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TREM-1, CD354 |
| Gene groups (HGNC) | CD molecules; V-set domain containing |
| Reactome | 6 pathways, smallest: DAP12 interactions; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Cell surface interactions at the vascular wall |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP99](https://www.uniprot.org/uniprotkb/Q9NP99) (Triggering receptor expressed on myeloid cells 1):

> [Isoform 1]: Cell surface receptor that plays important roles in innate and adaptive immunity by amplifying inflammatory responses. Upon activation by various ligands such as PGLYRP1, HMGB1 or HSP70, multimerizes and forms a complex with transmembrane adapter TYROBP/DAP12. In turn, initiates a SYK-mediated cascade of tyrosine phosphorylation, activating multiple downstream mediators such as BTK, MAPK1, MAPK3 or phospholipase C-gamma. This cascade promotes the neutrophil- and macrophage-mediated …

**Summary**, from NCBI Gene [54210](https://www.ncbi.nlm.nih.gov/gene/54210):

> This gene encodes a receptor belonging to the Ig superfamily that is expressed on myeloid cells. This protein amplifies neutrophil and monocyte-mediated inflammatory responses triggered by bacterial and fungal infections by stimulating release of pro-inflammatory chemokines and cytokines, as well as increased surface expression of cell activation markers. Alternatively spliced transcript variants encoding different isoforms have been noted for this gene.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:17760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17760) · Entrez [54210](https://www.ncbi.nlm.nih.gov/gene/54210) · UniProt [Q9NP99](https://www.uniprot.org/uniprotkb/Q9NP99) · Ensembl [ENSG00000124731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124731)

## Data

Gene col 4560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4560); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4560]; `tensor/DDL_lfc|DDL_z.npy` [4560]; `embed/gene_vectors.npy` [4560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4560 or target_col == 4560). Every well: [[TREM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TREM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
