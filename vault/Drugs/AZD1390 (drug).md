---
drug: "AZD1390"
type: "drug"
salt_base: "AZD1390"
targets: "ATM"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 16
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# AZD1390

*unclear (inhibitor/antagonist) · targets: ATM · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 13 / 5 / 16; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.09 / 0.33.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F9 | 10 / 3 | — | +0.12 | +0.2/+1.3/-0.6 | — |
| 0.5 µM | [[Plate 02]]:F9 | 5 / 0 | — | -0.28 | +0.2/+1.3/+0.6 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F9 | 8 / 8 | — | -0.03 | -2.0/+0.3/-0.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[SCG5]] 1.27× (z +3.6, 5/45 lines), [[CENPE]] 1.25× (z +3.6, 20/48 lines), [[DEPDC1B]] 1.20× (z +3.4, 12/48 lines), [[PIF1]] 1.32× (z +3.3, 14/47 lines), [[ASPM]] 1.28× (z +3.3, 18/47 lines), [[FAM83D]] 1.27× (z +3.2, 13/48 lines), [[ENSG00000250271]] 1.59× (z +3.0, 3/15 lines), [[KIF14]] 1.21× (z +3.0, 17/47 lines), [[TIPARP]] 1.29× (z +2.9, 19/47 lines), [[FAM72D]] 1.40× (z +2.9, 6/42 lines)

**0.5 µM** (5 genes, none with an alert): [[E2F7]] 1.31× (z +3.5, 14/43 lines), [[TPRA1]] 1.31× (z +3.1, 8/48 lines), [[ALDH1A3]] 1.49× (z +3.0, 11/28 lines), [[MIR181A1HG]] 1.31× (z +2.9, 15/41 lines), [[TIPARP]] 1.80× (z +2.8, 19/47 lines)

**5 µM** (8 genes, none with an alert): [[TATDN1]] 1.39× (z +3.7, 16/47 lines), [[TIPARP]] 1.77× (z +3.7, 22/47 lines), [[ENSG00000228793]] 1.81× (z +3.4, 5/32 lines), [[ALDH1A3]] 1.58× (z +3.1, 7/27 lines), [[EIF5]] 1.34× (z +2.9, 11/48 lines), [[GABARAPL1]] 1.44× (z +2.8, 7/45 lines), [[BAG1]] 1.31× (z +2.8, 6/46 lines), [[SNHG17]] 1.53× (z +2.6, 2/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[CDH1]] 0.777× (z -3.6, 0/17 lines), [[VAMP5]] 0.711× (z -3.1, 4/35 lines), [[KMT5C]] 0.788× (z -2.8, 6/47 lines)

**5 µM** (8 genes, none with an alert): [[TRERF1]] 0.697× (z -3.4, 15/42 lines), [[MIR924HG]] 0.625× (z -3.0, 15/40 lines), [[PSAT1]] 0.621× (z -2.9, 13/38 lines), [[EGR1]] 0.413× (z -2.9, 25/46 lines), [[SLC39A8]] 0.763× (z -2.8, 3/35 lines), [[ATAD5]] 0.743× (z -2.8, 10/48 lines), [[GPI]] 0.694× (z -2.8, 25/47 lines), [[PLEKHA2]] 0.757× (z -2.6, 14/43 lines)

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
| 5 µM | [[C32 (line)]] (-4.6), [[HCT15 (line)]] (-3.4), [[RPMI-7951 (line)]] (-3.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar.*

- [[Temsirolimus (drug)]] (+0.76, MTOR inhibitor); [[Rapamycin (drug)]] (+0.74, MTOR inhibitor); [[ULK-101 (drug)]] (+0.73, unclear); [[MK-3903 (drug)]] (+0.66, unclear); [[Resveratrol (drug)]] (+0.64, unclear); [[Drospirenone (drug)]] (+0.62, unclear); [[Docetaxel (Trihydrate) (drug)]] (+0.60, Microtubule inhibitor); [[Bimatoprost (drug)]] (+0.60, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SLC2A9]] | 5 µM | B | SLC2A9 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express SLC2A9 (6) vs lines expressing it (42) | the lines without SLC2A9: 1.42× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: VDR, SEMA4G, TBC1D8B; maybe low, not absent |
| [[LINC02306]] | 5 µM | B | LINC02306 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express LINC02306 (13) vs lines expressing it (35) | the lines without LINC02306: 1.28× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[HIPK2]] | 5 µM | B | HIPK2 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express HIPK2 (5) vs lines expressing it (43) | the lines without HIPK2: 1.46× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[ENSG00000259200]] | 5 µM | B | ENSG00000259200 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 1.22× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[VAV3]] | 5 µM | B | VAV3 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express VAV3 (30) vs lines expressing it (18) | the lines without VAV3: 1.19× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |
| [[TRIB1]] | 5 µM | B | TRIB1 activity lowers the cells' numbers under AZD1390 5 µM (makes them more sensitive) | lines that do not express TRIB1 (6) vs lines expressing it (42) | the lines without TRIB1: 1.34× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[EZR]], [[TMC7]] | 5 µM | C | EZR, TMC7 activity raises the cells' numbers under AZD1390 5 µM (protects the cells) | lines that do not express EZR, TMC7 (3) vs lines expressing them (45) | the lines without EZR, TMC7: 0.68× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: GRHL1, ENSG00000257489, NUDT7; maybe low, not absent; co-absent genes |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "AZD1390"
- `tables/drugdoses.parquet` — dd in 36, 37, 38
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
