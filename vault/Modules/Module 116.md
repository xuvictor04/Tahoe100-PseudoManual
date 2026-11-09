---
module: 116
type: "module"
n_genes: 42
n_plus: 42
n_minus: 0
arms_opposite: false
mean_cos_between_arms: null
label: ""
label_source: ""
tags: ["module"]
generated_by: "tahoemap"
---

# Module 116

*42 genes (single-armed) · [[Module 116.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: all its genes lie on one side of its main direction.

No gene set is enriched enough to label it (`validation/module_labels.csv`).

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 115), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Homoharringtonine (drug)]] 5 µM (+6.9, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+5.3, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+5.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (+5.1, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+4.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+4.6); [[Auranofin (drug)]] 5 µM (+4.4); [[Daptomycin (drug)]] 5 µM (+3.8, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (+3.7); [[Vinblastine (sulfate) (drug)]] 5 µM (+3.6); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+2.8); [[Peretinoin (drug)]] 0.5 µM (+2.8); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+2.7); [[Homoharringtonine (drug)]] 0.05 µM (+2.6); [[vincristine (drug)]] 0.5 µM (+2.3); [[vincristine (drug)]] 5 µM (+2.2) (35 in all, 18 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)
- Lower it: [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-3.0); [[Panobinostat (drug)]] 0.5 µM (-2.9, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 5 µM (-2.8); [[Trametinib (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-2.7, ⚠ cell-cycle shift); [[Binimetinib (drug)]] 0.5 µM (-2.6); [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM (-2.5); [[Trametinib (drug)]] 0.5 µM (-2.5); [[Belinostat (drug)]] 5 µM (-2.3, ⚠ cell-cycle shift); [[Triamcinolone (drug)]] 5 µM (-2.2); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM (-2.1); [[Binimetinib (drug)]] 5 µM (-2.0); [[Triamcinolone (drug)]] 0.5 µM (-2.0); [[Clobetasol propionate (drug)]] 5 µM (-1.8) (46 in all, 7 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H23 (line)]], [[A-172 (line)]], [[RKO (line)]], [[MIA PaCa-2 (line)]], [[NCI-H1573 (line)]], [[C32 (line)]], [[HS-578T (line)]], [[HT-29 (line)]]

## + arm (42)

| Gene | Projection | Name |
|---|---|---|
| [[ADTRP]] | 0.841 | androgen dependent TFPI regulating protein |
| [[NAV3]] | 0.825 | neuron navigator 3 |
| [[LINC01204]] | 0.806 | long independently transcribed non-coding RNA 1204 |
| [[ITGB1-DT]] | 0.802 | ITGB1 divergent transcript |
| [[MARCHF4]] | 0.799 | membrane associated ring-CH-type finger 4 |
| [[ROBO4]] | 0.790 | roundabout guidance receptor 4 |
| [[LTBP2]] | 0.771 | latent transforming growth factor beta binding protein 2 |
| [[IL31RA]] | 0.765 | interleukin 31 receptor A |
| [[FRMD6]] | 0.754 | FERM domain containing 6 |
| [[RDUR]] | 0.741 | RIG-I dependent antiviral response regulator RNA |
| [[LNCOG]] | 0.716 | lncRNA osteogenesis associated |
| [[ETS1]] | 0.704 | ETS proto-oncogene 1, transcription factor |
| [[FGF1]] | 0.702 | fibroblast growth factor 1 |
| [[NABP1]] | 0.697 | nucleic acid binding protein 1 |
| [[CFAP299]] | 0.687 | cilia and flagella associated protein 299 |
| [[BMAL2]] | 0.687 | basic helix-loop-helix ARNT like 2 |
| [[RGS4]] | 0.675 | regulator of G protein signaling 4 |
| [[LINC00513]] | 0.670 | long independently transcribed non-coding RNA 513 |
| [[PDCD1LG2]] | 0.669 | programmed cell death 1 ligand 2 |
| [[MGLL]] | 0.627 | monoglyceride lipase |
| [[AJAP1]] | 0.620 | adherens junctions associated protein 1 |
| [[LCP1]] | 0.615 | lymphocyte cytosolic protein 1 |
| [[DUSP5-DT]] | 0.614 | DUSP5 divergent transcript |
| [[GJC1]] | 0.612 | gap junction protein gamma 1 |
| [[CCDC190]] | 0.603 | coiled-coil domain containing 190 |
| [[NEMP2]] | 0.597 | nuclear envelope integral membrane protein 2 |
| [[MIR31HG]] | 0.590 | MIR31 host gene |
| [[RAB3B]] | 0.586 | RAB3B, member RAS oncogene family |
| [[AXL]] | 0.585 | AXL receptor tyrosine kinase |
| [[EGFR]] | 0.576 | epidermal growth factor receptor |
| [[GALNT6]] | 0.573 | polypeptide N-acetylgalactosaminyltransferase 6 |
| [[LAMA1]] | 0.568 | laminin subunit alpha 1 |
| [[CNST]] | 0.566 | consortin, connexin sorting protein |
| [[LINC-PINT]] | 0.563 | long independently transcribed non-coding RNA, p53 induced transcript |
| [[LINC01426]] | 0.526 | long independently transcribed non-coding RNA 1426 |
| [[ASAP1]] | 0.506 | ArfGAP with SH3 domain, ankyrin repeat and PH domain 1 |
| [[CA13]] | 0.485 | carbonic anhydrase 13 |
| [[LINC01399]] | 0.480 | long independently transcribed non-coding RNA 1399 |
| [[CLDN11]] | 0.462 | claudin 11 |
| [[FEZ2]] | 0.454 | fasciculation and elongation protein zeta 2 |
| [[TRIO]] | 0.428 | trio Rho guanine nucleotide exchange factor |
| [[TNFAIP1]] | 0.427 | TNF alpha induced protein 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 116; `graph/modules.parquet` — module == 116; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [115] (drug-dose × line)
