---
drug: "Gallic acid"
type: "drug"
salt_base: "Gallic acid"
targets: ""
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 13
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Gallic acid

*Cyclooxygenase inhibitor (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 8 / 0 / 13; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.48.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:H5 | 3 / 5 | — | -0.65 | -0.4/-1.2/-0.4 | — |
| 0.5 µM | [[Plate 05]]:H5 | 0 / 0 | — | +0.92 | +0.5/+0.2/+0.6 | — |
| 5 µM | [[Plate 14]]:H5 | 5 / 8 | 0.846 | +0.28 | -0.6/-0.9/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[CUZD1]] 1.47× (z +3.4, 3/34 lines), [[AADAT]] 1.25× (z +2.9, 4/40 lines), [[RNF25]] 1.27× (z +2.8, 5/45 lines)

**5 µM** (5 genes, none with an alert): [[SLCO5A1]] 1.22× (z +4.1, 5/42 lines), [[ENSG00000260060]] 1.41× (z +3.8, 5/47 lines), [[PER1]] 1.37× (z +3.5, 30/47 lines), [[ENSG00000286277]] 1.25× (z +3.0, 5/42 lines), [[SNAI2]] 1.27× (z +2.9, 7/25 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[TMEM107]] 0.738× (z -3.4, 14/47 lines), [[BNIP3]] 0.784× (z -3.1, 21/37 lines), [[SHISA5]] 0.785× (z -3.0, 18/48 lines), [[IGFBP5]] 0.679× (z -2.9, 1/14 lines), [[PTK6]] 0.801× (z -2.7, 4/31 lines)

**5 µM** (8 genes, none with an alert): [[NTAN1]] 0.831× (z -4.6, 9/48 lines), [[NAMPTP1]] 0.768× (z -3.5, 8/47 lines), [[NR2F1]] 0.774× (z -3.4, 15/40 lines), [[CREB3L4]] 0.776× (z -3.2, 9/47 lines), [[EGR3]] 0.721× (z -3.2, 15/39 lines), [[BCAP31]] 0.815× (z -3.0, 8/48 lines), [[HMMR]] 0.824× (z -2.8, 11/48 lines), [[TYMP]] 0.770× (z -2.8, 7/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 179]] (+2.2) | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 179]] (+2.9) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | [[SW 900 (line)]] (-3.4), [[SW 1088 (line)]] (-3.4), [[SNU-423 (line)]] (-3.3), [[A498 (line)]] (-3.2), [[NCI-H2030 (line)]] (-3.1) | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Capivasertib (drug)]] (+0.70, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Goserelin (acetate) (drug)]] (+0.70, unclear); [[Lopinavir (drug)]] (+0.69, unclear); [[NVP-BHG712 (drug)]] (+0.67, unclear); [[Pemetrexed (drug)]] (+0.67, DNA synthesis/repair inhibitor); [[Asciminib (drug)]] (+0.65, Other TK inhibitor); [[Fluvoxamine (drug)]] (+0.65, unclear); [[Acetazolamide (drug)]] (+0.63, unclear, ⚠ only 3 significant genes); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.59, unclear); [[Mozavaptan (drug)]] (+0.54, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[PWWP2B]] | 0.05 µM | C | PWWP2B activity raises the cells' numbers under Gallic acid 0.05 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.58× the cells of the other lines | 0.028 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[KLHL9]] | 0.05 µM | C | KLHL9 activity raises the cells' numbers under Gallic acid 0.05 µM (protects the cells) | lines that do not express KLHL9 (3) vs lines expressing it (45) | the lines without KLHL9: 0.63× the cells of the other lines | 0.079 | ⚠ few lines (3 vs 47); across organs; also absent: MTAP, TMEM117, CFL1P1-1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Gallic acid"
- `tables/drugdoses.parquet` — dd in 492, 493, 494
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
