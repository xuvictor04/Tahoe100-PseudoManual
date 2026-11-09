---
module: 70
type: "module"
n_genes: 70
n_plus: 70
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "interferon gamma response"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 070

*interferon gamma response · 70 genes (single-armed) · [[Module 070.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **interferon gamma response** (hallmark, q 6e-28; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | interferon gamma response | hallmark | 25/70 | 31.9 | 6e-28 |
| + | interferon gamma response | hallmark | 25/70 | 31.9 | 6e-28 |
| + | interferon alpha response | hallmark | 19/70 | 44.5 | 2e-23 |
| all | interferon alpha response | hallmark | 19/70 | 44.5 | 2e-23 |
| all | Antigen processing-Cross presentation | reactome | 14/70 | 33.9 | 9e-15 |
| + | Antigen processing-Cross presentation | reactome | 14/70 | 33.9 | 9e-15 |
| + | Interferon gamma signaling | reactome | 13/70 | 38.4 | 3e-14 |
| all | Interferon gamma signaling | reactome | 13/70 | 38.4 | 3e-14 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 69), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Cobimetinib (drug)]] 5 µM (+4.1); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (+3.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+3.5); [[Binimetinib (drug)]] 5 µM (+3.5); [[Binimetinib (drug)]] 0.5 µM (+3.2); [[Harringtonine (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+2.8); [[Trametinib (drug)]] 5 µM (+2.8, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 0.5 µM (+2.6); [[Binimetinib (drug)]] 0.05 µM (+2.6); [[Elimusertib hydrochloride (drug)]] 0.05 µM (+2.5); [[Trametinib (drug)]] 0.05 µM (+2.3) (51 in all, 17 with an alert ⚠; shown: the 10 strongest and the 3 next strongest without an alert)
- Lower it: [[Panobinostat (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-5.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-4.6, ⚠ cell-cycle shift); [[Tofacitinib (drug)]] 5 µM (-4.3); [[Auranofin (drug)]] 5 µM (-3.8); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.2, ⚠ unreliable plate only); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-3.2); [[Ixazomib citrate (drug)]] 5 µM (-3.2, ⚠ cell-cycle shift); [[Tofacitinib (drug)]] 0.5 µM (-3.1); [[Tofacitinib (citrate) (drug)]] 5 µM (-2.9); [[Tofacitinib (citrate) (drug)]] 0.5 µM (-2.7); [[Ixazomib citrate (drug)]] 0.5 µM (-2.6); [[Vinblastine (sulfate) (drug)]] 5 µM (-2.6); [[Budesonide (drug)]] 5 µM (-2.2); [[Dexamethasone (drug)]] 0.5 µM (-1.9) (62 in all, 16 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[COLO 205 (line)]], [[A498 (line)]], [[CFPAC-1 (line)]], [[A-172 (line)]], [[AsPC-1 (line)]], [[MIA PaCa-2 (line)]], [[KATO III (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 55 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[HLA-A]] | DAP12 interactions | +0.79 |
| 2 | [[B2M]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.73 |
| 3 | [[HLA-B]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.72 |
| 4 | [[TAP1]] | Endosomal/Vacuolar pathway | +0.71 |
| 5 | [[GBP4]] | Antigen processing-Cross presentation | +0.70 |
| 6 | [[HLA-F]] | Non-canonical inflammasome activation | +0.70 |
| 7 | [[PSMB9]] | Interferon gamma signaling | +0.69 |
| 8 | [[ISG15]] | Interferon gamma signaling | +0.67 |
| 9 | [[CFH]] | CASP4 inflammasome assembly | +0.67 |
| 10 | [[PSME2]] | Interferon Signaling | +0.67 |
| 11 | [[CFB]] | Interferon gamma signaling | +0.66 |
| 12 | [[CTSS]] | Antigen Presentation: Folding, assembly and peptide loading of class I MHC | +0.66 |
| 13 | [[TRIM5]] | ER-Phagosome pathway | +0.66 |
| 14 | [[TRANK1]] | Interferon gamma signaling | +0.66 |
| 15 | [[HCP5]] | Endosomal/Vacuolar pathway | +0.65 |

## + arm (70)

| Gene | Projection | Name |
|---|---|---|
| [[GBP4]] | 0.930 | guanylate binding protein 4 |
| [[PSMB9]] | 0.901 | proteasome 20S subunit beta 9 |
| [[GBP1]] | 0.882 | guanylate binding protein 1 |
| [[TRANK1]] | 0.876 | tetratricopeptide repeat and ankyrin repeat containing 1 |
| [[HLA-F]] | 0.875 | major histocompatibility complex, class I, F |
| [[CFB]] | 0.873 | complement factor B |
| [[TAP1]] | 0.865 | transporter 1, ATP binding cassette subfamily B member |
| [[B2M]] | 0.861 | beta-2-microglobulin |
| [[TRIM5]] | 0.832 | tripartite motif containing 5 |
| [[HLA-B]] | 0.828 | major histocompatibility complex, class I, B |
| [[TNFSF10]] | 0.828 | TNF superfamily member 10 |
| [[PSMB10]] | 0.822 | proteasome 20S subunit beta 10 |
| [[CTSS]] | 0.819 | cathepsin S |
| [[PSME2]] | 0.816 | proteasome activator subunit 2 |
| [[APOL3]] | 0.813 | apolipoprotein L3 |
| [[IDO1]] | 0.813 | indoleamine 2,3-dioxygenase 1 |
| [[APOL6]] | 0.809 | apolipoprotein L6 |
| [[ISG15]] | 0.798 | ISG15 ubiquitin like modifier |
| [[TLR3]] | 0.789 | toll like receptor 3 |
| [[APOL1]] | 0.777 | apolipoprotein L1 |
| [[HLA-E]] | 0.771 | major histocompatibility complex, class I, E |
| [[GBP2]] | 0.765 | guanylate binding protein 2 |
| [[CASP10]] | 0.757 | caspase 10 |
| [[IRF7]] | 0.743 | interferon regulatory factor 7 |
| [[PLAAT4]] | 0.738 | phospholipase A and acyltransferase 4 |
| [[MVP-DT]] | 0.723 | MVP divergent transcript |
| [[PSME1]] | 0.712 | proteasome activator subunit 1 |
| [[GSDMD]] | 0.709 | gasdermin D |
| [[CFH]] | 0.701 | complement factor H |
| [[IL15RA]] | 0.700 | interleukin 15 receptor subunit alpha |
| [[HLA-C]] | 0.700 | major histocompatibility complex, class I, C |
| [[HCP5]] | 0.688 | HLA complex P5 |
| [[HLA-A]] | 0.686 | major histocompatibility complex, class I, A |
| [[IFI30]] | 0.681 | IFI30 lysosomal thiol reductase |
| [[OGFR]] | 0.680 | opioid growth factor receptor |
| [[TAPBP]] | 0.679 | TAP binding protein |
| [[BTN3A1]] | 0.672 | butyrophilin subfamily 3 member A1 |
| [[LINC02100]] | 0.671 | long independently transcribed non-coding RNA 2100 |
| [[CD5L]] | 0.662 | CD5 molecule like |
| [[FBXO6]] | 0.660 | F-box protein 6 |
| [[FLT3LG]] | 0.648 | fms related receptor tyrosine kinase 3 ligand |
| [[TRAFD1]] | 0.644 | TRAF-type zinc finger domain containing 1 |
| [[MMP13]] | 0.641 | matrix metallopeptidase 13 |
| [[NUB1]] | 0.633 | negative regulator of ubiquitin like proteins 1 |
| [[CTSO]] | 0.628 | cathepsin O |
| [[RARRES1]] | 0.625 | retinoic acid receptor responder 1 |
| [[ISG20]] | 0.621 | interferon stimulated exonuclease gene 20 |
| [[BTN3A2]] | 0.613 | butyrophilin subfamily 3 member A2 |
| [[CXCL16]] | 0.595 | C-X-C motif chemokine ligand 16 |
| [[LINC02577]] | 0.584 | long independently transcribed non-coding RNA 2577 |
| [[NCOA7]] | 0.557 | nuclear receptor coactivator 7 |
| [[TENT5A]] | 0.556 | terminal nucleotidyltransferase 5A |
| [[HLA-H]] | 0.550 | major histocompatibility complex, class I, H (pseudogene) |
| [[ETV6]] | 0.543 | ETS variant transcription factor 6 |
| [[DUOX2]] | 0.534 | dual oxidase 2 |
| [[ALPK1]] | 0.515 | alpha kinase 1 |
| [[SIX1]] | 0.510 | SIX homeobox 1 |
| [[MDK]] | 0.507 | midkine |
| [[RGPD2]] | 0.499 | RANBP2 like and GRIP domain containing 2 |
| [[UBE2Z]] | 0.497 | ubiquitin conjugating enzyme E2 Z |
| [[ENKUR]] | 0.491 | enkurin, TRPC channel interacting protein |
| [[NT5C3A]] | 0.485 | 5'-nucleotidase, cytosolic IIIA |
| [[SLFN12]] | 0.482 | schlafen family member 12 |
| [[STING1]] | 0.481 | stimulator of interferon response cGAMP interactor 1 |
| [[MVP]] | 0.471 | major vault protein |
| [[LINC00278]] | 0.454 | long independently transcribed non-coding RNA 278 |
| [[PDGFRL]] | 0.425 | platelet derived growth factor receptor like |
| [[LYSMD2]] | 0.417 | LysM domain containing 2 |
| [[IL7]] | 0.410 | interleukin 7 |
| [[MAML2]] | 0.187 | mastermind like transcriptional coactivator 2 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 70; `graph/modules.parquet` — module == 70; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [69] (drug-dose × line)
