---
module: 42
type: "module"
n_genes: 103
n_plus: 103
n_minus: 0
arms_opposite: false
mean_cos_between_arms: -0.26413822174072266
label: "UPR ER"
label_source: "control"
tags: ["module"]
generated_by: "tahoemap"
---

# Module 042

*UPR ER · 103 genes (single-armed) · [[Module 042.canvas|open the canvas]]*

A module is a community of the gene graph that links each gene to its 15 strongest partners by |cos| that are replicated (`both halves`: same sign, fdr ≤ 0.10, in two random halves of the compounds) or very strong in one random half (`graph/`). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.

Label from the validation stage: **UPR ER** (control, q 9e-17; `validation/module_labels.csv`).

## Enriched for

*Hypergeometric test per arm, BH q (`validation/module_enrichment.csv`).*

| Arm | Set | Source | Overlap | Fold | q |
|---|---|---|---|---|---|
| all | UPR ER | control | 11/103 | 89.4 | 9e-17 |
| + | UPR ER | control | 11/103 | 89.4 | 9e-17 |
| + | Asparagine N-linked glycosylation | reactome | 23/103 | 11.8 | 4e-15 |
| all | Asparagine N-linked glycosylation | reactome | 23/103 | 11.8 | 4e-15 |
| all | Maturation of DENV proteins | reactome | 11/103 | 31.0 | 7e-11 |
| + | Maturation of DENV proteins | reactome | 11/103 | 31.0 | 7e-11 |
| + | Dengue Virus Genome Translation and Replication | reactome | 12/103 | 21.4 | 5e-10 |
| all | Dengue Virus Genome Translation and Replication | reactome | 12/103 | 21.4 | 5e-10 |

## Drugs that move it

*Mean pooled z of its genes (`graph/module_pooled_z.npy`, row 41), drug-doses with |z| ≥ 1: the 10 strongest, and any of the 10 strongest without an alert beyond them. ⚠ = the drug-dose's artifact flags: the module may move because of what the drug-dose did to the cells (cell death, a drop in transcription, a shift in the cell-cycle mix, ...); shown, not left out.*

- Raise it: [[Dinaciclib (drug)]] 0.5 µM (+6.8, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 5 µM (+6.4, ⚠ toxic; transcription drop; cell-cycle shift); [[Dinaciclib (drug)]] 0.05 µM (+4.1, ⚠ toxic; transcription drop; cell-cycle shift); [[Auranofin (drug)]] 5 µM (+3.4); [[Panobinostat (drug)]] 0.5 µM (+2.3, ⚠ cell-cycle shift); [[Ouabain (Octahydrate) (drug)]] 5 µM (+2.0, ⚠ cell-cycle shift); [[Panobinostat (drug)]] 5 µM (+1.9, ⚠ cell-cycle shift); [[TAK-901 (drug)]] 5 µM (+1.9, ⚠ cell-cycle shift); [[PH-797804 (drug)]] 5 µM (+1.7); [[Belinostat (drug)]] 5 µM (+1.7, ⚠ cell-cycle shift); [[Abemaciclib (drug)]] 0.5 µM (+1.6); [[Abemaciclib (drug)]] 5 µM (+1.6); [[Lipoic acid (drug)]] 5 µM (+1.4); [[Cloxacillin (sodium) (drug)]] 0.05 µM (+1.4); [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM (+1.3); [[Pasireotide (acetate) (drug)]] 5 µM (+1.2); [[EX229 (drug)]] 0.05 µM (+1.2); [[Fluvoxamine (maleate) (drug)]] 0.5 µM (+1.2) (35 in all, 17 with an alert ⚠; shown: the 10 strongest and the 8 next strongest without an alert)
- Lower it: [[Homoharringtonine (drug)]] 5 µM (-7.2, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 5 µM (-5.2, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.5 µM (-4.1, ⚠ cell-cycle shift); [[Homoharringtonine (drug)]] 0.05 µM (-3.6); [[Harringtonine (drug)]] 0.5 µM (-3.5, ⚠ cell-cycle shift); [[Topotecan (hydrochloride) (drug)]] 0.5 µM (-2.1, ⚠ cell-cycle shift); [[Harringtonine (drug)]] 0.05 µM (-2.0); [[Rapamycin (drug)]] 5 µM (-2.0); [[Temsirolimus (drug)]] 0.05 µM (-1.9); [[Selinexor (drug)]] 5 µM (-1.9, ⚠ cell-cycle shift); [[Verteporfin (drug)]] 5 µM (-1.6); [[Clobetasol propionate (drug)]] 0.05 µM (-1.4); [[Rapamycin (drug)]] 0.5 µM (-1.3); [[TAK-901 (drug)]] 0.05 µM (-1.3); [[AZD-8055 (drug)]] 5 µM (-1.2); [[Belumosudil (drug)]] 5 µM (-1.2) (35 in all, 8 with an alert ⚠; shown: the 10 strongest and the 6 next strongest without an alert)

## Cell lines where it responds most

*The lines with the largest mean |module score| over the module's 8 strongest drug-doses (`graph/modules.parquet` responsive_lines), strongest first.*

- [[A-172 (line)]], [[HS-578T (line)]], [[NCI-H2347 (line)]], [[A498 (line)]], [[J82 (line)]], [[A-427 (line)]], [[HOP62 (line)]], [[SNU-423 (line)]]

## Candidate new members

*Members not annotated to the set their arm is enriched for, ranked by mean cos to the annotated members (`validation/novel_members.csv`); ⚠ = a reason to doubt the gene's place (in the vector space only through flagged drug-doses), kept in its rank. 56 candidates, none with an alert; shown: the 15 strongest.*

| # | Gene | Set | Mean cos |
|---|---|---|---|
| 1 | [[PDIA4]] | Maturation of DENV proteins | +0.74 |
| 2 | [[P4HB]] | UPR ER | +0.73 |
| 3 | [[PDIA6]] | Maturation of DENV proteins | +0.72 |
| 4 | [[SEC61A1]] | UPR ER | +0.71 |
| 5 | [[HSP90B1]] | Maturation of DENV proteins | +0.70 |
| 6 | [[PDIA3]] | Unfolded Protein Response (UPR) | +0.69 |
| 7 | [[TMED9]] | UPR ER | +0.69 |
| 8 | [[LMAN1]] | UPR ER | +0.69 |
| 9 | [[SEL1L]] | Dengue Virus Genome Translation and Replication | +0.67 |
| 10 | [[CALU]] | UPR ER | +0.66 |
| 11 | [[CALR]] | IRE1alpha activates chaperones | +0.66 |
| 12 | [[TMED2]] | Dengue Virus Genome Translation and Replication | +0.65 |
| 13 | [[NUCB2]] | UPR ER | +0.65 |
| 14 | [[HSPA5]] | XBP1(S) activates chaperone genes | +0.64 |
| 15 | [[CRELD1]] | UPR ER | +0.64 |

## + arm (103)

| Gene | Projection | Name |
|---|---|---|
| [[PDIA4]] | 0.899 | protein disulfide isomerase family A member 4 |
| [[SEC61A1]] | 0.895 | SEC61 translocon subunit alpha 1 |
| [[P4HB]] | 0.852 | prolyl 4-hydroxylase subunit beta |
| [[HYOU1]] | 0.851 | hypoxia up-regulated 1 |
| [[CALU]] | 0.846 | calumenin |
| [[TMED2]] | 0.844 | transmembrane p24 trafficking protein 2 |
| [[HSP90B1]] | 0.844 | heat shock protein 90 beta family member 1 |
| [[PDIA6]] | 0.830 | protein disulfide isomerase family A member 6 |
| [[LMAN1]] | 0.827 | lectin, mannose binding 1 |
| [[SAR1A]] | 0.824 | secretion associated Ras related GTPase 1A |
| [[P3H1]] | 0.820 | prolyl 3-hydroxylase 1 |
| [[SEL1L]] | 0.818 | SEL1L adaptor subunit of SYVN1 ubiquitin ligase |
| [[TM9SF2]] | 0.805 | transmembrane 9 superfamily member 2 |
| [[DDB1]] | 0.802 | damage specific DNA binding protein 1 |
| [[HSPA5]] | 0.794 | heat shock protein family A (Hsp70) member 5 |
| [[TMED9]] | 0.794 | transmembrane p24 trafficking protein 9 |
| [[SURF4]] | 0.792 | surfeit 4 |
| [[DNAJB11]] | 0.792 | DnaJ heat shock protein family (Hsp40) member B11 |
| [[COPG1]] | 0.791 | coat protein complex I subunit gamma 1 |
| [[SSR1]] | 0.789 | signal sequence receptor subunit 1 |
| [[NOMO2]] | 0.787 | NODAL modulator 2 |
| [[CALR]] | 0.787 | calreticulin |
| [[MANF]] | 0.786 | mesencephalic astrocyte derived neurotrophic factor |
| [[MLEC]] | 0.783 | malectin |
| [[SEC24C]] | 0.781 | SEC24 homolog C, COPII component |
| [[STT3A]] | 0.780 | STT3 oligosaccharyltransferase complex catalytic subunit A |
| [[DNAJC3]] | 0.778 | DnaJ heat shock protein family (Hsp40) member C3 |
| [[PDIA3]] | 0.778 | protein disulfide isomerase family A member 3 |
| [[GGCX]] | 0.774 | gamma-glutamyl carboxylase |
| [[SEC63]] | 0.761 | SEC63 protein translocation regulator |
| [[SLC39A7]] | 0.736 | solute carrier family 39 member 7 |
| [[HDLBP]] | 0.722 | high density lipoprotein binding protein |
| [[LMAN2]] | 0.716 | lectin, mannose binding 2 |
| [[NUCB2]] | 0.708 | nucleobindin 2 |
| [[FKBP10]] | 0.707 | FKBP prolyl isomerase 10 |
| [[CRELD1]] | 0.704 | CRELD disulfide isomerase 1 |
| [[SRPRA]] | 0.703 | SRP receptor subunit alpha |
| [[ALDH18A1]] | 0.699 | aldehyde dehydrogenase 18 family member A1 |
| [[EFCAB14]] | 0.697 | EF-hand calcium binding domain 14 |
| [[SSR3]] | 0.695 | signal sequence receptor subunit 3 |
| [[TMED10]] | 0.692 | transmembrane p24 trafficking protein 10 |
| [[CANX]] | 0.687 | calnexin |
| [[STRAP]] | 0.686 | serine/threonine kinase receptor associated protein |
| [[GLG1]] | 0.686 | golgi glycoprotein 1 |
| [[MSTO2P]] | 0.684 | misato family member 2, pseudogene |
| [[DAP]] | 0.674 | death associated protein |
| [[SEPTIN7P14]] | 0.674 | septin 7 pseudogene 14 |
| [[TMEM167A]] | 0.673 | transmembrane protein 167A |
| [[TMEM214]] | 0.671 | transmembrane protein 214 |
| [[PPIB]] | 0.666 | peptidylprolyl isomerase B |
| [[RPN2]] | 0.661 | ribophorin II |
| [[ERP44]] | 0.657 | endoplasmic reticulum protein 44 |
| [[TIMM10B]] | 0.651 | translocase of inner mitochondrial membrane 10B |
| [[ATP6AP2]] | 0.647 | ATPase H+ transporting accessory protein 2 |
| [[OS9]] | 0.647 | OS9 endoplasmic reticulum lectin |
| [[AP2A1]] | 0.646 | adaptor related protein complex 2 subunit alpha 1 |
| [[GDI2]] | 0.637 | GDP dissociation inhibitor 2 |
| [[CRELD2]] | 0.621 | CRELD disulfide isomerase 2 |
| [[RECQL]] | 0.618 | RecQ like helicase |
| [[CA5B]] | 0.615 | carbonic anhydrase 5B |
| [[CHPF]] | 0.613 | chondroitin polymerizing factor |
| [[SND1]] | 0.611 | staphylococcal nuclease and tudor domain containing 1 |
| [[AMPD2]] | 0.606 | adenosine monophosphate deaminase 2 |
| [[PMPCA]] | 0.591 | peptidase, mitochondrial processing subunit alpha |
| [[TSPAN13]] | 0.589 | tetraspanin 13 |
| [[MAGT1]] | 0.577 | magnesium transporter 1 |
| [[MLF2]] | 0.570 | myeloid leukemia factor 2 |
| [[G3BP2]] | 0.564 | G3BP stress granule assembly factor 2 |
| [[NT5DC2]] | 0.551 | 5'-nucleotidase domain containing 2 |
| [[TMEM248]] | 0.547 | transmembrane protein 248 |
| [[TRAM1]] | 0.543 | translocation associated membrane protein 1 |
| [[OAT]] | 0.542 | ornithine aminotransferase |
| [[P3H3]] | 0.537 | prolyl 3-hydroxylase 3 |
| [[SAR1B]] | 0.536 | secretion associated Ras related GTPase 1B |
| [[TPP2]] | 0.533 | tripeptidyl peptidase 2 |
| [[TMED5]] | 0.525 | transmembrane p24 trafficking protein 5 |
| [[ODF2]] | 0.523 | outer dense fiber of sperm tails 2 |
| [[PRDX5]] | 0.513 | peroxiredoxin 5 |
| [[SEPTIN7P13]] | 0.501 | septin 7 pseudogene 13 |
| [[MCFD2]] | 0.497 | multiple coagulation factor deficiency 2, ER cargo receptor complex subunit |
| [[LDOC1]] | 0.491 | LDOC1 regulator of NFKB signaling |
| [[TRIM52]] | 0.462 | tripartite motif containing 52 |
| [[STAT5B]] | -0.456 | signal transducer and activator of transcription 5B |
| [[TMEM41B]] | 0.451 | transmembrane protein 41B |
| [[MTPN]] | 0.442 | myotrophin |
| [[MARK2]] | -0.442 | microtubule affinity regulating kinase 2 |
| [[USO1]] | 0.441 | USO1 vesicle transport factor |
| [[HMCES]] | 0.437 | 5-hydroxymethylcytosine binding, ES cell specific |
| [[ADAM17]] | 0.435 | ADAM metallopeptidase domain 17 |
| [[DDX43]] | -0.416 | DEAD-box helicase 43 |
| [[RMDN3]] | 0.391 | regulator of microtubule dynamics 3 |
| [[CKAP4]] | 0.389 | cytoskeleton associated protein 4 |
| [[SRP72]] | 0.388 | signal recognition particle 72 |
| [[DYNC1LI2]] | 0.386 | dynein cytoplasmic 1 light intermediate chain 2 |
| [[AFAP1-AS1]] | 0.365 | AFAP1 antisense RNA 1 |
| [[ATM]] | 0.333 | ATM serine/threonine kinase |
| [[YIPF6]] | 0.322 | Yip1 domain family member 6 |
| [[HSPA13]] | 0.305 | heat shock protein family A (Hsp70) member 13 |
| [[TM9SF1]] | 0.287 | transmembrane 9 superfamily member 1 |
| [[EDEM3]] | 0.251 | ER degradation enhancing alpha-mannosidase like protein 3 |
| [[COPZ1]] | 0.250 | coat protein complex I subunit zeta 1 |
| [[MORF4L1P1]] | 0.147 | mortality factor 4 like 1 pseudogene 1 |
| [[ARCN1]] | 0.138 | archain 1 coat protein complex I subunit delta |

## − arm (0)

None: a single-armed module.

## Data

- `graph/nodes.parquet` — module == 42; `graph/modules.parquet` — module == 42; `graph/edges.parquet` — both ends in the module; `graph/module_scores.npy` — [41] (drug-dose × line)
