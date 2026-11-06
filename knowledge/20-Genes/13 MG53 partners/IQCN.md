---
symbol: IQCN
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: IQ motif containing N
locus: 19p13.11
locus_type: gene with protein product
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# IQCN

*IQ motif containing N* — 19p13.11

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/IQCN.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | IQ motif containing N |
| Also known as | — (no recorded alias) |
| Locus | 19p13.11 — gene with protein product |
| Previously named | KIAA1683 |

**Function**, from UniProt [Q9H0B3](https://www.uniprot.org/uniprotkb/Q9H0B3) (reviewed):

> Essential for spermiogenesis and fertilization (PubMed:36321563). May be required for manchette assembly in elongating spermatids (By similarity)

**Summary**, from NCBI Gene [80726](https://www.ncbi.nlm.nih.gov/gene/80726):

> Involved in spermatid development. Located in mitochondrion. Implicated in spermatogenic failure 78. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29350) · Entrez [80726](https://www.ncbi.nlm.nih.gov/gene/80726) · UniProt [Q9H0B3](https://www.uniprot.org/uniprotkb/Q9H0B3) · Ensembl [ENSG00000130518](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130518) · OMIM [620160](https://www.omim.org/entry/620160)

**PubMed**, as HGNC records for this gene — [11214970](https://pubmed.ncbi.nlm.nih.gov/11214970/), [11230166](https://pubmed.ncbi.nlm.nih.gov/11230166/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07935 |
| As a percentage | +5.65% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09178 / 0.07305 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.555 raw, 0.523 with 3 PCs removed |

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
