---
module: 147
type: "module"
n_genes: 30
n_plus: 30
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3909740149974823
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 147

*30 genes (single-armed) · [[Module 147.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 146), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Daptomycin (drug)]] 5 µM (+2.6, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (+2.2); [[Daptomycin (drug)]] 0.5 µM (+2.2, ⚠ unreliable plate only); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.0); [[TAK-901 (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Rapamycin (drug)]] 5 µM (+1.9); [[BAY1125976 (drug)]] 5 µM (+1.9); [[Dinaciclib (drug)]] 0.05 µM (+1.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Larotrectinib sulfate (drug)]] 0.5 µM (+1.5, ⚠ unreliable plate only); [[Harringtonine (drug)]] 0.05 µM (+1.5); [[Temsirolimus (drug)]] 0.05 µM (+1.5); [[vincristine (drug)]] 0.5 µM (+1.5); [[Rapamycin (drug)]] 0.5 µM (+1.4); [[vincristine (drug)]] 5 µM (+1.3); [[Peretinoin (drug)]] 0.5 µM (+1.3) (29 in all, 7 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-10.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-9.8, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-8.2, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (-6.0, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (-5.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-4.9); [[Binimetinib (drug)]] 5 µM (-4.9); [[Cobimetinib (drug)]] 5 µM (-4.8); [[Binimetinib (drug)]] 0.5 µM (-4.8); [[Homoharringtonine (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-4.3); [[Cobimetinib (drug)]] 0.5 µM (-3.7); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.7); [[Ponatinib (drug)]] 5 µM (-3.6); [[Elimusertib hydrochloride (drug)]] 0.05 µM (-3.6) (68 in all, 22 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[AsPC-1 (line)]], [[HOP62 (line)]], [[RKO (line)]], [[NCI-H460 (line)]], [[NCI-H23 (line)]], [[PANC-1 (line)]], [[Hs 766T (line)]], [[HS-578T (line)]]

## + arm (30)

| Gene | Projection | Name |
|---|---|---|
| [[ELK3]] | 0.889 | ETS transcription factor ELK3 |
| [[HMGA2]] | 0.864 | high mobility group AT-hook 2 |
| [[MAP4K4]] | 0.845 | mitogen-activated protein kinase kinase kinase kinase 4 |
| [[LINC00941]] | 0.839 | long independently transcribed non-coding RNA 941 |
| [[LINC02454]] | 0.822 | long independently transcribed non-coding RNA 2454 |
| [[NT5E]] | 0.798 | 5'-nucleotidase ecto |
| [[RPSAP52]] | 0.798 | ribosomal protein SA pseudogene 52 |
| [[CAPRIN2]] | 0.773 | caprin family member 2 |
| [[BCAR3]] | 0.763 | BCAR3 adaptor protein, NSP family member |
| [[CLMP]] | 0.752 | CXADR like cell adhesion molecule |
| [[FOXL1]] | 0.751 | forkhead box L1 |
| [[PXN]] | 0.749 | paxillin |
| [[AKAP12]] | 0.723 | A-kinase anchoring protein 12 |
| [[TOMM34]] | 0.714 | translocase of outer mitochondrial membrane 34 |
| [[TMEM156]] | 0.702 | transmembrane protein 156 |
| [[PALM2AKAP2]] | 0.700 | PALM2 and AKAP2 fusion |
| [[ARHGAP31]] | 0.690 | Rho GTPase activating protein 31 |
| [[HMGA2-AS1]] | 0.668 | HMGA2 antisense RNA 1 |
| [[MACF1]] | 0.651 | microtubule actin crosslinking factor 1 |
| [[MOSMO]] | 0.623 | modulator of smoothened |
| [[CMTM3]] | 0.622 | CKLF like MARVEL transmembrane domain containing 3 |
| [[CDK17]] | 0.599 | cyclin dependent kinase 17 |
| [[EPB41]] | -0.595 | erythrocyte membrane protein band 4.1 |
| [[GPRC5B]] | -0.586 | G protein-coupled receptor class C group 5 member B |
| [[ASB1]] | 0.585 | ankyrin repeat and SOCS box containing 1 |
| [[BCL2L1]] | 0.550 | BCL2 like 1 |
| [[TFPI]] | 0.547 | tissue factor pathway inhibitor |
| [[DCBLD1]] | 0.541 | discoidin, CUB and LCCL domain containing 1 |
| [[CHIC2]] | 0.531 | cysteine rich hydrophobic domain 2 |
| [[PLXNA2]] | 0.520 | plexin A2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 147; `graph/modules.parquet` — module == 147; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [146] (drug-dose × line)
