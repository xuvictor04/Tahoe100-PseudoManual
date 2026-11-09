---
drug: "Ivermectin"
type: "drug"
salt_base: "Ivermectin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 19
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Ivermectin

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 18 / 19; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.36 / 0.47.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E12 | 0 / 4 | — | +0.08 | -0.8/-0.4/-0.7 | — |
| 0.5 µM | [[Plate 11]]:E12 | 17 / 1 | — | -0.86 | -1.2/-0.6/-0.4 | — |
| 5 µM | [[Plate 12]]:E12 | 1 / 18 | — | +0.18 | -1.7/-0.5/-0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (17 genes, none with an alert; 12 shown): [[RNF180]] 1.31× (z +3.7, 1/21 lines), [[LINC01119]] 1.41× (z +3.6, 6/29 lines), [[CCDC73]] 1.38× (z +3.5, 1/34 lines), [[ZNF596]] 1.30× (z +3.3, 3/44 lines), [[ZNF134]] 1.22× (z +3.3, 3/35 lines), [[BAAT]] 1.51× (z +3.3, 3/30 lines), [[ENSG00000285708]] 1.37× (z +3.2, 6/37 lines), [[ENSG00000198106]] 1.38× (z +3.2, 6/27 lines), [[OPRD1]] 1.53× (z +3.1, 0/8 lines), [[ENSG00000288520]] 1.45× (z +3.1, 3/23 lines), [[ZNF365]] 1.32× (z +3.1, 3/21 lines), [[ASIC2]] 1.24× (z +3.0, 3/42 lines)

**5 µM** (1 gene, none with an alert): [[IRGQ]] 1.25× (z +2.9, 6/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[ST3GAL5]] 0.768× (z -3.4, 7/40 lines), [[PRSS23-AS1]] 0.733× (z -3.3, 4/37 lines), [[CNNM1]] 0.799× (z -3.2, 1/23 lines), [[VSIR]] 0.792× (z -3.1, 3/31 lines)

**0.5 µM** (1 gene, none with an alert): [[HAUS4]] 0.827× (z -2.9, 10/46 lines)

**5 µM** (18 genes, none with an alert; 12 shown): [[CFD]] 0.646× (z -3.7, 11/42 lines), [[LIN7A]] 0.731× (z -3.6, 1/13 lines), [[EPHA3]] 0.718× (z -3.6, 4/21 lines), [[PPP1R3B-DT]] 0.749× (z -3.6, 3/42 lines), [[SAMD1]] 0.649× (z -3.5, 22/47 lines), [[ARSK]] 0.804× (z -3.5, 11/47 lines), [[SKAP1]] 0.795× (z -3.3, 1/14 lines), [[ESRRG]] 0.720× (z -3.3, 0/21 lines), [[ALKBH4]] 0.729× (z -3.2, 4/47 lines), [[DUT]] 0.733× (z -3.1, 17/48 lines), [[FAM216A]] 0.760× (z -3.1, 12/41 lines), [[GRHL2]] 0.814× (z -3.0, 0/14 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 179]] (+2.2) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Phenytoin (sodium) (drug)]] (+0.71, unclear, ⚠ only 7 significant genes); [[(S)-Crizotinib (drug)]] (+0.68, unclear); [[Cinacalcet (drug)]] (+0.67, unclear, ⚠ only 8 significant genes); [[Pentagastrin (drug)]] (+0.64, unclear, ⚠ only 9 significant genes); [[Clonidine (hydrochloride) (drug)]] (+0.63, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Fluvoxamine (drug)]] (+0.62, unclear); [[Dabrafenib (drug)]] (+0.61, RAF inhibitor); [[Dihydroartemisinin (drug)]] (+0.61, unclear); [[Lucanthone (drug)]] (+0.53, unclear); [[Fenofibrate (drug)]] (+0.52, unclear); [[Pentoxifylline (drug)]] (+0.52, unclear); [[Asciminib (drug)]] (+0.52, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 15 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.22× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.21× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ERBB3]] | 0.5 µM | B | ERBB3 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express ERBB3 (27) vs lines expressing it (21) | the lines without ERBB3: 0.84× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; also absent: LAD1, KDF1, EPCAM |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.83× the cells of the other lines | 0.032 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[SIRLNT]] | 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.24× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[EPCAM]] | 0.5 µM | B | EPCAM activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.85× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 1.17× the cells of the other lines | 0.036 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[SRGN]] | 0.5 µM | B | SRGN activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 1.23× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[CLDN3]] | 0.5 µM | B | CLDN3 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 0.86× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[VEGFC]] | 0.5 µM | B | VEGFC activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express VEGFC (22) vs lines expressing it (26) | the lines without VEGFC: 1.18× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: S1PR3, KCNMA1, BASP1 |
| [[CD44]] | 0.5 µM | B | CD44 activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 1.18× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[ZNF860]] | 0.5 µM | B | ZNF860 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express ZNF860 (16) vs lines expressing it (32) | the lines without ZNF860: 0.87× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CRYBG2, IL18, TMC4 |
| [[FGD3]] | 0.5 µM | B | FGD3 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express FGD3 (19) vs lines expressing it (29) | the lines without FGD3: 0.87× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CGN, SPINT1-AS1, SPINT1; maybe low, not absent |
| [[DCDC2]] | 0.5 µM | B | DCDC2 activity raises the cells' numbers under Ivermectin 0.5 µM (protects the cells) | lines that do not express DCDC2 (25) vs lines expressing it (23) | the lines without DCDC2: 0.90× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: FXYD2, PGBD5, HAVCR1 |
| [[PRSS23]] | 0.5 µM | B | PRSS23 activity lowers the cells' numbers under Ivermectin 0.5 µM (makes them more sensitive) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 1.20× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Ivermectin"
- `tables/drugdoses.parquet` — dd in 573, 574, 575
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
