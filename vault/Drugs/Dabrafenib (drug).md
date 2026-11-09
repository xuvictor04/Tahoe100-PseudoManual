---
drug: "Dabrafenib"
type: "drug"
salt_base: "Dabrafenib"
targets: "BRAF, RAF1"
moa_fine: "RAF inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 34
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Dabrafenib

*RAF inhibitor (inhibitor/antagonist) · targets: BRAF, RAF1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 0 / 34; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.14.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C7 | 2 / 1 | — | +0.10 | -1.1/-0.9/-0.3 | — |
| 0.5 µM | [[Plate 02]]:C7 | 0 / 0 | — | -0.24 | +0.4/+0.4/+0.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C7 | 21 / 13 | — | +1.84 | -1.8/-2.2/-1.7 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[WNT9A]] 1.31× (z +3.4, 5/37 lines), [[CORO2B]] 1.38× (z +3.1, 7/34 lines)

**5 µM** (21 genes, none with an alert; 12 shown): [[SHANK2]] 1.61× (z +4.2, 18/34 lines), [[SLC7A1]] 1.36× (z +3.9, 13/48 lines), [[ARHGEF4]] 1.60× (z +3.8, 12/34 lines), [[SIPA1L1]] 1.48× (z +3.6, 29/47 lines), [[ARHGEF2]] 1.59× (z +3.6, 22/48 lines), [[PSAT1]] 1.79× (z +3.6, 13/40 lines), [[SLC38A1]] 1.38× (z +3.5, 20/46 lines), [[NIBAN1]] 1.48× (z +3.4, 12/38 lines), [[AFF3]] 1.51× (z +3.2, 9/27 lines), [[WARS1]] 1.46× (z +3.2, 10/48 lines), [[CARS1]] 1.34× (z +3.2, 14/49 lines), [[IARS1]] 1.46× (z +3.1, 23/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[MUC17]] 0.613× (z -3.2, 0/4 lines)

**5 µM** (13 genes, none with an alert; 12 shown): [[ALOX5]] 0.563× (z -3.5, 1/20 lines), [[GBP2]] 0.539× (z -3.4, 4/36 lines), [[NGF]] 0.525× (z -3.3, 0/17 lines), [[ELF3]] 0.537× (z -3.3, 5/26 lines), [[GRHL2]] 0.664× (z -3.2, 0/15 lines), [[PDLIM1]] 0.703× (z -3.1, 4/38 lines), [[CCL28]] 0.648× (z -3.0, 1/24 lines), [[RNF128]] 0.702× (z -2.9, 0/25 lines), [[PTPRR]] 0.625× (z -2.9, 2/17 lines), [[IFIH1]] 0.663× (z -2.9, 8/46 lines), [[NCAPH]] 0.676× (z -2.8, 4/47 lines), [[ATP8B1]] 0.811× (z -2.8, 4/35 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 194]] (+2.1) | [[Module 059]] (-2.8), [[Module 045]] (-2.3), [[Module 048]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[LOX-IMVI (line)]] (-3.8), [[NCI-H2347 (line)]] (-3.7), [[CFPAC-1 (line)]] (-3.1) | [[SW 1271 (line)]] (1.52), [[SNU-1 (line)]] (1.48), [[SW 1088 (line)]] (1.39), [[hTERT-HPNE (line)]] (1.32) · weakest: [[COLO 205 (line)]] (0.357), [[NCI-H2122 (line)]] (0.367), [[C32 (line)]] (0.525) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Fenofibrate (drug)]] (+0.73, unclear); [[BAY1125976 (drug)]] (+0.69, PI3K/AKT inhibitor); [[Oxaliplatin (drug)]] (+0.66, DNA synthesis/repair inhibitor, ⚠ only 7 significant genes); [[Lucanthone (drug)]] (+0.64, unclear); [[Paclitaxel (drug)]] (+0.62, Microtubule inhibitor, ⚠ only 3 significant genes); [[Benproperine (phosphate) (drug)]] (+0.62, unclear); [[Erlotinib (drug)]] (+0.61, EGFR/ERBB inhibitor); [[Ivermectin (drug)]] (+0.61, unclear); [[Rutin (trihydrate) (drug)]] (+0.60, unclear); [[Dapagliflozin (drug)]] (+0.58, Glucose transporter inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[MTMR7]] | 5 µM | B | MTMR7 activity raises the cells' numbers under Dabrafenib 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.80× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[CYB561]] | 5 µM | C | CYB561 activity lowers the cells' numbers under Dabrafenib 5 µM (makes them more sensitive) | lines that do not express CYB561 (3) vs lines expressing it (45) | the lines without CYB561: 1.71× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); across organs; also absent: MATN1-AS1, E2F8, PBX4; maybe low, not absent |
| [[FZD6]] | 5 µM | C | FZD6 activity lowers the cells' numbers under Dabrafenib 5 µM (makes them more sensitive) | lines that do not express FZD6 (5) vs lines expressing it (43) | the lines without FZD6: 1.50× the cells of the other lines | 0.033 | ⚠ tissue-confounded; across organs; also absent: DOCK5, PMAIP1, ISG20 |
| [[HPS1]] | 5 µM | C | HPS1 activity lowers the cells' numbers under Dabrafenib 5 µM (makes them more sensitive) | lines that do not express HPS1 (3) vs lines expressing it (45) | the lines without HPS1: 1.68× the cells of the other lines | 0.044 | ⚠ few lines (3 vs 47); across organs; also absent: SH3D19, PWWP2B, APOBEC3B; maybe low, not absent |
| [[VRK2]] | 5 µM | C | VRK2 activity lowers the cells' numbers under Dabrafenib 5 µM (makes them more sensitive) | lines that do not express VRK2 (4) vs lines expressing it (44) | the lines without VRK2: 1.41× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: PTER, ZC3HAV1L, OSR2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Dabrafenib"
- `tables/drugdoses.parquet` — dd in 314, 315, 316
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
