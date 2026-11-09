---
drug: "Pioglitazone"
type: "drug"
salt_base: "Pioglitazone"
targets: "PPARG"
moa_fine: "unclear"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 16
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Pioglitazone

*unclear (activator/agonist) · targets: PPARG · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 2 / 16 / 7; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.10 / 0.07.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E7 | 2 / 0 | — | -0.00 | -0.4/-0.1/-0.1 | — |
| 0.5 µM | [[Plate 11]]:E7 | 16 / 0 | — | -0.61 | -0.4/+0.1/+0.3 | — |
| 5 µM | [[Plate 12]]:E7 | 7 / 0 | — | +0.43 | +0.3/+1.0/+0.8 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[SLCO5A1]] 1.56× (z +6.5, 15/41 lines), [[RYR2]] 1.33× (z +2.8, 2/47 lines)

**0.5 µM** (16 genes, none with an alert; 12 shown): [[PRSS12]] 1.30× (z +4.7, 8/27 lines), [[STON2]] 1.32× (z +4.1, 9/28 lines), [[ENSG00000290957]] 1.38× (z +4.0, 7/27 lines), [[CYP4F12]] 1.60× (z +3.7, 5/15 lines), [[PDK4]] 1.47× (z +3.5, 12/23 lines), [[LPCAT3]] 1.22× (z +3.5, 13/47 lines), [[SYT9]] 1.44× (z +3.5, 0/12 lines), [[ITGA8]] 1.57× (z +3.2, 0/7 lines), [[HAGLR]] 1.35× (z +3.2, 1/23 lines), [[ACSL5]] 1.21× (z +3.1, 7/23 lines), [[ENSG00000287306]] 1.30× (z +3.1, 3/30 lines), [[MCF2]] 1.37× (z +3.0, 4/36 lines)

**5 µM** (7 genes, none with an alert): [[LPCAT3]] 1.27× (z +4.5, 14/48 lines), [[PLIN2]] 1.60× (z +4.1, 22/31 lines), [[ACSL5]] 1.27× (z +3.9, 13/24 lines), [[PDK4]] 1.51× (z +3.7, 13/23 lines), [[PIM1]] 1.38× (z +3.3, 16/44 lines), [[CAT]] 1.23× (z +3.2, 12/47 lines), [[STON2]] 1.21× (z +2.9, 7/28 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

No gene is significantly lowered at any dose.

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

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Rosiglitazone (drug)]] (+0.67, unclear); [[Pimozide (drug)]] (+0.63, unclear); [[Valdecoxib (drug)]] (+0.61, Cyclooxygenase inhibitor); [[Hydroxyfasudil (drug)]] (+0.57, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.56, unclear); [[Simotinib (drug)]] (+0.56, EGFR/ERBB inhibitor, ⚠ vector dose flagged: toxic); [[AZD2858 (drug)]] (+0.54, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Vitamin K4 (drug)]] (+0.53, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.50, Glucose transporter inhibitor); [[Saquinavir (drug)]] (+0.50, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Pioglitazone 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.24× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[RSPO3]] | 0.5 µM | B | RSPO3 activity lowers the cells' numbers under Pioglitazone 0.5 µM (makes them more sensitive) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 1.27× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity lowers the cells' numbers under Pioglitazone 0.5 µM (makes them more sensitive) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 1.25× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[TBILA]] | 0.5 µM | C | TBILA activity lowers the cells' numbers under Pioglitazone 0.5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.32× the cells of the other lines | 0.027 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[ISG20]] | 0.5 µM | C | ISG20 activity lowers the cells' numbers under Pioglitazone 0.5 µM (makes them more sensitive) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 1.33× the cells of the other lines | 0.033 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| [[PWWP2B]] | 0.5 µM | C | PWWP2B activity raises the cells' numbers under Pioglitazone 0.5 µM (protects the cells) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 0.74× the cells of the other lines | 0.084 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Pioglitazone"
- `tables/drugdoses.parquet` — dd in 818, 819, 820
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
