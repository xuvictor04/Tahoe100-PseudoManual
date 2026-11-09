---
module: 45
type: "module"
n_genes: 102
n_plus: 93
n_minus: 9
arms_opposite: true
mean_cos_between_arms: -0.3121162950992584
label: "Iron uptake and transport"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 045

*Iron uptake and transport · 102 genes (93 in the + arm, 9 in the − arm) · [[Module 045.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Iron uptake and transport** (reactome, q 6e-04; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Iron uptake and transport | reactome | 6/93 | 17.7 | 6e-04 |
| all | Iron uptake and transport | reactome | 6/102 | 16.1 | 0.001 |
| + | Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy | reactome | 4/93 | 38.1 | 0.002 |
| all | Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy | reactome | 4/102 | 34.8 | 0.002 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 44), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Tucidinostat (drug)]] 5 µM (+6.5); [[Radotinib (drug)]] 5 µM (+6.5); [[Ponatinib (drug)]] 5 µM (+5.8); [[Selinexor (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Tucidinostat (drug)]] 0.5 µM (+4.9, ⚠ cell-cycle shift); [[NG25 (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Selinexor (drug)]] 0.5 µM (+4.0, ⚠ cell-cycle shift); [[Cabozantinib (S-malate) (drug)]] 5 µM (+3.6); [[Panobinostat (drug)]] 0.05 µM (+3.3, ⚠ cell-cycle shift); [[Ponatinib (drug)]] 0.05 µM (+3.1); [[Cobimetinib (drug)]] 5 µM (+3.0); [[Terfenadine (drug)]] 5 µM (+2.9); [[Osimertinib (mesylate) (drug)]] 5 µM (+2.9); [[Ponatinib (drug)]] 0.5 µM (+2.8); [[Brivudine (drug)]] 5 µM (+2.6) (138 in all, 27 with an alert ⚠; shown: the 10 strongest and the 5 next strongest without an alert)
- Lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM (-9.5, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-8.4, ⚠ cell-cycle shift); [[Auranofin (drug)]] 5 µM (-7.1); [[Homoharringtonine (drug)]] 0.5 µM (-6.6, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-6.3, ⚠ unreliable plate only); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-5.7); [[5-Azacytidine (drug)]] 5 µM (-4.6); [[Doxorubicin (hydrochloride) (drug)]] 5 µM (-4.5, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Daptomycin (drug)]] 0.5 µM (-3.3, ⚠ unreliable plate only); [[Peretinoin (drug)]] 5 µM (-3.2); [[Homoharringtonine (drug)]] 0.05 µM (-3.0); [[Demeclocycline (drug)]] 5 µM (-2.5); [[TAK-733 (drug)]] 5 µM (-2.5); [[c-Kit-IN-1 (drug)]] 5 µM (-2.4); [[Cinacalcet (drug)]] 5 µM (-2.3); [[Busulfan (drug)]] 0.05 µM (-2.3) (155 in all, 29 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[NCI-H460 (line)]], [[PANC-1 (line)]], [[Hs 766T (line)]], [[C32 (line)]], [[NCI-H2347 (line)]], [[NCI-H2030 (line)]], [[NCI-H1573 (line)]], [[AsPC-1 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 5 candidates, none with an alert.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[SCPEP1]] | Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy | +0.54 |
| 2 | [[CAT]] | Iron uptake and transport | +0.53 |
| 3 | [[SLC25A23]] | Iron uptake and transport | +0.51 |
| 4 | [[GSTM4]] | Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy | +0.50 |
| 5 | [[TMEM14A]] | Iron uptake and transport | +0.50 |

## + arm (93)

| Gene | Projection | Name |
|---|---|---|
| [[CAT]] | 0.859 | catalase |
| [[HMGN3]] | 0.802 | high mobility group nucleosomal binding domain 3 |
| [[TMEM14A]] | 0.802 | transmembrane protein 14A |
| [[KBTBD3]] | 0.777 | kelch repeat and BTB domain containing 3 |
| [[SLC25A23]] | 0.769 | solute carrier family 25 member 23 |
| [[LMBRD1]] | 0.765 | LMBR1 domain containing 1 |
| [[SNX2]] | 0.756 | sorting nexin 2 |
| [[SCPEP1]] | 0.750 | serine carboxypeptidase 1 |
| [[ALAD]] | 0.746 | aminolevulinate dehydratase |
| [[PLEKHH3]] | 0.735 | pleckstrin homology, MyTH4 and FERM domain containing H3 |
| [[THRA]] | 0.732 | thyroid hormone receptor alpha |
| [[MED30]] | 0.720 | mediator complex subunit 30 |
| [[COPS4]] | 0.715 | COP9 signalosome subunit 4 |
| [[CYB5A]] | 0.709 | cytochrome b5 type A |
| [[CXADR]] | 0.709 | CXADR cell adhesion molecule |
| [[FAM229B]] | 0.705 | family with sequence similarity 229 member B |
| [[USP33]] | 0.704 | ubiquitin specific peptidase 33 |
| [[RHOXF1]] | 0.703 | Rhox homeobox family member 1 |
| [[SNX1]] | 0.700 | sorting nexin 1 |
| [[ASAH1]] | 0.700 | N-acylsphingosine amidohydrolase 1 |
| [[NIPSNAP1]] | 0.697 | nipsnap homolog 1 |
| [[GAMT]] | 0.693 | guanidinoacetate N-methyltransferase |
| [[TMEM9]] | 0.693 | transmembrane protein 9 |
| [[GSTM4]] | 0.691 | glutathione S-transferase mu 4 |
| [[ARHGAP12]] | 0.690 | Rho GTPase activating protein 12 |
| [[PREPL]] | 0.688 | prolyl endopeptidase like |
| [[RCOR3]] | 0.686 | REST corepressor 3 |
| [[ARL6IP5]] | 0.686 | ARF like GTPase 6 interacting protein 5 |
| [[C20orf96]] | 0.684 | chromosome 20 open reading frame 96 |
| [[PIP4P2]] | 0.666 | phosphatidylinositol-4,5-bisphosphate 4-phosphatase 2 |
| [[FBXO3]] | 0.666 | F-box protein 3 |
| [[PNKD]] | 0.663 | PNKD metallo-beta-lactamase domain containing |
| [[SNX30]] | 0.661 | sorting nexin family member 30 |
| [[ACACB]] | 0.650 | acetyl-CoA carboxylase beta |
| [[FRRS1]] | 0.649 | ferric chelate reductase 1 |
| [[SNRPN]] | 0.647 | small nuclear ribonucleoprotein polypeptide N |
| [[OSBPL9]] | 0.646 | oxysterol binding protein like 9 |
| [[ACO1]] | 0.645 | aconitase 1 |
| [[FRG1CP]] | 0.644 | FSHD region gene 1 family member C, pseudogene |
| [[PRXL2A]] | 0.643 | peroxiredoxin like 2A |
| [[HAUS4]] | 0.637 | HAUS augmin like complex subunit 4 |
| [[MBIP]] | 0.635 | MAP3K12 binding inhibitory protein 1 |
| [[DENND4C]] | 0.635 | DENN domain containing 4C |
| [[MPP1]] | 0.628 | MAGUK p55 scaffold protein 1 |
| [[MARCHF6]] | 0.627 | membrane associated ring-CH-type finger 6 |
| [[ATP8A1]] | 0.624 | ATPase phospholipid transporting 8A1 |
| [[QPRT]] | 0.620 | quinolinate phosphoribosyltransferase |
| [[ERP29]] | 0.618 | endoplasmic reticulum protein 29 |
| [[TERF1]] | 0.614 | telomeric repeat binding factor 1 |
| [[AQP11]] | 0.614 | aquaporin 11 |
| [[GSTA4]] | 0.613 | glutathione S-transferase alpha 4 |
| [[SPOPL]] | 0.610 | speckle type BTB/POZ protein like |
| [[BEX3]] | 0.610 | brain expressed X-linked 3 |
| [[TP53TG1]] | 0.606 | TP53 target 1 |
| [[WDSUB1]] | 0.605 | WD repeat, sterile alpha motif and U-box domain containing 1 |
| [[RRAGD]] | 0.605 | Ras related GTP binding D |
| [[ATP6V1A]] | 0.599 | ATPase H+ transporting V1 subunit A |
| [[ATP6V0E2]] | 0.599 | ATPase H+ transporting V0 subunit e2 |
| [[ACBD4]] | 0.598 | acyl-CoA binding domain containing 4 |
| [[FKBP7]] | 0.597 | FKBP prolyl isomerase 7 |
| [[PTEN]] | 0.595 | phosphatase and tensin homolog |
| [[GXYLT2]] | 0.581 | glucoside xylosyltransferase 2 |
| [[DNASE2]] | 0.580 | deoxyribonuclease 2, lysosomal |
| [[CMBL]] | 0.579 | carboxymethylenebutenolidase homolog |
| [[LGR4]] | 0.579 | leucine rich repeat containing G protein-coupled receptor 4 |
| [[CAPZA2]] | 0.577 | capping actin protein of muscle Z-line subunit alpha 2 |
| [[EPHX2]] | 0.575 | epoxide hydrolase 2 |
| [[ATF2]] | 0.573 | activating transcription factor 2 |
| [[PTP4A2]] | 0.566 | protein tyrosine phosphatase 4A2 |
| [[SGCE]] | 0.563 | sarcoglycan epsilon |
| [[PCOLCE]] | 0.562 | procollagen C-endopeptidase enhancer |
| [[TRERF1]] | 0.555 | transcriptional regulating factor 1 |
| [[ATP6V1B2]] | 0.554 | ATPase H+ transporting V1 subunit B2 |
| [[DSTN]] | 0.552 | destrin, actin depolymerizing factor |
| [[ZNF540]] | 0.551 | zinc finger protein 540 |
| [[DOC2A]] | 0.549 | double C2 domain alpha |
| [[DUSP9]] | 0.542 | dual specificity phosphatase 9 |
| [[LINC00173]] | 0.527 | long independently transcribed non-coding RNA 173 |
| [[LRIG3]] | 0.520 | leucine rich repeats and immunoglobulin like domains 3 |
| [[NUDT7]] | 0.519 | nudix hydrolase 7 |
| [[SMIM10]] | 0.513 | small integral membrane protein 10 |
| [[CCNG1]] | 0.488 | cyclin G1 |
| [[TTC3P1]] | 0.484 | tetratricopeptide repeat domain 3 pseudogene 1 |
| [[SLC11A2]] | 0.483 | solute carrier family 11 member 2 |
| [[HMGN5]] | 0.479 | high mobility group nucleosome binding domain 5 |
| [[TSPAN7]] | 0.473 | tetraspanin 7 |
| [[PPP1R14A]] | 0.468 | protein phosphatase 1 regulatory inhibitor subunit 14A |
| [[ARHGAP35]] | 0.457 | Rho GTPase activating protein 35 |
| [[HSDL2]] | 0.440 | hydroxysteroid dehydrogenase like 2 |
| [[TMEM38B]] | 0.438 | transmembrane protein 38B |
| [[RAB3D]] | 0.438 | RAB3D, member RAS oncogene family |
| [[CYP39A1]] | 0.420 | cytochrome P450 family 39 subfamily A member 1 |
| [[JAK3]] | 0.402 | Janus kinase 3 |

## − arm (9)

| Gene | Projection | Name |
|---|---|---|
| [[DESI1]] | -0.649 | desumoylating isopeptidase 1 |
| [[CYREN]] | -0.612 | cell cycle regulator of NHEJ |
| [[FAM120B]] | -0.607 | family with sequence similarity 120 member B |
| [[KPNA4]] | -0.548 | karyopherin subunit alpha 4 |
| [[GATAD2A]] | -0.526 | GATA zinc finger domain containing 2A |
| [[PTRH1]] | -0.490 | peptidyl-tRNA hydrolase 1 homolog |
| [[ZSCAN5A]] | -0.465 | zinc finger and SCAN domain containing 5A |
| [[LARP4B]] | -0.462 | La ribonucleoprotein 4B |
| [[MELTF]] | -0.354 | melanotransferrin |

## Data

- `graph/nodes.parquet` — module == 45; `graph/modules.parquet` — module == 45; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [44] (drug-dose × line)
