---
symbol: "SLC45A1"
type: "gene"
col: 8516
ensembl_id: "ENSG00000162426"
name: "solute carrier family 45 member 1"
location: "1p36.23"
module: 113
arm: "+"
pooled_cpm: 3.64
n_lines_expressing: 31
n_dd_up: 30
n_dd_down: 11
n_dd_up_clean: 22
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 4
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# SLC45A1

*solute carrier family 45 member 1* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.94× (z +14.5, q 3e-45, up in 21 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.465× (z -6.3, q 2e-07, down in 14 of 23 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERRFI1]] (+0.67, fdr 1e-05), [[MT1A]] (+0.63, fdr 9e-06), [[TOX2]] (+0.63, fdr 1e-05); moves opposite to [[C5orf15]] (-0.51, fdr 1e-04), [[DECR1]] (-0.51, fdr 5e-04), [[SPAG16]] (-0.49, fdr 9e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[FSD1]] → it (grade B ⚠); 4 go from it, the strongest it → [[SERPINE1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8516.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.94×** | +14.5 | 3e-45 | 21/25 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.94×** | +14.5 | 3e-45 | 24/25 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.24×** | +13.5 | 2e-39 | 21/24 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **4.80×** | +12.8 | 3e-35 | 21/25 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.52×** | +9.9 | 6e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.86×** | +8.6 | 1e-15 | 23/25 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.84×** | +8.5 | 1e-15 | 16/21 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +6.5 | 4e-09 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.00×** | +5.6 | 1e-06 | 12/15 (MIA PaCa-2, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.93×** | +5.3 | 5e-06 | 0/6 | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.2 | 1e-05 | 2/25 (SW 900, AsPC-1) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.85×** | +5.0 | 3e-05 | 5/24 (HOP62, SNU-1, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.89×** | +4.8 | 7e-05 | 8/17 (PANC-1, A549, …) | inconsistent across doses |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.13×** | +4.4 | 4e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.70×** | +4.3 | 7e-04 | 11/23 (PANC-1, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.42×** | +4.0 | 0.002 | 7/23 (PANC-1, HOP62, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.63×** | +4.0 | 0.002 | 8/20 (PANC-1, Hs 766T, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.46×** | +3.8 | 0.004 | 6/19 (SW480, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.008 | 9/21 (PANC-1, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8516.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.465×** | -6.3 | 2e-07 | 14/23 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.474×** | -6.1 | 3e-07 | 13/17 (PANC-1, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.550×** | -4.9 | 2e-04 | 11/27 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.616×** | -4.0 | 0.011 | 12/25 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -3.8 | 0.018 | 12/23 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -3.7 | 0.018 | 12/23 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.637×** | -3.7 | 0.018 | 7/22 (HOP62, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.05 µM |  | **0.641×** | -3.4 | 0.042 | 4/23 (SNU-1, A-172, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.660×** | -3.4 | 0.043 | 9/25 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.654×** | -3.3 | 0.057 | 9/27 (NCI-H23, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.654×** | -3.2 | 0.069 | 2/25 (MIA PaCa-2, NCI-H2347) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8516. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 33.4 | 0 | 10 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0891× (z -21.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0955× (z -13.9) |
| [[PANC-1 (line)]] | alt | 20.9 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0738× (z -27.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0801× (z -18.8) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0589× (z -14.4) |
| [[A549 (line)]] | wt | 3.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -10.2) ⚠ cell-cycle shift, explains ~57% of this change |
| [[HOP62 (line)]] | alt | 2.79 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.20× (z +8.7) | — |
| [[NCI-H460 (line)]] | wt | 1.96 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -9.1) ⚠ cell-cycle shift, explains ~57% of this change |
| [[SW480 (line)]] | alt | 1.60 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0440× (z -10.5) |
| [[A-172 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.645 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.384 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.583 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.453 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.686 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.792 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.951 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.713 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.941 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.532 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.426 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.755 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8516), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERRFI1]] | +0.67 | +0.60 / +0.56 | both halves | 1e-05 | STRING 499 |
| [[MT1A]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[TOX2]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ANGPTL4]] | +0.60 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[CACNG7]] | +0.60 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[LPAR3]] | +0.60 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[HPCAL1]] | +0.59 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[PTPRS]] | +0.58 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[PAQR5]] | +0.56 | +0.37 / +0.44 | both halves | 7e-05 |  |
| [[BMERB1]] | +0.55 | +0.32 / +0.45 | both halves | 2e-04 |  |
| [[TBC1D8]] | +0.55 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[MAP6]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf15]] | -0.51 | -0.32 / -0.43 | both halves | 1e-04 |  |
| [[DECR1]] | -0.51 | -0.38 / -0.23 | both halves | 5e-04 |  |
| [[SPAG16]] | -0.49 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[NNT]] | -0.49 | -0.27 / -0.41 | both halves | 3e-04 |  |
| [[DNAI4]] | -0.49 | -0.32 / -0.31 | both halves | 2e-04 |  |
| [[ARMCX5-GPRASP2]] | -0.49 | -0.27 / -0.30 | both halves | 3e-04 |  |
| [[AHI1-DT]] | -0.48 | -0.28 / -0.27 | both halves | 3e-04 |  |
| [[UFL1-AS1]] | -0.47 | -0.34 / -0.20 | both halves | 7e-04 |  |
| [[LINC00571]] | -0.47 | -0.27 / -0.30 | both halves | 3e-04 |  |
| [[RC3H2]] | -0.47 | -0.24 / -0.34 | both halves | 4e-04 |  |
| [[ZNF532]] | -0.47 | -0.24 / -0.38 | both halves | 5e-04 |  |
| [[HOMEZ]] | -0.47 | -0.39 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSD1]] | B | FSD1 activity raises SLC45A1's level | lines that do not express FSD1 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without FSD1 | 0.045 | ⚠ within organs, on part of the lines; also absent: RFLNB, B4GALNT1, NTNG2 |
| [[PTPRB]] | B | PTPRB activity lowers SLC45A1's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 1.59× higher at baseline in the lines without PTPRB | 0.046 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[WT1-AS]] | B | WT1-AS activity raises SLC45A1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 1.89× lower at baseline in the lines without WT1-AS | 0.060 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG |
| [[KIF26A]] | B | KIF26A activity raises SLC45A1's level | lines that do not express KIF26A (17) vs lines expressing it (33) | 1.63× lower at baseline in the lines without KIF26A | 0.067 | ⚠ within organs, on part of the lines; also absent: SRRM3, LAMC3, BEGAIN |
| [[NR3C1]] | B | NR3C1 activity raises SLC45A1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[ITPRIP]] | B | ITPRIP activity raises SLC45A1's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without ITPRIP | 0.089 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE1]] | B | SLC45A1 activity raises SERPINE1's level | lines that do not express SLC45A1 (19) vs lines expressing it (31) | 3.43× lower at baseline in the lines without SLC45A1 | 0.020 | ⚠ within organs, on part of the lines; also absent: LRRC34, PNMA2, SSTR2 |
| [[SH3RF3]] | B | SLC45A1 activity raises SH3RF3's level | lines that do not express SLC45A1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without SLC45A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: LRRC34, PNMA2, SSTR2 |
| cells under [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM | B | SLC45A1 activity lowers the cells' numbers under 18β-Glycyrrhetinic acid 0.5 µM (makes them more sensitive) | lines that do not express SLC45A1 (19) vs lines expressing it (29) | the lines without SLC45A1: 1.14× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: LRRC34, PNMA2, SSTR2 |
| [[MAP6]] | B | SLC45A1 activity raises MAP6's level | lines that do not express SLC45A1 (19) vs lines expressing it (31) | 2.01× lower at baseline in the lines without SLC45A1 | 0.078 | ⚠ within organs, on part of the lines; also absent: LRRC34, PNMA2, SSTR2 |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.6, 13.2); signed map (13.4, 35.7). **Vector** length 54.8, 12.0% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +13.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +14.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +14.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.3 | +12.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +4.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.4 | +4.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.3 | +3.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.3 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.6 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -6.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 45 member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:8,318,114-8,344,167 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DNB5 |
| Gene groups (HGNC) | Solute carrier family 45 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2W3](https://www.uniprot.org/uniprotkb/Q9Y2W3) (Proton-associated sugar transporter A):

> Neuron-specific proton-associated hexose transporter, which mediates hexose efflux from lysosomes. Hexose efflux is required for the stability of the vacuolar ATPase (V-ATPase) complex on the lysosomal membrane.

**Summary**, from NCBI Gene [50651](https://www.ncbi.nlm.nih.gov/gene/50651):

> This gene was isolated initially from a region on chromosome 1p that is frequently deleted in human neuroblastoma, although no causal relationship has since been demonstrated. The encoded protein belongs to the glycoside-pentoside-hexuronide cation symporter transporter family and may play a role in glucose uptake. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:17939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17939) · Entrez [50651](https://www.ncbi.nlm.nih.gov/gene/50651) · UniProt [Q9Y2W3](https://www.uniprot.org/uniprotkb/Q9Y2W3) · Ensembl [ENSG00000162426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162426)

## Data

Gene col 8516: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8516); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8516, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8516]; `tensor/DDL_lfc|DDL_z.npy` [8516]; `embed/gene_vectors.npy` [8516]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8516 or target_col == 8516). Every well: [[SLC45A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC45A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
