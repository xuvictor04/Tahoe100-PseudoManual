---
drug: "Erythromycin"
type: "drug"
salt_base: "Erythromycin"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 39
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Erythromycin

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 8 / 39; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.54.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C12 | 0 / 1 | — | -0.21 | -1.0/-0.9/-1.3 | — |
| 0.5 µM | [[Plate 11]]:C12 | 4 / 4 | — | -0.24 | +0.0/+0.1/-0.3 | — |
| 5 µM | [[Plate 12]]:C12 | 35 / 4 | — | -0.59 | -0.2/-0.0/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (4 genes, none with an alert): [[ACSS1]] 1.22× (z +3.1, 0/37 lines), [[GRK2]] 1.21× (z +3.1, 7/47 lines), [[ENSG00000250602]] 1.26× (z +3.0, 1/44 lines), [[SLC66A1L]] 1.38× (z +2.9, 0/21 lines)

**5 µM** (35 genes, none with an alert; 12 shown): [[MARK1]] 1.28× (z +4.3, 0/23 lines), [[ENSG00000233928]] 1.47× (z +3.8, 0/9 lines), [[ENSG00000248515]] 1.34× (z +3.8, 0/14 lines), [[KDM5D]] 1.31× (z +3.7, 0/18 lines), [[FCHO1]] 1.32× (z +3.6, 7/41 lines), [[CSK]] 1.22× (z +3.6, 4/47 lines), [[SAMD10]] 1.42× (z +3.6, 4/36 lines), [[E4F1]] 1.32× (z +3.5, 9/47 lines), [[DKK3]] 1.32× (z +3.5, 0/19 lines), [[ENSG00000250602]] 1.29× (z +3.4, 2/45 lines), [[ENSG00000277938]] 1.45× (z +3.3, 1/42 lines), [[LINC01320]] 1.39× (z +3.3, 0/7 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[GALNT16]] 0.720× (z -3.6, 9/33 lines)

**0.5 µM** (4 genes, none with an alert): [[LINC02511]] 0.640× (z -3.8, 6/33 lines), [[FAM124A]] 0.736× (z -3.4, 2/30 lines), [[ENSG00000173867]] 0.789× (z -3.3, 7/44 lines), [[ZNF672]] 0.806× (z -3.1, 7/46 lines)

**5 µM** (4 genes, none with an alert): [[ENSG00000254706]] 0.708× (z -3.4, 6/35 lines), [[HSPA4L]] 0.824× (z -3.2, 7/46 lines), [[TMEM30A]] 0.820× (z -3.1, 27/48 lines), [[GLUL]] 0.795× (z -3.1, 11/38 lines)

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
| 0.5 µM | [[NCI-H1573 (line)]] (-3.3) | — |
| 5 µM | — | [[SNU-1 (line)]] (1.36), [[SW48 (line)]] (1.31), [[RKO (line)]] (1.28), [[SNU-423 (line)]] (1.21) · weakest: [[KATO III (line)]] (0.392), [[NCI-H2030 (line)]] (0.424), [[CFPAC-1 (line)]] (0.532) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Fingolimod (hydrochloride) (drug)]] (+0.82, unclear, ⚠ vector dose flagged: toxic); [[Methylprednisolone succinate (drug)]] (+0.81, Glucocorticoid receptor agonist); [[Darolutamide (drug)]] (+0.80, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Ipatasertib (drug)]] (+0.76, PI3K/AKT inhibitor); [[Imiquimod (hydrochloride) (drug)]] (+0.75, unclear, ⚠ vector dose flagged: toxic); [[Celecoxib (drug)]] (+0.74, Cyclooxygenase inhibitor); [[Aprepitant (drug)]] (+0.72, unclear); [[Docetaxel (Trihydrate) (drug)]] (+0.65, Microtubule inhibitor); [[Decitabine (drug)]] (+0.64, DNA methyltransferase inhibitor); [[Pemigatinib (drug)]] (+0.62, Other TK inhibitor); [[Bimatoprost (drug)]] (+0.59, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 17 arrows, 17 of them with an alert ⚠; grade A 0, B 10, C 7. Shown: the 15 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPTLC3]] | 0.5 µM | B | SPTLC3 activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 1.20× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[SERPINE2]] | 5 µM | B | SERPINE2 activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express SERPINE2 (21) vs lines expressing it (27) | the lines without SERPINE2: 1.14× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[VIL1]] | 0.5 µM | B | VIL1 activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express VIL1 (34) vs lines expressing it (14) | the lines without VIL1: 1.17× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: LINC02964, NPSR1-AS1, MOGAT3; maybe low, not absent |
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 1.20× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[ENSG00000259200]] | 5 µM | B | ENSG00000259200 activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 1.19× the cells of the other lines | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[LGALS3BP]] | 5 µM | B | LGALS3BP activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express LGALS3BP (7) vs lines expressing it (41) | the lines without LGALS3BP: 1.22× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: LGALS3, KLF4, APOL6 |
| [[SERPINE2]] | 0.5 µM | B | SERPINE2 activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express SERPINE2 (21) vs lines expressing it (27) | the lines without SERPINE2: 1.12× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[ENSG00000232884]] | 0.5 µM | B | ENSG00000232884 activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000232884 (12) vs lines expressing it (36) | the lines without ENSG00000232884: 1.18× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000235609, NRIP1, ATXN1; maybe low, not absent |
| [[IL15]] | 5 µM | B | IL15 activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 1.12× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[ZNF329]] | 0.5 µM | B | ZNF329 activity raises the cells' numbers under Erythromycin 0.5 µM (protects the cells) | lines that do not express ZNF329 (7) vs lines expressing it (41) | the lines without ZNF329: 0.81× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: C2orf27A |
| [[PYGB]] | 5 µM | C | PYGB activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 1.37× the cells of the other lines | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[STX1A]] | 5 µM | C | STX1A activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express STX1A (3) vs lines expressing it (45) | the lines without STX1A: 1.33× the cells of the other lines | 0.043 | ⚠ few lines (3 vs 47); across organs; also absent: RABGEF1P3, SKAP2, PYGB; maybe low, not absent |
| [[ENSG00000255031]] | 5 µM | C | ENSG00000255031 activity lowers the cells' numbers under Erythromycin 5 µM (makes them more sensitive) | lines that do not express ENSG00000255031 (3) vs lines expressing it (45) | the lines without ENSG00000255031: 1.31× the cells of the other lines | 0.068 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: GLMP, TCIRG1, MT1X; maybe low, not absent |
| [[PYGB]] | 0.5 µM | C | PYGB activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express PYGB (3) vs lines expressing it (45) | the lines without PYGB: 1.31× the cells of the other lines | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: PBX4, STX1A, UGDH; maybe low, not absent |
| [[ENSG00000255031]] | 0.5 µM | C | ENSG00000255031 activity lowers the cells' numbers under Erythromycin 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000255031 (3) vs lines expressing it (45) | the lines without ENSG00000255031: 1.28× the cells of the other lines | 0.091 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: GLMP, TCIRG1, MT1X; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Erythromycin"
- `tables/drugdoses.parquet` — dd in 426, 427, 428
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
