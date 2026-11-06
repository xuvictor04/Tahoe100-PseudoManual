---
symbol: USP15
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0529, UNPH4]
gene_name: ubiquitin specific peptidase 15
locus: 12q14.1
locus_type: gene with protein product
gene_family: [Ubiquitin specific peptidases, MicroRNA protein coding host genes]
family_siblings_here: [AEN, ATF5, BBC3, DNAJC5, DNMT3A, EZH1, FBXW7, GDF15, MGRN1, NADSYN1, NOTCH1, NUP210L]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 235.54
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# USP15

*ubiquitin specific peptidase 15* — 12q14.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/USP15.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ubiquitin specific peptidase 15 |
| Also known as | KIAA0529, UNPH4 |
| Locus | 12q14.1 — gene with protein product |
| Gene families | Ubiquitin specific peptidases; MicroRNA protein coding host genes |
| Other genes here in those families | [[AEN]], [[ATF5]], [[BBC3]], [[DNAJC5]], [[DNMT3A]], [[EZH1]], [[FBXW7]], [[GDF15]], [[MGRN1]], [[NADSYN1]], [[NOTCH1]], [[NUP210L]], [[PER1]], [[PLCL2]] |
| Previously named | ubiquitin specific protease 15 |

**Function**, from UniProt [Q9Y4E8](https://www.uniprot.org/uniprotkb/Q9Y4E8) (reviewed):

> Hydrolase that removes conjugated ubiquitin from target proteins and regulates various pathways such as the TGF-beta receptor signaling, NF-kappa-B and RNF41/NRDP1-PRKN pathways (PubMed:16005295, PubMed:17318178, PubMed:19576224, PubMed:19826004, PubMed:21947082, PubMed:22344298, PubMed:24852371). Acts as a key regulator of TGF-beta receptor signaling pathway, but the precise mechanism is still unclear: according to a report, acts by promoting deubiquitination of monoubiquitinated R-SMADs (SMAD1, SMAD2 and/or SMAD3), thereby alleviating inhibition of R-SMADs and promoting activation of TGF-beta target genes (PubMed:21947082). According to another reports, regulates the TGF-beta receptor signaling pathway by mediating deubiquitination and stabilization of TGFBR1, leading to an enhanced TGF-beta signal (PubMed:22344298). Able to mediate deubiquitination of monoubiquitinated substrates, 'Lys-27'-, 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains (PubMed:33093067). May also regulate gene expression and/or DNA repair through the deubiquitination of histone H2B (PubMed:24526689). Acts as an inhibitor of mitophagy by counteracting the action of parkin (PRKN): hydrolyzes cleavage of 'Lys-48'- and 'Lys-63'-linked polyubiquitin chains attached by parkin on target proteins such as MFN2, thereby reducing parkin's ability to drive mitophagy (PubMed:24852371). Acts as an associated component of COP9 signalosome complex (CSN) and regulates different pathways via this association: regulates NF-kappa-B by mediating deubiquitination of NFKBIA and deubiquitinates substrates bound to VCP (PubMed:16005295, PubMed:17318178, PubMed:19576224, PubMed:19826004). Involved in endosome organization by mediating deubiquitination of SQSTM1: ubiquitinated SQSTM1 forms a molecular bridge that restrains cognate vesicles in the perinuclear region and its deubiquitination releases target vesicles for fast transport into the cell periphery (PubMed:27368102). Acts as a negative regulator of antifungal immunity by mediating 'Lys-27'-linked deubiquitination of CARD9, thereby inactivating CARD9 (PubMed:33093067)

**Summary**, from NCBI Gene [9958](https://www.ncbi.nlm.nih.gov/gene/9958):

> This gene encodes a member of the ubiquitin specific protease (USP) family of deubiquitinating enzymes. USP enzymes play critical roles in ubiquitin-dependent processes through polyubiquitin chain disassembly and hydrolysis of ubiquitin-substrate bonds. The encoded protein associates with the COP9 signalosome, and also plays a role in transforming growth factor beta signalling through deubiquitination of receptor-activated SMAD transcription factors. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 2. [provided by RefSeq, Nov 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:12613](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12613) · Entrez [9958](https://www.ncbi.nlm.nih.gov/gene/9958) · UniProt [Q9Y4E8](https://www.uniprot.org/uniprotkb/Q9Y4E8) · Ensembl [ENSG00000135655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135655) · OMIM [604731](https://www.omim.org/entry/604731)

**PubMed**, as HGNC records for this gene — [12838346](https://pubmed.ncbi.nlm.nih.gov/12838346/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 235.54 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 77 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.082× |
| Wild-type minus altered | 1.032× |
| Compounds moving it up in WT lines | 81 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00093 |
| As a percentage | -0.06% |
| FDR, exposure-shuffle null | 0.6282 |
| In TP53-wild-type lines / altered lines | 0.00102 / -0.00211 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.216 raw, -0.004 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
