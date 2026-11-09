---
symbol: "SLIT1"
type: "gene"
col: 11890
ensembl_id: "ENSG00000187122"
name: "slit guidance ligand 1"
location: "10q24.1"
module: 75
arm: "+"
pooled_cpm: 4.68
n_lines_expressing: 43
n_dd_up: 26
n_dd_down: 12
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# SLIT1

*slit guidance ligand 1* — 10q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.73× (z +19.0, q 0e+00, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.517× (z -8.8, q 6e-16, down in 21 of 39 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02981]] (+0.59, fdr 7e-06), [[MYO18B]] (+0.59, fdr 1e-05), [[LINC02245]] (+0.55, fdr 8e-05); moves opposite to [[NRIP1]] (-0.44, fdr 3e-04), [[AMACR]] (-0.42, fdr 5e-04), [[KIAA1586]] (-0.41, fdr 3e-04).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANO4]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GPR143]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.73×** | +19.0 | 0e+00 | 24/32 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +15.9 | 0e+00 | 3/9 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **3.09×** | +15.1 | 0e+00 | 29/40 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +12.4 | 4e-33 | 26/38 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.41×** | +11.7 | 9e-30 | 8/16 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +10.8 | 3e-25 | 22/36 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.26×** | +10.1 | 5e-22 | 8/10 (SHP-77, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +9.9 | 3e-21 | 17/39 (SW480, NCI-H460, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.03×** | +9.4 | 2e-19 | 19/39 (A498, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +6.2 | 4e-08 | 13/39 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.3 | 6e-06 | 8/39 (HOP62, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 2e-04 | 10/37 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.91×** | +4.5 | 3e-04 | 6/38 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 3e-04 | 3/36 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 9/32 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.002 | 9/25 (BT-474, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.35×** | +3.7 | 0.006 | 3/25 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.015 | 3/38 (C32, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.517×** | -8.8 | 6e-16 | 21/39 (A-427, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.624×** | -6.1 | 4e-07 | 16/35 (HEC-1-A, SW480, …) | two highest doses | composition shift |
| [[crizotinib (drug)]] 5 µM |  | **0.685×** | -4.9 | 2e-04 | 8/38 (COLO 205, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.736×** | -4.1 | 0.006 | 10/28 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.749×** | -3.9 | 0.012 | 8/38 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.596×** | -3.6 | 0.026 | 7/37 (SW480, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.764×** | -3.6 | 0.026 | 11/39 (A498, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.768×** | -3.5 | 0.030 | 15/40 (SW480, SW1417, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -3.2 | 0.075 | 8/28 (A-427, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.791×** | -3.1 | 0.094 | 3/40 (NCI-H1573, A498, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.793×** | -3.1 | 0.094 | 13/36 (SW480, A549, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.724×** | -3.1 | 0.094 | 1/39 (MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.787× | -3.0 | 0.11 | 4/37 (SW48, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 13.2 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.2) |
| [[C-33 A (line)]] | alt | 9.19 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0837× (z -9.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Posaconazole (drug)]] 0.05 µM 0.0774× (z -8.6) |
| [[A-427 (line)]] | wt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.154× (z -10.0) |
| [[A498 (line)]] | wt | 1.82 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0544× (z -9.2) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 7.54 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H23 (line)]] | alt | 8.79 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0826× (z -10.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 15.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.164× (z -9.1) |
| [[SW48 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0848× (z -9.1) ⚠ cell-cycle shift, explains ~13% of this change |
| [[A-172 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.990 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.936 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.706 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02981]] | +0.59 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MYO18B]] | +0.59 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[LINC02245]] | +0.55 | +0.37 / +0.65 | both halves | 8e-05 |  |
| [[MAP1LC3B2]] | +0.54 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[TRD-AS1]] | +0.54 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[ERFL]] | +0.53 | +0.36 / +0.62 | both halves | 9e-05 |  |
| [[GSG1L]] | +0.53 | +0.37 / +0.62 | both halves | 8e-05 |  |
| [[CELF5]] | +0.53 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[PRMT5-DT]] | +0.53 | +0.43 / +0.54 | both halves | 4e-05 |  |
| [[CFAP92]] | +0.52 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[RNF157]] | +0.50 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[MIAT]] | +0.50 | +0.41 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRIP1]] | -0.44 | -0.29 / -0.51 | both halves | 3e-04 |  |
| [[AMACR]] | -0.42 | -0.23 / -0.52 | both halves | 5e-04 |  |
| [[KIAA1586]] | -0.41 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[ZNF214]] | -0.40 | -0.15 / -0.49 | ⚠ not reproduced | 0.001 |  |
| [[HOXA10]] | -0.40 | -0.37 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO4]] | B | ANO4 activity raises SLIT1's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.56× lower at baseline in the lines without ANO4 | 0.056 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent |
| [[EMID1]] | B | EMID1 activity raises SLIT1's level | lines that do not express EMID1 (19) vs lines expressing it (31) | 2.10× lower at baseline in the lines without EMID1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ENSG00000291189, BEGAIN, TBX1; maybe low, not absent |
| [[PSD2]] | B | PSD2 activity raises SLIT1's level | lines that do not express PSD2 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without PSD2 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, CACNA1C, SSC5D; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR143]] | B | SLIT1 activity lowers GPR143's level | lines that do not express SLIT1 (7) vs lines expressing it (43) | 2.29× higher at baseline in the lines without SLIT1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ZNF423, CCNP, TSPEAR; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.382). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.8, 32.4); signed map (30.3, 19.5). **Vector** length 56.1, 8.31% of its response variance represented; |z| ≥ 3 in 962 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.3 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +19.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.3 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.5 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.5 | -6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | slit guidance ligand 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.1 — chr10:96,998,038-97,185,959 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEGF4, Slit-1, SLIT3; previously SLIL1 |
| Gene groups (HGNC) | Slit guidance ligands |
| Hallmark sets | HEDGEHOG_SIGNALING |
| Reactome | 7 pathways, smallest: Regulation of cortical dendrite branching; Regulation of commissural axon pathfinding by SLIT and ROBO; Netrin-1 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O75093](https://www.uniprot.org/uniprotkb/O75093) (Slit homolog 1 protein):

> Thought to act as molecular guidance cue in cellular migration, and function appears to be mediated by interaction with roundabout homolog receptors. During neural development involved in axonal navigation at the ventral midline of the neural tube and projection of axons to different regions (By similarity). SLIT1 and SLIT2 together seem to be essential for midline guidance in the forebrain by acting as repulsive signal preventing inappropriate midline crossing by axons projecting from the …

**Summary**, from NCBI Gene [6585](https://www.ncbi.nlm.nih.gov/gene/6585):

> Enables Roundabout binding activity. Involved in axon extension involved in axon guidance; motor neuron axon guidance; and negative chemotaxis. Predicted to be located in extracellular region. Predicted to be active in obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11085](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11085) · Entrez [6585](https://www.ncbi.nlm.nih.gov/gene/6585) · UniProt [O75093](https://www.uniprot.org/uniprotkb/O75093) · Ensembl [ENSG00000187122](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187122)

## Data

Gene col 11890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11890); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11890]; `tensor/DDL_lfc|DDL_z.npy` [11890]; `embed/gene_vectors.npy` [11890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11890 or target_col == 11890). Every well: [[SLIT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLIT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
