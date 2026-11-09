---
symbol: "CCK"
type: "gene"
col: 11884
ensembl_id: "ENSG00000187094"
name: "cholecystokinin"
location: "3p22.1"
module: 34
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 8
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CCK

*cholecystokinin* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 9.72× (z +9.8, q 1e-19, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 3.57× (z +8.0, q 2e-13, up in 5 of 5 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.179×; ⚠ cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.123×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYPD3]] (+0.58, fdr 1e-05), [[SH3BGRL3]] (+0.58, fdr 3e-05), [[PLIN3]] (+0.57, fdr 3e-05); moves opposite to [[PIP5K1B]] (-0.50, fdr 3e-05), [[MGAM2]] (-0.49, fdr 4e-05), [[PLEKHA3]] (-0.49, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[PMEL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11884.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.72×** | +9.8 | 1e-19 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **6.15×** | +8.1 | 2e-13 | 1/2 (KATO III) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.57×** | +8.0 | 2e-13 | 5/5 (BT-474, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.33×** | +7.6 | 4e-12 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.89×** | +6.7 | 2e-09 | 2/4 (KATO III, BT-474) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **3.39×** | +5.4 | 5e-06 | 4/5 (KATO III, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.50×** | +5.4 | 6e-06 | 2/3 (KATO III, BT-474) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.26×** | +5.3 | 1e-05 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.16×** | +5.1 | 2e-05 | 5/5 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.08×** | +4.6 | 2e-04 | 0/5 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.03×** | +4.1 | 0.002 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.86×** | +3.9 | 0.005 | 0/4 | top dose only | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.27×** | +3.7 | 0.011 | 4/5 (KATO III, BT-474, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.26×** | +3.6 | 0.011 | 2/4 (SNU-1, KATO III) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **2.32×** | +3.6 | 0.012 | 0/2 | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.21×** | +3.5 | 0.014 | 3/4 (BT-474, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.97×** | +3.0 | 0.065 | 2/2 (SNU-1, KATO III) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11884.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SNU-1 0.179×; ⚠ cell-cycle shift, explains ~36% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (SNU-1 0.123×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.447× | -3.6 | 0.18 | 0/5 | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.457× | -3.2 | 0.34 | 0/5 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11884. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 9.36 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 16.4× (z +9.5) | — |
| [[SNU-1 (line)]] | wt | 195 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -10.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.207 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.203 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.500 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.319 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.468 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.465 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.312 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.232 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.307 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.242 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.289 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.246 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.355 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.319 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.206 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.244 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.261 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.344 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.899 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.614 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.729 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.570 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.272 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11884), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPD3]] | +0.58 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SH3BGRL3]] | +0.58 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[PLIN3]] | +0.57 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[AMN1]] | +0.53 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[GOLT1A]] | +0.53 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[DKK1]] | +0.49 | +0.30 / +0.51 | both halves | 2e-04 |  |
| [[PSD3]] | +0.49 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[S100A6]] | +0.48 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[PTAFR]] | +0.48 | +0.39 / +0.44 | both halves | 6e-05 | pathway: Class A/1 (Rhodopsin-like receptors) |
| [[AREG]] | +0.48 | +0.38 / +0.48 | both halves | 6e-05 |  |
| [[TMSB10]] | +0.48 | +0.34 / +0.40 | both halves | 1e-04 |  |
| [[OTUD7A]] | +0.47 | +0.18 / +0.40 | ⚠ not reproduced | 9e-04 |  |
| [[TIAM1]] | +0.47 | +0.30 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIP5K1B]] | -0.50 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[MGAM2]] | -0.49 | -0.46 / -0.43 | both halves | 4e-05 |  |
| [[PLEKHA3]] | -0.49 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[NHLRC3]] | -0.47 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ARHGEF9]] | -0.47 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[FAAH2]] | -0.46 | -0.29 / -0.42 | both halves | 2e-04 |  |
| [[MGC32805]] | -0.45 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[NNT]] | -0.43 | -0.29 / -0.45 | both halves | 2e-04 |  |
| [[ERBB3]] | -0.43 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[HNF1A]] | -0.42 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[CRACR2A]] | -0.42 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[UGT1A9]] | -0.42 | -0.25 / -0.45 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMEL]] | B | CCK activity raises PMEL's level | lines that do not express CCK (42) vs lines expressing it (8) | 1.06× lower at baseline in the lines without CCK | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: BMP10, ENSG00000287530, S100A8 |
| [[ARFGEF2]] | B | CCK activity raises ARFGEF2's level | lines that do not express CCK (42) vs lines expressing it (8) | 1.39× lower at baseline in the lines without CCK | 0.098 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: BMP10, ENSG00000287530, S100A8 |
| [[LINC00698]] | C | CCK activity raises LINC00698's level | lines that do not express CCK (42) vs lines expressing it (8) | 1.17× lower at baseline in the lines without CCK | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: BMP10, ENSG00000287530, S100A8; co-absent with the target |
| [[MGAM2]] | C | CCK activity raises MGAM2's level | lines that do not express CCK (42) vs lines expressing it (8) | 3.06× lower at baseline in the lines without CCK | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: BMP10, ENSG00000287530, S100A8; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.421). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.0, 0.7); signed map (46.6, -12.9). **Vector** length 14.8, 4.94% of its response variance represented; |z| ≥ 3 in 96 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +8.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.8 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +0.7 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.3 | -0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.3 | +0.0 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | +0.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | +1.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | -0.3 | +3.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.3 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.3 | -1.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.3 | +0.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.2 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | cholecystokinin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.1 — chr3:42,257,825-42,266,185 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neuropeptides |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P06307](https://www.uniprot.org/uniprotkb/P06307) (Cholecystokinin):

> This peptide hormone induces gall bladder contraction and the release of pancreatic enzymes in the gut. Its function in the brain is not clear. Binding to CCK-A receptors stimulates amylase release from the pancreas, binding to CCK-B receptors stimulates gastric acid secretion.

**Summary**, from NCBI Gene [885](https://www.ncbi.nlm.nih.gov/gene/885):

> This gene encodes a member of the gastrin/cholecystokinin family of proteins. The encoded preproprotein is proteolytically processed to generate multiple protein products, including the peptide hormones cholecystokinin-8, -12, -33, and others. The encoded peptides have been shown to regulate gastric acid secretion and food intake. A sulfated form of cholecystokinin-8 may modulate neuronal activity in the brain. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:1569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1569) · Entrez [885](https://www.ncbi.nlm.nih.gov/gene/885) · UniProt [P06307](https://www.uniprot.org/uniprotkb/P06307) · Ensembl [ENSG00000187094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187094)

## Data

Gene col 11884: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11884); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11884, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11884]; `tensor/DDL_lfc|DDL_z.npy` [11884]; `embed/gene_vectors.npy` [11884]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11884 or target_col == 11884). Every well: [[CCK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
