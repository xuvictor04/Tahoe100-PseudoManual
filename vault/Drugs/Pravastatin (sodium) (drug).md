---
drug: "Pravastatin (sodium)"
type: "drug"
salt_base: "Pravastatin"
targets: "HMGCR"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 134
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Pravastatin (sodium)

*unclear (inhibitor/antagonist) · targets: HMGCR · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 8 / 11 / 134; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.44 / 0.64.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A10 | 3 / 5 | — | -0.18 | -0.4/-0.4/-1.0 | — |
| 0.5 µM | [[Plate 08]]:A10 | 0 / 11 | — | +0.64 | -0.8/-1.0/-1.2 | — |
| 5 µM | [[Plate 09]]:A10 | 51 / 83 | — | +1.18 | -0.4/+0.4/-0.2 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[ENSG00000270149]] 1.29× (z +3.3, 5/27 lines), [[ENSG00000228643]] 1.54× (z +3.1, 8/39 lines), [[KIF17]] 1.41× (z +2.9, 3/34 lines)

**5 µM** (51 genes, none with an alert; 12 shown): [[NDRG1]] 1.55× (z +5.0, 41/42 lines), [[INSIG2]] 1.41× (z +4.8, 39/48 lines), [[KMT2E]] 1.25× (z +4.6, 36/48 lines), [[NPEPPS]] 1.26× (z +4.4, 34/48 lines), [[PLEKHA2]] 1.28× (z +4.3, 25/43 lines), [[RYBP]] 1.35× (z +4.1, 35/48 lines), [[ZDHHC9]] 1.25× (z +4.1, 12/48 lines), [[ZNF292]] 1.22× (z +4.1, 24/48 lines), [[KANSL3]] 1.24× (z +4.0, 24/48 lines), [[ELL2]] 1.31× (z +3.9, 24/36 lines), [[SEC23A]] 1.24× (z +3.9, 34/48 lines), [[CLK4]] 1.24× (z +3.8, 8/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[TAP1]] 0.748× (z -3.9, 24/48 lines), [[ZFP1]] 0.810× (z -3.4, 13/46 lines), [[C8orf58]] 0.744× (z -3.2, 7/40 lines), [[RFESD]] 0.749× (z -3.2, 5/32 lines), [[DECR1]] 0.805× (z -3.1, 10/47 lines)

**0.5 µM** (11 genes, none with an alert): [[RASGEF1A]] 0.608× (z -4.4, 1/21 lines), [[HNF4A]] 0.740× (z -4.0, 0/14 lines), [[GPR141]] 0.605× (z -3.7, 1/9 lines), [[MXRA5]] 0.614× (z -3.7, 1/13 lines), [[LINC01518]] 0.670× (z -3.6, 0/11 lines), [[REG4]] 0.482× (z -3.5, 0/5 lines), [[ENSG00000259925]] 0.586× (z -3.4, 1/16 lines), [[MYB]] 0.710× (z -3.3, 0/24 lines), [[ENSG00000256915]] 0.715× (z -3.2, 3/32 lines), [[COLGALT2]] 0.749× (z -3.2, 0/24 lines), [[GRHL2]] 0.820× (z -2.9, 0/14 lines)

**5 µM** (83 genes, none with an alert; 12 shown): [[RASGRF1]] 0.600× (z -4.2, 4/28 lines), [[OR3A2]] 0.551× (z -4.1, 1/13 lines), [[ENSG00000286026]] 0.544× (z -4.0, 1/19 lines), [[ENSG00000262160]] 0.694× (z -4.0, 3/38 lines), [[C2CD4A]] 0.453× (z -4.0, 0/8 lines), [[ENSG00000270792]] 0.661× (z -3.9, 9/41 lines), [[ENSG00000286797]] 0.636× (z -3.9, 0/12 lines), [[TGIF2-RAB5IF]] 0.669× (z -3.9, 6/45 lines), [[UGT1A1]] 0.461× (z -3.9, 2/11 lines), [[THBS4-AS1]] 0.577× (z -3.8, 8/35 lines), [[ENSG00000289956]] 0.743× (z -3.8, 8/40 lines), [[TMEM139]] 0.610× (z -3.8, 3/15 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 207]] (+2.3) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[SW 1088 (line)]] (1.69), [[H4 (line)]] (1.46), [[hTERT-HPNE (line)]] (1.43), [[CHP-212 (line)]] (1.34) · weakest: [[LoVo (line)]] (0.605), [[HEC-1-A (line)]] (0.640), [[COLO 205 (line)]] (0.690) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Fumaric acid (drug)]] (+0.83, unclear); [[Ranolazine (drug)]] (+0.79, unclear); [[Dimethyl fumarate (drug)]] (+0.78, unclear); [[Daidzin (drug)]] (+0.77, unclear, ⚠ only 3 significant genes); [[Piroxicam (drug)]] (+0.74, Cyclooxygenase inhibitor); [[Tomivosertib (drug)]] (+0.72, Protein synthesis inhibitor); [[Captopril (drug)]] (+0.71, unclear); [[Goserelin (acetate) (drug)]] (+0.69, unclear); [[Cloxacillin (sodium) (drug)]] (+0.68, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 13 arrows, 13 of them with an alert ⚠; grade A 0, B 12, C 1.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AOX1]] | 5 µM | B | AOX1 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.86× the cells of the other lines | 0.049 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ARHGEF6]] | 5 µM | B | ARHGEF6 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.87× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[LINC00922]] | 5 µM | B | LINC00922 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express LINC00922 (9) vs lines expressing it (39) | the lines without LINC00922: 0.86× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[TBX3]] | 5 µM | B | TBX3 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express TBX3 (10) vs lines expressing it (38) | the lines without TBX3: 0.87× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.85× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[EPCAM]] | 5 µM | B | EPCAM activity lowers the cells' numbers under Pravastatin (sodium) 5 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.14× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |
| [[BMPER]] | 5 µM | B | BMPER activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.87× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[MIR3659HG]] | 5 µM | B | MIR3659HG activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express MIR3659HG (5) vs lines expressing it (43) | the lines without MIR3659HG: 0.82× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: USP31, ZNF594, WHRN; maybe low, not absent |
| [[DOCK2]] | 5 µM | B | DOCK2 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express DOCK2 (21) vs lines expressing it (27) | the lines without DOCK2: 0.87× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[HSD11B2]] | 5 µM | B | HSD11B2 activity lowers the cells' numbers under Pravastatin (sodium) 5 µM (makes them more sensitive) | lines that do not express HSD11B2 (16) vs lines expressing it (32) | the lines without HSD11B2: 1.15× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: MCF2L, CHDH, IL17RB; maybe low, not absent |
| [[ENPP1]] | 5 µM | B | ENPP1 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express ENPP1 (11) vs lines expressing it (37) | the lines without ENPP1: 0.87× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: MEIS3, EPHB1, MCTP1; maybe low, not absent |
| [[ITPK1]] | 5 µM | C | ITPK1 activity lowers the cells' numbers under Pravastatin (sodium) 5 µM (makes them more sensitive) | lines that do not express ITPK1 (4) vs lines expressing it (44) | the lines without ITPK1: 1.24× the cells of the other lines | 0.035 | ⚠ few lines (4 vs 46); across organs; also absent: ENSG00000253796; maybe low, not absent |

### Its targets: what acting on them probably does

*Drug-target arrows of the compound classes it belongs to (compounds sharing a listed target and mechanism; one molecule counts once, under all its names): the target → a gene whose level those compounds move. A row that names several targets is one test: the compounds share them all, and any of them could be the cause. 4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Its target | Gene it moves | This drug | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|---|
| [[HMGCR]] | [[PMP22]] | moves it that way too | B | HMGCR activity lowers PMP22's level | compounds that target HMGCR: 2 of 2 raise it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds |
| [[HMGCR]] | [[IQCD]] | moves it that way too | B | HMGCR activity raises IQCD's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HMGCR]] | [[NDRG1]] | moves it that way too | B | HMGCR activity lowers NDRG1's level | compounds that target HMGCR: 2 of 2 raise it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds |
| [[HMGCR]] | [[SLC35G1]] | moves it that way too | B | HMGCR activity raises SLC35G1's level | compounds that target HMGCR: 2 of 2 lower it (Pitavastatin, Pravastatin) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

## Data

- `tables/drugs.parquet` — drug == "Pravastatin (sodium)"
- `tables/drugdoses.parquet` — dd in 839, 840, 841
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
