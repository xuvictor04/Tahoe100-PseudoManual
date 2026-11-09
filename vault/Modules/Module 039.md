---
module: 39
type: "module"
n_genes: 115
n_plus: 115
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.34668901562690735
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 039

*115 genes (single-armed) · [[Module 039.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 38), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (+8.8, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (+8.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.2, ⚠ cell-cycle shift); [[Filgotinib (drug)]] 5 µM (+4.5); [[Dinaciclib (drug)]] 5 µM (+4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (+4.2, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.9); [[Dinaciclib (drug)]] 0.05 µM (+3.8, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 0.05 µM (+3.4); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+3.4); [[Tucidinostat (drug)]] 5 µM (+2.5); [[ERK5-IN-2 (drug)]] 5 µM (+1.8); [[Demeclocycline (drug)]] 5 µM (+1.7); [[PF-06260933 (drug)]] 5 µM (+1.7); [[5-Azacytidine (drug)]] 5 µM (+1.6); [[GSK1059615 (drug)]] 5 µM (+1.6) (48 in all, 15 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.2, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[HI-TOPK-032 (drug)]] 0.05 µM (-2.6); [[Radotinib (drug)]] 5 µM (-2.5); [[Dimethyl fumarate (drug)]] 5 µM (-2.0); [[Belinostat (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Bexarotene (drug)]] 5 µM (-1.8); [[Pralsetinib (drug)]] 5 µM (-1.7); [[Dexamethasone (drug)]] 5 µM (-1.7); [[Infigratinib (drug)]] 0.05 µM (-1.6); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.4); [[LB-100 (drug)]] 0.05 µM (-1.4); [[Pimitespib (drug)]] 0.05 µM (-1.3) (43 in all, 11 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[NCI-H460 (line)]], [[NCI-H23 (line)]], [[MIA PaCa-2 (line)]], [[NCI-H1573 (line)]], [[LoVo (line)]], [[PANC-1 (line)]], [[SK-MEL-2 (line)]]

## + arm (115)

| Gene | Projection | Name |
|---|---|---|
| [[MYOCOS]] | 0.945 | myocilin opposite strand |
| [[SLC6A13]] | 0.930 | solute carrier family 6 member 13 |
| [[USP50]] | 0.923 | ubiquitin specific peptidase 50 |
| [[ALDH8A1]] | 0.915 | aldehyde dehydrogenase 8 family member A1 |
| [[ANKDD1B]] | 0.907 | ankyrin repeat and death domain containing 1B |
| [[LINC01191]] | 0.898 | long independently transcribed non-coding RNA 1191 |
| [[SLC22A14]] | 0.895 | solute carrier family 22 member 14 |
| [[C3orf20]] | 0.889 | family with sequence similarity 194 member C |
| [[CDKL4]] | 0.886 | cyclin dependent kinase like 4 |
| [[GARIN1A]] | 0.886 | golgi associated RAB2 interactor 1A |
| [[OIT3]] | 0.883 | oncoprotein induced transcript 3 |
| [[MPP4]] | 0.877 | MAGUK p55 scaffold protein 4 |
| [[GARIN1B]] | 0.876 | golgi associated RAB2 interactor 1B |
| [[IMPA1P1]] | 0.869 | inositol monophosphatase 1 pseudogene 1 |
| [[HCLS1]] | 0.869 | hematopoietic cell-specific Lyn substrate 1 |
| [[DPYS]] | 0.865 | dihydropyrimidinase |
| [[IMPG2]] | 0.863 | interphotoreceptor matrix proteoglycan 2 |
| [[TMEM236]] | 0.860 | transmembrane protein 236 |
| [[SLC22A1]] | 0.859 | solute carrier family 22 member 1 |
| [[SCUBE2]] | 0.855 | signal peptide, CUB domain and EGF like domain containing 2 |
| [[FAM151B]] | 0.850 | family with sequence similarity 151 member B |
| [[C21orf91-OT1]] | 0.846 | C21orf91 overlapping transcript 1 |
| [[GABRR2]] | 0.831 | gamma-aminobutyric acid type A receptor subunit rho2 |
| [[LINC01934]] | 0.828 | long independently transcribed non-coding RNA 1934 |
| [[SELPLG]] | 0.824 | selectin P ligand |
| [[MSH4]] | 0.822 | mutS homolog 4 |
| [[LINC02803]] | 0.819 | long independently transcribed non-coding RNA 2803 |
| [[PLAC8L1]] | 0.816 | PLAC8 like 1 |
| [[MFSD2B]] | 0.809 | MFSD2 lysolipid transporter B, sphingolipid |
| [[BAAT]] | 0.807 | bile acid-CoA:amino acid N-acyltransferase |
| [[LINC00486]] | 0.807 | long independently transcribed non-coding RNA 486 |
| [[BTG3-AS1]] | 0.800 | BTG3 antisense RNA 1 |
| [[LINC03016]] | 0.800 | long independently transcribed non-coding RNA 3016 |
| [[XG]] | 0.799 | Xg glycoprotein (Xg blood group) |
| [[LINC01031]] | 0.794 | long independently transcribed non-coding RNA 1031 |
| [[SPOCK2]] | 0.791 | SPARC (osteonectin), cwcv and kazal like domains proteoglycan 2 |
| [[FLACC1]] | 0.785 | flagellum associated containing coiled-coil domains 1 |
| [[LINC02798]] | 0.784 | long independently transcribed non-coding RNA 2798 |
| [[EFCAB8]] | 0.782 | EF-hand calcium binding domain 8 |
| [[YIPF7]] | 0.780 | Yip1 domain family member 7 |
| [[RAPSN]] | 0.780 | receptor associated protein of the synapse |
| [[CFAP70]] | 0.779 | cilia and flagella associated protein 70 |
| [[GCNA]] | 0.778 | germ cell nuclear acidic peptidase |
| [[LINC01030]] | 0.774 | long independently transcribed non-coding RNA 1030 |
| [[PHEX]] | 0.772 | phosphate regulating endopeptidase X-linked |
| [[TXK]] | 0.770 | TXK tyrosine kinase |
| [[LINC02631]] | 0.768 | long independently transcribed non-coding RNA 2631 |
| [[SLC5A11]] | 0.767 | solute carrier family 5 member 11 |
| [[SLC7A9]] | 0.758 | solute carrier family 7 member 9 |
| [[LINC01619]] | 0.753 | long independently transcribed non-coding RNA 1619 |
| [[TMED6]] | 0.753 | transmembrane p24 trafficking protein 6 |
| [[LMO7DN]] | 0.745 | LMO7 downstream neighbor |
| [[MIRLET7IHG]] | 0.744 | MIRLET7I host gene |
| [[SLC22A13]] | 0.736 | solute carrier family 22 member 13 |
| [[LRRC39]] | 0.733 | leucine rich repeat containing 39 |
| [[MYRFL]] | 0.733 | myelin regulatory factor like |
| [[ERI2]] | 0.731 | ERI1 exoribonuclease family member 2 |
| [[TIAM2]] | 0.717 | TIAM Rac1 associated GEF 2 |
| [[ADAM32]] | 0.710 | ADAM metallopeptidase domain 32 |
| [[LINC02363]] | 0.708 | long independently transcribed non-coding RNA 2363 |
| [[CLDN15]] | 0.706 | claudin 15 |
| [[TAGLN]] | 0.706 | transgelin |
| [[TRIM59]] | 0.705 | tripartite motif containing 59 |
| [[NEK10]] | 0.703 | NIMA related kinase 10 |
| [[TTC33]] | 0.700 | tetratricopeptide repeat domain 33 |
| [[SSUH2]] | 0.698 | ssu-2 homolog |
| [[LINC02362]] | 0.696 | long independently transcribed non-coding RNA 2362 |
| [[C3orf62]] | 0.694 | chromosome 3 open reading frame 62 |
| [[LINC01393]] | 0.691 | long independently transcribed non-coding RNA 1393 |
| [[PRC1-AS1]] | 0.688 | PRC1 antisense RNA 1 |
| [[EFCAB10]] | 0.683 | EF-hand calcium binding domain 10 |
| [[ITPR2-AS1]] | 0.675 | SSPN antisense RNA 1 |
| [[ABCA10]] | 0.672 | ATP binding cassette subfamily A member 10 |
| [[MYH15]] | 0.671 | myosin heavy chain 15 |
| [[ACOT12]] | 0.664 | acyl-CoA thioesterase 12 |
| [[B3GALT1-AS1]] | 0.661 | B3GALT1 antisense RNA 1 |
| [[CCDC181]] | 0.655 | coiled-coil domain containing 181 |
| [[CAVIN4]] | 0.650 | caveolae associated protein 4 |
| [[LINC00654]] | 0.639 | long independently transcribed non-coding RNA 654 |
| [[LINC02284]] | 0.639 | long independently transcribed non-coding RNA 2284 |
| [[SMCO2]] | 0.635 | single-pass membrane protein with coiled-coil domains 2 |
| [[ANKAR]] | 0.632 | ankyrin and armadillo repeat containing |
| [[CCDC162P]] | 0.627 | coiled-coil domain containing 162, pseudogene |
| [[LINC01355]] | 0.618 | long independently transcribed non-coding RNA 1355 |
| [[DGKI]] | 0.607 | diacylglycerol kinase iota |
| [[MOCS2-DT]] | 0.605 | MOCS2 divergent transcript |
| [[GPR156]] | 0.602 | G protein-coupled receptor 156 |
| [[SH3BP5-AS1]] | 0.597 | SH3BP5 antisense RNA 1 |
| [[TERB1]] | 0.593 | telomere repeat binding bouquet formation protein 1 |
| [[C9orf24]] | 0.593 | sperm microtubule inner protein 6 |
| [[POLN]] | 0.591 | DNA polymerase nu |
| [[KANSL1L-AS1]] | 0.586 | KANSL1L antisense RNA 1 |
| [[LRRC66]] | 0.583 | leucine rich repeat containing 66 |
| [[STON1]] | 0.573 | stonin 1 |
| [[GTF2IP14]] | 0.571 | general transcription factor IIi pseudogene 14 |
| [[MAP1LC3A]] | 0.563 | microtubule associated protein 1 light chain 3 alpha |
| [[CCDC144CP]] | 0.555 | coiled-coil domain containing 144C, pseudogene |
| [[SLC4A5]] | 0.549 | solute carrier family 4 member 5 |
| [[LINC01909]] | 0.545 | long independently transcribed non-coding RNA 1909 |
| [[MPPE1]] | -0.539 | metallophosphoesterase 1 |
| [[COQ3]] | 0.528 | coenzyme Q3, methyltransferase |
| [[LYG1]] | 0.516 | lysozyme g1 |
| [[GPRC5D-AS1]] | 0.515 | GPRC5D and HEBP1 antisense RNA 1 |
| [[RN7SL76P]] | 0.513 | RNA, 7SL, cytoplasmic 76, pseudogene |
| [[CD226]] | 0.512 | CD226 molecule |
| [[SPDYA]] | 0.479 | speedy/RINGO cell cycle regulator family member A |
| [[USP3-AS1]] | 0.474 | USP3 antisense RNA 1 |
| [[OGDH]] | 0.459 | oxoglutarate dehydrogenase |
| [[TTN-AS1]] | 0.458 | TTN antisense RNA 1 |
| [[APH1B]] | 0.458 | aph-1B gamma-secretase subunit |
| [[LPCAT3]] | -0.455 | lysophosphatidylcholine acyltransferase 3 |
| [[LARP1B]] | 0.455 | La ribonucleoprotein 1B |
| [[FHDC1]] | 0.453 | FH2 domain containing 1 |
| [[RIC8B]] | 0.440 | RIC8 guanine nucleotide exchange factor B |
| [[PPP2CB]] | 0.418 | protein phosphatase 2 catalytic subunit beta |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 39; `graph/modules.parquet` — module == 39; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [38] (drug-dose × line)
