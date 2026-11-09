---
drug: "Bentamapimod"
type: "drug"
salt_base: "Bentamapimod"
targets: "MAPK8, MAPK9, MAPK10"
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 131
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bentamapimod

*Other MAPK inhibitor (inhibitor/antagonist) · targets: MAPK8, MAPK9, MAPK10 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 131 / 0 / 54; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.23 / 0.19.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C6 | 110 / 21 | — | -0.40 | +1.6/+0.5/-1.2 | — |
| 0.5 µM | [[Plate 02]]:C6 | 0 / 0 | — | -0.13 | +0.6/+0.5/+0.5 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C6 | 49 / 5 | — | +0.70 | +1.7/+0.8/-1.2 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (110 genes, none with an alert; 12 shown): [[MAP2K6]] 2.22× (z +6.7, 18/24 lines), [[CREB5]] 1.45× (z +6.1, 20/33 lines), [[DIXDC1]] 1.30× (z +4.8, 14/47 lines), [[TRERF1]] 1.32× (z +4.8, 27/41 lines), [[PPM1H]] 1.32× (z +4.6, 12/37 lines), [[ZNF618]] 1.45× (z +4.6, 16/38 lines), [[PIK3C2B]] 1.33× (z +4.5, 16/44 lines), [[SCARA3]] 1.59× (z +4.4, 8/26 lines), [[SORL1]] 1.34× (z +4.4, 14/27 lines), [[CAMK2G]] 1.21× (z +4.4, 15/47 lines), [[ADAM22]] 1.33× (z +4.3, 11/35 lines), [[CCDC15]] 1.30× (z +4.2, 9/45 lines)

**5 µM** (49 genes, none with an alert; 12 shown): [[TRERF1]] 1.67× (z +4.9, 25/42 lines), [[EEF2K]] 1.48× (z +4.7, 14/48 lines), [[KDM1B]] 1.36× (z +4.5, 8/48 lines), [[MAP2K6]] 2.53× (z +4.3, 11/24 lines), [[PIP4P2]] 1.59× (z +4.1, 13/44 lines), [[TM7SF3]] 1.40× (z +4.1, 7/48 lines), [[STAMBPL1]] 1.81× (z +3.9, 13/42 lines), [[GRK5]] 1.42× (z +3.7, 10/45 lines), [[ZNF618]] 1.70× (z +3.6, 10/39 lines), [[NRG2]] 1.57× (z +3.6, 8/33 lines), [[CAP2]] 1.41× (z +3.6, 8/41 lines), [[NFIA]] 1.43× (z +3.6, 18/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (21 genes, none with an alert; 12 shown): [[BMP2]] 0.694× (z -4.4, 8/26 lines), [[PRDM1]] 0.741× (z -4.2, 11/32 lines), [[TBC1D25]] 0.798× (z -4.0, 10/47 lines), [[DUSP5]] 0.739× (z -3.6, 18/41 lines), [[ENSG00000282988]] 0.663× (z -3.5, 13/34 lines), [[CDKN2B]] 0.792× (z -3.5, 8/35 lines), [[HMOX1]] 0.679× (z -3.4, 11/38 lines), [[ENSG00000291174]] 0.733× (z -3.4, 19/44 lines), [[ENSG00000205236]] 0.766× (z -3.4, 9/44 lines), [[CHMP1B]] 0.811× (z -3.4, 19/47 lines), [[CD55]] 0.827× (z -3.3, 15/32 lines), [[PTGS2]] 0.747× (z -3.2, 9/21 lines)

**5 µM** (5 genes, none with an alert): [[CD55]] 0.688× (z -3.6, 12/32 lines), [[ENSG00000282988]] 0.477× (z -3.5, 6/34 lines), [[MIR22HG]] 0.558× (z -3.3, 12/47 lines), [[TP53INP2]] 0.634× (z -3.1, 8/45 lines), [[TC2N]] 0.731× (z -2.9, 2/20 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 006]] (+2.8), [[Module 146]] (+2.3) | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 006]] (+2.5) | [[Module 043]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H1573 (line)]] (1.24), [[COLO 205 (line)]] (1.20), [[SK-MEL-2 (line)]] (1.17), [[NCI-H1792 (line)]] (1.15) · weakest: [[HEC-1-A (line)]] (0.428), [[HCT15 (line)]] (0.445), [[SHP-77 (line)]] (0.473) |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H1792 (line)]] (1.49), [[PANC-1 (line)]] (1.39), [[LOX-IMVI (line)]] (1.35), [[SNU-423 (line)]] (1.33) · weakest: [[HCT15 (line)]] (0.383), [[NCI-H2347 (line)]] (0.415), [[NCI-H661 (line)]] (0.451) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Ralimetinib dimesylate (drug)]] (+0.73, Other MAPK inhibitor); [[Flumatinib (mesylate) (drug)]] (+0.62, Other TK inhibitor); [[Regorafenib (drug)]] (+0.59, Multi-TK inhibitor); [[Radotinib (drug)]] (+0.59, Other TK inhibitor); [[8-Hydroxyquinoline (drug)]] (+0.53, unclear); [[Folic acid (drug)]] (+0.47, unclear); [[Mozavaptan (drug)]] (+0.47, unclear); [[Afatinib (drug)]] (+0.45, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity raises the cells' numbers under Bentamapimod 5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.89× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ENSG00000259200]] | 5 µM | B | ENSG00000259200 activity raises the cells' numbers under Bentamapimod 5 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.87× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[LINC02315]] | 5 µM | B | LINC02315 activity lowers the cells' numbers under Bentamapimod 5 µM (makes them more sensitive) | lines that do not express LINC02315 (31) vs lines expressing it (17) | the lines without LINC02315: 1.19× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1 |
| [[LINC01583]] | 5 µM | B | LINC01583 activity raises the cells' numbers under Bentamapimod 5 µM (protects the cells) | lines that do not express LINC01583 (28) vs lines expressing it (20) | the lines without LINC01583: 0.84× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |
| [[BMPER]] | 5 µM | B | BMPER activity raises the cells' numbers under Bentamapimod 5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.90× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[ATAD1]], [[PTEN]] | 5 µM | C | ATAD1, PTEN activity lowers the cells' numbers under Bentamapimod 5 µM (makes them more sensitive) | lines that do not express ATAD1, PTEN (4) vs lines expressing them (44) | the lines without ATAD1, PTEN: 1.41× the cells of the other lines | 0.098 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CFL1P1-1, ZC3HAV1L, OSR2; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Bentamapimod"
- `tables/drugdoses.parquet` — dd in 161, 162, 163
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
