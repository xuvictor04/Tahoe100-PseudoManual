---
drug: "Hesperidin"
type: "drug"
salt_base: "Hesperidin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 31
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Hesperidin

*unclear (unclear) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 31 / 5 / 8; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.25 / 0.30.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E10 | 5 / 26 | — | +0.46 | +0.2/+1.0/+0.1 | — |
| 0.5 µM | [[Plate 08]]:E10 | 0 / 5 | — | -0.34 | +0.0/+0.5/+0.2 | — |
| 5 µM | [[Plate 09]]:E10 | 3 / 5 | — | -0.36 | +1.1/+0.6/+0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[SYT7]] 1.26× (z +3.2, 3/38 lines), [[MALAT1]] 1.21× (z +3.1, 28/48 lines), [[EGR1]] 1.53× (z +3.1, 28/46 lines), [[ATP5F1B]] 1.29× (z +3.0, 23/48 lines), [[EPHA4]] 1.24× (z +2.9, 2/29 lines)

**5 µM** (3 genes, none with an alert): [[C8orf88]] 1.35× (z +4.1, 3/31 lines), [[CFAP210]] 1.82× (z +3.2, 16/38 lines), [[ADD2]] 1.23× (z +3.0, 0/15 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (26 genes, none with an alert; 12 shown): [[KLRG1]] 0.499× (z -4.8, 8/27 lines), [[TMEM138]] 0.771× (z -3.8, 4/47 lines), [[ST20-MTHFS]] 0.797× (z -3.4, 13/47 lines), [[ENSG00000257735]] 0.660× (z -3.4, 15/42 lines), [[SMCO2]] 0.670× (z -3.4, 8/35 lines), [[CXXC4]] 0.627× (z -3.4, 4/21 lines), [[ATP6V0D1-DT]] 0.677× (z -3.4, 11/45 lines), [[EPHA7]] 0.668× (z -3.4, 2/15 lines), [[ZNF169]] 0.794× (z -3.3, 7/47 lines), [[MIR3142HG]] 0.666× (z -3.3, 10/20 lines), [[ZNF815P]] 0.677× (z -3.2, 8/38 lines), [[ZNF234]] 0.824× (z -3.2, 7/42 lines)

**0.5 µM** (5 genes, none with an alert): [[ADGRB1]] 0.682× (z -3.6, 9/26 lines), [[ENSG00000266994]] 0.715× (z -3.4, 9/43 lines), [[CCDC17]] 0.631× (z -3.3, 15/39 lines), [[B4GAT1-DT]] 0.684× (z -3.2, 9/39 lines), [[GPR146]] 0.786× (z -3.1, 11/46 lines)

**5 µM** (5 genes, none with an alert): [[ENSG00000277007]] 0.581× (z -4.4, 7/29 lines), [[ENSG00000227355]] 0.644× (z -3.6, 3/16 lines), [[LRRC36]] 0.704× (z -3.3, 2/16 lines), [[NFATC4]] 0.689× (z -3.1, 6/26 lines), [[ENSG00000285382]] 0.747× (z -2.9, 9/43 lines)

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
| 0.05 µM | — | [[hTERT-HPNE (line)]] (1.55), [[COLO 205 (line)]] (1.49), [[C-33 A (line)]] (1.46), [[SW48 (line)]] (1.43) · weakest: [[CHP-212 (line)]] (0.350), [[RKO (line)]] (0.481), [[Hs 766T (line)]] (0.569) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Allopurinol (drug)]] (+0.69, unclear); [[Tazarotene (drug)]] (+0.69, Retinoic receptor agonist); [[Cloxacillin (sodium) (drug)]] (+0.66, unclear); [[Daidzin (drug)]] (+0.62, unclear, ⚠ only 3 significant genes); [[Fumaric acid (drug)]] (+0.60, unclear); [[Sacubitril_Valsartan (drug)]] (+0.60, unclear, ⚠ only 1 significant gene); [[Sinomenine (drug)]] (+0.59, unclear); [[Ranolazine (drug)]] (+0.59, unclear); [[Methotrexate (drug)]] (+0.57, DNA synthesis/repair inhibitor); [[Malotilate (drug)]] (+0.57, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[CCL3]] | 0.05 µM | B | CCL3 activity raises the cells' numbers under Hesperidin 0.05 µM (protects the cells) | lines that do not express CCL3 (37) vs lines expressing it (11) | the lines without CCL3: 0.83× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMPRSS15, ENSG00000224865, ESM1 |
| [[GJA1]] | 0.05 µM | B | GJA1 activity raises the cells' numbers under Hesperidin 0.05 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.87× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[ULK2]] | 0.05 µM | B | ULK2 activity lowers the cells' numbers under Hesperidin 0.05 µM (makes them more sensitive) | lines that do not express ULK2 (14) vs lines expressing it (34) | the lines without ULK2: 1.10× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[CERT1]] | 0.05 µM | C | CERT1's natural level lowers the cells' numbers under Hesperidin 0.05 µM (makes them more sensitive) | CERT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.079 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[FNBP4]] | 0.05 µM | C | FNBP4's natural level lowers the cells' numbers under Hesperidin 0.05 µM (makes them more sensitive) | FNBP4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.084 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000269635]] | 0.05 µM | C | ENSG00000269635's natural level raises the cells' numbers under Hesperidin 0.05 µM (protects the cells) | ENSG00000269635's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.383 over the table, 0.084 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[DRC1]] | 0.05 µM | C | DRC1's natural level raises the cells' numbers under Hesperidin 0.05 µM (protects the cells) | DRC1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.383 over the table, 0.084 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000249951]] | 0.05 µM | C | ENSG00000249951's natural level raises the cells' numbers under Hesperidin 0.05 µM (protects the cells) | ENSG00000249951's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.390 over the table, 0.084 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ZBTB26]] | 0.05 µM | C | ZBTB26's natural level lowers the cells' numbers under Hesperidin 0.05 µM (makes them more sensitive) | ZBTB26's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.63 | 0.403 over the table, 0.089 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Hesperidin"
- `tables/drugdoses.parquet` — dd in 522, 523, 524
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
