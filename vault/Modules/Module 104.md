---
module: 104
type: "module"
n_genes: 44
n_plus: 44
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Molecules associated with elastic fibres"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 104

*Molecules associated with elastic fibres · 44 genes (single-armed) · [[Module 104.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Molecules associated with elastic fibres** (reactome, q 0.025; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Molecules associated with elastic fibres | reactome | 3/44 | 38.1 | 0.025 |
| + | Molecules associated with elastic fibres | reactome | 3/44 | 38.1 | 0.025 |
| all | Elastic fibre formation | reactome | 3/44 | 30.2 | 0.046 |
| + | Elastic fibre formation | reactome | 3/44 | 30.2 | 0.046 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 103), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+7.5); [[Dinaciclib (drug)]] 5 µM (+5.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+4.9, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.05 µM (+4.3); [[Dinaciclib (drug)]] 0.05 µM (+4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Clobetasol propionate (drug)]] 0.5 µM (+3.9); [[Budesonide (drug)]] 0.5 µM (+3.8); [[Betamethasone dipropionate (drug)]] 0.5 µM (+3.8); [[Budesonide (drug)]] 0.05 µM (+3.4); [[Betamethasone dipropionate (drug)]] 0.05 µM (+3.4); [[Triamcinolone (drug)]] 0.5 µM (+3.1); [[Triamcinolone (drug)]] 5 µM (+3.1); [[Betamethasone dipropionate (drug)]] 5 µM (+2.9) (39 in all, 11 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-1.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-1.6, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (-1.6); [[Ixazomib citrate (drug)]] 0.5 µM (-1.6); [[Ouabain (Octahydrate) (drug)]] 5 µM (-1.5, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.5); [[Harringtonine (drug)]] 0.5 µM (-1.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.05 µM (-1.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-1.2, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-1.2, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-1.2); [[TAK-733 (drug)]] 0.05 µM (-1.0) (12 in all, 7 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H1792 (line)]], [[SW 900 (line)]], [[HS-578T (line)]], [[HOP62 (line)]], [[RPMI-7951 (line)]], [[A-172 (line)]], [[SNU-423 (line)]], [[NCI-H1573 (line)]]

## + arm (44)

| Gene | Projection | Name |
|---|---|---|
| [[DCN]] | 0.818 | decorin |
| [[PID1]] | 0.802 | phosphotyrosine interaction domain containing 1 |
| [[HSD11B1]] | 0.794 | hydroxysteroid 11-beta dehydrogenase 1 |
| [[DNER]] | 0.775 | delta/notch like EGF repeat containing |
| [[TMTC1]] | 0.744 | transmembrane O-mannosyltransferase targeting cadherins 1 |
| [[DAAM2]] | 0.737 | dishevelled associated activator of morphogenesis 2 |
| [[IRAK3]] | 0.732 | interleukin 1 receptor associated kinase 3 |
| [[IL1R1]] | 0.694 | interleukin 1 receptor type 1 |
| [[GAB3]] | 0.672 | GRB2 associated binding protein 3 |
| [[PDGFRA]] | 0.671 | platelet derived growth factor receptor alpha |
| [[ATOH8]] | 0.657 | atonal bHLH transcription factor 8 |
| [[COPS8]] | 0.654 | COP9 signalosome subunit 8 |
| [[RNF175]] | 0.642 | ring finger protein 175 |
| [[ITGA8]] | 0.639 | integrin subunit alpha 8 |
| [[HS3ST3B1]] | 0.630 | heparan sulfate-glucosamine 3-sulfotransferase 3B1 |
| [[FN1]] | 0.617 | fibronectin 1 |
| [[LPAR1]] | 0.608 | lysophosphatidic acid receptor 1 |
| [[JCAD]] | 0.605 | junctional cadherin 5 associated |
| [[CCBE1]] | 0.602 | collagen and calcium binding EGF domains 1 |
| [[CACNA1C]] | 0.600 | calcium voltage-gated channel subunit alpha1 C |
| [[SRPX]] | 0.600 | sushi repeat containing protein X-linked |
| [[AMPH]] | 0.595 | amphiphysin |
| [[MGP]] | 0.590 | matrix Gla protein |
| [[NPR3]] | 0.590 | natriuretic peptide receptor 3 |
| [[RBMS1]] | 0.589 | RNA binding motif single stranded interacting protein 1 |
| [[SLC7A2]] | 0.584 | solute carrier family 7 member 2 |
| [[AFAP1L1]] | 0.580 | actin filament associated protein 1 like 1 |
| [[IL18R1]] | 0.578 | interleukin 18 receptor 1 |
| [[NTS]] | 0.577 | neurotensin |
| [[PTPRM]] | 0.577 | protein tyrosine phosphatase receptor type M |
| [[ANPEP]] | 0.535 | alanyl aminopeptidase, membrane |
| [[STEAP3]] | 0.528 | STEAP3 metalloreductase |
| [[SRGN]] | 0.518 | serglycin |
| [[TWIST1]] | 0.516 | twist family bHLH transcription factor 1 |
| [[SLC1A3]] | 0.514 | solute carrier family 1 member 3 |
| [[FAH]] | 0.497 | fumarylacetoacetate hydrolase |
| [[LTBP1]] | 0.495 | latent transforming growth factor beta binding protein 1 |
| [[GHR]] | 0.487 | growth hormone receptor |
| [[TRAM2]] | 0.481 | translocation associated membrane protein 2 |
| [[RNF144A]] | 0.424 | ring finger protein 144A |
| [[JAK2]] | 0.397 | Janus kinase 2 |
| [[RDX]] | 0.394 | radixin |
| [[GRAMD2B]] | 0.382 | GRAM domain containing 2B |
| [[DNAH5]] | 0.320 | dynein axonemal heavy chain 5 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 104; `graph/modules.parquet` — module == 104; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [103] (drug-dose × line)
