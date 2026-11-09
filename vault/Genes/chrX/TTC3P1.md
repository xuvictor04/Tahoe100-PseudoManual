---
symbol: "TTC3P1"
type: "gene"
col: 13245
ensembl_id: "ENSG00000215105"
name: "tetratricopeptide repeat domain 3 pseudogene 1"
location: "Xq13.3"
module: 45
arm: "+"
pooled_cpm: 3.49
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# TTC3P1

*tetratricopeptide repeat domain 3 pseudogene 1* — Xq13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.70× (z +11.3, q 8e-27, up in 4 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.15× (z +9.7, q 6e-20, up in 36 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.445× (z -7.3, q 2e-10, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC110]] (+0.61, fdr 2e-05), [[NBEA]] (+0.60, fdr 4e-05), [[IFTAP]] (+0.59, fdr 1e-05); moves opposite to [[AOC2]] (-0.57, fdr 2e-04), [[S100PBP]] (-0.57, fdr 5e-05), [[NDOR1]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.70×** | +11.3 | 8e-27 | 4/4 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.15×** | +9.7 | 6e-20 | 36/44 (SW480, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +9.1 | 2e-17 | 13/15 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.97×** | +6.1 | 2e-07 | 26/45 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.93×** | +5.7 | 1e-06 | 21/46 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +5.5 | 3e-06 | 19/43 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +5.1 | 3e-05 | 21/46 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.59×** | +3.8 | 0.008 | 2/6 (HEC-1-A, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.79×** | +3.6 | 0.017 | 1/7 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.021 | 5/44 (HOP62, A-427, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +3.5 | 0.023 | 5/19 (HOP62, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.054 | 12/43 (RKO, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.40× | +3.0 | 0.10 | 3/45 (HEC-1-A, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13245.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.445×** | -7.3 | 2e-10 | 29/45 (HS-578T, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.464×** | -6.9 | 2e-09 | 26/46 (SNU-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.527×** | -5.7 | 2e-06 | 20/43 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -5.5 | 6e-06 | 20/33 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.615×** | -4.4 | 0.001 | 17/33 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.637×** | -3.9 | 0.007 | 11/46 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -3.8 | 0.014 | 16/47 (Panc 03.27, C-33 A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.679×** | -3.4 | 0.046 | 9/41 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.676×** | -3.4 | 0.046 | 15/32 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.706×** | -3.1 | 0.099 | 9/35 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.525× | -3.0 | 0.12 | 8/35 (SNU-423, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | 0.525× | -3.0 | 0.12 | 11/40 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3.19 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0459× (z -9.1) |
| [[LoVo (line)]] | wt | 3.86 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 3.42 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0564× (z -8.6) |
| [[PANC-1 (line)]] | alt | 3.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC110]] | +0.61 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[NBEA]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[IFTAP]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[SMIM30]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[MNAT1]] | +0.56 | +0.21 / +0.56 | both halves | 7e-04 |  |
| [[KCTD17]] | +0.56 | +0.18 / +0.56 | ⚠ one half (not replicated) | 1e-03 |  |
| [[LINC00173]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CFD]] | +0.56 | +0.19 / +0.53 | ⚠ one half (not replicated) | 9e-04 |  |
| [[OSBPL9]] | +0.56 | +0.38 / +0.40 | both halves | 6e-05 |  |
| [[SUSD4]] | +0.55 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[CCDC112]] | +0.55 | +0.22 / +0.54 | both halves | 6e-04 |  |
| [[VWA5A]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[USP9X]] | +0.54 | +0.29 / +0.43 | both halves | 2e-04 |  |
| [[CDC73]] | +0.54 | +0.37 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AOC2]] | -0.57 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[S100PBP]] | -0.57 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[NDOR1]] | -0.54 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[PRDM10]] | -0.54 | -0.25 / -0.57 | both halves | 4e-04 |  |
| [[SUV39H2]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[MSL1]] | -0.53 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[METTL4]] | -0.53 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[DBF4B]] | -0.52 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[DHRS11]] | -0.52 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[DDX59]] | -0.51 | -0.11 / -0.48 | ⚠ not reproduced | 0.002 |  |
| [[PRDM15]] | -0.51 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[SAP30L-AS1]] | -0.51 | -0.23 / -0.26 | both halves | 5e-04 |  |
| [[IGF2BP1]] | -0.50 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers TTC3P1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LINC00173]] | B | LINC00173 activity raises TTC3P1's level | lines that do not express LINC00173 (18) vs lines expressing it (32) | 1.22× lower at baseline in the lines without LINC00173 | 0.097 | ⚠ within organs, on part of the lines; also absent: GBX1, RAB3C, NOVA2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.484). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-21.5, 29.1); signed map (-7.2, 13.0). **Vector** length 49.6, 6.17% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +9.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.9 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.3 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | +6.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +1.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -0.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.8 | -0.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | tetratricopeptide repeat domain 3 pseudogene 1 |
| Locus type | pseudogene |
| Location | Xq13.3 — chrX:75,740,831-75,746,911 (-) |
| Ensembl biotype | processed_pseudogene |
| Also known as | RNF105L; previously TTC3L |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23318](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23318) · Entrez [286495](https://www.ncbi.nlm.nih.gov/gene/286495) · Ensembl [ENSG00000215105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215105)

## Data

Gene col 13245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13245); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13245]; `tensor/DDL_lfc|DDL_z.npy` [13245]; `embed/gene_vectors.npy` [13245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13245 or target_col == 13245). Every well: [[TTC3P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTC3P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
