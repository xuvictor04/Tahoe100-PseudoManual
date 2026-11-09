---
drug: "Methyl aminolevulinate (hydrochloride)"
type: "drug"
salt_base: "Methyl aminolevulinate"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 3
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Methyl aminolevulinate (hydrochloride)

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 3 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.38 / 0.36.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D5 | 0 / 0 | — | -0.14 | +0.3/+0.3/+0.7 | — |
| 0.5 µM | [[Plate 11]]:D5 | 0 / 3 | — | +0.85 | -0.5/-0.1/-0.7 | — |
| 5 µM | [[Plate 12]]:D5 | 0 / 0 | — | +0.21 | -0.5/+0.1/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

No gene is significantly raised at any dose.

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (3 genes, none with an alert): [[NAA11]] 0.627× (z -3.7, 0/7 lines), [[PIP5K1B]] 0.778× (z -3.5, 0/15 lines), [[SNCA]] 0.809× (z -3.1, 1/19 lines)

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
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 3 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Clopidogrel (drug)]] (+0.83, unclear); [[Rutin (trihydrate) (drug)]] (+0.76, unclear); [[Lucanthone (drug)]] (+0.74, unclear); [[Tucatinib (drug)]] (+0.74, EGFR/ERBB inhibitor); [[Ranolazine (drug)]] (+0.66, unclear); [[Relugolix (drug)]] (+0.66, unclear, ⚠ only 5 significant genes); [[Benproperine (phosphate) (drug)]] (+0.65, unclear); [[Anethole trithione (drug)]] (+0.65, unclear); [[Berberine (chloride hydrate) (drug)]] (+0.61, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[RSPO3]] | 0.5 µM | B | RSPO3 activity raises the cells' numbers under Methyl aminolevulinate (hydrochloride) 0.5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.86× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[IKZF3]] | 0.5 µM | B | IKZF3 activity lowers the cells' numbers under Methyl aminolevulinate (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express IKZF3 (31) vs lines expressing it (17) | the lines without IKZF3: 1.16× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC34A2, ENSG00000244468, ENSG00000255026; maybe low, not absent |
| [[ENSG00000275119]] | 0.5 µM | B | ENSG00000275119 activity raises the cells' numbers under Methyl aminolevulinate (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000275119 (10) vs lines expressing it (38) | the lines without ENSG00000275119: 0.87× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: LINC01252; maybe low, not absent |
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity raises the cells' numbers under Methyl aminolevulinate (hydrochloride) 0.5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.90× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[BMPER]] | 0.5 µM | B | BMPER activity raises the cells' numbers under Methyl aminolevulinate (hydrochloride) 0.5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.90× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Methyl aminolevulinate (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 675, 676, 677
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
