---
symbol: ADORA1
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [RDC7]
gene_name: adenosine A1 receptor
locus: 1q32.1
locus_type: gene with protein product
gene_family: [Adenosine receptors]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# ADORA1

*adenosine A1 receptor* — 1q32.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ADORA1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | adenosine A1 receptor |
| Also known as | RDC7 |
| Locus | 1q32.1 — gene with protein product |
| Gene families | Adenosine receptors |

**Function**, from UniProt [P30542](https://www.uniprot.org/uniprotkb/P30542) (reviewed):

> Receptor for adenosine (PubMed:29925945). The activity of this receptor is mediated by G proteins such as GNAI2 which inhibit adenylyl cyclase

**Summary**, from NCBI Gene [134](https://www.ncbi.nlm.nih.gov/gene/134):

> The protein encoded by this gene is an adenosine receptor that belongs to the G-protein coupled receptor 1 family. There are 3 types of adenosine receptors, each with a specific pattern of ligand binding and tissue distribution, and together they regulate a diverse set of physiologic functions. The type A1 receptors inhibit adenylyl cyclase, and play a role in the fertilization process. Animal studies also suggest a role for A1 receptors in kidney function and ethanol intoxication. Transcript variants with alternative splicing in the 5' UTR have been found for this gene. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:262](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:262) · Entrez [134](https://www.ncbi.nlm.nih.gov/gene/134) · UniProt [P30542](https://www.uniprot.org/uniprotkb/P30542) · Ensembl [ENSG00000163485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163485) · OMIM [102775](https://www.omim.org/entry/102775)

**PubMed**, as HGNC records for this gene — [1662665](https://pubmed.ncbi.nlm.nih.gov/1662665/), [2541503](https://pubmed.ncbi.nlm.nih.gov/2541503/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06357 |
| As a percentage | +4.51% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.05677 / 0.06787 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.358 raw, 0.466 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
