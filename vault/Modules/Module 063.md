---
module: 63
type: "module"
n_genes: 77
n_plus: 77
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.3318980634212494
label: "ISR ATF4"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 063

*ISR ATF4 · 77 genes (single-armed) · [[Module 063.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **ISR ATF4** (control, q 2e-29; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | ISR ATF4 | control | 16/77 | 142 | 2e-29 |
| + | ISR ATF4 | control | 16/77 | 142 | 2e-29 |
| + | mTORC1 signaling | hallmark | 20/77 | 20.0 | 2e-17 |
| all | mTORC1 signaling | hallmark | 20/77 | 20.0 | 2e-17 |
| all | Cytosolic tRNA aminoacylation | reactome | 9/77 | 73.4 | 3e-12 |
| + | Cytosolic tRNA aminoacylation | reactome | 9/77 | 73.4 | 3e-12 |
| + | tRNA Aminoacylation | reactome | 9/77 | 44.1 | 5e-10 |
| all | tRNA Aminoacylation | reactome | 9/77 | 44.1 | 5e-10 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 62), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Artesunate (drug)]] 5 µM (+6.5, ⚠ cell-cycle shift); [[Neratinib (maleate) (drug)]] 0.5 µM (+5.4, ⚠ cell-cycle shift); [[c-Kit-IN-1 (drug)]] 0.05 µM (+5.3, ⚠ unreliable plate only); [[Auranofin (drug)]] 5 µM (+4.8); [[5-Azacytidine (drug)]] 5 µM (+4.7); [[Neratinib (maleate) (drug)]] 5 µM (+4.7); [[Ponatinib (drug)]] 5 µM (+4.2); [[Artesunate (drug)]] 0.5 µM (+4.1); [[Niclosamide (olamine) (drug)]] 5 µM (+4.1, ⚠ toxic; cell-cycle shift); [[Neratinib (drug)]] 5 µM (+3.6); [[Chlorhexidine (diacetate) (drug)]] 5 µM (+3.4); [[Dihydroartemisinin (drug)]] 5 µM (+3.2); [[Vinblastine (sulfate) (drug)]] 5 µM (+3.0); [[Abemaciclib (drug)]] 5 µM (+2.8) (56 in all, 13 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-7.4, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-5.9, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-4.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-4.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-4.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-3.6, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-3.4); [[Harringtonine (drug)]] 0.05 µM (-3.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.6); [[Temsirolimus (drug)]] 0.05 µM (-1.9); [[TAK-901 (drug)]] 0.05 µM (-1.7); [[Temsirolimus (drug)]] 0.5 µM (-1.3); [[Pyridoxine (hydrochloride) (drug)]] 5 µM (-1.3); [[Filgotinib (drug)]] 5 µM (-1.3); [[Rapamycin (drug)]] 5 µM (-1.3); [[Rapamycin (drug)]] 0.5 µM (-1.3) (32 in all, 17 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[LoVo (line)]], [[PANC-1 (line)]], [[HT-29 (line)]], [[KATO III (line)]], [[SW480 (line)]], [[NCI-H460 (line)]], [[A498 (line)]], [[H4 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 54 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[XPOT]] | Cytosolic tRNA aminoacylation | +0.85 |
| 2 | [[ASNS]] | Cytosolic tRNA aminoacylation | +0.82 |
| 3 | [[PSAT1]] | Cytosolic tRNA aminoacylation | +0.82 |
| 4 | [[MTHFD2]] | Cytosolic tRNA aminoacylation | +0.81 |
| 5 | [[AARS1]] | unfolded protein response | +0.80 |
| 6 | [[GARS1]] | Response of EIF2AK1 (HRI) to heme deficiency | +0.79 |
| 7 | [[PHGDH]] | Cytosolic tRNA aminoacylation | +0.79 |
| 8 | [[TCEA1]] | Cytosolic tRNA aminoacylation | +0.78 |
| 9 | [[CARS1]] | Response of EIF2AK1 (HRI) to heme deficiency | +0.78 |
| 10 | [[TRIB3]] | Cytosolic tRNA aminoacylation | +0.77 |
| 11 | [[GOT1]] | Response of EIF2AK1 (HRI) to heme deficiency | +0.77 |
| 12 | [[MARS1]] | unfolded protein response | +0.77 |
| 13 | [[CHAC1]] | Cytosolic tRNA aminoacylation | +0.76 |
| 14 | [[HSPA9]] | Cytosolic tRNA aminoacylation | +0.76 |
| 15 | [[SARS1]] | Response of EIF2AK1 (HRI) to heme deficiency | +0.76 |

## + arm (77)

| Gene | Projection | Name |
|---|---|---|
| [[GARS1]] | 0.939 | glycyl-tRNA synthetase 1 |
| [[AARS1]] | 0.938 | alanyl-tRNA synthetase 1 |
| [[XPOT]] | 0.930 | exportin for tRNA |
| [[ASNS]] | 0.925 | asparagine synthetase (glutamine-hydrolyzing) |
| [[SARS1]] | 0.912 | seryl-tRNA synthetase 1 |
| [[PHGDH]] | 0.900 | phosphoglycerate dehydrogenase |
| [[TRIB3]] | 0.897 | tribbles pseudokinase 3 |
| [[IARS1]] | 0.893 | isoleucyl-tRNA synthetase 1 |
| [[MTHFD2]] | 0.891 | methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2, methenyltetrahydrofolate cyclohydrolase |
| [[MARS1]] | 0.888 | methionyl-tRNA synthetase 1 |
| [[PSAT1]] | 0.887 | phosphoserine aminotransferase 1 |
| [[CARS1]] | 0.879 | cysteinyl-tRNA synthetase 1 |
| [[CHAC1]] | 0.861 | ChaC glutathione specific gamma-glutamylcyclotransferase 1 |
| [[TCEA1]] | 0.850 | transcription elongation factor A1 |
| [[SESN2]] | 0.842 | sestrin 2 |
| [[TARS1]] | 0.838 | threonyl-tRNA synthetase 1 |
| [[HSPA9]] | 0.830 | heat shock protein family A (Hsp70) member 9 |
| [[NARS1]] | 0.827 | asparaginyl-tRNA synthetase 1 |
| [[GOT1]] | 0.821 | glutamic-oxaloacetic transaminase 1 |
| [[SLC1A4]] | 0.816 | solute carrier family 1 member 4 |
| [[EPRS1]] | 0.814 | glutamyl-prolyl-tRNA synthetase 1 |
| [[EIF2S2]] | 0.806 | eukaryotic translation initiation factor 2 subunit beta |
| [[ADM2]] | 0.774 | adrenomedullin 2 |
| [[LINC00662]] | 0.774 | long independently transcribed non-coding RNA 662 |
| [[ZFAND1]] | 0.769 | zinc finger AN1-type containing 1 |
| [[RSL24D1]] | 0.768 | ribosomal L24 domain containing 1 |
| [[SHMT2]] | 0.763 | serine hydroxymethyltransferase 2 |
| [[GPT2]] | 0.758 | glutamic--pyruvic transaminase 2 |
| [[CLGN]] | 0.756 | calmegin |
| [[ALDH1L2]] | 0.739 | aldehyde dehydrogenase 1 family member L2 |
| [[AKNA]] | 0.723 | AT-hook transcription factor |
| [[PYCR1]] | 0.719 | pyrroline-5-carboxylate reductase 1 |
| [[ULBP1]] | 0.718 | UL16 binding protein 1 |
| [[IDH1]] | 0.713 | isocitrate dehydrogenase (NADP(+)) 1 |
| [[SLC1A5]] | 0.710 | solute carrier family 1 member 5 |
| [[JDP2]] | 0.701 | Jun dimerization protein 2 |
| [[ARHGEF2]] | 0.698 | Rho/Rac guanine nucleotide exchange factor 2 |
| [[SLC7A1]] | 0.695 | solute carrier family 7 member 1 |
| [[TUBE1]] | 0.685 | tubulin epsilon 1 |
| [[SLC7A5]] | 0.664 | solute carrier family 7 member 5 |
| [[GRPEL2]] | 0.654 | GrpE like 2, mitochondrial |
| [[ANKRD11]] | 0.653 | ankyrin repeat domain 11 |
| [[ASNSP1]] | 0.643 | ASNS pseudogene 1 |
| [[GTPBP2]] | 0.630 | GTP binding protein 2 |
| [[NUPR1]] | 0.630 | nuclear protein 1, transcriptional regulator |
| [[KDM4A]] | 0.629 | lysine demethylase 4A |
| [[ERICH2]] | 0.629 | glutamate rich 2 |
| [[RBCK1]] | 0.619 | RANBP2-type and C3HC4-type zinc finger containing 1 |
| [[ANK2]] | 0.618 | ankyrin 2 |
| [[PYROXD1]] | 0.606 | pyridine nucleotide-disulphide oxidoreductase domain 1 |
| [[RNF187]] | 0.605 | ring finger protein 187 |
| [[CTH]] | 0.603 | cystathionine gamma-lyase |
| [[CCPG1]] | 0.598 | cell cycle progression 1 |
| [[LARP6]] | 0.591 | La ribonucleoprotein 6, translational regulator |
| [[TOM1L1]] | 0.583 | target of myb1 like 1 membrane trafficking protein |
| [[PABPC1L]] | 0.570 | poly(A) binding protein cytoplasmic 1 like |
| [[DESI2]] | 0.556 | desumoylating isopeptidase 2 |
| [[DTD1]] | 0.549 | D-aminoacyl-tRNA deacylase 1 |
| [[DDIT3]] | 0.542 | DNA damage inducible transcript 3 |
| [[TXNDC12]] | 0.534 | thioredoxin domain containing 12 |
| [[CAMTA2]] | 0.523 | calmodulin binding transcription activator 2 |
| [[TTC39B]] | 0.517 | tetratricopeptide repeat domain 39B |
| [[TSEN15]] | 0.516 | tRNA splicing endonuclease subunit 15 |
| [[PSPH]] | 0.516 | phosphoserine phosphatase |
| [[CMKLR2]] | 0.514 | chemerin chemokine-like receptor 2 |
| [[STC2]] | 0.514 | stanniocalcin 2 |
| [[POLR2L]] | -0.494 | RNA polymerase II, I and III subunit L |
| [[SLC22A15]] | 0.480 | solute carrier family 22 member 15 |
| [[BEX2]] | 0.477 | brain expressed X-linked 2 |
| [[CYP2R1]] | 0.474 | cytochrome P450 family 2 subfamily R member 1 |
| [[BCAT1]] | 0.470 | branched chain amino acid transaminase 1 |
| [[AP1AR]] | 0.467 | adaptor related protein complex 1 associated regulatory protein |
| [[CSRP1-AS1]] | 0.465 | CSRP1 antisense RNA 1 |
| [[SMIM20]] | 0.454 | small integral membrane protein 20 |
| [[ITPKA]] | 0.447 | inositol-trisphosphate 3-kinase A |
| [[TNFRSF10B]] | 0.418 | TNF receptor superfamily member 10b |
| [[SH3YL1]] | 0.346 | SH3 and SYLF domain containing 1 |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 63; `graph/modules.parquet` — module == 63; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [62] (drug-dose × line)
