---
drug: "Valdecoxib"
type: "drug"
salt_base: "Valdecoxib"
targets: "PTGS2"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 12
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Valdecoxib

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS2 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 8 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.25 / -0.02.
> Flags by dose: low cells (technical?) / - / -.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:G4 | 11 / 1 | — | -1.00 | -0.8/-0.4/-0.3 | low cells (technical?) |
| 0.5 µM | [[Plate 11]]:G4 | 5 / 3 | — | -0.62 | -0.0/+0.7/-0.2 | — |
| 5 µM | [[Plate 12]]:G4 | 0 / 0 | — | -0.07 | -0.6/-0.7/-0.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (11 genes, none with an alert): [[RASSF2]] 1.46× (z +4.7, 5/27 lines), [[TPRXL]] 1.66× (z +4.3, 1/12 lines), [[ENSG00000290588]] 1.50× (z +3.8, 0/23 lines), [[LINC03041]] 1.46× (z +3.8, 4/24 lines), [[BTN2A3P-1]] 1.38× (z +3.5, 6/37 lines), [[HTR2C]] 1.46× (z +3.1, 1/10 lines), [[GALNT16]] 1.32× (z +3.0, 1/25 lines), [[ENSG00000291061]] 1.41× (z +3.0, 0/19 lines), [[LHX6]] 1.39× (z +2.9, 0/18 lines), [[TSPEAR]] 1.41× (z +2.9, 1/22 lines), [[PLPP4]] 1.37× (z +2.8, 0/15 lines)

**0.5 µM** (5 genes, none with an alert): [[POLR2J3]] 1.43× (z +3.7, 10/43 lines), [[PPIA]] 1.25× (z +3.6, 25/48 lines), [[FAAH]] 1.43× (z +3.6, 5/29 lines), [[KLHL2P1]] 1.43× (z +3.5, 7/38 lines), [[ARHGAP28]] 1.29× (z +2.9, 1/23 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (1 gene, none with an alert): [[TELO2]] 0.760× (z -4.0, 10/43 lines)

**0.5 µM** (3 genes, none with an alert): [[CIAO3]] 0.784× (z -3.5, 11/43 lines), [[MFSD9]] 0.832× (z -3.4, 11/46 lines), [[GLRB]] 0.798× (z -3.0, 5/27 lines)

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
| 5 µM | [[NCI-H1792 (line)]] (-3.7) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Pimozide (drug)]] (+0.68, unclear); [[Vismodegib (drug)]] (+0.64, Sonic inhibitor, ⚠ only 5 significant genes); [[Pioglitazone (drug)]] (+0.61, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.59, unclear); [[Nafamostat (mesylate) (drug)]] (+0.53, unclear, ⚠ only 3 significant genes); [[Atazanavir (sulfate) (drug)]] (+0.50, unclear); [[AZD2858 (drug)]] (+0.49, GSK3 inhibitor, ⚠ vector dose flagged: toxic); [[Mitoxantrone (dihydrochloride) (drug)]] (+0.49, DNA synthesis/repair inhibitor); [[Rosiglitazone (drug)]] (+0.49, unclear); [[Isocorydine (drug)]] (+0.48, unclear); [[Orlistat (drug)]] (+0.48, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Valdecoxib"
- `tables/drugdoses.parquet` — dd in 1069, 1070, 1071
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
