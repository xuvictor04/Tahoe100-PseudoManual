---
drug: "Fumaric acid"
type: "drug"
salt_base: "Fumaric acid"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 77
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Fumaric acid

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 13 / 77; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.03 / 0.47.
> Flags by dose: - / - / plate-row cell shift.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:A9 | 2 / 3 | — | +0.05 | -0.6/+0.2/-0.4 | — |
| 0.5 µM | [[Plate 08]]:A9 | 2 / 11 | — | +0.60 | -0.6/-0.5/-0.2 | — |
| 5 µM | [[Plate 09]]:A9 | 43 / 34 | — | +0.96 | -0.5/+0.3/+0.3 | plate-row cell shift |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[STK11]] 1.24× (z +3.8, 3/45 lines), [[CPNE1]] 1.21× (z +3.8, 25/48 lines)

**0.5 µM** (2 genes, none with an alert): [[VIM-AS1]] 1.34× (z +4.4, 4/41 lines), [[LAMTOR3]] 1.23× (z +3.0, 8/48 lines)

**5 µM** (43 genes, none with an alert; 12 shown): [[KMT2E]] 1.22× (z +4.3, 27/49 lines), [[SLC2A1]] 1.33× (z +4.2, 33/45 lines), [[ZNF292]] 1.22× (z +4.0, 24/49 lines), [[ZMIZ1]] 1.25× (z +3.9, 23/45 lines), [[SLC11A2]] 1.22× (z +3.9, 14/49 lines), [[PFKFB4]] 1.36× (z +3.8, 36/49 lines), [[WDR45B]] 1.41× (z +3.8, 42/49 lines), [[RBPJ]] 1.25× (z +3.8, 31/49 lines), [[PLEKHA2]] 1.23× (z +3.7, 20/44 lines), [[NPTN]] 1.23× (z +3.7, 25/49 lines), [[ERO1A]] 1.29× (z +3.7, 33/48 lines), [[RAB8B]] 1.28× (z +3.6, 25/49 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[HAPLN3]] 0.754× (z -3.2, 10/38 lines), [[ENSG00000285043]] 0.713× (z -3.2, 7/41 lines), [[SERPINB9]] 0.809× (z -3.0, 5/24 lines)

**0.5 µM** (11 genes, none with an alert): [[HDGFL2]] 0.726× (z -4.5, 27/48 lines), [[TNIP1]] 0.823× (z -4.3, 20/48 lines), [[GZF1]] 0.786× (z -3.8, 2/48 lines), [[DHX16]] 0.799× (z -3.8, 12/48 lines), [[FOXJ2]] 0.783× (z -3.5, 9/48 lines), [[DBN1]] 0.733× (z -3.4, 13/45 lines), [[USP18]] 0.722× (z -3.1, 7/44 lines), [[TBC1D10B]] 0.825× (z -3.1, 2/48 lines), [[MMP15]] 0.763× (z -3.1, 3/41 lines), [[OSTC]] 0.778× (z -3.0, 12/48 lines), [[HLA-C]] 0.799× (z -3.0, 21/46 lines)

**5 µM** (34 genes, none with an alert; 12 shown): [[ENSG00000255983]] 0.611× (z -3.9, 1/16 lines), [[ZFP69B]] 0.721× (z -3.8, 7/41 lines), [[ST6GALNAC2]] 0.690× (z -3.7, 6/37 lines), [[ENSG00000254733]] 0.754× (z -3.6, 2/39 lines), [[ENSG00000291185]] 0.684× (z -3.6, 2/30 lines), [[PSMD6-AS2]] 0.783× (z -3.5, 11/47 lines), [[ITPR2-AS1]] 0.598× (z -3.5, 8/39 lines), [[PRKG1-AS1]] 0.695× (z -3.4, 1/31 lines), [[RPAP3-DT]] 0.700× (z -3.4, 3/43 lines), [[ZNF382]] 0.737× (z -3.3, 4/29 lines), [[HSPBAP1]] 0.803× (z -3.3, 7/47 lines), [[ENOX2]] 0.751× (z -3.3, 24/48 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 207]] (+2.2), [[Module 164]] (+2.1) | [[Module 137]] (-2.5), [[Module 010]] (-2.1) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[CHP-212 (line)]] (1.63), [[NCI-H661 (line)]] (1.50), [[AN3 CA (line)]] (1.33), [[NCI-H2030 (line)]] (1.32) · weakest: [[LoVo (line)]] (0.627), [[KATO III (line)]] (0.627), [[SW 1271 (line)]] (0.714) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Pravastatin (sodium) (drug)]] (+0.83, unclear); [[Dimethyl fumarate (drug)]] (+0.77, unclear); [[Piroxicam (drug)]] (+0.76, Cyclooxygenase inhibitor); [[Daidzin (drug)]] (+0.76, unclear, ⚠ only 3 significant genes); [[Ranolazine (drug)]] (+0.71, unclear); [[Acetazolamide (drug)]] (+0.68, unclear, ⚠ only 3 significant genes); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.67, unclear); [[Allopurinol (drug)]] (+0.66, unclear); [[Aprepitant (drug)]] (+0.65, unclear); [[Sinomenine (drug)]] (+0.62, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[AOX1]] | 5 µM | B | AOX1 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.85× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ARHGEF6]] | 5 µM | B | ARHGEF6 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express ARHGEF6 (20) vs lines expressing it (28) | the lines without ARHGEF6: 0.84× the cells of the other lines | 0.064 | ⚠ within organs, on part of the lines; also absent: SRPX, MSRB3, ENSG00000230615; maybe low, not absent |
| [[SPOCK1]] | 5 µM | B | SPOCK1 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.84× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[KIRREL3]] | 5 µM | B | KIRREL3 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express KIRREL3 (36) vs lines expressing it (12) | the lines without KIRREL3: 0.81× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN |
| [[ENSG00000230647]] | 5 µM | B | ENSG00000230647 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.84× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[C2orf74]] | 5 µM | C | C2orf74 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express C2orf74 (13) vs lines expressing it (35) | the lines without C2orf74: 0.86× the cells of the other lines | 0.087 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: C2orf74-DT, ENSG00000286964, NR3C1 |
| [[FIGN]] | 5 µM | C | FIGN activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express FIGN (16) vs lines expressing it (32) | the lines without FIGN: 0.87× the cells of the other lines | 0.095 | ⚠ tissue-confounded; across organs; also absent: SPART-AS1, CCDC169, SPART |
| [[ACTR3-AS1]] | 5 µM | C | ACTR3-AS1's natural level raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | ACTR3-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.291 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Fumaric acid"
- `tables/drugdoses.parquet` — dd in 477, 478, 479
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
