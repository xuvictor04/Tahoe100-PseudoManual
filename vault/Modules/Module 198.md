---
module: 198
type: "module"
n_genes: 16
n_plus: 16
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.40540674328804016
label: "Antigen processing: Ubiquitination & Proteasome degradation"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 198

*Antigen processing: Ubiquitination & Proteasome degradation · 16 genes (single-armed) · [[Module 198.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Antigen processing: Ubiquitination & Proteasome degradation** (reactome, q 0.003; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Antigen processing: Ubiquitination & Proteasome degradation | reactome | 5/16 | 17.4 | 0.003 |
| + | Antigen processing: Ubiquitination & Proteasome degradation | reactome | 5/16 | 17.4 | 0.003 |
| all | Class I MHC mediated antigen processing & presentation | reactome | 5/16 | 13.9 | 0.009 |
| + | Class I MHC mediated antigen processing & presentation | reactome | 5/16 | 13.9 | 0.009 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 197), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM (+4.1, ⚠ toxic; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+2.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+2.2); [[Harringtonine (drug)]] 5 µM (+2.1, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (+1.6); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.5); [[PH-797804 (drug)]] 5 µM (+1.5); [[Radotinib (drug)]] 5 µM (+1.4); [[Verteporfin (drug)]] 5 µM (+1.2); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.1); [[Pasireotide (acetate) (drug)]] 5 µM (+1.1); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.1); [[Terfenadine (drug)]] 5 µM (+1.0) (24 in all, 14 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-2.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (-2.2); [[Dinaciclib (drug)]] 5 µM (-2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-1.5, ⚠ toxic; transcription drop; cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (-1.4); [[Demeclocycline (drug)]] 5 µM (-1.4); [[Omeprazole (drug)]] 0.05 µM (-1.3); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (-1.3); [[Estrone sulfate (potassium) (drug)]] 5 µM (-1.2); [[Busulfan (drug)]] 0.05 µM (-1.2); [[(S)-Crizotinib (drug)]] 0.5 µM (-1.2); [[Diphenhydramine (drug)]] 0.5 µM (-1.2); [[Retinoic acid (drug)]] 0.05 µM (-1.1) (26 in all, 6 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[SW480 (line)]], [[RKO (line)]], [[BT-474 (line)]], [[NCI-H2030 (line)]], [[LoVo (line)]], [[HEC-1-A (line)]], [[HT-29 (line)]]

## + arm (16)

| Gene | Projection | Name |
|---|---|---|
| [[RWDD3]] | 0.846 | RWD domain containing 3 |
| [[FBXO9]] | 0.819 | F-box protein 9 |
| [[XPA]] | 0.788 | XPA, DNA damage recognition and repair factor |
| [[RCHY1]] | 0.777 | ring finger and CHY zinc finger domain containing 1 |
| [[UBA3]] | 0.763 | ubiquitin like modifier activating enzyme 3 |
| [[MORN4]] | 0.746 | MORN repeat containing 4 |
| [[DTWD1]] | 0.742 | DTW motif tRNA-uridine aminocarboxypropyltransferase 1 |
| [[SPATA5L1]] | 0.726 | AAA ATPase AFG2B |
| [[MTFMT]] | 0.720 | mitochondrial methionyl-tRNA formyltransferase |
| [[ANKRD13C]] | 0.702 | ankyrin repeat domain 13C |
| [[FBXL5]] | 0.670 | F-box and leucine rich repeat protein 5 |
| [[CLPX]] | 0.669 | caseinolytic mitochondrial matrix peptidase chaperone subunit X |
| [[ETF1]] | -0.629 | eukaryotic translation termination factor 1 |
| [[GNPAT]] | 0.608 | glyceronephosphate O-acyltransferase |
| [[RELT]] | -0.581 | RELT TNF receptor |
| [[UBR4]] | -0.550 | ubiquitin protein ligase E3 component n-recognin 4 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 198; `graph/modules.parquet` — module == 198; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [197] (drug-dose × line)
