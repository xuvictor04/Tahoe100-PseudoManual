---
drug: "Norepinephrine (hydrochloride)"
type: "drug"
salt_base: "Norepinephrine"
targets: "ADRA1A, ADRA1B, ADRA1D, ADRA2A, ADRA2B, ADRA2C, ADRB1"
moa_fine: "Adrenoceptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 27
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Norepinephrine (hydrochloride)

*Adrenoceptor agonist (activator/agonist) · targets: ADRA1A, ADRA1B, ADRA1D, ADRA2A, ADRA2B, ADRA2C, ADRB1 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 0 / 3 / 27; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.40.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E4 | 0 / 0 | — | -0.11 | -0.3/-0.2/-0.7 | — |
| 0.5 µM | [[Plate 05]]:E4 | 1 / 2 | — | +0.72 | -0.0/-0.7/-0.8 | — |
| 5 µM | [[Plate 14]]:E4 | 21 / 6 | 0.631 | -0.19 | +0.9/+0.4/-0.7 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (1 gene, none with an alert): [[ENSG00000283201]] 1.30× (z +3.0, 2/39 lines)

**5 µM** (21 genes, none with an alert; 12 shown): [[ENSG00000259033]] 1.45× (z +4.7, 14/42 lines), [[ENSG00000289084]] 1.23× (z +3.9, 3/44 lines), [[MIR4527HG]] 1.35× (z +3.8, 2/12 lines), [[SH3GL2]] 1.25× (z +3.6, 4/25 lines), [[KCNQ3]] 1.26× (z +3.6, 4/21 lines), [[MTUS2]] 1.23× (z +3.5, 7/44 lines), [[ERBB4]] 1.23× (z +3.4, 2/15 lines), [[HS6ST3]] 1.23× (z +3.3, 6/27 lines), [[ENSG00000271860]] 1.24× (z +3.3, 2/46 lines), [[TMEFF2]] 1.30× (z +3.2, 4/41 lines), [[MAP2]] 1.23× (z +3.2, 5/33 lines), [[UBR5-DT]] 1.21× (z +3.1, 6/45 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (2 genes, none with an alert): [[SLC1A2]] 0.531× (z -4.3, 3/19 lines), [[ENSG00000259678]] 0.770× (z -3.3, 7/44 lines)

**5 µM** (6 genes, none with an alert): [[NOMO1]] 0.809× (z -6.2, 24/48 lines), [[PARP3]] 0.775× (z -3.9, 3/43 lines), [[PAIP2B]] 0.831× (z -3.5, 5/38 lines), [[RPL4]] 0.828× (z -3.4, 27/48 lines), [[ENSG00000256029]] 0.804× (z -3.2, 3/38 lines), [[CAPN1-AS1]] 0.809× (z -3.2, 9/41 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[Module 207]] (-2.5), [[Module 059]] (-2.0) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | — |
| 5 µM | — | [[MIA PaCa-2 (line)]] (1.96), [[C32 (line)]] (1.83), [[SW1417 (line)]] (1.66), [[NCI-H23 (line)]] (1.44) · weakest: [[Hs 766T (line)]] (-0.390), [[COLO 205 (line)]] (0.0982), [[AN3 CA (line)]] (0.137) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Acetohexamide (drug)]] (+0.76, unclear); [[Busulfan (drug)]] (+0.69, DNA synthesis/repair inhibitor); [[Brimonidine (drug)]] (+0.67, Adrenoceptor agonist); [[Finasteride (drug)]] (+0.65, unclear); [[Olanzapine (drug)]] (+0.65, unclear, ⚠ only 5 significant genes); [[Diammonium Glycyrrhizinate (drug)]] (+0.62, unclear); [[Palmatine (chloride) (drug)]] (+0.59, unclear); [[Megestrol (drug)]] (+0.58, unclear, ⚠ vector dose flagged: cell-cycle shift); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.57, unclear); [[MK-8353 (drug)]] (+0.56, Other MAPK inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Norepinephrine (hydrochloride)"
- `tables/drugdoses.parquet` — dd in 726, 727, 728
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
