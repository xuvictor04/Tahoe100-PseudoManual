---
drug: "Sulfisoxazole"
type: "drug"
salt_base: "Sulfisoxazole"
targets: "EDNRA, EDNRB"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 16
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Sulfisoxazole

*unclear (inhibitor/antagonist) · targets: EDNRA, EDNRB · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 1 / 16; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.08 / 0.31.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E3 | 0 / 0 | — | -0.09 | -0.4/-0.0/-0.3 | — |
| 0.5 µM | [[Plate 05]]:E3 | 0 / 1 | — | +0.08 | -0.4/-0.3/-1.0 | — |
| 5 µM | [[Plate 14]]:E3 | 9 / 7 | 0.378 | -0.04 | -1.2/-0.9/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (9 genes, none with an alert): [[SH3GL2]] 1.28× (z +3.9, 5/25 lines), [[KCNQ3]] 1.27× (z +3.8, 3/21 lines), [[SUSD4]] 1.35× (z +3.7, 2/30 lines), [[EBLN2]] 1.22× (z +3.3, 6/46 lines), [[HS6ST3]] 1.22× (z +3.2, 6/27 lines), [[VAT1L]] 1.27× (z +3.2, 3/19 lines), [[PLD5]] 1.22× (z +2.8, 2/42 lines), [[ENSG00000259124]] 1.24× (z +2.8, 6/42 lines), [[TEX15]] 1.22× (z +2.7, 1/19 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[CCND2]] 0.736× (z -3.6, 10/11 lines)

**5 µM** (7 genes, none with an alert): [[AP2A1]] 0.822× (z -5.4, 23/48 lines), [[SNX32]] 0.725× (z -4.4, 24/48 lines), [[RPL4]] 0.794× (z -4.4, 41/48 lines), [[RIPOR1]] 0.819× (z -4.2, 17/47 lines), [[HCFC1]] 0.827× (z -3.8, 24/48 lines), [[GPR146]] 0.828× (z -3.5, 7/47 lines), [[PRR36]] 0.759× (z -3.1, 4/27 lines)

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
| 0.5 µM | [[Hs 766T (line)]] (-4.9) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Ciclopirox (drug)]] (+0.59, unclear); [[Trimetrexate (drug)]] (+0.56, DNA synthesis/repair inhibitor); [[Tetracycline (hydrochloride) (drug)]] (+0.55, unclear, ⚠ only 6 significant genes); [[Allantoin (drug)]] (+0.53, unclear); [[Ivabradine (hydrochloride) (drug)]] (+0.52, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Entecavir (monohydrate) (drug)]] (+0.47, unclear); [[Rifaximin (drug)]] (+0.43, unclear); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.42, unclear); [[Verteporfin (drug)]] (+0.39, unclear); [[Baicalin (drug)]] (+0.39, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000233420]] | 0.5 µM | C | ENSG00000233420 activity raises the cells' numbers under Sulfisoxazole 0.5 µM (protects the cells) | lines that do not express ENSG00000233420 (3) vs lines expressing it (45) | the lines without ENSG00000233420: 0.80× the cells of the other lines | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: STPG2, ARHGEF10L, ARHGAP15; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Sulfisoxazole"
- `tables/drugdoses.parquet` — dd in 967, 968, 969
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
