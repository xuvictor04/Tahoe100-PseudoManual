---
module: 65
type: "module"
n_genes: 76
n_plus: 56
n_minus: 20
arms_opposite: true
mean_cos_between_arms: -0.2865532338619232
label: "BBSome-mediated cargo-targeting to cilium"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 065

*BBSome-mediated cargo-targeting to cilium · 76 genes (56 in the + arm, 20 in the − arm) · [[Module 065.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **BBSome-mediated cargo-targeting to cilium** (reactome, q 0.021; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | BBSome-mediated cargo-targeting to cilium | reactome | 3/56 | 40.4 | 0.021 |
| all | BBSome-mediated cargo-targeting to cilium | reactome | 3/76 | 29.8 | 0.046 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 64), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Belinostat (drug)]] 5 µM (+7.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+7.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+6.7, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.4, ⚠ cell-cycle shift); [[Radotinib (drug)]] 5 µM (+4.2); [[NG25 (drug)]] 5 µM (+4.0, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (+3.8); [[Verteporfin (drug)]] 5 µM (+3.5); [[Tucidinostat (drug)]] 5 µM (+3.4); [[Brivudine (drug)]] 5 µM (+3.3); [[Cabozantinib (S-malate) (drug)]] 5 µM (+2.8); [[Flumatinib (mesylate) (drug)]] 5 µM (+2.5); [[Dimethyl fumarate (drug)]] 5 µM (+2.2); [[Ponatinib (drug)]] 0.05 µM (+2.0); [[Ponatinib (drug)]] 0.5 µM (+1.9) (70 in all, 13 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-17.4, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-10.7, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-9.5); [[Harringtonine (drug)]] 5 µM (-9.5, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-9.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-8.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-8.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-7.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-5.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.5, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-4.2); [[Peretinoin (drug)]] 5 µM (-3.9); [[5-Azacytidine (drug)]] 5 µM (-3.6); [[Ixazomib citrate (drug)]] 0.5 µM (-3.5); [[Temsirolimus (drug)]] 0.05 µM (-2.9); [[Peretinoin (drug)]] 0.5 µM (-2.8); [[Rapamycin (drug)]] 5 µM (-2.7); [[Belumosudil (drug)]] 5 µM (-2.6); [[Homoharringtonine (drug)]] 0.05 µM (-2.5) (129 in all, 39 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[HOP62 (line)]], [[AsPC-1 (line)]], [[A-172 (line)]], [[NCI-H2347 (line)]], [[PANC-1 (line)]], [[HS-578T (line)]], [[SNU-423 (line)]]

## + arm (56)

| Gene | Projection | Name |
|---|---|---|
| [[ALG9]] | 0.867 | ALG9 alpha-1,2-mannosyltransferase |
| [[ANAPC4]] | 0.839 | anaphase promoting complex subunit 4 |
| [[ATG4C]] | 0.831 | autophagy related 4C cysteine peptidase |
| [[PRMT9]] | 0.829 | protein arginine methyltransferase 9 |
| [[VDAC3]] | 0.817 | voltage dependent anion channel 3 |
| [[MINDY3]] | 0.814 | MINDY lysine 48 deubiquitinase 3 |
| [[ORC4]] | 0.805 | origin recognition complex subunit 4 |
| [[LRIG2]] | 0.788 | leucine rich repeats and immunoglobulin like domains 2 |
| [[HACE1]] | 0.787 | HECT domain and ankyrin repeat containing E3 ubiquitin protein ligase 1 |
| [[ABHD10]] | 0.777 | abhydrolase domain containing 10, depalmitoylase |
| [[KCTD6]] | 0.776 | potassium channel tetramerization domain containing 6 |
| [[MTX2]] | 0.773 | metaxin 2 |
| [[ARL6]] | 0.768 | ARF like GTPase 6 |
| [[MRS2]] | 0.748 | magnesium transporter MRS2 |
| [[DUSP11]] | 0.748 | dual specificity phosphatase 11 |
| [[SDHAF3]] | 0.735 | succinate dehydrogenase complex assembly factor 3 |
| [[POGLUT2]] | 0.729 | protein O-glucosyltransferase 2 |
| [[EXD2]] | 0.719 | exonuclease 3'-5' domain containing 2 |
| [[FAM168A]] | 0.715 | family with sequence similarity 168 member A |
| [[REPS1]] | 0.713 | RALBP1 associated Eps domain containing 1 |
| [[ARNT]] | 0.713 | aryl hydrocarbon receptor nuclear translocator |
| [[LTA4H]] | 0.709 | leukotriene A4 hydrolase |
| [[MRPL39]] | 0.691 | mitochondrial ribosomal protein L39 |
| [[TM7SF3]] | 0.690 | transmembrane 7 superfamily member 3 |
| [[UBA5]] | 0.690 | ubiquitin like modifier activating enzyme 5 |
| [[NDUFV2]] | 0.683 | NADH:ubiquinone oxidoreductase core subunit V2 |
| [[KIF3A]] | 0.678 | kinesin family member 3A |
| [[TSNAX]] | 0.676 | translin associated factor X |
| [[C6orf136]] | 0.673 | chromosome 6 open reading frame 136 |
| [[CMC1]] | 0.671 | C-X9-C motif containing 1 |
| [[SLC35A1]] | 0.669 | solute carrier family 35 member A1 |
| [[FIG4]] | 0.668 | FIG4 phosphoinositide 5-phosphatase |
| [[BBS2]] | 0.666 | Bardet-Biedl syndrome 2 |
| [[EDEM2]] | 0.651 | ER degradation enhancing alpha-mannosidase like protein 2 |
| [[PGAP1]] | 0.648 | post-GPI attachment to proteins inositol deacylase 1 |
| [[FIP1L1]] | 0.640 | factor interacting with PAPOLA and CPSF1 |
| [[VPS33B]] | 0.639 | VPS33B late endosome and lysosome associated |
| [[NUP54]] | 0.637 | nucleoporin 54 |
| [[RNF145]] | 0.625 | ring finger protein 145 |
| [[LRRC40]] | 0.622 | leucine rich repeat containing 40 |
| [[CASC3]] | 0.620 | CASC3 exon junction complex subunit |
| [[MTF2]] | 0.617 | metal response element binding transcription factor 2 |
| [[HIBADH]] | 0.588 | 3-hydroxyisobutyrate dehydrogenase |
| [[ACP1]] | 0.583 | acid phosphatase 1 |
| [[SNX27]] | 0.583 | sorting nexin 27 |
| [[PXK]] | 0.564 | PX domain containing serine/threonine kinase like |
| [[FAM168B]] | 0.417 | family with sequence similarity 168 member B |
| [[TAFAZZIN]] | 0.414 | tafazzin, phospholipid-lysophospholipid transacylase |
| [[WDR41]] | 0.403 | WD repeat domain 41 |
| [[TTC21B]] | 0.398 | tetratricopeptide repeat domain 21B |
| [[GNA13]] | 0.396 | G protein subunit alpha 13 |
| [[DIPK1A]] | 0.372 | divergent protein kinase domain 1A |
| [[BBS7]] | 0.364 | Bardet-Biedl syndrome 7 |
| [[CDC16]] | 0.364 | cell division cycle 16 |
| [[ZDHHC6]] | 0.311 | zDHHC palmitoyltransferase 6 |
| [[TRAK2]] | 0.0780 | trafficking kinesin protein 2 |

## − arm (20)

| Gene | Projection | Name |
|---|---|---|
| [[ANKLE2]] | -0.715 | ankyrin repeat and LEM domain containing 2 |
| [[NPIPB4]] | -0.668 | nuclear pore complex interacting protein family member B4 |
| [[NPIPB5]] | -0.617 | nuclear pore complex interacting protein family member B5 |
| [[DGKH]] | -0.608 | diacylglycerol kinase eta |
| [[PEPD]] | -0.595 | peptidase D |
| [[OSTM1]] | -0.591 | osteoclastogenesis associated transmembrane protein 1 |
| [[WSB2]] | -0.582 | WD repeat and SOCS box containing 2 |
| [[PKNOX1]] | -0.567 | PBX/knotted 1 homeobox 1 |
| [[ZNF469]] | -0.543 | zinc finger protein 469 |
| [[AP5B1]] | -0.529 | adaptor related protein complex 5 subunit beta 1 |
| [[FER]] | -0.483 | FER tyrosine kinase |
| [[PVR]] | -0.450 | PVR cell adhesion molecule |
| [[USP34]] | -0.430 | ubiquitin specific peptidase 34 |
| [[CSNK1A1]] | -0.429 | casein kinase 1 alpha 1 |
| [[SLC36A1]] | -0.407 | solute carrier family 36 member 1 |
| [[PEA15]] | -0.406 | proliferation and apoptosis adaptor protein 15 |
| [[DEGS1]] | -0.397 | delta 4-desaturase, sphingolipid 1 |
| [[MICALL1]] | -0.380 | MICAL like 1 |
| [[SIK3]] | -0.327 | SIK family kinase 3 |
| [[CCSER2]] | -0.162 | coiled-coil serine rich protein 2 |

## Data

- `graph/nodes.parquet` — module == 65; `graph/modules.parquet` — module == 65; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [64] (drug-dose × line)
