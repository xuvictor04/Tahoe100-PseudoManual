---
drug: "Volasertib"
type: "drug"
salt_base: "Volasertib"
targets: "PLK1, PLK2, PLK3"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 54
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Volasertib

*unclear (inhibitor/antagonist) · targets: PLK1, PLK2, PLK3 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 54 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.11 / -0.15.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:B2 | 0 / 0 | — | +0.07 | +0.8/+0.5/-0.4 | — |
| 0.5 µM | [[Plate 02]]:B2 | 22 / 32 | — | -0.07 | +0.5/-1.0/-0.9 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:B2 | 0 / 0 | — | -0.59 | +0.6/+0.5/+0.0 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (22 genes, none with an alert; 12 shown): [[SNX5]] 1.25× (z +3.8, 11/48 lines), [[LRPPRC]] 1.35× (z +3.6, 29/48 lines), [[SECISBP2]] 1.32× (z +3.4, 16/48 lines), [[URB1]] 1.33× (z +3.4, 11/48 lines), [[C19orf48]] 1.30× (z +3.4, 3/48 lines), [[NSUN2]] 1.36× (z +3.3, 20/48 lines), [[XPO5]] 1.24× (z +3.3, 4/48 lines), [[ZNF34]] 1.45× (z +3.2, 1/47 lines), [[MAPRE1]] 1.29× (z +3.2, 13/48 lines), [[RBM19]] 1.28× (z +3.0, 8/48 lines), [[C3orf52]] 1.45× (z +3.0, 7/42 lines), [[ETF1]] 1.24× (z +2.9, 13/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (32 genes, none with an alert; 12 shown): [[UBALD2]] 0.536× (z -4.6, 29/48 lines), [[ING4]] 0.730× (z -4.2, 11/48 lines), [[CCDC28A]] 0.728× (z -3.9, 8/48 lines), [[GCC2]] 0.779× (z -3.7, 30/48 lines), [[ACOT8]] 0.723× (z -3.6, 6/48 lines), [[NBR1]] 0.752× (z -3.4, 26/48 lines), [[FBXO32]] 0.721× (z -3.4, 12/34 lines), [[MXD4]] 0.668× (z -3.3, 11/48 lines), [[CRIPT]] 0.787× (z -3.3, 11/48 lines), [[KLHDC2]] 0.793× (z -3.3, 3/48 lines), [[ATXN3]] 0.799× (z -3.3, 16/48 lines), [[UBALD1]] 0.736× (z -3.2, 3/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 020]] (+2.0) | [[Module 059]] (-2.0) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[LOX-IMVI (line)]] (-3.4) | [[AN3 CA (line)]] (1.35), [[MIA PaCa-2 (line)]] (1.32), [[NCI-H23 (line)]] (1.25), [[SNU-1 (line)]] (1.21) · weakest: [[SK-MEL-2 (line)]] (0.653), [[HCT15 (line)]] (0.689), [[A498 (line)]] (0.702) |
| 5 µM | [[PANC-1 (line)]] (-3.9), [[NCI-H1573 (line)]] (-3.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[MK-8353 (drug)]] (+0.70, Other MAPK inhibitor); [[Pentagastrin (drug)]] (+0.67, unclear, ⚠ only 9 significant genes); [[Folic acid (drug)]] (+0.67, unclear); [[Balsalazide (sodium hydrate) (drug)]] (+0.66, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[c-Kit-IN-1 (drug)]] (+0.65, Multi-TK inhibitor); [[Abemaciclib (drug)]] (+0.64, CDK inhibitor); [[Tucatinib (drug)]] (+0.62, EGFR/ERBB inhibitor); [[Clonidine (hydrochloride) (drug)]] (+0.62, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Fenofibrate (drug)]] (+0.61, unclear); [[TAK-733 (drug)]] (+0.61, MEK inhibitor); [[Benproperine (phosphate) (drug)]] (+0.60, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[FHAD1]] | 5 µM | B | FHAD1 activity raises the cells' numbers under Volasertib 5 µM (protects the cells) | lines that do not express FHAD1 (14) vs lines expressing it (34) | the lines without FHAD1: 0.91× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: LINC01798, LINC01426; maybe low, not absent |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Volasertib 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.21× the cells of the other lines | 0.049 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ENSG00000286964]] | 0.5 µM | C | ENSG00000286964 activity lowers the cells' numbers under Volasertib 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 1.23× the cells of the other lines | 0.068 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |
| [[ENSG00000285458]] | 5 µM | C | ENSG00000285458 activity lowers the cells' numbers under Volasertib 5 µM (makes them more sensitive) | lines that do not express ENSG00000285458 (5) vs lines expressing it (43) | the lines without ENSG00000285458: 1.39× the cells of the other lines | 0.083 | ⚠ tissue-confounded; across organs; also absent: TBILA, GCA, RILP; maybe low, not absent |
| [[SDC3]] | 5 µM | C | SDC3 activity lowers the cells' numbers under Volasertib 5 µM (makes them more sensitive) | lines that do not express SDC3 (4) vs lines expressing it (44) | the lines without SDC3: 1.44× the cells of the other lines | 0.087 | ⚠ few lines (4 vs 46); across organs |
| [[PTS]] | 0.5 µM | C | PTS's natural level raises the cells' numbers under Volasertib 0.5 µM (protects the cells) | PTS's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.291 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000287555]] | 0.5 µM | C | ENSG00000287555's natural level raises the cells' numbers under Volasertib 0.5 µM (protects the cells) | ENSG00000287555's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[BCO2]] | 0.5 µM | C | BCO2's natural level raises the cells' numbers under Volasertib 0.5 µM (protects the cells) | BCO2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ENSG00000240571]] | 0.5 µM | C | ENSG00000240571's natural level raises the cells' numbers under Volasertib 0.5 µM (protects the cells) | ENSG00000240571's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[TICAM2-AS1]] | 0.5 µM | C | TICAM2-AS1's natural level raises the cells' numbers under Volasertib 0.5 µM (protects the cells) | TICAM2-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.091 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Volasertib"
- `tables/drugdoses.parquet` — dd in 1096, 1097, 1098
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
