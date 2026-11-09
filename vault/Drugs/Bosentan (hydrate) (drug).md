---
drug: "Bosentan (hydrate)"
type: "drug"
salt_base: "Bosentan"
targets: "EDNRA, EDNRB"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "5"
max_sig_genes: 301
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Bosentan (hydrate)

*unclear (inhibitor/antagonist) · targets: EDNRA, EDNRB · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 12 / 52 / 301; best dose 5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.44 / -0.02.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 07]]:B4 | 2 / 10 | — | -0.25 | -0.1/+0.1/+1.1 | — |
| 0.5 µM | [[Plate 08]]:B4 | 1 / 51 | — | +0.21 | +0.5/+0.9/+1.2 | — |
| 5 µM | [[Plate 09]]:B4 | 145 / 156 | — | -0.95 | -1.2/-1.2/-0.5 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000287176]] 1.48× (z +2.9, 0/12 lines), [[ENSG00000249328]] 1.32× (z +2.7, 1/37 lines)

**0.5 µM** (1 gene, none with an alert): [[FBXO33]] 1.20× (z +3.0, 7/48 lines)

**5 µM** (145 genes, none with an alert; 12 shown): [[MGC4859]] 1.66× (z +4.8, 6/28 lines), [[LINC02112]] 1.59× (z +4.7, 3/23 lines), [[VPS26B]] 1.27× (z +4.6, 18/47 lines), [[FUT3]] 1.54× (z +4.5, 4/13 lines), [[MT-ND1]] 1.80× (z +4.5, 47/47 lines), [[GOLGA7B]] 1.49× (z +4.4, 7/32 lines), [[DARS1-AS1]] 1.50× (z +4.4, 17/44 lines), [[DPYSL4]] 1.62× (z +4.3, 6/17 lines), [[HYAL3]] 1.57× (z +4.2, 5/25 lines), [[FCHSD1]] 1.45× (z +4.2, 20/42 lines), [[PPP1R32]] 1.44× (z +4.2, 9/37 lines), [[ENSG00000290951]] 1.52× (z +4.2, 3/30 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (10 genes, none with an alert): [[NKD2]] 0.706× (z -3.6, 10/31 lines), [[CCDC136]] 0.755× (z -3.5, 11/35 lines), [[IPCEF1]] 0.725× (z -3.3, 6/33 lines), [[MPP2]] 0.768× (z -3.2, 8/37 lines), [[FSCN2]] 0.530× (z -3.2, 18/38 lines), [[TNKS1BP1]] 0.767× (z -3.1, 24/47 lines), [[ENSG00000230021]] 0.775× (z -3.1, 14/47 lines), [[FBN1]] 0.809× (z -3.1, 6/19 lines), [[ENSG00000270019]] 0.686× (z -3.0, 9/37 lines), [[RTKN]] 0.817× (z -2.9, 12/41 lines)

**0.5 µM** (51 genes, none with an alert; 12 shown): [[MT-RNR1]] 0.325× (z -6.6, 48/48 lines), [[DHFR]] 0.485× (z -6.0, 46/48 lines), [[KMT2B]] 0.751× (z -4.7, 27/48 lines), [[NSMF]] 0.681× (z -4.5, 23/45 lines), [[TBC1D10B]] 0.783× (z -4.0, 8/47 lines), [[TNKS1BP1]] 0.706× (z -3.9, 31/48 lines), [[ARHGAP33]] 0.703× (z -3.9, 9/45 lines), [[H4C5]] 0.534× (z -3.8, 18/43 lines), [[INPPL1]] 0.744× (z -3.7, 14/48 lines), [[CEP170B]] 0.720× (z -3.7, 18/47 lines), [[RPS2P5]] 0.547× (z -3.6, 13/43 lines), [[CRAT]] 0.757× (z -3.6, 15/45 lines)

**5 µM** (156 genes, none with an alert; 12 shown): [[GSK3B-DT]] 0.598× (z -5.8, 25/43 lines), [[THUMPD3-AS1]] 0.693× (z -5.7, 36/47 lines), [[LINC01619]] 0.615× (z -5.7, 40/45 lines), [[SNHG26]] 0.632× (z -5.4, 19/33 lines), [[PRKAG1]] 0.811× (z -5.4, 18/47 lines), [[ENSG00000273269]] 0.498× (z -5.3, 20/36 lines), [[ACTR3-AS1]] 0.605× (z -5.3, 22/44 lines), [[ENSG00000290180]] 0.603× (z -5.1, 21/44 lines), [[ENSG00000255639]] 0.610× (z -5.0, 20/37 lines), [[ENSG00000278419]] 0.560× (z -4.9, 23/40 lines), [[ENSG00000279838]] 0.587× (z -4.9, 19/38 lines), [[CYB5B]] 0.806× (z -4.9, 24/47 lines)

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
| 0.5 µM | — | [[C-33 A (line)]] (1.38), [[hTERT-HPNE (line)]] (1.35), [[A549 (line)]] (1.27), [[Panc 03.27 (line)]] (1.22) · weakest: [[SW 1271 (line)]] (0.429), [[SW 1088 (line)]] (0.518), [[A498 (line)]] (0.790) |
| 5 µM | — | [[SNU-423 (line)]] (1.24), [[H4 (line)]] (1.18), [[SW48 (line)]] (1.18), [[RPMI-7951 (line)]] (1.16) · weakest: [[NCI-H1573 (line)]] (0.640), [[NCI-H460 (line)]] (0.668), [[SK-MEL-2 (line)]] (0.705) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 4 next most similar without an alert.*

- [[Mozavaptan (drug)]] (+0.67, unclear); [[Eplerenone (drug)]] (+0.56, unclear, ⚠ only 4 significant genes); [[Sildenafil (drug)]] (+0.54, unclear, ⚠ only 5 significant genes); [[Roxadustat (drug)]] (+0.48, unclear); [[Pemigatinib (drug)]] (+0.46, Other TK inhibitor); [[Imiquimod (maleate) (drug)]] (+0.46, unclear); [[Uridine (drug)]] (+0.46, unclear, ⚠ only 6 significant genes); [[Docetaxel (drug)]] (+0.46, Microtubule inhibitor, ⚠ vector dose flagged: transcription drop; cell-cycle shift); [[Riluzole hydrochloride (drug)]] (+0.44, unclear); [[Pyridoxine (drug)]] (+0.39, unclear); [[Lopinavir (drug)]] (+0.38, unclear); [[Dihydroartemisinin (drug)]] (+0.36, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Bosentan (hydrate)"
- `tables/drugdoses.parquet` — dd in 209, 210, 211
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
