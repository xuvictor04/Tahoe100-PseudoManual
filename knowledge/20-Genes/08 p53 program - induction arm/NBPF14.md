---
symbol: NBPF14
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DJ328E19.C1.1]
gene_name: NBPF member 14
locus: 1q21.2
locus_type: gene with protein product
gene_family: [NBPF members]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 25.56
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# NBPF14

*NBPF member 14* — 1q21.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NBPF14.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | NBPF member 14 |
| Also known as | DJ328E19.C1.1 |
| Locus | 1q21.2 — gene with protein product |
| Gene families | NBPF members |
| Previously named | neuroblastoma breakpoint family, member 14 |

UniProt [Q5TI25](https://www.uniprot.org/uniprotkb/Q5TI25) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [25832](https://www.ncbi.nlm.nih.gov/gene/25832):

> This gene is a member of the neuroblastoma breakpoint family (NBPF) which consists of dozens of recently duplicated genes primarily located in segmental duplications on human chromosome 1. This gene family has experienced its greatest expansion within the human lineage and has expanded, to a lesser extent, among primates in general. Members of this gene family are characterized by tandemly repeated copies of DUF1220 protein domains. Gene copy number variations in the human chromosomal region 1q21.1, where most DUF1220 domains are located, have been implicated in a number of developmental and neurogenetic diseases such as microcephaly, macrocephaly, autism, schizophrenia, cognitive disability, congenital heart disease, neuroblastoma, and congenital kidney and urinary tract anomalies. Altered expression of some gene family members is associated with several types of cancer. This gene family contains numerous pseudogenes. [provided by RefSeq, May 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25232](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25232) · Entrez [25832](https://www.ncbi.nlm.nih.gov/gene/25832) · UniProt [Q5TI25](https://www.uniprot.org/uniprotkb/Q5TI25) · Ensembl [ENSG00000270629](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000270629) · OMIM [614003](https://www.omim.org/entry/614003)

**PubMed**, as HGNC records for this gene — [8619474](https://pubmed.ncbi.nlm.nih.gov/8619474/), [9110174](https://pubmed.ncbi.nlm.nih.gov/9110174/), [16079250](https://pubmed.ncbi.nlm.nih.gov/16079250/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 25.56 CPM |
| Lines where detected | 48 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 155 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.034× |
| Wild-type minus altered | 1.026× |
| Compounds moving it up in WT lines | 61 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00057 |
| As a percentage | +0.04% |
| FDR, exposure-shuffle null | 0.8747 |
| In TP53-wild-type lines / altered lines | 0.00395 / -0.00138 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.163 raw, 0.088 with 3 PCs removed |

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
