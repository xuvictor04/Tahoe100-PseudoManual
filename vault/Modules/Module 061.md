---
module: 61
type: "module"
n_genes: 78
n_plus: 78
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.24788931012153625
label: "Neuronal System"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 061

*Neuronal System · 78 genes (single-armed) · [[Module 061.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Neuronal System** (reactome, q 2e-07; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Neuronal System | reactome | 14/78 | 9.60 | 2e-07 |
| + | Neuronal System | reactome | 14/78 | 9.60 | 2e-07 |
| all | Transmission across Chemical Synapses | reactome | 8/78 | 8.14 | 0.003 |
| + | Transmission across Chemical Synapses | reactome | 8/78 | 8.14 | 0.003 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 60), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+16.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+14.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+13.9); [[Dinaciclib (drug)]] 5 µM (+10.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+9.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+9.3, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+7.9, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+7.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+7.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Belinostat (drug)]] 5 µM (+6.9, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+6.2); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.8); [[Brivudine (drug)]] 5 µM (+3.0); [[Ipatasertib (drug)]] 0.5 µM (+2.1); [[Tucidinostat (drug)]] 0.05 µM (+1.8); [[XRK3F2 (drug)]] 0.5 µM (+1.7); [[Amsacrine (drug)]] 5 µM (+1.6); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+1.5); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+1.5) (63 in all, 32 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Adagrasib (drug)]] 0.05 µM (-2.1, ⚠ position not correctable); [[Lucanthone (drug)]] 0.05 µM (-1.5); [[Goserelin (acetate) (drug)]] 5 µM (-1.4); [[Rutin (trihydrate) (drug)]] 0.05 µM (-1.3); [[Artesunate (drug)]] 0.5 µM (-1.3); [[(S)-Crizotinib (drug)]] 0.05 µM (-1.3); [[Dexamethasone (drug)]] 0.5 µM (-1.2); [[Erlotinib (drug)]] 0.05 µM (-1.2); [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM (-1.2); [[Dabrafenib (drug)]] 5 µM (-1.2); [[Fenofibrate (drug)]] 0.05 µM (-1.2) (21 in all, 2 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[NCI-H23 (line)]], [[PANC-1 (line)]], [[HOP62 (line)]], [[SK-MEL-2 (line)]], [[NCI-H1573 (line)]], [[NCI-H2030 (line)]], [[A-172 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 1 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[SGCZ]] | Transmission across Chemical Synapses | +0.53 |

## + arm (78)

| Gene | Projection | Name |
|---|---|---|
| [[SGCZ]] | 0.850 | sarcoglycan zeta |
| [[SLC35F1]] | 0.827 | solute carrier family 35 member F1 |
| [[LINC02511]] | 0.805 | long independently transcribed non-coding RNA 2511 |
| [[XKR4]] | 0.803 | XK related 4 |
| [[GRIA4]] | 0.797 | glutamate ionotropic receptor AMPA type subunit 4 |
| [[SH3GL2]] | 0.796 | SH3 domain containing GRB2 like 2, endophilin A1 |
| [[PCSK2]] | 0.754 | proprotein convertase subtilisin/kexin type 2 |
| [[HS6ST3]] | 0.752 | heparan sulfate 6-O-sulfotransferase 3 |
| [[GPM6A]] | 0.748 | glycoprotein M6A |
| [[SNAP91]] | 0.737 | synaptosome associated protein 91 |
| [[PKNOX2]] | 0.735 | PBX/knotted 1 homeobox 2 |
| [[DACH2]] | 0.733 | dachshund family transcription factor 2 |
| [[KCNN3]] | 0.725 | potassium calcium-activated channel subfamily N member 3 |
| [[CELF4]] | 0.724 | CUGBP Elav-like family member 4 |
| [[COLEC12]] | 0.721 | collectin subfamily member 12 |
| [[SNTG2]] | 0.717 | syntrophin gamma 2 |
| [[ERC2]] | 0.711 | ELKS/RAB6-interacting/CAST family member 2 |
| [[NDRG4]] | 0.706 | NDRG family member 4 |
| [[KCNH1]] | 0.705 | potassium voltage-gated channel subfamily H member 1 |
| [[TMEFF2]] | 0.696 | transmembrane protein with EGF like and two follistatin like domains 2 |
| [[PLCL1]] | 0.696 | phospholipase C like 1 (inactive) |
| [[ALK]] | 0.695 | ALK receptor tyrosine kinase |
| [[KCNN2]] | 0.691 | potassium calcium-activated channel subfamily N member 2 |
| [[RGS7]] | 0.685 | regulator of G protein signaling 7 |
| [[SYN1]] | 0.673 | synapsin I |
| [[IL3RA]] | 0.670 | interleukin 3 receptor subunit alpha |
| [[OLFM2]] | 0.657 | olfactomedin 2 |
| [[CHST8]] | 0.649 | carbohydrate sulfotransferase 8 |
| [[ELAVL2]] | 0.647 | ELAV like RNA binding protein 2 |
| [[AFF2]] | 0.645 | ALF transcription elongation factor 2 |
| [[ADAMTSL1]] | 0.641 | ADAMTS like 1 |
| [[HYDIN]] | 0.639 | HYDIN axonemal central pair apparatus protein |
| [[CHRM3]] | 0.631 | cholinergic receptor muscarinic 3 |
| [[WIPF3]] | 0.624 | WAS/WASL interacting protein family member 3 |
| [[EPHB1]] | 0.620 | EPH receptor B1 |
| [[CCDC85A]] | 0.620 | coiled-coil domain containing 85A |
| [[SLC1A2]] | 0.617 | solute carrier family 1 member 2 |
| [[NHSL2]] | 0.612 | NHS like 2 |
| [[C11orf96]] | 0.607 | chromosome 11 open reading frame 96 |
| [[MYO18B]] | 0.603 | myosin XVIIIB |
| [[ACHE]] | 0.597 | acetylcholinesterase (Yt blood group) |
| [[SLCO2B1]] | 0.592 | solute carrier organic anion transporter family member 2B1 |
| [[VAT1L]] | 0.590 | vesicle amine transport 1 like |
| [[GPR158]] | 0.589 | G protein-coupled receptor 158 |
| [[STXBP5L]] | 0.585 | syntaxin binding protein 5L |
| [[NTRK3]] | 0.581 | neurotrophic receptor tyrosine kinase 3 |
| [[PDLIM3]] | 0.581 | PDZ and LIM domain 3 |
| [[OLFM1]] | 0.578 | olfactomedin 1 |
| [[NEURL1]] | 0.567 | neuralized E3 ubiquitin protein ligase 1 |
| [[KCNQ3]] | 0.556 | potassium voltage-gated channel subfamily Q member 3 |
| [[ADAM7-AS1]] | 0.554 | ADAM7, ADAMDEC1 and ADAM28 antisense RNA 1 |
| [[ISM1]] | 0.554 | isthmin 1 |
| [[LINC02968]] | 0.548 | long independently transcribed non-coding RNA 2968 |
| [[MIR4527HG]] | 0.547 | MIR4527 host gene |
| [[RGS16]] | 0.538 | regulator of G protein signaling 16 |
| [[CHRNA7]] | 0.535 | cholinergic receptor nicotinic alpha 7 subunit |
| [[P2RY1]] | 0.524 | purinergic receptor P2Y1 |
| [[ANOS2P]] | 0.523 | anosmin 2, pseudogene |
| [[ENTREP1]] | 0.516 | endosomal transmembrane epsin interactor 1 |
| [[PPM1E]] | 0.514 | protein phosphatase, Mg2+/Mn2+ dependent 1E |
| [[PAPLN]] | 0.513 | papilin, proteoglycan like sulfated glycoprotein |
| [[PLAAT1]] | 0.511 | phospholipase A and acyltransferase 1 |
| [[GRIP2]] | 0.505 | glutamate receptor interacting protein 2 |
| [[CLSTN2]] | 0.493 | calsyntenin 2 |
| [[SCG3]] | 0.489 | secretogranin III |
| [[CAMK4]] | 0.481 | calcium/calmodulin dependent protein kinase IV |
| [[CHGB]] | 0.473 | chromogranin B |
| [[PAK1]] | 0.463 | p21 (RAC1) activated kinase 1 |
| [[NR0B1]] | 0.459 | nuclear receptor subfamily 0 group B member 1 |
| [[ABCB1]] | 0.445 | ATP binding cassette subfamily B member 1 |
| [[SYT12]] | 0.433 | synaptotagmin 12 |
| [[XKR7]] | 0.430 | XK related 7 |
| [[TCEANC2]] | -0.424 | transcription elongation factor A N-terminal and central domain containing 2 |
| [[IRF4]] | 0.402 | interferon regulatory factor 4 |
| [[APBB1]] | 0.388 | amyloid beta precursor protein binding family B member 1 |
| [[PRKCH]] | 0.375 | protein kinase C eta |
| [[LINC02842]] | 0.257 | long independently transcribed non-coding RNA 2842 |
| [[SRD5A3]] | 0.219 | steroid 5 alpha-reductase 3 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 61; `graph/modules.parquet` — module == 61; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [60] (drug-dose × line)
