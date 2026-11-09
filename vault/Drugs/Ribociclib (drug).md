---
drug: "Ribociclib"
type: "drug"
salt_base: "Ribociclib"
targets: "CDK4, CDK6"
moa_fine: "CDK inhibitor"
moa_broad: "inhibitor/antagonist"
approved: "yes"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 433
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Ribociclib

*CDK inhibitor (inhibitor/antagonist) · targets: CDK4, CDK6 · approved: yes*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 433 / 15 / 0; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.29 / 0.27.
> Flags by dose: unreliable plate only; position not correctable / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; position not correctable; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H12 | 146 / 287 | — | +0.11 | +0.4/-0.4/+0.4 | ⚠ unreliable plate only; position not correctable |
| 0.5 µM | [[Plate 13]]:G12 | 8 / 7 | — | -0.09 | +1.0/+0.7/+1.3 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F12 | 0 / 0 | — | +0.13 | +0.0/-0.1/+0.6 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (146 genes, 146 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; position not correctable; 12 shown): [[ENSG00000289177]] ⚠ 2.64× (z +9.4, 32/42 lines), [[MT-CO3]] ⚠ 2.25× (z +8.4, 47/49 lines), [[RAB1B]] ⚠ 1.48× (z +7.2, 39/48 lines), [[GM2A]] ⚠ 1.61× (z +7.0, 33/48 lines), [[WDR55]] ⚠ 1.45× (z +6.6, 31/47 lines), [[ENSG00000289901]] ⚠ 3.94× (z +6.6, 46/47 lines), [[GTF3C2-AS2]] ⚠ 1.73× (z +6.5, 22/47 lines), [[POLR2J3]] ⚠ 1.92× (z +6.3, 26/47 lines), [[H3C6]] ⚠ 1.97× (z +6.3, 17/38 lines), [[TSPAN31]] ⚠ 1.48× (z +6.2, 26/45 lines), [[UBE2I]] ⚠ 1.32× (z +6.2, 40/49 lines), [[DLGAP4-AS1]] ⚠ 1.60× (z +6.1, 19/47 lines)

**0.5 µM** (8 genes, 8 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[ZNF618]] ⚠ 1.29× (z +3.4, 9/39 lines), [[CRYZL2P]] ⚠ 1.39× (z +3.2, 4/34 lines), [[TGFBR3]] ⚠ 1.21× (z +3.2, 5/42 lines), [[SAMHD1]] ⚠ 1.28× (z +3.1, 13/45 lines), [[IQGAP2]] ⚠ 1.22× (z +3.0, 1/22 lines), [[ADAM22]] ⚠ 1.20× (z +2.9, 3/36 lines), [[ZNF738]] ⚠ 1.23× (z +2.9, 1/38 lines), [[DENND2B]] ⚠ 1.20× (z +2.8, 1/42 lines)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (287 genes, 287 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; position not correctable; 12 shown): [[ENSG00000217801]] ⚠ 0.405× (z -7.8, 30/41 lines), [[RPS18]] ⚠ 0.499× (z -7.7, 48/48 lines), [[RPL3]] ⚠ 0.521× (z -7.3, 47/49 lines), [[POLR2J3-1]] ⚠ 0.503× (z -7.2, 29/45 lines), [[PET100]] ⚠ 0.467× (z -6.9, 25/45 lines), [[TNKS1BP1]] ⚠ 0.584× (z -6.8, 45/48 lines), [[NFE2L1]] ⚠ 0.670× (z -6.8, 46/49 lines), [[ASMTL-AS1]] ⚠ 0.457× (z -6.6, 41/47 lines), [[RALB]] ⚠ 0.745× (z -6.5, 39/48 lines), [[ENSG00000230021]] ⚠ 0.618× (z -6.3, 35/48 lines), [[MT-ND6]] ⚠ 0.545× (z -6.2, 44/49 lines), [[ENSG00000283765]] ⚠ 0.505× (z -6.0, 22/44 lines)

**0.5 µM** (7 genes, 7 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[ALS2CL]] ⚠ 0.774× (z -3.4, 5/34 lines), [[FAM110C]] ⚠ 0.774× (z -3.3, 3/22 lines), [[ADAMTS16]] ⚠ 0.830× (z -3.1, 0/23 lines), [[ENSG00000286511]] ⚠ 0.751× (z -3.1, 7/41 lines), [[ARRDC2]] ⚠ 0.821× (z -3.0, 3/48 lines), [[ZNF185]] ⚠ 0.815× (z -3.0, 4/33 lines), [[FAM83G]] ⚠ 0.781× (z -2.9, 5/41 lines)

## Modules it moves

*Mean pooled z of a module's + arm minus its − arm, or of its genes in a single-armed module (`graph/module_pooled_z.npy`); shown when |z| ≥ 2. Raising a module = its + arm up and its − arm down (its genes up, in a single-armed module).*

| Dose | Raises | Lowers |
|---|---|---|
| 0.05 µM | — | [[Module 173]] (-2.2), [[Module 138]] (-2.1) |
| 0.5 µM | — | [[Module 170]] (-2.1) |
| 5 µM | — | — |

## In which cell lines

*Depleted = the line's relative abundance z ≤ −3 (`atlas/effects/DD_Az.npy`: the drug kills or stops that line more than the others). Response strength β = slope of the line's changes on the drug-dose's consensus over its significant genes (`DD_beta.npy`; 1 = typical line, 0 = no response; drug-doses with ≥ 20 significant genes).*

| Dose | Most depleted lines (Az) | Strongest responders (β) |
|---|---|---|
| 0.05 µM | — | [[NCI-H1792 (line)]] (1.14), [[NCI-H460 (line)]] (1.11), [[CHP-212 (line)]] (1.09), [[COLO 205 (line)]] (1.09) · weakest: [[NCI-H2122 (line)]] (0.493), [[SW 1088 (line)]] (0.703), [[AN3 CA (line)]] (0.926) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 2 next most similar without an alert.*

- [[Carbidopa (monohydrate) (drug)]] (+0.75, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only; position not correctable)); [[Doxycycline (monohydrate) (drug)]] (+0.71, unclear); [[Bisoprolol (hemifumarate) (drug)]] (+0.57, Adrenoceptor agonist); [[Atazanavir (sulfate) (drug)]] (+0.57, unclear); [[Loperamide (hydrochloride) (drug)]] (+0.52, unclear); [[Ivabradine (hydrochloride) (drug)]] (+0.51, unclear, ⚠ no trustworthy dose (vector dose flagged: unreliable plate only)); [[Gallic acid (hydrate) (drug)]] (+0.44, Cyclooxygenase inhibitor); [[Arbutin (drug)]] (+0.44, unclear); [[Valdecoxib (drug)]] (+0.43, Cyclooxygenase inhibitor); [[Rosiglitazone (drug)]] (+0.40, unclear)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Ribociclib"
- `tables/drugdoses.parquet` — dd in 890, 891, 892
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
