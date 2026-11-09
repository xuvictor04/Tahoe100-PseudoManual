---
drug: "Artemether"
type: "drug"
salt_base: "Artemether"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 7
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Artemether

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 7 / 4 / 4; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): none.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.37 / 0.15.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:F6 | 4 / 3 | — | +0.58 | +0.4/+0.5/+0.3 | — |
| 0.5 µM | [[Plate 11]]:F6 | 3 / 1 | — | -0.15 | +0.0/+0.1/+0.9 | — |
| 5 µM | [[Plate 12]]:F6 | 3 / 1 | — | +0.42 | -0.2/+1.1/-0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[CFAP210]] 2.06× (z +4.0, 19/46 lines), [[MLF1]] 1.49× (z +3.3, 26/43 lines), [[FAM222A]] 1.69× (z +3.3, 13/47 lines), [[RRP12]] 1.33× (z +2.9, 17/48 lines)

**0.5 µM** (3 genes, none with an alert): [[GPC5]] 1.61× (z +4.0, 18/39 lines), [[MIR193BHG]] 1.37× (z +3.5, 16/44 lines), [[USP3-AS1]] 1.23× (z +3.1, 5/47 lines)

**5 µM** (3 genes, none with an alert): [[MIR193BHG]] 1.55× (z +4.9, 27/44 lines), [[ALAS1]] 1.21× (z +3.8, 10/48 lines), [[GPC5]] 1.49× (z +3.3, 13/40 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[GSTA4]] 0.775× (z -3.1, 3/42 lines), [[EXO5-DT]] 0.746× (z -3.1, 3/39 lines), [[PPP1R26-AS1]] 0.785× (z -3.0, 7/45 lines)

**0.5 µM** (1 gene, none with an alert): [[ZNF320]] 0.827× (z -3.1, 5/37 lines)

**5 µM** (1 gene, none with an alert): [[KIF5C]] 0.794× (z -3.7, 11/48 lines)

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

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Aspirin (drug)]] (+0.73, Cyclooxygenase inhibitor, ⚠ only 3 significant genes); [[Clopidogrel (drug)]] (+0.70, unclear); [[Methylthiouracil (drug)]] (+0.69, unclear, ⚠ only 9 significant genes); [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.64, unclear, ⚠ only 3 significant genes); [[Rucaparib (phosphate) (drug)]] (+0.64, DNA synthesis/repair inhibitor, ⚠ only 5 significant genes); [[Malotilate (drug)]] (+0.63, unclear); [[Gefitinib (drug)]] (+0.60, EGFR/ERBB inhibitor); [[Gemfibrozil (drug)]] (+0.58, unclear, ⚠ only 2 significant genes); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] (+0.54, unclear); [[Allopurinol (drug)]] (+0.54, unclear); [[Tazarotene (drug)]] (+0.52, Retinoic receptor agonist); [[Omeprazole (drug)]] (+0.51, unclear); [[Aliskiren (drug)]] (+0.49, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.78× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.81× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[BMPER]] | 0.05 µM | B | BMPER activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.83× the cells of the other lines | 0.070 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |
| [[PAPPA]] | 0.05 µM | B | PAPPA activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express PAPPA (33) vs lines expressing it (15) | the lines without PAPPA: 0.78× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB |
| [[RSPO3]] | 0.05 µM | B | RSPO3 activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.80× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[CNRIP1]] | 0.05 µM | B | CNRIP1 activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express CNRIP1 (25) vs lines expressing it (23) | the lines without CNRIP1: 0.86× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, LINC03047 |
| [[PPP1R9A]] | 0.05 µM | B | PPP1R9A activity lowers the cells' numbers under Artemether 0.05 µM (makes them more sensitive) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 1.25× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[ZC3HAV1L]] | 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Artemether 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.36× the cells of the other lines | 0.032 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| [[ISG20]] | 0.05 µM | C | ISG20 activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express ISG20 (4) vs lines expressing it (44) | the lines without ISG20: 0.72× the cells of the other lines | 0.054 | ⚠ few lines (4 vs 46); tissue-confounded; across organs; also absent: TBILA, C3orf52, PERP; maybe low, not absent |
| [[TBILA]] | 0.05 µM | C | TBILA activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express TBILA (5) vs lines expressing it (43) | the lines without TBILA: 0.74× the cells of the other lines | 0.055 | ⚠ tissue-confounded; across organs; also absent: C3orf52, ISG20, PSMB8 |
| [[PSMB8]] | 0.05 µM | C | PSMB8 activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express PSMB8 (4) vs lines expressing it (44) | the lines without PSMB8: 0.71× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52 |
| [[LRRCC1]], [[OXR1]] | 0.05 µM | C | LRRCC1, OXR1 activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.73× the cells of the other lines | 0.059 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[CDKN1A]] | 0.05 µM | C | CDKN1A activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express CDKN1A (3) vs lines expressing it (45) | the lines without CDKN1A: 0.70× the cells of the other lines | 0.074 | ⚠ few lines (3 vs 47); across organs; also absent: LRRCC1, FAT1, SFXN3; maybe low, not absent |
| [[CEBPD]], [[GCA]] | 0.05 µM | C | CEBPD, GCA activity raises the cells' numbers under Artemether 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.69× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| [[RAB11FIP1]] | 0.05 µM | C | RAB11FIP1 activity lowers the cells' numbers under Artemether 0.05 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.45× the cells of the other lines | 0.085 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Artemether"
- `tables/drugdoses.parquet` — dd in 105, 106, 107
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
