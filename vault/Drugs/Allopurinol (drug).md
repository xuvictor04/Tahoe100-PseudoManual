---
drug: "Allopurinol"
type: "drug"
salt_base: "Allopurinol"
targets: "XDH"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 18
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Allopurinol

*unclear (inhibitor/antagonist) · targets: XDH · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 18 / 1 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.03 / 0.29.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:D3 | 3 / 15 | — | +0.88 | +0.6/+1.5/+1.4 | — |
| 0.5 µM | [[Plate 11]]:D3 | 0 / 1 | — | +0.18 | -1.1/-0.4/-0.3 | — |
| 5 µM | [[Plate 12]]:D3 | 0 / 0 | — | +0.38 | -0.1/-0.1/+0.4 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[CFAP210]] 1.79× (z +3.2, 18/46 lines), [[MLF1]] 1.46× (z +3.2, 25/43 lines), [[RRP12]] 1.35× (z +3.0, 21/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (15 genes, none with an alert; 12 shown): [[ENSG00000267699]] 0.687× (z -3.7, 4/43 lines), [[EXO5-DT]] 0.712× (z -3.6, 8/39 lines), [[PEX1]] 0.808× (z -3.3, 7/48 lines), [[PIGL]] 0.818× (z -3.2, 18/48 lines), [[ENSG00000286787]] 0.687× (z -3.2, 11/47 lines), [[ZFP2]] 0.696× (z -3.2, 9/44 lines), [[ADAMTS9-AS2]] 0.779× (z -3.2, 4/18 lines), [[MOB3B]] 0.787× (z -3.2, 7/38 lines), [[CRYL1]] 0.828× (z -3.1, 11/48 lines), [[ENSG00000254363]] 0.697× (z -3.1, 9/46 lines), [[PIGC]] 0.803× (z -3.0, 4/48 lines), [[GGACT]] 0.721× (z -3.0, 6/45 lines)

**0.5 µM** (1 gene, none with an alert): [[C3orf62]] 0.780× (z -3.3, 5/46 lines)

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

- [[Sacubitril_Valsartan (drug)]] (+0.91, unclear, ⚠ only 1 significant gene); [[Clopidogrel (drug)]] (+0.81, unclear); [[Ranolazine (drug)]] (+0.77, unclear); [[Cloxacillin (sodium) (drug)]] (+0.76, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.74, unclear); [[Piroxicam (drug)]] (+0.72, Cyclooxygenase inhibitor); [[Hesperidin (drug)]] (+0.69, unclear); [[Verapamil (drug)]] (+0.69, unclear, ⚠ only 5 significant genes); [[Dimethyl fumarate (drug)]] (+0.67, unclear); [[Fumaric acid (drug)]] (+0.66, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[ENSG00000230647]] | 0.05 µM | B | ENSG00000230647 activity raises the cells' numbers under Allopurinol 0.05 µM (protects the cells) | lines that do not express ENSG00000230647 (24) vs lines expressing it (24) | the lines without ENSG00000230647: 0.82× the cells of the other lines | 0.056 | ⚠ within organs, on part of the lines; also absent: ADAM12, ENSG00000253891, SPOCK1 |
| [[SPOCK1]] | 0.05 µM | B | SPOCK1 activity raises the cells' numbers under Allopurinol 0.05 µM (protects the cells) | lines that do not express SPOCK1 (29) vs lines expressing it (19) | the lines without SPOCK1: 0.79× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41 |
| [[RSPO3]] | 0.05 µM | B | RSPO3 activity raises the cells' numbers under Allopurinol 0.05 µM (protects the cells) | lines that do not express RSPO3 (39) vs lines expressing it (9) | the lines without RSPO3: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2 |
| [[LINC03004]] | 0.05 µM | B | LINC03004 activity raises the cells' numbers under Allopurinol 0.05 µM (protects the cells) | lines that do not express LINC03004 (22) vs lines expressing it (26) | the lines without LINC03004: 0.81× the cells of the other lines | 0.080 | ⚠ within organs, on part of the lines; also absent: MSC-AS1, OR4F15, ADAM12; maybe low, not absent |
| [[KCNMA1]] | 0.05 µM | B | KCNMA1 activity raises the cells' numbers under Allopurinol 0.05 µM (protects the cells) | lines that do not express KCNMA1 (26) vs lines expressing it (22) | the lines without KCNMA1: 0.79× the cells of the other lines | 0.088 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[LINC02057]] | 0.05 µM | B | LINC02057 activity raises the cells' numbers under Allopurinol 0.05 µM (protects the cells) | lines that do not express LINC02057 (25) vs lines expressing it (23) | the lines without LINC02057: 0.80× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[PPP1R9A]] | 0.05 µM | B | PPP1R9A activity lowers the cells' numbers under Allopurinol 0.05 µM (makes them more sensitive) | lines that do not express PPP1R9A (16) vs lines expressing it (32) | the lines without PPP1R9A: 1.25× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, PRR36 |
| [[PRSS23]] | 0.05 µM | B | PRSS23 activity raises the cells' numbers under Allopurinol 0.05 µM (protects the cells) | lines that do not express PRSS23 (13) vs lines expressing it (35) | the lines without PRSS23: 0.78× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[ZC3HAV1L]] | 0.05 µM | C | ZC3HAV1L activity lowers the cells' numbers under Allopurinol 0.05 µM (makes them more sensitive) | lines that do not express ZC3HAV1L (5) vs lines expressing it (43) | the lines without ZC3HAV1L: 1.32× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; also absent: OSR2, PTER, VRK2 |
| [[PTPN3]] | 0.05 µM | C | PTPN3 activity lowers the cells' numbers under Allopurinol 0.05 µM (makes them more sensitive) | lines that do not express PTPN3 (3) vs lines expressing it (45) | the lines without PTPN3: 1.34× the cells of the other lines | 0.094 | ⚠ few lines (3 vs 47); across organs; also absent: FOXRED2, MMP15, PBX4 |
| [[RAB11FIP1]] | 0.05 µM | C | RAB11FIP1 activity lowers the cells' numbers under Allopurinol 0.05 µM (makes them more sensitive) | lines that do not express RAB11FIP1 (3) vs lines expressing it (45) | the lines without RAB11FIP1: 1.40× the cells of the other lines | 0.096 | ⚠ few lines (3 vs 47); across organs; also absent: PTPN3, ZFHX2 |
| [[PWWP2B]] | 0.05 µM | C | PWWP2B activity lowers the cells' numbers under Allopurinol 0.05 µM (makes them more sensitive) | lines that do not express PWWP2B (3) vs lines expressing it (45) | the lines without PWWP2B: 1.40× the cells of the other lines | 0.097 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "Allopurinol"
- `tables/drugdoses.parquet` — dd in 72, 73, 74
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
