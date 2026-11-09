---
module: 49
type: "module"
n_genes: 93
n_plus: 93
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.11892502009868622
label: "XBP1(S) activates chaperone genes"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 049

*XBP1(S) activates chaperone genes · 93 genes (single-armed) · [[Module 049.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **XBP1(S) activates chaperone genes** (reactome, q 3e-07; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | XBP1(S) activates chaperone genes | reactome | 8/93 | 28.2 | 3e-07 |
| + | XBP1(S) activates chaperone genes | reactome | 8/93 | 28.2 | 3e-07 |
| + | IRE1alpha activates chaperones | reactome | 8/93 | 27.0 | 5e-07 |
| all | IRE1alpha activates chaperones | reactome | 8/93 | 27.0 | 5e-07 |
| all | Unfolded Protein Response (UPR) | reactome | 8/93 | 14.6 | 5e-05 |
| + | Unfolded Protein Response (UPR) | reactome | 8/93 | 14.6 | 5e-05 |
| + | Cotranslational targeting of proteins to the endoplasmic reticulum | reactome | 8/93 | 8.59 | 0.002 |
| all | Cotranslational targeting of proteins to the endoplasmic reticulum | reactome | 8/93 | 8.59 | 0.002 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 48), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Abemaciclib (drug)]] 0.5 µM (+1.5); [[c-Kit-IN-1 (drug)]] 0.05 µM (+1.5, ⚠ unreliable plate only); [[TAK-733 (drug)]] 0.05 µM (+1.4); [[Lipoic acid (drug)]] 5 µM (+1.3); [[EX229 (drug)]] 0.5 µM (+1.3); [[Vinblastine (sulfate) (drug)]] 5 µM (+1.3); [[Sapanisertib (drug)]] 0.5 µM (+1.2); [[Abemaciclib (drug)]] 5 µM (+1.2); [[Auranofin (drug)]] 5 µM (+1.1); [[Terfenadine (drug)]] 5 µM (+1.1); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (+1.0) (18 in all, 1 with an alert ⚠; shown: the 10 strongest and the 1 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-4.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-4.1, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 5 µM (-3.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-3.6, ⚠ cell-cycle shift); [[Digitoxin (drug)]] 0.5 µM (-3.1, ⚠ cell-cycle shift); [[Idarubicin (hydrochloride) (drug)]] 5 µM (-3.0, ⚠ cell-cycle shift); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (-2.9); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.7, ⚠ cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (-2.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (-2.0, ⚠ toxic; transcription drop; cell-cycle shift); [[Retinoic acid (drug)]] 0.05 µM (-1.6); [[Busulfan (drug)]] 0.05 µM (-1.6); [[Homoharringtonine (drug)]] 0.05 µM (-1.6); [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM (-1.6); [[Ixazomib citrate (drug)]] 0.5 µM (-1.6); [[Temsirolimus (drug)]] 0.05 µM (-1.6); [[TAK-901 (drug)]] 0.05 µM (-1.5); [[Berbamine (drug)]] 0.05 µM (-1.5); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (-1.4) (39 in all, 16 with an alert ⚠; shown: the 10 strongest and the 9 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[HS-578T (line)]], [[H4 (line)]], [[A498 (line)]], [[HOP62 (line)]], [[KATO III (line)]], [[A-172 (line)]], [[SW 900 (line)]], [[hTERT-HPNE (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 30 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[MYDGF]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.67 |
| 2 | [[SLC33A1]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.67 |
| 3 | [[GMPPA]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.66 |
| 4 | [[COG3]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.66 |
| 5 | [[SSR2]] | XBP1(S) activates chaperone genes | +0.64 |
| 6 | [[DNAJC25]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.64 |
| 7 | [[SELENOS]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.64 |
| 8 | [[HM13]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.62 |
| 9 | [[GORASP2]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.62 |
| 10 | [[SEC61B]] | XBP1(S) activates chaperone genes | +0.61 |
| 11 | [[PDIA5]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.61 |
| 12 | [[NFXL1]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.60 |
| 13 | [[DNAJB9]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.58 |
| 14 | [[RINT1]] | Cotranslational targeting of proteins to the endoplasmic reticulum | +0.58 |
| 15 | [[MED8]] | XBP1(S) activates chaperone genes | +0.58 |

## + arm (93)

| Gene | Projection | Name |
|---|---|---|
| [[COG3]] | 0.890 | component of oligomeric golgi complex 3 |
| [[SSR2]] | 0.876 | signal sequence receptor subunit 2 |
| [[GORASP2]] | 0.857 | golgi reassembly stacking protein 2 |
| [[PDIA5]] | 0.839 | protein disulfide isomerase family A member 5 |
| [[GMPPA]] | 0.839 | GDP-mannose pyrophosphorylase A |
| [[SLC33A1]] | 0.829 | solute carrier family 33 member 1 |
| [[OSTC]] | 0.829 | oligosaccharyltransferase complex non-catalytic subunit |
| [[HM13]] | 0.815 | histocompatibility minor 13 |
| [[RINT1]] | 0.810 | RAD50 interactor 1 |
| [[RARS1]] | 0.804 | arginyl-tRNA synthetase 1 |
| [[MED8]] | 0.803 | mediator complex subunit 8 |
| [[SLC30A5]] | 0.803 | solute carrier family 30 member 5 |
| [[SELENOS]] | 0.797 | selenoprotein S |
| [[DNAJC25]] | 0.796 | DnaJ heat shock protein family (Hsp40) member C25 |
| [[SEC61B]] | 0.790 | SEC61 translocon subunit beta |
| [[SRPRB]] | 0.787 | SRP receptor subunit beta |
| [[ARL1]] | 0.783 | ARF like GTPase 1 |
| [[SERP1]] | 0.773 | stress associated endoplasmic reticulum protein 1 |
| [[NFXL1]] | 0.766 | nuclear transcription factor, X-box binding like 1 |
| [[RUSF1]] | 0.763 | RUS family member 1 |
| [[MYDGF]] | 0.754 | myeloid derived growth factor |
| [[TMED3]] | 0.747 | transmembrane p24 trafficking protein 3 |
| [[NAT9]] | 0.747 | N-acetyltransferase 9 |
| [[TMEM208]] | 0.744 | transmembrane protein 208 |
| [[ZNF526]] | 0.732 | zinc finger protein 526 |
| [[AKR1A1]] | 0.712 | aldo-keto reductase family 1 member A1 |
| [[DERL2]] | 0.706 | derlin 2 |
| [[ZNF417]] | 0.692 | zinc finger protein 417 |
| [[TMEM243]] | 0.687 | transmembrane protein 243 |
| [[FBXO16]] | 0.684 | F-box protein 16 |
| [[CUL7]] | 0.674 | cullin 7 |
| [[FAM98A]] | 0.671 | tRNA splicing ligase complex subunit 3A |
| [[SLC15A2]] | 0.667 | solute carrier family 15 member 2 |
| [[TIMM17A]] | 0.661 | translocase of inner mitochondrial membrane 17A |
| [[NCK1]] | 0.639 | NCK adaptor protein 1 |
| [[DNAJB9]] | 0.636 | DnaJ heat shock protein family (Hsp40) member B9 |
| [[RTCB]] | 0.635 | RNA 2',3'-cyclic phosphate and 5'-OH ligase |
| [[LINC02693]] | 0.628 | long independently transcribed non-coding RNA 2693 |
| [[UTP6]] | 0.624 | UTP6 small subunit processome component |
| [[ALG5]] | 0.624 | ALG5 dolichyl-phosphate beta-glucosyltransferase |
| [[PREB]] | 0.621 | prolactin regulatory element binding |
| [[SEPTIN7P2]] | 0.621 | septin 7 pseudogene 2 |
| [[SLC25A32]] | 0.605 | solute carrier family 25 member 32 |
| [[RBAK-RBAKDN]] | 0.604 | RBAK-RBAKDN readthrough |
| [[FICD]] | 0.603 | FIC domain protein adenylyltransferase |
| [[ENTPD7]] | 0.593 | ectonucleoside triphosphate diphosphohydrolase 7 |
| [[SEC11C]] | 0.593 | SEC11 homolog C, signal peptidase complex subunit |
| [[MRPL2]] | 0.579 | mitochondrial ribosomal protein L2 |
| [[HID1]] | 0.577 | HID1 domain containing |
| [[ZNF70]] | 0.576 | zinc finger protein 70 |
| [[POLR2C]] | 0.562 | RNA polymerase II subunit C |
| [[SKIC8]] | 0.560 | SKI8 subunit of superkiller complex |
| [[PCGF3-AS1]] | 0.559 | PCGF3 antisense RNA 1 |
| [[GPR180]] | 0.559 | G protein-coupled receptor 180 |
| [[UBE2J1]] | 0.557 | ubiquitin conjugating enzyme E2 J1 |
| [[PLPP5]] | 0.557 | phospholipid phosphatase 5 |
| [[SMCO4]] | 0.541 | single-pass membrane protein with coiled-coil domains 4 |
| [[PARL]] | 0.540 | presenilin associated rhomboid like |
| [[SPCS2]] | 0.538 | signal peptidase complex subunit 2 |
| [[PRPF3]] | 0.534 | pre-mRNA processing factor 3 |
| [[SEC23B]] | 0.531 | SEC23 homolog B, COPII component |
| [[SLC35B1]] | 0.530 | solute carrier family 35 member B1 |
| [[STAM2]] | 0.526 | signal transducing adaptor molecule 2 |
| [[CUTC]] | 0.523 | cutC copper transporter |
| [[TMEM165]] | 0.517 | transmembrane protein 165 |
| [[MPC1]] | 0.511 | mitochondrial pyruvate carrier 1 |
| [[RWDD2A]] | 0.496 | RWD domain containing 2A |
| [[IBTK]] | 0.493 | inhibitor of Bruton tyrosine kinase |
| [[P3H4]] | 0.491 | prolyl 3-hydroxylase family member 4 (inactive) |
| [[KIAA0513]] | 0.483 | KIAA0513 |
| [[SMN1]] | 0.459 | survival of motor neuron 1, telomeric |
| [[SIL1]] | 0.458 | SIL1 nucleotide exchange factor |
| [[CADPS2]] | 0.457 | calcium dependent secretion activator 2 |
| [[CCDC149]] | 0.449 | coiled-coil domain containing 149 |
| [[GOLPH3]] | 0.447 | golgi phosphoprotein 3 |
| [[TMC3-AS1]] | 0.447 | TMC3 antisense RNA 1 |
| [[XBP1]] | 0.442 | X-box binding protein 1 |
| [[FKBP11]] | 0.436 | FKBP prolyl isomerase 11 |
| [[SLC1A1]] | 0.430 | solute carrier family 1 member 1 |
| [[MINAR1]] | 0.424 | membrane integral NOTCH2 associated receptor 1 |
| [[AGR2]] | 0.409 | anterior gradient 2, protein disulphide isomerase family member |
| [[RPGRIP1L]] | 0.409 | RPGRIP1 like |
| [[TAF12]] | 0.401 | TATA-box binding protein associated factor 12 |
| [[PICK1]] | 0.394 | protein interacting with PRKCA 1 |
| [[AQR]] | 0.378 | aquarius intron-binding spliceosomal factor |
| [[WDR25]] | 0.374 | WD repeat domain 25 |
| [[CUZD1]] | 0.361 | CUB and zona pellucida like domains 1 |
| [[MESD]] | 0.343 | mesoderm development LRP chaperone |
| [[NUP160]] | 0.339 | nucleoporin 160 |
| [[SIKE1]] | 0.336 | suppressor of IKBKE 1 |
| [[B4GALT4]] | 0.320 | beta-1,4-galactosyltransferase 4 |
| [[PITHD1]] | 0.293 | PITH domain containing 1 |
| [[RAB10]] | -0.206 | RAB10, member RAS oncogene family |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 49; `graph/modules.parquet` — module == 49; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [48] (drug-dose × line)
