---
module: 122
type: "module"
n_genes: 40
n_plus: 40
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "Transferrin endocytosis and recycling"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 122

*Transferrin endocytosis and recycling · 40 genes (single-armed) · [[Module 122.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **Transferrin endocytosis and recycling** (reactome, q 0.022; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Transferrin endocytosis and recycling | reactome | 3/40 | 40.4 | 0.022 |
| + | Transferrin endocytosis and recycling | reactome | 3/40 | 40.4 | 0.022 |
| all | Glycosphingolipid catabolism | reactome | 3/40 | 39.0 | 0.024 |
| + | Glycosphingolipid catabolism | reactome | 3/40 | 39.0 | 0.024 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 121), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+8.9, ⚠ cell-cycle shift); [[Selinexor (drug)]] 5 µM (+6.5, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (+5.7); [[Ouabain (Octahydrate) (drug)]] 5 µM (+5.0, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+4.0, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+3.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+3.1, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+2.8); [[Ponatinib (drug)]] 5 µM (+2.5); [[Afatinib (drug)]] 5 µM (+2.1); [[Osimertinib (mesylate) (drug)]] 5 µM (+2.0); [[Rapamycin (drug)]] 5 µM (+1.9); [[Temsirolimus (drug)]] 5 µM (+1.8); [[Bimiralisib (drug)]] 5 µM (+1.7); [[Belumosudil (drug)]] 5 µM (+1.7); [[Cobimetinib (drug)]] 5 µM (+1.6) (73 in all, 32 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)
- Lower it: [[Tucidinostat (drug)]] 5 µM (-5.0); [[Tucidinostat (drug)]] 0.5 µM (-3.6, ⚠ cell-cycle shift); [[PF-06260933 (drug)]] 5 µM (-1.9); [[Harringtonine (drug)]] 0.5 µM (-1.5, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.05 µM (-1.3); [[Harringtonine (drug)]] 0.05 µM (-1.1); [[Verteporfin (drug)]] 5 µM (-1.1) (7 in all, 2 with an alert ⚠)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[J82 (line)]], [[PANC-1 (line)]], [[A-172 (line)]], [[NCI-H1573 (line)]], [[KATO III (line)]], [[COLO 205 (line)]], [[Hs 766T (line)]]

## + arm (40)

| Gene | Projection | Name |
|---|---|---|
| [[WASHC2C]] | 0.866 | WASH complex subunit 2C |
| [[HEXA]] | 0.847 | hexosaminidase subunit alpha |
| [[WASHC2A]] | 0.843 | WASH complex subunit 2A |
| [[ATP6V1C1]] | 0.823 | ATPase H+ transporting V1 subunit C1 |
| [[VPS11]] | 0.822 | VPS11 core subunit of CORVET and HOPS complexes |
| [[CLN3]] | 0.774 | CLN3 lysosomal/endosomal transmembrane protein, battenin |
| [[SPNS1]] | 0.773 | SPNS lysolipid transporter 1, lysophospholipid |
| [[GLMP]] | 0.746 | glycosylated lysosomal membrane protein |
| [[RRAGB]] | 0.743 | Ras related GTP binding B |
| [[TPP1]] | 0.741 | tripeptidyl peptidase 1 |
| [[TSC1]] | 0.713 | TSC complex subunit 1 |
| [[VPS41]] | 0.703 | VPS41 subunit of HOPS complex |
| [[ZFYVE26]] | 0.700 | zinc finger FYVE-type containing 26 |
| [[ATP6V1H]] | 0.697 | ATPase H+ transporting V1 subunit H |
| [[AP5Z1]] | 0.691 | adaptor related protein complex 5 subunit zeta 1 |
| [[MCOLN1]] | 0.676 | mucolipin TRP cation channel 1 |
| [[GET3]] | 0.674 | guided entry of tail-anchored proteins factor 3, ATPase |
| [[DPP7]] | 0.666 | dipeptidyl peptidase 7 |
| [[GBA1]] | 0.661 | glucosylceramidase beta 1 |
| [[MCCC1]] | 0.644 | methylcrotonyl-CoA carboxylase subunit 1 |
| [[WASHC5]] | 0.640 | WASH complex subunit 5 |
| [[SPG21]] | 0.637 | SPG21 abhydrolase domain containing, maspardin |
| [[IGF2R]] | 0.625 | insulin like growth factor 2 receptor |
| [[DVL2]] | 0.624 | dishevelled segment polarity protein 2 |
| [[ARFGEF2]] | 0.619 | ARF guanine nucleotide exchange factor 2 |
| [[TRAPPC2L]] | 0.611 | trafficking protein particle complex subunit 2L |
| [[NAGPA]] | 0.609 | N-acetylglucosamine-1-phosphodiester alpha-N-acetylglucosaminidase |
| [[CTSA]] | 0.607 | cathepsin A |
| [[BOD1]] | 0.591 | biorientation of chromosomes in cell division 1 |
| [[GNPTG]] | 0.574 | N-acetylglucosamine-1-phosphate transferase subunit gamma |
| [[TMEM126B]] | 0.568 | transmembrane protein 126B |
| [[SLC26A11]] | 0.561 | solute carrier family 26 member 11 |
| [[HPS4]] | 0.559 | HPS4 biogenesis of lysosomal organelles complex 3 subunit 2 |
| [[ARMCX1]] | 0.549 | armadillo repeat containing X-linked 1 |
| [[HS1BP3]] | 0.542 | HCLS1 binding protein 3 |
| [[CTNS]] | 0.528 | cystinosin, lysosomal cystine transporter |
| [[VPS26A]] | 0.520 | VPS26 retromer complex component A |
| [[BLOC1S6]] | 0.480 | biogenesis of lysosomal organelles complex 1 subunit 6 |
| [[PLPBP]] | 0.477 | pyridoxal phosphate binding protein |
| [[RCBTB1]] | 0.448 | RCC1 and BTB domain containing protein 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 122; `graph/modules.parquet` — module == 122; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [121] (drug-dose × line)
