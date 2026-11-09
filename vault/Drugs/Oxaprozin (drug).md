---
drug: "Oxaprozin"
type: "drug"
salt_base: "Oxaprozin"
targets: "PTGS1, PTGS2, NFKB1"
moa_fine: "Cyclooxygenase inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 118
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Oxaprozin

*Cyclooxygenase inhibitor (inhibitor/antagonist) · targets: PTGS1, PTGS2, NFKB1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 13 / 118 / 3; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.31 / 0.51.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:C3 | 10 / 3 | — | -0.44 | -1.2/-1.1/+0.2 | — |
| 0.5 µM | [[Plate 11]]:C3 | 118 / 0 | — | -0.87 | -0.7/-1.5/+0.1 | — |
| 5 µM | [[Plate 12]]:C3 | 3 / 0 | — | -0.17 | -0.2/-1.3/+0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[TELO2]] 1.26× (z +3.3, 2/44 lines), [[SLCO1C1]] 1.58× (z +3.3, 1/19 lines), [[NKAIN1]] 1.39× (z +3.2, 1/35 lines), [[TMPRSS3]] 1.43× (z +3.2, 2/18 lines), [[FUT3]] 1.33× (z +3.1, 0/17 lines), [[LRRC7]] 1.26× (z +3.1, 4/29 lines), [[CEACAM16-AS1]] 1.23× (z +3.1, 8/44 lines), [[PKNOX2]] 1.36× (z +3.0, 3/27 lines), [[RUBCNL]] 1.38× (z +2.9, 0/13 lines), [[CTTN-DT]] 1.21× (z +2.8, 4/46 lines)

**0.5 µM** (118 genes, none with an alert; 12 shown): [[ENSG00000286251]] 1.44× (z +4.3, 0/17 lines), [[ATXN7L3-AS1]] 1.47× (z +4.3, 4/35 lines), [[ZNF503-AS1]] 1.49× (z +4.2, 0/19 lines), [[PTOV1-AS1]] 1.44× (z +4.0, 8/40 lines), [[GAB3]] 1.50× (z +3.9, 2/21 lines), [[LINC02284]] 1.51× (z +3.9, 3/25 lines), [[ENSG00000261543]] 1.84× (z +3.9, 5/15 lines), [[MYOM3]] 1.54× (z +3.9, 0/15 lines), [[TRPA1]] 1.47× (z +3.9, 1/16 lines), [[CYP4F11]] 1.47× (z +3.9, 0/18 lines), [[LINC01169]] 1.59× (z +3.8, 0/6 lines), [[UBE2QL1]] 1.62× (z +3.8, 1/13 lines)

**5 µM** (3 genes, none with an alert): [[CDH3]] 1.26× (z +3.2, 2/21 lines), [[IL31RA]] 1.31× (z +3.0, 0/19 lines), [[LINC02438]] 1.33× (z +3.0, 0/12 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (3 genes, none with an alert): [[FAAP100]] 0.719× (z -3.8, 12/44 lines), [[CELSR2]] 0.737× (z -3.5, 6/37 lines), [[ENSG00000286677]] 0.581× (z -3.3, 11/36 lines)

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
| 0.5 µM | — | [[SW 1088 (line)]] (1.92), [[NCI-H661 (line)]] (1.71), [[SW 1271 (line)]] (1.54), [[AN3 CA (line)]] (1.47) · weakest: [[NCI-H1573 (line)]] (-0.104), [[CFPAC-1 (line)]] (0.109), [[SW480 (line)]] (0.266) |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Bestatin (hydrochloride) (drug)]] (+0.80, unclear); [[Canagliflozin (hemihydrate) (drug)]] (+0.76, Glucose transporter inhibitor); [[Bimatoprost (drug)]] (+0.75, unclear); [[Nimesulide (drug)]] (+0.74, Cyclooxygenase inhibitor, ⚠ no trustworthy dose (vector dose flagged: toxic; unreliable plate only)); [[LY-2584702 (tosylate salt) (drug)]] (+0.74, MTOR inhibitor, ⚠ vector dose flagged: toxic); [[Drospirenone (drug)]] (+0.73, unclear); [[Vitamin K4 (drug)]] (+0.71, unclear); [[Isocorydine (drug)]] (+0.71, unclear); [[Celecoxib (drug)]] (+0.71, Cyclooxygenase inhibitor); [[Thymol (drug)]] (+0.70, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Oxaprozin"
- `tables/drugdoses.parquet` — dd in 759, 760, 761
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
