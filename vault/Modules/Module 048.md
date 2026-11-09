---
module: 48
type: "module"
n_genes: 93
n_plus: 87
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.371128112077713
label: "Aerobic respiration and respiratory electron transport"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 048

*Aerobic respiration and respiratory electron transport · 93 genes (87 in the + arm, 6 in the − arm) · [[Module 048.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Aerobic respiration and respiratory electron transport** (reactome, q 1e-30; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Aerobic respiration and respiratory electron transport | reactome | 31/87 | 23.3 | 1e-30 |
| all | Aerobic respiration and respiratory electron transport | reactome | 31/93 | 21.8 | 1e-29 |
| + | Respiratory electron transport | reactome | 24/87 | 29.5 | 1e-25 |
| all | Respiratory electron transport | reactome | 24/93 | 27.6 | 7e-25 |
| + | oxidative phosphorylation | hallmark | 24/87 | 20.8 | 7e-22 |
| all | oxidative phosphorylation | hallmark | 24/93 | 19.5 | 4e-21 |
| + | Complex IV assembly | reactome | 11/87 | 47.7 | 5e-13 |
| all | Complex IV assembly | reactome | 11/93 | 44.6 | 1e-12 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 47), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Digitoxin (drug)]] 5 µM (+7.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (+6.1, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+4.9, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (+3.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+3.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+3.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+3.4, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (+3.1); [[Azithromycin (hydrate) (drug)]] 5 µM (+2.9); [[Thymol (drug)]] 0.5 µM (+2.6); [[Methylprednisolone succinate (drug)]] 0.5 µM (+2.5); [[Arbutin (drug)]] 5 µM (+2.5); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (+2.4); [[Darolutamide (drug)]] 5 µM (+2.3); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.3); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM (+2.2); [[Celecoxib (drug)]] 0.5 µM (+2.2) (144 in all, 28 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-12.2, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-9.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-8.6, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-8.5, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-6.8, ⚠ toxic; transcription drop; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.8, ⚠ unreliable plate only); [[Ralimetinib dimesylate (drug)]] 0.05 µM (-3.5, ⚠ unreliable plate only); [[GSK1059615 (drug)]] 5 µM (-3.3); [[Trametinib (drug)]] 5 µM (-3.1, ⚠ cell-cycle shift); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.9); [[Bimiralisib (drug)]] 5 µM (-2.8); [[Ponatinib (drug)]] 5 µM (-2.8); [[Budesonide (drug)]] 5 µM (-2.8); [[Homoharringtonine (drug)]] 0.05 µM (-2.7); [[Sapanisertib (drug)]] 5 µM (-2.7); [[Glycyrrhizic acid (drug)]] 0.5 µM (-2.7); [[Erlotinib (drug)]] 0.05 µM (-2.6); [[Folic acid (drug)]] 5 µM (-2.6) (180 in all, 30 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[LoVo (line)]], [[NCI-H2347 (line)]], [[RKO (line)]], [[NCI-H23 (line)]], [[HT-29 (line)]], [[J82 (line)]], [[NCI-H2030 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 62 candidates, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[ROMO1]] | Formation of ATP by chemiosmotic coupling | +0.80 |  |
| 2 | [[COX6B1]] | Formation of ATP by chemiosmotic coupling | +0.79 |  |
| 3 | [[UQCRQ]] ⚠ | Formation of ATP by chemiosmotic coupling | +0.79 | ⚠ in the vector space only through drug-doses that carry an alert |
| 4 | [[NDUFA1]] | Formation of ATP by chemiosmotic coupling | +0.76 |  |
| 5 | [[COX6C]] | Formation of ATP by chemiosmotic coupling | +0.75 |  |
| 6 | [[COX7C]] | Formation of ATP by chemiosmotic coupling | +0.74 |  |
| 7 | [[UBL5]] | Formation of ATP by chemiosmotic coupling | +0.74 |  |
| 8 | [[UQCR11]] | Formation of ATP by chemiosmotic coupling | +0.74 |  |
| 9 | [[NDUFB11]] ⚠ | Cytoprotection by HMOX1 | +0.73 | ⚠ in the vector space only through drug-doses that carry an alert |
| 10 | [[COX6A1]] | Formation of ATP by chemiosmotic coupling | +0.73 |  |
| 11 | [[ATP5MK]] | Cytoprotection by HMOX1 | +0.72 |  |
| 12 | [[ATP5PD]] | Cytoprotection by HMOX1 | +0.72 |  |
| 13 | [[ATP5MJ]] | Cytoprotection by HMOX1 | +0.71 |  |
| 14 | [[NDUFA2]] | TP53 Regulates Metabolic Genes | +0.71 |  |
| 15 | [[ATP5F1E]] | Cytoprotection by HMOX1 | +0.70 |  |
| 16 | [[NDUFA4]] | Formation of ATP by chemiosmotic coupling | +0.70 |  |
| 17 | [[SPCS1]] | Formation of ATP by chemiosmotic coupling | +0.70 |  |

*⚠ 7 of its 93 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (87)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[UQCRQ]] | 0.923 | ubiquinol-cytochrome c reductase complex III subunit VII | ⚠ only flagged evidence |
| [[ROMO1]] | 0.920 | reactive oxygen species modulator 1 |  |
| [[UBL5]] | 0.919 | ubiquitin like 5 |  |
| [[COX6B1]] | 0.900 | cytochrome c oxidase subunit 6B1 |  |
| [[COX6A1]] | 0.895 | cytochrome c oxidase subunit 6A1 |  |
| [[ATP5MK]] | 0.892 | ATP synthase membrane subunit k |  |
| [[NDUFB11]] | 0.880 | NADH:ubiquinone oxidoreductase subunit B11 | ⚠ only flagged evidence |
| [[UQCR11]] | 0.879 | ubiquinol-cytochrome c reductase, complex III subunit XI |  |
| [[NDUFA2]] | 0.876 | NADH:ubiquinone oxidoreductase subunit A2 |  |
| [[COX6C]] | 0.872 | cytochrome c oxidase subunit 6C |  |
| [[ATP5PD]] | 0.866 | ATP synthase peripheral stalk subunit d |  |
| [[ATP5MJ]] | 0.861 | ATP synthase membrane subunit j |  |
| [[COX7C]] | 0.858 | cytochrome c oxidase subunit 7C |  |
| [[NDUFA1]] | 0.854 | NADH:ubiquinone oxidoreductase subunit A1 |  |
| [[C4orf48]] | 0.852 | NELL2 interacting cell ontogeny regulator 1 |  |
| [[MIF]] | 0.851 | macrophage migration inhibitory factor |  |
| [[NDUFA4]] | 0.840 | cytochrome c oxidase associated subunit FA4 |  |
| [[COX7A2]] | 0.831 | cytochrome c oxidase subunit 7A2 | ⚠ only flagged evidence |
| [[OST4]] | 0.827 | oligosaccharyltransferase complex subunit 4, non-catalytic |  |
| [[SSR4]] | 0.827 | signal sequence receptor subunit 4 |  |
| [[ELOB]] | 0.822 | elongin B |  |
| [[SPCS1]] | 0.819 | signal peptidase complex subunit 1 |  |
| [[RABAC1]] | 0.811 | Rab acceptor 1 |  |
| [[ANAPC11]] | 0.811 | anaphase promoting complex subunit 11 |  |
| [[NDUFA11]] | 0.808 | NADH:ubiquinone oxidoreductase subunit A11 | ⚠ only flagged evidence |
| [[ATP5F1E]] | 0.807 | ATP synthase F1 subunit epsilon |  |
| [[LAMTOR2]] | 0.800 | late endosomal/lysosomal adaptor, MAPK and MTOR activator 2 |  |
| [[ATP5ME]] | 0.797 | ATP synthase membrane subunit e |  |
| [[NENF]] | 0.795 | neudesin neurotrophic factor |  |
| [[DDT]] | 0.791 | D-dopachrome tautomerase |  |
| [[SEC61G]] | 0.787 | SEC61 translocon subunit gamma |  |
| [[ATOX1]] | 0.785 | antioxidant 1 copper chaperone |  |
| [[ATP5PF]] | 0.780 | ATP synthase peripheral stalk subunit F6 |  |
| [[UQCR10]] | 0.773 | ubiquinol-cytochrome c reductase, complex III subunit X | ⚠ only flagged evidence |
| [[PCSK1N]] | 0.768 | proprotein convertase subtilisin/kexin type 1 inhibitor |  |
| [[BBLN]] | 0.764 | bublin coiled coil protein |  |
| [[COPS9]] | 0.761 | COP9 signalosome subunit 9 |  |
| [[SERF2]] | 0.752 | small EDRK-rich factor 2 |  |
| [[NDUFB1]] | 0.746 | NADH:ubiquinone oxidoreductase subunit B1 |  |
| [[NEDD8]] | 0.743 | NEDD8 ubiquitin like modifier |  |
| [[ZNHIT1]] | 0.741 | zinc finger HIT-type containing 1 |  |
| [[MRPL51]] | 0.737 | mitochondrial ribosomal protein L51 | ⚠ only flagged evidence |
| [[COX17]] | 0.734 | cytochrome c oxidase copper chaperone COX17 |  |
| [[CHMP2A]] | 0.730 | charged multivesicular body protein 2A |  |
| [[HIGD2A]] | 0.724 | HIG1 hypoxia inducible domain family member 2A |  |
| [[COX8A]] | 0.721 | cytochrome c oxidase subunit 8A |  |
| [[TMSB10]] | 0.706 | thymosin beta 10 |  |
| [[COX5B]] | 0.695 | cytochrome c oxidase subunit 5B |  |
| [[NDUFC2]] | 0.692 | NADH:ubiquinone oxidoreductase subunit C2 |  |
| [[AP2S1]] | 0.671 | adaptor related protein complex 2 subunit sigma 1 |  |
| [[ATP5MF]] | 0.667 | ATP synthase membrane subunit f |  |
| [[COX7B]] | 0.665 | cytochrome c oxidase subunit 7B |  |
| [[NDUFA13]] | 0.657 | NADH:ubiquinone oxidoreductase subunit A13 | ⚠ only flagged evidence |
| [[CHCHD10]] | 0.656 | coiled-coil-helix-coiled-coil-helix domain containing 10 |  |
| [[MRPL33]] | 0.649 | mitochondrial ribosomal protein L33 |  |
| [[ATP5IF1]] | 0.622 | ATP synthase inhibitory factor subunit 1 |  |
| [[PHPT1]] | 0.618 | phosphohistidine phosphatase 1 |  |
| [[PPP1R14B]] | 0.605 | protein phosphatase 1 regulatory inhibitor subunit 14B |  |
| [[POLR2K]] | 0.603 | RNA polymerase II, I and III subunit K |  |
| [[ETFB]] | 0.592 | electron transfer flavoprotein subunit beta |  |
| [[NDUFB2]] | 0.591 | NADH:ubiquinone oxidoreductase subunit B2 |  |
| [[TAF3]] | 0.589 | TATA-box binding protein associated factor 3 |  |
| [[ARF5]] | 0.586 | ARF GTPase 5 |  |
| [[RPA3]] | 0.575 | replication protein A3 |  |
| [[GTF2A2]] | 0.573 | general transcription factor IIA subunit 2 |  |
| [[PRDX4]] | 0.573 | peroxiredoxin 4 |  |
| [[BLOC1S1]] | 0.571 | biogenesis of lysosomal organelles complex 1 subunit 1 |  |
| [[MIR210HG]] | 0.565 | MIR210 host gene |  |
| [[CST3]] | 0.560 | cystatin C |  |
| [[HYCC2]] | 0.551 | hyccin PI4KA lipid kinase complex subunit 2 |  |
| [[PRKD2]] | 0.541 | protein kinase D2 |  |
| [[ZDHHC12]] | 0.540 | zDHHC palmitoyltransferase 12 |  |
| [[EGFL7]] | 0.538 | EGF like domain multiple 7 |  |
| [[RIC1]] | 0.537 | RIC1 partner of RAB6A GEF complex |  |
| [[ZCRB1]] | 0.527 | zinc finger CCHC-type and RNA binding motif containing 1 |  |
| [[GSTP1]] | 0.527 | glutathione S-transferase pi 1 |  |
| [[SUPT4H1]] | 0.519 | SPT4 homolog, DSIF elongation factor subunit |  |
| [[ZNF277]] | 0.514 | zinc finger protein 277 |  |
| [[HSBP1]] | 0.505 | heat shock factor binding protein 1 |  |
| [[ANKS1A]] | 0.501 | ankyrin repeat and sterile alpha motif domain containing 1A |  |
| [[MAP4K3]] | 0.465 | mitogen-activated protein kinase kinase kinase kinase 3 |  |
| [[TMED1]] | 0.452 | transmembrane p24 trafficking protein 1 |  |
| [[C18orf32]] | 0.420 | chromosome 18 open reading frame 32 |  |
| [[TAOK3]] | 0.419 | TAO kinase 3 |  |
| [[NDUFAF8]] | 0.395 | NADH:ubiquinone oxidoreductase complex assembly factor 8 |  |
| [[RNASEH2C]] | 0.394 | ribonuclease H2 subunit C |  |
| [[PSENEN]] | 0.281 | presenilin enhancer, gamma-secretase subunit |  |

## − arm (6)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[TEX261]] | -0.657 | testis expressed 261 |  |
| [[BACE1-AS]] | -0.648 | BACE1 antisense RNA |  |
| [[ADSS2]] | -0.603 | adenylosuccinate synthase 2 |  |
| [[MATR3-1]] | -0.537 | — |  |
| [[PM20D2]] | -0.450 | peptidase M20 domain containing 2 |  |
| [[SHTN1]] | -0.386 | shootin 1 |  |

## Data

- `graph/nodes.parquet` — module == 48; `graph/modules.parquet` — module == 48; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [47] (drug-dose × line)
