---
drug: "Sodium Salicylate"
type: "drug"
salt_base: "Sodium Salicylate"
targets: "PTGS2"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 27
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Sodium Salicylate

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 14 / 27; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.45 / 0.40.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:B3 | 1 / 1 | — | -0.03 | -1.0/+1.5/-0.3 | — |
| 0.5 µM | [[Plate 05]]:B3 | 6 / 8 | — | -0.14 | -1.6/+0.8/-1.2 | — |
| 5 µM | [[Plate 14]]:B3 | 13 / 14 | 0.838 | +0.11 | -1.0/+3.1/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[GRHL3]] 1.34× (z +2.9, 0/27 lines)

**0.5 µM** (6 genes, none with an alert): [[AMPH]] 1.47× (z +3.5, 0/11 lines), [[FPGT]] 1.25× (z +3.3, 8/47 lines), [[ENSG00000285827]] 1.21× (z +3.1, 11/48 lines), [[CCDC183]] 1.31× (z +3.1, 2/40 lines), [[BEST1]] 1.35× (z +2.9, 13/44 lines), [[HPSE]] 1.27× (z +2.9, 2/32 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[PRR11]] 1.25× (z +3.7, 29/47 lines), [[SAP30]] 1.33× (z +3.6, 22/48 lines), [[ENSG00000291075]] 1.22× (z +3.6, 4/46 lines), [[HMMR]] 1.26× (z +3.5, 20/48 lines), [[TNFAIP8L1]] 1.22× (z +3.4, 10/47 lines), [[CROCCP2-1]] 1.33× (z +3.3, 25/48 lines), [[ENSG00000260912]] 1.37× (z +3.3, 6/42 lines), [[ENSG00000291174]] 1.22× (z +3.2, 19/46 lines), [[MARCHF2]] 1.22× (z +3.2, 7/48 lines), [[LINC01687]] 1.30× (z +3.0, 0/17 lines), [[CCN2]] 1.26× (z +3.0, 3/31 lines), [[CDKN3]] 1.24× (z +2.9, 11/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[STRA6]] 0.731× (z -2.8, 4/21 lines)

**0.5 µM** (8 genes, none with an alert): [[CREB5]] 0.808× (z -3.8, 13/33 lines), [[DVL2]] 0.809× (z -3.6, 10/47 lines), [[TMEM116]] 0.785× (z -3.6, 14/47 lines), [[LINC02977]] 0.745× (z -3.6, 4/34 lines), [[TARS1]] 0.829× (z -3.5, 21/48 lines), [[TFRC]] 0.735× (z -3.4, 38/48 lines), [[FIGNL1]] 0.803× (z -3.3, 11/46 lines), [[DPYSL4]] 0.703× (z -3.3, 4/20 lines)

**5 µM** (14 genes, none with an alert; 12 shown): [[TFRC]] 0.693× (z -5.8, 48/49 lines), [[KBTBD8]] 0.735× (z -4.0, 15/41 lines), [[AOC2]] 0.727× (z -4.0, 13/45 lines), [[CCDC13]] 0.741× (z -4.0, 8/44 lines), [[SNHG1]] 0.754× (z -3.9, 29/48 lines), [[ENSG00000286230]] 0.730× (z -3.9, 6/44 lines), [[RPE]] 0.824× (z -3.8, 22/48 lines), [[OCRL]] 0.831× (z -3.4, 20/48 lines), [[NOMO2]] 0.789× (z -3.4, 12/48 lines), [[ENSG00000268403]] 0.753× (z -3.4, 9/44 lines), [[ENSG00000254979]] 0.759× (z -3.4, 2/25 lines), [[PLAGL2]] 0.819× (z -3.4, 15/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H2122 (line)]] (1.41), [[MIA PaCa-2 (line)]] (1.28), [[COLO 205 (line)]] (1.28), [[RKO (line)]] (1.27) · weakest: [[C32 (line)]] (0.556), [[HepG2_C3A (line)]] (0.636), [[BT-474 (line)]] (0.675) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Azithromycin (hydrate) (drug)]] (+0.63, unclear); [[Bendamustine (drug)]] (+0.58, DNA synthesis/repair inhibitor); [[Resveratrol (drug)]] (+0.56, unclear); [[Tranilast (drug)]] (+0.56, unclear, ⚠ only 6 significant genes); [[Decitabine (drug)]] (+0.54, DNA methyltransferase inhibitor); [[Ligustrazine (drug)]] (+0.53, unclear, ⚠ only 2 significant genes); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.53, unclear); [[Gallic acid (hydrate) (drug)]] (+0.51, Cyclooxygenase inhibitor); [[MK-3903 (drug)]] (+0.48, unclear); [[Methylprednisolone succinate (drug)]] (+0.48, Glucocorticoid receptor agonist)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 28 arrows, 28 of them with an alert ⚠; grade A 0, B 23, C 5. Shown: the 15 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[TCEAL3]] | 0.5 µM | B | TCEAL3 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express TCEAL3 (7) vs lines expressing it (41) | the lines without TCEAL3: 1.23× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |
| [[PMP22]] | 0.5 µM | B | PMP22 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express PMP22 (10) vs lines expressing it (38) | the lines without PMP22: 1.16× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[ENSG00000281091]] | 0.5 µM | B | ENSG00000281091 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000281091 (12) vs lines expressing it (36) | the lines without ENSG00000281091: 1.16× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, TGFB1I1, AKT3 |
| [[CCDC80]] | 5 µM | B | CCDC80 activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express CCDC80 (21) vs lines expressing it (27) | the lines without CCDC80: 1.11× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[TMSB4X]] | 5 µM | B | TMSB4X activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express TMSB4X (9) vs lines expressing it (39) | the lines without TMSB4X: 1.11× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: PRSS23, TCN2; maybe low, not absent |
| [[P3H3]] | 0.5 µM | B | P3H3 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express P3H3 (10) vs lines expressing it (38) | the lines without P3H3: 1.19× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[P3H3]] | 5 µM | B | P3H3 activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express P3H3 (10) vs lines expressing it (38) | the lines without P3H3: 1.12× the cells of the other lines | 0.059 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[SCNN1A]] | 0.5 µM | B | SCNN1A activity raises the cells' numbers under Sodium Salicylate 0.5 µM (protects the cells) | lines that do not express SCNN1A (27) vs lines expressing it (21) | the lines without SCNN1A: 0.85× the cells of the other lines | 0.067 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[CLIP4]] | 0.5 µM | B | CLIP4 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express CLIP4 (12) vs lines expressing it (36) | the lines without CLIP4: 1.19× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: RTL8C, ENSG00000289526, MSN |
| [[CLIP4]] | 5 µM | B | CLIP4 activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express CLIP4 (12) vs lines expressing it (36) | the lines without CLIP4: 1.10× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: RTL8C, ENSG00000289526, MSN |
| [[FAM110C]] | 0.5 µM | B | FAM110C activity raises the cells' numbers under Sodium Salicylate 0.5 µM (protects the cells) | lines that do not express FAM110C (26) vs lines expressing it (22) | the lines without FAM110C: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PRR15, PLEKHG6 |
| [[ESRP1]] | 0.5 µM | B | ESRP1 activity raises the cells' numbers under Sodium Salicylate 0.5 µM (protects the cells) | lines that do not express ESRP1 (31) vs lines expressing it (17) | the lines without ESRP1: 0.83× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ST14, KDF1, CLDN7 |
| [[PRR15-DT]] | 0.5 µM | B | PRR15-DT activity raises the cells' numbers under Sodium Salicylate 0.5 µM (protects the cells) | lines that do not express PRR15-DT (25) vs lines expressing it (23) | the lines without PRR15-DT: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PRR15, FAM110C, PLEKHG6; maybe low, not absent |
| [[ADGRB2]] | 0.5 µM | B | ADGRB2 activity lowers the cells' numbers under Sodium Salicylate 0.5 µM (makes them more sensitive) | lines that do not express ADGRB2 (7) vs lines expressing it (41) | the lines without ADGRB2: 1.16× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[CD109]] | 5 µM | B | CD109 activity lowers the cells' numbers under Sodium Salicylate 5 µM (makes them more sensitive) | lines that do not express CD109 (15) vs lines expressing it (33) | the lines without CD109: 1.09× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: KMO, PID1, EVA1A-AS |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Sodium Salicylate"
- `tables/drugdoses.parquet` — dd in 958, 959, 960
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
