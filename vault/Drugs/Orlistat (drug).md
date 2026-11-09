---
drug: "Orlistat"
type: "drug"
salt_base: "Orlistat"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 52
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Orlistat

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 52 / 2 / 3; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.19 / 0.12.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:D2 | 50 / 2 | — | -0.82 | -0.4/-0.8/+0.1 | — |
| 0.5 µM | [[Plate 08]]:D2 | 2 / 0 | — | -0.20 | +0.0/-0.5/+0.7 | — |
| 5 µM | [[Plate 09]]:D2 | 2 / 1 | — | +0.46 | -0.6/-1.2/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (50 genes, none with an alert; 12 shown): [[ENSG00000288591]] 1.77× (z +4.3, 2/13 lines), [[PTOV1-AS1]] 1.52× (z +4.2, 6/36 lines), [[TLCD4-RWDD3]] 1.47× (z +3.8, 2/18 lines), [[TEKTIP1]] 1.44× (z +3.7, 2/23 lines), [[GLS2]] 1.52× (z +3.7, 2/18 lines), [[ARL17A]] 1.29× (z +3.7, 3/41 lines), [[LINC02932]] 1.45× (z +3.7, 3/21 lines), [[GABRB3]] 1.30× (z +3.6, 1/15 lines), [[ARNT2-DT]] 1.82× (z +3.5, 0/11 lines), [[ENSG00000226640]] 1.55× (z +3.5, 0/12 lines), [[ENSG00000285000]] 1.35× (z +3.4, 3/35 lines), [[WDR24]] 1.39× (z +3.4, 2/29 lines)

**0.5 µM** (2 genes, none with an alert): [[LMNTD1]] 1.38× (z +3.1, 1/24 lines), [[MEGF11]] 1.22× (z +2.7, 0/40 lines)

**5 µM** (2 genes, none with an alert): [[MVK]] 1.28× (z +3.3, 4/47 lines), [[FASN]] 1.34× (z +2.8, 13/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000257452]] 0.716× (z -3.9, 12/43 lines), [[MTFR1L]] 0.805× (z -3.2, 10/43 lines)

**5 µM** (1 gene, none with an alert): [[FUT3]] 0.739× (z -3.2, 4/18 lines)

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
| 0.05 µM | — | [[NCI-H661 (line)]] (1.66), [[SW 1271 (line)]] (1.64), [[AN3 CA (line)]] (1.63), [[CHP-212 (line)]] (1.33) · weakest: [[PANC-1 (line)]] (0.0411), [[SW480 (line)]] (0.0608), [[NCI-H1792 (line)]] (0.201) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Monocrotaline (drug)]] (+0.69, unclear); [[Lonafarnib (drug)]] (+0.63, RAS inhibitor, ⚠ vector dose flagged: toxic); [[Lidocaine (hydrochloride) (drug)]] (+0.61, unclear); [[Ataluren (drug)]] (+0.56, unclear, ⚠ only 7 significant genes); [[Cysteamine (hydrochloride) (drug)]] (+0.56, unclear); [[Dinaciclib (drug)]] (+0.54, CDK inhibitor, ⚠ vector dose flagged: toxic; transcription drop; cell-cycle shift); [[Nevirapine (drug)]] (+0.54, unclear, ⚠ only 7 significant genes); [[Drospirenone (drug)]] (+0.54, unclear); [[Imiquimod (maleate) (drug)]] (+0.50, unclear); [[Pimozide (drug)]] (+0.49, unclear); [[Pyridoxine (drug)]] (+0.48, unclear); [[Riluzole hydrochloride (drug)]] (+0.48, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Orlistat"
- `tables/drugdoses.parquet` — dd in 744, 745, 746
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
