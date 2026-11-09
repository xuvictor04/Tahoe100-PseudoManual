---
drug: "Methylthiouracil"
type: "drug"
salt_base: "Methylthiouracil"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 9
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Methylthiouracil

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 1 / 9; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.06 / 0.09.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:H4 | 1 / 1 | — | +1.13 | +0.2/+0.5/-0.1 | — |
| 0.5 µM | [[Plate 11]]:H4 | 1 / 0 | — | +0.40 | -1.0/-0.8/-1.4 | — |
| 5 µM | [[Plate 12]]:H4 | 5 / 4 | — | +0.91 | +0.4/+0.2/-0.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CFAP210]] 1.83× (z +3.3, 17/47 lines)

**0.5 µM** (1 gene, none with an alert): [[STX17-DT]] 1.25× (z +3.1, 3/47 lines)

**5 µM** (5 genes, none with an alert): [[ATF3]] 1.52× (z +3.2, 26/49 lines), [[JUN]] 1.35× (z +3.0, 21/49 lines), [[TAP1]] 1.21× (z +2.8, 6/48 lines), [[CENPT]] 1.22× (z +2.8, 1/48 lines), [[EIF4A3]] 1.24× (z +2.7, 8/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[MT-ND1]] 0.670× (z -3.2, 43/50 lines)

**5 µM** (4 genes, none with an alert): [[ENSG00000279838]] 0.721× (z -3.1, 6/48 lines), [[ANKUB1]] 0.819× (z -3.1, 7/48 lines), [[PHC2]] 0.828× (z -2.9, 8/49 lines), [[GPAT3]] 0.823× (z -2.9, 7/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 170]] (+2.0) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 9 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Uridine (drug)]] (+0.86, unclear, ⚠ only 6 significant genes); [[Malotilate (drug)]] (+0.73, unclear); [[Artemether (drug)]] (+0.69, unclear, ⚠ only 7 significant genes); [[Pentoxifylline (drug)]] (+0.67, unclear); [[Gefitinib (drug)]] (+0.61, EGFR/ERBB inhibitor); [[Omeprazole (drug)]] (+0.61, unclear); [[Clopidogrel (drug)]] (+0.58, unclear); [[Gemfibrozil (drug)]] (+0.56, unclear, ⚠ only 2 significant genes); [[Cloxacillin (sodium) (drug)]] (+0.49, unclear); [[Allopurinol (drug)]] (+0.47, unclear); [[LJI308 (drug)]] (+0.43, Other MAPK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.82× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[RSPO3]] | 0.05 µM | B | RSPO3 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.81× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[CNRIP1]] | 0.05 µM | B | CNRIP1 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.87× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[ADAM12]] | 0.05 µM | B | ADAM12 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.83× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[BMPER]] | 0.05 µM | B | BMPER activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.85× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.83× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[CCL3]] | 0.05 µM | B | CCL3 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.80× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[ENSG00000259200]] | 0.05 µM | B | ENSG00000259200 activity raises the cells' numbers under Methylthiouracil 0.05 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.85× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[ZC3HAV1L]] | 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Methylthiouracil 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.30× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| [[PWWP2B]] | 0.05 µM | C | PWWP2B activity lowers the cells' numbers under Methylthiouracil 0.05 µM (makes them more sensitive) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 1.39× the cells of the other lines | 0.055 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[PTPN3]] | 0.05 µM | C | PTPN3 activity lowers the cells' numbers under Methylthiouracil 0.05 µM (makes them more sensitive) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 1.34× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| [[RAB11FIP1]] | 0.05 µM | C | RAB11FIP1 activity lowers the cells' numbers under Methylthiouracil 0.05 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.36× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Methylthiouracil"
- `tables/drugdoses.parquet` — dd in 681, 682, 683
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
