---
drug: "Fingolimod (hydrochloride)"
type: "drug"
salt_base: "Fingolimod"
targets: "PAK1"
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 144
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Fingolimod (hydrochloride)

*unclear (unclear) · targets: PAK1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 5 / 8 / 144; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.65 / -0.23.
> Flags by dose: - / - / toxic. ⚠ 5 µM: toxic (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:B11 | 0 / 5 | — | +0.17 | -0.1/+1.8/-0.8 | — |
| 0.5 µM | [[Plate 11]]:B11 | 1 / 7 | — | +0.52 | -0.3/+1.2/-0.7 | — |
| 5 µM | [[Plate 12]]:B11 | 128 / 16 | — | -1.13 | -1.0/+1.6/+1.1 | ⚠ toxic |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[MED12L]] 1.21× (z +2.9, 0/29 lines)

**5 µM** (128 genes, 128 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[MVK]] ⚠ 1.40× (z +4.7, 8/45 lines), [[ACAT2]] ⚠ 1.35× (z +4.4, 22/47 lines), [[FDPS]] ⚠ 1.42× (z +4.4, 35/48 lines), [[SOD3]] ⚠ 2.48× (z +4.4, 1/9 lines), [[TMEM154]] ⚠ 1.55× (z +4.4, 8/21 lines), [[WT1-AS]] ⚠ 1.72× (z +4.3, 0/10 lines), [[SCD]] ⚠ 1.35× (z +4.2, 35/48 lines), [[IDI1]] ⚠ 1.37× (z +4.2, 28/47 lines), [[TRBC2]] ⚠ 2.23× (z +4.0, 1/9 lines), [[KCNE4]] ⚠ 1.50× (z +3.9, 2/14 lines), [[HMGCS1]] ⚠ 1.37× (z +3.9, 26/47 lines), [[ENSG00000249803]] ⚠ 1.64× (z +3.9, 3/11 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[LINC01748]] 0.680× (z -4.6, 0/14 lines), [[OTUD1]] 0.785× (z -3.5, 6/45 lines), [[LINC02864]] 0.787× (z -3.1, 0/12 lines), [[POF1B]] 0.780× (z -3.0, 0/14 lines), [[ESRP1]] 0.802× (z -2.9, 0/17 lines)

**0.5 µM** (7 genes, none with an alert): [[LINC01029]] 0.472× (z -4.2, 1/6 lines), [[SFTA3-1]] 0.565× (z -4.1, 0/12 lines), [[PLAAT4]] 0.631× (z -3.5, 4/24 lines), [[ZIC1]] 0.662× (z -3.4, 0/12 lines), [[TNFRSF9]] 0.716× (z -3.3, 5/27 lines), [[TMEM30B]] 0.727× (z -3.2, 0/13 lines), [[ENSG00000258646]] 0.718× (z -3.2, 2/43 lines)

**5 µM** (16 genes, 16 with an alert ⚠; the drug-dose carries ⚠ toxic; 12 shown): [[ERLIN2]] ⚠ 0.769× (z -4.0, 18/46 lines), [[PHLDB2]] ⚠ 0.793× (z -3.8, 19/37 lines), [[IL11RA]] ⚠ 0.686× (z -3.6, 10/39 lines), [[VPS35L]] ⚠ 0.826× (z -3.6, 11/38 lines), [[ENSG00000290931]] ⚠ 0.794× (z -3.5, 12/27 lines), [[FZD7]] ⚠ 0.760× (z -3.4, 6/43 lines), [[ARHGAP28]] ⚠ 0.747× (z -3.3, 6/23 lines), [[EFCAB2]] ⚠ 0.822× (z -3.3, 15/47 lines), [[PCAT1]] ⚠ 0.818× (z -3.1, 10/36 lines), [[CDKN2B-AS1]] ⚠ 0.726× (z -3.1, 8/30 lines), [[LACC1]] ⚠ 0.813× (z -3.1, 9/41 lines), [[C1QTNF6]] ⚠ 0.763× (z -3.0, 6/45 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | [[Module 086]] (+2.5), [[Module 048]] (+2.2) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[NCI-H661 (line)]] (1.79), [[SW 1271 (line)]] (1.67), [[SW 1088 (line)]] (1.65), [[SW48 (line)]] (1.32) · weakest: [[SW480 (line)]] (0.259), [[CFPAC-1 (line)]] (0.360), [[Hs 766T (line)]] (0.474) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: vector dose flagged: toxic. Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Erythromycin (drug)]] (+0.82, unclear); [[Methylprednisolone succinate (drug)]] (+0.81, Glucocorticoid receptor agonist); [[Imiquimod (hydrochloride) (drug)]] (+0.79, unclear, ⚠ vector dose flagged: toxic); [[Darolutamide (drug)]] (+0.75, Androgen receptor antagonist, ⚠ only 5 significant genes); [[Docetaxel (Trihydrate) (drug)]] (+0.74, Microtubule inhibitor); [[Tranilast (drug)]] (+0.71, unclear, ⚠ only 6 significant genes); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.70, unclear); [[Decitabine (drug)]] (+0.70, DNA methyltransferase inhibitor); [[Celecoxib (drug)]] (+0.70, Cyclooxygenase inhibitor); [[Ipatasertib (drug)]] (+0.69, PI3K/AKT inhibitor); [[Bicalutamide (drug)]] (+0.67, Androgen receptor antagonist)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Fingolimod (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 453, 454, 455
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
