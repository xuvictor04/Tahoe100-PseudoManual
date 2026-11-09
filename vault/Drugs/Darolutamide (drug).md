---
drug: "Darolutamide"
type: "drug"
salt_base: "Darolutamide"
targets: "AR"
moa_fine: "Androgen receptor antagonist"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 5
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Darolutamide

*Androgen receptor antagonist (inhibitor/antagonist) · targets: AR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 2 / 5; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.51 / 0.44.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F11 | 0 / 1 | — | +0.58 | -0.1/+1.4/+0.5 | — |
| 0.5 µM | [[Plate 11]]:F11 | 1 / 1 | — | +0.11 | +0.1/+1.0/+0.6 | — |
| 5 µM | [[Plate 12]]:F11 | 5 / 0 | — | +0.04 | -0.2/+1.0/+0.9 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[LINC02643]] 1.44× (z +2.9, 0/9 lines)

**5 µM** (5 genes, none with an alert): [[LINC02335]] 1.76× (z +4.2, 0/7 lines), [[EPS8L3]] 1.50× (z +3.9, 0/13 lines), [[LINC02253]] 1.33× (z +3.0, 0/12 lines), [[PLTP]] 1.32× (z +3.0, 0/20 lines), [[MGAT4C]] 1.29× (z +3.0, 0/13 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[FAHD2A]] 0.826× (z -3.3, 5/47 lines)

**0.5 µM** (1 gene, none with an alert): [[FAM124A]] 0.750× (z -3.2, 4/29 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 048]] (+2.3), [[Module 054]] (+2.0) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 5 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Methylprednisolone succinate (drug)]] (+0.87, Glucocorticoid receptor agonist); [[Celecoxib (drug)]] (+0.82, Cyclooxygenase inhibitor); [[Decitabine (drug)]] (+0.81, DNA methyltransferase inhibitor); [[Ipatasertib (drug)]] (+0.81, PI3K/AKT inhibitor); [[Docetaxel (Trihydrate) (drug)]] (+0.80, Microtubule inhibitor); [[Erythromycin (drug)]] (+0.80, unclear); [[Tranilast (drug)]] (+0.80, unclear, ⚠ only 6 significant genes); [[Nimesulide (drug)]] (+0.80, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Bimatoprost (drug)]] (+0.76, unclear); [[Bendamustine (drug)]] (+0.75, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 18 arrows, 18 of them with an alert ⚠; grade A 0, B 12, C 6. Shown: the 15 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.79× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[PLA2G4A]] | 0.05 µM | B | PLA2G4A activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.85× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[PRR36]] | 0.05 µM | B | PRR36 activity lowers the cells' numbers under Darolutamide 0.05 µM (makes them more sensitive) | lines that do not express PRR36 (19) vs lines expressing it (29) | the lines without PRR36: 1.20× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: NUP210, TTC9, CGN |
| [[PAPPA]] | 0.05 µM | B | PAPPA activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.80× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[CD44]] | 0.05 µM | B | CD44 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express CD44 (15) vs lines expressing it (33) | the lines without CD44: 0.79× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16 |
| [[MYH14]] | 0.05 µM | B | MYH14 activity lowers the cells' numbers under Darolutamide 0.05 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.25× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.78× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[PRSS23]] | 0.05 µM | B | PRSS23 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 0.79× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[F2RL2]] | 0.05 µM | B | F2RL2 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express F2RL2 (32) vs lines expressing it (16) | the lines without F2RL2: 0.78× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: SRGN, KCNMA1, PAPPA |
| [[SRGN]] | 0.05 µM | B | SRGN activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express SRGN (30) vs lines expressing it (18) | the lines without SRGN: 0.78× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SIRLNT, SPOCK1, KIRREL3 |
| [[SLFN5]] | 0.05 µM | B | SLFN5 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 0.79× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[PSMB8]] | 0.05 µM | C | PSMB8 activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.73× the cells of the other lines | 0.027 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[CEBPD]], [[GCA]] | 0.05 µM | C | CEBPD, GCA activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.72× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[TBILA]] | 0.05 µM | C | TBILA activity raises the cells' numbers under Darolutamide 0.05 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.76× the cells of the other lines | 0.041 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Darolutamide"
- `tables/drugdoses.parquet` — dd in 332, 333, 334
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
