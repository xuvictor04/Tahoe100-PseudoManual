---
drug: "Salicylic acid"
type: "drug"
salt_base: "Salicylic acid"
targets: ""
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 3
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Salicylic acid

*Cyclooxygenase inhibitor (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 1 / 3; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.09 / 0.12.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C1 | 0 / 0 | — | +0.20 | -0.3/+0.2/+0.1 | — |
| 0.5 µM | [[Plate 05]]:C1 | 0 / 1 | — | +0.56 | +0.5/+0.1/-0.3 | — |
| 5 µM | [[Plate 14]]:C1 | 1 / 2 | 0.704 | -0.39 | -0.2/-0.4/+0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**5 µM** (1 gene, none with an alert): [[UGT2B7]] 1.40× (z +3.5, 0/10 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[TPRG1L]] 0.766× (z -3.3, 13/47 lines)

**5 µM** (2 genes, none with an alert): [[ENSG00000260911]] 0.794× (z -3.4, 8/47 lines), [[ADAMTS12]] 0.828× (z -3.1, 1/16 lines)

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
| 5 µM | [[NCI-H1792 (line)]] (-3.1) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: only 3 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.71, unclear); [[Lipoic acid (drug)]] (+0.69, unclear, ⚠ only 6 significant genes); [[Indacaterol (maleate) (drug)]] (+0.67, Adrenoceptor agonist, ⚠ only 3 significant genes); [[Pravastatin (sodium) (drug)]] (+0.67, unclear); [[Cloxacillin (sodium) (drug)]] (+0.67, unclear); [[Dimethyl fumarate (drug)]] (+0.66, unclear); [[Acetazolamide (drug)]] (+0.65, unclear, ⚠ only 3 significant genes); [[Fumaric acid (drug)]] (+0.65, unclear); [[Gallic acid (drug)]] (+0.62, Cyclooxygenase inhibitor); [[Asciminib (drug)]] (+0.62, Other TK inhibitor); [[Piroxicam (drug)]] (+0.62, Cyclooxygenase inhibitor)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[EPCAM]] | 5 µM | B | EPCAM activity raises the cells' numbers under Salicylic acid 5 µM (protects the cells) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.16× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[BSPRY]] | 5 µM | B | BSPRY activity raises the cells' numbers under Salicylic acid 5 µM (protects the cells) | lines that do not express BSPRY (29) vs lines expressing it (19) | the lines without BSPRY: 0.87× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KDF1, EPCAM, RAB25 |
| [[CLDN3]] | 5 µM | B | CLDN3 activity raises the cells' numbers under Salicylic acid 5 µM (protects the cells) | lines that do not express CLDN3 (28) vs lines expressing it (20) | the lines without CLDN3: 0.89× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, ESRP1 |
| [[CCL5]] | 5 µM | B | CCL5 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 1.17× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[NR3C1]] | 5 µM | C | NR3C1 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.14× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[FIGN]] | 5 µM | C | FIGN activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.11× the cells of the other lines | 0.058 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[C2orf74]] | 5 µM | C | C2orf74 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.12× the cells of the other lines | 0.079 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[ENSG00000288587]], [[KDELR3]], [[MICA]], [[POLD4]], [[PPP1R14B-AS1]] | 5 µM | C | ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000288587, KDELR3, MICA, POLD4, PPP1R14B-AS1 (3) vs lines expressing them (45) | the lines without ENSG00000288587, KDELR3, MICA (+2 more): 1.21× the cells of the other lines | 0.080 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: ACCS, SAT1, ADAMTSL5; maybe low, not absent; co-absent genes |
| [[SPART-AS1]] | 5 µM | C | SPART-AS1 activity lowers the cells' numbers under Salicylic acid 5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.10× the cells of the other lines | 0.097 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Salicylic acid"
- `tables/drugdoses.parquet` — dd in 931, 932, 933
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
