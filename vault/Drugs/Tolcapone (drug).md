---
drug: "Tolcapone"
type: "drug"
salt_base: "Tolcapone"
targets: "COMT"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 6
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tolcapone

*unclear (inhibitor/antagonist) · targets: COMT · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 2 / 6; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.35 / 0.32.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C7 | 1 / 1 | — | +0.28 | -0.5/-0.5/+0.5 | — |
| 0.5 µM | [[Plate 05]]:C7 | 2 / 0 | — | +0.64 | -0.3/-0.3/+0.4 | — |
| 5 µM | [[Plate 14]]:C7 | 4 / 2 | 0.735 | +0.31 | -0.2/-0.1/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000282943]] 1.32× (z +2.8, 1/22 lines)

**0.5 µM** (2 genes, none with an alert): [[SDHA]] 1.31× (z +5.1, 28/49 lines), [[HCG20]] 1.41× (z +3.5, 9/43 lines)

**5 µM** (4 genes, none with an alert): [[KLRD1]] 1.32× (z +3.1, 6/40 lines), [[MSMO1]] 1.21× (z +2.9, 17/48 lines), [[ENSG00000282943]] 1.22× (z +2.9, 2/24 lines), [[CD247]] 1.25× (z +2.8, 3/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[HLCS-AS1]] 0.724× (z -3.1, 4/41 lines)

**5 µM** (2 genes, none with an alert): [[LINC00659]] 0.726× (z -3.4, 0/20 lines), [[ENSG00000258944]] 0.776× (z -3.3, 8/43 lines)

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
| 5 µM | [[CHP-212 (line)]] (-3.0) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 6 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Sulfatinib (drug)]] (+0.67, Multi-TK inhibitor); [[Gemfibrozil (drug)]] (+0.66, unclear, ⚠ only 2 significant genes); [[Terfenadine (drug)]] (+0.66, unclear); [[Adagrasib (drug)]] (+0.65, RAS inhibitor); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.61, unclear); [[Tetracycline (hydrochloride) (drug)]] (+0.58, unclear, ⚠ only 6 significant genes); [[Entecavir (monohydrate) (drug)]] (+0.56, unclear); [[Trimetrexate (drug)]] (+0.53, DNA synthesis/repair inhibitor); [[Arbutin (drug)]] (+0.53, unclear); [[Silodosin (drug)]] (+0.50, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 33 arrows, 33 of them with an alert ⚠; grade A 0, B 24, C 9. Shown: the 15 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[IL15]] | 5 µM | B | IL15 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express IL15 (10) vs lines expressing it (38) | the lines without IL15: 0.81× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[CXCL3]] | 5 µM | B | CXCL3 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 0.82× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[ENSG00000253227]] | 5 µM | B | ENSG00000253227 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ENSG00000253227 (18) vs lines expressing it (30) | the lines without ENSG00000253227: 0.87× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: COL16A1, SERPINE2, SLCO2B1; maybe low, not absent |
| [[LINC02257]] | 5 µM | B | LINC02257 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express LINC02257 (15) vs lines expressing it (33) | the lines without LINC02257: 0.89× the cells of the other lines | 0.067 | ⚠ within organs, on part of the lines; also absent: CTSS, PAG1, ZNF365; maybe low, not absent |
| [[LINC02057]] | 5 µM | B | LINC02057 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.89× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[CRYBG1]] | 5 µM | B | CRYBG1 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express CRYBG1 (18) vs lines expressing it (30) | the lines without CRYBG1: 0.85× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: TSPOAP1, MPZL3, LNX1 |
| [[IFIT2]] | 5 µM | B | IFIT2 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express IFIT2 (8) vs lines expressing it (40) | the lines without IFIT2: 0.85× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[GBP2]] | 5 µM | B | GBP2 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express GBP2 (13) vs lines expressing it (35) | the lines without GBP2: 0.85× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.86× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[SPTLC3]] | 5 µM | B | SPTLC3 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express SPTLC3 (16) vs lines expressing it (32) | the lines without SPTLC3: 0.85× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, CXCL3, PTPRB; maybe low, not absent |
| [[NMRAL2P-1]] | 5 µM | B | NMRAL2P-1 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express NMRAL2P-1 (18) vs lines expressing it (30) | the lines without NMRAL2P-1: 0.86× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[MAML2]] | 5 µM | B | MAML2 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express MAML2 (8) vs lines expressing it (40) | the lines without MAML2: 0.84× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: TNS3, SMOX, ALDH3B1 |
| [[PCED1B]] | 5 µM | B | PCED1B activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express PCED1B (11) vs lines expressing it (37) | the lines without PCED1B: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |
| [[GBP3]] | 5 µM | B | GBP3 activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express GBP3 (11) vs lines expressing it (37) | the lines without GBP3: 0.80× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: PHLDA2, CD44, ITGA3 |
| [[CSMD3]] | 5 µM | B | CSMD3 activity lowers the cells' numbers under Tolcapone 5 µM (makes them more sensitive) | lines that do not express CSMD3 (36) vs lines expressing it (12) | the lines without CSMD3: 1.15× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Tolcapone"
- `tables/drugdoses.parquet` — dd in 1018, 1019, 1020
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
