---
module: 64
type: "module"
n_genes: 77
n_plus: 71
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.262782484292984
label: "proteasome"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 064

*proteasome · 77 genes (71 in the + arm, 6 in the − arm) · [[Module 064.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **proteasome** (control, q 2e-11; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | proteasome | control | 9/71 | 61.6 | 2e-11 |
| all | proteasome | control | 9/77 | 56.8 | 4e-11 |
| + | Vif-mediated degradation of APOBEC3G | reactome | 9/71 | 46.6 | 3e-10 |
| + | Signaling by Hedgehog | reactome | 12/71 | 20.7 | 6e-10 |
| all | Vif-mediated degradation of APOBEC3G | reactome | 9/77 | 43.0 | 7e-10 |
| + | Hedgehog 'on' state | reactome | 10/71 | 30.8 | 1e-09 |
| all | Signaling by Hedgehog | reactome | 12/77 | 19.1 | 2e-09 |
| + | Proteasome assembly | reactome | 9/71 | 38.2 | 2e-09 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 63), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Bortezomib (drug)]] 0.05 µM (+10.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+10.7, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+10.3); [[Dinaciclib (drug)]] 0.5 µM (+10.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+9.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+7.5); [[Dinaciclib (drug)]] 0.05 µM (+7.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 5 µM (+7.0, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.9, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+5.6, ⚠ toxic; cell-cycle shift); [[Bortezomib (drug)]] 0.5 µM (+3.6); [[Ponatinib (drug)]] 5 µM (+3.5); [[Homoharringtonine (drug)]] 0.05 µM (+3.4); [[Ponatinib (drug)]] 0.5 µM (+2.7); [[Binimetinib (drug)]] 0.05 µM (+2.3); [[Bendamustine (drug)]] 5 µM (+2.3); [[TAK-733 (drug)]] 5 µM (+2.3); [[Sulfatinib (drug)]] 5 µM (+2.2) (142 in all, 30 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Digitoxin (drug)]] 0.5 µM (-7.3, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-7.2, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-6.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-5.8); [[Belinostat (drug)]] 5 µM (-5.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-5.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (-4.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.2, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-4.0, ⚠ cell-cycle shift); [[Brivudine (drug)]] 5 µM (-3.0); [[PF-06260933 (drug)]] 5 µM (-2.8); [[HI-TOPK-032 (drug)]] 5 µM (-2.6); [[Irinotecan (hydrochloride) (drug)]] 0.5 µM (-2.3); [[BAY1125976 (drug)]] 5 µM (-2.1); [[Pitavastatin (Calcium) (drug)]] 0.5 µM (-2.0); [[Irinotecan (drug)]] 0.5 µM (-1.8); [[Roxadustat (drug)]] 5 µM (-1.8); [[Dihydroartemisinin (drug)]] 5 µM (-1.7) (110 in all, 29 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HOP62 (line)]], [[LOX-IMVI (line)]], [[A498 (line)]], [[A-172 (line)]], [[PANC-1 (line)]], [[HT-29 (line)]], [[HEC-1-A (line)]], [[NCI-H1573 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 11 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PSMD3]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.56 |
| 2 | [[PSMD4]] | Regulation of activated PAK-2p34 by proteasome mediated degradation | +0.55 |
| 3 | [[MRPL45]] | proteasome | +0.55 |
| 4 | [[RHBDD3]] | Regulation of activated PAK-2p34 by proteasome mediated degradation | +0.53 |
| 5 | [[TYW3]] | Vif-mediated degradation of APOBEC3G | +0.53 |
| 6 | [[UBXN4]] | proteasome | +0.52 |
| 7 | [[PSMC5]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.52 |
| 8 | [[PSMC1]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.52 |
| 9 | [[SLC38A6]] | Regulation of activated PAK-2p34 by proteasome mediated degradation | +0.51 |
| 10 | [[DNAJC7]] | Hedgehog 'on' state | +0.51 |
| 11 | [[CCDC117]] | Antigen processing: Ub, ATP-independent proteasomal degradation | +0.50 |

## + arm (71)

| Gene | Projection | Name |
|---|---|---|
| [[DNAJC7]] | 0.840 | DnaJ heat shock protein family (Hsp40) member C7 |
| [[PSMC1]] | 0.833 | proteasome 26S subunit, ATPase 1 |
| [[TYW3]] | 0.818 | tRNA-yW synthesizing protein 3 homolog |
| [[NUDT9]] | 0.798 | nudix hydrolase 9 |
| [[EFCAB7]] | 0.792 | EF-hand calcium binding domain 7 |
| [[MRPL45]] | 0.764 | mitochondrial ribosomal protein L45 |
| [[CUL5]] | 0.758 | cullin 5 |
| [[PSMD4]] | 0.745 | proteasome 26S subunit ubiquitin receptor, non-ATPase 4 |
| [[PSMD6]] | 0.737 | proteasome 26S subunit, non-ATPase 6 |
| [[MTA3]] | 0.722 | metastasis associated 1 family member 3 |
| [[TMLHE]] | 0.701 | trimethyllysine hydroxylase, epsilon |
| [[PSMC5]] | 0.701 | proteasome 26S subunit, ATPase 5 |
| [[TCTN1]] | 0.693 | tectonic family member 1 |
| [[SLC38A6]] | 0.687 | solute carrier family 38 member 6 |
| [[INTU]] | 0.680 | inturned planar cell polarity protein |
| [[DCTN4]] | 0.677 | dynactin subunit 4 |
| [[COPS2]] | 0.669 | COP9 signalosome subunit 2 |
| [[PSMA4]] | 0.669 | proteasome 20S subunit alpha 4 |
| [[UBXN4]] | 0.666 | UBX domain protein 4 |
| [[GAS8]] | 0.664 | dynein regulatory complex subunit 4 |
| [[RBSN]] | 0.653 | rabenosyn, RAB effector |
| [[RBM41]] | 0.648 | RNA binding motif protein 41 |
| [[LINC01278]] | 0.644 | long independently transcribed non-coding RNA 1278 |
| [[USP47]] | 0.638 | ubiquitin specific peptidase 47 |
| [[RHBDD3]] | 0.638 | rhomboid domain containing 3 |
| [[BBS1]] | 0.634 | Bardet-Biedl syndrome 1 |
| [[PGGT1B]] | 0.632 | protein geranylgeranyltransferase type I subunit beta |
| [[PFDN4]] | 0.627 | prefoldin subunit 4 |
| [[C19orf44]] | 0.620 | chromosome 19 open reading frame 44 |
| [[NRDE2]] | 0.618 | NRDE-2, necessary for RNA interference, domain containing |
| [[PPID]] | 0.617 | peptidylprolyl isomerase D |
| [[PIGB]] | 0.614 | phosphatidylinositol glycan anchor biosynthesis class B |
| [[PSMD3]] | 0.607 | proteasome 26S subunit, non-ATPase 3 |
| [[CAP2]] | 0.604 | cyclase associated actin cytoskeleton regulatory protein 2 |
| [[SPART]] | 0.600 | spartin |
| [[PSMB6]] | 0.600 | proteasome 20S subunit beta 6 |
| [[TTC1]] | 0.597 | tetratricopeptide repeat domain 1 |
| [[NSFL1C]] | 0.572 | NSFL1 cofactor |
| [[ANXA7]] | 0.564 | annexin A7 |
| [[DNAJC18]] | 0.556 | DnaJ heat shock protein family (Hsp40) member C18 |
| [[FAM217B]] | 0.551 | family with sequence similarity 217 member B |
| [[ACOT13]] | 0.536 | acyl-CoA thioesterase 13 |
| [[EHHADH]] | 0.535 | enoyl-CoA hydratase and 3-hydroxyacyl CoA dehydrogenase |
| [[RCC1L]] | 0.525 | RCC1 like |
| [[LMAN2L]] | 0.517 | lectin, mannose binding 2 like |
| [[CENATAC]] | 0.514 | centrosomal AT-AC splicing factor |
| [[SHLD1]] | 0.502 | shieldin complex subunit 1 |
| [[ZNF444]] | 0.501 | zinc finger protein 444 |
| [[IGHMBP2]] | 0.500 | immunoglobulin mu DNA binding protein 2 |
| [[ZRANB2]] | 0.497 | zinc finger RANBP2-type containing 2 |
| [[TP53BP1]] | 0.492 | tumor protein p53 binding protein 1 |
| [[IPP]] | 0.491 | kelch like family member 27 |
| [[PSMB5]] | 0.473 | proteasome 20S subunit beta 5 |
| [[CYB5R1]] | 0.471 | cytochrome b5 reductase 1 |
| [[CCDC117]] | 0.464 | coiled-coil domain containing 117 |
| [[UNKL]] | 0.461 | unk like zinc finger |
| [[ALG1]] | 0.460 | ALG1 chitobiosyldiphosphodolichol beta-mannosyltransferase |
| [[VPS29]] | 0.454 | VPS29 retromer complex component |
| [[DCTN2]] | 0.435 | dynactin subunit 2 |
| [[TIRAP]] | 0.429 | TIR domain containing adaptor protein |
| [[TXNDC9]] | 0.419 | thioredoxin domain containing 9 |
| [[PSMA5]] | 0.418 | proteasome 20S subunit alpha 5 |
| [[BLTP3B]] | 0.410 | bridge-like lipid transfer protein family member 3B |
| [[CAPZA1]] | 0.382 | capping actin protein of muscle Z-line subunit alpha 1 |
| [[METTL25]] | 0.369 | methyltransferase like 25 |
| [[CIAO3]] | 0.369 | cytosolic iron-sulfur assembly component 3 |
| [[TAB1]] | 0.325 | TGF-beta activated kinase 1 (MAP3K7) binding protein 1 |
| [[CPPED1]] | 0.314 | calcineurin like phosphoesterase domain containing 1 |
| [[IFT88]] | 0.271 | intraflagellar transport 88 |
| [[ZNF33B]] | 0.212 | zinc finger protein 33B |
| [[SENP7]] | 0.165 | SUMO specific peptidase 7 |

## − arm (6)

| Gene | Projection | Name |
|---|---|---|
| [[RELL1]] | -0.623 | RELT like 1 |
| [[LINC01128]] | -0.606 | long independently transcribed non-coding RNA 1128 |
| [[CTBP2]] | -0.471 | C-terminal binding protein 2 |
| [[SRGAP2]] | -0.469 | SLIT-ROBO Rho GTPase activating protein 2 |
| [[PICALM]] | -0.366 | phosphatidylinositol binding clathrin assembly protein |
| [[SP3]] | -0.343 | Sp3 transcription factor |

## Data

- `graph/nodes.parquet` — module == 64; `graph/modules.parquet` — module == 64; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [63] (drug-dose × line)
