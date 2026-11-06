---
symbol: SNX31
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [MGC39715]
gene_name: sorting nexin 31
locus: 8q22.3
locus_type: gene with protein product
gene_family: [Sorting nexins]
family_siblings_here: [SNX2]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SNX31

*sorting nexin 31* — 8q22.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SNX31.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | sorting nexin 31 |
| Also known as | MGC39715 |
| Locus | 8q22.3 — gene with protein product |
| Gene families | Sorting nexins |
| Other genes here in those families | [[SNX2]] |

**Function**, from UniProt [Q8N9S9](https://www.uniprot.org/uniprotkb/Q8N9S9) (reviewed):

> May be involved in protein trafficking

**Summary**, from NCBI Gene [169166](https://www.ncbi.nlm.nih.gov/gene/169166):

> Predicted to enable phosphatidylinositol binding activity. Predicted to be involved in endocytic recycling and intracellular protein transport. Predicted to be part of protein-containing complex. Predicted to be active in early endosome. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:28605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28605) · Entrez [169166](https://www.ncbi.nlm.nih.gov/gene/169166) · UniProt [Q8N9S9](https://www.uniprot.org/uniprotkb/Q8N9S9) · Ensembl [ENSG00000174226](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174226) · OMIM [619839](https://www.omim.org/entry/619839)

**PubMed**, as HGNC records for this gene — [16782399](https://pubmed.ncbi.nlm.nih.gov/16782399/), [24914955](https://pubmed.ncbi.nlm.nih.gov/24914955/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07983 |
| As a percentage | +5.69% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07728 / 0.08138 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.647 raw, 0.337 with 3 PCs removed |

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
