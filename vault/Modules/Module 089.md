---
module: 89
type: "module"
n_genes: 51
n_plus: 51
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3286953866481781
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 089

*51 genes (single-armed) · [[Module 089.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Mitochondrial transcription | reactome | 2/51 | 118 | 0.040 |
| + | Mitochondrial transcription | reactome | 2/51 | 118 | 0.040 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 88), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Selinexor (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (+3.8, ⚠ toxic; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.4); [[Ponatinib (drug)]] 5 µM (+2.5); [[Selinexor (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+2.3, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.1); [[Ponatinib (drug)]] 0.5 µM (+1.9); [[Cabozantinib (S-malate) (drug)]] 5 µM (+1.7); [[TAK-901 (drug)]] 5 µM (+1.6, ⚠ cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+1.6); [[Trametinib (drug)]] 0.05 µM (+1.5); [[Binimetinib (drug)]] 0.05 µM (+1.4); [[Clobetasol propionate (drug)]] 0.5 µM (+1.4); [[Bimiralisib (drug)]] 0.05 µM (+1.3) (37 in all, 14 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-4.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-4.2, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-3.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (-2.3); [[Digitoxin (drug)]] 5 µM (-2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-2.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.0, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-2.0, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-1.5); [[Cyclosporin A (drug)]] 0.05 µM (-1.4); [[Clopidogrel (drug)]] 0.05 µM (-1.4); [[PF-06260933 (drug)]] 5 µM (-1.3); [[Peretinoin (drug)]] 5 µM (-1.1) (20 in all, 14 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[RKO (line)]], [[NCI-H1573 (line)]], [[SW480 (line)]], [[PANC-1 (line)]], [[NCI-H460 (line)]], [[KATO III (line)]], [[SK-MEL-2 (line)]]

## + arm (51)

| Gene | Projection | Name |
|---|---|---|
| [[TEFM]] | 0.870 | transcription elongation factor, mitochondrial |
| [[PAAF1]] | 0.801 | proteasomal ATPase associated factor 1 |
| [[SLC25A17]] | 0.796 | solute carrier family 25 member 17 |
| [[ALKBH3]] | 0.790 | alkB homolog 3, alpha-ketoglutarate dependent dioxygenase |
| [[MAFIP]] | 0.780 | MAFF interacting protein |
| [[METTL22]] | 0.776 | methyltransferase 22, Kin17 lysine |
| [[POLL]] | 0.769 | DNA polymerase lambda |
| [[ZSCAN25]] | 0.768 | zinc finger and SCAN domain containing 25 |
| [[ZNF383]] | 0.763 | zinc finger protein 383 |
| [[VPS33A]] | 0.758 | VPS33A core subunit of CORVET and HOPS complexes |
| [[ZNF234]] | 0.738 | zinc finger protein 234 |
| [[POLR3F]] | 0.732 | RNA polymerase III subunit F |
| [[ZNF573]] | 0.717 | zinc finger protein 573 |
| [[COA6]] | 0.713 | cytochrome c oxidase assembly factor 6 |
| [[UQCC1]] | 0.699 | ubiquinol-cytochrome c reductase complex assembly factor 1 |
| [[MTERF4]] | 0.698 | mitochondrial transcription termination factor 4 |
| [[ZNF133]] | 0.691 | zinc finger protein 133 |
| [[ZNF790]] | 0.681 | zinc finger protein 790 |
| [[ELMOD3]] | 0.674 | ELMO domain containing 3 |
| [[TMEM79]] | 0.655 | transmembrane protein 79 |
| [[WDR73]] | 0.654 | WD repeat domain 73 |
| [[MIX23]] | 0.650 | mitochondrial matrix import factor 23 |
| [[TBP]] | 0.630 | TATA-box binding protein |
| [[TEKT4P2-1]] | 0.625 | — |
| [[IREB2]] | 0.621 | iron responsive element binding protein 2 |
| [[ZNF283]] | 0.617 | zinc finger protein 283 |
| [[ZKSCAN4]] | 0.615 | zinc finger with KRAB and SCAN domains 4 |
| [[ZNF302]] | 0.615 | zinc finger protein 302 |
| [[MTERF1]] | 0.615 | mitochondrial transcription termination factor 1 |
| [[ZNF493]] | 0.612 | zinc finger protein 493 |
| [[APTX]] | 0.600 | aprataxin |
| [[CRY1]] | -0.589 | cryptochrome circadian regulator 1 |
| [[TDG]] | 0.583 | thymine DNA glycosylase |
| [[RNPC3]] | 0.579 | RNA binding region (RNP1, RRM) containing 3 |
| [[TMEM234]] | 0.567 | transmembrane protein 234 |
| [[FBXL9P]] | 0.539 | F-box and leucine rich repeat protein 9, pseudogene |
| [[VPS39]] | 0.535 | VPS39 subunit of HOPS complex |
| [[PEX11A]] | 0.535 | peroxisomal biogenesis factor 11 alpha |
| [[TM2D1]] | 0.531 | TM2 domain containing 1 |
| [[SMN2]] | 0.527 | survival of motor neuron 2, centromeric |
| [[C12orf4]] | 0.525 | FERRY endosomal RAB5 effector complex subunit 3 |
| [[LINC01535]] | 0.523 | long independently transcribed non-coding RNA 1535 |
| [[HYCC1]] | -0.519 | hyccin PI4KA lipid kinase complex subunit 1 |
| [[HEXD]] | 0.501 | hexosaminidase D |
| [[LINC00665]] | 0.492 | long independently transcribed non-coding RNA 665 |
| [[PCGF3]] | 0.486 | polycomb group ring finger 3 |
| [[IQCK]] | 0.447 | IQ motif containing K |
| [[CLK2]] | 0.395 | CDC like kinase 2 |
| [[KIF9-AS1]] | 0.382 | KIF9 antisense RNA 1 |
| [[TMEM223]] | 0.327 | transmembrane protein 223 |
| [[FBXL14]] | 0.217 | F-box and leucine rich repeat protein 14 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 89; `graph/modules.parquet` — module == 89; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [88] (drug-dose × line)
