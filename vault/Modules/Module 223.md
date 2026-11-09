---
module: 223
type: "module"
n_genes: 10
n_plus: 10
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 223

*10 genes (single-armed) · [[Module 223.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | immediate early | control | 2/10 | 151 | 0.028 |
| + | immediate early | control | 2/10 | 151 | 0.028 |
| all | DAP12 signaling | reactome | 2/10 | 126 | 0.039 |
| + | DAP12 signaling | reactome | 2/10 | 126 | 0.039 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 222), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+11.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+6.4); [[Dinaciclib (drug)]] 5 µM (+6.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+6.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+5.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.7, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+4.5, ⚠ cell-cycle shift); [[Filgotinib (drug)]] 5 µM (+3.3); [[Panobinostat (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.6); [[Entrectinib (drug)]] 5 µM (+2.3); [[Binimetinib (drug)]] 0.05 µM (+2.2); [[Ponatinib (drug)]] 5 µM (+2.0); [[Bimiralisib (drug)]] 0.5 µM (+1.9); [[XRK3F2 (drug)]] 0.5 µM (+1.9); [[Ixazomib (drug)]] 5 µM (+1.7); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+1.6) (80 in all, 26 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Ixazomib citrate (drug)]] 5 µM (-4.8, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-4.2, ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM (-4.1); [[Ixazomib citrate (drug)]] 0.5 µM (-3.7); [[Bortezomib (drug)]] 0.05 µM (-3.5, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 5 µM (-3.3, ⚠ unreliable plate only); [[Mebendazole (drug)]] 5 µM (-3.0); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-2.9); [[Daptomycin (drug)]] 0.5 µM (-2.8, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (-2.8); [[Abemaciclib (drug)]] 5 µM (-2.7); [[5-Azacytidine (drug)]] 5 µM (-2.5); [[Abemaciclib (drug)]] 0.5 µM (-2.5); [[EX229 (drug)]] 5 µM (-2.1); [[Peretinoin (drug)]] 0.5 µM (-2.1) (57 in all, 9 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[CHP-212 (line)]], [[RPMI-7951 (line)]], [[NCI-H460 (line)]], [[SW48 (line)]], [[C32 (line)]], [[LoVo (line)]], [[SHP-77 (line)]], [[hTERT-HPNE (line)]]

## + arm (10)

| Gene | Projection | Name |
|---|---|---|
| [[KLRC2]] | 0.933 | killer cell lectin like receptor C2 |
| [[KLRC4-KLRK1]] | 0.930 | KLRC4-KLRK1 readthrough |
| [[KLRK1]] | 0.920 | killer cell lectin like receptor K1 |
| [[KLRC3]] | 0.919 | killer cell lectin like receptor C3 |
| [[CXXC4]] | 0.807 | CXXC finger protein 4 |
| [[NR4A3]] | 0.788 | nuclear receptor subfamily 4 group A member 3 |
| [[NR4A2]] | 0.735 | nuclear receptor subfamily 4 group A member 2 |
| [[ID4]] | 0.723 | inhibitor of DNA binding 4 |
| [[CFAP300]] | 0.633 | cilia and flagella associated protein 300 |
| [[SIK2]] | 0.418 | salt inducible kinase 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 223; `graph/modules.parquet` — module == 223; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [222] (drug-dose × line)
