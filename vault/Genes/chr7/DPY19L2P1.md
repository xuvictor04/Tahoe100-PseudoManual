---
symbol: "DPY19L2P1"
type: "gene"
col: 12104
ensembl_id: "ENSG00000189212"
name: "DPY19L2 pseudogene 1"
location: "7p14.2"
module: 9
arm: "+"
pooled_cpm: 9.44
n_lines_expressing: 24
n_dd_up: 25
n_dd_down: 6
n_dd_up_clean: 11
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# DPY19L2P1

*DPY19L2 pseudogene 1* — 7p14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +11.2, q 2e-26, up in 13 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.691× (z -4.5, q 0.005, down in 12 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DPY19L2P2-1]] (+0.64, fdr 7e-06), [[FMN2]] (+0.58, fdr 1e-05), [[NEGR1]] (+0.57, fdr 2e-05); moves opposite to [[RNF14]] (-0.53, fdr 2e-05), [[NRBP1]] (-0.47, fdr 2e-05), [[UMAD1]] (-0.46, fdr 5e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DPY19L2]] → it (grade C ⚠); 4 go from it, the strongest it → [[MYBL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12104.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +11.2 | 2e-26 | 13/22 (LOX-IMVI, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.51×** | +10.6 | 6e-24 | 2/11 (NCI-H2347, LOX-IMVI) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +10.5 | 1e-23 | 14/22 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +9.4 | 6e-19 | 8/21 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +7.9 | 3e-13 | 18/21 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.02×** | +7.6 | 4e-12 | 3/16 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.87×** | +7.2 | 4e-11 | 11/19 (A-172, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.70×** | +6.4 | 1e-08 | 13/21 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.77×** | +6.4 | 1e-08 | 4/14 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.62×** | +5.8 | 4e-07 | 15/21 (NCI-H460, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.60×** | +5.7 | 7e-07 | 11/20 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.54×** | +5.2 | 9e-06 | 14/21 (NCI-H2347, A-172, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +4.6 | 2e-04 | 17/22 (NCI-H2347, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.001 | 6/21 (SNU-423, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.41×** | +4.1 | 0.001 | 6/20 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +4.1 | 0.001 | 13/21 (A-172, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.40×** | +3.7 | 0.006 | 6/19 (A-172, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.024 | 8/21 (NCI-H23, PANC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.024 | 7/21 (PANC-1, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12104.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -4.5 | 0.005 | 12/21 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -4.2 | 0.007 | 14/21 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.701×** | -4.1 | 0.007 | 12/21 (NCI-H23, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.733×** | -3.7 | 0.025 | 8/21 (H4, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.759×** | -3.3 | 0.086 | 13/21 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Resveratrol (drug)]] 5 µM |  | **0.824×** | -3.3 | 0.086 | 8/22 (H4, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12104. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 40.8 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -11.4) |
| [[A549 (line)]] | wt | 14.8 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +13.2) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.143× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 32.3 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.84× (z +21.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -10.5) |
| [[A-172 (line)]] | wt | 9.16 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.23× (z +13.8) | — |
| [[A-427 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.0) ⚠ cell-cycle shift, explains ~91% of this change |
| [[H4 (line)]] | wt | 49.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0897× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HOP62 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0941× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 5.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.6× (z +12.0) | — |
| [[NCI-H2347 (line)]] | alt | 4.35 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.46× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 9.50 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.102× (z -8.6) |
| [[SNU-423 (line)]] | alt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.58× (z +15.7) | — |
| [[A498 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.823 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.801 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.882 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.764 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.963 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.859 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.860 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.914 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.929 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12104), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L2P2-1]] | +0.64 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[FMN2]] | +0.58 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[NEGR1]] | +0.57 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[FAM184A]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[TERT]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CAMK4]] | +0.56 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ADAMTS3]] | +0.55 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ADAM22]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SLFN11]] | +0.55 | +0.63 / +0.44 | both halves | 3e-05 |  |
| [[MMP16]] | +0.54 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[DPY19L2]] | +0.54 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ANKRD20A7P]] | +0.54 | +0.40 / +0.53 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF14]] | -0.53 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[NRBP1]] | -0.47 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[UMAD1]] | -0.46 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[ZDHHC24]] | -0.46 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[YPEL5]] | -0.45 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[SHARPIN]] | -0.45 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[AAMP]] | -0.44 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[ATXN3]] | -0.44 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[NUDT16-DT]] | -0.44 | -0.36 / -0.44 | both halves | 9e-05 |  |
| [[PRR13]] | -0.44 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ATP6V1E1]] | -0.44 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[TMEM234]] | -0.43 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L2]] | C | DPY19L2 activity raises DPY19L2P1's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 3.78× lower at baseline in the lines without DPY19L2 | 0.088 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | DPY19L2P1 activity raises MYBL1's level | lines that do not express DPY19L2P1 (26) vs lines expressing it (24) | 2.14× lower at baseline in the lines without DPY19L2P1 | 0.084 | ⚠ within organs, on part of the lines; also absent: STAC, RNF180, SRGN |
| cells under [[Sulfatinib (drug)]] 0.5 µM | B | DPY19L2P1 activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express DPY19L2P1 (26) vs lines expressing it (22) | the lines without DPY19L2P1: 1.22× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: STAC, RNF180, SRGN |
| [[FAT4]] | C | DPY19L2P1 activity raises FAT4's level | lines that do not express DPY19L2P1 (26) vs lines expressing it (24) | 4.91× lower at baseline in the lines without DPY19L2P1 | 0.066 | ⚠ within organs, on part of the lines; also absent: STAC, RNF180, SRGN; co-absent with the target |
| [[ADRA1B]] | C | DPY19L2P1 activity raises ADRA1B's level | lines that do not express DPY19L2P1 (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without DPY19L2P1 | 0.070 | ⚠ within organs, on part of the lines; also absent: STAC, RNF180, SRGN; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.444). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (32.3, 29.0); signed map (30.8, 32.2). **Vector** length 59.5, 15.8% of its response variance represented; |z| ≥ 3 in 526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.6 | +6.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +11.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +3.3 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +2.4 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.5 | +1.3 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.8 | -4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | DPY19L2 pseudogene 1 |
| Locus type | pseudogene |
| Location | 7p14.2 — chr7:35,081,590-35,186,041 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NXN4](https://www.uniprot.org/uniprotkb/Q6NXN4) (Putative C-mannosyltransferase DPY19L2P1):

> Probable C-mannosyltransferase that mediates C-mannosylation of tryptophan residues on target proteins.

**Summary**, from NCBI Gene [554236](https://www.ncbi.nlm.nih.gov/gene/554236):

> Predicted to enable glycosyltransferase activity. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22305](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22305) · Entrez [554236](https://www.ncbi.nlm.nih.gov/gene/554236) · UniProt [Q6NXN4](https://www.uniprot.org/uniprotkb/Q6NXN4) · Ensembl [ENSG00000189212](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189212)

## Data

Gene col 12104: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12104); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12104, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12104]; `tensor/DDL_lfc|DDL_z.npy` [12104]; `embed/gene_vectors.npy` [12104]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12104 or target_col == 12104). Every well: [[DPY19L2P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPY19L2P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
