---
drug: "Tucatinib"
type: "drug"
salt_base: "Tucatinib"
targets: "ERBB2"
moa_fine: "EGFR/ERBB inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 10
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tucatinib

*EGFR/ERBB inhibitor (inhibitor/antagonist) · targets: ERBB2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 10 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.11 / 0.36.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B8 | 1 / 0 | — | +0.20 | -0.2/-0.1/+0.4 | — |
| 0.5 µM | [[Plate 02]]:B8 | 0 / 10 | — | +0.17 | -0.5/-0.1/-0.8 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B8 | 0 / 0 | — | +1.18 | +1.2/+0.9/-0.1 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[HSPA1B]] 1.39× (z +2.8, 6/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (10 genes, none with an alert): [[UTY]] 0.633× (z -4.5, 0/17 lines), [[USP9Y]] 0.737× (z -3.6, 0/18 lines), [[SNCA]] 0.711× (z -3.6, 0/19 lines), [[TMEM45B]] 0.656× (z -3.4, 0/16 lines), [[ENSG00000267284]] 0.697× (z -3.3, 0/16 lines), [[PRKY]] 0.719× (z -3.3, 0/18 lines), [[NR5A2]] 0.682× (z -3.2, 0/15 lines), [[ENSG00000227088]] 0.706× (z -3.0, 0/15 lines), [[SYK]] 0.741× (z -2.9, 0/18 lines), [[ESRP1]] 0.687× (z -2.8, 0/17 lines)

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
| 0.5 µM | [[NCI-H661 (line)]] (-3.1), [[A-427 (line)]] (-3.1) | — |
| 5 µM | [[BT-474 (line)]] (-3.6), [[SHP-77 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Lucanthone (drug)]] (+0.87, unclear); [[Lapatinib ditosylate (drug)]] (+0.81, EGFR/ERBB inhibitor, ⚠ only 9 significant genes); [[Benproperine (phosphate) (drug)]] (+0.81, unclear); [[Fenofibrate (drug)]] (+0.79, unclear); [[Erlotinib (drug)]] (+0.79, EGFR/ERBB inhibitor); [[Rutin (trihydrate) (drug)]] (+0.79, unclear); [[MK-8353 (drug)]] (+0.78, Other MAPK inhibitor); [[Anethole trithione (drug)]] (+0.78, unclear); [[Fusidic acid (drug)]] (+0.67, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 27 arrows, 27 of them with an alert ⚠; grade A 0, B 17, C 10. Shown: the 15 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[NAV3]] | 5 µM | B | NAV3 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express NAV3 (16) vs lines expressing it (32) | the lines without NAV3: 0.82× the cells of the other lines | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, PRR16, ADAM12 |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.86× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ENSG00000275119]] | 5 µM | B | ENSG00000275119 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express ENSG00000275119 (10) vs lines expressing it (38) | the lines without ENSG00000275119: 0.85× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01252; maybe low, not absent |
| [[SIRLNT]] | 5 µM | B | SIRLNT activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.82× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[IL7R]] | 5 µM | B | IL7R activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express IL7R (30) vs lines expressing it (18) | the lines without IL7R: 0.83× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1 |
| [[PLA2G4A]] | 5 µM | B | PLA2G4A activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express PLA2G4A (22) vs lines expressing it (26) | the lines without PLA2G4A: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: PTGS2, ITGA4, EPB41L3 |
| [[HTRA1]] | 5 µM | B | HTRA1 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express HTRA1 (19) vs lines expressing it (29) | the lines without HTRA1: 0.81× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[ALDH3B1]] | 5 µM | B | ALDH3B1 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.76× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[HMGA2]] | 5 µM | B | HMGA2 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express HMGA2 (9) vs lines expressing it (39) | the lines without HMGA2: 0.85× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |
| [[IL6]] | 5 µM | B | IL6 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express IL6 (32) vs lines expressing it (16) | the lines without IL6: 0.84× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[GPR39]] | 5 µM | B | GPR39 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express GPR39 (11) vs lines expressing it (37) | the lines without GPR39: 0.83× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: MET, AHR, ABCC3 |
| [[PHLDA2]] | 5 µM | B | PHLDA2 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express PHLDA2 (7) vs lines expressing it (41) | the lines without PHLDA2: 0.73× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: MET, TGFBR2, SDC4; maybe low, not absent |
| [[GJA1]] | 5 µM | B | GJA1 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.87× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[ZNF469]] | 5 µM | B | ZNF469 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express ZNF469 (20) vs lines expressing it (28) | the lines without ZNF469: 0.81× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02057, IL6, TMEM158 |
| [[CXCL3]] | 5 µM | B | CXCL3 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express CXCL3 (14) vs lines expressing it (34) | the lines without CXCL3: 0.81× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Tucatinib"
- `tables/drugdoses.parquet` — dd in 1057, 1058, 1059
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
