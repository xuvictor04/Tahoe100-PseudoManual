---
drug: "Vilanterol"
type: "drug"
salt_base: "Vilanterol"
targets: "ADRB2"
moa_fine: "Adrenoceptor agonist"
moa_broad: "activator/agonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 138
tags: ["drug", "moa/activator_agonist"]
generated_by: "tahoemap"
---

# Vilanterol

*Adrenoceptor agonist (activator/agonist) · targets: ADRB2 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 24 / 92 / 138; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.62.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:D9 | 17 / 7 | — | -0.89 | -0.9/-0.1/+1.1 | — |
| 0.5 µM | [[Plate 05]]:D9 | 60 / 32 | — | -0.42 | -0.7/-0.2/+1.8 | — |
| 5 µM | [[Plate 14]]:D9 | 66 / 72 | 0.902 | -0.11 | +0.1/+0.5/+2.3 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (17 genes, none with an alert; 12 shown): [[C7orf57]] 1.66× (z +3.7, 2/22 lines), [[ENSG00000273014]] 1.39× (z +3.4, 2/32 lines), [[SPNS2]] 1.38× (z +3.2, 5/22 lines), [[ENSG00000239462]] 1.29× (z +3.2, 10/27 lines), [[FCHO1]] 1.27× (z +3.1, 2/37 lines), [[GJC1]] 1.23× (z +3.1, 9/34 lines), [[MOAP1]] 1.23× (z +3.1, 5/46 lines), [[C3orf52]] 1.31× (z +3.1, 21/42 lines), [[ACP7]] 1.51× (z +3.0, 1/13 lines), [[AGTR1]] 1.51× (z +3.0, 0/10 lines), [[COLEC12]] 1.39× (z +2.9, 2/19 lines), [[LCK]] 1.52× (z +2.9, 0/11 lines)

**0.5 µM** (60 genes, none with an alert; 12 shown): [[STAG3]] 1.42× (z +4.4, 1/24 lines), [[KLHL21]] 1.45× (z +4.3, 20/45 lines), [[ENSG00000291156]] 1.54× (z +4.1, 17/41 lines), [[DEDD2]] 1.44× (z +4.1, 21/46 lines), [[DHPS]] 1.37× (z +4.1, 23/48 lines), [[CHPF2]] 1.43× (z +4.0, 17/45 lines), [[RER1]] 1.21× (z +4.0, 16/48 lines), [[KDELR3]] 1.36× (z +3.9, 14/44 lines), [[TFF1]] 2.02× (z +3.9, 9/16 lines), [[SPOCK1]] 1.27× (z +3.8, 4/19 lines), [[IGF2]] 1.52× (z +3.8, 12/16 lines), [[TRIM8]] 1.27× (z +3.8, 10/46 lines)

**5 µM** (66 genes, none with an alert; 12 shown): [[ENSG00000288000]] 1.44× (z +4.4, 35/49 lines), [[NGRN]] 1.20× (z +4.1, 20/48 lines), [[IER3]] 1.49× (z +4.1, 41/44 lines), [[SMIM41]] 1.54× (z +4.0, 13/43 lines), [[PYGM]] 1.52× (z +3.9, 18/45 lines), [[SLC43A3]] 1.25× (z +3.9, 12/20 lines), [[CRLF2]] 1.44× (z +3.9, 5/11 lines), [[ENSG00000254732]] 1.23× (z +3.9, 13/48 lines), [[ENSG00000267476]] 1.21× (z +3.8, 5/48 lines), [[NR4A2]] 1.28× (z +3.8, 26/42 lines), [[ENSG00000290180]] 1.28× (z +3.7, 11/46 lines), [[PPP1R32]] 1.24× (z +3.6, 4/44 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (7 genes, none with an alert): [[C5AR1]] 0.656× (z -3.4, 17/41 lines), [[RTN4RL1]] 0.727× (z -3.4, 2/26 lines), [[C19orf38]] 0.663× (z -3.4, 13/41 lines), [[TFEB]] 0.807× (z -3.1, 10/47 lines), [[FSTL3]] 0.716× (z -3.1, 11/39 lines), [[SIRT3]] 0.818× (z -2.9, 6/45 lines), [[CEP126]] 0.800× (z -2.7, 5/39 lines)

**0.5 µM** (32 genes, none with an alert; 12 shown): [[ZNG1E]] 0.752× (z -4.9, 17/44 lines), [[HERC2P9]] 0.704× (z -4.8, 18/44 lines), [[SENP2]] 0.821× (z -4.4, 19/48 lines), [[MDC1]] 0.807× (z -3.9, 19/48 lines), [[ENSG00000289985]] 0.689× (z -3.9, 12/36 lines), [[CEP120]] 0.819× (z -3.8, 15/48 lines), [[RCN1]] 0.779× (z -3.8, 24/47 lines), [[MRPS31P4]] 0.783× (z -3.7, 9/46 lines), [[ASMTL-AS1]] 0.646× (z -3.7, 19/46 lines), [[METTL14]] 0.822× (z -3.6, 17/48 lines), [[PRDM4]] 0.821× (z -3.6, 14/48 lines), [[SMN2]] 0.744× (z -3.6, 10/32 lines)

**5 µM** (72 genes, none with an alert; 12 shown): [[ENSG00000223727]] 0.637× (z -6.4, 28/40 lines), [[FHIT]] 0.697× (z -6.4, 39/43 lines), [[DIAPH2]] 0.796× (z -6.3, 35/42 lines), [[ENSG00000289986]] 0.731× (z -5.6, 15/43 lines), [[SUGCT]] 0.772× (z -5.5, 28/44 lines), [[ENSG00000226965]] 0.771× (z -5.4, 23/38 lines), [[LINC01505]] 0.785× (z -5.2, 23/43 lines), [[BCAS3]] 0.823× (z -4.9, 29/49 lines), [[LPP]] 0.818× (z -4.9, 29/49 lines), [[IMMP2L]] 0.768× (z -4.8, 38/49 lines), [[LINC01473]] 0.790× (z -4.8, 35/49 lines), [[ENSG00000251314]] 0.766× (z -4.7, 24/39 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 184]] (+2.1) | [[Module 194]] (-2.0) |
| 5 µM | [[Module 041]] (+2.5), [[Module 043]] (+2.3), [[Module 024]] (+2.2) | [[Module 200]] (-3.8), [[Module 185]] (-2.5), [[Module 211]] (-2.2) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[MIA PaCa-2 (line)]] (1.79), [[SW 1088 (line)]] (1.78), [[SW48 (line)]] (1.62), [[H4 (line)]] (1.52) · weakest: [[NCI-H2347 (line)]] (0.0940), [[SNU-423 (line)]] (0.137), [[BT-474 (line)]] (0.140) |
| 0.5 µM | — | [[SW 1271 (line)]] (1.39), [[HCT15 (line)]] (1.34), [[CFPAC-1 (line)]] (1.16), [[SK-MEL-2 (line)]] (1.13) · weakest: [[SW 900 (line)]] (0.506), [[SW48 (line)]] (0.541), [[AN3 CA (line)]] (0.569) |
| 5 µM | — | [[RPMI-7951 (line)]] (1.33), [[C32 (line)]] (1.27), [[SW48 (line)]] (1.17), [[COLO 205 (line)]] (1.15) · weakest: [[NCI-H1792 (line)]] (0.667), [[HepG2_C3A (line)]] (0.717), [[HCT15 (line)]] (0.719) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Tranilast (drug)]] (+0.68, unclear, ⚠ only 6 significant genes); [[Fingolimod (hydrochloride) (drug)]] (+0.64, unclear, ⚠ vector dose flagged: toxic); [[Methylprednisolone succinate (drug)]] (+0.63, Glucocorticoid receptor agonist); [[Docetaxel (Trihydrate) (drug)]] (+0.63, Microtubule inhibitor); [[Azithromycin (hydrate) (drug)]] (+0.61, unclear); [[Sivelestat (sodium tetrahydrate) (drug)]] (+0.60, unclear); [[APTO-253 (drug)]] (+0.59, unclear, ⚠ only 4 significant genes); [[AT7519 (drug)]] (+0.59, CDK inhibitor, ⚠ only 6 significant genes); [[Celecoxib (drug)]] (+0.57, Cyclooxygenase inhibitor); [[PF-06260933 (drug)]] (+0.56, Other MAPK inhibitor); [[Almonertinib (hydrochloride) (drug)]] (+0.55, EGFR/ERBB inhibitor); [[Bimatoprost (drug)]] (+0.54, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Vilanterol"
- `tables/drugdoses.parquet` — dd in 1084, 1085, 1086
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
