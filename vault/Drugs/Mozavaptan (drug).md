---
drug: "Mozavaptan"
type: "drug"
salt_base: "Mozavaptan"
targets: "AVPR2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 10
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Mozavaptan

*unclear (inhibitor/antagonist) · targets: AVPR2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 10 / 10 / 3; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.08 / -0.03.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G9 | 5 / 5 | — | -0.29 | +0.5/+0.8/-0.2 | — |
| 0.5 µM | [[Plate 08]]:G9 | 3 / 7 | — | -0.37 | -0.8/-1.0/-0.9 | — |
| 5 µM | [[Plate 09]]:G9 | 1 / 2 | — | -0.38 | -0.3/-0.6/+0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[ZFP1]] 1.28× (z +4.0, 5/46 lines), [[TMA7]] 1.52× (z +3.5, 33/47 lines), [[ENSG00000250920]] 1.72× (z +3.3, 4/6 lines), [[PRRT3]] 1.36× (z +3.2, 4/34 lines), [[LINC01414]] 1.40× (z +3.1, 1/35 lines)

**0.5 µM** (3 genes, none with an alert): [[GRK2]] 1.23× (z +3.3, 3/47 lines), [[ENSG00000236498]] 1.33× (z +2.9, 5/45 lines), [[RNF25]] 1.29× (z +2.9, 1/47 lines)

**5 µM** (1 gene, none with an alert): [[IPCEF1]] 1.36× (z +3.3, 6/35 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[LMBR1L]] 0.815× (z -3.4, 10/47 lines), [[SMPD4]] 0.814× (z -3.3, 14/47 lines), [[SFXN2]] 0.763× (z -3.3, 11/44 lines), [[LINC00674]] 0.729× (z -3.2, 11/44 lines), [[FGD1]] 0.823× (z -3.2, 7/37 lines)

**0.5 µM** (7 genes, none with an alert): [[ENSG00000284772]] 0.705× (z -3.7, 10/43 lines), [[ENSG00000285155]] 0.652× (z -3.7, 11/39 lines), [[LINC02798]] 0.653× (z -3.5, 18/40 lines), [[GARIN1A]] 0.640× (z -3.3, 15/47 lines), [[RASGRP3]] 0.766× (z -3.2, 5/31 lines), [[AVIL]] 0.674× (z -3.2, 18/46 lines), [[WNT2B]] 0.767× (z -2.8, 20/48 lines)

**5 µM** (2 genes, none with an alert): [[ENSG00000285755]] 0.694× (z -3.3, 6/27 lines), [[SH3BGR]] 0.781× (z -3.1, 9/43 lines)

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
| 0.5 µM | [[HOP62 (line)]] (-4.8), [[SNU-423 (line)]] (-3.9), [[HS-578T (line)]] (-3.3), [[A549 (line)]] (-3.0) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Lopinavir (drug)]] (+0.73, unclear); [[Pemetrexed (drug)]] (+0.67, DNA synthesis/repair inhibitor); [[Bosentan (hydrate) (drug)]] (+0.67, unclear); [[Fluvoxamine (drug)]] (+0.65, unclear); [[Dimethyl fumarate (drug)]] (+0.62, unclear); [[Roxadustat (drug)]] (+0.61, unclear); [[Erdafitinib (drug)]] (+0.59, Other TK inhibitor, ⚠ only 6 significant genes); [[Salicylic acid (drug)]] (+0.57, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Pemigatinib (drug)]] (+0.56, Other TK inhibitor); [[Gallic acid (drug)]] (+0.54, Cyclooxygenase inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 11 arrows, 11 of them with an alert ⚠; grade A 0, B 2, C 9.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[P2RY1]] | 0.5 µM | B | P2RY1 activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express P2RY1 (21) vs lines expressing it (27) | the lines without P2RY1: 1.15× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: RGS2, FGF14, BASP1-AS1 |
| [[PTGS2]] | 0.5 µM | B | PTGS2 activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 1.22× the cells of the other lines | 0.085 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.25× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[SCAMP5]] | 0.5 µM | C | SCAMP5 activity raises the cells' numbers under Mozavaptan 0.5 µM (protects the cells) | lines that do not express SCAMP5 (3) vs lines expressing it (45) | the lines without SCAMP5: 0.67× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: ENSG00000262160, SLC4A11, CORO2A; maybe low, not absent |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.22× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.27× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[GSTP1]] | 0.5 µM | C | GSTP1 activity raises the cells' numbers under Mozavaptan 0.5 µM (protects the cells) | lines that do not express GSTP1 (5) vs lines expressing it (43) | the lines without GSTP1: 0.75× the cells of the other lines | 0.043 | ⚠ tissue-confounded; across organs; also absent: MARVELD1 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.22× the cells of the other lines | 0.046 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ITPK1]] | 0.5 µM | C | ITPK1 activity raises the cells' numbers under Mozavaptan 0.5 µM (protects the cells) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 0.75× the cells of the other lines | 0.069 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |
| [[PRR5]], [[PRR5-ARHGAP8]] | 0.5 µM | C | PRR5, PRR5-ARHGAP8 activity raises the cells' numbers under Mozavaptan 0.5 µM (protects the cells) | lines that do not express PRR5, PRR5-ARHGAP8 (4) vs lines expressing them (44) | the lines without PRR5, PRR5-ARHGAP8: 0.75× the cells of the other lines | 0.094 | ⚠ few lines (4 vs 46); across organs; also absent: NECTIN1, PLEKHG3, SNED1; co-absent genes |
| [[LIFR]] | 0.5 µM | C | LIFR activity lowers the cells' numbers under Mozavaptan 0.5 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.21× the cells of the other lines | 0.096 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Mozavaptan"
- `tables/drugdoses.parquet` — dd in 696, 697, 698
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
