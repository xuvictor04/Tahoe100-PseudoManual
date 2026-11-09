---
drug: "Encorafenib"
type: "drug"
salt_base: "Encorafenib"
targets: "BRAF"
moa_fine: "RAF inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "5"]
best_dose: "5"
max_sig_genes: 120
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Encorafenib

*RAF inhibitor (inhibitor/antagonist) · targets: BRAF · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 5 µM): 1 / 120; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.19.
> Flags by dose: - / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C8 | 1 / 0 | — | +0.38 | -0.2/-0.2/+0.5 | — |
| 5 µM | [[Plate 03]]:C8 | 62 / 58 | — | +1.74 | -0.3/-1.2/-2.2 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CORO2B]] 1.43× (z +3.5, 7/34 lines)

**5 µM** (62 genes, none with an alert; 12 shown): [[WARS1]] 1.95× (z +5.7, 32/47 lines), [[ASNS]] 2.10× (z +5.0, 30/44 lines), [[PSAT1]] 2.21× (z +4.9, 18/40 lines), [[AARS1]] 1.84× (z +4.8, 28/48 lines), [[SLC7A1]] 1.44× (z +4.7, 21/47 lines), [[CARS1]] 1.53× (z +4.6, 27/48 lines), [[PCK2]] 1.88× (z +4.6, 10/47 lines), [[NCOA7]] 1.61× (z +4.5, 29/48 lines), [[YARS1]] 1.53× (z +4.5, 24/48 lines), [[APOL6]] 1.64× (z +4.4, 19/42 lines), [[SLC7A11]] 1.95× (z +4.3, 28/42 lines), [[NIBAN1]] 1.63× (z +4.2, 18/37 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (58 genes, none with an alert; 12 shown): [[GJA1]] 0.560× (z -4.0, 3/22 lines), [[TFPI2]] 0.393× (z -3.9, 15/26 lines), [[DHRS9]] 0.342× (z -3.8, 4/8 lines), [[STC1]] 0.461× (z -3.7, 15/24 lines), [[KLK6]] 0.421× (z -3.7, 2/14 lines), [[LINC00540]] 0.572× (z -3.7, 0/15 lines), [[INHBA]] 0.442× (z -3.7, 6/16 lines), [[BCL2A1]] 0.382× (z -3.7, 11/21 lines), [[AKAP12]] 0.528× (z -3.6, 17/30 lines), [[UTY]] 0.667× (z -3.6, 0/17 lines), [[SLC25A24P1]] 0.392× (z -3.6, 0/7 lines), [[MARCHF4]] 0.572× (z -3.5, 4/20 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 5 µM | [[Module 194]] (+2.4), [[Module 230]] (+2.3) | [[Module 048]] (-2.4) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 5 µM | [[SK-MEL-2 (line)]] (-5.2), [[LOX-IMVI (line)]] (-4.1), [[NCI-H2347 (line)]] (-3.2), [[NCI-H1792 (line)]] (-3.2) | [[NCI-H23 (line)]] (1.35), [[AN3 CA (line)]] (1.31), [[SK-MEL-2 (line)]] (1.29), [[SNU-1 (line)]] (1.28) · weakest: [[SNU-423 (line)]] (0.723), [[SHP-77 (line)]] (0.735), [[A549 (line)]] (0.740) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Paclitaxel (drug)]] (+0.76, Microtubule inhibitor, ⚠ only 3 significant genes); [[Fenofibrate (drug)]] (+0.75, unclear); [[Erlotinib (drug)]] (+0.74, EGFR/ERBB inhibitor); [[Benproperine (phosphate) (drug)]] (+0.72, unclear); [[Anethole trithione (drug)]] (+0.72, unclear); [[MK-8353 (drug)]] (+0.69, Other MAPK inhibitor); [[Lucanthone (drug)]] (+0.68, unclear); [[Rutin (trihydrate) (drug)]] (+0.67, unclear); [[Tucatinib (drug)]] (+0.59, EGFR/ERBB inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[BMPER]] | 5 µM | B | BMPER activity raises the cells' numbers under Encorafenib 5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.81× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[VAV3]] | 5 µM | B | VAV3 activity raises the cells' numbers under Encorafenib 5 µM (protects the cells) | lines that do not express VAV3 (30) vs lines expressing it (18) | the lines without VAV3: 0.84× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RSPO3, ENSG00000289418, NRCAM |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Encorafenib"
- `tables/drugdoses.parquet` — dd in 407, 408
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
