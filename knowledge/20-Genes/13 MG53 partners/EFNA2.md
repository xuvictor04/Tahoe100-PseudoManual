---
symbol: EFNA2
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [ELF-1, LERK6]
gene_name: ephrin A2
locus: 19p13.3
locus_type: gene with protein product
gene_family: [Ephrins]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# EFNA2

*ephrin A2* — 19p13.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/EFNA2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ephrin A2 |
| Also known as | ELF-1, LERK6, EPH-related receptor tyrosine kinase ligand 6 |
| Locus | 19p13.3 — gene with protein product |
| Gene families | Ephrins |
| Previously named | ephrin-A2 |

**Function**, from UniProt [O43921](https://www.uniprot.org/uniprotkb/O43921) (reviewed):

> Cell surface GPI-bound ligand for Eph receptors, a family of receptor tyrosine kinases which are crucial for migration, repulsion and adhesion during neuronal, vascular and epithelial development. Binds promiscuously Eph receptors residing on adjacent cells, leading to contact-dependent bidirectional signaling into neighboring cells. The signaling pathway downstream of the receptor is referred to as forward signaling while the signaling pathway downstream of the ephrin ligand is referred to as reverse signaling. With the EPHA2 receptor may play a role in bone remodeling through regulation of osteoclastogenesis and osteoblastogenesis (By similarity)

**Summary**, from NCBI Gene [1943](https://www.ncbi.nlm.nih.gov/gene/1943):

> This gene encodes a member of the ephrin family. The protein is composed of a signal sequence, a receptor-binding region, a spacer region, and a hydrophobic region. The EPH and EPH-related receptors comprise the largest subfamily of receptor protein-tyrosine kinases and have been implicated in mediating developmental events, particularly in the nervous system. Based on their structures and sequence relationships, ephrins are divided into the ephrin-A (EFNA) class, which are anchored to the membrane by a glycosylphosphatidylinositol linkage, and the ephrin-B (EFNB) class, which are transmembrane proteins. Posttranslational modifications determine whether this protein localizes to the nucleus or the cytoplasm. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:3222](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3222) · Entrez [1943](https://www.ncbi.nlm.nih.gov/gene/1943) · UniProt [O43921](https://www.uniprot.org/uniprotkb/O43921) · Ensembl [ENSG00000099617](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099617) · OMIM [602756](https://www.omim.org/entry/602756)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07317 |
| As a percentage | +5.20% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06059 / 0.08054 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.565 raw, 0.334 with 3 PCs removed |

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
