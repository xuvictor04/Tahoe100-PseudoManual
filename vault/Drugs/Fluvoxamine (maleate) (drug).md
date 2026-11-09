---
drug: "Fluvoxamine (maleate)"
type: "drug"
salt_base: "Fluvoxamine"
targets: ""
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.5"
max_sig_genes: 23
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Fluvoxamine (maleate)

*unclear (inhibitor/antagonist) · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 7 / 23 / 15; best dose 0.5 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.55 / 0.53.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:C10 | 2 / 5 | — | -0.26 | -0.3/+0.2/+1.1 | — |
| 0.5 µM | [[Plate 05]]:C10 | 10 / 13 | — | -0.49 | +0.0/+0.1/+1.1 | — |
| 5 µM | [[Plate 14]]:C10 | 10 / 5 | 0.809 | -0.04 | -0.9/+0.0/+1.1 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (2 genes, none with an alert): [[ENSG00000267175]] 1.37× (z +3.0, 1/25 lines), [[ENSG00000266573]] 1.53× (z +2.8, 0/7 lines)

**0.5 µM** (10 genes, none with an alert): [[BEST1]] 1.45× (z +3.6, 19/44 lines), [[EAF2]] 1.38× (z +3.5, 18/45 lines), [[PRKCA-AS1]] 1.42× (z +3.3, 7/37 lines), [[GALNT3]] 1.21× (z +3.3, 12/18 lines), [[LINC00888]] 1.45× (z +3.3, 5/28 lines), [[ENSG00000288025]] 1.31× (z +3.0, 12/44 lines), [[LIN7A]] 1.30× (z +3.0, 2/11 lines), [[GALNT13]] 1.21× (z +3.0, 3/17 lines), [[ZNF57]] 1.25× (z +3.0, 4/40 lines), [[LAMA1]] 1.26× (z +2.7, 1/16 lines)

**5 µM** (10 genes, none with an alert): [[RABGGTA]] 1.22× (z +3.2, 1/44 lines), [[ISYNA1]] 1.21× (z +3.2, 4/41 lines), [[SEMA4A]] 1.43× (z +3.1, 11/39 lines), [[SLC31A1]] 1.21× (z +3.1, 21/48 lines), [[ENSG00000283573]] 1.57× (z +3.0, 13/39 lines), [[FNDC7]] 1.45× (z +3.0, 8/42 lines), [[ENSG00000288000]] 1.29× (z +3.0, 16/48 lines), [[EFCAB12]] 1.33× (z +3.0, 5/42 lines), [[RRP12]] 1.23× (z +3.0, 19/48 lines), [[INSIG1]] 1.23× (z +2.9, 15/47 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (5 genes, none with an alert): [[KLHL2P1]] 0.689× (z -3.6, 5/37 lines), [[PCLO]] 0.831× (z -3.0, 7/33 lines), [[ENSG00000247134]] 0.811× (z -3.0, 6/26 lines), [[PPP1R3E]] 0.810× (z -2.9, 10/46 lines), [[HOXD3]] 0.799× (z -2.9, 6/29 lines)

**0.5 µM** (13 genes, none with an alert; 12 shown): [[ENSG00000249258]] 0.647× (z -3.8, 9/25 lines), [[CYB5D2]] 0.808× (z -3.8, 15/47 lines), [[ZNF19]] 0.715× (z -3.6, 9/41 lines), [[ENSG00000286681]] 0.693× (z -3.5, 12/39 lines), [[SETMAR]] 0.720× (z -3.3, 7/35 lines), [[SYCP2]] 0.801× (z -3.3, 10/31 lines), [[CYP27A1]] 0.809× (z -3.2, 3/34 lines), [[ENTPD3-AS1]] 0.726× (z -3.2, 12/46 lines), [[TLCD2]] 0.777× (z -3.1, 8/46 lines), [[STON1]] 0.786× (z -3.1, 9/46 lines), [[ZNF493]] 0.802× (z -3.1, 15/40 lines), [[CYP27C1]] 0.809× (z -2.8, 4/27 lines)

**5 µM** (5 genes, none with an alert): [[ENSG00000259275]] 0.748× (z -3.5, 6/41 lines), [[ZNF19]] 0.809× (z -3.2, 6/45 lines), [[ENSG00000227627]] 0.824× (z -3.0, 7/45 lines), [[PDCL3P4]] 0.816× (z -3.0, 8/48 lines), [[ENSG00000224658]] 0.815× (z -2.9, 5/40 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | [[Module 041]] (+2.0) | — |
| 5 µM | [[Module 041]] (+2.6) | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | — |
| 0.5 µM | — | [[CFPAC-1 (line)]] (1.64), [[SW 1088 (line)]] (1.63), [[HepG2_C3A (line)]] (1.62), [[Hs 766T (line)]] (1.49) · weakest: [[C32 (line)]] (0.191), [[SNU-1 (line)]] (0.200), [[SK-MEL-2 (line)]] (0.352) |
| 5 µM | [[A-172 (line)]] (-3.2) | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 3 next most similar without an alert.*

- [[Silodosin (drug)]] (+0.63, unclear); [[Altretamine (drug)]] (+0.62, DNA synthesis/repair inhibitor, ⚠ only 1 significant gene); [[Pimitespib (drug)]] (+0.59, unclear); [[Hesperidin (drug)]] (+0.56, unclear); [[Vortioxetine (drug)]] (+0.56, unclear, ⚠ vector dose flagged: toxic); [[Sacubitril_Valsartan (drug)]] (+0.55, unclear, ⚠ only 1 significant gene); [[Pemigatinib (drug)]] (+0.55, Other TK inhibitor); [[Terfenadine (drug)]] (+0.55, unclear); [[Tazarotene (drug)]] (+0.53, Retinoic receptor agonist); [[Allopurinol (drug)]] (+0.51, unclear); [[Quinidine (15% dihydroquinidine) (drug)]] (+0.50, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Fluvoxamine (maleate)"
- `tables/drugdoses.parquet` — dd in 465, 466, 467
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
