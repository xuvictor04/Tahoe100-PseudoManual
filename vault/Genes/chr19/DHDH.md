---
symbol: "DHDH"
type: "gene"
col: 2499
ensembl_id: "ENSG00000104808"
name: "dihydrodiol dehydrogenase"
location: "19q13.33"
module: 53
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# DHDH

*dihydrodiol dehydrogenase* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.70× (z +19.0, q 0e+00, up in 34 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.413× (z -6.8, q 4e-09, down in 27 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CPT1C]] (+0.74, fdr 7e-06), [[SPSB2]] (+0.72, fdr 7e-06), [[PHKG1]] (+0.70, fdr 1e-05); moves opposite to [[EFTUD2]] (-0.60, fdr 7e-06), [[GFM1]] (-0.59, fdr 2e-05), [[TMEM33]] (-0.59, fdr 1e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.70×** | +19.0 | 0e+00 | 34/35 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.20×** | +12.7 | 1e-34 | 28/36 (LoVo, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **4.33×** | +11.3 | 2e-27 | 33/41 (A-172, C32, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **3.03×** | +8.6 | 1e-15 | 28/43 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +7.2 | 6e-11 | 17/24 (NCI-H2347, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +7.0 | 3e-10 | 27/41 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.36×** | +6.6 | 3e-09 | 18/36 (hTERT-HPNE, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.35×** | +6.6 | 3e-09 | 23/41 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.82×** | +6.6 | 4e-09 | 15/43 (HEC-1-A, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +6.3 | 2e-08 | 18/36 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.90×** | +4.8 | 8e-05 | 1/6 (SW1417) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +4.8 | 9e-05 | 19/42 (HT-29, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +4.4 | 6e-04 | 12/31 (MIA PaCa-2, C32, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.62×** | +3.7 | 0.008 | 13/41 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.026 | 6/41 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.038 | 4/41 (C-33 A, Panc 03.27, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +3.2 | 0.046 | 3/31 (SW1417, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2499.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.413×** | -6.8 | 4e-09 | 27/41 (CFPAC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.500×** | -5.4 | 2e-05 | 23/41 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.531×** | -4.9 | 2e-04 | 22/44 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.607×** | -3.9 | 0.016 | 18/40 (C32, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | 0.755× | -3.1 | 0.24 | 9/42 (SHP-77, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -10.5) |
| [[SW480 (line)]] | alt | 2.44 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.82× (z +10.2) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0854× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 7.86 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 2.56 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 2.16 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +9.6) | — |
| [[A498 (line)]] | wt | 5.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.26× (z +9.8) | — |
| [[A549 (line)]] | wt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.96× (z +9.4) | — |
| [[C32 (line)]] | wt | 6.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.69× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 6.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.51× (z +9.2) | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +9.1) | — |
| [[hTERT-HPNE (line)]] | wt | 2.89 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.4× (z +11.4) | — |
| [[KATO III (line)]] | alt | 6.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.54× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 4.16 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0460× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 1.47 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.0× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 3.57 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +8.5) | — |
| [[A-172 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1C]] | +0.74 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[SPSB2]] | +0.72 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.70 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[LRRC23]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[GGT1]] | +0.70 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[FAM53C]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[TINCR]] | +0.68 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[SPACDR]] | +0.67 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.66 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[CDKL2]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[RYR1]] | +0.65 | +0.62 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.60 | -0.65 / -0.59 | both halves | 7e-06 |  |
| [[GFM1]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[TMEM33]] | -0.59 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[VMA21]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[RPE]] | -0.56 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ATIC]] | -0.56 | -0.38 / -0.65 | both halves | 6e-05 |  |
| [[PRPF19]] | -0.56 | -0.46 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DHDH's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PTPN6]] | B | PTPN6 activity raises DHDH's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without PTPN6 | 0.071 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[CRABP2]] | B | CRABP2 activity raises DHDH's level | lines that do not express CRABP2 (24) vs lines expressing it (26) | 1.28× lower at baseline in the lines without CRABP2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ESPN, ACP7, HAS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.704). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.3, -24.8); signed map (12.1, 15.8). **Vector** length 80.0, 15.4% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +19.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +3.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.6 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.2 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.5 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.3 | -5.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.2 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.7 | -1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | dihydrodiol dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,933,699-48,944,969 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUM2DD |
| Gene groups (HGNC) | Gfo/Idh/MocA-like oxidoreductase domain containing; Oxidoreductases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ10](https://www.uniprot.org/uniprotkb/Q9UQ10) (Trans-1,2-dihydrobenzene-1,2-diol dehydrogenase):

> Catalyzes the NADP(+)-linked oxidation of trans-dihydrodiols of aromatic hydrocarbons to the corresponding catechols. It also catalyzes the oxidation of several pentoses and hexoses. In the reverse reaction in the presence of NADPH, it acts as NADPH-linked reductase on a broad range of substrates including aldehydes, chetones, and alpha-dicarbonyl compounds such as 3-deoxyglucosone, camphorquinone and methylglyoxal.

**Summary**, from NCBI Gene [27294](https://www.ncbi.nlm.nih.gov/gene/27294):

> This gene encodes an enzyme that belongs to the family of dihydrodiol dehydrogenases, which exist in multiple forms in mammalian tissues and are involved in the metabolism of xenobiotics and sugars. These enzymes catalyze the NADP1-linked oxidation of transdihydrodiols of aromatic hydrocarbons to corresponding catechols. This enzyme is a dimeric dihydrodiol dehydrogenase, and it differs from monomeric dihydrodiol dehydrogenases in its high substrate specificity for trans-dihydrodiols of …

**Accessions** — [HGNC:17887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17887) · Entrez [27294](https://www.ncbi.nlm.nih.gov/gene/27294) · UniProt [Q9UQ10](https://www.uniprot.org/uniprotkb/Q9UQ10) · Ensembl [ENSG00000104808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104808)

## Data

Gene col 2499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2499); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2499]; `tensor/DDL_lfc|DDL_z.npy` [2499]; `embed/gene_vectors.npy` [2499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2499 or target_col == 2499). Every well: [[DHDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
