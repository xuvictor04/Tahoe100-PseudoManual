---
drug: "Fulvestrant"
type: "drug"
salt_base: "Fulvestrant"
targets: "ESR1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 8
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Fulvestrant

*unclear (inhibitor/antagonist) · targets: ESR1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 4 / 8 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.10 / -0.03.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F3 | 0 / 4 | — | -0.06 | -0.3/+0.1/+0.3 | — |
| 0.5 µM | [[Plate 11]]:F3 | 7 / 1 | — | -0.44 | -1.2/-1.2/-0.2 | — |
| 5 µM | [[Plate 12]]:F3 | 0 / 0 | — | +0.94 | -0.1/-0.2/-0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (7 genes, none with an alert): [[TMEM150C]] 1.37× (z +3.4, 2/29 lines), [[GAP43]] 1.47× (z +3.2, 1/19 lines), [[FAHD2A]] 1.20× (z +3.1, 7/47 lines), [[SLC12A4]] 1.23× (z +3.1, 12/46 lines), [[MMP17]] 1.30× (z +3.1, 2/26 lines), [[ENSG00000272297]] 1.32× (z +3.1, 0/17 lines), [[DPP6]] 1.25× (z +2.9, 3/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[IFTAP]] 0.759× (z -3.1, 6/45 lines), [[CHN2]] 0.817× (z -3.1, 2/27 lines), [[RPS10P7]] 0.771× (z -2.9, 7/43 lines), [[TLE6]] 0.728× (z -2.8, 8/40 lines)

**0.5 µM** (1 gene, none with an alert): [[PHOSPHO2]] 0.768× (z -3.2, 9/44 lines)

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

⚠ This drug's own vector: only 8 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Idoxuridine (drug)]] (+0.74, DNA synthesis/repair inhibitor, ⚠ only 4 significant genes); [[Celecoxib (drug)]] (+0.66, Cyclooxygenase inhibitor); [[Methylprednisolone succinate (drug)]] (+0.62, Glucocorticoid receptor agonist); [[Macitentan (drug)]] (+0.62, unclear, ⚠ only 5 significant genes); [[Ipatasertib (drug)]] (+0.62, PI3K/AKT inhibitor); [[Oxaprozin (drug)]] (+0.60, Cyclooxygenase inhibitor); [[Erythromycin (drug)]] (+0.59, unclear); [[Darolutamide (drug)]] (+0.57, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Thymol (drug)]] (+0.56, unclear); [[Lactate (calcium) (drug)]] (+0.55, unclear); [[Hydroxyurea (drug)]] (+0.54, DNA synthesis/repair inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 13 arrows, 13 of them with an alert ⚠; grade A 0, B 9, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.83× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[CNRIP1]] | 5 µM | B | CNRIP1 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.88× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[RSPO3]] | 5 µM | B | RSPO3 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.82× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.85× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ENSG00000251537]] | 5 µM | B | ENSG00000251537 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express ENSG00000251537 (9) vs lines expressing it (39) | the lines without ENSG00000251537: 0.84× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: FBXW10B, PCED1B, NHS; maybe low, not absent |
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.79× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[PTGER4]] | 5 µM | B | PTGER4 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express PTGER4 (12) vs lines expressing it (36) | the lines without PTGER4: 0.85× the cells of the other lines | 0.092 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[TGFBR2]] | 5 µM | B | TGFBR2 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express TGFBR2 (7) vs lines expressing it (41) | the lines without TGFBR2: 0.77× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: VDR, TRIB1, MET |
| [[LIF]] | 5 µM | B | LIF activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express LIF (10) vs lines expressing it (38) | the lines without LIF: 0.81× the cells of the other lines | 0.0996 | ⚠ within organs, on part of the lines; co-occurs with WNK2; also absent: CD82, RABGEF1P3, ENSG00000236213 |
| [[TBILA]] | 5 µM | C | TBILA activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.79× the cells of the other lines | 0.039 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[PSMB8]] | 5 µM | C | PSMB8 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.75× the cells of the other lines | 0.047 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[PRRG1]] | 5 µM | C | PRRG1 activity raises the cells' numbers under Fulvestrant 5 µM (protects the cells) | lines that do not express PRRG1 (3) vs lines expressing it (45) | the lines without PRRG1: 0.76× the cells of the other lines | 0.056 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: MYD88, S100A6, AIFM2 |
| [[ZC3HAV1L]] | 5 µM | C | ZC3HAV1L activity lowers the cells' numbers under Fulvestrant 5 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.26× the cells of the other lines | 0.071 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Fulvestrant"
- `tables/drugdoses.parquet` — dd in 474, 475, 476
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
