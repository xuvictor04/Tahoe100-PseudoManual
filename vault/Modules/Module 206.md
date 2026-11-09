---
module: 206
type: "module"
n_genes: 15
n_plus: 15
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Constitutive Signaling by Aberrant PI3K in Cancer"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 206

*Constitutive Signaling by Aberrant PI3K in Cancer · 15 genes (single-armed) · [[Module 206.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Constitutive Signaling by Aberrant PI3K in Cancer** (reactome, q 0.012; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Constitutive Signaling by Aberrant PI3K in Cancer | reactome | 3/15 | 48.6 | 0.012 |
| + | Constitutive Signaling by Aberrant PI3K in Cancer | reactome | 3/15 | 48.6 | 0.012 |
| all | PI5P, PP2A and IER3 Regulate PI3K/AKT Signaling | reactome | 3/15 | 33.9 | 0.032 |
| all | PI3K/AKT Signaling in Cancer | reactome | 3/15 | 33.9 | 0.032 |
| + | PI5P, PP2A and IER3 Regulate PI3K/AKT Signaling | reactome | 3/15 | 33.9 | 0.032 |
| + | PI3K/AKT Signaling in Cancer | reactome | 3/15 | 33.9 | 0.032 |
| all | Negative regulation of the PI3K/AKT network | reactome | 3/15 | 31.4 | 0.039 |
| + | Negative regulation of the PI3K/AKT network | reactome | 3/15 | 31.4 | 0.039 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 205), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+12.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+6.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.7); [[Tucidinostat (drug)]] 0.5 µM (+3.2, ⚠ cell-cycle shift); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.5); [[Harringtonine (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.2); [[Daptomycin (drug)]] 5 µM (+2.2, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (+1.9); [[Peretinoin (drug)]] 0.5 µM (+1.9); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+1.9); [[vincristine (drug)]] 0.5 µM (+1.5); [[9-ING-41 (drug)]] 0.5 µM (+1.5); [[Vilanterol (drug)]] 0.5 µM (+1.4); [[Auranofin (drug)]] 5 µM (+1.4) (35 in all, 14 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Selinexor (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.9); [[Trametinib (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.05 µM (-2.7); [[Trametinib (drug)]] 0.05 µM (-2.7); [[Clobetasol propionate (drug)]] 5 µM (-2.7); [[Binimetinib (drug)]] 0.05 µM (-2.5); [[Trametinib (drug)]] 0.5 µM (-2.4); [[Binimetinib (drug)]] 0.5 µM (-2.4); [[Clobetasol propionate (drug)]] 0.5 µM (-2.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.3); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-2.1) (51 in all, 9 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-172 (line)]], [[A498 (line)]], [[SNU-423 (line)]], [[HOP62 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H460 (line)]], [[NCI-H1573 (line)]]

## + arm (15)

| Gene | Projection | Name |
|---|---|---|
| [[N4BP3]] | 0.878 | NEDD4 binding protein 3 |
| [[PDGFB]] | 0.782 | platelet derived growth factor subunit B |
| [[DRAP1]] | 0.780 | DR1 associated protein 1 |
| [[HMGA1]] | 0.755 | high mobility group AT-hook 1 |
| [[PIK3CD]] | 0.750 | phosphatidylinositol-4,5-bisphosphate 3-kinase catalytic subunit delta |
| [[CYTH4]] | 0.741 | cytohesin 4 |
| [[PDGFA]] | 0.701 | platelet derived growth factor subunit A |
| [[DOT1L]] | 0.647 | DOT1 like histone lysine methyltransferase |
| [[MEAK7]] | 0.641 | MTOR associated protein MEAK7 |
| [[PRR7]] | 0.616 | proline rich 7, synaptic |
| [[RARA]] | 0.614 | retinoic acid receptor alpha |
| [[FIBP]] | 0.554 | FGF1 intracellular binding protein |
| [[SNX9]] | 0.535 | sorting nexin 9 |
| [[BACH2]] | 0.471 | BACH transcriptional regulator 2 |
| [[LBH]] | 0.415 | LBH regulator of Wnt signaling pathway |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 206; `graph/modules.parquet` — module == 206; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [205] (drug-dose × line)
