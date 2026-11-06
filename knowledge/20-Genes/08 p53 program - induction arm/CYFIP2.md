---
symbol: CYFIP2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [PIR121]
gene_name: cytoplasmic FMR1 interacting protein 2
locus: 5q33.3
locus_type: gene with protein product
gene_family: [SCAR/WAVE complex]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 21.11
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CYFIP2

*cytoplasmic FMR1 interacting protein 2* — 5q33.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CYFIP2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | cytoplasmic FMR1 interacting protein 2 |
| Also known as | PIR121, p53 inducible protein |
| Locus | 5q33.3 — gene with protein product |
| Gene families | SCAR/WAVE complex |

**Function**, from UniProt [Q96F07](https://www.uniprot.org/uniprotkb/Q96F07) (reviewed):

> Involved in T-cell adhesion and p53/TP53-dependent induction of apoptosis. Does not bind RNA. As component of the WAVE1 complex, required for BDNF-NTRK2 endocytic trafficking and signaling from early endosomes (By similarity)

**Summary**, from NCBI Gene [26999](https://www.ncbi.nlm.nih.gov/gene/26999):

> Predicted to enable small GTPase binding activity. Involved in several processes, including cell-cell adhesion; positive regulation of proteolysis; and regulation of postsynapse assembly. Located in cytosol; perinuclear region of cytoplasm; and synapse. Part of SCAR complex. Implicated in developmental and epileptic encephalopathy 65. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13760) · Entrez [26999](https://www.ncbi.nlm.nih.gov/gene/26999) · UniProt [Q96F07](https://www.uniprot.org/uniprotkb/Q96F07) · Ensembl [ENSG00000055163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055163) · OMIM [606323](https://www.omim.org/entry/606323)

**PubMed**, as HGNC records for this gene — [11438699](https://pubmed.ncbi.nlm.nih.gov/11438699/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 21.11 CPM |
| Lines where detected | 41 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 20 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.114× |
| Wild-type minus altered | 1.177× |
| Compounds moving it up in WT lines | 75 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00190 |
| As a percentage | +0.13% |
| FDR, exposure-shuffle null | 0.8015 |
| In TP53-wild-type lines / altered lines | -0.00589 / 0.00841 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.225 raw, -0.246 with 3 PCs removed |

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
