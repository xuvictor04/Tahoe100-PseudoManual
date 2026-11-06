---
symbol: DDB2
type: gene
tier: 1
pathway_role: p53 effector: DNA repair
aliases: [XPE]
gene_name: damage specific DNA binding protein 2
locus: 11p11.2
locus_type: gene with protein product
gene_family: [WD repeat domain containing, Xeroderma pigmentosum complementation groups, Nucleotide excision repair]
family_siblings_here: [COP1, DNAI3, FBXW7, LIG1, POLH, RIC1, TLE4, WDR48, XPC]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
curated_effector: true
effector_role: DNA repair
median_line_cpm: 54.26
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [curated-effector, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DDB2

*damage specific DNA binding protein 2* — 11p11.2

> [!summary] In one line
> DDB2 is the damage-recognition subunit of the UV-DDB complex and the substrate receptor of a CRL4 ubiquitin ligase, it is a direct p53 target, and it is the gene mutated in xeroderma pigmentosum group E.

## What it is

DDB2 (p48) is the small subunit of UV-DDB, the heterodimer it forms with DDB1 (p127). UV-DDB binds UV photoproducts — cyclobutane pyrimidine dimers and 6-4 photoproducts — and also abasic sites and short mismatches, with the highest affinity of any known damage sensor for the poorly helix-distorting CPD lesion. Crystallography showed how: DDB2's WD40 β-propeller holds the duplex and the damaged bases are flipped out of the helix into a hydrophobic pocket on the propeller face, which is why a lesion that barely deforms DNA can still be read. UV-DDB then hands the lesion to XPC–RAD23B to initiate global-genome nucleotide excision repair.

DDB2 has a second, inseparable job. DDB1 is the adaptor of CUL4A/CUL4B–RBX1, and DDB2 is the substrate receptor of the resulting CRL4^DDB2 ligase, which ubiquitylates XPC, core histones H2A/H3/H4 at the lesion, and DDB2 itself. The histone marks loosen nucleosomes around the damage; the autoubiquitylation drives DDB2's own proteasomal turnover and so times the handoff and terminates the response. CRL4^DDB2 activity is further gated by the COP9 signalosome after damage.

The p53 connection is at the level of expression rather than activity: DDB2 mRNA depends on basal p53 and rises further after damage in a p53-dependent way. This is the accepted explanation for a long-standing species difference — rodent cells lack appreciable UV-DDB activity and repair CPDs poorly in non-transcribed DNA, because they do not express DDB2 the way human cells do. Clinically, biallelic DDB2 loss causes xeroderma pigmentosum group E: the mildest XP complementation group, with late-onset skin cancer and without the neurological degeneration of other groups. Beyond repair, DDB2 has reported roles in oncogene-induced senescence, in CRL4-dependent transcriptional repression, and in ROS control, all on narrower evidence.

## Why it appears in this work

DDB2 is the member of [[p53 program P]] that reports p53 output reaching the repair machinery rather than the arrest arm through [[The p21-DREAM axis]] or the apoptotic effectors. It is a direct target with a wild-type-selective induction, so it serves both as a reporter and as evidence that [[The p53 pathway]] is being engaged as a damage response and not only as a growth-suppressive program.

## What is uncertain

The direct-target status is secure, but what induction means functionally at 24 h is not. DDB2 protein is autoubiquitylated and short-lived at damage sites, so more mRNA does not straightforwardly mean more active UV-DDB; the limiting quantity may be CRL4 assembly or chromatin access rather than transcript abundance. The lesions DDB2 reads best are UV photoproducts, which are not what most compounds in this panel produce, so DDB2 induction here should be read as a p53 signature and not as evidence of relevant repair capacity. DDB2 also responds to inputs other than p53, and in lines with high basal replication stress its baseline may be set by those. The CRL4^DDB2-as-repressor and ROS results come from fewer systems than the repair biochemistry and should carry less weight.

## References

- Hwang et al., 1999, PNAS — showed DDB2/p48 expression depends on basal p53 and is further induced after DNA damage p53-dependently, accounting for the human/rodent difference in UV-DDB activity.
- Scrima et al., 2008, Cell — structural basis of UV DNA-damage recognition by the DDB1–DDB2 complex, with the lesion flipped into a pocket on the DDB2 β-propeller.
- Groisman et al., 2003, Cell — showed the ubiquitin ligase activity of the DDB2 and CSA complexes is differentially regulated by the COP9 signalosome in response to DNA damage.
- Sugasawa et al., 2005, Cell — UV-induced ubiquitylation of XPC mediated by the UV-DDB–ubiquitin ligase complex.
- Rapić-Otrin et al., 2003, Human Molecular Genetics — established that true xeroderma pigmentosum group E patients have a defective DDB2 component of the UV-DDB complex.

## What is on record

| | |
|---|---|
| Official name | damage specific DNA binding protein 2 |
| Also known as | DDBB, UV-DDB2, FLJ34321, XPE, xeroderma pigmentosum group E protein, UV-damaged DNA-binding protein 2, DDB p48 subunit |
| Locus | 11p11.2 — gene with protein product |
| Gene families | WD repeat domain containing; Xeroderma pigmentosum complementation groups; Nucleotide excision repair |
| Other genes here in those families | [[COP1]], [[DNAI3]], [[FBXW7]], [[LIG1]], [[POLH]], [[RIC1]], [[TLE4]], [[WDR48]], [[XPC]] |
| Previously named | damage-specific DNA binding protein 2 (48kD) |

**Function**, from UniProt [Q92466](https://www.uniprot.org/uniprotkb/Q92466) (reviewed):

> Protein, which is both involved in DNA repair and protein ubiquitination, as part of the UV-DDB complex and DCX (DDB1-CUL4-X-box) complexes, respectively (PubMed:10882109, PubMed:11278856, PubMed:11705987, PubMed:12732143, PubMed:15882621, PubMed:16473935, PubMed:18593899, PubMed:32789493, PubMed:9892649). Core component of the UV-DDB complex (UV-damaged DNA-binding protein complex), a complex that recognizes UV-induced DNA damage and recruit proteins of the nucleotide excision repair pathway (the NER pathway) to initiate DNA repair (PubMed:10882109, PubMed:11278856, PubMed:11705987, PubMed:12944386, PubMed:14751237, PubMed:16260596, PubMed:32789493). The UV-DDB complex preferentially binds to cyclobutane pyrimidine dimers (CPD), 6-4 photoproducts (6-4 PP), apurinic sites and short mismatches (PubMed:10882109, PubMed:11278856, PubMed:11705987, PubMed:12944386, PubMed:16260596). Also functions as the substrate recognition module for the DCX (DDB2-CUL4-X-box) E3 ubiquitin-protein ligase complex DDB2-CUL4-ROC1 (also known as CUL4-DDB-ROC1 and CUL4-DDB-RBX1) (PubMed:12732143, PubMed:15882621, PubMed:16473935, PubMed:18593899, PubMed:26572825). The DDB2-CUL4-ROC1 complex may ubiquitinate histone H2A, histone H3 and histone H4 at sites of UV-induced DNA damage (PubMed:16473935, PubMed:16678110). The ubiquitination of histones may facilitate their removal from the nucleosome and promote subsequent DNA repair (PubMed:16473935, PubMed:16678110). The DDB2-CUL4-ROC1 complex also ubiquitinates XPC, which may enhance DNA-binding by XPC and promote NER (PubMed:15882621). The DDB2-CUL4-ROC1 complex also ubiquitinates KAT7/HBO1 in response to DNA damage, leading to its degradation: recognizes KAT7/HBO1 following phosphorylation by ATR (PubMed:26572825)

**Summary**, from NCBI Gene [1643](https://www.ncbi.nlm.nih.gov/gene/1643):

> This gene encodes a protein that is necessary for the repair of ultraviolet light-damaged DNA. This protein is the smaller subunit of a heterodimeric protein complex that participates in nucleotide excision repair, and this complex mediates the ubiquitylation of histones H3 and H4, which facilitates the cellular response to DNA damage. This subunit appears to be required for DNA binding. Mutations in this gene cause xeroderma pigmentosum complementation group E, a recessive disease that is characterized by an increased sensitivity to UV light and a high predisposition for skin cancer development, in some cases accompanied by neurological abnormalities. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2718) · Entrez [1643](https://www.ncbi.nlm.nih.gov/gene/1643) · UniProt [Q92466](https://www.uniprot.org/uniprotkb/Q92466) · Ensembl [ENSG00000134574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134574) · OMIM [600811](https://www.omim.org/entry/600811)

**PubMed**, as HGNC records for this gene — [8407967](https://pubmed.ncbi.nlm.nih.gov/8407967/), [8530102](https://pubmed.ncbi.nlm.nih.gov/8530102/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 54.26 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 10 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.139× |
| Wild-type minus altered | 1.154× |
| Compounds moving it up in WT lines | 81 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00752 |
| As a percentage | -0.52% |
| FDR, exposure-shuffle null | 0.0405 |
| In TP53-wild-type lines / altered lines | -0.00377 / -0.00980 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.173 raw, 0.028 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** curated p53 effector; p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
