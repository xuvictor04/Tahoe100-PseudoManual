---
module: 14
type: "module"
n_genes: 212
n_plus: 212
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.20021173357963562
label: "TNF-alpha signaling via NF-kB"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 014

*TNF-alpha signaling via NF-kB · 212 genes (single-armed) · [[Module 014.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **TNF-alpha signaling via NF-kB** (hallmark, q 3e-36; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | TNF-alpha signaling via NF-kB | hallmark | 43/212 | 16.3 | 3e-36 |
| + | TNF-alpha signaling via NF-kB | hallmark | 43/212 | 16.3 | 3e-36 |
| + | NF-kB | control | 12/212 | 56.9 | 6e-17 |
| all | NF-kB | control | 12/212 | 56.9 | 6e-17 |
| all | inflammatory response | hallmark | 22/212 | 11.3 | 8e-14 |
| + | inflammatory response | hallmark | 22/212 | 11.3 | 8e-14 |
| + | Cytokine Signaling in Immune system | reactome | 35/212 | 3.78 | 1e-08 |
| all | Cytokine Signaling in Immune system | reactome | 35/212 | 3.78 | 1e-08 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 13), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+17.8, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+10.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+7.1, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.8); [[TAK-901 (drug)]] 5 µM (+4.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+4.2, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+3.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (+3.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+2.6, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+1.8); [[Homoharringtonine (drug)]] 0.05 µM (+1.6); [[Binimetinib (drug)]] 5 µM (+1.5); [[Trametinib (drug)]] 0.5 µM (+1.3); [[PH-797804 (drug)]] 5 µM (+1.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+1.2); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (+1.1); [[Radotinib (drug)]] 5 µM (+1.1); [[XRK3F2 (drug)]] 0.5 µM (+1.1) (32 in all, 19 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Auranofin (drug)]] 5 µM (-2.9); [[Panobinostat (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-2.0, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (-1.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (-1.7, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (-1.6); [[Ixazomib citrate (drug)]] 0.5 µM (-1.5); [[Dexamethasone (drug)]] 0.5 µM (-1.5); [[Belinostat (drug)]] 5 µM (-1.3, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (-1.3, ⚠ cell-cycle shift); [[Clobetasol propionate (drug)]] 0.5 µM (-1.3); [[Clobetasol propionate (drug)]] 5 µM (-1.2); [[Dexamethasone (drug)]] 0.05 µM (-1.2); [[Budesonide (drug)]] 5 µM (-1.2); [[Triamcinolone (drug)]] 0.5 µM (-1.1) (16 in all, 7 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[A-172 (line)]], [[NCI-H460 (line)]], [[J82 (line)]], [[HS-578T (line)]], [[A498 (line)]], [[HEC-1-A (line)]], [[HOP62 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 30 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[TNFAIP2]] | Chemokine receptors bind chemokines | +0.59 |
| 2 | [[BCL3]] | NF-kB | +0.59 |
| 3 | [[IRF1]] | NF-kB | +0.59 |
| 4 | [[CX3CL1]] | NF-kB | +0.58 |
| 5 | [[LINC02605]] | Chemokine receptors bind chemokines | +0.57 |
| 6 | [[RELB]] | IkBA variant leads to EDA-ID | +0.57 |
| 7 | [[CXCL2]] | IkBA variant leads to EDA-ID | +0.57 |
| 8 | [[HIVEP2]] | NF-kB | +0.57 |
| 9 | [[CSF1]] | NF-kB | +0.56 |
| 10 | [[ZC3H12A]] | NF-kB | +0.55 |
| 11 | [[CXCL3]] | Interleukin-10 signaling | +0.55 |
| 12 | [[TNFAIP3]] | IkBA variant leads to EDA-ID | +0.54 |
| 13 | [[STAT5A]] | NF-kB | +0.54 |
| 14 | [[REL]] | NF-kB | +0.54 |
| 15 | [[NFKBIA]] | Nucleotide-binding domain, leucine rich repeat containing receptor (NLR) signaling pathways | +0.53 |

## + arm (212)

| Gene | Projection | Name |
|---|---|---|
| [[TNFAIP2]] | 0.872 | TNF alpha induced protein 2 |
| [[BCL3]] | 0.832 | BCL3 transcription coactivator |
| [[CX3CL1]] | 0.815 | C-X3-C motif chemokine ligand 1 |
| [[SLC2A6]] | 0.797 | solute carrier family 2 member 6 |
| [[NINJ1]] | 0.784 | ninjurin 1 |
| [[STAT5A]] | 0.783 | signal transducer and activator of transcription 5A |
| [[CCL5]] | 0.771 | C-C motif chemokine ligand 5 |
| [[NEURL3]] | 0.766 | neuralized E3 ubiquitin protein ligase 3 |
| [[CSF1]] | 0.759 | colony stimulating factor 1 |
| [[IRF1]] | 0.756 | interferon regulatory factor 1 |
| [[BTN2A2]] | 0.751 | butyrophilin subfamily 2 member A2 |
| [[NFKBIA]] | 0.743 | NFKB inhibitor alpha |
| [[TIFA]] | 0.737 | TRAF interacting protein with forkhead associated domain |
| [[LINC02605]] | 0.731 | long independently transcribed non-coding RNA 2605 |
| [[CXCL3]] | 0.729 | C-X-C motif chemokine ligand 3 |
| [[STAP2]] | 0.729 | signal transducing adaptor family member 2 |
| [[NFKB2]] | 0.727 | nuclear factor kappa B subunit 2 |
| [[IKBKE]] | 0.723 | inhibitor of nuclear factor kappa B kinase subunit epsilon |
| [[REL]] | 0.719 | REL proto-oncogene, NF-kB subunit |
| [[DRAM1]] | 0.718 | DNA damage regulated autophagy modulator 1 |
| [[SLC6A7]] | 0.717 | solute carrier family 6 member 7 |
| [[SYNPO]] | 0.717 | synaptopodin |
| [[NFKBIE]] | 0.715 | NFKB inhibitor epsilon |
| [[RASGRP1]] | 0.714 | RAS guanyl releasing protein 1 |
| [[TEF]] | 0.713 | TEF transcription factor, PAR bZIP family member |
| [[DENND2B]] | 0.711 | DENN domain containing 2B |
| [[CXCL2]] | 0.705 | C-X-C motif chemokine ligand 2 |
| [[IL32]] | 0.704 | interleukin 32 |
| [[S100A3]] | 0.702 | S100 calcium binding protein A3 |
| [[MARCKS]] | 0.694 | myristoylated alanine rich protein kinase C substrate |
| [[EFNA1]] | 0.690 | ephrin A1 |
| [[RRAD]] | 0.690 | RRAD, Ras related glycolysis inhibitor and calcium channel regulator |
| [[TNIP1]] | 0.689 | TNFAIP3 interacting protein 1 |
| [[NR1D1]] | 0.684 | nuclear receptor subfamily 1 group D member 1 |
| [[TNFRSF9]] | 0.684 | TNF receptor superfamily member 9 |
| [[ANO9]] | 0.683 | anoctamin 9 |
| [[GATA6]] | 0.683 | GATA binding protein 6 |
| [[IFNGR2]] | 0.682 | interferon gamma receptor 2 |
| [[EBI3]] | 0.682 | Epstein-Barr virus induced 3 |
| [[KMO]] | 0.680 | kynurenine 3-monooxygenase |
| [[CGNL1]] | 0.680 | cingulin like 1 |
| [[CCL2]] | 0.674 | C-C motif chemokine ligand 2 |
| [[LTB]] | 0.674 | lymphotoxin beta |
| [[ANKRD33B]] | 0.674 | ankyrin repeat domain 33B |
| [[STX11]] | 0.673 | syntaxin 11 |
| [[ATP23]] | 0.672 | ATP23 metallopeptidase and ATP synthase assembly factor homolog |
| [[ARHGEF40]] | 0.671 | Rho guanine nucleotide exchange factor 40 |
| [[NUAK2]] | 0.667 | NUAK family kinase 2 |
| [[BCOR]] | 0.666 | BCL6 corepressor |
| [[LITAF]] | 0.666 | lipopolysaccharide induced TNF factor |
| [[ADORA2A]] | 0.661 | adenosine A2a receptor |
| [[CD70]] | 0.661 | CD70 molecule |
| [[TNFAIP6]] | 0.659 | TNF alpha induced protein 6 |
| [[FAM111A-DT]] | 0.658 | FAM111A divergent transcript |
| [[CD83]] | 0.654 | CD83 molecule |
| [[GATM]] | 0.652 | glycine amidinotransferase |
| [[MAP3K8]] | 0.651 | mitogen-activated protein kinase kinase kinase 8 |
| [[RELB]] | 0.650 | RELB proto-oncogene, NF-kB subunit |
| [[LGALS3]] | 0.649 | galectin 3 |
| [[PRR14]] | 0.647 | proline rich 14 |
| [[BHLHE41]] | 0.639 | basic helix-loop-helix family member e41 |
| [[RARG]] | 0.638 | retinoic acid receptor gamma |
| [[DDR1]] | 0.638 | discoidin domain receptor tyrosine kinase 1 |
| [[NKX3-1]] | 0.635 | NK3 homeobox 1 |
| [[CCDC148]] | 0.634 | coiled-coil domain containing 148 |
| [[C1QTNF1]] | 0.631 | C1q and TNF related 1 |
| [[ZC3H12A]] | 0.625 | zinc finger CCCH-type containing 12A |
| [[RASSF5]] | 0.624 | Ras association domain family member 5 |
| [[HIVEP2]] | 0.622 | HIVEP zinc finger 2 |
| [[C1QTNF1-AS1]] | 0.622 | C1QTNF1 antisense RNA 1 |
| [[TNFAIP3]] | 0.621 | TNF alpha induced protein 3 |
| [[OGFRL1]] | 0.621 | opioid growth factor receptor like 1 |
| [[USP43]] | 0.617 | ubiquitin specific peptidase 43 |
| [[SERPINB7]] | 0.616 | serpin family B member 7 |
| [[SLC39A1]] | 0.614 | solute carrier family 39 member 1 |
| [[IRF2]] | 0.613 | interferon regulatory factor 2 |
| [[GPR108]] | 0.609 | G protein-coupled receptor 108 |
| [[NFKB1]] | 0.607 | nuclear factor kappa B subunit 1 |
| [[RHOV]] | 0.607 | ras homolog family member V |
| [[ADGRG1]] | 0.604 | adhesion G protein-coupled receptor G1 |
| [[NFIX]] | 0.604 | nuclear factor I X |
| [[RIPK2]] | 0.600 | receptor interacting serine/threonine kinase 2 |
| [[VCAM1]] | 0.600 | vascular cell adhesion molecule 1 |
| [[COL16A1]] | 0.600 | collagen type XVI alpha 1 chain |
| [[NDRG2]] | 0.599 | NDRG family member 2 |
| [[BHLHE40]] | 0.599 | basic helix-loop-helix family member e40 |
| [[PAXIP1-DT]] | 0.599 | PAXIP1 divergent transcript |
| [[MAK]] | 0.593 | male germ cell associated kinase |
| [[MB21D2]] | 0.592 | Mab-21 domain containing 2 |
| [[CD40]] | 0.590 | CD40 molecule |
| [[SLC41A2]] | 0.589 | solute carrier family 41 member 2 |
| [[WTAP]] | 0.587 | WT1 associated protein |
| [[CXCL1]] | 0.587 | C-X-C motif chemokine ligand 1 |
| [[SSTR2]] | 0.586 | somatostatin receptor 2 |
| [[CADM1]] | 0.586 | cell adhesion molecule 1 |
| [[NFKBIZ]] | 0.585 | NFKB inhibitor zeta |
| [[MSC]] | 0.585 | musculin |
| [[BAHCC1]] | 0.584 | BAH domain and coiled-coil containing 1 |
| [[ZNF385C]] | 0.583 | zinc finger protein 385C |
| [[RND1]] | 0.579 | Rho family GTPase 1 |
| [[RAB32]] | 0.575 | RAB32, member RAS oncogene family |
| [[SMAD7]] | 0.573 | SMAD family member 7 |
| [[ABCG2]] | 0.573 | ATP binding cassette subfamily G member 2 (JR blood group) |
| [[NOD2]] | 0.572 | nucleotide binding oligomerization domain containing 2 |
| [[PLPP3]] | 0.570 | phospholipid phosphatase 3 |
| [[SLC50A1]] | 0.567 | solute carrier family 50 member 1 |
| [[DMRTA1]] | 0.566 | DMRT like family A1 |
| [[SYNGAP1]] | 0.565 | synaptic Ras GTPase activating protein 1 |
| [[KLF10]] | 0.565 | KLF transcription factor 10 |
| [[CPAMD8]] | 0.564 | C3 and PZP like alpha-2-macroglobulin domain containing 8 |
| [[NR3C1]] | 0.564 | nuclear receptor subfamily 3 group C member 1 |
| [[SLC12A7]] | 0.564 | solute carrier family 12 member 7 |
| [[FCHSD2]] | 0.563 | FCH and double SH3 domains 2 |
| [[PBX2]] | 0.562 | PBX homeobox 2 |
| [[IL15]] | 0.560 | interleukin 15 |
| [[TSPAN15]] | 0.557 | tetraspanin 15 |
| [[NFATC2]] | 0.557 | nuclear factor of activated T cells 2 |
| [[PLEKHG3]] | 0.557 | pleckstrin homology and RhoGEF domain containing G3 |
| [[CLDN1]] | 0.556 | claudin 1 |
| [[BDKRB2]] | 0.553 | bradykinin receptor B2 |
| [[SAV1]] | 0.553 | salvador family WW domain containing protein 1 |
| [[IRAG2]] | 0.552 | inositol 1,4,5-triphosphate receptor associated 2 |
| [[ELOVL7]] | 0.549 | ELOVL fatty acid elongase 7 |
| [[C15orf48]] | 0.548 | cytochrome c oxidase associated subunit FA4L3 |
| [[TLCD1]] | 0.548 | TLC domain containing 1 |
| [[PLXNB2]] | 0.548 | plexin B2 |
| [[BCL9L]] | 0.546 | BCL9 like |
| [[HMSD]] | 0.546 | histocompatibility minor serpin domain containing |
| [[IFNAR2]] | 0.545 | interferon alpha and beta receptor subunit 2 |
| [[ICAM1]] | 0.545 | intercellular adhesion molecule 1 |
| [[ZDHHC23]] | 0.545 | zDHHC palmitoyltransferase 23 |
| [[TSPAN2]] | 0.544 | tetraspanin 2 |
| [[GALT]] | 0.538 | galactose-1-phosphate uridylyltransferase |
| [[ARRDC3]] | 0.538 | arrestin domain containing 3 |
| [[PATL1]] | 0.538 | PAT1 homolog 1, processing body mRNA decay factor |
| [[CIART]] | 0.537 | circadian associated repressor of transcription |
| [[IL6]] | 0.537 | interleukin 6 |
| [[TRAF4]] | 0.536 | TNF receptor associated factor 4 |
| [[BIRC2]] | 0.529 | baculoviral IAP repeat containing 2 |
| [[SLCO5A1]] | 0.528 | solute carrier organic anion transporter family member 5A1 |
| [[CDKN2B]] | 0.526 | cyclin dependent kinase inhibitor 2B |
| [[ZNF318]] | 0.525 | zinc finger protein 318 |
| [[SLCO3A1]] | 0.521 | solute carrier organic anion transporter family member 3A1 |
| [[TNFRSF14]] | 0.521 | TNF receptor superfamily member 14 |
| [[TMEM63B]] | 0.520 | transmembrane protein 63B |
| [[LRRC49]] | 0.517 | leucine rich repeat containing 49 |
| [[NUAK1]] | 0.516 | NUAK family kinase 1 |
| [[PER2]] | 0.511 | period circadian regulator 2 |
| [[SBNO2]] | 0.509 | strawberry notch homolog 2 |
| [[RAB29]] | 0.505 | RAB29, member RAS oncogene family |
| [[TNFRSF1B]] | 0.503 | TNF receptor superfamily member 1B |
| [[ECH1]] | 0.501 | enoyl-CoA hydratase 1 |
| [[TBC1D9]] | 0.501 | TBC1 domain family member 9 |
| [[PER3]] | 0.494 | period circadian regulator 3 |
| [[ACKR3]] | 0.493 | atypical chemokine receptor 3 |
| [[CDC14A]] | 0.491 | cell division cycle 14A |
| [[CYB561]] | 0.491 | cytochrome b561 |
| [[QKI]] | 0.491 | QKI, KH domain containing RNA binding |
| [[CCDC24]] | 0.484 | coiled-coil domain containing 24 |
| [[TNKS1BP1]] | 0.482 | CCR4-NOT transcription complex subunit 12 |
| [[LHFPL6]] | 0.482 | LHFPL tetraspan subfamily member 6 |
| [[BTG3]] | 0.478 | BTG anti-proliferation factor 3 |
| [[BASP1]] | 0.475 | brain abundant membrane attached signal protein 1 |
| [[ZNF217]] | 0.474 | zinc finger protein 217 |
| [[PPP4R4]] | 0.472 | protein phosphatase 4 regulatory subunit 4 |
| [[SOCS3]] | 0.472 | suppressor of cytokine signaling 3 |
| [[CDKN2A]] | 0.472 | cyclin dependent kinase inhibitor 2A |
| [[IRF2BPL]] | 0.464 | interferon regulatory factor 2 binding protein like |
| [[ARRB1]] | 0.463 | arrestin beta 1 |
| [[CSF3]] | 0.462 | colony stimulating factor 3 |
| [[PTX3]] | 0.458 | pentraxin 3 |
| [[LRRN1]] | 0.456 | leucine rich repeat neuronal 1 |
| [[CCNL1]] | 0.455 | cyclin L1 |
| [[HLF]] | 0.451 | HLF transcription factor, PAR bZIP family member |
| [[IFT57]] | 0.451 | intraflagellar transport 57 |
| [[SHISAL1]] | 0.447 | shisa like 1 |
| [[RTN4RL2]] | 0.446 | reticulon 4 receptor like 2 |
| [[MICOS10]] | 0.443 | mitochondrial contact site and cristae organizing system subunit 10 |
| [[RNF144B]] | 0.439 | ring finger protein 144B |
| [[PPP1R15B]] | 0.437 | protein phosphatase 1 regulatory subunit 15B |
| [[UVRAG]] | 0.436 | UV radiation resistance associated |
| [[CNTNAP1]] | 0.435 | contactin associated protein 1 |
| [[GSE1]] | 0.434 | Gse1 coiled-coil protein |
| [[PTP4A3]] | 0.433 | protein tyrosine phosphatase 4A3 |
| [[YBX3]] | 0.433 | Y-box binding protein 3 |
| [[SMPD2]] | 0.430 | sphingomyelin phosphodiesterase 2 |
| [[HLA-L-1]] | 0.426 | — |
| [[CPNE8]] | 0.420 | copine 8 |
| [[S100A4]] | 0.419 | S100 calcium binding protein A4 |
| [[SSH2]] | 0.419 | slingshot protein phosphatase 2 |
| [[MAF]] | 0.419 | MAF bZIP transcription factor |
| [[CYRIA]] | 0.417 | CYFIP related Rac1 interactor A |
| [[LSP1P4]] | -0.415 | LSP1 pseudogene 4 |
| [[ABTB2]] | 0.400 | ankyrin repeat and BTB domain containing 2 |
| [[IKBKB]] | 0.394 | inhibitor of nuclear factor kappa B kinase subunit beta |
| [[TMPRSS5]] | -0.393 | transmembrane serine protease 5 |
| [[RAB3IP]] | 0.393 | RAB3A interacting protein |
| [[USP12]] | 0.389 | ubiquitin specific peptidase 12 |
| [[OR4F15]] | 0.381 | olfactory receptor family 4 subfamily F member 15 |
| [[MIDEAS]] | 0.373 | mitotic deacetylase associated SANT domain protein |
| [[TP53BP2]] | 0.363 | tumor protein p53 binding protein 2 |
| [[SLC30A4]] | 0.362 | solute carrier family 30 member 4 |
| [[TRMT2B]] | -0.357 | tRNA methyltransferase 2B |
| [[CD47]] | 0.355 | CD47 molecule |
| [[ONECUT2]] | 0.346 | one cut homeobox 2 |
| [[LYST]] | 0.343 | lysosomal trafficking regulator |
| [[ARHGAP40]] | 0.333 | Rho GTPase activating protein 40 |
| [[CXCL5]] | 0.326 | C-X-C motif chemokine ligand 5 |
| [[UBR5-DT]] | 0.309 | UBR5 divergent transcript |
| [[TLCD5]] | 0.308 | TLC domain containing 5 |
| [[BID]] | 0.303 | BH3 interacting domain death agonist |
| [[BDH1]] | -0.253 | 3-hydroxybutyrate dehydrogenase 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 14; `graph/modules.parquet` — module == 14; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [13] (drug-dose × line)
