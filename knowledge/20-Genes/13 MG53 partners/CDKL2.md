---
symbol: CDKL2
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [P56, KKIAMRE]
gene_name: cyclin dependent kinase like 2
locus: 4q21.1
locus_type: gene with protein product
gene_family: [Cyclin dependent kinase like family]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CDKL2

*cyclin dependent kinase like 2* — 4q21.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CDKL2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | cyclin dependent kinase like 2 |
| Also known as | P56, KKIAMRE |
| Locus | 4q21.1 — gene with protein product |
| Gene families | Cyclin dependent kinase like family |
| Previously named | cyclin-dependent kinase-like 2 (CDC2-related kinase) |

UniProt [Q92772](https://www.uniprot.org/uniprotkb/Q92772) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [8999](https://www.ncbi.nlm.nih.gov/gene/8999):

> This gene product is a member of a large family of CDC2-related serine/threonine protein kinases. It accumulates primarily in the cytoplasm, with lower levels in the nucleus. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:1782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1782) · Entrez [8999](https://www.ncbi.nlm.nih.gov/gene/8999) · UniProt [Q92772](https://www.uniprot.org/uniprotkb/Q92772) · Ensembl [ENSG00000138769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138769) · OMIM [603442](https://www.omim.org/entry/603442)

**PubMed**, as HGNC records for this gene — [9000130](https://pubmed.ncbi.nlm.nih.gov/9000130/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07195 |
| As a percentage | +5.11% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08945 / 0.06222 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.532 raw, 0.414 with 3 PCs removed |

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
