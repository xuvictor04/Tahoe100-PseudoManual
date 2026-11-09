---
drug: "Quinidine (15% dihydroquinidine)"
type: "drug"
salt_base: "Quinidine"
targets: "KCNH2"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 18
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Quinidine (15% dihydroquinidine)

*unclear (inhibitor/antagonist) · targets: KCNH2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 18 / 1; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.42 / -0.18.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F3 | 0 / 3 | — | +0.53 | +0.5/+0.5/+0.4 | — |
| 0.5 µM | [[Plate 08]]:F3 | 2 / 16 | — | +0.20 | +0.6/+1.0/+1.4 | — |
| 5 µM | [[Plate 09]]:F3 | 0 / 1 | — | +0.02 | +0.2/-0.0/+0.2 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[CFAP210]] 1.68× (z +2.9, 9/46 lines), [[EIF4A3]] 1.24× (z +2.7, 11/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[ASNSP1]] 0.557× (z -3.5, 2/10 lines), [[ENSG00000255983]] 0.658× (z -3.2, 3/15 lines), [[FLJ12825]] 0.677× (z -3.0, 2/30 lines)

**0.5 µM** (16 genes, none with an alert; 12 shown): [[PSTK]] 0.827× (z -3.3, 2/46 lines), [[NOTCH3]] 0.793× (z -3.3, 4/34 lines), [[KBTBD11]] 0.765× (z -3.2, 4/34 lines), [[B3GALT9]] 0.688× (z -3.2, 4/43 lines), [[METTL25]] 0.805× (z -3.1, 4/48 lines), [[LINC02981]] 0.714× (z -3.1, 7/33 lines), [[LINC01119]] 0.747× (z -3.1, 7/40 lines), [[HELQ]] 0.810× (z -3.0, 6/48 lines), [[MATN1-AS1]] 0.756× (z -3.0, 2/40 lines), [[GGACT]] 0.652× (z -3.0, 3/45 lines), [[ANKRD6]] 0.809× (z -3.0, 7/31 lines), [[TECPR2]] 0.759× (z -3.0, 14/48 lines)

**5 µM** (1 gene, none with an alert): [[METTL25B]] 0.807× (z -3.3, 7/45 lines)

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

- [[Sacubitril_Valsartan (drug)]] (+0.75, unclear, ⚠ only 1 significant gene); [[Allopurinol (drug)]] (+0.74, unclear); [[Entecavir (monohydrate) (drug)]] (+0.69, unclear); [[Ranolazine (drug)]] (+0.69, unclear); [[Fumaric acid (drug)]] (+0.67, unclear); [[Tetracycline (hydrochloride) (drug)]] (+0.65, unclear, ⚠ only 6 significant genes); [[Cloxacillin (sodium) (drug)]] (+0.64, unclear); [[Piroxicam (drug)]] (+0.62, Cyclooxygenase inhibitor); [[Pravastatin (sodium) (drug)]] (+0.62, unclear); [[Tomivosertib (drug)]] (+0.58, Protein synthesis inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 21 arrows, 21 of them with an alert ⚠; grade A 0, B 10, C 11. Shown: the 15 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 0.5 µM | B | ENSG00000230647 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.85× the cells of the other lines | 0.052 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[ALDH3B1]] | 0.5 µM | B | ALDH3B1 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.80× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[IGSF9]] | 0.5 µM | B | IGSF9 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express IGSF9 (16) vs lines expressing it (32) | the lines without IGSF9: 0.83× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[PPP1R9A]] | 0.5 µM | B | PPP1R9A activity lowers the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (makes them more sensitive) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 1.19× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[LINC02057]] | 0.5 µM | B | LINC02057 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.85× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[ADAM12]] | 0.5 µM | B | ADAM12 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.84× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[SPOCK1]] | 0.5 µM | B | SPOCK1 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.85× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[SIRLNT]] | 0.5 µM | B | SIRLNT activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.83× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[ENSG00000259200]] | 0.5 µM | B | ENSG00000259200 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express ENSG00000259200 (18) vs lines expressing it (30) | the lines without ENSG00000259200: 0.88× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000203635, CSGALNACT1, ENSG00000232692; maybe low, not absent |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.83× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[PHF11]] | 0.5 µM | C | PHF11 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express PHF11 (3) vs lines expressing it (45) | the lines without PHF11: 0.68× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: NABP1, ANXA2, SDC4 |
| [[PSMB8]] | 0.5 µM | C | PSMB8 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.71× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[LRRCC1]], [[OXR1]] | 0.5 µM | C | LRRCC1, OXR1 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.74× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[CEBPD]], [[GCA]] | 0.5 µM | C | CEBPD, GCA activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.69× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[TBILA]] | 0.5 µM | C | TBILA activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.77× the cells of the other lines | 0.026 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Quinidine (15% dihydroquinidine)"
- `tables/drugdoses.parquet` — dd in 857, 858, 859
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
