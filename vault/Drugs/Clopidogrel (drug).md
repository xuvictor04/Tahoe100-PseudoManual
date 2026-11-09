---
drug: "Clopidogrel"
type: "drug"
salt_base: "Clopidogrel"
targets: "P2RY12"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 80
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Clopidogrel

*unclear (inhibitor/antagonist) · targets: P2RY12 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 80 / 12 / 3; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.47 / 0.35.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D4 | 6 / 74 | — | +0.72 | +1.4/+1.5/+0.5 | — |
| 0.5 µM | [[Plate 11]]:D4 | 0 / 12 | — | +0.49 | +0.4/-0.1/-0.4 | — |
| 5 µM | [[Plate 12]]:D4 | 1 / 2 | — | -0.08 | +0.0/+0.2/-0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (6 genes, none with an alert): [[IFRD1]] 1.32× (z +3.2, 29/48 lines), [[FUS]] 1.21× (z +3.1, 26/48 lines), [[RPL10]] 1.25× (z +3.0, 14/48 lines), [[EIF4A2]] 1.22× (z +3.0, 25/48 lines), [[RPS3A]] 1.25× (z +2.9, 10/48 lines), [[CSRP2]] 1.31× (z +2.9, 4/42 lines)

**5 µM** (1 gene, none with an alert): [[MIR181A1HG]] 1.22× (z +3.0, 11/41 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (74 genes, none with an alert; 12 shown): [[ENSG00000287778]] 0.678× (z -4.5, 6/20 lines), [[GPR87]] 0.490× (z -4.4, 5/11 lines), [[ASAH2B]] 0.715× (z -4.3, 13/46 lines), [[ILDR2]] 0.579× (z -4.3, 2/16 lines), [[ENSG00000275016]] 0.523× (z -4.2, 0/3 lines), [[LINC01535]] 0.628× (z -4.1, 4/25 lines), [[LINC02566]] 0.457× (z -4.0, 0/2 lines), [[ENSG00000283128]] 0.741× (z -4.0, 8/47 lines), [[GPLD1]] 0.690× (z -3.9, 6/40 lines), [[ENSG00000241168]] 0.540× (z -3.9, 0/3 lines), [[IQCA1]] 0.645× (z -3.9, 2/15 lines), [[JPH3]] 0.704× (z -3.9, 3/18 lines)

**0.5 µM** (12 genes, none with an alert): [[MTMR7]] 0.636× (z -4.4, 5/27 lines), [[GRHL2]] 0.750× (z -4.2, 0/14 lines), [[C4BPB]] 0.666× (z -4.1, 0/11 lines), [[LINC01551]] 0.570× (z -3.9, 2/10 lines), [[MSI1]] 0.650× (z -3.8, 4/20 lines), [[ZNF667-AS1]] 0.656× (z -3.6, 1/14 lines), [[DNMBP-AS1]] 0.732× (z -3.6, 4/44 lines), [[ENSG00000286964]] 0.648× (z -3.2, 9/31 lines), [[LINC01029]] 0.568× (z -3.2, 0/6 lines), [[SHC2]] 0.755× (z -3.0, 7/37 lines), [[B3GNT3]] 0.746× (z -3.0, 0/17 lines), [[HS3ST1]] 0.793× (z -3.0, 0/17 lines)

**5 µM** (2 genes, none with an alert): [[C1orf216]] 0.745× (z -3.3, 3/41 lines), [[CCDC183]] 0.749× (z -3.2, 5/43 lines)

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
| 0.05 µM | [[C-33 A (line)]] (-3.5), [[NCI-H661 (line)]] (-3.3), [[A-427 (line)]] (-3.3), [[CFPAC-1 (line)]] (-3.3) | [[SW 1088 (line)]] (1.48), [[SW48 (line)]] (1.45), [[A-172 (line)]] (1.40), [[NCI-H2030 (line)]] (1.39) · weakest: [[NCI-H661 (line)]] (-0.0856), [[BT-474 (line)]] (0.556), [[NCI-H2347 (line)]] (0.628) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.83, unclear, ⚠ only 3 significant genes); [[Allopurinol (drug)]] (+0.81, unclear); [[Ranolazine (drug)]] (+0.75, unclear); [[Cloxacillin (sodium) (drug)]] (+0.75, unclear); [[Sacubitril_Valsartan (drug)]] (+0.73, unclear, ⚠ only 1 significant gene); [[Artemether (drug)]] (+0.70, unclear, ⚠ only 7 significant genes); [[Malotilate (drug)]] (+0.68, unclear); [[Tucatinib (drug)]] (+0.67, EGFR/ERBB inhibitor); [[Piroxicam (drug)]] (+0.64, Cyclooxygenase inhibitor); [[Lucanthone (drug)]] (+0.63, unclear); [[Rutin (trihydrate) (drug)]] (+0.59, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 30 arrows, 30 of them with an alert ⚠; grade A 0, B 25, C 5. Shown: the 15 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.75× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[BMPER]] | 0.05 µM | B | BMPER activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.77× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.77× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.75× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[SRPX]] | 0.05 µM | B | SRPX activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express SRPX (22) vs lines expressing it (26) | the lines without SRPX: 0.81× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: COL15A1, ARHGEF6, ENSG00000230647 |
| [[ENSG00000230479]] | 0.05 µM | B | ENSG00000230479 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express ENSG00000230479 (13) vs lines expressing it (35) | the lines without ENSG00000230479: 0.78× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: CLDN14-AS1, HRH1, ENSG00000289526; maybe low, not absent |
| [[SIRLNT]] | 0.05 µM | B | SIRLNT activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express SIRLNT (32) vs lines expressing it (16) | the lines without SIRLNT: 0.73× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SRGN, LINC01411, KCNMA1 |
| [[RSPO3]] | 0.05 µM | B | RSPO3 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.76× the cells of the other lines | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[ADAM12]] | 0.05 µM | B | ADAM12 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express ADAM12 (27) vs lines expressing it (21) | the lines without ADAM12: 0.77× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: ZEB2, MSC-AS1, CNRIP1 |
| [[CNRIP1]] | 0.05 µM | B | CNRIP1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.83× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[CFAP45]] | 0.05 µM | B | CFAP45 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express CFAP45 (6) vs lines expressing it (42) | the lines without CFAP45: 0.70× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[ALDH3B1]] | 0.05 µM | B | ALDH3B1 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express ALDH3B1 (9) vs lines expressing it (39) | the lines without ALDH3B1: 0.71× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[MYH14]] | 0.05 µM | B | MYH14 activity lowers the cells' numbers under Clopidogrel 0.05 µM (makes them more sensitive) | lines that do not express MYH14 (21) vs lines expressing it (27) | the lines without MYH14: 1.32× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |
| [[MGC4859]] | 0.05 µM | B | MGC4859 activity raises the cells' numbers under Clopidogrel 0.05 µM (protects the cells) | lines that do not express MGC4859 (8) vs lines expressing it (40) | the lines without MGC4859: 0.74× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |
| [[EPCAM]] | 0.05 µM | B | EPCAM activity lowers the cells' numbers under Clopidogrel 0.05 µM (makes them more sensitive) | lines that do not express EPCAM (28) vs lines expressing it (20) | the lines without EPCAM: 1.23× the cells of the other lines | 0.087 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, KDF1, CLDN3 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Clopidogrel"
- `tables/drugdoses.parquet` — dd in 281, 282, 283
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
