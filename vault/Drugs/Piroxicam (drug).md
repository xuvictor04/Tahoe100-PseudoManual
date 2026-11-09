---
drug: "Piroxicam"
type: "drug"
salt_base: "Piroxicam"
targets: "PTGS1, PTGS2"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 104
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Piroxicam

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS1, PTGS2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 104 / 2 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.44 / 0.26.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E2 | 1 / 103 | — | +0.53 | +0.2/+0.8/+0.7 | — |
| 0.5 µM | [[Plate 11]]:E2 | 0 / 2 | — | +0.26 | +0.1/+0.8/+0.4 | — |
| 5 µM | [[Plate 12]]:E2 | 0 / 0 | — | +0.16 | -0.1/+0.1/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[EIF4A3]] 1.26× (z +3.0, 12/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (103 genes, none with an alert; 12 shown): [[ITGB3BP]] 0.804× (z -3.8, 22/47 lines), [[ARMC2]] 0.771× (z -3.8, 8/46 lines), [[TMEM177]] 0.667× (z -3.8, 10/42 lines), [[ZNF818P]] 0.629× (z -3.7, 3/24 lines), [[SMCO2]] 0.672× (z -3.7, 9/36 lines), [[ZFHX3-AS1]] 0.806× (z -3.7, 15/48 lines), [[DICER1-AS1]] 0.730× (z -3.7, 9/47 lines), [[ARHGAP27P1-BPTFP1-KPNA2P3]] 0.740× (z -3.6, 14/48 lines), [[PIGL]] 0.800× (z -3.6, 19/48 lines), [[ENSG00000286739]] 0.719× (z -3.6, 11/42 lines), [[ENSG00000235978]] 0.770× (z -3.5, 5/43 lines), [[ZCWPW2]] 0.794× (z -3.5, 11/48 lines)

**0.5 µM** (2 genes, none with an alert): [[ANKDD1A]] 0.821× (z -3.4, 6/47 lines), [[FRY]] 0.823× (z -3.3, 4/34 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 207]] (+2.1) | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.87), [[SW 1271 (line)]] (1.77), [[SNU-423 (line)]] (1.63), [[SW 900 (line)]] (1.53) · weakest: [[KATO III (line)]] (0.129), [[LoVo (line)]] (0.347), [[A-427 (line)]] (0.407) |
| 0.5 µM | — | — |
| 5 µM | [[CHP-212 (line)]] (-4.0) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Acetazolamide (drug)]] (+0.80, unclear, ⚠ only 3 significant genes); [[Cloxacillin (sodium) (drug)]] (+0.78, unclear); [[Fumaric acid (drug)]] (+0.76, unclear); [[Ranolazine (drug)]] (+0.75, unclear); [[Pravastatin (sodium) (drug)]] (+0.74, unclear); [[Allopurinol (drug)]] (+0.72, unclear); [[Dimethyl fumarate (drug)]] (+0.66, unclear); [[Clopidogrel (drug)]] (+0.64, unclear); [[Asciminib (drug)]] (+0.62, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.85× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[SRGN]] | 0.05 µM | B | SRGN activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.77× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[ENSG00000230615]] | 0.05 µM | B | ENSG00000230615 activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 0.81× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[HES4]] | 0.05 µM | C | HES4 activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express HES4 (4) vs lines expressing it (44) | the lines without HES4: 0.75× the cells of the other lines | 0.027 | ⚠ few lines (4 vs 46); across organs; also absent: SLC26A4, ADAMTSL5 |
| [[ITPK1]] | 0.05 µM | C | ITPK1 activity lowers the cells' numbers under Piroxicam 0.05 µM (makes them more sensitive) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 1.29× the cells of the other lines | 0.047 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[FIGN]] | 0.05 µM | C | FIGN activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.86× the cells of the other lines | 0.073 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SCAMP5]] | 0.05 µM | C | SCAMP5 activity lowers the cells' numbers under Piroxicam 0.05 µM (makes them more sensitive) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 1.34× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 0.05 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 0.75× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| [[ACCS]] | 0.05 µM | C | ACCS activity raises the cells' numbers under Piroxicam 0.05 µM (protects the cells) | lines that do not express ACCS (5) vs lines expressing it (43) | the lines without ACCS: 0.79× the cells of the other lines | 0.083 | ⚠ tissue-confounded; across organs; also absent: FXYD5, CAV2, KDELR3 |
| [[RNU4-2]] | 0.05 µM | C | RNU4-2's natural level lowers the cells' numbers under Piroxicam 0.05 µM (makes them more sensitive) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[MAST1]] | 0.05 µM | C | MAST1's natural level lowers the cells' numbers under Piroxicam 0.05 µM (makes them more sensitive) | MAST1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.305 over the table, 0.055 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Piroxicam"
- `tables/drugdoses.parquet` — dd in 821, 822, 823
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
