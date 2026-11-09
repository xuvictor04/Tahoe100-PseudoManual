---
symbol: "PAX5"
type: "gene"
col: 12129
ensembl_id: "ENSG00000196092"
name: "paired box 5"
location: "9p13.2"
module: 140
arm: "+"
pooled_cpm: 3.46
n_lines_expressing: 32
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# PAX5

*paired box 5* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.42× (z +27.8, q 0e+00, up in 16 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-427 0.0724×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.0776×); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (A-427 0.194×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.183×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC25A48]] (+0.61, fdr 1e-05), [[CDH23]] (+0.60, fdr 9e-06), [[ATP8B4]] (+0.60, fdr 1e-05); moves opposite to [[NSL1]] (-0.46, fdr 2e-04).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[XKR7]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12129.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.42×** | +27.8 | 0e+00 | 16/18 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.23×** | +16.2 | 0e+00 | 2/4 (LoVo, SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **4.56×** | +14.0 | 4e-42 | 20/27 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.46×** | +13.8 | 4e-41 | 4/8 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.25×** | +10.6 | 4e-24 | 7/18 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +9.7 | 4e-20 | 1/4 (SW480) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.91×** | +9.5 | 3e-19 | 4/14 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.32×** | +7.7 | 7e-13 | 13/25 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.13×** | +6.9 | 2e-10 | 9/26 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.94×** | +6.1 | 5e-08 | 8/25 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +5.9 | 2e-07 | 9/27 (PANC-1, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +5.9 | 2e-07 | 5/19 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.2 | 7e-06 | 2/27 (PANC-1, A549) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +4.3 | 7e-04 | 3/20 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.42×** | +4.3 | 7e-04 | 0/6 | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.008 | 1/11 (HOP62) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.014 | 4/24 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.67×** | +3.4 | 0.019 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.46×** | +3.2 | 0.033 | 0/11 | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +3.1 | 0.041 | 1/9 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.044 | 1/11 (SW480) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12129.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (A-427 0.0724×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.0776×); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.103×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (A-427 0.194×); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.183×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Asciminib (drug)]] 0.5 µM |  | 0.696× | -3.4 | 0.44 | 6/26 (NCI-H2347, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12129. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 25.8 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0724× (z -14.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0776× (z -13.7) |
| [[LoVo (line)]] | wt | 17.1 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.03× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.203× (z -8.7) |
| [[PANC-1 (line)]] | alt | 1.28 | 4 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 59.6× (z +12.3) | — |
| [[A549 (line)]] | wt | 1.18 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.2× (z +9.0) | — |
| [[SW480 (line)]] | alt | 8.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.2) | — |
| [[A-172 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.721 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.741 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.705 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.831 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.704 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.891 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.949 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.710 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.778 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.696 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.670 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12129), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A48]] | +0.61 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[CDH23]] | +0.60 | +0.58 / +0.57 | both halves | 9e-06 | same gene group |
| [[ATP8B4]] | +0.60 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[AATK]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[SGCZ]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 | same gene group |
| [[LINC00578]] | +0.58 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[RBFOX3]] | +0.58 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SSTR2]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[GRHL3]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CFAP92]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[WIPF3]] | +0.56 | +0.57 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSL1]] | -0.46 | -0.39 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XKR7]] | B | XKR7 activity raises PAX5's level | lines that do not express XKR7 (39) vs lines expressing it (11) | 2.81× lower at baseline in the lines without XKR7 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, LINC01205, BMP5 |
| [[MAPK8IP2]] | B | MAPK8IP2 activity raises PAX5's level | lines that do not express MAPK8IP2 (18) vs lines expressing it (32) | 1.63× lower at baseline in the lines without MAPK8IP2 | 0.072 | ⚠ within organs, on part of the lines; also absent: AP3B2, FBXO27, LTB; maybe low, not absent |
| [[ENTREP2]] | B | ENTREP2 activity raises PAX5's level | lines that do not express ENTREP2 (22) vs lines expressing it (28) | 1.92× lower at baseline in the lines without ENTREP2 | 0.081 | ⚠ within organs, on part of the lines; also absent: TBX1, JPH3, MAPK4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PAX5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.572). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.9, 35.8); signed map (33.0, 18.9). **Vector** length 34.5, 5.02% of its response variance represented; |z| ≥ 3 in 658 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +27.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +13.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +0.5 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | paired box 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:36,833,269-37,034,268 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BSAP, PAX-5 |
| Gene groups (HGNC) | PRD class homeoboxes and pseudogenes; Paired boxes; MicroRNA protein coding host genes |
| Reactome | 6 pathways, smallest: RUNX1 regulates transcription of genes involved in BCR signaling; Transcriptional regulation by RUNX1; Somatic hypermutation of immunoglobulin genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02548](https://www.uniprot.org/uniprotkb/Q02548) (Paired box protein Pax-5):

> Transcription factor that plays an essential role in commitment of lymphoid progenitors to the B-lymphocyte lineage. Fulfills a dual role by repressing B-lineage inappropriate genes and simultaneously activating B-lineage-specific genes. In turn, regulates cell adhesion and migration, induces V(H)-to-D(H)J(H) recombination, facilitates pre-B-cell receptor signaling and promotes development to the mature B-cell stage. Repression of the cohesin-release factor WAPL causes global changes of the …

**Summary**, from NCBI Gene [5079](https://www.ncbi.nlm.nih.gov/gene/5079):

> This gene encodes a member of the paired box (PAX) family of transcription factors. The central feature of this gene family is a novel, highly conserved DNA-binding motif, known as the paired box. Paired box transcription factors are important regulators in early development, and alterations in the expression of their genes are thought to contribute to neoplastic transformation. This gene encodes the B-cell lineage specific activator protein that is expressed at early, but not late stages of …

**Accessions** — [HGNC:8619](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8619) · Entrez [5079](https://www.ncbi.nlm.nih.gov/gene/5079) · UniProt [Q02548](https://www.uniprot.org/uniprotkb/Q02548) · Ensembl [ENSG00000196092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196092)

## Data

Gene col 12129: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12129); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12129, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12129]; `tensor/DDL_lfc|DDL_z.npy` [12129]; `embed/gene_vectors.npy` [12129]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12129 or target_col == 12129). Every well: [[PAX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
