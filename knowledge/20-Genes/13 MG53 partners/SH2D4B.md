---
symbol: SH2D4B
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: SH2 domain containing 4B
locus: 10q23.1
locus_type: gene with protein product
gene_family: [SH2 domain containing]
family_siblings_here: [STAT3, STAT4]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SH2D4B

*SH2 domain containing 4B* — 10q23.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SH2D4B.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | SH2 domain containing 4B |
| Also known as | — (no recorded alias) |
| Locus | 10q23.1 — gene with protein product |
| Gene families | SH2 domain containing |
| Other genes here in those families | [[STAT3]], [[STAT4]] |

UniProt [Q5SQS7](https://www.uniprot.org/uniprotkb/Q5SQS7) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [387694](https://www.ncbi.nlm.nih.gov/gene/387694):

> Predicted to enable protein-macromolecule adaptor activity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:31440](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31440) · Entrez [387694](https://www.ncbi.nlm.nih.gov/gene/387694) · UniProt [Q5SQS7](https://www.uniprot.org/uniprotkb/Q5SQS7) · Ensembl [ENSG00000178217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178217)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06929 |
| As a percentage | +4.92% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06091 / 0.07470 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.574 raw, 0.436 with 3 PCs removed |

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
