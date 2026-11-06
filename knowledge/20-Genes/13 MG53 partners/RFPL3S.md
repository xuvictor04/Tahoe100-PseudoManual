---
symbol: RFPL3S
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [RFPL3-AS, NCRNA00005]
gene_name: RFPL3 antisense
locus: 22q12.3
locus_type: RNA, long non-coding
gene_family: [Long non-coding RNAs with non-systematic symbols]
family_siblings_here: [ENSG00000251095, LMO7DN, PINCR, PURPL, PVT1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# RFPL3S

*RFPL3 antisense* — 22q12.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RFPL3S.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | RFPL3 antisense |
| Also known as | RFPL3-AS, NCRNA00005, non-protein coding RNA 5 |
| Locus | 22q12.3 — RNA, long non-coding |
| Gene families | Long non-coding RNAs with non-systematic symbols |
| Other genes here in those families | [[ENSG00000251095]], [[LMO7DN]], [[PINCR]], [[PURPL]], [[PVT1]] |
| Previously named | RFPL3 antisense RNA 1 |

UniProt [P0C7P2](https://www.uniprot.org/uniprotkb/P0C7P2) carries no FUNCTION annotation.

NCBI Gene carries no summary paragraph for this locus, which is usual for a non-coding RNA.

**Accessions** — [HGNC:9981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9981) · Entrez [10737](https://www.ncbi.nlm.nih.gov/gene/10737) · UniProt [P0C7P2](https://www.uniprot.org/uniprotkb/P0C7P2) · Ensembl [ENSG00000205853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205853) · OMIM [605971](https://www.omim.org/entry/605971)

**PubMed**, as HGNC records for this gene — [10508838](https://pubmed.ncbi.nlm.nih.gov/10508838/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06311 |
| As a percentage | +4.47% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.05434 / 0.06865 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.660 raw, 0.474 with 3 PCs removed |

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
