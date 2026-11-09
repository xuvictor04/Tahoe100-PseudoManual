---
module: 59
type: "module"
n_genes: 80
n_plus: 66
n_minus: 14
arms_opposite: true
mean_cos_between_arms: -0.3024829924106598
label: "Amino acids regulate mTORC1"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 059

*Amino acids regulate mTORC1 · 80 genes (66 in the + arm, 14 in the − arm) · [[Module 059.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Amino acids regulate mTORC1** (reactome, q 0.002; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Amino acids regulate mTORC1 | reactome | 5/66 | 22.0 | 0.002 |
| + | BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members | reactome | 3/66 | 76.1 | 0.003 |
| all | Amino acids regulate mTORC1 | reactome | 5/80 | 18.1 | 0.004 |
| all | BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members | reactome | 3/80 | 62.8 | 0.006 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 58), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Homoharringtonine (drug)]] 5 µM (+17.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+10.0, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+5.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Trametinib (drug)]] 0.5 µM (+4.5); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+4.0); [[Osimertinib (mesylate) (drug)]] 5 µM (+3.9); [[TAK-901 (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+3.8, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+3.6); [[Binimetinib (drug)]] 5 µM (+3.6); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+3.5); [[Binimetinib (drug)]] 0.5 µM (+3.4); [[Cobimetinib (drug)]] 0.05 µM (+3.3); [[Radotinib (drug)]] 5 µM (+3.3); [[Entrectinib (drug)]] 5 µM (+3.2) (155 in all, 28 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-7.0, ⚠ unreliable plate only); [[Daptomycin (drug)]] 5 µM (-4.0, ⚠ unreliable plate only); [[Dinaciclib (drug)]] 5 µM (-3.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Daptomycin (drug)]] 0.5 µM (-3.7, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (-3.5); [[Digitoxin (drug)]] 0.05 µM (-3.4, ⚠ cell-cycle shift); [[5-Azacytidine (drug)]] 5 µM (-3.1); [[Auranofin (drug)]] 5 µM (-3.0); [[Bortezomib (drug)]] 0.05 µM (-3.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-2.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dabrafenib (drug)]] 5 µM (-2.8); [[Clobetasol propionate (drug)]] 5 µM (-2.8); [[Budesonide (drug)]] 5 µM (-2.7); [[Fenofibrate (drug)]] 0.05 µM (-2.6); [[BAY1125976 (drug)]] 5 µM (-2.5); [[Vinblastine (sulfate) (drug)]] 0.5 µM (-2.4); [[Clobetasol propionate (drug)]] 0.5 µM (-2.4) (182 in all, 24 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[PANC-1 (line)]], [[HEC-1-A (line)]], [[J82 (line)]], [[RKO (line)]], [[A498 (line)]], [[A-427 (line)]], [[NCI-H23 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 10 candidates, 1 with an alert ⚠.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[NEU1]] | Amino acids regulate mTORC1 | +0.64 |  |
| 2 | [[UAP1L1]] | Amino acids regulate mTORC1 | +0.57 |  |
| 3 | [[MYLIP]] | BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members | +0.55 |  |
| 4 | [[GABARAP]] ⚠ | Amino acids regulate mTORC1 | +0.54 | ⚠ in the vector space only through drug-doses that carry an alert |
| 5 | [[PIM3]] | BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members | +0.52 |  |
| 6 | [[SAT2]] | Amino acids regulate mTORC1 | +0.52 |  |
| 7 | [[VASN]] | BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members | +0.51 |  |
| 8 | [[DBP]] | BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members | +0.51 |  |
| 9 | [[TOLLIP]] | Amino acids regulate mTORC1 | +0.50 |  |
| 10 | [[ABCA5]] | BH3-only proteins associate with and inactivate anti-apoptotic BCL-2 members | +0.50 |  |

*⚠ 1 of its 80 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (66)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[RAB9A]] | 0.806 | RAB9A, member RAS oncogene family |  |
| [[KMT2E]] | 0.805 | lysine methyltransferase 2E (inactive) |  |
| [[SAT2]] | 0.802 | spermidine/spermine N1-acetyltransferase family member 2 |  |
| [[ABCA5]] | 0.802 | ATP binding cassette subfamily A member 5 |  |
| [[DBP]] | 0.762 | D-box binding PAR bZIP transcription factor |  |
| [[PIM3]] | 0.750 | Pim-3 proto-oncogene, serine/threonine kinase |  |
| [[GABARAP]] | 0.734 | GABA type A receptor-associated protein | ⚠ only flagged evidence |
| [[NEU1]] | 0.730 | neuraminidase 1 |  |
| [[RRAGC]] | 0.726 | Ras related GTP binding C |  |
| [[LINC01273]] | 0.720 | long independently transcribed non-coding RNA 1273 |  |
| [[RAB30]] | 0.715 | RAB30, member RAS oncogene family |  |
| [[CBX4]] | 0.712 | chromobox 4 |  |
| [[BMF]] | 0.702 | Bcl2 modifying factor |  |
| [[VASN]] | 0.688 | vasorin |  |
| [[FLCN]] | 0.685 | folliculin |  |
| [[VAMP2]] | 0.684 | vesicle associated membrane protein 2 |  |
| [[BBC3]] | 0.680 | BCL2 binding component 3 |  |
| [[TCEAL3]] | 0.676 | transcription elongation factor A like 3 |  |
| [[AFTPH]] | 0.672 | aftiphilin |  |
| [[LCA5]] | 0.669 | lebercilin LCA5 |  |
| [[IST1]] | 0.663 | IST1 factor associated with ESCRT-III |  |
| [[OPTN]] | 0.661 | optineurin |  |
| [[MYLIP]] | 0.659 | myosin regulatory light chain interacting protein |  |
| [[HOOK2]] | 0.658 | hook microtubule tethering protein 2 |  |
| [[CHMP2B]] | 0.653 | charged multivesicular body protein 2B |  |
| [[APBA3]] | 0.653 | amyloid beta precursor protein binding family A member 3 |  |
| [[CXXC5]] | 0.647 | CXXC finger protein 5 |  |
| [[UAP1L1]] | 0.645 | UDP-N-acetylglucosamine pyrophosphorylase 1 like 1 |  |
| [[MITD1]] | 0.640 | microtubule interacting and trafficking domain containing 1 |  |
| [[LACTB]] | 0.637 | lactamase beta |  |
| [[GIHCG]] | 0.633 | GIHCG inhibitor of miR-200b/200a/429 expression |  |
| [[RILP]] | 0.629 | Rab interacting lysosomal protein |  |
| [[TRA2A]] | 0.624 | transformer 2 alpha homolog |  |
| [[ARMCX3]] | 0.624 | armadillo repeat containing X-linked 3 |  |
| [[DNAJC12]] | 0.620 | DnaJ heat shock protein family (Hsp40) member C12 |  |
| [[NUDT14]] | 0.619 | nudix hydrolase 14 |  |
| [[CBX8]] | 0.601 | chromobox 8 |  |
| [[TOM1]] | 0.587 | target of myb1 membrane trafficking protein |  |
| [[CTNND1]] | 0.578 | catenin delta 1 |  |
| [[PIM2]] | 0.570 | Pim-2 proto-oncogene, serine/threonine kinase |  |
| [[DAAM1]] | 0.538 | dishevelled associated activator of morphogenesis 1 |  |
| [[TP53INP2]] | 0.531 | tumor protein p53 inducible nuclear protein 2 |  |
| [[TOLLIP]] | 0.509 | toll interacting protein |  |
| [[BCL2L11]] | 0.507 | BCL2 like 11 |  |
| [[PRICKLE3]] | 0.503 | prickle planar cell polarity protein 3 |  |
| [[ID2]] | 0.502 | inhibitor of DNA binding 2 |  |
| [[COQ10A]] | 0.498 | coenzyme Q10A |  |
| [[PLPP1]] | 0.498 | phospholipid phosphatase 1 |  |
| [[ZNF706]] | 0.497 | zinc finger protein 706 |  |
| [[PITX2]] | 0.496 | paired like homeodomain 2 |  |
| [[RNF19B]] | 0.492 | ring finger protein 19B |  |
| [[RABGAP1]] | 0.490 | RAB GTPase activating protein 1 |  |
| [[LRRC37B]] | 0.488 | leucine rich repeat containing 37B |  |
| [[TOB1]] | 0.487 | transducer of ERBB2, 1 |  |
| [[TRPM7]] | 0.484 | transient receptor potential cation channel subfamily M member 7 |  |
| [[GRINA]] | 0.479 | glutamate ionotropic receptor NMDA type subunit associated protein 1 |  |
| [[MEX3B]] | 0.461 | mex-3 RNA binding family member B |  |
| [[MAP3K13]] | 0.452 | mitogen-activated protein kinase kinase kinase 13 |  |
| [[TM7SF2]] | 0.449 | transmembrane 7 superfamily member 2 |  |
| [[SSBP3]] | 0.444 | single stranded DNA binding protein 3 |  |
| [[FNIP1]] | 0.441 | folliculin interacting protein 1 |  |
| [[ATP6V0C]] | 0.430 | ATPase H+ transporting V0 subunit c |  |
| [[SWAP70]] | 0.425 | switching B cell complex subunit SWAP70 |  |
| [[VPS18]] | 0.380 | VPS18 core subunit of CORVET and HOPS complexes |  |
| [[ABCG1]] | 0.358 | ATP binding cassette subfamily G member 1 |  |
| [[ATP6V0D1]] | 0.342 | ATPase H+ transporting V0 subunit d1 |  |

## − arm (14)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[TTL]] | -0.728 | tubulin tyrosine ligase |  |
| [[ZNF731P]] | -0.720 | zinc finger protein 731, pseudogene |  |
| [[UGGT2]] | -0.636 | UDP-glucose glycoprotein glucosyltransferase 2 |  |
| [[SRPK1]] | -0.618 | SRSF protein kinase 1 |  |
| [[SEC14L1]] | -0.598 | SEC14 like lipid binding 1 |  |
| [[TMEM181]] | -0.590 | transmembrane protein 181 |  |
| [[NBPF20]] | -0.575 | NBPF member 20 |  |
| [[FARP1]] | -0.561 | FERM, ARH/RhoGEF and pleckstrin domain protein 1 |  |
| [[STK39]] | -0.557 | serine/threonine kinase 39 |  |
| [[TXLNA]] | -0.527 | taxilin alpha |  |
| [[MAN2A1]] | -0.490 | mannosidase alpha class 2A member 1 |  |
| [[ICE1]] | -0.463 | interactor of little elongation complex ELL subunit 1 |  |
| [[ZNF8]] | -0.450 | zinc finger protein 8 |  |
| [[CARS2]] | -0.238 | cysteinyl-tRNA synthetase 2, mitochondrial |  |

## Data

- `graph/nodes.parquet` — module == 59; `graph/modules.parquet` — module == 59; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [58] (drug-dose × line)
