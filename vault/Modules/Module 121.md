---
module: 121
type: "module"
n_genes: 41
n_plus: 41
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 121

*41 genes (single-armed) · [[Module 121.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 120), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+10.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+8.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+5.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.9); [[Dinaciclib (drug)]] 5 µM (+4.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+4.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.2); [[Dinaciclib (drug)]] 0.05 µM (+2.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+2.7); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+2.1); [[Trametinib (drug)]] 0.5 µM (+2.1); [[Filgotinib (drug)]] 5 µM (+2.1); [[Cobimetinib (drug)]] 0.5 µM (+2.0); [[Binimetinib (drug)]] 5 µM (+1.8); [[Ponatinib (drug)]] 0.5 µM (+1.8); [[Binimetinib (drug)]] 0.5 µM (+1.8) (63 in all, 15 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 0.5 µM (-6.1, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-6.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-2.6, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (-2.3); [[Mebendazole (drug)]] 5 µM (-2.2); [[HI-TOPK-032 (drug)]] 5 µM (-2.0); [[Belinostat (drug)]] 0.5 µM (-1.9, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-1.9, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.8); [[Vilanterol (drug)]] 5 µM (-1.4); [[Abemaciclib (drug)]] 5 µM (-1.3); [[Pasireotide (acetate) (drug)]] 5 µM (-1.3); [[Dexamethasone (drug)]] 0.5 µM (-1.2); [[Pravastatin (sodium) (drug)]] 5 µM (-1.2); [[Goserelin (acetate) (drug)]] 5 µM (-1.2) (35 in all, 13 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HepG2_C3A (line)]], [[RKO (line)]], [[SNU-1 (line)]], [[SW480 (line)]], [[HT-29 (line)]], [[NCI-H1792 (line)]], [[J82 (line)]], [[SNU-423 (line)]]

## + arm (41)

| Gene | Projection | Name |
|---|---|---|
| [[ARHGAP24]] | 0.807 | Rho GTPase activating protein 24 |
| [[FLRT2]] | 0.803 | fibronectin leucine rich transmembrane protein 2 |
| [[TEX41]] | 0.772 | testis expressed 41 |
| [[LINC00882]] | 0.771 | long independently transcribed non-coding RNA 882 |
| [[MAGI2-AS3]] | 0.769 | MAGI2 antisense RNA 3 |
| [[RBMS3]] | 0.762 | RNA binding motif single stranded interacting protein 3 |
| [[MAGI2]] | 0.742 | membrane associated guanylate kinase, WW and PDZ domain containing 2 |
| [[KCNT2]] | 0.712 | potassium sodium-activated channel subfamily T member 2 |
| [[FAP]] | 0.711 | fibroblast activation protein alpha |
| [[L3MBTL4]] | 0.709 | L3MBTL histone methyl-lysine binding protein 4 |
| [[LINC01687]] | 0.702 | long independently transcribed non-coding RNA 1687 |
| [[ZEB2]] | 0.693 | zinc finger E-box binding homeobox 2 |
| [[EBF1]] | 0.689 | EBF transcription factor 1 |
| [[DPY19L2]] | 0.687 | dpy-19 like 2 |
| [[PHACTR1]] | 0.677 | phosphatase and actin regulator 1 |
| [[CNTN6]] | 0.677 | contactin 6 |
| [[HECW2]] | 0.676 | HECT, C2 and WW domain containing E3 ubiquitin protein ligase 2 |
| [[DOCK10]] | 0.673 | dedicator of cytokinesis 10 |
| [[TRPC4]] | 0.662 | transient receptor potential cation channel subfamily C member 4 |
| [[MIR137HG]] | 0.646 | MIR137 host gene |
| [[LINC01776]] | 0.643 | long independently transcribed non-coding RNA 1776 |
| [[NLGN1]] | 0.642 | neuroligin 1 |
| [[LINC00383]] | 0.634 | long independently transcribed non-coding RNA 383 |
| [[DNAH11]] | 0.634 | dynein axonemal heavy chain 11 |
| [[ITGBL1]] | 0.625 | integrin subunit beta like 1 |
| [[LINC02438]] | 0.599 | long independently transcribed non-coding RNA 2438 |
| [[BNC2]] | 0.583 | basonuclin zinc finger protein 2 |
| [[PCDH7]] | 0.582 | protocadherin 7 |
| [[NALCN]] | 0.579 | sodium leak channel, non-selective |
| [[TRPS1]] | 0.577 | transcriptional repressor GATA binding 1 |
| [[FBN2]] | 0.572 | fibrillin 2 |
| [[GLI3]] | 0.556 | GLI family zinc finger 3 |
| [[SYT14]] | 0.555 | synaptotagmin 14 |
| [[SOHLH2]] | 0.552 | spermatogenesis and oogenesis specific basic helix-loop-helix 2 |
| [[FAT4]] | 0.548 | FAT atypical cadherin 4 |
| [[GPR176]] | 0.545 | G protein-coupled receptor 176 |
| [[FGF13]] | 0.529 | fibroblast growth factor 13 |
| [[LRMDA]] | 0.526 | leucine rich melanocyte differentiation associated |
| [[PDGFC]] | 0.514 | platelet derived growth factor C |
| [[LINC03041]] | 0.448 | long independently transcribed non-coding RNA 3041 |
| [[PTH2R]] | 0.426 | parathyroid hormone 2 receptor |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 121; `graph/modules.parquet` — module == 121; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [120] (drug-dose × line)
