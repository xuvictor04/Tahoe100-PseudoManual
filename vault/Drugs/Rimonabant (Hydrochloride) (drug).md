---
drug: "Rimonabant (Hydrochloride)"
type: "drug"
salt_base: "Rimonabant"
targets: "CNR1"
moa_fine: "unclear"
moa_broad: "inhibitor/antagonist"
approved: "no"
doses: ["0.05", "0.5", "5"]
best_dose: "0.05"
max_sig_genes: 23
tags: ["drug", "moa/inhibitor_antagonist"]
generated_by: "tahoemap"
---

# Rimonabant (Hydrochloride)

*unclear (inhibitor/antagonist) · targets: CNR1 · approved: no*

> [!summary] At a glance
> Significant genes by dose (0.05 µM / 0.5 µM / 5 µM): 23 / 1 / 1; best dose 0.05 µM; lowest active dose (it and every higher dose with ≥ 10 significant genes): low dose only (noise?).
> Signature similarity between consecutive doses (low–mid / mid–high): 0.15 / 0.17.
> Flags by dose: unreliable plate only / unreliable plate only / unreliable plate only. ⚠ 0.05 µM: unreliable plate only; 0.5 µM: unreliable plate only; 5 µM: unreliable plate only (artifact flags: its changes there are shown with an alert, not left out).

## Doses

*`tables/drugdoses.parquet`. Sig. genes = raised / lowered significantly (q < 0.10, ≥ 1.2×). Cells = log2 cells per well vs the plate's median drug well. S / G2M / proteasome = module z (cell-cycle mix and proteasome load). Flags: ⚠ = artifact flags (the changes may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem); after · the soft caveats. A `cell-cycle shift` is weighed per gene: the gene lists below say for which genes it explains the change.*

| Dose | Wells | Sig. genes up / down | Replicate r | Cells (log2) | S / G2M / prot. z | Flags |
|---|---|---|---|---|---|---|
| 0.05 µM | [[Plate 13]]:H10 | 19 / 4 | — | +0.10 | +0.7/-0.4/+0.4 | ⚠ unreliable plate only |
| 0.5 µM | [[Plate 13]]:G10 | 0 / 1 | — | -0.72 | +0.8/-0.5/+0.2 | ⚠ unreliable plate only |
| 5 µM | [[Plate 13]]:F10 | 0 / 1 | — | +0.19 | +1.3/+1.0/+0.8 | ⚠ unreliable plate only |

## Genes it raises

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (19 genes, 19 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only; 12 shown): [[RN7SKP71]] ⚠ 31.3× (z +12.8, 47/47 lines; unreliable plate only; position correction uncertain), [[CSNK2A2]] ⚠ 1.25× (z +6.8, 36/49 lines; unreliable plate only; position correction uncertain), [[ENSG00000290823]] ⚠ 2.02× (z +6.7, 21/43 lines; unreliable plate only; position correction uncertain), [[ALG2]] ⚠ 1.65× (z +6.6, 39/48 lines; unreliable plate only; position correction uncertain), [[BMS1P2]] ⚠ 1.88× (z +6.2, 14/44 lines; unreliable plate only; position correction uncertain), [[GRINA]] ⚠ 1.62× (z +6.0, 40/48 lines; unreliable plate only; position correction uncertain), [[PET100]] ⚠ 1.89× (z +5.7, 24/45 lines; unreliable plate only; position correction uncertain), [[CNPY3]] ⚠ 1.33× (z +5.5, 17/48 lines; unreliable plate only; position correction uncertain), [[ATP2C2-AS1]] ⚠ 1.67× (z +5.4, 17/43 lines; unreliable plate only; position correction uncertain), [[ENSG00000273014]] ⚠ 1.66× (z +5.2, 5/42 lines; unreliable plate only; position correction uncertain), [[VDAC2]] ⚠ 1.32× (z +5.0, 33/49 lines; unreliable plate only; position correction uncertain), [[AGPAT3]] ⚠ 1.21× (z +4.8, 24/49 lines; unreliable plate only; position correction uncertain)

## Genes it lowers

*Per dose, the significant genes with the largest |z| (`tables/drug_effects.parquet`, dd == the row of the dose): the 12 strongest, and any of the 12 strongest without an alert below them. ⚠ = an artifact flag on the drug-dose or on the gene: shown, not left out; its reasons are the dose's own alert, named once after the dose, unless they are given in the gene's brackets. For a `cell-cycle shift` each gene says how much of its change the shift explains; a gene without the alert at such a dose is one whose change the shift does not explain.*

**0.05 µM** (4 genes, 4 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[ENSG00000255422]] ⚠ 0.658× (z -5.1, 22/47 lines; unreliable plate only; position correction uncertain), [[ENSG00000271204]] ⚠ 0.760× (z -4.5, 16/43 lines; unreliable plate only; position correction uncertain), [[GRIPAP1]] ⚠ 0.814× (z -4.4, 25/48 lines; unreliable plate only; position correction uncertain), [[ENSG00000258757]] ⚠ 0.590× (z -4.3, 23/47 lines; unreliable plate only; position correction uncertain)

**0.5 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[ENSG00000259124]] ⚠ 0.652× (z -4.0, 8/42 lines)

**5 µM** (1 gene, 1 with an alert ⚠; the drug-dose carries ⚠ unreliable plate only): [[C9orf153]] ⚠ 0.805× (z -3.0, 2/47 lines)

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
| 0.05 µM | — | [[Panc 03.27 (line)]] (1.05), [[SW 900 (line)]] (1.05), [[A-427 (line)]] (1.05), [[MIA PaCa-2 (line)]] (1.04) · weakest: [[SW 1088 (line)]] (0.517), [[NCI-H2122 (line)]] (0.714), [[SW 1271 (line)]] (0.807) |
| 0.5 µM | — | — |
| 5 µM | — | — |

## Nearest drugs in the vector space

*Cosine of the drug vectors (each drug's most active dose projected into the gene vector space; `embed/drug_vectors.npy`): drugs that move the same genes the same way. Every drug with a vector is ranked; ⚠ = its vector rests on fewer than the space's 10 significant genes, or on a dose with an artifact flag or none trustworthy (`embed/drugs.parquet` alert); such a drug keeps its place.*

⚠ This drug's own vector: no trustworthy dose (vector dose flagged: unreliable plate only). Read its neighbours with that in mind.

*378 other drugs have a vector, 121 with an alert ⚠; shown: the 8 most similar and the 5 next most similar without an alert.*

- [[Imiquimod (hydrochloride) (drug)]] (+0.63, unclear, ⚠ vector dose flagged: toxic); [[Cysteamine (hydrochloride) (drug)]] (+0.61, unclear); [[Lidocaine (hydrochloride) (drug)]] (+0.60, unclear); [[Talc (drug)]] (+0.55, unclear, ⚠ only 7 significant genes); [[Ataluren (drug)]] (+0.55, unclear, ⚠ only 7 significant genes); [[Fostamatinib (disodium hexahydrate) (drug)]] (+0.53, Other TK inhibitor, ⚠ only 3 significant genes; no trustworthy dose (vector dose flagged: unreliable plate only)); [[Clofarabine (drug)]] (+0.53, DNA synthesis/repair inhibitor, ⚠ only 8 significant genes); [[Benztropine (mesylate) (drug)]] (+0.48, unclear); [[Verteporfin (drug)]] (+0.48, unclear); [[Elagolix sodium (drug)]] (+0.47, unclear); [[Monocrotaline (drug)]] (+0.47, unclear); [[Vitamin K4 (drug)]] (+0.45, unclear); [[Decitabine (drug)]] (+0.42, DNA methyltransferase inhibitor)

## Direction (probable)

No arrow involves this drug in this run: no gene was found to set how the cells fare under it, and it is not one of the compounds of a drug-target arrow (how the arrows are made: [[Probable direction]]).

## Data

- `tables/drugs.parquet` — drug == "Rimonabant (Hydrochloride)"
- `tables/drugdoses.parquet` — dd in 902, 903, 904
- `tables/drug_effects.parquet` — rows with dd in those rows; `atlas/effects/DD_*.npy` — those rows
- `embed/drugdose_vectors.npy` — those rows
- `direction/edges.parquet` — target_dd in those rows; drug_target rows whose compounds include it
