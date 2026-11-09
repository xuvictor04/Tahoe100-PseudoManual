---
module: 117
type: "module"
n_genes: 41
n_plus: 41
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: "NRF2"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 117

*NRF2 · 41 genes (single-armed) · [[Module 117.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

Label from the validation stage: **NRF2** (control, q 4e-13; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | NRF2 | control | 8/41 | 147 | 4e-13 |
| + | NRF2 | control | 8/41 | 147 | 4e-13 |
| + | Nuclear events mediated by NFE2L2 | reactome | 7/41 | 30.3 | 2e-06 |
| all | Nuclear events mediated by NFE2L2 | reactome | 7/41 | 30.3 | 2e-06 |
| all | KEAP1-NFE2L2 pathway | reactome | 7/41 | 23.2 | 1e-05 |
| + | KEAP1-NFE2L2 pathway | reactome | 7/41 | 23.2 | 1e-05 |
| + | NFE2L2 regulating anti-oxidant/detoxification enzymes | reactome | 4/41 | 86.5 | 7e-05 |
| all | NFE2L2 regulating anti-oxidant/detoxification enzymes | reactome | 4/41 | 86.5 | 7e-05 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 116), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Auranofin (drug)]] 5 µM (+9.5); [[Bortezomib (drug)]] 0.05 µM (+8.8, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+8.3); [[Ixazomib citrate (drug)]] 5 µM (+8.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+6.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Bortezomib (drug)]] 5 µM (+3.8, ⚠ toxic; cell-cycle shift); [[Cobimetinib (drug)]] 5 µM (+3.7); [[Homoharringtonine (drug)]] 0.5 µM (+3.6, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.3); [[Bortezomib (drug)]] 0.5 µM (+3.3); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (+3.1); [[Binimetinib (drug)]] 5 µM (+2.7); [[Cobimetinib (drug)]] 0.5 µM (+2.7); [[Auranofin (drug)]] 0.5 µM (+2.6); [[Trametinib (drug)]] 0.5 µM (+2.6) (67 in all, 21 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM (-2.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-2.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-2.4, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-2.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-2.1, ⚠ cell-cycle shift); [[Mebendazole (drug)]] 5 µM (-1.9); [[Panobinostat (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[Dexamethasone (drug)]] 0.5 µM (-1.5); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-1.4, ⚠ cell-cycle shift); [[Fumaric acid (drug)]] 5 µM (-1.4); [[Pravastatin (sodium) (drug)]] 5 µM (-1.3); [[Dexamethasone (drug)]] 5 µM (-1.3); [[BAY1125976 (drug)]] 5 µM (-1.3); [[Goserelin (acetate) (drug)]] 5 µM (-1.2); [[Sapanisertib (drug)]] 5 µM (-1.2); [[APTO-253 (drug)]] 5 µM (-1.1); [[Ciclopirox (drug)]] 5 µM (-1.1) (29 in all, 14 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[COLO 205 (line)]], [[HOP62 (line)]], [[LS 180 (line)]], [[LoVo (line)]], [[KATO III (line)]], [[NCI-H1792 (line)]], [[HT-29 (line)]], [[HEC-1-A (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 20 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[NMRAL2P]] | NFE2L2 regulating anti-oxidant/detoxification enzymes | +0.66 |
| 2 | [[EID3]] | NFE2L2 regulating anti-oxidant/detoxification enzymes | +0.65 |
| 3 | [[PIR]] | Nuclear events mediated by NFE2L2 | +0.62 |
| 4 | [[NMRAL2P-1]] | NFE2L2 regulating anti-oxidant/detoxification enzymes | +0.61 |
| 5 | [[CYP4F11]] | Nuclear events mediated by NFE2L2 | +0.60 |
| 6 | [[AKR1C1]] | xenobiotic metabolism | +0.60 |
| 7 | [[ME1]] | NFE2L2 regulating anti-oxidant/detoxification enzymes | +0.60 |
| 8 | [[ABCC2]] | Synthesis of bile acids and bile salts via 27-hydroxycholesterol | +0.59 |
| 9 | [[VEGFD]] | NFE2L2 regulating anti-oxidant/detoxification enzymes | +0.59 |
| 10 | [[TRIM16L]] | NRF2 | +0.58 |
| 11 | [[LINC01564]] | NFE2L2 regulating anti-oxidant/detoxification enzymes | +0.57 |
| 12 | [[SEL1L3]] | NFE2L2 regulating anti-oxidant/detoxification enzymes | +0.57 |
| 13 | [[SLC7A11]] | NRF2 | +0.55 |
| 14 | [[PTGR1]] | Synthesis of bile acids and bile salts via 27-hydroxycholesterol | +0.54 |
| 15 | [[ALOX12P2-1]] | Nuclear events mediated by NFE2L2 | +0.52 |

## + arm (41)

| Gene | Projection | Name |
|---|---|---|
| [[TRIM16L]] | 0.856 | tripartite motif containing 16 like (pseudogene) |
| [[NMRAL2P-1]] | 0.840 | — |
| [[ME1]] | 0.807 | malic enzyme 1 |
| [[CYP4F11]] | 0.806 | cytochrome P450 family 4 subfamily F member 11 |
| [[NMRAL2P]] | 0.804 | NmrA like redox sensor 2, pseudogene |
| [[PIR]] | 0.803 | pirin |
| [[ABCC2]] | 0.795 | ATP binding cassette subfamily C member 2 |
| [[GCLM]] | 0.795 | glutamate-cysteine ligase modifier subunit |
| [[ALOX12P2-1]] | 0.782 | — |
| [[EGF]] | 0.777 | epidermal growth factor |
| [[VEGFD]] | 0.770 | vascular endothelial growth factor D |
| [[CAPS2]] | 0.755 | calcyphosine 2 |
| [[AKR1C1]] | 0.742 | aldo-keto reductase family 1 member C1 |
| [[SLC7A11]] | 0.736 | solute carrier family 7 member 11 |
| [[LRP1B]] | 0.727 | LDL receptor related protein 1B |
| [[AKR1C3]] | 0.707 | aldo-keto reductase family 1 member C3 |
| [[TXNRD1]] | 0.705 | thioredoxin reductase 1 |
| [[ZSCAN31]] | 0.705 | zinc finger and SCAN domain containing 31 |
| [[PSMD11]] | 0.696 | proteasome 26S subunit, non-ATPase 11 |
| [[TRIM16L-1]] | 0.688 | — |
| [[TRIM16]] | 0.687 | tripartite motif containing 16 |
| [[JAKMIP3]] | 0.687 | Janus kinase and microtubule interacting protein 3 |
| [[GNGT1]] | 0.686 | G protein subunit gamma transducin 1 |
| [[EID3]] | 0.655 | EP300 interacting inhibitor of differentiation 3 |
| [[PTGR1]] | 0.651 | prostaglandin reductase 1 |
| [[TDO2]] | 0.643 | tryptophan 2,3-dioxygenase |
| [[TLR6]] | 0.630 | toll like receptor 6 |
| [[LINC02328]] | 0.625 | long independently transcribed non-coding RNA 2328 |
| [[UCHL1]] | 0.599 | ubiquitin C-terminal hydrolase L1 |
| [[AKR1C2]] | 0.595 | aldo-keto reductase family 1 member C2 |
| [[HKDC1]] | 0.589 | hexokinase domain containing 1 |
| [[TLR1]] | 0.583 | toll like receptor 1 |
| [[GCNT2]] | 0.581 | glucosaminyl (N-acetyl) transferase 2 (I blood group) |
| [[LINC01564]] | 0.574 | long independently transcribed non-coding RNA 1564 |
| [[SEL1L3]] | 0.573 | SEL1L family member 3 |
| [[GCLC]] | 0.562 | glutamate-cysteine ligase catalytic subunit |
| [[MAP1A]] | 0.556 | microtubule associated protein 1A |
| [[XKR9]] | 0.483 | XK related 9 |
| [[PRKACB]] | 0.473 | protein kinase cAMP-activated catalytic subunit beta |
| [[ATF6]] | 0.369 | activating transcription factor 6 |
| [[ADCY7]] | 0.332 | adenylate cyclase 7 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 117; `graph/modules.parquet` — module == 117; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [116] (drug-dose × line)
