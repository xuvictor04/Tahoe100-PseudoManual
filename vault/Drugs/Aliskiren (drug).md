---
drug: "Aliskiren"
type: "drug"
salt_base: "Aliskiren"
targets: "REN"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 13
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Aliskiren

*unclear (inhibitor/antagonist) · targets: REN · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 13 / 4; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.26 / 0.47.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C9 | 1 / 0 | — | +0.49 | +0.2/-0.1/+0.7 | — |
| 0.5 µM | [[Plate 05]]:C9 | 4 / 9 | — | +0.15 | +0.7/+0.4/+0.7 | — |
| 5 µM | [[Plate 14]]:C9 | 2 / 2 | 0.798 | +0.02 | +2.3/+0.9/+2.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000260710]] 1.43× (z +2.8, 2/27 lines)

**0.5 µM** (4 genes, none with an alert): [[LMAN2]] 1.24× (z +3.6, 24/49 lines), [[TMEM183A]] 1.31× (z +3.6, 15/48 lines), [[WBP11]] 1.23× (z +3.2, 26/49 lines), [[SLC9A3R1]] 1.26× (z +3.2, 13/47 lines)

**5 µM** (2 genes, none with an alert): [[ENSG00000261227]] 1.48× (z +3.1, 5/29 lines), [[PCLAF]] 1.21× (z +2.8, 8/46 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (9 genes, none with an alert): [[RABEP2]] 0.807× (z -3.6, 17/48 lines), [[PGS1]] 0.773× (z -3.5, 17/48 lines), [[TEP1]] 0.794× (z -3.5, 22/49 lines), [[SNRNP35]] 0.813× (z -3.4, 11/48 lines), [[SPRED3]] 0.768× (z -3.2, 11/47 lines), [[ZNF212]] 0.817× (z -3.2, 10/48 lines), [[CROCCP3]] 0.747× (z -3.1, 6/43 lines), [[ATP7B]] 0.826× (z -3.0, 6/45 lines), [[KLF7]] 0.816× (z -2.6, 14/37 lines)

**5 µM** (2 genes, none with an alert): [[PRR5-ARHGAP8]] 0.808× (z -3.5, 6/40 lines), [[ENSG00000253100]] 0.795× (z -3.0, 4/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 234]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[A-172 (line)]] (-5.4), [[J82 (line)]] (-3.4), [[HOP62 (line)]] (-3.1), [[SNU-423 (line)]] (-3.0), [[RKO (line)]] (-3.0) | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Aspirin (drug)]] (+0.57, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[γ-Oryzanol (drug)]] (+0.57, DNA methyltransferase inhibitor, ⚠ only 1 significant gene); [[Riluzole hydrochloride (drug)]] (+0.55, unclear); [[Gemfibrozil (drug)]] (+0.52, unclear, ⚠ only 2 significant genes); [[Sulfatinib (drug)]] (+0.51, Multi-TK inhibitor); [[Gefitinib (drug)]] (+0.51, EGFR/ERBB inhibitor); [[Arbutin (drug)]] (+0.50, unclear); [[Nevirapine (drug)]] (+0.49, unclear, ⚠ only 7 significant genes); [[Hydroxyfasudil (drug)]] (+0.45, unclear); [[Adagrasib (drug)]] (+0.44, RAS inhibitor); [[Fluvoxamine (maleate) (drug)]] (+0.41, unclear); [[Terfenadine (drug)]] (+0.40, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 133 arrows, 133 of them with an alert ⚠; grade A 0, B 128, C 5. Shown: the 15 strongest; 118 more arrows (118 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MAL2]] | 0.5 µM | B | MAL2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express MAL2 (31) vs lines expressing it (17) | the lines without MAL2: 0.73× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1 |
| [[C1orf116]], [[IRF6]] | 0.5 µM | B | C1orf116, IRF6 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (17) | the lines without C1orf116, IRF6: 0.73× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[CATSPERB]] | 0.5 µM | B | CATSPERB activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express CATSPERB (30) vs lines expressing it (18) | the lines without CATSPERB: 0.74× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SGPP2, TC2N, ST14 |
| [[MPZL3]] | 0.5 µM | B | MPZL3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express MPZL3 (25) vs lines expressing it (23) | the lines without MPZL3: 0.74× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[INAVA]], [[MROH3P]] | 0.5 µM | B | INAVA, MROH3P activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express INAVA, MROH3P (29) vs lines expressing them (19) | the lines without INAVA, MROH3P: 0.74× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[AQP3]] | 0.5 µM | B | AQP3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express AQP3 (19) vs lines expressing it (29) | the lines without AQP3: 0.74× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[LIPH]] | 0.5 µM | B | LIPH activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express LIPH (27) vs lines expressing it (21) | the lines without LIPH: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: CATSPERB, TC2N, SDR16C5 |
| [[GALNT3]] | 0.5 µM | B | GALNT3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express GALNT3 (30) vs lines expressing it (18) | the lines without GALNT3: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[ABCC3]] | 0.5 µM | B | ABCC3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express ABCC3 (16) vs lines expressing it (32) | the lines without ABCC3: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[ELF3]] | 0.5 µM | B | ELF3 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express ELF3 (23) vs lines expressing it (25) | the lines without ELF3: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[IL1R2]] | 0.5 µM | B | IL1R2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express IL1R2 (23) vs lines expressing it (25) | the lines without IL1R2: 0.76× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TMEM139, NMRAL2P-1, NPSR1-AS1 |
| [[STON2]] | 0.5 µM | B | STON2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express STON2 (19) vs lines expressing it (29) | the lines without STON2: 0.81× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3 |
| [[LCN2]] | 0.5 µM | B | LCN2 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express LCN2 (33) vs lines expressing it (15) | the lines without LCN2: 0.74× the cells of the other lines | 0.022 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: PRSS8, RAB25, TMPRSS4 |
| [[ENSG00000243004]] | 0.5 µM | B | ENSG00000243004 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express ENSG00000243004 (31) vs lines expressing it (17) | the lines without ENSG00000243004: 0.74× the cells of the other lines | 0.024 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: MACC1, TMEM125, GRHL2 |
| [[ADGRF1]] | 0.5 µM | B | ADGRF1 activity raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | lines that do not express ADGRF1 (35) vs lines expressing it (13) | the lines without ADGRF1: 0.71× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Aliskiren"
- `tables/drugdoses.parquet` — dd in 66, 67, 68
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
