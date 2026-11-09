---
drug: "Roxadustat"
type: "drug"
salt_base: "Roxadustat"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 66
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Roxadustat

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 36 / 3 / 66; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.40 / -0.30.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:E4 | 34 / 2 | — | -0.48 | -0.2/-0.5/+1.0 | — |
| 0.5 µM | [[Plate 08]]:E4 | 2 / 1 | — | -0.09 | -0.3/+0.2/+1.5 | — |
| 5 µM | [[Plate 09]]:E4 | 47 / 19 | — | +0.14 | -1.3/-0.5/-1.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (34 genes, none with an alert; 12 shown): [[RPUSD2]] 1.58× (z +3.9, 6/26 lines), [[LINC01535]] 1.59× (z +3.8, 2/18 lines), [[ENSG00000281883]] 1.63× (z +3.7, 1/22 lines), [[ENSG00000268833]] 1.56× (z +3.5, 2/21 lines), [[ENSG00000228714]] 1.34× (z +3.5, 3/22 lines), [[ZNF365]] 1.40× (z +3.4, 0/21 lines), [[LINC02257]] 1.49× (z +3.4, 2/20 lines), [[TMEM201]] 1.31× (z +3.3, 5/38 lines), [[SNCAIP]] 1.42× (z +3.3, 2/19 lines), [[FAM219B]] 1.26× (z +3.2, 8/43 lines), [[CX3CL1]] 1.54× (z +3.2, 2/16 lines), [[WAKMAR2]] 1.38× (z +3.2, 5/30 lines)

**0.5 µM** (2 genes, none with an alert): [[MTCO1P12]] 1.44× (z +3.2, 3/46 lines), [[BAX]] 1.24× (z +3.1, 8/46 lines)

**5 µM** (47 genes, none with an alert; 12 shown): [[AK4]] 1.46× (z +7.2, 36/47 lines), [[UPRT]] 1.35× (z +5.6, 23/45 lines), [[HLA-L-1]] 1.48× (z +5.4, 18/37 lines), [[ZNF470]] 1.29× (z +4.6, 10/28 lines), [[VLDLR]] 1.36× (z +4.4, 18/38 lines), [[ENSG00000291136]] 1.24× (z +4.4, 27/48 lines), [[PLOD2]] 1.34× (z +4.4, 26/33 lines), [[ZNF654]] 1.26× (z +4.3, 31/48 lines), [[GYS1]] 1.29× (z +4.3, 28/48 lines), [[RBAK]] 1.22× (z +4.2, 20/48 lines), [[DIPK2A]] 1.27× (z +4.2, 23/46 lines), [[ZNF12]] 1.22× (z +4.1, 23/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[RPS18P9]] 0.750× (z -3.6, 7/41 lines), [[ENPP4]] 0.827× (z -2.9, 7/29 lines)

**0.5 µM** (1 gene, none with an alert): [[ZNF324B]] 0.717× (z -3.4, 7/43 lines)

**5 µM** (19 genes, none with an alert; 12 shown): [[TMSB4X]] 0.668× (z -4.2, 38/39 lines), [[PPP5D1P-1]] 0.709× (z -4.0, 11/44 lines), [[ANKHD1-EIF4EBP3]] 0.704× (z -3.9, 16/47 lines), [[NOMO1]] 0.825× (z -3.8, 12/47 lines), [[ENSG00000258757]] 0.657× (z -3.7, 17/46 lines), [[FGFBP1]] 0.521× (z -3.7, 2/11 lines), [[LINC01019]] 0.768× (z -3.5, 7/45 lines), [[IL18]] 0.779× (z -3.5, 8/30 lines), [[NDUFAF1]] 0.750× (z -3.4, 11/45 lines), [[CMAHP]] 0.789× (z -3.4, 4/44 lines), [[DIRC3-AS1]] 0.750× (z -3.4, 9/42 lines), [[DTD2]] 0.806× (z -3.3, 9/46 lines)

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
| 0.05 µM | — | [[CHP-212 (line)]] (2.05), [[SW 1271 (line)]] (1.83), [[HepG2_C3A (line)]] (1.60), [[RKO (line)]] (1.60) · weakest: [[NCI-H460 (line)]] (-0.149), [[PANC-1 (line)]] (-0.0449), [[BT-474 (line)]] (-0.0279) |
| 0.5 µM | — | — |
| 5 µM | — | [[HepG2_C3A (line)]] (1.46), [[NCI-H1792 (line)]] (1.38), [[BT-474 (line)]] (1.35), [[HOP62 (line)]] (1.32) · weakest: [[AsPC-1 (line)]] (0.308), [[A498 (line)]] (0.346), [[KATO III (line)]] (0.581) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Fluvoxamine (drug)]] (+0.62, unclear); [[Mozavaptan (drug)]] (+0.61, unclear); [[Asciminib (drug)]] (+0.57, Other TK inhibitor); [[Folic acid (drug)]] (+0.54, unclear); [[Clopidogrel (drug)]] (+0.54, unclear); [[Pentagastrin (drug)]] (+0.53, unclear, ⚠ only 9 significant genes); [[Methyl aminolevulinate (hydrochloride) (drug)]] (+0.52, unclear, ⚠ only 3 significant genes); [[Lucanthone (drug)]] (+0.51, unclear); [[Bosentan (hydrate) (drug)]] (+0.48, unclear); [[Tadalafil (drug)]] (+0.48, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Roxadustat"
- `tables/drugdoses.parquet` — dd in 914, 915, 916
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
