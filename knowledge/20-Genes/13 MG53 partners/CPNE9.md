---
symbol: CPNE9
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [KIAA4217]
gene_name: copine family member 9
locus: 3p25.3
locus_type: gene with protein product
gene_family: [Copines]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CPNE9

*copine family member 9* — 3p25.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CPNE9.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | copine family member 9 |
| Also known as | KIAA4217 |
| Locus | 3p25.3 — gene with protein product |
| Gene families | Copines |
| Previously named | copine family member IX |

**Function**, from UniProt [Q8IYJ1](https://www.uniprot.org/uniprotkb/Q8IYJ1) (reviewed):

> Probable calcium-dependent phospholipid-binding protein that may play a role in calcium-mediated intracellular processes (By similarity). Plays a role in dendrite formation by melanocytes (PubMed:23999003)

**Summary**, from NCBI Gene [151835](https://www.ncbi.nlm.nih.gov/gene/151835):

> Predicted to enable calcium-dependent phospholipid binding activity. Involved in positive regulation of dendrite extension. Located in extracellular exosome and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24336](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24336) · Entrez [151835](https://www.ncbi.nlm.nih.gov/gene/151835) · UniProt [Q8IYJ1](https://www.uniprot.org/uniprotkb/Q8IYJ1) · Ensembl [ENSG00000144550](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144550)

**PubMed**, as HGNC records for this gene — [9430674](https://pubmed.ncbi.nlm.nih.gov/9430674/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06826 |
| As a percentage | +4.84% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06636 / 0.06941 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.717 raw, 0.508 with 3 PCs removed |

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
