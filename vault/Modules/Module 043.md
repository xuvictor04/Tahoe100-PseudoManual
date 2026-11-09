---
module: 43
type: "module"
n_genes: 103
n_plus: 97
n_minus: 6
arms_opposite: true
mean_cos_between_arms: -0.4276859164237976
label: "Eukaryotic Translation Elongation"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 043

*Eukaryotic Translation Elongation · 103 genes (97 in the + arm, 6 in the − arm) · [[Module 043.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Eukaryotic Translation Elongation** (reactome, q 8e-98; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Eukaryotic Translation Elongation | reactome | 55/97 | 92.9 | 8e-98 |
| all | Eukaryotic Translation Elongation | reactome | 55/103 | 87.5 | 5e-96 |
| + | Peptide chain elongation | reactome | 52/97 | 92.9 | 4e-92 |
| + | Formation of a pool of free 40S subunits | reactome | 53/97 | 83.2 | 1e-90 |
| all | Peptide chain elongation | reactome | 52/103 | 87.5 | 2e-90 |
| + | L13a-mediated translational silencing of Ceruloplasmin expression | reactome | 54/97 | 77.0 | 3e-90 |
| + | Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC) | reactome | 52/97 | 86.9 | 3e-90 |
| + | PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA | reactome | 51/97 | 90.1 | 1e-89 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 42), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Panobinostat (drug)]] 0.5 µM (+7.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+6.1, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 0.05 µM (+5.9, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (+5.7, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+4.8); [[Ixazomib citrate (drug)]] 5 µM (+4.6, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.05 µM (+4.2, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 5 µM (+4.0, ⚠ toxic; cell-cycle shift); [[Tucidinostat (drug)]] 5 µM (+3.8); [[Tucidinostat (drug)]] 0.5 µM (+3.5, ⚠ cell-cycle shift); [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM (+3.1); [[Bortezomib (drug)]] 0.5 µM (+2.9); [[Terfenadine (drug)]] 5 µM (+2.6); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (+2.6); [[Temsirolimus (drug)]] 0.5 µM (+2.5); [[Vinblastine (sulfate) (drug)]] 5 µM (+2.5); [[Adagrasib (drug)]] 5 µM (+2.4); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (+2.4) (146 in all, 26 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Dinaciclib (drug)]] 0.5 µM (-7.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 5 µM (-6.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-6.7, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-4.4, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.8, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-3.4, ⚠ toxic; transcription drop; cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (-3.2, ⚠ unreliable plate only); [[Harringtonine (drug)]] 0.5 µM (-3.0, ⚠ cell-cycle shift); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-2.9); [[Busulfan (drug)]] 0.05 µM (-2.7); [[Demeclocycline (drug)]] 5 µM (-2.7); [[Folic acid (drug)]] 5 µM (-2.6); [[Balsalazide (sodium hydrate) (drug)]] 5 µM (-2.3); [[Filgotinib (drug)]] 5 µM (-2.2); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (-2.2); [[Retinoic acid (drug)]] 0.05 µM (-2.1); [[Clofarabine (drug)]] 0.5 µM (-2.1); [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM (-2.1) (152 in all, 22 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[RKO (line)]], [[KATO III (line)]], [[A-427 (line)]], [[PANC-1 (line)]], [[SHP-77 (line)]], [[HS-578T (line)]], [[C32 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 81 candidates, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert.*

| # | Gene | Set | Mean cos | Alert |
|---|---|---|---|---|
| 1 | [[RPS8]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.88 |  |
| 2 | [[RPS17]] ⚠ | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.87 | ⚠ in the vector space only through drug-doses that carry an alert |
| 3 | [[RPS14]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.87 |  |
| 4 | [[RPS3]] ⚠ | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.86 | ⚠ in the vector space only through drug-doses that carry an alert |
| 5 | [[RPS12]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.86 |  |
| 6 | [[RPS27]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.85 |  |
| 7 | [[RPS6]] ⚠ | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.85 | ⚠ in the vector space only through drug-doses that carry an alert |
| 8 | [[RPS20]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.85 |  |
| 9 | [[RPS28]] ⚠ | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.83 | ⚠ in the vector space only through drug-doses that carry an alert |
| 10 | [[RPS19]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.82 |  |
| 11 | [[RPL26]] | SARS-CoV-1 modulates host translation machinery | +0.82 |  |
| 12 | [[RPS5]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.82 |  |
| 13 | [[RPL34]] | SARS-CoV-1 modulates host translation machinery | +0.82 |  |
| 14 | [[RPL11]] | SARS-CoV-1 modulates host translation machinery | +0.82 |  |
| 15 | [[RPL19]] | SARS-CoV-1 modulates host translation machinery | +0.81 |  |
| 16 | [[RPL13]] | SARS-CoV-1 modulates host translation machinery | +0.81 |  |
| 17 | [[RPL17]] | SARS-CoV-1 modulates host translation machinery | +0.81 |  |
| 18 | [[RPS4X]] | Ribosome Quality Control (RQC) complex extracts and degrades nascent peptide | +0.81 |  |
| 19 | [[RPL31]] | SARS-CoV-1 modulates host translation machinery | +0.81 |  |

*⚠ 18 of its 103 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (97)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[RPL26]] | 0.982 | ribosomal protein L26 |  |
| [[RPL34]] | 0.980 | ribosomal protein L34 |  |
| [[RPL31]] | 0.977 | ribosomal protein L31 |  |
| [[RPS8]] | 0.973 | ribosomal protein S8 |  |
| [[RPL35A]] | 0.971 | ribosomal protein L35a |  |
| [[RPL19]] | 0.970 | ribosomal protein L19 |  |
| [[RPL9]] | 0.966 | ribosomal protein L9 | ⚠ only flagged evidence |
| [[RPL13]] | 0.965 | ribosomal protein L13 |  |
| [[RPS3]] | 0.963 | ribosomal protein S3 | ⚠ only flagged evidence |
| [[RPL17]] | 0.963 | ribosomal protein L17 |  |
| [[RPS17]] | 0.962 | ribosomal protein S17 | ⚠ only flagged evidence |
| [[RPL23]] | 0.962 | ribosomal protein L23 |  |
| [[RPL37]] | 0.960 | ribosomal protein L37 | ⚠ only flagged evidence |
| [[RPS14]] | 0.959 | ribosomal protein S14 |  |
| [[RPL11]] | 0.959 | ribosomal protein L11 |  |
| [[RPS12]] | 0.957 | ribosomal protein S12 |  |
| [[RPS27]] | 0.951 | ribosomal protein S27 |  |
| [[RPL12]] | 0.947 | ribosomal protein L12 |  |
| [[RPLP1]] | 0.947 | ribosomal protein lateral stalk subunit P1 |  |
| [[RPL35]] | 0.944 | ribosomal protein L35 | ⚠ only flagged evidence |
| [[RPS6]] | 0.938 | ribosomal protein S6 | ⚠ only flagged evidence |
| [[RPS27A]] | 0.938 | ribosomal protein S27a | ⚠ only flagged evidence |
| [[RPL30]] | 0.936 | ribosomal protein L30 | ⚠ only flagged evidence |
| [[RPL5]] | 0.932 | ribosomal protein L5 |  |
| [[RPL7]] | 0.923 | ribosomal protein L7 |  |
| [[RPS19]] | 0.920 | ribosomal protein S19 |  |
| [[RPS20]] | 0.920 | ribosomal protein S20 |  |
| [[RPL27]] | 0.919 | ribosomal protein L27 |  |
| [[RPS28]] | 0.918 | ribosomal protein S28 | ⚠ only flagged evidence |
| [[RPL18]] | 0.918 | ribosomal protein L18 | ⚠ only flagged evidence |
| [[RPL37A]] | 0.917 | ribosomal protein L37a | ⚠ only flagged evidence |
| [[RPL36]] | 0.912 | ribosomal protein L36 |  |
| [[RPL13A]] | 0.910 | ribosomal protein L13a |  |
| [[RPL21]] | 0.903 | ribosomal protein L21 | ⚠ only flagged evidence |
| [[RACK1]] | 0.898 | receptor for activated C kinase 1 |  |
| [[UBA52]] | 0.898 | ubiquitin A-52 residue ribosomal protein fusion product 1 |  |
| [[RPS5]] | 0.895 | ribosomal protein S5 |  |
| [[RPL27A]] | 0.895 | ribosomal protein L27a |  |
| [[NACA]] | 0.893 | nascent polypeptide associated complex subunit alpha | ⚠ only flagged evidence |
| [[RPL24]] | 0.892 | ribosomal protein L24 |  |
| [[RPL10A]] | 0.889 | ribosomal protein L10a | ⚠ only flagged evidence |
| [[SNHG6]] | 0.875 | small nucleolar RNA host gene 6 |  |
| [[RPS4X]] | 0.874 | ribosomal protein S4 X-linked |  |
| [[RPS15A]] | 0.854 | ribosomal protein S15a |  |
| [[UQCRB]] | 0.849 | ubiquinol-cytochrome c reductase binding protein | ⚠ only flagged evidence |
| [[RPLP0]] | 0.845 | ribosomal protein lateral stalk subunit P0 |  |
| [[TOMM7]] | 0.837 | translocase of outer mitochondrial membrane 7 |  |
| [[NACA4P]] | 0.823 | NACA family member 4, pseudogene | ⚠ only flagged evidence |
| [[RPL23A]] | 0.814 | ribosomal protein L23a |  |
| [[PFDN5]] | 0.807 | prefoldin subunit 5 |  |
| [[ADGRL3-AS1]] | 0.806 | ADGRL3 antisense RNA 1 |  |
| [[CAMLG]] | 0.801 | calcium modulating ligand |  |
| [[COX4I1]] | 0.798 | cytochrome c oxidase subunit 4I1 | ⚠ only flagged evidence |
| [[ATP5MC2]] | 0.777 | ATP synthase membrane subunit c locus 2 |  |
| [[RPL39]] | 0.774 | ribosomal protein L39 |  |
| [[RPS2]] | 0.768 | ribosomal protein S2 |  |
| [[NSA2]] | 0.768 | NSA2 ribosome biogenesis factor |  |
| [[UQCRH]] | 0.754 | ubiquinol-cytochrome c reductase hinge protein |  |
| [[RPS26]] | 0.736 | ribosomal protein S26 |  |
| [[CEP164P1]] | 0.729 | centrosomal protein 164 pseudogene 1 |  |
| [[RBIS]] | 0.729 | ribosomal biogenesis factor |  |
| [[BTF3]] | 0.724 | basic transcription factor 3 |  |
| [[EEF1G]] | 0.722 | eukaryotic translation elongation factor 1 gamma |  |
| [[EEF1D]] | 0.719 | eukaryotic translation elongation factor 1 delta |  |
| [[TOMM20]] | 0.705 | translocase of outer mitochondrial membrane 20 |  |
| [[MRPS24]] | 0.702 | mitochondrial ribosomal protein S24 |  |
| [[RPL22]] | 0.692 | ribosomal protein L22 |  |
| [[RPL29]] | 0.692 | ribosomal protein L29 |  |
| [[NME2]] | 0.688 | NME/NM23 nucleoside diphosphate kinase 2 |  |
| [[SLC25A6]] | 0.684 | solute carrier family 25 member 6 |  |
| [[FTL]] | 0.665 | ferritin light chain |  |
| [[EEF1B2]] | 0.659 | eukaryotic translation elongation factor 1 beta 2 |  |
| [[SF3B6]] | 0.658 | splicing factor 3b subunit 6 |  |
| [[NOP53]] | 0.654 | NOP53 ribosome biogenesis factor |  |
| [[SLC25A5]] | 0.640 | solute carrier family 25 member 5 |  |
| [[RPS7]] | 0.632 | ribosomal protein S7 |  |
| [[COX5A]] | 0.631 | cytochrome c oxidase subunit 5A | ⚠ only flagged evidence |
| [[FAM182B]] | 0.630 | family with sequence similarity 182 member B |  |
| [[RPL14]] | 0.622 | ribosomal protein L14 |  |
| [[GPX4]] | 0.606 | glutathione peroxidase 4 |  |
| [[EDF1]] | 0.566 | endothelial differentiation related factor 1 |  |
| [[SLC25A3]] | 0.557 | solute carrier family 25 member 3 |  |
| [[CCDC126]] | 0.546 | coiled-coil domain containing 126 |  |
| [[ZNF235]] | 0.530 | zinc finger protein 235 |  |
| [[NAP1L1]] | 0.528 | nucleosome assembly protein 1 like 1 |  |
| [[SNHG29]] | 0.527 | small nucleolar RNA host gene 29 |  |
| [[EIF3E]] | 0.502 | eukaryotic translation initiation factor 3 subunit E |  |
| [[POLR1D]] | 0.477 | RNA polymerase I and III subunit D |  |
| [[PPIP5K1]] | 0.470 | diphosphoinositol pentakisphosphate kinase 1 |  |
| [[RPS9]] | 0.441 | ribosomal protein S9 |  |
| [[NPM1]] | 0.431 | nucleophosmin 1 |  |
| [[PABPC1]] | 0.411 | poly(A) binding protein cytoplasmic 1 |  |
| [[EEF2]] | 0.371 | eukaryotic translation elongation factor 2 |  |
| [[EIF3L]] | 0.364 | eukaryotic translation initiation factor 3 subunit L |  |
| [[HNRNPA1]] | 0.278 | heterogeneous nuclear ribonucleoprotein A1 |  |
| [[YBX1]] | 0.259 | Y-box binding protein 1 |  |
| [[PCBP2]] | 0.190 | poly(rC) binding protein 2 |  |

## − arm (6)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[NUP188]] | -0.633 | nucleoporin 188 |  |
| [[POGLUT3]] | -0.626 | protein O-glucosyltransferase 3 |  |
| [[FGD5-AS1]] | -0.591 | FGD5 antisense RNA 1 |  |
| [[PTPA]] | -0.543 | protein phosphatase 2 phosphatase activator |  |
| [[CDC42EP1]] | -0.532 | CDC42 effector protein 1 |  |
| [[THOP1]] | -0.519 | thimet oligopeptidase 1 |  |

## Data

- `graph/nodes.parquet` — module == 43; `graph/modules.parquet` — module == 43; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [42] (drug-dose × line)
