---
symbol: CDS2
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: CDP-diacylglycerol synthase 2
locus: 20p12.3
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 52.61
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CDS2

*CDP-diacylglycerol synthase 2* — 20p12.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CDS2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | CDP-diacylglycerol synthase 2 |
| Also known as | phosphatidate cytidylyltransferase 2, cytidine diphosphate diacylglycerol synthase 2 |
| Locus | 20p12.3 — gene with protein product |

**Function**, from UniProt [O95674](https://www.uniprot.org/uniprotkb/O95674) (reviewed):

> Catalyzes the conversion of phosphatidic acid (PA) to CDP-diacylglycerol (CDP-DAG), an essential intermediate in the synthesis of phosphatidylglycerol, cardiolipin and phosphatidylinositol (PubMed:25375833). Exhibits specificity for the nature of the acyl chains at the sn-1 and sn-2 positions in the substrate, PA and the preferred acyl chain composition is 1-stearoyl-2-arachidonoyl-sn-phosphatidic acid (PubMed:25375833). Plays an important role in regulating the growth and maturation of lipid droplets which are storage organelles at the center of lipid and energy homeostasis (PubMed:26946540, PubMed:31548309)

**Summary**, from NCBI Gene [8760](https://www.ncbi.nlm.nih.gov/gene/8760):

> Breakdown products of phosphoinositides are ubiquitous second messengers that function downstream of many G protein-coupled receptors and tyrosine kinases regulating cell growth, calcium metabolism, and protein kinase C activity. This gene encodes an enzyme which regulates the amount of phosphatidylinositol available for signaling by catalyzing the conversion of phosphatidic acid to CDP-diacylglycerol. This enzyme is an integral membrane protein localized to two subcellular domains, the matrix side of the inner mitochondrial membrane where it is thought to be involved in the synthesis of phosphatidylglycerol and cardiolipin and the cytoplasmic side of the endoplasmic reticulum where it functions in phosphatidylinositol biosynthesis. Two genes encoding this enzyme have been identified in humans, one mapping to human chromosome 4q21 and a second to 20p13. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:1801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1801) · Entrez [8760](https://www.ncbi.nlm.nih.gov/gene/8760) · UniProt [O95674](https://www.uniprot.org/uniprotkb/O95674) · Ensembl [ENSG00000101290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101290) · OMIM [603549](https://www.omim.org/entry/603549)

**PubMed**, as HGNC records for this gene — [9806839](https://pubmed.ncbi.nlm.nih.gov/9806839/), [9889000](https://pubmed.ncbi.nlm.nih.gov/9889000/), [40615674](https://pubmed.ncbi.nlm.nih.gov/40615674/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 52.61 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 104 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.032× |
| Wild-type minus altered | 1.023× |
| Compounds moving it up in WT lines | 74 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00732 |
| As a percentage | -0.51% |
| FDR, exposure-shuffle null | 0.0062 |
| In TP53-wild-type lines / altered lines | -0.00371 / -0.00951 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.529 raw, -0.213 with 3 PCs removed |

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
