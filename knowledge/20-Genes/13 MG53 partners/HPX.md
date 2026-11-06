---
symbol: HPX
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: hemopexin
locus: 11p15.4
locus_type: gene with protein product
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# HPX

*hemopexin* — 11p15.4

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HPX.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | hemopexin |
| Also known as | — (no recorded alias) |
| Locus | 11p15.4 — gene with protein product |

**Function**, from UniProt [P02790](https://www.uniprot.org/uniprotkb/P02790) (reviewed):

> Binds heme and transports it to the liver for breakdown and iron recovery, after which the free hemopexin returns to the circulation

**Summary**, from NCBI Gene [3263](https://www.ncbi.nlm.nih.gov/gene/3263):

> This gene encodes a plasma glycoprotein that binds heme with high affinity. The encoded protein is an acute phase protein that transports heme from the plasma to the liver and may be involved in protecting cells from oxidative stress. [provided by RefSeq, Apr 2009]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:5171](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5171) · Entrez [3263](https://www.ncbi.nlm.nih.gov/gene/3263) · UniProt [P02790](https://www.uniprot.org/uniprotkb/P02790) · Ensembl [ENSG00000110169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110169) · OMIM [142290](https://www.omim.org/entry/142290)

**PubMed**, as HGNC records for this gene — [2989777](https://pubmed.ncbi.nlm.nih.gov/2989777/), [2842511](https://pubmed.ncbi.nlm.nih.gov/2842511/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07192 |
| As a percentage | +5.11% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07654 / 0.06911 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.642 raw, 0.541 with 3 PCs removed |

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
