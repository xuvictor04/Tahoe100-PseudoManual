---
module: 58
type: "module"
n_genes: 80
n_plus: 80
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3545856177806854
label: "oxidative phosphorylation"
label_source: "hallmark"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 058

*oxidative phosphorylation · 80 genes (single-armed) · [[Module 058.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **oxidative phosphorylation** (hallmark, q 5e-07; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | oxidative phosphorylation | hallmark | 12/80 | 11.3 | 5e-07 |
| + | oxidative phosphorylation | hallmark | 12/80 | 11.3 | 5e-07 |
| all | Aerobic respiration and respiratory electron transport | reactome | 12/80 | 9.79 | 3e-06 |
| + | Aerobic respiration and respiratory electron transport | reactome | 12/80 | 9.79 | 3e-06 |
| + | Complex I biogenesis | reactome | 7/80 | 21.3 | 3e-05 |
| all | Complex I biogenesis | reactome | 7/80 | 21.3 | 3e-05 |
| all | Respiratory electron transport | reactome | 9/80 | 12.0 | 4e-05 |
| + | Respiratory electron transport | reactome | 9/80 | 12.0 | 4e-05 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 57), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+7.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Docetaxel (drug)]] 0.05 µM (+4.0, ⚠ transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+3.0, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+2.7, ⚠ toxic; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+2.6, ⚠ toxic; cell-cycle shift); [[Belinostat (drug)]] 5 µM (+2.5, ⚠ cell-cycle shift); [[Bendamustine (drug)]] 5 µM (+2.2); [[Arbutin (drug)]] 5 µM (+2.1); [[9-ING-41 (drug)]] 0.5 µM (+2.1); [[XRK3F2 (drug)]] 0.5 µM (+2.1); [[vincristine (drug)]] 0.5 µM (+1.8); [[Azithromycin (hydrate) (drug)]] 5 µM (+1.8); [[Ipatasertib (drug)]] 0.5 µM (+1.7); [[Sulfatinib (drug)]] 5 µM (+1.7); [[Celecoxib (drug)]] 0.5 µM (+1.7); [[Thymol (drug)]] 5 µM (+1.7) (98 in all, 23 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-3.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-2.3, ⚠ cell-cycle shift); [[Lucanthone (drug)]] 0.05 µM (-2.1); [[Fenofibrate (drug)]] 0.05 µM (-2.1); [[Sapanisertib (drug)]] 5 µM (-2.1); [[Diphenhydramine (drug)]] 0.05 µM (-2.1); [[GSK1059615 (drug)]] 5 µM (-2.1); [[Tirabrutinib (drug)]] 0.05 µM (-1.9); [[Erlotinib (drug)]] 0.05 µM (-1.9); [[BAY1125976 (drug)]] 5 µM (-1.8); [[Hydroxyurea (drug)]] 5 µM (-1.8); [[TAK-901 (drug)]] 0.05 µM (-1.7) (113 in all, 19 with an alert ⚠; shown: the 10 strongest and the 2 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[KATO III (line)]], [[SK-MEL-2 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[HT-29 (line)]], [[CFPAC-1 (line)]], [[HOP62 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 19 candidates, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[TMEM160]] | Complex I biogenesis | +0.66 |  |
| 2 | [[C19orf53]] | Complex I biogenesis | +0.64 |  |
| 3 | [[MRPL12]] | Cristae formation | +0.63 |  |
| 4 | [[ANTKMT]] | Cristae formation | +0.60 |  |
| 5 | [[MRPL41]] ⚠ | Cristae formation | +0.60 | ⚠ in the vector space only through drug-doses that carry an alert |
| 6 | [[TMEM147]] | Cristae formation | +0.59 |  |
| 7 | [[CENPX]] | Complex I biogenesis | +0.57 |  |
| 8 | [[NDUFA3]] | Cristae formation | +0.57 |  |
| 9 | [[NAA10]] ⚠ | Cristae formation | +0.56 | ⚠ in the vector space only through drug-doses that carry an alert |
| 10 | [[TMEM256]] | Cristae formation | +0.56 |  |
| 11 | [[APRT]] | Cristae formation | +0.55 |  |
| 12 | [[NDUFB3]] | Cristae formation | +0.51 |  |
| 13 | [[MICOS13]] | oxidative phosphorylation | +0.51 |  |
| 14 | [[TMEM141]] | Complex I biogenesis | +0.51 |  |
| 15 | [[METRN]] | Cristae formation | +0.51 |  |
| 16 | [[ATP5MC1]] | Respiratory electron transport | +0.51 |  |
| 17 | [[SLC39A4]] | Cristae formation | +0.50 |  |

*⚠ 8 of its 80 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (80)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[ANTKMT]] | 0.916 | adenine nucleotide translocase lysine methyltransferase |  |
| [[MICOS13]] | 0.862 | mitochondrial contact site and cristae organizing system subunit 13 |  |
| [[TMEM160]] | 0.835 | transmembrane protein 160 |  |
| [[MRPL41]] | 0.822 | mitochondrial ribosomal protein L41 | ⚠ only flagged evidence |
| [[TMEM256]] | 0.815 | transmembrane protein 256 |  |
| [[NDUFA3]] | 0.777 | NADH:ubiquinone oxidoreductase subunit A3 |  |
| [[TMEM276]] | 0.776 | transmembrane protein 276 |  |
| [[NME3]] | 0.776 | NME/NM23 nucleoside diphosphate kinase 3 |  |
| [[PAXX]] | 0.771 | PAXX non-homologous end joining factor | ⚠ only flagged evidence |
| [[ATP5F1D]] | 0.763 | ATP synthase F1 subunit delta | ⚠ only flagged evidence |
| [[PUSL1]] | 0.749 | pseudouridine synthase like 1 |  |
| [[METRN]] | 0.739 | meteorin, glial cell differentiation regulator |  |
| [[SLC39A4]] | 0.737 | solute carrier family 39 member 4 |  |
| [[SNRNP25]] | 0.733 | small nuclear ribonucleoprotein U11/U12 subunit 25 |  |
| [[DUSP23]] | 0.718 | dual specificity phosphatase 23 |  |
| [[CENPX]] | 0.713 | centromere protein X |  |
| [[MRPL12]] | 0.711 | mitochondrial ribosomal protein L12 |  |
| [[STUB1]] | 0.709 | STIP1 homology and U-box containing protein 1 |  |
| [[NAA10]] | 0.707 | N-alpha-acetyltransferase 10, NatA catalytic subunit | ⚠ only flagged evidence |
| [[TSTD1]] | 0.704 | thiosulfate sulfurtransferase like domain containing 1 |  |
| [[TMEM191A-1]] | 0.691 | — |  |
| [[RAC3]] | 0.690 | Rac family small GTPase 3 |  |
| [[SCRN2]] | 0.684 | secernin 2 |  |
| [[NDUFS8]] | 0.682 | NADH:ubiquinone oxidoreductase core subunit S8 |  |
| [[GCHFR]] | 0.678 | GTP cyclohydrolase I feedback regulator |  |
| [[C19orf53]] | 0.674 | chromosome 19 open reading frame 53 |  |
| [[TMEM147]] | 0.668 | transmembrane protein 147 |  |
| [[POP5]] | 0.668 | POP5 ribonuclease P/MRP subunit |  |
| [[NDUFS7]] | 0.667 | NADH:ubiquinone oxidoreductase core subunit S7 |  |
| [[SLC25A11]] | 0.667 | solute carrier family 25 member 11 |  |
| [[TMEM141]] | 0.664 | transmembrane protein 141 |  |
| [[CDK5]] | 0.646 | cyclin dependent kinase 5 |  |
| [[NDUFB3]] | 0.634 | NADH:ubiquinone oxidoreductase subunit B3 |  |
| [[MFSD3]] | 0.625 | solute carrier family 33 member 2 |  |
| [[DDX39B]] | -0.622 | DExD-box helicase 39B |  |
| [[ATP5MC1]] | 0.621 | ATP synthase membrane subunit c locus 1 |  |
| [[COMTD1]] | 0.616 | catechol-O-methyltransferase domain containing 1 |  |
| [[REX1BD]] | 0.613 | required for excision 1-B domain containing |  |
| [[HAGHL]] | 0.611 | hydroxyacylglutathione hydrolase like |  |
| [[MCRIP2]] | 0.605 | MAPK regulated corepressor interacting protein 2 |  |
| [[SLC39A3]] | 0.596 | solute carrier family 39 member 3 |  |
| [[AKR7A2]] | 0.595 | aldo-keto reductase family 7 member A2 |  |
| [[RBM6]] | 0.584 | RNA binding motif protein 6 |  |
| [[NTHL1]] | 0.582 | nth like DNA glycosylase 1 |  |
| [[POLR3K]] | 0.577 | RNA polymerase III subunit K |  |
| [[APRT]] | 0.570 | adenine phosphoribosyltransferase |  |
| [[CYBA]] | 0.568 | cytochrome b-245 alpha chain |  |
| [[PTMAP2]] | 0.564 | prothymosin alpha pseudogene 2 | ⚠ only flagged evidence |
| [[SPATC1L]] | 0.564 | spermatogenesis and centriole associated 1 like |  |
| [[POLR2G]] | 0.557 | RNA polymerase II subunit G | ⚠ only flagged evidence |
| [[TMEM179B]] | 0.556 | transmembrane protein 179B |  |
| [[NDUFAB1]] | 0.552 | NADH:ubiquinone oxidoreductase subunit AB1 |  |
| [[NDUFS5]] | 0.552 | NADH:ubiquinone oxidoreductase subunit S5 |  |
| [[HTRA2]] | 0.546 | HtrA serine peptidase 2 |  |
| [[ATP5MC3]] | 0.542 | ATP synthase membrane subunit c locus 3 | ⚠ only flagged evidence |
| [[HSD17B10]] | 0.535 | hydroxysteroid 17-beta dehydrogenase 10 | ⚠ only flagged evidence |
| [[NDUFAF3]] | 0.527 | NADH:ubiquinone oxidoreductase complex assembly factor 3 |  |
| [[RPUSD1]] | 0.521 | RNA pseudouridine synthase domain containing 1 |  |
| [[HINT2]] | 0.520 | histidine triad nucleotide binding protein 2 |  |
| [[FAM104B]] | 0.518 | VCP nuclear cofactor family member 2 |  |
| [[CELF1]] | 0.502 | CUGBP Elav-like family member 1 |  |
| [[CYC1]] | 0.494 | cytochrome c1 |  |
| [[MRPL40]] | 0.485 | mitochondrial ribosomal protein L40 |  |
| [[CHD1]] | 0.483 | chromodomain helicase DNA binding protein 1 |  |
| [[PIGQ]] | 0.470 | phosphatidylinositol glycan anchor biosynthesis class Q |  |
| [[C19orf33]] | 0.463 | chromosome 19 open reading frame 33 |  |
| [[PRELID1]] | 0.458 | PRELI domain containing 1 |  |
| [[MRPL52]] | 0.454 | mitochondrial ribosomal protein L52 |  |
| [[SLC37A4]] | 0.450 | solute carrier family 37 member 4 |  |
| [[LSM7]] | 0.432 | LSM7 homolog, U6 small nuclear RNA and mRNA degradation associated |  |
| [[IGFBP2]] | 0.425 | insulin like growth factor binding protein 2 |  |
| [[EIF5AL1]] | 0.407 | eukaryotic translation initiation factor 5A like 1 |  |
| [[CRACR2B]] | 0.393 | calcium release activated channel regulator 2B |  |
| [[A2MP1]] | 0.387 | PZP alpha-2-macroglobulin like 2, pseudogene |  |
| [[CRIP1]] | 0.376 | cysteine rich protein 1 |  |
| [[PTMAP5]] | 0.376 | prothymosin alpha pseudogene 5 |  |
| [[PHF13]] | 0.335 | PHD finger protein 13 |  |
| [[MIF4GD]] | 0.332 | MIF4G domain containing |  |
| [[ATF7]] | 0.275 | activating transcription factor 7 |  |
| [[CST6]] | 0.189 | cystatin E/M |  |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 58; `graph/modules.parquet` — module == 58; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [57] (drug-dose × line)
