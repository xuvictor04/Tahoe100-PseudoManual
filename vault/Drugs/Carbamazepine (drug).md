---
drug: "Carbamazepine"
type: "drug"
salt_base: "Carbamazepine"
targets: ""
moa_fine: "HDAC inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 149
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Carbamazepine

*HDAC inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 24 / 149; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.25 / 0.39.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C7 | 2 / 0 | — | -0.14 | +0.2/-0.1/-0.2 | — |
| 0.5 µM | [[Plate 11]]:C7 | 19 / 5 | — | -0.32 | -0.4/-0.9/-0.0 | — |
| 5 µM | [[Plate 12]]:C7 | 86 / 63 | — | -0.83 | +0.4/+0.6/+0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000289177]] 1.40× (z +3.3, 5/40 lines), [[SLC4A2]] 1.24× (z +3.1, 7/48 lines)

**0.5 µM** (19 genes, none with an alert; 12 shown): [[ENSG00000289421]] 1.56× (z +3.7, 6/39 lines), [[ZNF101]] 1.20× (z +3.5, 3/47 lines), [[C19orf12]] 1.22× (z +3.5, 8/47 lines), [[LYSMD4]] 1.35× (z +3.4, 4/44 lines), [[APTR]] 1.26× (z +3.4, 10/47 lines), [[TP53TG5]] 1.43× (z +3.4, 4/38 lines), [[DENND10]] 1.27× (z +3.3, 8/47 lines), [[SRGAP2D]] 1.27× (z +3.2, 7/37 lines), [[ENSG00000255339]] 1.28× (z +3.2, 3/45 lines), [[MORN4]] 1.37× (z +3.2, 7/43 lines), [[PEX11A]] 1.33× (z +3.2, 6/44 lines), [[CD72]] 1.35× (z +3.1, 3/41 lines)

**5 µM** (86 genes, none with an alert; 12 shown): [[ADGRB3]] 1.44× (z +4.0, 8/19 lines), [[LOXL4]] 1.58× (z +3.9, 5/16 lines), [[TEX41]] 1.40× (z +3.9, 6/18 lines), [[BHMT2]] 1.86× (z +3.9, 0/8 lines), [[PTPRD]] 1.33× (z +3.7, 10/22 lines), [[ENSG00000289694]] 1.36× (z +3.6, 5/45 lines), [[DKK1]] 1.57× (z +3.6, 10/27 lines), [[PRSS23]] 1.34× (z +3.6, 24/34 lines), [[CAVIN3]] 1.83× (z +3.6, 15/25 lines), [[LIMD2]] 1.51× (z +3.5, 4/37 lines), [[TMEM45A]] 1.32× (z +3.5, 15/34 lines), [[LANCL3]] 1.40× (z +3.5, 2/23 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (5 genes, none with an alert): [[WDR5B-DT]] 0.733× (z -4.0, 20/47 lines), [[FOSB]] 0.429× (z -3.7, 39/47 lines), [[ENSG00000255946]] 0.724× (z -3.2, 11/44 lines), [[ENSG00000249476]] 0.680× (z -2.9, 14/46 lines), [[EMP1]] 0.773× (z -2.8, 11/38 lines)

**5 µM** (63 genes, none with an alert; 12 shown): [[SUPV3L1]] 0.718× (z -4.5, 30/47 lines), [[LMTK2]] 0.830× (z -4.0, 22/47 lines), [[KLHL28]] 0.815× (z -4.0, 23/47 lines), [[HBS1L]] 0.812× (z -3.9, 28/47 lines), [[FBXO31]] 0.782× (z -3.9, 14/47 lines), [[PPTC7]] 0.775× (z -3.8, 23/47 lines), [[PLEKHB2]] 0.817× (z -3.8, 24/47 lines), [[WDR49]] 0.660× (z -3.8, 15/44 lines), [[HYCC2]] 0.803× (z -3.8, 23/47 lines), [[PPM1B]] 0.832× (z -3.7, 16/47 lines), [[SEC61A2]] 0.709× (z -3.7, 15/47 lines), [[NUP93]] 0.798× (z -3.7, 19/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 179]] (-2.5), [[Module 207]] (-2.4), [[Module 163]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[SW 1088 (line)]] (1.83), [[NCI-H661 (line)]] (1.54), [[CHP-212 (line)]] (1.48), [[C32 (line)]] (1.44) · weakest: [[SW 1271 (line)]] (-0.0816), [[BT-474 (line)]] (-0.0356), [[LoVo (line)]] (0.133) |
| 5 µM | [[HEC-1-A (line)]] (-4.0) | [[SW 1271 (line)]] (1.50), [[SW48 (line)]] (1.25), [[hTERT-HPNE (line)]] (1.22), [[HT-29 (line)]] (1.17) · weakest: [[BT-474 (line)]] (0.389), [[NCI-H2347 (line)]] (0.543), [[AN3 CA (line)]] (0.574) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Estrone sulfate (potassium) (drug)]] (+0.87, unclear); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.84, unclear); [[Apalutamide (drug)]] (+0.71, Androgen receptor antagonist); [[Mifepristone (drug)]] (+0.69, unclear); [[Omeprazole (sodium) (drug)]] (+0.65, unclear); [[Proglumide (drug)]] (+0.65, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.60, unclear); [[Rosiglitazone (drug)]] (+0.59, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 24 arrows, 24 of them with an alert ⚠; grade A 0, B 18, C 6. Shown: the 15 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[TBC1D8]] | 5 µM | B | TBC1D8 activity lowers the cells' numbers under Carbamazepine 5 µM (makes them more sensitive) | lines that do not express TBC1D8 (6) vs lines expressing it (42) | the lines without TBC1D8: 1.20× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[BMPER]] | 0.5 µM | B | BMPER activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 1.19× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.18× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity lowers the cells' numbers under Carbamazepine 5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.20× the cells of the other lines | 0.064 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[SIRLNT]] | 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.26× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[KPNA7]] | 5 µM | B | KPNA7 activity lowers the cells' numbers under Carbamazepine 5 µM (makes them more sensitive) | lines that do not express KPNA7 (10) vs lines expressing it (38) | the lines without KPNA7: 1.20× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: STS, LGALS3, ENSG00000248993; maybe low, not absent |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.21× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ENSG00000251537]] | 5 µM | B | ENSG00000251537 activity lowers the cells' numbers under Carbamazepine 5 µM (makes them more sensitive) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 1.19× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[IL15]] | 5 µM | B | IL15 activity lowers the cells' numbers under Carbamazepine 5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.23× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[PPP1R9A]] | 0.5 µM | B | PPP1R9A activity raises the cells' numbers under Carbamazepine 0.5 µM (protects the cells) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 0.81× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[GPRC5A]] | 5 µM | B | GPRC5A activity lowers the cells' numbers under Carbamazepine 5 µM (makes them more sensitive) | lines that do not express GPRC5A (12) vs lines expressing it (36) | the lines without GPRC5A: 1.24× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[DOCK10]] | 0.5 µM | B | DOCK10 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express DOCK10 (24) vs lines expressing it (24) | the lines without DOCK10: 1.17× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, TRPA1 |
| [[CD44]] | 0.5 µM | B | CD44 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 1.18× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[ATP1B1]] | 5 µM | B | ATP1B1 activity lowers the cells' numbers under Carbamazepine 5 µM (makes them more sensitive) | lines that do not express ATP1B1 (8) vs lines expressing it (40) | the lines without ATP1B1: 1.16× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: PYROXD2, IL15, IER3; maybe low, not absent |
| [[ADAM12]] | 0.5 µM | B | ADAM12 activity lowers the cells' numbers under Carbamazepine 0.5 µM (makes them more sensitive) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 1.17× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Carbamazepine"
- `tables/drugdoses.parquet` — dd in 245, 246, 247
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
