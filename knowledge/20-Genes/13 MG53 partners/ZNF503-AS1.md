---
symbol: ZNF503-AS1
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [uc.286]
gene_name: ZNF503 antisense RNA 1
locus: 10q22.2
locus_type: RNA, long non-coding
gene_family: [Antisense RNAs]
family_siblings_here: [ENSG00000225420, ENSG00000258851, ENSG00000285190, EPHA1-AS1, KCNMB2-AS1, PITRM1-AS1, PYCARD-AS1, TRAF3IP2-AS1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# ZNF503-AS1

*ZNF503 antisense RNA 1* — 10q22.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ZNF503-AS1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ZNF503 antisense RNA 1 |
| Also known as | uc.286 |
| Locus | 10q22.2 — RNA, long non-coding |
| Gene families | Antisense RNAs |
| Other genes here in those families | [[ENSG00000225420]], [[ENSG00000258851]], [[ENSG00000285190]], [[EPHA1-AS1]], [[KCNMB2-AS1]], [[PITRM1-AS1]], [[PYCARD-AS1]], [[TRAF3IP2-AS1]] |
| Previously named | ZNF503 antisense RNA 1 (non-protein coding) |

NCBI Gene carries no summary paragraph for this locus, which is usual for a non-coding RNA.

**Accessions** — [HGNC:27370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27370) · Entrez [253264](https://www.ncbi.nlm.nih.gov/gene/253264) · Ensembl [ENSG00000226051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226051)

**PubMed**, as HGNC records for this gene — [41309966](https://pubmed.ncbi.nlm.nih.gov/41309966/), [28880276](https://pubmed.ncbi.nlm.nih.gov/28880276/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06347 |
| As a percentage | +4.50% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07702 / 0.05524 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.533 raw, 0.374 with 3 PCs removed |

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
