---
module: 74
type: "module"
n_genes: 63
n_plus: 63
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.34523531794548035
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 074

*63 genes (single-armed) · [[Module 074.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 73), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+7.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+3.7, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (+3.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (+1.7, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+1.7, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+1.6, ⚠ cell-cycle shift); [[GSK1059615 (drug)]] 0.5 µM (+1.5); [[NG25 (drug)]] 5 µM (+1.5, ⚠ cell-cycle shift); [[Resveratrol (drug)]] 5 µM (+1.3); [[Terfenadine (drug)]] 5 µM (+1.3); [[Bimiralisib (drug)]] 0.5 µM (+1.2); [[Temsirolimus (drug)]] 0.5 µM (+1.2); [[Entrectinib (drug)]] 5 µM (+1.2); [[XRK3F2 (drug)]] 0.5 µM (+1.2); [[Cobimetinib (drug)]] 5 µM (+1.1); [[Trametinib (drug)]] 0.5 µM (+1.1); [[Temsirolimus (drug)]] 5 µM (+1.1) (29 in all, 9 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM (-9.5, ⚠ unreliable plate only); [[Dinaciclib (drug)]] 5 µM (-4.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-4.7, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-733 (drug)]] 5 µM (-4.5); [[Dinaciclib (drug)]] 0.5 µM (-4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 5 µM (-4.3); [[Abemaciclib (drug)]] 5 µM (-4.0); [[EX229 (drug)]] 5 µM (-4.0); [[Topotecan (hydrochloride) (drug)]] 5 µM (-3.8, ⚠ toxic; cell-cycle shift); [[venetoclax (drug)]] 5 µM (-3.7); [[Abemaciclib (drug)]] 0.5 µM (-3.1); [[EX229 (drug)]] 0.05 µM (-2.6); [[EX229 (drug)]] 0.5 µM (-2.0); [[Belzutifan (drug)]] 5 µM (-1.9); [[Sapanisertib (drug)]] 0.5 µM (-1.8) (34 in all, 14 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[HT-29 (line)]], [[NCI-H23 (line)]], [[RKO (line)]], [[KATO III (line)]], [[MIA PaCa-2 (line)]], [[PANC-1 (line)]], [[LoVo (line)]]

## + arm (63)

| Gene | Projection | Name |
|---|---|---|
| [[CIR1]] | 0.848 | corepressor of RBPJ and splicing regulator |
| [[SYF2]] | 0.846 | SYF2 pre-mRNA splicing factor |
| [[SLU7]] | 0.843 | spliceosome associated SLU7 |
| [[AKAP9]] | 0.837 | A-kinase anchoring protein 9 |
| [[WDR48]] | 0.821 | WD repeat domain 48 |
| [[KMT2A]] | 0.801 | lysine methyltransferase 2A |
| [[RSF1]] | 0.795 | remodeling and spacing factor 1 |
| [[NBR1]] | 0.772 | NBR1 autophagy cargo receptor |
| [[GCC2]] | 0.767 | GRIP and coiled-coil domain containing 2 |
| [[UBXN1]] | 0.766 | UBX domain protein 1 |
| [[IK]] | 0.764 | IK cytokine |
| [[BOD1L1]] | 0.764 | biorientation of chromosomes in cell division 1 like 1 |
| [[UBE2B]] | 0.758 | ubiquitin conjugating enzyme E2 B |
| [[TRIM23]] | 0.748 | tripartite motif containing 23 |
| [[PHF3]] | 0.728 | PHD finger protein 3 |
| [[PNRC1]] | 0.721 | proline rich nuclear receptor coactivator 1 |
| [[CCDC186]] | 0.697 | coiled-coil domain containing 186 |
| [[ZRANB1]] | 0.696 | zinc finger RANBP2-type containing 1 |
| [[GOLGB1]] | 0.695 | golgin B1 |
| [[RAB13]] | 0.692 | RAB13, member RAS oncogene family |
| [[ZBTB20]] | 0.691 | zinc finger and BTB domain containing 20 |
| [[ANKRD12]] | 0.689 | ankyrin repeat domain 12 |
| [[XRN1]] | 0.683 | 5'-3' exoribonuclease 1 |
| [[WBP2]] | 0.681 | WW domain binding protein 2 |
| [[HDAC5]] | 0.666 | histone deacetylase 5 |
| [[CRBN]] | 0.659 | cereblon |
| [[TBC1D17]] | 0.657 | TBC1 domain family member 17 |
| [[NIPBL]] | 0.645 | NIPBL cohesin loading factor |
| [[SMDT1]] | 0.645 | single-pass membrane protein with aspartate rich tail 1 |
| [[YY1]] | 0.641 | YY1 transcription factor |
| [[UBE2N]] | -0.635 | ubiquitin conjugating enzyme E2 N |
| [[BCAS3]] | 0.630 | BCAS3 microtubule associated cell migration factor |
| [[YIPF3]] | 0.625 | Yip1 domain family member 3 |
| [[CCNDBP1]] | 0.617 | cyclin D1 binding protein 1 |
| [[YIPF4]] | 0.617 | Yip1 domain family member 4 |
| [[KDM5A]] | 0.604 | lysine demethylase 5A |
| [[BAZ2A]] | 0.592 | bromodomain adjacent to zinc finger domain 2A |
| [[DHX40]] | 0.589 | DEAH-box helicase 40 |
| [[PSMD10]] | 0.589 | proteasome 26S subunit, non-ATPase 10 |
| [[CDKN1C]] | 0.572 | cyclin dependent kinase inhibitor 1C |
| [[ANKHD1]] | 0.570 | ankyrin repeat and KH domain containing 1 |
| [[PHIP]] | 0.562 | PHIP subunit of CUL4-Ring ligase complex |
| [[UPF2]] | 0.552 | UPF2 regulator of nonsense mediated mRNA decay |
| [[WDR19]] | 0.546 | WD repeat domain 19 |
| [[CHMP5]] | 0.537 | charged multivesicular body protein 5 |
| [[ELOVL6]] | -0.532 | ELOVL fatty acid elongase 6 |
| [[FOXO3]] | 0.523 | forkhead box O3 |
| [[C11orf54]] | 0.510 | beta-keto-L-gulonate decarboxylase |
| [[MBD5]] | 0.486 | methyl-CpG binding domain protein 5 |
| [[ZNF106]] | 0.475 | zinc finger protein 106 |
| [[CHMP1B]] | 0.471 | charged multivesicular body protein 1B |
| [[NCOA1]] | 0.470 | nuclear receptor coactivator 1 |
| [[PRMT2]] | 0.469 | protein arginine methyltransferase 2 |
| [[MAP2K5]] | 0.467 | mitogen-activated protein kinase kinase 5 |
| [[BEX4]] | 0.463 | brain expressed X-linked 4 |
| [[BRWD1]] | 0.434 | bromodomain and WD repeat domain containing 1 |
| [[PAFAH1B1]] | 0.428 | platelet activating factor acetylhydrolase 1b regulatory subunit 1 |
| [[MOSPD1]] | 0.422 | motile sperm domain containing 1 |
| [[GOLGA7]] | 0.392 | golgin A7 |
| [[UBL7]] | 0.387 | ubiquitin like 7 |
| [[CCDC91]] | 0.314 | coiled-coil domain containing 91 |
| [[ATXN2]] | 0.290 | ataxin 2 |
| [[MEAF6]] | 0.282 | MYST/Esa1 associated factor 6 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 74; `graph/modules.parquet` — module == 74; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [73] (drug-dose × line)
