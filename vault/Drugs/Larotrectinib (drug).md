---
drug: "Larotrectinib"
type: "drug"
salt_base: "Larotrectinib"
targets: "NTRK1, NTRK2, NTRK3"
moa_fine: "Other TK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 97
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Larotrectinib

*Other TK inhibitor (inhibitor/antagonist) · targets: NTRK1, NTRK2, NTRK3 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 97 / 6 / 94; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 5 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): 0.27 / 0.28.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:E9 | 19 / 78 | — | +0.31 | +1.4/+1.9/+0.5 | — |
| 0.5 µM | [[Plate 05]]:E9 | 4 / 2 | — | -0.14 | -0.9/+0.0/-0.4 | — |
| 5 µM | [[Plate 14]]:E9 | 31 / 63 | 0.785 | -0.88 | +0.8/-0.4/+0.0 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, none with an alert; 12 shown): [[TNC]] 1.39× (z +3.8, 5/26 lines), [[FHL2]] 1.22× (z +3.7, 11/45 lines), [[ENC1]] 1.43× (z +3.5, 13/43 lines), [[CHML]] 1.20× (z +3.5, 8/49 lines), [[NTN4]] 1.42× (z +3.4, 7/31 lines), [[ZNF281]] 1.22× (z +3.3, 12/49 lines), [[ENSG00000285016]] 1.34× (z +3.3, 24/48 lines), [[C6orf47]] 1.34× (z +3.2, 2/47 lines), [[ASPM]] 1.25× (z +3.2, 14/48 lines), [[DCBLD2]] 1.23× (z +3.1, 16/40 lines), [[DKK1]] 1.45× (z +3.0, 4/28 lines), [[NEGR1]] 1.20× (z +2.9, 0/24 lines)

**0.5 µM** (4 genes, none with an alert): [[P4HB]] 1.38× (z +4.4, 42/49 lines), [[ZYG11A]] 1.26× (z +3.1, 0/18 lines), [[DENND2A]] 1.23× (z +3.0, 0/24 lines), [[FGFRL1]] 1.32× (z +3.0, 5/45 lines)

**5 µM** (31 genes, none with an alert; 12 shown): [[DNAJC14]] 1.21× (z +3.9, 10/48 lines), [[H2BC6]] 1.29× (z +3.8, 4/48 lines), [[MSRB1]] 1.42× (z +3.7, 7/44 lines), [[KRBA2]] 1.23× (z +3.7, 7/48 lines), [[B3GALT9]] 1.35× (z +3.6, 3/40 lines), [[ZNF512B]] 1.27× (z +3.5, 9/38 lines), [[ZNF667]] 1.33× (z +3.5, 0/13 lines), [[KPTN]] 1.25× (z +3.4, 3/44 lines), [[ENSG00000280128]] 1.27× (z +3.4, 5/46 lines), [[DTX3L]] 1.25× (z +3.4, 20/45 lines), [[OAS2]] 1.36× (z +3.4, 20/34 lines), [[IFI44]] 1.21× (z +3.3, 13/36 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (78 genes, none with an alert; 12 shown): [[DNAJC25]] 0.678× (z -4.4, 32/49 lines), [[SRP54-AS1]] 0.697× (z -4.2, 30/48 lines), [[ELP2]] 0.741× (z -4.1, 37/49 lines), [[DGKE]] 0.790× (z -4.1, 16/36 lines), [[NFXL1]] 0.778× (z -4.1, 28/49 lines), [[GOLPH3L]] 0.794× (z -4.0, 25/48 lines), [[FBXO42]] 0.768× (z -4.0, 30/49 lines), [[LINC01881]] 0.746× (z -3.9, 15/48 lines), [[PREPL]] 0.783× (z -3.9, 29/49 lines), [[UBE2O]] 0.784× (z -3.9, 27/49 lines), [[JMY]] 0.786× (z -3.9, 22/48 lines), [[TMEM185A]] 0.770× (z -3.8, 14/48 lines)

**0.5 µM** (2 genes, none with an alert): [[LCP1]] 0.772× (z -3.2, 7/15 lines), [[CASC19]] 0.813× (z -2.8, 13/21 lines)

**5 µM** (63 genes, none with an alert; 12 shown): [[ZEB2]] 0.806× (z -5.3, 17/21 lines), [[ENSG00000230021]] 0.757× (z -5.2, 28/48 lines), [[EPB41L4A]] 0.813× (z -5.0, 18/22 lines), [[GRHL2]] 0.789× (z -4.9, 14/14 lines), [[ENSG00000282278]] 0.809× (z -4.9, 15/48 lines), [[ENSG00000255476]] 0.767× (z -4.8, 16/46 lines), [[TMEM108]] 0.764× (z -4.8, 7/23 lines), [[ALDH1A1]] 0.740× (z -4.6, 10/12 lines), [[SNX32]] 0.721× (z -4.5, 19/48 lines), [[FOXO3B]] 0.790× (z -4.5, 10/44 lines), [[CDH1]] 0.817× (z -4.3, 17/17 lines), [[ENSG00000259712]] 0.748× (z -4.2, 13/46 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 207]] (-2.8), [[Module 179]] (-2.7), [[Module 171]] (-2.6) |
| 0.5 µM | — | — |
| 5 µM | [[Module 010]] (+2.2), [[Module 148]] (+2.2), [[Module 137]] (+2.2) | [[Module 207]] (-2.8) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.64), [[LS 180 (line)]] (1.42), [[NCI-H1573 (line)]] (1.40), [[H4 (line)]] (1.36) · weakest: [[BT-474 (line)]] (0.247), [[AN3 CA (line)]] (0.569), [[SK-MEL-2 (line)]] (0.578) |
| 0.5 µM | — | — |
| 5 µM | — | [[H4 (line)]] (1.29), [[NCI-H661 (line)]] (1.18), [[SW 1088 (line)]] (1.18), [[NCI-H2030 (line)]] (1.14) · weakest: [[CHP-212 (line)]] (0.462), [[HOP62 (line)]] (0.596), [[hTERT-HPNE (line)]] (0.721) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Busulfan (drug)]] (+0.94, DNA synthesis/repair inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.94, unclear); [[Palmatine (chloride) (drug)]] (+0.93, unclear); [[Megestrol (drug)]] (+0.91, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Retinoic acid (drug)]] (+0.87, Retinoic receptor agonist); [[Diphenhydramine (drug)]] (+0.85, unclear); [[Esmolol (hydrochloride) (drug)]] (+0.82, unclear); [[Berbamine (drug)]] (+0.80, unclear); [[L-Eflornithine (monohydrochloride) (drug)]] (+0.80, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Larotrectinib"
- `tables/drugdoses.parquet` — dd in 606, 607, 608
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
