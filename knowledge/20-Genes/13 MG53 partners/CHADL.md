---
symbol: CHADL
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [SLRR4B]
gene_name: chondroadherin like
locus: 22q13.2
locus_type: gene with protein product
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CHADL

*chondroadherin like* — 22q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CHADL.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | chondroadherin like |
| Also known as | SLRR4B |
| Locus | 22q13.2 — gene with protein product |
| Previously named | chondroadherin-like |

**Function**, from UniProt [Q6NUI6](https://www.uniprot.org/uniprotkb/Q6NUI6) (reviewed):

> Potential negative modulator of chondrocyte differentiation. Inhibits collagen fibrillogenesis in vitro. May influence chondrocyte's differentiation by acting on its cellular collagenous microenvironment

**Summary**, from NCBI Gene [150356](https://www.ncbi.nlm.nih.gov/gene/150356):

> Enables collagen binding activity and collagen fibril binding activity. Involved in negative regulation of collagen fibril organization. Is active in gel phase of interstitial matrix. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25165](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25165) · Entrez [150356](https://www.ncbi.nlm.nih.gov/gene/150356) · UniProt [Q6NUI6](https://www.uniprot.org/uniprotkb/Q6NUI6) · Ensembl [ENSG00000100399](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100399) · OMIM [616236](https://www.omim.org/entry/616236)

**PubMed**, as HGNC records for this gene — [25451920](https://pubmed.ncbi.nlm.nih.gov/25451920/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07182 |
| As a percentage | +5.10% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07371 / 0.07067 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.595 raw, 0.468 with 3 PCs removed |

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
