---
drug: "Rifaximin"
type: "drug"
salt_base: "Rifaximin"
targets: ""
moa_fine: "unclear"
moa_broad: "unclear"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 43
tags: ["drug", "moa/unclear"]
generated_by: "tahoemap"
---

# Rifaximin

*unclear (unclear) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 6 / 6 / 43; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.63 / 0.66.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:G1 | 2 / 4 | — | +0.17 | -0.2/-0.3/-1.2 | — |
| 0.5 µM | [[Plate 08]]:G1 | 1 / 5 | — | +0.06 | -0.8/-0.0/-1.7 | — |
| 5 µM | [[Plate 09]]:G1 | 14 / 29 | — | -0.10 | -1.7/-0.3/-2.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[CD47]] 1.23× (z +3.6, 20/46 lines), [[SCAMP4]] 1.21× (z +3.2, 5/47 lines)

**0.5 µM** (1 gene, none with an alert): [[ENSG00000205236]] 1.32× (z +3.8, 1/47 lines)

**5 µM** (14 genes, none with an alert; 12 shown): [[LPCAT2]] 1.21× (z +4.3, 10/39 lines), [[TRIQK]] 1.29× (z +4.3, 20/46 lines), [[FRY]] 1.25× (z +3.7, 11/34 lines), [[C2CD5]] 1.28× (z +3.5, 23/48 lines), [[PRMT7]] 1.23× (z +3.4, 12/48 lines), [[ZNF362]] 1.38× (z +3.4, 7/44 lines), [[METTL25]] 1.28× (z +3.4, 10/47 lines), [[KALRN]] 1.21× (z +3.2, 9/38 lines), [[DGLUCY]] 1.23× (z +3.2, 9/46 lines), [[FLJ46284]] 1.42× (z +3.2, 9/43 lines), [[NPIPB14P]] 1.25× (z +3.2, 13/48 lines), [[ATP6AP1L]] 1.30× (z +3.1, 9/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, none with an alert): [[LINC03002]] 0.620× (z -3.6, 2/20 lines), [[THEM4]] 0.829× (z -3.4, 8/42 lines), [[ENSG00000283765]] 0.667× (z -3.3, 14/40 lines), [[EREG]] 0.782× (z -3.0, 4/22 lines)

**0.5 µM** (5 genes, none with an alert): [[DHX33]] 0.831× (z -4.1, 8/47 lines), [[FSTL3]] 0.645× (z -4.0, 22/40 lines), [[DUSP1]] 0.684× (z -3.3, 23/42 lines), [[SLC16A14]] 0.758× (z -3.2, 4/31 lines), [[STRA6]] 0.715× (z -3.0, 2/20 lines)

**5 µM** (29 genes, none with an alert; 12 shown): [[LRRC17]] 0.504× (z -4.9, 6/19 lines), [[HSP90AA2P]] 0.580× (z -4.5, 12/39 lines), [[DHX33]] 0.820× (z -4.2, 7/47 lines), [[MRM3]] 0.733× (z -4.1, 13/46 lines), [[FSTL3]] 0.632× (z -4.1, 20/40 lines), [[PSMG1]] 0.776× (z -4.0, 9/46 lines), [[FASTKD3]] 0.731× (z -4.0, 6/43 lines), [[METTL13]] 0.821× (z -3.9, 7/46 lines), [[PSMD6]] 0.769× (z -3.8, 22/47 lines), [[HIGD1A]] 0.766× (z -3.7, 17/47 lines), [[SLC35A4]] 0.734× (z -3.7, 12/46 lines), [[ABCF2]] 0.777× (z -3.7, 11/47 lines)

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
| 5 µM | — | [[hTERT-HPNE (line)]] (1.61), [[Hs 766T (line)]] (1.42), [[RPMI-7951 (line)]] (1.38), [[LOX-IMVI (line)]] (1.34) · weakest: [[AN3 CA (line)]] (0.468), [[SW 1271 (line)]] (0.497), [[HepG2_C3A (line)]] (0.603) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Trimetrexate (drug)]] (+0.50, DNA synthesis/repair inhibitor); [[Tetracycline (hydrochloride) (drug)]] (+0.44, unclear, ⚠ only 6 significant genes); [[Entecavir (monohydrate) (drug)]] (+0.43, unclear); [[Sulfisoxazole (drug)]] (+0.43, unclear); [[Tolcapone (drug)]] (+0.41, unclear, ⚠ only 6 significant genes); [[Rucaparib (phosphate) (drug)]] (+0.37, DNA synthesis/repair inhibitor, ⚠ only 5 significant genes); [[Triclosan (drug)]] (+0.36, unclear, ⚠ only 2 significant genes); [[Captopril (drug)]] (+0.36, unclear); [[ULK-101 (drug)]] (+0.35, unclear); [[Ciclopirox (drug)]] (+0.35, unclear); [[Vilanterol (drug)]] (+0.33, Adrenoceptor agonist); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.33, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Rifaximin"
- `tables/drugdoses.parquet` — dd in 893, 894, 895
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
