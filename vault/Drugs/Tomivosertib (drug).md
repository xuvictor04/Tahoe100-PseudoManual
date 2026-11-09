---
drug: "Tomivosertib"
type: "drug"
salt_base: "Tomivosertib"
targets: ""
moa_fine: "Protein synthesis inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 212
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Tomivosertib

*Protein synthesis inhibitor (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 7 / 0 / 212; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.39 / -0.05.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C4 | 6 / 1 | — | +0.04 | +0.9/+0.4/+0.8 | — |
| 0.5 µM | [[Plate 02]]:C4 | 0 / 0 | — | +0.14 | +0.7/+0.9/+0.6 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C4 | 195 / 17 | — | +0.54 | -0.8/-0.1/-0.2 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[PXN-AS1]] 2.18× (z +8.0, 30/43 lines), [[BCL7B]] 1.21× (z +3.8, 10/48 lines), [[PLBD2]] 1.22× (z +3.6, 10/48 lines), [[ZNF574]] 1.37× (z +3.5, 5/45 lines), [[PTBP1]] 1.21× (z +3.0, 17/48 lines), [[DUS3L]] 1.25× (z +2.9, 4/45 lines)

**5 µM** (195 genes, none with an alert; 12 shown): [[IARS1]] 1.71× (z +4.4, 32/48 lines), [[TCEA1]] 1.51× (z +4.1, 27/48 lines), [[GPCPD1]] 1.85× (z +4.0, 30/48 lines), [[FBXO42]] 1.64× (z +4.0, 32/48 lines), [[ENSG00000274322]] 1.79× (z +4.0, 15/48 lines), [[XPO1]] 1.46× (z +3.9, 38/48 lines), [[RAB3GAP1]] 1.42× (z +3.9, 34/48 lines), [[LRRC49]] 1.44× (z +3.8, 13/37 lines), [[NIBAN1]] 1.57× (z +3.8, 13/37 lines), [[LUC7L]] 1.51× (z +3.8, 25/48 lines), [[TPD52]] 1.41× (z +3.8, 28/46 lines), [[TRIM33]] 1.38× (z +3.8, 21/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ZNF250]] 0.808× (z -3.2, 6/46 lines)

**5 µM** (17 genes, none with an alert; 12 shown): [[MT-ND2]] 0.456× (z -3.4, 42/48 lines), [[CYP1B1-AS1]] 0.496× (z -3.3, 7/28 lines), [[C1QTNF3-AMACR]] 0.606× (z -3.1, 11/48 lines), [[TGFB2]] 0.698× (z -3.1, 4/33 lines), [[MPV17]] 0.765× (z -3.1, 2/48 lines), [[MSH2]] 0.788× (z -3.1, 8/48 lines), [[NR5A2]] 0.607× (z -3.1, 3/14 lines), [[NIPAL2]] 0.629× (z -3.1, 8/37 lines), [[NCKAP5]] 0.669× (z -3.1, 3/26 lines), [[LINC01091]] 0.585× (z -3.0, 3/29 lines), [[PLA2G4A]] 0.725× (z -3.0, 2/26 lines), [[IRS1]] 0.644× (z -2.9, 9/42 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 204]] (+2.3), [[Module 233]] (+2.2), [[Module 234]] (+2.2) | [[Module 010]] (-2.2), [[Module 016]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[BT-474 (line)]] (-5.8), [[AsPC-1 (line)]] (-3.0) | [[MIA PaCa-2 (line)]] (1.49), [[NCI-H2030 (line)]] (1.39), [[NCI-H1573 (line)]] (1.39), [[LS 180 (line)]] (1.36) · weakest: [[AN3 CA (line)]] (0.693), [[SHP-77 (line)]] (0.772), [[A-427 (line)]] (0.773) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Goserelin (acetate) (drug)]] (+0.73, unclear); [[Pravastatin (sodium) (drug)]] (+0.72, unclear); [[Capivasertib (drug)]] (+0.72, PI3K/AKT inhibitor, ⚠ only 5 significant genes); [[Ranolazine (drug)]] (+0.66, unclear); [[Entecavir (monohydrate) (drug)]] (+0.64, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.58, unclear); [[Captopril (drug)]] (+0.56, unclear); [[Fumaric acid (drug)]] (+0.56, unclear); [[Cloxacillin (sodium) (drug)]] (+0.56, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[IGF2BP2]] | 5 µM | C | IGF2BP2 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express IGF2BP2 (3) vs lines expressing it (45) | the lines without IGF2BP2: 0.66× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| [[FCHSD1]] | 5 µM | C | FCHSD1 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express FCHSD1 (3) vs lines expressing it (45) | the lines without FCHSD1: 0.68× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: PLS3, CDK6, SH2B3 |
| [[IFT74]] | 5 µM | C | IFT74 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express IFT74 (3) vs lines expressing it (45) | the lines without IFT74: 0.69× the cells of the other lines | 0.007 | ⚠ few lines (3 vs 47); across organs; also absent: LCA5, P3H4, TOMM40L; maybe low, not absent |
| [[IGF2BP3]] | 5 µM | C | IGF2BP3 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express IGF2BP3 (4) vs lines expressing it (44) | the lines without IGF2BP3: 0.74× the cells of the other lines | 0.030 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: CDK6, RGL1, UACA |
| [[TCEAL9]] | 5 µM | C | TCEAL9 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express TCEAL9 (4) vs lines expressing it (44) | the lines without TCEAL9: 0.80× the cells of the other lines | 0.040 | ⚠ few lines (4 vs 46); tissue-confounded; across organs |
| [[SLC22A4]] | 5 µM | C | SLC22A4 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express SLC22A4 (5) vs lines expressing it (43) | the lines without SLC22A4: 0.79× the cells of the other lines | 0.040 | ⚠ tissue-confounded; across organs; also absent: TGFB1, ITGA7, CAVIN1; maybe low, not absent |
| [[PCOLCE]] | 5 µM | C | PCOLCE activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express PCOLCE (7) vs lines expressing it (41) | the lines without PCOLCE: 0.80× the cells of the other lines | 0.059 | ⚠ tissue-confounded; across organs; also absent: SLC25A43; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Tomivosertib"
- `tables/drugdoses.parquet` — dd in 1024, 1025, 1026
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
