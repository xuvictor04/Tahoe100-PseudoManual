---
module: 20
type: "module"
n_genes: 191
n_plus: 99
n_minus: 92
arms_opposite: true
mean_cos_between_arms: -0.29104718565940857
label: "Cap-dependent Translation Initiation"
label_source: "reactome"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 020

*Cap-dependent Translation Initiation · 191 genes (99 in the + arm, 92 in the − arm) · [[Module 020.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **Cap-dependent Translation Initiation** (reactome, q 2e-08; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | Eukaryotic Translation Initiation | reactome | 12/99 | 15.6 | 2e-08 |
| + | Cap-dependent Translation Initiation | reactome | 12/99 | 15.6 | 2e-08 |
| + | L13a-mediated translational silencing of Ceruloplasmin expression | reactome | 11/99 | 15.4 | 1e-07 |
| + | GTP hydrolysis and joining of the 60S ribosomal subunit | reactome | 11/99 | 15.2 | 1e-07 |
| + | Eukaryotic Translation Elongation | reactome | 10/99 | 16.6 | 4e-07 |
| + | Viral Infection Pathways | reactome | 25/99 | 4.15 | 7e-07 |
| + | Formation of a pool of free 40S subunits | reactome | 10/99 | 15.4 | 8e-07 |
| + | Translation | reactome | 15/99 | 7.01 | 3e-06 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 19), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Dinaciclib (drug)]] 0.5 µM (+11.5, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+10.9, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+9.9, ⚠ toxic; transcription drop; cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+6.5, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+5.8); [[c-Kit-IN-1 (drug)]] 0.05 µM (+4.2, ⚠ unreliable plate only); [[Niclosamide (olamine) (drug)]] 5 µM (+3.6, ⚠ toxic; cell-cycle shift); [[Lonafarnib (drug)]] 5 µM (+3.5, ⚠ toxic); [[Auranofin (drug)]] 5 µM (+3.1); [[Digitoxin (drug)]] 0.5 µM (+3.0, ⚠ cell-cycle shift); [[Erlotinib (drug)]] 0.05 µM (+2.7); [[Fenofibrate (drug)]] 0.05 µM (+2.4); [[Benproperine (phosphate) (drug)]] 0.05 µM (+2.3); [[Folic acid (drug)]] 5 µM (+2.3); [[c-Kit-IN-1 (drug)]] 0.5 µM (+2.3); [[Budesonide (drug)]] 5 µM (+2.2); [[Clobetasol propionate (drug)]] 5 µM (+2.2); [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM (+2.1) (146 in all, 31 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-11.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-6.9, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.0, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.5 µM (-3.5, ⚠ cell-cycle shift); [[Ipatasertib (drug)]] 0.5 µM (-3.4); [[Celecoxib (drug)]] 0.5 µM (-2.6); [[Homoharringtonine (drug)]] 0.05 µM (-2.4); [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM (-2.4); [[9-ING-41 (drug)]] 0.5 µM (-2.3); [[Azithromycin (hydrate) (drug)]] 5 µM (-2.3); [[Docetaxel (Trihydrate) (drug)]] 0.5 µM (-2.3); [[Bimiralisib (drug)]] 0.5 µM (-2.3); [[Entrectinib (drug)]] 5 µM (-2.3); [[Adagrasib (drug)]] 5 µM (-2.2) (116 in all, 15 with an alert ⚠; shown: the 10 strongest and the 4 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[PANC-1 (line)]], [[SW480 (line)]], [[A-172 (line)]], [[LoVo (line)]], [[HOP62 (line)]], [[NCI-H460 (line)]], [[MIA PaCa-2 (line)]], [[KATO III (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 32 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[EEF1A1]] | Formation of a pool of free 40S subunits | +0.71 |
| 2 | [[ANKRD30BL]] | Eukaryotic Translation Elongation | +0.70 |
| 3 | [[RPL10]] | Formation of the ternary complex, and subsequently, the 43S complex | +0.67 |
| 4 | [[RPL6]] | Formation of the ternary complex, and subsequently, the 43S complex | +0.67 |
| 5 | [[RPL18A]] | Formation of the ternary complex, and subsequently, the 43S complex | +0.67 |
| 6 | [[RPL4]] | Formation of the ternary complex, and subsequently, the 43S complex | +0.67 |
| 7 | [[EEF1A1P5]] | Formation of a pool of free 40S subunits | +0.66 |
| 8 | [[RPL3]] | Formation of the ternary complex, and subsequently, the 43S complex | +0.65 |
| 9 | [[HFM1]] | Eukaryotic Translation Elongation | +0.64 |
| 10 | [[DHFR]] | Eukaryotic Translation Elongation | +0.63 |
| 11 | [[HNRNPA1L3]] | Eukaryotic Translation Elongation | +0.60 |
| 12 | [[EIF4B]] | Peptide chain elongation | +0.59 |
| 13 | [[TMED7]] | Maturation of DENV proteins | +0.59 |
| 14 | [[IPO5]] | Eukaryotic Translation Elongation | +0.58 |
| 15 | [[RPN1]] | Eukaryotic Translation Elongation | +0.57 |

*⚠ 2 of its 191 genes are in the vector space only through drug-doses that carry an alert (`embed/genes.parquet` evidence_flagged_only): their place here may reflect what those drug-doses did to the cells. They are marked in the tables of this note.*

## + arm (99)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[RPSA]] | 0.879 | ribosomal protein SA |  |
| [[TXNDC5]] | 0.839 | thioredoxin domain containing 5 |  |
| [[DHFR]] | 0.826 | dihydrofolate reductase |  |
| [[HNRNPA3]] | 0.815 | heterogeneous nuclear ribonucleoprotein A3 |  |
| [[RPN1]] | 0.809 | ribophorin I |  |
| [[IPO5]] | 0.793 | importin 5 |  |
| [[BPNT2]] | 0.783 | 3'(2'), 5'-bisphosphate nucleotidase 2 |  |
| [[UGGT1]] | 0.755 | UDP-glucose glycoprotein glucosyltransferase 1 |  |
| [[ANKRD30BL]] | 0.737 | ankyrin repeat domain 30B like |  |
| [[EEF1A1]] | 0.729 | eukaryotic translation elongation factor 1 alpha 1 |  |
| [[PABIR2]] | 0.722 | PABIR family member 2 |  |
| [[MAT2A]] | 0.719 | methionine adenosyltransferase 2A |  |
| [[TMED7]] | 0.717 | transmembrane p24 trafficking protein 7 |  |
| [[PAICS]] | 0.712 | phosphoribosylaminoimidazole carboxylase and phosphoribosylaminoimidazolesuccinocarboxamide synthase |  |
| [[YWHAQ]] | 0.707 | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein theta |  |
| [[FAM91A1]] | 0.705 | family with sequence similarity 91 member A1 |  |
| [[RPL10]] | 0.703 | ribosomal protein L10 |  |
| [[DPAGT1]] | 0.703 | dolichyl-phosphate N-acetylglucosaminephosphotransferase 1 |  |
| [[RPS3A]] | 0.689 | ribosomal protein S3A |  |
| [[RPL6]] | 0.682 | ribosomal protein L6 |  |
| [[DHX15]] | 0.671 | DEAH-box helicase 15 |  |
| [[EIF3F]] | 0.668 | eukaryotic translation initiation factor 3 subunit F |  |
| [[EDEM1]] | 0.665 | ER degradation enhancing alpha-mannosidase like protein 1 |  |
| [[VMA21]] | 0.664 | vacuolar ATPase assembly factor VMA21 |  |
| [[LINC03009]] | 0.659 | — |  |
| [[SIGMAR1]] | 0.651 | sigma receptor chaperone 1 |  |
| [[ILF2]] | 0.647 | interleukin enhancer binding factor 2 |  |
| [[ATP2A2]] | 0.645 | ATPase sarcoplasmic/endoplasmic reticulum Ca2+ transporting 2 |  |
| [[EEF1A1P5]] | 0.645 | eukaryotic translation elongation factor 1 alpha 1 pseudogene 5 |  |
| [[HFM1]] | 0.641 | helicase for meiosis 1 |  |
| [[RPL4]] | 0.634 | ribosomal protein L4 |  |
| [[PTPN18]] | 0.633 | protein tyrosine phosphatase non-receptor type 18 |  |
| [[CPSF6]] | 0.632 | cleavage and polyadenylation specific factor 6 |  |
| [[CA5BP1-1]] | 0.631 | — |  |
| [[RPL18A]] | 0.630 | ribosomal protein L18a |  |
| [[RPS18]] | 0.630 | ribosomal protein S18 |  |
| [[ICMT]] | 0.627 | isoprenylcysteine carboxyl methyltransferase |  |
| [[EIF3H]] | 0.627 | eukaryotic translation initiation factor 3 subunit H |  |
| [[SUMO1]] | 0.622 | small ubiquitin like modifier 1 |  |
| [[TM9SF3]] | 0.621 | transmembrane 9 superfamily member 3 |  |
| [[CRKL]] | 0.617 | CRK like proto-oncogene, adaptor protein |  |
| [[ENOPH1]] | 0.616 | enolase-phosphatase 1 |  |
| [[LIG3]] | 0.615 | DNA ligase 3 |  |
| [[RPL3]] | 0.615 | ribosomal protein L3 |  |
| [[HNRNPA1L3]] | 0.614 | heterogeneous nuclear ribonucleoprotein A1 like 3 |  |
| [[EIF5A]] | 0.610 | eukaryotic translation initiation factor 5A |  |
| [[TSN]] | 0.609 | translin |  |
| [[NAXD]] | 0.606 | NAD(P)HX dehydratase |  |
| [[ELAVL1]] | 0.601 | ELAV like RNA binding protein 1 |  |
| [[NDUFA10]] | 0.596 | NADH:ubiquinone oxidoreductase subunit A10 |  |
| [[SPTLC1]] | 0.576 | serine palmitoyltransferase long chain base subunit 1 |  |
| [[SDHD]] | 0.573 | succinate dehydrogenase complex subunit D |  |
| [[AGBL5]] | 0.550 | AGBL carboxypeptidase 5 |  |
| [[SMG1P1]] | 0.548 | SMG1 pseudogene 1 |  |
| [[POLR2B]] | 0.546 | RNA polymerase II subunit B |  |
| [[VDAC2]] | 0.546 | voltage dependent anion channel 2 |  |
| [[PCDHGC3]] | 0.542 | protocadherin gamma subfamily C, 3 |  |
| [[AP2B1]] | 0.542 | adaptor related protein complex 2 subunit beta 1 |  |
| [[DCAF16]] | 0.539 | DDB1 and CUL4 associated factor 16 |  |
| [[G6PD]] | 0.539 | glucose-6-phosphate dehydrogenase |  |
| [[ARF1]] | 0.535 | ARF GTPase 1 |  |
| [[PDCL3]] | 0.527 | phosducin like 3 |  |
| [[C1D]] | 0.521 | C1D nuclear receptor corepressor |  |
| [[DNAJC10]] | 0.516 | DnaJ heat shock protein family (Hsp40) member C10 |  |
| [[EOLA2]] | 0.515 | endothelium and lymphocyte associated ASCH domain 2 |  |
| [[GPAA1]] | 0.513 | glycosylphosphatidylinositol anchor attachment 1 |  |
| [[EIF2D]] | 0.503 | eukaryotic translation initiation factor 2D |  |
| [[IL18BP]] | 0.499 | interleukin 18 binding protein |  |
| [[OGT]] | 0.495 | O-linked N-acetylglucosamine (GlcNAc) transferase |  |
| [[SPCS3]] | 0.493 | signal peptidase complex subunit 3 |  |
| [[USF1]] | 0.492 | upstream transcription factor 1 |  |
| [[CTC1]] | 0.483 | CST telomere replication complex component 1 |  |
| [[CLNS1A]] | 0.481 | chloride nucleotide-sensitive channel 1A |  |
| [[APEX1]] | 0.481 | apurinic/apyrimidinic endodeoxyribonuclease 1 |  |
| [[EIF2B1]] | 0.481 | eukaryotic translation initiation factor 2B subunit alpha |  |
| [[PPIP5K2]] | 0.473 | diphosphoinositol pentakisphosphate kinase 2 |  |
| [[EIF4B]] | 0.464 | eukaryotic translation initiation factor 4B |  |
| [[FUNDC2]] | 0.451 | FUN14 domain containing 2 |  |
| [[PTP4A1]] | 0.448 | protein tyrosine phosphatase 4A1 |  |
| [[DPM2]] | 0.447 | dolichyl-phosphate mannosyltransferase subunit 2, regulatory |  |
| [[STAG3L4]] | 0.439 | STAG3 cohesin complex component like 4 (pseudogene) | ⚠ only flagged evidence |
| [[STYX]] | 0.438 | serine/threonine/tyrosine interacting protein |  |
| [[PMS2]] | 0.430 | PMS1 homolog 2, mismatch repair system component |  |
| [[MINPP1]] | 0.424 | multiple inositol-polyphosphate phosphatase 1 |  |
| [[CSDE1]] | 0.423 | cold shock domain containing E1 |  |
| [[C2CD3]] | 0.420 | C2 domain containing 3 centriole elongation regulator |  |
| [[NPEPPSP1]] | 0.414 | NPEPPS pseudogene 1 |  |
| [[ZCCHC4]] | 0.390 | zinc finger CCHC-type containing 4 |  |
| [[CLTC]] | 0.388 | clathrin heavy chain |  |
| [[TLN1]] | 0.380 | talin 1 |  |
| [[IDH3A]] | 0.378 | isocitrate dehydrogenase (NAD(+)) 3 catalytic subunit alpha |  |
| [[LINC01232]] | 0.372 | long independently transcribed non-coding RNA 1232 |  |
| [[MRPS22]] | 0.347 | mitochondrial ribosomal protein S22 |  |
| [[GALNT2]] | 0.342 | polypeptide N-acetylgalactosaminyltransferase 2 |  |
| [[TSKU]] | 0.328 | tsukushi, small leucine rich proteoglycan |  |
| [[MREG]] | 0.311 | melanoregulin |  |
| [[CFL1]] | 0.298 | cofilin 1 |  |
| [[SNUPN]] | 0.287 | snurportin 1 |  |
| [[SNX33]] | 0.261 | sorting nexin 33 |  |

## − arm (92)

| Gene | Projection | Name | Alert |
|---|---|---|---|
| [[CROCCP2-1]] | -0.845 | — |  |
| [[NKAP]] | -0.799 | NFKB activating protein |  |
| [[ZNF503]] | -0.787 | zinc finger protein 503 |  |
| [[ZMYM5]] | -0.780 | zinc finger MYM-type containing 5 |  |
| [[INAFM1]] | -0.768 | InaF motif containing 1 |  |
| [[EIF1B]] | -0.760 | eukaryotic translation initiation factor 1B |  |
| [[ING2]] | -0.736 | inhibitor of growth family member 2 |  |
| [[FOXA2]] | -0.731 | forkhead box A2 |  |
| [[METTL23]] | -0.727 | methyltransferase 23, arginine |  |
| [[ERVK3-1]] | -0.724 | endogenous retrovirus group K3 member 1 |  |
| [[OFD1]] | -0.721 | OFD1 centriole and centriolar satellite protein |  |
| [[GGNBP2]] | -0.720 | gametogenetin binding protein 2 |  |
| [[DYNLL1]] | -0.713 | dynein light chain LC8-type 1 |  |
| [[SUMO4]] | -0.710 | small ubiquitin like modifier 4 |  |
| [[TERF2IP]] | -0.702 | TERF2 interacting protein |  |
| [[PIAS4]] | -0.698 | protein inhibitor of activated STAT 4 |  |
| [[IL10RB]] | -0.695 | interleukin 10 receptor subunit beta |  |
| [[SIRT6]] | -0.692 | sirtuin 6 |  |
| [[LRCH3]] | -0.687 | leucine rich repeats and calponin homology domain containing 3 |  |
| [[BTG1]] | -0.687 | BTG anti-proliferation factor 1 |  |
| [[ZKSCAN1]] | -0.677 | zinc finger with KRAB and SCAN domains 1 |  |
| [[RBX1]] | -0.672 | ring-box 1 |  |
| [[SNHG8]] | -0.666 | small nucleolar RNA host gene 8 |  |
| [[LRRC8E]] | -0.661 | leucine rich repeat containing 8 VRAC subunit E |  |
| [[ADPRM]] | -0.657 | ADP-ribose/CDP-alcohol diphosphatase, manganese dependent |  |
| [[WHAMM]] | -0.656 | WASP homolog associated with actin, golgi membranes and microtubules |  |
| [[SNHG32]] | -0.654 | small nucleolar RNA host gene 32 |  |
| [[IRX5]] | -0.652 | iroquois homeobox 5 |  |
| [[PQBP1]] | -0.639 | polyglutamine binding protein 1 |  |
| [[FOXD1]] | -0.637 | forkhead box D1 |  |
| [[GATAD1]] | -0.635 | GATA zinc finger domain containing 1 |  |
| [[IER5]] | -0.633 | immediate early response 5 |  |
| [[POLR1H]] | -0.633 | RNA polymerase I subunit H |  |
| [[CHKB]] | -0.620 | choline kinase beta |  |
| [[UPF3B]] | -0.614 | UPF3B regulator of nonsense mediated mRNA decay |  |
| [[PURA]] | -0.613 | purine rich element binding protein A |  |
| [[MSX2]] | -0.607 | msh homeobox 2 |  |
| [[SNHG12]] | -0.606 | small nucleolar RNA host gene 12 |  |
| [[SMIM29]] | -0.603 | small integral membrane protein 29 |  |
| [[FAM98C]] | -0.599 | tRNA splicing ligase complex subunit 3C |  |
| [[H3-3B]] | -0.596 | H3.3 histone B |  |
| [[FAM193A]] | -0.593 | family with sequence similarity 193 member A |  |
| [[EIF1]] | -0.592 | eukaryotic translation initiation factor 1 |  |
| [[TMEM60]] | -0.585 | transmembrane protein 60 |  |
| [[WBP4]] | -0.583 | WW domain binding protein 4 |  |
| [[SERTAD1]] | -0.581 | SERTA domain containing 1 |  |
| [[UBN1]] | -0.573 | ubinuclein 1 |  |
| [[EPB41L4A-AS1]] | -0.571 | EPB41L4A antisense RNA 1 |  |
| [[GGT7]] | -0.560 | gamma-glutamyltransferase 7 |  |
| [[SUGP1]] | -0.554 | SURP and G-patch domain containing 1 |  |
| [[SOX4]] | -0.554 | SRY-box transcription factor 4 |  |
| [[NBPF11]] | -0.553 | NBPF member 11 |  |
| [[NFKBIB]] | -0.541 | NFKB inhibitor beta |  |
| [[PHF20]] | -0.529 | PHD finger protein 20 |  |
| [[PHACTR4]] | -0.523 | phosphatase and actin regulator 4 |  |
| [[ITSN2]] | -0.521 | intersectin 2 |  |
| [[RSPH3]] | -0.510 | radial spoke head 3 |  |
| [[RHOG]] | -0.506 | ras homolog family member G |  |
| [[MAP1S]] | -0.503 | microtubule associated protein 1S |  |
| [[NBPF12]] | -0.503 | NBPF member 12 |  |
| [[NPHP3]] | -0.503 | nephrocystin 3 |  |
| [[CBR3]] | -0.501 | carbonyl reductase 3 |  |
| [[KCTD11]] | -0.495 | potassium channel tetramerization domain containing 11 |  |
| [[KLHL22]] | -0.492 | kelch like family member 22 |  |
| [[MRNIP]] | -0.489 | MRN complex interacting protein |  |
| [[UBAP1]] | -0.476 | ubiquitin associated protein 1 |  |
| [[DNAJC21]] | -0.470 | DnaJ heat shock protein family (Hsp40) member C21 |  |
| [[TNIP2]] | -0.464 | TNFAIP3 interacting protein 2 |  |
| [[C11orf68]] | -0.458 | chromosome 11 open reading frame 68 |  |
| [[CERS4]] | -0.457 | ceramide synthase 4 |  |
| [[RHOD]] | -0.450 | ras homolog family member D |  |
| [[IRX2]] | -0.440 | iroquois homeobox 2 |  |
| [[ZFAS1]] | -0.426 | ZNFX1 antisense RNA 1 |  |
| [[ZIC2]] | -0.422 | Zic family zinc finger 2 |  |
| [[TNFRSF10C]] | -0.415 | TNF receptor superfamily member 10c |  |
| [[SRSF9]] | -0.415 | serine and arginine rich splicing factor 9 | ⚠ only flagged evidence |
| [[AKIRIN2]] | -0.413 | akirin 2 |  |
| [[TAF1D]] | -0.411 | TATA-box binding protein associated factor, RNA polymerase I subunit D |  |
| [[CXorf38]] | -0.409 | chromosome X open reading frame 38 |  |
| [[MAP7D3]] | -0.407 | MAP7 domain containing 3 |  |
| [[PWWP2B]] | -0.398 | PWWP domain containing 2B |  |
| [[MYO9A]] | -0.394 | myosin IXA |  |
| [[CHMP4C]] | -0.389 | charged multivesicular body protein 4C |  |
| [[DYNC2I1]] | -0.386 | dynein 2 intermediate chain 1 |  |
| [[PAOX]] | -0.360 | polyamine oxidase |  |
| [[GTF2IRD1]] | -0.360 | GTF2I repeat domain containing 1 |  |
| [[ARRDC4]] | -0.347 | arrestin domain containing 4 |  |
| [[IGIP]] | -0.316 | IgA inducing protein |  |
| [[DDI2]] | -0.299 | DDI proteasomal shuttling factor 2 |  |
| [[KLHL36]] | -0.0660 | kelch like family member 36 |  |
| [[MED15]] | -0.0625 | mediator complex subunit 15 |  |
| [[SNHG1]] | -0.0158 | small nucleolar RNA host gene 1 |  |

## Data

- `graph/nodes.parquet` — module == 20; `graph/modules.parquet` — module == 20; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [19] (drug-dose × line)
