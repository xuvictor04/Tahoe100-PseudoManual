---
symbol: SYT16
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [yt14r, CHR14SYT, Strep14]
gene_name: synaptotagmin 16
locus: 14q23.2
locus_type: gene with protein product
gene_family: [Synaptotagmins]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SYT16

*synaptotagmin 16* — 14q23.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SYT16.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | synaptotagmin 16 |
| Also known as | yt14r, CHR14SYT, Strep14, synaptotagmin XIV-related, chr14 synaptotagmin |
| Locus | 14q23.2 — gene with protein product |
| Gene families | Synaptotagmins |
| Previously named | synaptotagmin XIV-like; synaptotagmin XVI |

**Function**, from UniProt [Q17RD7](https://www.uniprot.org/uniprotkb/Q17RD7) (reviewed):

> May be involved in the trafficking and exocytosis of secretory vesicles in non-neuronal tissues. Is Ca(2+)-independent

**Summary**, from NCBI Gene [83851](https://www.ncbi.nlm.nih.gov/gene/83851):

> Predicted to enable phospholipid binding activity. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:23142](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23142) · Entrez [83851](https://www.ncbi.nlm.nih.gov/gene/83851) · UniProt [Q17RD7](https://www.uniprot.org/uniprotkb/Q17RD7) · Ensembl [ENSG00000139973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139973) · OMIM [610950](https://www.omim.org/entry/610950)

**PubMed**, as HGNC records for this gene — [11543631](https://pubmed.ncbi.nlm.nih.gov/11543631/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08556 |
| As a percentage | +6.11% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08078 / 0.08846 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.680 raw, 0.411 with 3 PCs removed |

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
