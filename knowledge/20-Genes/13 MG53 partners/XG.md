---
symbol: XG
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: Xg glycoprotein (Xg blood group)
locus: Xp22.33
locus_type: gene with protein product
gene_family: [Blood group antigens, Pseudoautosomal region 1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# XG

*Xg glycoprotein (Xg blood group)* — Xp22.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/XG.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | Xg glycoprotein (Xg blood group) |
| Also known as | — (no recorded alias) |
| Locus | Xp22.33 — gene with protein product |
| Gene families | Blood group antigens; Pseudoautosomal region 1 |
| Previously named | Xg blood group (pseudoautosomal boundary-divided on the X chromosome); Xg blood group |

UniProt [P55808](https://www.uniprot.org/uniprotkb/P55808) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [7499](https://www.ncbi.nlm.nih.gov/gene/7499):

> This gene encodes the XG blood group antigen, and is located at the pseudoautosomal boundary on the short (p) arm of chromosome X. The three 5' exons reside in the pseudoautosomal region and the remaining exons within the X-specific end. A truncated copy of this gene is found on the Y chromosome at the pseudoautosomal boundary. It is transcribed, but not expected to make a Y-chromosome specific gene product. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:12806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12806) · Entrez [7499](https://www.ncbi.nlm.nih.gov/gene/7499) · UniProt [P55808](https://www.uniprot.org/uniprotkb/P55808) · Ensembl [ENSG00000124343](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124343) · OMIM [300879](https://www.omim.org/entry/300879)

**PubMed**, as HGNC records for this gene — [8054981](https://pubmed.ncbi.nlm.nih.gov/8054981/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08303 |
| As a percentage | +5.92% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07793 / 0.08612 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.573 raw, 0.499 with 3 PCs removed |

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
