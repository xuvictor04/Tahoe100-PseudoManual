---
drug: "BI-78D3"
type: "drug"
salt_base: "BI-78D3"
targets: ""
moa_fine: "Other MAPK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 14
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# BI-78D3

*Other MAPK inhibitor (inhibitor/antagonist) · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 3 / 14 / 0; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): -0.10 / -0.45.
> Flags by dose: - / noisy plate (z scaled) / plate-row cell shift; noisy plate (z scaled).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 01]]:C3 | 1 / 2 | — | -0.32 | +0.4/-0.3/-0.1 | — |
| 0.5 µM | [[Plate 02]]:C3 | 13 / 1 | — | -0.66 | +1.0/+0.8/+1.9 | noisy plate (z scaled) |
| 5 µM | [[Plate 03]]:C3 | 0 / 0 | — | +1.05 | +1.1/+0.3/-0.5 | plate-row cell shift; noisy plate (z scaled) |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[LONRF3]] 1.23× (z +3.1, 5/37 lines)

**0.5 µM** (13 genes, none with an alert; 12 shown): [[MRPS18A]] 1.28× (z +3.4, 3/45 lines), [[AKR7A2]] 1.54× (z +3.3, 14/46 lines), [[ENSG00000250899]] 1.65× (z +3.3, 2/33 lines), [[SGPP2]] 1.30× (z +3.1, 0/16 lines), [[PPP4C]] 1.23× (z +3.0, 5/48 lines), [[ATP5F1B]] 1.49× (z +3.0, 26/48 lines), [[KLF10]] 1.32× (z +3.0, 14/48 lines), [[RHOT2]] 1.46× (z +2.9, 8/47 lines), [[HEXB]] 1.22× (z +2.8, 6/48 lines), [[YRDC]] 1.48× (z +2.8, 0/45 lines), [[EIF3I]] 1.42× (z +2.8, 21/48 lines), [[PHGDH]] 1.37× (z +2.8, 8/43 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENTREP2]] 0.804× (z -3.1, 2/24 lines), [[PLCD1]] 0.752× (z -3.0, 3/42 lines)

**0.5 µM** (1 gene, none with an alert): [[TTC31]] 0.766× (z -2.9, 4/48 lines)

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
| 5 µM | [[J82 (line)]] (-3.4) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[9-ING-41 (drug)]] (+0.78, GSK3 inhibitor); [[Sonidegib (drug)]] (+0.76, Sonic inhibitor); [[Canagliflozin (drug)]] (+0.75, Glucose transporter inhibitor); [[XRK3F2 (drug)]] (+0.75, unclear); [[LY-2584702 (tosylate salt) (drug)]] (+0.70, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[DT-061 (drug)]] (+0.69, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.64, Glucose transporter inhibitor); [[Nimesulide (drug)]] (+0.64, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[Lenalidomide (hemihydrate) (drug)]] (+0.63, unclear); [[Hydroxyfasudil (drug)]] (+0.61, unclear)

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Genes that set how the cells fare under it

*Arrows gene → cells under this drug at one of its doses (the cells' numbers relative to the other lines in the same wells). 5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Gene | Dose | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|---|
| [[KLRK1-AS1]] | 5 µM | B | KLRK1-AS1 activity raises the cells' numbers under BI-78D3 5 µM (protects the cells) | lines that do not express KLRK1-AS1 (11) vs lines expressing it (37) | the lines without KLRK1-AS1: 0.87× the cells of the other lines | 0.078 | ⚠ within organs, on part of the lines; also absent: BACH2; maybe low, not absent |
| [[LINC02306]] | 5 µM | B | LINC02306 activity raises the cells' numbers under BI-78D3 5 µM (protects the cells) | lines that do not express LINC02306 (13) vs lines expressing it (35) | the lines without LINC02306: 0.81× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: KCNMB2, COP1-DT, LINC02398; maybe low, not absent |
| [[SOX6]] | 5 µM | B | SOX6 activity raises the cells' numbers under BI-78D3 5 µM (protects the cells) | lines that do not express SOX6 (22) vs lines expressing it (26) | the lines without SOX6: 0.86× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent |
| [[MTMR7]] | 5 µM | B | MTMR7 activity raises the cells' numbers under BI-78D3 5 µM (protects the cells) | lines that do not express MTMR7 (16) vs lines expressing it (32) | the lines without MTMR7: 0.82× the cells of the other lines | 0.081 | ⚠ within organs, on part of the lines; also absent: GAP43, NRXN1, LOXL3; maybe low, not absent |
| [[BMPER]] | 5 µM | B | BMPER activity raises the cells' numbers under BI-78D3 5 µM (protects the cells) | lines that do not express BMPER (21) vs lines expressing it (27) | the lines without BMPER: 0.92× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: SPOCK1, ENSG00000253471, IL7R |

### Its targets: what acting on them probably does

None: it is not one of the compounds of a drug-target arrow.

## Data

- `tables/drugs.parquet` — drug == "BI-78D3"
- `tables/drugdoses.parquet` — dd in 135, 136, 137
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
