---
drug: "Belumosudil (mesylate)"
type: "drug"
salt_base: "Belumosudil"
targets: "ROCK2, ROCK1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 67
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Belumosudil (mesylate)

*unclear (inhibitor/antagonist) · targets: ROCK2, ROCK1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 1 / 0 / 67; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.30 / 0.33.
> Flags by dose: - / noisy plate (z scaled) / noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:F3 | 0 / 1 | — | +0.05 | +0.0/-0.3/-0.3 | — |
| 0.5 µM | [[Plate 02]]:F3 | 0 / 0 | — | +0.02 | -0.2/+0.1/+0.2 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:F3 | 51 / 16 | — | -0.26 | -1.6/-1.7/+0.8 | noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (51 genes, none with an alert; 12 shown): [[NIBAN1]] 2.08× (z +6.3, 27/37 lines), [[WARS1]] 2.03× (z +6.0, 34/47 lines), [[ASNS]] 2.08× (z +4.9, 24/44 lines), [[TRIB3]] 1.94× (z +4.8, 20/43 lines), [[PCK2]] 1.93× (z +4.8, 17/43 lines), [[CEBPG]] 1.80× (z +4.6, 31/47 lines), [[CCPG1]] 1.46× (z +4.5, 27/48 lines), [[PSAT1]] 2.06× (z +4.5, 15/40 lines), [[SLC7A1]] 1.41× (z +4.4, 20/47 lines), [[MARS1]] 1.63× (z +4.3, 27/48 lines), [[XPOT]] 1.48× (z +4.2, 28/48 lines), [[YARS1]] 1.47× (z +4.1, 22/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[ENSG00000230021]] 0.783× (z -3.0, 11/48 lines)

**5 µM** (16 genes, none with an alert; 12 shown): [[SREBF2]] 0.658× (z -3.6, 28/48 lines), [[PNPLA3]] 0.657× (z -3.4, 8/43 lines), [[GAS2L3]] 0.694× (z -3.3, 11/48 lines), [[ANLN]] 0.652× (z -3.1, 21/46 lines), [[HROB]] 0.696× (z -3.1, 7/43 lines), [[KATNAL1]] 0.720× (z -3.0, 9/41 lines), [[INSIG1]] 0.565× (z -3.0, 17/47 lines), [[FADS2]] 0.719× (z -2.9, 6/47 lines), [[CEP152]] 0.809× (z -2.9, 7/48 lines), [[KIF11]] 0.691× (z -2.9, 18/48 lines), [[DEPDC1B]] 0.751× (z -2.9, 9/48 lines), [[CIT]] 0.719× (z -2.9, 15/47 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 133]] (+2.2), [[Module 063]] (+2.2) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[NCI-H1792 (line)]] (-3.5) | [[RPMI-7951 (line)]] (1.65), [[NCI-H1573 (line)]] (1.38), [[Panc 03.27 (line)]] (1.37), [[COLO 205 (line)]] (1.37) · weakest: [[PANC-1 (line)]] (0.123), [[AN3 CA (line)]] (0.384), [[NCI-H661 (line)]] (0.404) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Neratinib (maleate) (drug)]] (+0.65, EGFR/ERBB inhibitor, ⚠ vector dose flagged: cell-cycle shift); [[Bestatin (drug)]] (+0.56, unclear, ⚠ only 3 significant genes); [[5-Azacytidine (drug)]] (+0.53, DNA methyltransferase inhibitor); [[Chlorhexidine (diacetate) (drug)]] (+0.51, unclear); [[BI-78D3 (drug)]] (+0.44, Other MAPK inhibitor); [[Lipoic acid (drug)]] (+0.44, unclear, ⚠ only 6 significant genes); [[Bestatin (hydrochloride) (drug)]] (+0.44, unclear); [[Clotrimazole (drug)]] (+0.42, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.41, Glucose transporter inhibitor); [[Hydroxyurea (drug)]] (+0.40, DNA synthesis/repair inhibitor); [[Pralsetinib (drug)]] (+0.39, Other TK inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000256514]] | 5 µM | B | ENSG00000256514 activity lowers the cells' numbers under Belumosudil (mesylate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000256514 (9) vs lines expressing it (39) | the lines without ENSG00000256514: 1.26× the cells of the other lines | 0.043 | ⚠ within organs, on part of the lines; also absent: HTATIP2, CLCF1, SAT1; maybe low, not absent |
| [[ENSG00000284716]] | 5 µM | C | ENSG00000284716 activity lowers the cells' numbers under Belumosudil (mesylate) 5 µM (makes them more sensitive) | lines that do not express ENSG00000284716 (5) vs lines expressing it (43) | the lines without ENSG00000284716: 1.23× the cells of the other lines | 0.085 | ⚠ tissue-confounded; across organs; also absent: FTH1, TMEM184A, ZFP36; maybe low, not absent |
| [[FAM111A]] | 5 µM | C | FAM111A activity lowers the cells' numbers under Belumosudil (mesylate) 5 µM (makes them more sensitive) | lines that do not express FAM111A (3) vs lines expressing it (45) | the lines without FAM111A: 1.35× the cells of the other lines | 0.093 | ⚠ few lines (3 vs 47); across organs; also absent: FXYD5, ACCS, TFAP2A; maybe low, not absent |
| [[TRAF3IP2]] | 5 µM | C | TRAF3IP2 activity lowers the cells' numbers under Belumosudil (mesylate) 5 µM (makes them more sensitive) | lines that do not express TRAF3IP2 (3) vs lines expressing it (45) | the lines without TRAF3IP2: 1.35× the cells of the other lines | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: ARMCX3, SFXN3, HBEGF |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Belumosudil (mesylate)"
- `tables/drugdoses.parquet` — dd in 150, 151, 152
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
