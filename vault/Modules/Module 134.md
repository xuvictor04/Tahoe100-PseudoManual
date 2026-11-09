---
module: 134
type: "module"
n_genes: 35
n_plus: 35
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 134

*35 genes (single-armed) · [[Module 134.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Reelin signalling pathway | reactome | 2/35 | 172 | 0.021 |
| + | Reelin signalling pathway | reactome | 2/35 | 172 | 0.021 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 133), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Tucidinostat (drug)]] 5 µM (+3.9); [[Belinostat (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+3.7, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+2.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 0.5 µM (+2.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+2.5, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+2.4, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (+2.4); [[Brivudine (drug)]] 5 µM (+2.4); [[Dimethyl fumarate (drug)]] 5 µM (+1.7); [[Roxadustat (drug)]] 5 µM (+1.7); [[Tomivosertib (drug)]] 5 µM (+1.3); [[Fumaric acid (drug)]] 5 µM (+1.3); [[Irinotecan (hydrochloride) (drug)]] 0.5 µM (+1.3); [[HI-TOPK-032 (drug)]] 5 µM (+1.3); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (+1.2) (20 in all, 7 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-14.3, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-10.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-10.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-10.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-9.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-7.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 5 µM (-5.6, ⚠ toxic; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (-4.9, ⚠ toxic; cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-3.5, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.5); [[Belumosudil (drug)]] 5 µM (-2.4); [[Clobetasol propionate (drug)]] 0.05 µM (-1.7); [[Homoharringtonine (drug)]] 0.05 µM (-1.7); [[Binimetinib (drug)]] 0.05 µM (-1.6); [[Trametinib (drug)]] 0.5 µM (-1.5); [[Retinoic acid (drug)]] 0.05 µM (-1.4); [[Pralsetinib (drug)]] 5 µM (-1.4); [[Bimiralisib (drug)]] 0.5 µM (-1.3); [[Temsirolimus (drug)]] 0.05 µM (-1.3) (57 in all, 26 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[C32 (line)]], [[LOX-IMVI (line)]], [[SK-MEL-2 (line)]], [[J82 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[C-33 A (line)]], [[NCI-H1792 (line)]]

## + arm (35)

| Gene | Projection | Name |
|---|---|---|
| [[KIAA1958]] | 0.828 | KIAA1958 |
| [[FAM117B]] | 0.808 | family with sequence similarity 117 member B |
| [[HK1]] | 0.801 | hexokinase 1 |
| [[CHSY1]] | 0.798 | chondroitin sulfate synthase 1 |
| [[PDXP]] | 0.795 | pyridoxal phosphatase |
| [[CABIN1]] | 0.789 | calcineurin binding protein 1 |
| [[SLC2A3]] | 0.769 | solute carrier family 2 member 3 |
| [[FAM234B]] | 0.761 | family with sequence similarity 234 member B |
| [[SERGEF]] | 0.760 | secretion regulating guanine nucleotide exchange factor |
| [[ATRN]] | 0.756 | attractin |
| [[PLEKHA8]] | 0.754 | pleckstrin homology domain containing A8 |
| [[TENT4A]] | 0.734 | terminal nucleotidyltransferase 4A |
| [[RIMKLA]] | 0.726 | ribosomal modification protein rimK like family member A |
| [[SNX25]] | 0.705 | sorting nexin 25 |
| [[DNAJC5]] | 0.702 | DnaJ heat shock protein family (Hsp40) member C5 |
| [[RNF126]] | 0.690 | ring finger protein 126 |
| [[FBL]] | 0.667 | fibrillarin rRNA 2'-O-methyltransferase |
| [[VLDLR]] | 0.664 | very low density lipoprotein receptor |
| [[DDHD1]] | 0.663 | DDHD domain containing 1 |
| [[VDAC1]] | 0.660 | voltage dependent anion channel 1 |
| [[TFB1M]] | 0.659 | transcription factor B1, mitochondrial |
| [[RERE]] | 0.631 | arginine-glutamic acid dipeptide repeats |
| [[SNX14]] | 0.630 | sorting nexin 14 |
| [[CACNB4]] | 0.621 | calcium voltage-gated channel auxiliary subunit beta 4 |
| [[SH3GL3]] | 0.619 | SH3 domain containing GRB2 like 3, endophilin A3 |
| [[FYN]] | 0.617 | FYN proto-oncogene, Src family tyrosine kinase |
| [[AGAP1]] | 0.606 | ArfGAP with GTPase domain, ankyrin repeat and PH domain 1 |
| [[NDUFB8]] | 0.605 | NADH:ubiquinone oxidoreductase subunit B8 |
| [[MGAT5]] | 0.574 | alpha-1,6-mannosylglycoprotein 6-beta-N-acetylglucosaminyltransferase |
| [[EIF4A1]] | 0.562 | eukaryotic translation initiation factor 4A1 |
| [[INTS13]] | 0.533 | integrator complex subunit 13 |
| [[JARID2]] | 0.503 | jumonji and AT-rich interaction domain containing 2 |
| [[PREP]] | 0.503 | prolyl endopeptidase |
| [[PHF12]] | 0.430 | PHD finger protein 12 |
| [[NSF]] | 0.400 | N-ethylmaleimide sensitive factor, vesicle fusing ATPase |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 134; `graph/modules.parquet` — module == 134; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [133] (drug-dose × line)
