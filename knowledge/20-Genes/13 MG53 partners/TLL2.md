---
symbol: TLL2
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: tolloid like 2
locus: 10q24.1
locus_type: gene with protein product
gene_family: [Astacins]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# TLL2

*tolloid like 2* — 10q24.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TLL2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | tolloid like 2 |
| Also known as | — (no recorded alias) |
| Locus | 10q24.1 — gene with protein product |
| Gene families | Astacins |

**Function**, from UniProt [Q9Y6L7](https://www.uniprot.org/uniprotkb/Q9Y6L7) (reviewed):

> Protease which specifically processes pro-lysyl oxidase. Required for the embryonic development. Predominant protease, which in the development, influences dorsal-ventral patterning and skeletogenesis

**Summary**, from NCBI Gene [7093](https://www.ncbi.nlm.nih.gov/gene/7093):

> This gene encodes an astacin-like zinc-dependent metalloprotease and is a subfamily member of the metzincin family. Unlike other family members, a similar protein in mice does not cleave procollagen C-propeptides or chordin. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11844) · Entrez [7093](https://www.ncbi.nlm.nih.gov/gene/7093) · UniProt [Q9Y6L7](https://www.uniprot.org/uniprotkb/Q9Y6L7) · Ensembl [ENSG00000095587](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000095587) · OMIM [606743](https://www.omim.org/entry/606743)

**PubMed**, as HGNC records for this gene — [10516436](https://pubmed.ncbi.nlm.nih.gov/10516436/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07258 |
| As a percentage | +5.16% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07111 / 0.07347 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.603 raw, 0.459 with 3 PCs removed |

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
