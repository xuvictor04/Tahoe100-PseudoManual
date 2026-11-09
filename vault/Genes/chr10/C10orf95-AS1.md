---
symbol: "C10orf95-AS1"
type: "gene"
col: 15627
ensembl_id: "ENSG00000269609"
name: "C10orf95 antisense RNA 1"
location: "10q24.32"
module: 46
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 46
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 9
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# C10orf95-AS1

*C10orf95 antisense RNA 1* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.84× (z +12.3, q 3e-32, up in 5 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +8.5, q 2e-15, up in 17 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.418× (z -8.3, q 8e-14, down in 22 of 42 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOTAIR]] (+0.64, fdr 3e-05), [[ZBED3]] (+0.62, fdr 2e-05), [[LRRC61]] (+0.61, fdr 4e-05); moves opposite to [[EHD4]] (-0.51, fdr 3e-04), [[CAP1]] (-0.51, fdr 1e-04), [[MYO1E]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HSD11B2]] → it (grade B ⚠); 9 go from it, the strongest it → [[ZNF32]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15627.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.84×** | +12.3 | 3e-32 | 5/5 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.45×** | +11.8 | 1e-29 | 16/19 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.97×** | +9.6 | 2e-19 | 6/8 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.61×** | +8.8 | 2e-16 | 20/23 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +8.5 | 2e-15 | 17/30 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +7.5 | 8e-12 | 19/40 (HT-29, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.79×** | +5.6 | 2e-06 | 19/41 (J82, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.0 | 4e-05 | 12/31 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.1 | 0.003 | 10/37 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +3.8 | 0.008 | 7/29 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.018 | 8/41 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.5 | 0.022 | 7/21 (NCI-H1573, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.71×** | +3.5 | 0.022 | 2/29 (PANC-1, A-427) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.038 | 6/43 (NCI-H2030, PANC-1, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.59×** | +3.0 | 0.099 | 2/34 (C-33 A, SW480) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15627.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.418×** | -8.3 | 8e-14 | 22/42 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.428×** | -8.1 | 2e-13 | 23/39 (C-33 A, SW48, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.544×** | -5.8 | 2e-06 | 20/38 (KATO III, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.634×** | -4.3 | 0.002 | 15/26 (A-427, C-33 A, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.636×** | -4.3 | 0.002 | 7/41 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.617×** | -4.2 | 0.002 | 14/29 (NCI-H1573, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.457×** | -3.9 | 0.008 | 15/29 (SW480, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.480×** | -3.6 | 0.020 | 7/34 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.679×** | -3.5 | 0.025 | 12/37 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Sapanisertib (drug)]] 0.05 µM |  | **0.674×** | -3.5 | 0.025 | 4/41 (H4, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.681×** | -3.4 | 0.032 | 15/34 (MIA PaCa-2, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.510×** | -3.3 | 0.040 | 10/35 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Hexylresorcinol (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.042 | 5/42 (H4, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15627. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0850× (z -12.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 10.00 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -11.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0539× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 4.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0393× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 2.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.97× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 4.52 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0613× (z -8.6) |
| [[SW48 (line)]] | wt | 10.9 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0716× (z -8.7) |
| [[SW480 (line)]] | alt | 7.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.709 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.762 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.963 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15627), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 10 of them with an alert (⚠; 10 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOTAIR]] | +0.64 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[ZBED3]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[LRRC61]] | +0.61 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[CNN3-DT]] | +0.56 | +0.64 / +0.28 | both halves | 3e-04 |  |
| [[C14orf93]] | +0.56 | +0.54 / +0.40 | both halves | 5e-05 |  |
| [[ABRACL]] | +0.55 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[TTC32]] | +0.54 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[ZCCHC8]] | +0.53 | +0.41 / +0.36 | both halves | 9e-05 |  |
| [[ZNF236-DT]] | +0.53 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[ZNF665]] | +0.53 | +0.39 / +0.39 | both halves | 6e-05 |  |
| [[KCTD21-AS1]] | +0.53 | +0.53 / +0.39 | both halves | 5e-05 | same gene group |
| [[SIAH1]] | +0.53 | +0.54 / +0.07 | ⚠ one half (not replicated) | 0.004 |  |
| [[TFAP2A-AS1]] | +0.53 | +0.50 / +0.41 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHD4]] | -0.51 | -0.55 / -0.27 | both halves | 3e-04 |  |
| [[CAP1]] | -0.51 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[MYO1E]] | -0.47 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[TGM2]] | -0.47 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[DIAPH1]] | -0.46 | -0.29 / -0.51 | both halves | 2e-04 |  |
| [[AKAP13]] | -0.46 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[PSD3]] | -0.45 | -0.40 / -0.26 | both halves | 4e-04 |  |
| [[SCART1]] | -0.45 | -0.37 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD11B2]] | B | HSD11B2 activity raises C10orf95-AS1's level | lines that do not express HSD11B2 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without HSD11B2 | 0.011 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers C10orf95-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ZBED3]] | C | ZBED3 activity raises C10orf95-AS1's level | lines that do not express ZBED3 (3) vs lines expressing it (47) | 2.35× lower at baseline in the lines without ZBED3 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPD1L, DBNDD1, CDON; maybe low, not absent; its own permutation p |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF32]] | C | C10orf95-AS1 activity raises ZNF32's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 2.37× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |
| [[GAS2]] | C | C10orf95-AS1 activity raises GAS2's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |
| [[DHRS4L2]] | C | C10orf95-AS1 activity raises DHRS4L2's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 2.05× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; co-absent with the target; its own permutation p |
| [[DICER1-AS1]] | C | C10orf95-AS1 activity raises DICER1-AS1's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.92× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |
| [[TIRAP-AS1]] | C | C10orf95-AS1 activity raises TIRAP-AS1's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.53× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |
| [[ZNF514]] | C | C10orf95-AS1 activity raises ZNF514's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without C10orf95-AS1 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent |
| [[ANKHD1-DT]] | C | C10orf95-AS1 activity raises ANKHD1-DT's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without C10orf95-AS1 | 0.083 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent |
| [[EIF3J-DT]] | C | C10orf95-AS1 activity raises EIF3J-DT's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.21× lower at baseline in the lines without C10orf95-AS1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent |
| [[C14orf93]] | C | C10orf95-AS1 activity raises C14orf93's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.67× lower at baseline in the lines without C10orf95-AS1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-12.1, 42.9); signed map (37.0, -18.8). **Vector** length 49.7, 7.29% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.0 | +7.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +8.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +2.1 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.9 | -8.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -8.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -0.9 | -2.4 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -0.9 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | C10orf95 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q24.32 — chr10:102,449,816-102,461,106 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously RPARP-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:45238](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:45238) · Entrez [100505761](https://www.ncbi.nlm.nih.gov/gene/100505761) · Ensembl [ENSG00000269609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269609)

## Data

Gene col 15627: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15627); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15627, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15627]; `tensor/DDL_lfc|DDL_z.npy` [15627]; `embed/gene_vectors.npy` [15627]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15627 or target_col == 15627). Every well: [[C10orf95-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C10orf95-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
