---
drug: "Berbamine"
type: "drug"
salt_base: "Berbamine"
targets: "CACNA1C"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 302
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Berbamine

*unclear (inhibitor/antagonist) · targets: CACNA1C · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 302 / 33 / 112; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): 0.05 µM.
> Signature similarity between consecutive doses (low–mid / mid–high): -0.03 / 0.27.

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 04]]:A4 | 74 / 228 | — | +0.35 | +3.8/+3.0/+2.0 | — |
| 0.5 µM | [[Plate 05]]:A4 | 26 / 7 | — | +0.32 | -1.2/-0.7/+0.4 | — |
| 5 µM | [[Plate 14]]:A4 | 106 / 6 | 0.828 | +0.25 | -1.0/+1.1/+0.6 | — |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (74 genes, none with an alert; 12 shown): [[PNPT1]] 1.34× (z +4.5, 22/47 lines), [[NCAPG]] 1.31× (z +4.1, 17/47 lines), [[STAT1]] 1.31× (z +4.1, 29/48 lines), [[DIAPH3]] 1.21× (z +4.0, 16/45 lines), [[TMEM19]] 1.37× (z +3.8, 14/47 lines), [[KIF15]] 1.24× (z +3.7, 8/47 lines), [[PBK]] 1.38× (z +3.6, 18/44 lines), [[H2AZ2]] 1.27× (z +3.5, 20/48 lines), [[CENPN]] 1.26× (z +3.5, 14/47 lines), [[KIF23]] 1.25× (z +3.5, 19/47 lines), [[FAM111B]] 1.50× (z +3.5, 9/38 lines), [[DMAC2L]] 1.23× (z +3.4, 4/47 lines)

**0.5 µM** (26 genes, none with an alert; 12 shown): [[DHCR7]] 1.73× (z +5.6, 27/42 lines), [[SCD]] 1.49× (z +5.6, 36/48 lines), [[HMGCR]] 1.47× (z +5.6, 31/48 lines), [[MSMO1]] 1.62× (z +5.2, 30/47 lines), [[FASN]] 1.66× (z +5.0, 36/47 lines), [[FDFT1]] 1.43× (z +4.9, 33/47 lines), [[DHCR24]] 1.43× (z +4.6, 21/44 lines), [[FADS2]] 1.31× (z +4.6, 21/48 lines), [[HMGCS1]] 1.44× (z +4.4, 26/47 lines), [[ACSS2]] 1.32× (z +4.4, 22/47 lines), [[IDI1]] 1.37× (z +4.2, 27/48 lines), [[ACAT2]] 1.32× (z +4.1, 19/48 lines)

**5 µM** (106 genes, none with an alert; 12 shown): [[HMGCR]] 2.60× (z +19.5, 48/49 lines), [[MSMO1]] 3.60× (z +19.4, 45/48 lines), [[SCD]] 2.52× (z +18.5, 48/49 lines), [[IDI1]] 2.66× (z +18.4, 45/49 lines), [[CYP51A1]] 2.27× (z +18.2, 47/48 lines), [[ACSS2]] 2.22× (z +17.8, 45/48 lines), [[HMGCS1]] 2.76× (z +17.6, 46/48 lines), [[LPIN1]] 1.71× (z +17.1, 43/49 lines), [[FDPS]] 2.59× (z +16.8, 47/49 lines), [[FDFT1]] 2.34× (z +16.4, 45/48 lines), [[DHCR7]] 3.02× (z +16.1, 42/44 lines), [[ACAT2]] 2.03× (z +15.0, 46/48 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (228 genes, none with an alert; 12 shown): [[ENSG00000257759]] 0.660× (z -5.8, 30/47 lines), [[CBLB]] 0.727× (z -5.3, 33/47 lines), [[SLC15A2]] 0.574× (z -5.3, 24/44 lines), [[ENSG00000284697]] 0.571× (z -5.3, 29/48 lines), [[TNFRSF11A]] 0.697× (z -5.3, 18/39 lines), [[LINC00598]] 0.736× (z -5.0, 21/43 lines), [[ADCY10]] 0.566× (z -5.0, 17/45 lines), [[GPC5]] 0.553× (z -5.0, 19/40 lines), [[EIF2AK3]] 0.675× (z -4.9, 37/48 lines), [[DNAJC25]] 0.655× (z -4.8, 35/48 lines), [[PLAG1]] 0.765× (z -4.8, 16/39 lines), [[CNNM2]] 0.733× (z -4.8, 34/48 lines)

**0.5 µM** (7 genes, none with an alert): [[ENSG00000279598]] 0.604× (z -5.0, 17/39 lines), [[NOTCH2NLB]] 0.642× (z -4.7, 19/42 lines), [[ENSG00000290835]] 0.798× (z -3.9, 16/48 lines), [[H4C3]] 0.532× (z -3.8, 35/48 lines), [[ENSG00000260796]] 0.654× (z -3.8, 12/39 lines), [[POLR2J3-1]] 0.715× (z -3.5, 11/43 lines), [[GTF2IP4]] 0.748× (z -3.4, 9/40 lines)

**5 µM** (6 genes, none with an alert): [[MT-ND4]] 0.725× (z -4.6, 41/49 lines), [[ENSG00000285043]] 0.773× (z -3.7, 9/45 lines), [[MT-CO1]] 0.807× (z -3.6, 31/49 lines), [[CGREF1]] 0.825× (z -3.3, 8/37 lines), [[KCNQ4]] 0.826× (z -3.2, 3/39 lines), [[ELFN2]] 0.809× (z -3.2, 8/28 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | [[Module 004]] (+2.6), [[Module 016]] (+2.1) | [[Module 179]] (-3.5), [[Module 041]] (-3.3), [[Module 207]] (-3.2) |
| 0.5 µM | [[Module 086]] (+2.9) | — |
| 5 µM | [[Module 086]] (+10.8) | [[Module 170]] (-2.6) |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[SW 1088 (line)]] (1.82), [[LS 180 (line)]] (1.60), [[H4 (line)]] (1.48), [[NCI-H1573 (line)]] (1.43) · weakest: [[BT-474 (line)]] (0.424), [[NCI-H2347 (line)]] (0.475), [[AsPC-1 (line)]] (0.538) |
| 0.5 µM | — | [[LS 180 (line)]] (2.40), [[LoVo (line)]] (2.02), [[HT-29 (line)]] (1.88), [[SNU-1 (line)]] (1.76) · weakest: [[A498 (line)]] (0.455), [[NCI-H1573 (line)]] (0.471), [[RKO (line)]] (0.492) |
| 5 µM | — | [[LoVo (line)]] (1.72), [[A549 (line)]] (1.67), [[HOP62 (line)]] (1.58), [[LS 180 (line)]] (1.57) · weakest: [[SHP-77 (line)]] (0.181), [[NCI-H661 (line)]] (0.377), [[A-427 (line)]] (0.447) |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

*378 other drugs have a vector, 122 with an alert ⚠; shown: the 8 most similar and the 1 next most similar without an alert.*

- [[Palmatine (chloride) (drug)]] (+0.90, unclear); [[Retinoic acid (drug)]] (+0.90, Retinoic receptor agonist); [[Megestrol (drug)]] (+0.88, unclear, ⚠ vector dose flagged: cell-cycle shift); [[Diammonium Glycyrrhizinate (drug)]] (+0.87, unclear); [[Busulfan (drug)]] (+0.85, DNA synthesis/repair inhibitor); [[Gallic acid (hydrate) (drug)]] (+0.83, Cyclooxygenase inhibitor); [[Larotrectinib (drug)]] (+0.80, Other TK inhibitor); [[(R)-Verapamil (hydrochloride) (drug)]] (+0.80, unclear); [[Pyridoxine (hydrochloride) (drug)]] (+0.65, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Berbamine"
- `tables/drugdoses.parquet` — dd in 167, 168, 169
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
