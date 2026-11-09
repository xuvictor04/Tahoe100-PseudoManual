---
drug: "Oxaliplatin"
type: "drug"
salt_base: "Oxaliplatin"
targets: ""
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 7
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Oxaliplatin

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 7 / 6; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.15 / -0.35.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:A9 | 4 / 1 | — | +0.20 | -0.1/-0.6/-0.1 | — |
| 0.5 µM | [[Plate 02]]:A9 | 6 / 1 | — | +0.74 | +2.6/+0.1/-0.5 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:A9 | 5 / 1 | — | +0.28 | +1.4/+1.2/+0.6 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[ARGLU1]] 1.24× (z +3.7, 24/48 lines), [[ENSG00000254929]] 1.27× (z +3.6, 8/46 lines), [[LSM12]] 1.36× (z +3.5, 19/48 lines), [[ZNF707]] 1.24× (z +2.9, 2/48 lines)

**0.5 µM** (6 genes, none with an alert): [[DIAPH3]] 1.23× (z +3.1, 9/45 lines), [[DTL]] 1.36× (z +3.1, 9/48 lines), [[POLA2]] 1.27× (z +3.1, 3/48 lines), [[CDC45]] 1.38× (z +2.9, 3/45 lines), [[MCM8]] 1.26× (z +2.7, 5/48 lines), [[FANCA]] 1.29× (z +2.7, 5/48 lines)

**5 µM** (5 genes, none with an alert): [[NONO]] 1.40× (z +3.8, 26/48 lines), [[STK11]] 1.41× (z +3.7, 1/44 lines), [[GOLIM4]] 1.27× (z +3.2, 10/48 lines), [[CLTB]] 1.52× (z +3.1, 10/47 lines), [[NOLC1]] 1.47× (z +2.6, 17/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[GCNT1]] 0.622× (z -8.2, 25/43 lines)

**0.5 µM** (1 gene, none with an alert): [[TNIP1]] 0.833× (z -2.9, 8/48 lines)

**5 µM** (1 gene, none with an alert): [[GCNT1]] 0.528× (z -6.1, 23/42 lines)

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

⚠ This drug's own vector: only 7 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Temuterkib (drug)]] (+0.77, Other MAPK inhibitor, ⚠ only 3 significant genes); [[Balsalazide (sodium hydrate) (drug)]] (+0.76, JAK/STAT inhibitor, ⚠ only 9 significant genes); [[Fenofibrate (drug)]] (+0.73, unclear); [[MK-8353 (drug)]] (+0.70, Other MAPK inhibitor); [[Rutin (trihydrate) (drug)]] (+0.69, unclear); [[Pyridoxine (hydrochloride) (drug)]] (+0.66, unclear); [[Dabrafenib (drug)]] (+0.66, RAF inhibitor); [[Olanzapine (drug)]] (+0.66, unclear, ⚠ only 5 significant genes); [[Erlotinib (drug)]] (+0.60, EGFR/ERBB inhibitor); [[Lucanthone (drug)]] (+0.59, unclear); [[Fusidic acid (drug)]] (+0.58, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[RASGEF1B]] | 0.05 µM | B | RASGEF1B activity lowers the cells' numbers under Oxaliplatin 0.05 µM (makes them more sensitive) | lines that do not express RASGEF1B (10) vs lines expressing it (38) | the lines without RASGEF1B: 1.23× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: FBXW10B; maybe low, not absent |
| [[TREM1]] | 0.05 µM | B | TREM1 activity lowers the cells' numbers under Oxaliplatin 0.05 µM (makes them more sensitive) | lines that do not express TREM1 (25) vs lines expressing it (23) | the lines without TREM1: 1.07× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: EDIL3-DT, DTNA, MAF |
| [[SEMA4G]] | 0.05 µM | C | SEMA4G activity lowers the cells' numbers under Oxaliplatin 0.05 µM (makes them more sensitive) | lines that do not express SEMA4G (6) vs lines expressing it (42) | the lines without SEMA4G: 1.26× the cells of the other lines | 0.045 | ⚠ tissue-confounded; across organs; also absent: SLC2A9, HMGA2; maybe low, not absent |
| [[ENSG00000288755]] | 0.05 µM | C | ENSG00000288755 activity lowers the cells' numbers under Oxaliplatin 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000288755 (3) vs lines expressing it (45) | the lines without ENSG00000288755: 1.38× the cells of the other lines | 0.051 | ⚠ few lines (3 vs 47); across organs; also absent: SLC25A45; maybe low, not absent |
| [[C2orf74]] | 0.05 µM | C | C2orf74 activity raises the cells' numbers under Oxaliplatin 0.05 µM (protects the cells) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 0.84× the cells of the other lines | 0.063 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ENSG00000286964]] | 0.05 µM | C | ENSG00000286964 activity raises the cells' numbers under Oxaliplatin 0.05 µM (protects the cells) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 0.84× the cells of the other lines | 0.091 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Oxaliplatin"
- `tables/drugdoses.parquet` — dd in 756, 757, 758
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
