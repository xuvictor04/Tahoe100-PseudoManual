---
module: 60
type: "module"
n_genes: 78
n_plus: 70
n_minus: 8
arms_opposite: true
mean_cos_between_arms: -0.3240617513656616
label: "heat shock"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 060

*heat shock · 78 genes (70 in the + arm, 8 in the − arm) · [[Module 060.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32). The + arm rises where the − arm falls. Arm = the side of the module's main direction a gene sits on.

Label from the validation stage: **heat shock** (control, q 1e-26; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| + | heat shock | control | 13/70 | 200 | 1e-26 |
| all | heat shock | control | 13/78 | 179 | 5e-26 |
| + | Attenuation phase | reactome | 13/70 | 127 | 3e-22 |
| + | HSF1-dependent transactivation | reactome | 14/70 | 97.3 | 5e-22 |
| all | Attenuation phase | reactome | 13/78 | 114 | 1e-21 |
| + | Cellular response to heat stress | reactome | 18/70 | 42.1 | 2e-21 |
| all | HSF1-dependent transactivation | reactome | 14/78 | 87.3 | 3e-21 |
| + | HSF1 activation | reactome | 13/70 | 112 | 3e-21 |

## Drugs that move it

*Mean pooled z of the + arm minus the − arm (`graph/module_pooled_z.npy`, row 59), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it (+ arm up, − arm down): [[Auranofin (drug)]] 5 µM (+24.8); [[Ixazomib citrate (drug)]] 5 µM (+20.4, ⚠ cell-cycle shift); [[Ixazomib citrate (drug)]] 0.5 µM (+18.5); [[Bortezomib (drug)]] 0.05 µM (+17.3, ⚠ cell-cycle shift); [[Bortezomib (drug)]] 5 µM (+12.3, ⚠ toxic; cell-cycle shift); [[Dinaciclib (drug)]] 0.5 µM (+12.2, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+10.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Bortezomib (drug)]] 0.5 µM (+8.1); [[Dinaciclib (drug)]] 0.05 µM (+8.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Niclosamide (olamine) (drug)]] 5 µM (+6.8, ⚠ toxic; cell-cycle shift); [[Infigratinib (drug)]] 5 µM (+4.1); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM (+4.1); [[Peretinoin (drug)]] 5 µM (+3.5); [[Peretinoin (drug)]] 0.5 µM (+3.3); [[Abemaciclib (drug)]] 5 µM (+2.9); [[Thymol (drug)]] 5 µM (+2.8); [[Vinblastine (sulfate) (drug)]] 0.5 µM (+2.7) (119 in all, 29 with an alert ⚠; shown: the 10 strongest and the 7 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-16.5, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-9.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-6.6, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (-5.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (-4.8, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (-4.7, ⚠ cell-cycle shift); [[Belinostat (drug)]] 5 µM (-4.3, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 0.5 µM (-3.9, ⚠ cell-cycle shift); [[Trametinib (drug)]] 5 µM (-2.8, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 0.5 µM (-2.8, ⚠ cell-cycle shift); [[Bimiralisib (drug)]] 0.05 µM (-2.3); [[Brivudine (drug)]] 5 µM (-2.2); [[NVP-BHG712 (drug)]] 0.05 µM (-2.2); [[Homoharringtonine (drug)]] 0.05 µM (-2.2); [[Trametinib (drug)]] 0.05 µM (-2.1); [[Budesonide (drug)]] 5 µM (-2.1); [[Goserelin (acetate) (drug)]] 5 µM (-2.1); [[Bimiralisib (drug)]] 5 µM (-2.1); [[ULK-101 (drug)]] 0.05 µM (-2.1); [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM (-2.0) (124 in all, 24 with an alert ⚠; shown: the 10 strongest and the 10 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[SW480 (line)]], [[HT-29 (line)]], [[KATO III (line)]], [[HOP62 (line)]], [[HEC-1-A (line)]], [[A498 (line)]], [[A-172 (line)]], [[PANC-1 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 43 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PTGES3]] | Folding of actin by CCT/TriC | +0.70 |
| 2 | [[HSP90AA1]] | Mitochondrial unfolded protein response (UPRmt) | +0.67 |
| 3 | [[FKBP4]] | Folding of actin by CCT/TriC | +0.66 |
| 4 | [[HSP90AA2P]] | HSF1 activation | +0.65 |
| 5 | [[PSMD2]] | Folding of actin by CCT/TriC | +0.65 |
| 6 | [[PSMD12]] | Folding of actin by CCT/TriC | +0.64 |
| 7 | [[SOD1]] | HSF1 activation | +0.62 |
| 8 | [[HSP90AB3P]] | Attenuation phase | +0.61 |
| 9 | [[ATPSCKMT]] | Folding of actin by CCT/TriC | +0.61 |
| 10 | [[HSP90AB1]] | Formation of tubulin folding intermediates by CCT/TriC | +0.60 |
| 11 | [[HSPA1B]] | Chaperone Mediated Autophagy | +0.60 |
| 12 | [[CACYBP]] | heat shock | +0.60 |
| 13 | [[HSP90AB2P]] | Attenuation phase | +0.59 |
| 14 | [[STIP1]] | Formation of tubulin folding intermediates by CCT/TriC | +0.59 |
| 15 | [[PSMD14]] | Folding of actin by CCT/TriC | +0.58 |

## + arm (70)

| Gene | Projection | Name |
|---|---|---|
| [[HSP90AA2P]] | 0.922 | heat shock protein 90 alpha family class A member 2, pseudogene |
| [[CACYBP]] | 0.868 | calcyclin binding protein |
| [[HSP90AB3P]] | 0.859 | heat shock protein 90 alpha family class B member 3, pseudogene |
| [[HSP90AA1]] | 0.844 | heat shock protein 90 alpha family class A member 1 |
| [[HSP90AB2P]] | 0.822 | heat shock protein 90 alpha family class B member 2, pseudogene |
| [[HSPD1]] | 0.820 | heat shock protein family D (Hsp60) member 1 |
| [[HSPE1]] | 0.820 | heat shock protein family E (Hsp10) member 1 |
| [[AHSA1]] | 0.818 | activator of HSP90 ATPase activity 1 |
| [[SOD1]] | 0.816 | superoxide dismutase 1 |
| [[CCT4]] | 0.815 | chaperonin containing TCP1 subunit 4 |
| [[HSPA8]] | 0.794 | heat shock protein family A (Hsp70) member 8 |
| [[HSP90AB1]] | 0.787 | heat shock protein 90 alpha family class B member 1 |
| [[TCP1]] | 0.781 | t-complex 1 |
| [[CCT3]] | 0.781 | chaperonin containing TCP1 subunit 3 |
| [[CHORDC1]] | 0.779 | cysteine and histidine rich domain containing 1 |
| [[SERPINH1]] | 0.774 | serpin family H member 1 |
| [[ATP2C1]] | 0.772 | ATPase secretory pathway Ca2+ transporting 1 |
| [[HSPA1B]] | 0.767 | heat shock protein family A (Hsp70) member 1B |
| [[HSPH1]] | 0.755 | heat shock protein family H (Hsp110) member 1 |
| [[PTGES3]] | 0.746 | prostaglandin E synthase 3 |
| [[STIP1]] | 0.726 | stress induced phosphoprotein 1 |
| [[VCP]] | 0.724 | valosin containing protein |
| [[FKBP4]] | 0.709 | FKBP prolyl isomerase 4 |
| [[PSMB7]] | 0.707 | proteasome 20S subunit beta 7 |
| [[CCT6A]] | 0.705 | chaperonin containing TCP1 subunit 6A |
| [[B4GALNT1]] | 0.703 | beta-1,4-N-acetyl-galactosaminyltransferase 1 |
| [[CHRNA5]] | 0.681 | cholinergic receptor nicotinic alpha 5 subunit |
| [[HIBCH]] | 0.677 | 3-hydroxyisobutyryl-CoA hydrolase |
| [[DNAJA4]] | 0.669 | DnaJ heat shock protein family (Hsp40) member A4 |
| [[PSMD2]] | 0.665 | proteasome 26S subunit ubiquitin receptor, non-ATPase 2 |
| [[MLLT11]] | 0.660 | MLLT11 transcription factor 7 cofactor |
| [[PRDX1]] | 0.657 | peroxiredoxin 1 |
| [[ATPSCKMT]] | 0.650 | ATP synthase c subunit lysine N-methyltransferase |
| [[BAG3]] | 0.646 | BAG cochaperone 3 |
| [[PWWP3A]] | 0.642 | PWWP domain containing 3A, DNA repair factor |
| [[PSMD12]] | 0.629 | proteasome 26S subunit, non-ATPase 12 |
| [[HSPA1A]] | 0.627 | heat shock protein family A (Hsp70) member 1A |
| [[POPDC3]] | 0.623 | popeye domain cAMP effector 3 |
| [[PSMD14]] | 0.621 | proteasome 26S subunit, non-ATPase 14 |
| [[PHTF1]] | 0.616 | putative homeodomain transcription factor 1 |
| [[UBB]] | 0.615 | ubiquitin B |
| [[ABCC5]] | 0.595 | ATP binding cassette subfamily C member 5 |
| [[KCMF1]] | 0.586 | potassium channel modulatory factor 1 |
| [[TXN]] | 0.584 | thioredoxin |
| [[HSPB1]] | 0.577 | heat shock protein family B (small) member 1 |
| [[GLA]] | 0.576 | galactosidase alpha |
| [[ST13]] | 0.575 | ST13 Hsp70 interacting protein |
| [[PCBD1]] | 0.567 | pterin-4 alpha-carbinolamine dehydratase 1 |
| [[FXR1]] | 0.567 | FMR1 autosomal homolog 1 |
| [[DNAJB1]] | 0.567 | DnaJ heat shock protein family (Hsp40) member B1 |
| [[HSPA4]] | 0.558 | heat shock protein family A (Hsp70) member 4 |
| [[DNAJA1]] | 0.554 | DnaJ heat shock protein family (Hsp40) member A1 |
| [[HSPE1-MOB4]] | 0.554 | HSPE1-MOB4 readthrough |
| [[YWHAG]] | 0.526 | tyrosine 3-monooxygenase/tryptophan 5-monooxygenase activation protein gamma |
| [[ARPC5]] | 0.512 | actin related protein 2/3 complex subunit 5 |
| [[EIF3I]] | 0.508 | eukaryotic translation initiation factor 3 subunit I |
| [[NECAB3]] | 0.506 | N-terminal EF-hand calcium binding protein 3 |
| [[CRYAB]] | 0.502 | crystallin alpha B |
| [[SNX3]] | 0.501 | sorting nexin 3 |
| [[SUGT1]] | 0.493 | SGT1 assembly cochaperone of MIS12 kinetochore complex |
| [[RUVBL2]] | 0.488 | RuvB like AAA ATPase 2 |
| [[KIF1B]] | 0.471 | kinesin family member 1B |
| [[MORC4]] | 0.471 | MORC family CW-type zinc finger 4 |
| [[SORBS1]] | 0.469 | sorbin and SH3 domain containing 1 |
| [[DEDD2]] | 0.463 | death effector domain containing 2 |
| [[ZNF114]] | 0.444 | zinc finger protein 114 |
| [[RHOQ]] | 0.399 | ras homolog family member Q |
| [[CLU]] | 0.395 | clusterin |
| [[SRP14]] | 0.377 | signal recognition particle 14 |
| [[TUBA4A]] | 0.360 | tubulin alpha 4a |

## − arm (8)

| Gene | Projection | Name |
|---|---|---|
| [[YY1AP1]] | -0.642 | YY1 associated protein 1 |
| [[DOP1A]] | -0.630 | DOP1 leucine zipper like protein A |
| [[LSM14B]] | -0.520 | LSM family member 14B |
| [[SUSD6]] | -0.503 | sushi domain containing 6 |
| [[TYK2]] | -0.499 | tyrosine kinase 2 |
| [[H6PD]] | -0.499 | hexose-6-phosphate dehydrogenase/glucose 1-dehydrogenase |
| [[ARL13B]] | -0.494 | ARF like GTPase 13B |
| [[LCOR]] | -0.465 | ligand dependent nuclear receptor corepressor |

## Data

- `graph/nodes.parquet` — module == 60; `graph/modules.parquet` — module == 60; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [59] (drug-dose × line)
