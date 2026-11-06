---
symbol: PPP1R36
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: protein phosphatase 1 regulatory subunit 36
locus: 14q23.3
locus_type: gene with protein product
gene_family: [Protein phosphatase 1 regulatory subunits]
family_siblings_here: [ELL]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PPP1R36

*protein phosphatase 1 regulatory subunit 36* — 14q23.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PPP1R36.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | protein phosphatase 1 regulatory subunit 36 |
| Also known as | — (no recorded alias) |
| Locus | 14q23.3 — gene with protein product |
| Gene families | Protein phosphatase 1 regulatory subunits |
| Other genes here in those families | [[ELL]] |
| Previously named | chromosome 14 open reading frame 50; protein phosphatase 1, regulatory subunit 36 |

**Function**, from UniProt [Q96LQ0](https://www.uniprot.org/uniprotkb/Q96LQ0) (reviewed):

> Inhibits phosphatase activity of protein phosphatase 1 (PP1) complexes

**Summary**, from NCBI Gene [145376](https://www.ncbi.nlm.nih.gov/gene/145376):

> Predicted to enable phosphatase binding activity and protein phosphatase inhibitor activity. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:20097](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20097) · Entrez [145376](https://www.ncbi.nlm.nih.gov/gene/145376) · UniProt [Q96LQ0](https://www.uniprot.org/uniprotkb/Q96LQ0) · Ensembl [ENSG00000165807](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165807) · OMIM [619923](https://www.omim.org/entry/619923)

**PubMed**, as HGNC records for this gene — [27098880](https://pubmed.ncbi.nlm.nih.gov/27098880/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08670 |
| As a percentage | +6.19% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08896 / 0.08533 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.679 raw, 0.515 with 3 PCs removed |

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
