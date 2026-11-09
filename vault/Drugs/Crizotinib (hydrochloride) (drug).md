---
drug: "Crizotinib (hydrochloride)"
type: "drug"
salt_base: "Crizotinib"
targets: "ALK, MET, ROS1"
moa_fine: "Multi-TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 98
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Crizotinib (hydrochloride)

*Multi-TK inhibitor (inhibitor/antagonist) · targets: ALK, MET, ROS1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 22 / 98; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.32 / 0.22.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F8 | 0 / 0 | — | -0.02 | +0.1/+0.3/+0.6 | — |
| 0.5 µM | [[Plate 11]]:F8 | 17 / 5 | — | -0.69 | +0.7/+0.4/+0.7 | — |
| 5 µM | [[Plate 12]]:F8 | 13 / 85 | — | +0.50 | -1.3/+1.2/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (17 genes, none with an alert; 12 shown): [[TRHDE]] 1.29× (z +3.6, 0/19 lines), [[SRSF5]] 1.22× (z +3.6, 21/48 lines), [[PREX1]] 1.23× (z +3.4, 1/28 lines), [[SCRIB]] 1.29× (z +3.4, 9/46 lines), [[SALL4]] 1.27× (z +3.4, 0/25 lines), [[IPO4]] 1.35× (z +3.4, 10/46 lines), [[COL19A1]] 1.48× (z +3.3, 0/9 lines), [[ENSG00000283765]] 1.44× (z +3.2, 7/41 lines), [[DPYS]] 1.60× (z +3.2, 1/21 lines), [[CD200R1]] 1.60× (z +3.2, 2/32 lines), [[GDNF-AS1]] 1.42× (z +3.0, 0/10 lines), [[WNK3]] 1.21× (z +3.0, 2/18 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[SCD]] 1.37× (z +4.5, 32/49 lines), [[LPIN1]] 1.20× (z +4.1, 17/48 lines), [[ACAT2]] 1.26× (z +3.4, 11/48 lines), [[HMGCR]] 1.27× (z +3.4, 15/48 lines), [[CYP51A1]] 1.24× (z +3.4, 21/48 lines), [[LIPG]] 1.35× (z +3.3, 9/23 lines), [[FDFT1]] 1.26× (z +3.2, 18/47 lines), [[SQLE]] 1.31× (z +3.1, 17/47 lines), [[HMGCS1]] 1.28× (z +3.0, 19/48 lines), [[FDPS]] 1.27× (z +3.0, 22/49 lines), [[IDI1]] 1.24× (z +2.9, 15/49 lines), [[INSIG1]] 1.32× (z +2.7, 18/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (5 genes, none with an alert): [[CIAO3]] 0.763× (z -3.9, 9/43 lines), [[GTPBP3]] 0.783× (z -3.7, 11/44 lines), [[ENSG00000203546]] 0.754× (z -3.3, 8/43 lines), [[MAST1]] 0.809× (z -3.1, 7/45 lines), [[C3orf18]] 0.719× (z -3.0, 5/26 lines)

**5 µM** (85 genes, none with an alert; 12 shown): [[OR51B5]] 0.715× (z -4.8, 16/32 lines), [[TRIM22]] 0.633× (z -4.6, 20/30 lines), [[PCLO]] 0.727× (z -4.6, 16/34 lines), [[CYP2J2]] 0.654× (z -4.4, 10/35 lines), [[LINC02112]] 0.666× (z -4.2, 9/40 lines), [[HBG2]] 0.621× (z -4.2, 7/29 lines), [[ENSG00000287231]] 0.617× (z -4.2, 4/25 lines), [[IFI44L]] 0.622× (z -4.2, 18/26 lines), [[ENSG00000291144]] 0.514× (z -4.1, 12/35 lines), [[ENSG00000239920]] 0.731× (z -4.1, 18/46 lines), [[COLQ]] 0.673× (z -4.1, 11/46 lines), [[ANKRD7]] 0.722× (z -4.0, 9/37 lines)

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
| 0.5 µM | — | [[HepG2_C3A (line)]] (2.04), [[HCT15 (line)]] (1.64), [[SW 1088 (line)]] (1.62), [[SW48 (line)]] (1.44) · weakest: [[NCI-H2347 (line)]] (-0.309), [[C32 (line)]] (-0.165), [[CFPAC-1 (line)]] (-0.0660) |
| 5 µM | — | [[SW 1088 (line)]] (1.68), [[HCT15 (line)]] (1.45), [[SW48 (line)]] (1.42), [[SNU-423 (line)]] (1.39) · weakest: [[NCI-H2122 (line)]] (0.286), [[HEC-1-A (line)]] (0.473), [[KATO III (line)]] (0.600) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[crizotinib (drug)]] (+0.74, Multi-TK inhibitor); [[Berbamine (dihydrochloride) (drug)]] (+0.50, unclear); [[Fedratinib (hydrochloride hydrate) (drug)]] (+0.42, JAK/STAT inhibitor); [[APTO-253 (drug)]] (+0.41, unclear, ⚠ only 4 significant genes); [[Oleic acid (drug)]] (+0.39, unclear, ⚠ only 1 significant gene); [[BAY1125976 (drug)]] (+0.38, PI3K/AKT inhibitor); [[Pitavastatin (Calcium) (drug)]] (+0.37, unclear, ⚠ vector dose flagged: cell-cycle shift); [[HI-TOPK-032 (drug)]] (+0.36, unclear); [[Pexidartinib (hydrochloride) (drug)]] (+0.34, Multi-TK inhibitor); [[Tofacitinib (drug)]] (+0.34, JAK/STAT inhibitor); [[(S)-Crizotinib (drug)]] (+0.31, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

None: no gene was found to set how the cells fare under it.

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[MET]] | [[TNFAIP1]] | moves it that way too | B | MET activity raises TNFAIP1's level | compounds that target MET: 3 of 4 lower it (Cabozantinib, Crizotinib / crizotinib, c-Kit-IN-1) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Crizotinib (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 293, 294, 295
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
