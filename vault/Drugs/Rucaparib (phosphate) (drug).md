---
drug: "Rucaparib (phosphate)"
type: "drug"
salt_base: "Rucaparib"
targets: "PARP1, PARP2, PARP3"
moa_fine: "DNA synthesis/repair inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 5
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Rucaparib (phosphate)

*DNA synthesis/repair inhibitor (inhibitor/antagonist) · targets: PARP1, PARP2, PARP3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 1 / 5; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.28 / 0.44.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B1 | 0 / 3 | — | +0.40 | -0.0/-0.4/+0.8 | — |
| 0.5 µM | [[Plate 08]]:B1 | 1 / 0 | — | +0.21 | +0.2/+0.5/+1.3 | — |
| 5 µM | [[Plate 09]]:B1 | 1 / 4 | — | +1.28 | +0.5/+0.4/+0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[STEAP1B]] 1.27× (z +3.3, 10/47 lines)

**5 µM** (1 gene, none with an alert): [[KLF9]] 1.21× (z +3.0, 11/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[GBP5]] 0.573× (z -3.5, 2/20 lines), [[SLAIN1]] 0.765× (z -3.4, 5/25 lines), [[AK7]] 0.749× (z -2.9, 6/42 lines)

**5 µM** (4 genes, none with an alert): [[ENSG00000285572]] 0.645× (z -3.6, 4/41 lines), [[TSHZ3-AS1]] 0.654× (z -3.2, 1/23 lines), [[MAP3K14-AS1]] 0.760× (z -3.0, 5/45 lines), [[PDE4B]] 0.819× (z -2.9, 2/25 lines)

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

⚠ This drug's own vector: only 5 significant genes. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Artemether (drug)]] (+0.64, unclear, ⚠ only 7 significant genes); [[Ranolazine (drug)]] (+0.58, unclear); [[Entecavir (monohydrate) (drug)]] (+0.55, unclear); [[Clopidogrel (drug)]] (+0.53, unclear); [[Mebendazole (drug)]] (+0.53, Microtubule inhibitor); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] (+0.52, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.50, unclear); [[Gemfibrozil (drug)]] (+0.49, unclear, ⚠ only 2 significant genes); [[Malotilate (drug)]] (+0.49, unclear); [[Cloxacillin (sodium) (drug)]] (+0.47, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 20 arrows, 20 of them with an alert ⚠; grade A 0, B 5, C 15. Shown: the 15 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.80× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[KCNMA1]] | 5 µM | B | KCNMA1 activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.77× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[GJA1]] | 5 µM | B | GJA1 activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express GJA1 (26) vs lines expressing it (22) | the lines without GJA1: 0.81× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: SALL1, SHISAL1, EPHA5-AS1 |
| [[CCL5]] | 5 µM | B | CCL5 activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express CCL5 (22) vs lines expressing it (26) | the lines without CCL5: 0.79× the cells of the other lines | 0.096 | ⚠ within organs, on part of the lines; also absent: SRGN, FLI1, KCNMA1 |
| [[PRDM5]] | 0.5 µM | B | PRDM5 activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express PRDM5 (13) vs lines expressing it (35) | the lines without PRDM5: 0.86× the cells of the other lines | 0.097 | ⚠ within organs, on part of the lines; also absent: UBE2E2, JHY, SSPN |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 0.83× the cells of the other lines | 0.008 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[FIGN]] | 0.5 µM | C | FIGN activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.86× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 0.85× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[PWWP2B]] | 5 µM | C | PWWP2B activity lowers the cells' numbers under Rucaparib (phosphate) 5 µM (makes them more sensitive) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 1.48× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 0.87× the cells of the other lines | 0.035 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[TBILA]] | 5 µM | C | TBILA activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.74× the cells of the other lines | 0.042 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[SIX1]] | 0.5 µM | C | SIX1 activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express SIX1 (8) vs lines expressing it (40) | the lines without SIX1: 0.85× the cells of the other lines | 0.053 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: TIGD7, ENSG00000286964, FERMT2 |
| [[ISG20]] | 5 µM | C | ISG20 activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.73× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| [[CEBPD]], [[GCA]] | 5 µM | C | CEBPD, GCA activity raises the cells' numbers under Rucaparib (phosphate) 5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.70× the cells of the other lines | 0.059 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[ENSG00000286964]] | 0.5 µM | C | ENSG00000286964 activity raises the cells' numbers under Rucaparib (phosphate) 0.5 µM (protects the cells) | lines that do not express ENSG00000286964 (10) vs lines expressing it (38) | the lines without ENSG00000286964: 0.86× the cells of the other lines | 0.068 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: SIX1, C2orf74, SYDE1 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Rucaparib (phosphate)"
- `tables/drugdoses.parquet` — dd in 917, 918, 919
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
