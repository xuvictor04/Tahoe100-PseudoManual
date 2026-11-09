---
drug: "Bexarotene"
type: "drug"
salt_base: "Bexarotene"
targets: "RXRA, RXRB, RXRG"
moa_fine: "Retinoic receptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 99
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Bexarotene

*Retinoic receptor agonist (activator/agonist) · targets: RXRA, RXRB, RXRG · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 25 / 43 / 99; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.55 / 0.44.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 10]]:E8 | 25 / 0 | — | +0.01 | +0.2/+0.2/+0.5 | — |
| 0.5 µM | [[Plate 11]]:E8 | 27 / 16 | — | +0.22 | +1.1/+0.7/+1.2 | — |
| 5 µM | [[Plate 12]]:E8 | 37 / 62 | — | +0.12 | -0.1/+0.7/+0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (25 genes, none with an alert; 12 shown): [[ACSL3]] 1.86× (z +13.5, 47/48 lines), [[ABCA1]] 2.56× (z +11.1, 27/28 lines), [[ABCG1]] 2.80× (z +11.1, 32/33 lines), [[LPCAT3]] 1.65× (z +9.4, 40/48 lines), [[SCD]] 1.89× (z +9.0, 48/48 lines), [[ACACA]] 1.56× (z +7.8, 38/47 lines), [[OLMALINC]] 1.71× (z +7.0, 35/47 lines), [[RARB]] 1.45× (z +5.9, 12/20 lines), [[SREBF1]] 1.68× (z +5.6, 42/48 lines), [[FASN]] 1.58× (z +4.6, 27/47 lines), [[TMEM135]] 1.32× (z +4.4, 30/48 lines), [[DLC1]] 1.20× (z +4.3, 13/34 lines)

**0.5 µM** (27 genes, none with an alert; 12 shown): [[ACSL3]] 1.98× (z +14.9, 48/48 lines), [[ABCG1]] 3.14× (z +12.3, 31/32 lines), [[ABCA1]] 2.56× (z +11.1, 27/28 lines), [[SCD]] 2.12× (z +10.7, 46/48 lines), [[ACACA]] 1.76× (z +10.0, 42/47 lines), [[LPCAT3]] 1.74× (z +9.5, 38/48 lines), [[OLMALINC]] 1.68× (z +6.9, 36/47 lines), [[TMEM135]] 1.47× (z +6.1, 34/48 lines), [[SREBF1]] 1.69× (z +5.7, 39/48 lines), [[FASN]] 1.75× (z +5.6, 34/47 lines), [[RARB]] 1.35× (z +4.8, 13/20 lines), [[PLIN2]] 1.72× (z +4.7, 21/31 lines)

**5 µM** (37 genes, none with an alert; 12 shown): [[ACSL3]] 1.72× (z +11.8, 46/48 lines), [[ABCG1]] 2.01× (z +7.5, 25/33 lines), [[CPT1A]] 1.44× (z +7.0, 33/47 lines), [[SCD]] 1.63× (z +6.9, 46/48 lines), [[PLIN2]] 2.19× (z +6.8, 27/31 lines), [[DLC1]] 1.30× (z +6.0, 20/34 lines), [[ABCA1]] 1.64× (z +5.9, 22/28 lines), [[LPCAT3]] 1.35× (z +5.7, 20/48 lines), [[PDK4]] 1.80× (z +5.4, 16/23 lines), [[ACACA]] 1.35× (z +5.3, 28/47 lines), [[SLC25A20]] 1.51× (z +5.1, 7/46 lines), [[HAUS6]] 1.26× (z +4.9, 20/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.5 µM** (16 genes, none with an alert; 12 shown): [[LYPD6B]] 0.765× (z -4.1, 8/25 lines), [[PCBP3]] 0.805× (z -4.0, 8/26 lines), [[ENSG00000287023]] 0.705× (z -3.5, 5/22 lines), [[ARAP3]] 0.791× (z -3.4, 6/39 lines), [[SPATA24]] 0.739× (z -3.3, 4/43 lines), [[OLFML2A]] 0.738× (z -3.3, 6/27 lines), [[RPSAP52]] 0.745× (z -3.3, 12/28 lines), [[EGFR]] 0.818× (z -3.3, 18/41 lines), [[LINC01798]] 0.658× (z -3.3, 8/29 lines), [[KPNA2P3]] 0.777× (z -3.1, 7/43 lines), [[LINC02968]] 0.765× (z -3.1, 8/21 lines), [[PRR16]] 0.786× (z -3.0, 7/24 lines)

**5 µM** (62 genes, none with an alert; 12 shown): [[PLEKHS1]] 0.565× (z -4.6, 10/31 lines), [[BMP8A]] 0.639× (z -4.3, 12/45 lines), [[C21orf91-OT1]] 0.601× (z -4.2, 10/42 lines), [[RAMP1]] 0.691× (z -4.1, 6/28 lines), [[SLC22A20P]] 0.672× (z -4.0, 11/44 lines), [[OIT3]] 0.615× (z -3.8, 13/43 lines), [[IDI2-AS1]] 0.666× (z -3.8, 20/47 lines), [[ENSG00000289254]] 0.586× (z -3.7, 14/43 lines), [[MYLIP]] 0.732× (z -3.7, 26/47 lines), [[BATF2]] 0.633× (z -3.7, 11/33 lines), [[MYOCOS]] 0.617× (z -3.7, 15/46 lines), [[ENSG00000274949]] 0.637× (z -3.6, 13/46 lines)

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
| 0.05 µM | — | [[COLO 205 (line)]] (1.87), [[HCT15 (line)]] (1.71), [[HT-29 (line)]] (1.66), [[SW480 (line)]] (1.61) · weakest: [[A498 (line)]] (0.513), [[NCI-H2347 (line)]] (0.520), [[RKO (line)]] (0.598) |
| 0.5 µM | — | [[COLO 205 (line)]] (1.69), [[SW 1271 (line)]] (1.67), [[SW480 (line)]] (1.52), [[HT-29 (line)]] (1.50) · weakest: [[NCI-H661 (line)]] (0.423), [[NCI-H2347 (line)]] (0.431), [[NCI-H1573 (line)]] (0.576) |
| 5 µM | — | [[HS-578T (line)]] (1.61), [[A-172 (line)]] (1.46), [[LOX-IMVI (line)]] (1.36), [[HepG2_C3A (line)]] (1.31) · weakest: [[HCT15 (line)]] (0.439), [[AN3 CA (line)]] (0.617), [[BT-474 (line)]] (0.713) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Dimethyl fumarate (drug)]] (+0.62, unclear); [[Pravastatin (sodium) (drug)]] (+0.56, unclear); [[Tomivosertib (drug)]] (+0.54, Protein synthesis inhibitor); [[Edoxaban (tosylate monohydrate) (drug)]] (+0.53, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Mozavaptan (drug)]] (+0.51, unclear); [[LB-100 (drug)]] (+0.50, unclear, ⚠ only 5 significant genes); [[L-Thyroxine (sodium salt pentahydrate) (drug)]] (+0.49, unclear); [[Pimitespib (drug)]] (+0.49, unclear); [[Lopinavir (drug)]] (+0.47, unclear); [[Brivudine (drug)]] (+0.45, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Bexarotene"
- `tables/drugdoses.parquet` — dd in 188, 189, 190
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
