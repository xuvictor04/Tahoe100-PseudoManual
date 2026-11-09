---
module: 56
type: "module"
n_genes: 87
n_plus: 87
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.33070939779281616
label: "Asparagine N-linked glycosylation"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 056

*Asparagine N-linked glycosylation · 87 genes (single-armed) · [[Module 056.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **Asparagine N-linked glycosylation** (reactome, q 7e-17; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | Asparagine N-linked glycosylation | reactome | 23/87 | 14.0 | 7e-17 |
| + | Asparagine N-linked glycosylation | reactome | 23/87 | 14.0 | 7e-17 |
| + | ER to Golgi Anterograde Transport | reactome | 16/87 | 19.7 | 2e-13 |
| all | ER to Golgi Anterograde Transport | reactome | 16/87 | 19.7 | 2e-13 |
| all | Transport to the Golgi and subsequent modification | reactome | 16/87 | 16.5 | 3e-12 |
| + | Transport to the Golgi and subsequent modification | reactome | 16/87 | 16.5 | 3e-12 |
| + | Membrane Trafficking | reactome | 20/87 | 6.04 | 7e-08 |
| all | Membrane Trafficking | reactome | 20/87 | 6.04 | 7e-08 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 55), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Terfenadine (drug)]] 5 µM (+1.6); [[Cloxacillin (sodium) (drug)]] 0.05 µM (+1.4); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (+1.4); [[Abemaciclib (drug)]] 0.5 µM (+1.4); [[TAK-733 (drug)]] 0.05 µM (+1.4); [[Fluvoxamine (maleate) (drug)]] 5 µM (+1.3); [[palbociclib (drug)]] 0.5 µM (+1.2, ⚠ cell-cycle shift); [[Goserelin (acetate) (drug)]] 5 µM (+1.2); [[Trimetrexate (drug)]] 5 µM (+1.2); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (+1.2); [[Pravastatin (sodium) (drug)]] 5 µM (+1.2) (15 in all, 1 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-8.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-7.6, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-6.3, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-6.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (-6.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-5.6, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-5.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-5.3, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-5.1); [[Topotecan (hydrochloride) (drug)]] 5 µM (-4.5, ⚠ toxic; cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-4.2); [[Belumosudil (drug)]] 5 µM (-3.8); [[Harringtonine (drug)]] 0.05 µM (-2.9); [[Retinoic acid (drug)]] 0.05 µM (-2.3); [[Berbamine (drug)]] 0.05 µM (-2.2); [[Temsirolimus (drug)]] 0.05 µM (-2.1); [[TAK-901 (drug)]] 0.05 µM (-2.1); [[Ixazomib citrate (drug)]] 0.5 µM (-2.0); [[Pralsetinib (drug)]] 5 µM (-1.9) (68 in all, 29 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A498 (line)]], [[HS-578T (line)]], [[RPMI-7951 (line)]], [[NCI-H2347 (line)]], [[A-172 (line)]], [[AsPC-1 (line)]], [[H4 (line)]], [[HOP62 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 65 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[KDELR2]] | Antigen Presentation: Folding, assembly and peptide loading of class I MHC | +0.81 |
| 2 | [[COPA]] | Antigen Presentation: Folding, assembly and peptide loading of class I MHC | +0.80 |
| 3 | [[COPB1]] | Antigen Presentation: Folding, assembly and peptide loading of class I MHC | +0.78 |
| 4 | [[SEC24D]] | COPI-mediated anterograde transport | +0.76 |
| 5 | [[SEC31A]] | COPI-mediated anterograde transport | +0.75 |
| 6 | [[COG6]] | COPII-mediated vesicle transport | +0.75 |
| 7 | [[TMEM263]] | ER to Golgi Anterograde Transport | +0.74 |
| 8 | [[SEC22B]] | Antigen Presentation: Folding, assembly and peptide loading of class I MHC | +0.73 |
| 9 | [[TMEM39A]] | ER to Golgi Anterograde Transport | +0.72 |
| 10 | [[PDXDC1]] | ER to Golgi Anterograde Transport | +0.72 |
| 11 | [[EIF2AK3]] | ER to Golgi Anterograde Transport | +0.72 |
| 12 | [[KDELR3]] | Antigen Presentation: Folding, assembly and peptide loading of class I MHC | +0.71 |
| 13 | [[PGM3]] | ER to Golgi Anterograde Transport | +0.71 |
| 14 | [[SEC23A]] | COPI-mediated anterograde transport | +0.71 |
| 15 | [[SEC13]] | Intra-Golgi and retrograde Golgi-to-ER traffic | +0.70 |

## + arm (87)

| Gene | Projection | Name |
|---|---|---|
| [[COG6]] | 0.933 | component of oligomeric golgi complex 6 |
| [[SEC24D]] | 0.920 | SEC24 homolog D, COPII component |
| [[KDELR2]] | 0.909 | KDEL endoplasmic reticulum protein retention receptor 2 |
| [[PDXDC1]] | 0.901 | pyridoxal dependent decarboxylase domain containing 1 |
| [[COPB1]] | 0.900 | coat protein complex I subunit beta 1 |
| [[TMEM263]] | 0.899 | transmembrane protein 263 |
| [[COPA]] | 0.897 | coat protein complex I subunit alpha |
| [[SEC31A]] | 0.885 | SEC31 homolog A, COPII component |
| [[EIF2AK3]] | 0.883 | eukaryotic translation initiation factor 2 alpha kinase 3 |
| [[PDXDC2P]] | 0.873 | pyridoxal dependent decarboxylase domain containing 2, pseudogene |
| [[PGM3]] | 0.872 | phosphoglucomutase 3 |
| [[SEC13]] | 0.869 | SEC13 homolog, nuclear pore and COPII component |
| [[TMEM39A]] | 0.861 | transmembrane protein 39A |
| [[SEC23A]] | 0.854 | SEC23 homolog A, COPII component |
| [[ERLEC1]] | 0.852 | endoplasmic reticulum lectin 1 |
| [[GFPT1]] | 0.851 | glutamine--fructose-6-phosphate transaminase 1 |
| [[TXNDC11]] | 0.841 | thioredoxin domain containing 11 |
| [[SLC31A1]] | 0.834 | solute carrier family 31 member 1 |
| [[PRRC1]] | 0.833 | proline rich coiled-coil 1 |
| [[SEC22B]] | 0.827 | SEC22 homolog B, vesicle trafficking protein |
| [[TTC3]] | 0.825 | tetratricopeptide repeat domain 3 |
| [[SUCO]] | 0.822 | SUN domain containing ossification factor |
| [[NDEL1]] | 0.817 | nudE neurodevelopment protein 1 like 1 |
| [[DHDDS]] | 0.797 | dehydrodolichyl diphosphate synthase subunit |
| [[KDELR3]] | 0.795 | KDEL endoplasmic reticulum protein retention receptor 3 |
| [[PDXDC2P-NPIPB14P]] | 0.791 | PDXDC2P-NPIPB14P readthrough, transcribed pseudogene |
| [[MCEE]] | 0.781 | methylmalonyl-CoA epimerase |
| [[GOLT1B]] | 0.780 | golgi transport 1B |
| [[EAF2]] | 0.772 | ELL associated factor 2 |
| [[NANS]] | 0.766 | N-acetylneuraminate synthase |
| [[GBF1]] | 0.762 | golgi brefeldin A resistant guanine nucleotide exchange factor 1 |
| [[FAM114A1]] | 0.761 | family with sequence similarity 114 member A1 |
| [[CLINT1]] | 0.761 | clathrin interactor 1 |
| [[HERPUD1]] | 0.754 | homocysteine inducible ER protein with ubiquitin like domain 1 |
| [[SLC17A5]] | 0.753 | solute carrier family 17 member 5 |
| [[RAB2A]] | 0.733 | RAB2A, member RAS oncogene family |
| [[RAB1A]] | 0.732 | RAB1A, member RAS oncogene family |
| [[TVP23C]] | 0.722 | trans-golgi network vesicle protein 23 homolog C |
| [[POFUT2]] | 0.721 | protein O-fucosyltransferase 2 |
| [[NUS1]] | 0.720 | NUS1 dehydrodolichyl diphosphate synthase subunit |
| [[COPB2]] | 0.717 | coat protein complex I subunit beta 2 |
| [[SEC24A]] | 0.714 | SEC24 homolog A, COPII component |
| [[SLC35A2]] | 0.712 | solute carrier family 35 member A2 |
| [[MON2]] | 0.712 | MON2 regulator of endosome-to-Golgi trafficking |
| [[KCNQ1OT1]] | 0.710 | KCNQ1 opposite strand/antisense transcript 1 |
| [[UFM1]] | 0.710 | ubiquitin fold modifier 1 |
| [[ARFGAP3]] | 0.707 | ARF GTPase activating protein 3 |
| [[SWI5]] | 0.703 | SWI5 homologous recombination repair protein |
| [[FKBP14]] | 0.700 | FKBP prolyl isomerase 14 |
| [[RRBP1]] | 0.691 | ribosome binding protein 1 |
| [[WIPI1]] | 0.691 | WD repeat domain, phosphoinositide interacting 1 |
| [[LINC00632]] | 0.673 | long independently transcribed non-coding RNA 632 |
| [[TARS3]] | 0.672 | threonyl-tRNA synthetase 3 |
| [[MORF4L2]] | 0.657 | mortality factor 4 like 2 |
| [[SLC39A9]] | 0.647 | solute carrier family 39 member 9 |
| [[NAA35]] | 0.643 | N-alpha-acetyltransferase 35, NatC auxiliary subunit |
| [[TFG]] | 0.634 | trafficking from ER to golgi regulator |
| [[NPIPB14P]] | 0.631 | nuclear pore complex interacting protein family member B14, pseudogene |
| [[TRIM3]] | 0.622 | tripartite motif containing 3 |
| [[DERL1]] | 0.618 | derlin 1 |
| [[CREB3L2]] | 0.616 | cAMP responsive element binding protein 3 like 2 |
| [[TBC1D8B]] | 0.613 | TBC1 domain family member 8B |
| [[TVP23C-CDRT4]] | 0.613 | TVP23C-CDRT4 readthrough |
| [[RCN3]] | 0.610 | reticulocalbin 3 |
| [[SLC25A42]] | 0.608 | solute carrier family 25 member 42 |
| [[TET3]] | -0.585 | tet methylcytosine dioxygenase 3 |
| [[PDE4DIP]] | 0.566 | phosphodiesterase 4D interacting protein |
| [[CDRT4]] | 0.564 | CMT1A duplicated region transcript 4 |
| [[SIAH2]] | 0.549 | siah E3 ubiquitin protein ligase 2 |
| [[RPS6KC1]] | 0.546 | ribosomal protein S6 kinase C1 |
| [[PPARA]] | 0.541 | peroxisome proliferator activated receptor alpha |
| [[ARG2]] | 0.538 | arginase 2 |
| [[MCTP2]] | 0.533 | multiple C2 and transmembrane domain containing 2 |
| [[RTRAF]] | 0.531 | RNA transcription, translation and transport factor |
| [[EIF2A]] | 0.529 | eukaryotic translation initiation factor 2A |
| [[AHCYL1]] | 0.518 | adenosylhomocysteinase like 1 |
| [[HEATR5A]] | 0.515 | HEAT repeat containing 5A |
| [[TRIQK]] | 0.506 | triple QxxK/R motif containing |
| [[TMEM182]] | 0.477 | transmembrane protein 182 |
| [[DIP2B]] | -0.476 | DIP2 acetate--CoA ligase B (putative) |
| [[AP3B1]] | 0.474 | adaptor related protein complex 3 subunit beta 1 |
| [[RESF1]] | -0.464 | retroelement silencing factor 1 |
| [[MTDH]] | 0.463 | metadherin |
| [[SURF1]] | 0.455 | SURF1 cytochrome c oxidase assembly factor |
| [[PAPSS2]] | 0.409 | 3'-phosphoadenosine 5'-phosphosulfate synthase 2 |
| [[BTBD9]] | 0.399 | BTB domain containing 9 |
| [[SINHCAF]] | -0.386 | SIN3-HDAC complex associated factor |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 56; `graph/modules.parquet` — module == 56; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [55] (drug-dose × line)
