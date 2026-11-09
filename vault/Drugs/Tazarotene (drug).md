---
drug: "Tazarotene"
type: "drug"
salt_base: "Tazarotene"
targets: "RARA, RARB, RARG"
moa_fine: "Retinoic receptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 20
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Tazarotene

*Retinoic receptor agonist (activator/agonist) · targets: RARA, RARB, RARG · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 20 / 8; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.33 / 0.18.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E9 | 2 / 2 | — | -0.03 | -0.7/-0.3/+0.1 | — |
| 0.5 µM | [[Plate 11]]:E9 | 18 / 2 | — | -0.21 | +0.2/+0.7/+0.7 | — |
| 5 µM | [[Plate 12]]:E9 | 3 / 5 | — | +0.04 | -0.2/+0.1/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[UTY]] 1.20× (z +3.1, 0/18 lines), [[RARB]] 1.20× (z +2.9, 2/20 lines)

**0.5 µM** (18 genes, none with an alert; 12 shown): [[USP9Y]] 1.34× (z +4.9, 0/19 lines), [[ZYG11A]] 1.34× (z +3.9, 0/19 lines), [[EHF]] 1.24× (z +3.8, 0/22 lines), [[DHRS3]] 1.25× (z +3.8, 18/36 lines), [[ST6GALNAC1]] 1.97× (z +3.7, 1/10 lines), [[HS6ST2]] 1.23× (z +3.6, 0/20 lines), [[NRP2]] 1.26× (z +3.6, 4/25 lines), [[USP3-AS1]] 1.27× (z +3.5, 7/47 lines), [[CYP26B1]] 1.54× (z +3.5, 8/23 lines), [[RNF212]] 1.35× (z +3.4, 0/12 lines), [[BTG2]] 1.35× (z +3.3, 6/39 lines), [[RARB]] 1.23× (z +3.2, 1/20 lines)

**5 µM** (3 genes, none with an alert): [[DHRS3]] 1.32× (z +4.5, 21/35 lines), [[NRIP1]] 1.26× (z +3.7, 25/40 lines), [[RARB]] 1.24× (z +3.4, 6/20 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[CSTF2T]] 0.744× (z -3.3, 9/45 lines), [[TP53I11]] 0.783× (z -3.1, 3/41 lines)

**0.5 µM** (2 genes, none with an alert): [[ENSG00000230479]] 0.820× (z -2.9, 7/36 lines), [[LYPD6B]] 0.829× (z -2.9, 7/23 lines)

**5 µM** (5 genes, none with an alert): [[CDK3]] 0.613× (z -4.1, 9/45 lines), [[MT-ND4L]] 0.591× (z -3.6, 41/48 lines), [[TP53I11]] 0.776× (z -3.2, 9/41 lines), [[COL5A1]] 0.790× (z -3.2, 14/18 lines), [[ENSG00000268797]] 0.823× (z -3.2, 6/48 lines)

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
| 0.5 µM | — | [[A-172 (line)]] (1.47), [[SNU-1 (line)]] (1.44), [[HCT15 (line)]] (1.35), [[HS-578T (line)]] (1.27) · weakest: [[A-427 (line)]] (-0.685), [[NCI-H23 (line)]] (-0.0327), [[NCI-H2347 (line)]] (0.162) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Hesperidin (drug)]] (+0.69, unclear); [[Aspirin (drug)]] (+0.69, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Allopurinol (drug)]] (+0.66, unclear); [[Sacubitril_Valsartan (drug)]] (+0.61, unclear, ⚠ only 1 significant gene); [[Cloxacillin (sodium) (drug)]] (+0.61, unclear); [[Piroxicam (drug)]] (+0.61, Cyclooxygenase inhibitor); [[ML264 (drug)]] (+0.58, unclear, ⚠ only 5 significant genes); [[Fumaric acid (drug)]] (+0.55, unclear); [[Silodosin (drug)]] (+0.55, unclear); [[Malotilate (drug)]] (+0.54, unclear); [[Fluvoxamine (maleate) (drug)]] (+0.53, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[RARA]], [[RARB]], [[RARG]] | [[NRP2]] | moves it that way too | B | RARA, RARB, RARG activity raises NRP2's level | compounds that target RARA, RARB, RARG: 2 of 2 raise it (Retinoic acid, Tazarotene) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

## Data

- `tables/drugs.parquet` — drug == "Tazarotene"
- `tables/drugdoses.parquet` — dd in 985, 986, 987
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
