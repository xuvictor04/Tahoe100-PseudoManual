---
drug: "Sulfatinib"
type: "drug"
salt_base: "Sulfatinib"
targets: "FLT1, KDR, FLT4, FGFR1, CSF1R"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 239
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Sulfatinib

*Multi-TK inhibitor (inhibitor/antagonist) · targets: FLT1, KDR, FLT4, FGFR1, CSF1R · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 239; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / -0.44.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G11 | 1 / 0 | — | -0.15 | -0.2/-0.4/-0.8 | — |
| 0.5 µM | [[Plate 08]]:G11 | 0 / 0 | — | +0.08 | -1.0/-1.2/-1.3 | — |
| 5 µM | [[Plate 09]]:G11 | 90 / 149 | — | +0.44 | +1.4/+1.6/+1.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[RTN4RL1]] 1.33× (z +2.8, 2/27 lines)

**5 µM** (90 genes, none with an alert; 12 shown): [[APOLD1]] 1.31× (z +7.0, 24/49 lines), [[OSCP1]] 1.45× (z +4.5, 8/42 lines), [[ENSG00000286533]] 1.43× (z +4.1, 20/44 lines), [[ACAT2]] 1.33× (z +4.0, 15/47 lines), [[GDE1]] 1.28× (z +3.9, 14/48 lines), [[LINC01208]] 1.42× (z +3.9, 6/44 lines), [[LRRC23]] 1.52× (z +3.7, 31/49 lines), [[CFAP210]] 2.02× (z +3.7, 20/45 lines), [[FBXO32]] 1.30× (z +3.7, 11/35 lines), [[POLR1D]] 1.20× (z +3.6, 18/48 lines), [[TMEM97]] 1.42× (z +3.6, 11/44 lines), [[IDI1]] 1.33× (z +3.6, 20/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (149 genes, none with an alert; 12 shown): [[TTC7B]] 0.698× (z -5.6, 26/39 lines), [[CDYL2]] 0.713× (z -4.7, 16/28 lines), [[ABTB3]] 0.757× (z -4.7, 14/26 lines), [[HSPA12A]] 0.805× (z -4.5, 15/44 lines), [[SSBP3]] 0.818× (z -4.3, 17/47 lines), [[ENSG00000228793]] 0.664× (z -4.3, 8/40 lines), [[SMURF1]] 0.815× (z -4.2, 27/48 lines), [[HIVEP3]] 0.764× (z -4.2, 26/42 lines), [[PPP2R2C]] 0.727× (z -4.2, 13/30 lines), [[APBB2]] 0.829× (z -4.1, 23/49 lines), [[ENSG00000255367]] 0.723× (z -4.1, 5/28 lines), [[SLC4A3]] 0.677× (z -4.1, 10/36 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 095]] (+2.2), [[Module 064]] (+2.2), [[Module 059]] (+2.1) | [[Module 193]] (-2.3), [[Module 195]] (-2.2), [[Module 170]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HOP62 (line)]] (-3.6) | — |
| 5 µM | — | [[H4 (line)]] (1.59), [[HOP62 (line)]] (1.58), [[SW 1088 (line)]] (1.42), [[A549 (line)]] (1.36) · weakest: [[NCI-H2122 (line)]] (0.544), [[SNU-1 (line)]] (0.696), [[C-33 A (line)]] (0.728) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Arbutin (drug)]] (+0.70, unclear); [[Tolcapone (drug)]] (+0.67, unclear, ⚠ only 6 significant genes); [[Almonertinib (hydrochloride) (drug)]] (+0.57, EGFR/ERBB inhibitor); [[Adagrasib (drug)]] (+0.55, RAS inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.55, unclear); [[Silodosin (drug)]] (+0.54, unclear); [[Bendamustine (drug)]] (+0.54, DNA synthesis/repair inhibitor); [[Aliskiren (drug)]] (+0.51, unclear); [[Cobimetinib (drug)]] (+0.51, MEK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 51 arrows, 51 of them with an alert ⚠; grade A 0, B 25, C 26. Shown: the 15 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[LINC02057]] | 5 µM | B | LINC02057 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.78× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[SLFN5]] | 5 µM | B | SLFN5 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.75× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[NLGN4X]] | 0.5 µM | B | NLGN4X activity raises the cells' numbers under Sulfatinib 0.5 µM (protects the cells) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 0.96× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.84× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[NLGN4X]] | 5 µM | B | NLGN4X activity lowers the cells' numbers under Sulfatinib 5 µM (makes them more sensitive) | lines that do not express NLGN4X (37) vs lines expressing it (11) | the lines without NLGN4X: 1.12× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01029, ENSG00000291025, ANKRD20A8P |
| [[CKMT1B]] | 0.5 µM | B | CKMT1B activity raises the cells' numbers under Sulfatinib 0.5 µM (protects the cells) | lines that do not express CKMT1B (28) vs lines expressing it (20) | the lines without CKMT1B: 0.84× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: CKMT1A, SYK, PPP1R1B |
| [[MYH14]] | 0.5 µM | B | MYH14 activity raises the cells' numbers under Sulfatinib 0.5 µM (protects the cells) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 0.79× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ENSG00000225751]] | 5 µM | B | ENSG00000225751 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express ENSG00000225751 (14) vs lines expressing it (34) | the lines without ENSG00000225751: 0.77× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: SLFN5, MMRN2, MGLL |
| [[ENSG00000230615]] | 0.5 µM | B | ENSG00000230615 activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000230615 (25) vs lines expressing it (23) | the lines without ENSG00000230615: 1.26× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: FRMD4A, ENSG00000253891, SRGN; maybe low, not absent |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.78× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[SIRLNT]] | 0.5 µM | B | SIRLNT activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 1.27× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[PRSS23]] | 5 µM | B | PRSS23 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 0.76× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[PTGS2]] | 5 µM | B | PTGS2 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express PTGS2 (27) vs lines expressing it (21) | the lines without PTGS2: 0.82× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.79× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[PRDM5]] | 0.5 µM | B | PRDM5 activity lowers the cells' numbers under Sulfatinib 0.5 µM (makes them more sensitive) | lines that do not express PRDM5 (13) vs lines expressing it (35) | the lines without PRDM5: 1.18× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| KDR | [[PPARD]] | moves it that way too | B | KDR activity raises PPARD's level | compounds that target KDR: 5 of 8 lower it (Cabozantinib, Ponatinib, Regorafenib, Sulfatinib, Sunitinib) | 62% of the class's compounds vs 6.2% of all compounds | 0.036 | ⚠ off-target possible; 5 compounds; artifact flags |
| KDR | [[DNAJB6]] | does not move it that way (the class's other compounds do) | B | KDR activity raises DNAJB6's level | compounds that target KDR: 3 of 8 lower it (Cabozantinib, Ponatinib, c-Kit-IN-1) | 38% of the class's compounds vs 1.7% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| KDR | [[DUSP10]] | does not move it that way (the class's other compounds do) | B | KDR activity raises DUSP10's level | compounds that target KDR: 4 of 8 lower it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| KDR | [[PGLS-DT]] | does not move it that way (the class's other compounds do) | B | KDR activity lowers PGLS-DT's level | compounds that target KDR: 4 of 8 raise it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Sulfatinib"
- `tables/drugdoses.parquet` — dd in 964, 965, 966
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
