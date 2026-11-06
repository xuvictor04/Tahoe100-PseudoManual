---
symbol: GARIN1B
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [NYD-SP18, GARI-L1]
gene_name: golgi associated RAB2 interactor 1B
locus: 7q32.1
locus_type: gene with protein product
gene_family: [Golgi associated RAB2 interactor family]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# GARIN1B

*golgi associated RAB2 interactor 1B* — 7q32.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/GARIN1B.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | golgi associated RAB2 interactor 1B |
| Also known as | NYD-SP18, GARI-L1, Golgi-associated RAB2B interactor like 1 |
| Locus | 7q32.1 — gene with protein product |
| Gene families | Golgi associated RAB2 interactor family |
| Previously named | family with sequence similarity 137, member A; family with sequence similarity 71 member F1 |

**Function**, from UniProt [Q96KD3](https://www.uniprot.org/uniprotkb/Q96KD3) (reviewed):

> RAB2B effector protein required for accurate acrosome formation and normal male fertility. In complex with RAB2A/RAB2B, seems to suppress excessive vesicle trafficking during acrosome formation

**Summary**, from NCBI Gene [84691](https://www.ncbi.nlm.nih.gov/gene/84691):

> Predicted to be involved in acrosome assembly and acrosome reaction. Predicted to be located in Golgi apparatus. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30704) · Entrez [84691](https://www.ncbi.nlm.nih.gov/gene/84691) · UniProt [Q96KD3](https://www.uniprot.org/uniprotkb/Q96KD3) · Ensembl [ENSG00000135248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135248) · OMIM [619905](https://www.omim.org/entry/619905)

**PubMed**, as HGNC records for this gene — [34714330](https://pubmed.ncbi.nlm.nih.gov/34714330/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08772 |
| As a percentage | +6.27% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08413 / 0.09000 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.620 raw, 0.501 with 3 PCs removed |

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
