---
symbol: DCTN5
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MGC3248, p25]
gene_name: dynactin subunit 5
locus: 16p12.2
locus_type: gene with protein product
gene_family: [Dynactin subunits]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 44.5
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DCTN5

*dynactin subunit 5* — 16p12.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DCTN5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | dynactin subunit 5 |
| Also known as | MGC3248, p25 |
| Locus | 16p12.2 — gene with protein product |
| Gene families | Dynactin subunits |
| Previously named | dynactin 5 (p25) |

**Function**, from UniProt [Q9BTE1](https://www.uniprot.org/uniprotkb/Q9BTE1) (reviewed):

> Part of the dynactin complex that activates the molecular motor dynein for ultra-processive transport along microtubules

**Summary**, from NCBI Gene [84516](https://www.ncbi.nlm.nih.gov/gene/84516):

> This gene encodes a subunit of dynactin, a component of the cytoplasmic dynein motor machinery involved in minus-end-directed transport. The encoded protein is a component of the pointed-end subcomplex and is thought to bind membranous cargo. A pseudogene of this gene is located on the long arm of chromosome 1. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Jan 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24594) · Entrez [84516](https://www.ncbi.nlm.nih.gov/gene/84516) · UniProt [Q9BTE1](https://www.uniprot.org/uniprotkb/Q9BTE1) · Ensembl [ENSG00000166847](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166847) · OMIM [612962](https://www.omim.org/entry/612962)

**PubMed**, as HGNC records for this gene — [10525537](https://pubmed.ncbi.nlm.nih.gov/10525537/), [15043994](https://pubmed.ncbi.nlm.nih.gov/15043994/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 44.50 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 145 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.049× |
| Wild-type minus altered | 1.025× |
| Compounds moving it up in WT lines | 72 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00192 |
| As a percentage | +0.13% |
| FDR, exposure-shuffle null | 0.4795 |
| In TP53-wild-type lines / altered lines | 0.00303 / 0.00124 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.269 raw, 0.037 with 3 PCs removed |

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
