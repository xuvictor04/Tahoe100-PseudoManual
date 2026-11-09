---
drug: "Fluvoxamine"
type: "drug"
salt_base: "Fluvoxamine"
targets: "SLC6A4"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 29
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Fluvoxamine

*unclear (unclear) · targets: SLC6A4 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 8 / 29 / 5; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.24 / -0.01.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:F9 | 1 / 7 | — | +0.40 | +0.5/+0.4/+0.5 | — |
| 0.5 µM | [[Plate 08]]:F9 | 2 / 27 | — | -0.08 | -0.6/-1.6/-0.8 | — |
| 5 µM | [[Plate 09]]:F9 | 4 / 1 | — | -0.32 | +0.7/+0.4/+1.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[CCDC200]] 1.58× (z +3.5, 14/46 lines)

**0.5 µM** (2 genes, none with an alert): [[SYN1]] 1.40× (z +3.2, 5/45 lines), [[GLB1L2]] 1.30× (z +3.2, 2/31 lines)

**5 µM** (4 genes, none with an alert): [[MIR181A1HG]] 1.26× (z +3.3, 19/41 lines), [[CYP1B1]] 1.56× (z +2.9, 14/19 lines), [[ALDH1A3]] 1.26× (z +2.9, 5/27 lines), [[ORAI1]] 1.37× (z +2.8, 6/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[ENSG00000267248]] 0.615× (z -4.0, 9/34 lines), [[ZNF2]] 0.789× (z -3.7, 12/46 lines), [[LINC01569]] 0.666× (z -3.3, 4/38 lines), [[SEC24B-AS1]] 0.711× (z -3.2, 4/43 lines), [[ENSG00000242021]] 0.764× (z -3.2, 2/18 lines), [[ADD3-AS1]] 0.689× (z -3.0, 3/34 lines), [[MMP17]] 0.769× (z -2.8, 2/26 lines)

**0.5 µM** (27 genes, none with an alert; 12 shown): [[FBN2]] 0.744× (z -4.4, 0/17 lines), [[POF1B]] 0.711× (z -4.2, 0/14 lines), [[GALNT13]] 0.777× (z -4.0, 0/17 lines), [[MIR548XHG]] 0.672× (z -3.9, 0/10 lines), [[ITGB6]] 0.780× (z -3.8, 0/16 lines), [[PSENEN]] 0.679× (z -3.7, 17/47 lines), [[CDH6]] 0.648× (z -3.7, 0/14 lines), [[SERPINB5]] 0.715× (z -3.6, 0/14 lines), [[ENSG00000285669]] 0.739× (z -3.6, 8/45 lines), [[GSDMC]] 0.570× (z -3.5, 0/6 lines), [[PRKY]] 0.778× (z -3.5, 0/17 lines), [[BMP5]] 0.659× (z -3.5, 0/10 lines)

**5 µM** (1 gene, none with an alert): [[TMTC1]] 0.765× (z -4.0, 6/23 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 179]] (+2.2) | — |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[HOP62 (line)]] (-4.9), [[A498 (line)]] (-4.4), [[A549 (line)]] (-4.2), [[Hs 766T (line)]] (-3.8), [[HS-578T (line)]] (-3.7) | [[HepG2_C3A (line)]] (1.98), [[AN3 CA (line)]] (1.96), [[NCI-H2030 (line)]] (1.85), [[RKO (line)]] (1.59) · weakest: [[HS-578T (line)]] (0.456), [[BT-474 (line)]] (0.559), [[LoVo (line)]] (0.656) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Thymopentin (drug)]] (+0.77, unclear, ⚠ only 2 significant genes); [[Clonidine (hydrochloride) (drug)]] (+0.70, Adrenoceptor agonist, ⚠ only 4 significant genes); [[Asciminib (drug)]] (+0.70, Other TK inhibitor); [[Pemetrexed (drug)]] (+0.67, DNA synthesis/repair inhibitor); [[Mozavaptan (drug)]] (+0.65, unclear); [[Gallic acid (drug)]] (+0.65, Cyclooxygenase inhibitor); [[Tadalafil (drug)]] (+0.64, unclear); [[Roxadustat (drug)]] (+0.62, unclear); [[Ivermectin (drug)]] (+0.62, unclear); [[Lopinavir (drug)]] (+0.61, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 48 arrows, 48 of them with an alert ⚠; grade A 0, B 2, C 46. Shown: the 15 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SLFN5]] | 0.5 µM | B | SLFN5 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express SLFN5 (11) vs lines expressing it (37) | the lines without SLFN5: 1.41× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000261273, ETS1, SAMD9; maybe low, not absent |
| [[KCNMA1]] | 0.5 µM | B | KCNMA1 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 1.39× the cells of the other lines | 0.094 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[FIGN]] | 0.5 µM | C | FIGN activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 1.33× the cells of the other lines | 0.013 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[NR3C1]] | 0.5 µM | C | NR3C1 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express NR3C1 (13) vs lines expressing it (35) | the lines without NR3C1: 1.41× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; co-occurs with SETD1B, ZFHX3; also absent: C2orf74-DT, C2orf74, SPART-AS1 |
| [[C2orf74]] | 0.5 µM | C | C2orf74 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 1.35× the cells of the other lines | 0.022 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[SPART-AS1]] | 0.5 µM | C | SPART-AS1 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express SPART-AS1 (16) vs lines expressing it (32) | the lines without SPART-AS1: 1.28× the cells of the other lines | 0.043 | ⚠ tissue-confounded; across organs; also absent: CCDC169, FIGN, SPART |
| [[PICART1]] | 0.5 µM | C | PICART1 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express PICART1 (4) vs lines expressing it (44) | the lines without PICART1: 1.52× the cells of the other lines | 0.066 | ⚠ few lines (4 vs 46); across organs; also absent: GULP1, RND3, MYO10; maybe low, not absent |
| [[TBILA]] | 0.5 µM | C | TBILA activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 1.47× the cells of the other lines | 0.070 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[PSMB8]] | 0.5 µM | C | PSMB8 activity lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 1.44× the cells of the other lines | 0.092 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[RNU4-2]] | 0.5 µM | C | RNU4-2's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | RNU4-2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72 | 0.234 over the table, 0.015 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[SIRT5]] | 0.5 µM | C | SIRT5's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | SIRT5's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.70 | 0.268 over the table, 0.019 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[EML2]] | 0.5 µM | C | EML2's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | EML2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.317 over the table, 0.044 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[KIF27]] | 0.5 µM | C | KIF27's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | KIF27's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65 | 0.390 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ZNF333]] | 0.5 µM | C | ZNF333's natural level raises the cells' numbers under Fluvoxamine 0.5 µM (protects the cells) | ZNF333's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64 | 0.390 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| [[ACTR3-AS1]] | 0.5 µM | C | ACTR3-AS1's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.390 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Fluvoxamine"
- `tables/drugdoses.parquet` — dd in 462, 463, 464
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
