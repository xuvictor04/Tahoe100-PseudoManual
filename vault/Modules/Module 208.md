---
module: 208
type: "module"
n_genes: 14
n_plus: 14
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 208

*14 genes (single-armed) · [[Module 208.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Striated Muscle Contraction | reactome | 2/14 | 135 | 0.035 |
| + | Striated Muscle Contraction | reactome | 2/14 | 135 | 0.035 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 207), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+9.3); [[Panobinostat (drug)]] 0.5 µM (+8.0, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+7.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+7.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+5.6, ⚠ cell-cycle shift); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (+4.5); [[Pitavastatin (Calcium) (drug)]] 5 µM (+4.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Brivudine (drug)]] 5 µM (+3.2); [[Tucidinostat (drug)]] 0.05 µM (+3.0); [[Entrectinib (drug)]] 5 µM (+1.7); [[PF-06260933 (drug)]] 5 µM (+1.5); [[Ipatasertib (drug)]] 0.5 µM (+1.5); [[Pitavastatin (Calcium) (drug)]] 0.05 µM (+1.4); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.4); [[Neratinib (drug)]] 5 µM (+1.3) (33 in all, 13 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-8.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-7.1, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-6.8, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-6.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.3, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.7, ⚠ unreliable plate only); [[PH-797804 (drug)]] 5 µM (-3.6); [[TAK-901 (drug)]] 0.05 µM (-2.9); [[TAK-733 (drug)]] 5 µM (-2.5); [[Belumosudil (drug)]] 5 µM (-2.1); [[Clobetasol propionate (drug)]] 5 µM (-2.0); [[EX229 (drug)]] 5 µM (-1.8); [[Budesonide (drug)]] 5 µM (-1.8); [[Homoharringtonine (drug)]] 0.05 µM (-1.8); [[c-Kit-IN-1 (drug)]] 5 µM (-1.8); [[Budesonide (drug)]] 0.05 µM (-1.7) (54 in all, 22 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[A-172 (line)]], [[HS-578T (line)]], [[LS 180 (line)]], [[PANC-1 (line)]], [[NCI-H1792 (line)]], [[KATO III (line)]], [[MIA PaCa-2 (line)]]

## + arm (14)

| Gene | Projection | Name |
|---|---|---|
| [[TNNT1]] | 0.823 | troponin T1, slow skeletal type |
| [[GIPR]] | 0.805 | gastric inhibitory polypeptide receptor |
| [[TMOD1]] | 0.795 | tropomodulin 1 |
| [[F11R]] | 0.795 | F11 receptor |
| [[LTBP4]] | 0.775 | latent transforming growth factor beta binding protein 4 |
| [[RGS9]] | 0.774 | regulator of G protein signaling 9 |
| [[SYT7]] | 0.742 | synaptotagmin 7 |
| [[KLC3]] | 0.720 | kinesin light chain 3 |
| [[ZNF385A]] | 0.708 | zinc finger protein 385A |
| [[DYNLT3]] | 0.657 | dynein light chain Tctex-type 3 |
| [[TUBA1A]] | 0.613 | tubulin alpha 1a |
| [[C11orf80]] | 0.566 | TOP6B like initiator of meiotic double strand breaks |
| [[ATP8B2]] | 0.525 | ATPase phospholipid transporting 8B2 |
| [[TDRKH]] | 0.521 | tudor and KH domain containing |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 208; `graph/modules.parquet` — module == 208; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [207] (drug-dose × line)
