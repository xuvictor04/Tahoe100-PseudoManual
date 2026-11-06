---
symbol: CATSPERD
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [MGC39581]
gene_name: catsper channel auxiliary subunit delta
locus: 19p13.3
locus_type: gene with protein product
gene_family: [CatSpermasome complex]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# CATSPERD

*catsper channel auxiliary subunit delta* — 19p13.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CATSPERD.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | catsper channel auxiliary subunit delta |
| Also known as | MGC39581 |
| Locus | 19p13.3 — gene with protein product |
| Gene families | CatSpermasome complex |
| Previously named | cation channel sperm associated auxiliary subunit delta; transmembrane protein 146 |

**Function**, from UniProt [Q86XM0](https://www.uniprot.org/uniprotkb/Q86XM0) (reviewed):

> Auxiliary component of the CatSper complex, a complex involved in sperm cell hyperactivation. Sperm cell hyperactivation is needed for sperm motility which is essential late in the preparation of sperm for fertilization. Required for CATSPER1 stability before intraflagellar transport and/or incorporation of the CatSper complex channel into the flagellar membrane

**Summary**, from NCBI Gene [257062](https://www.ncbi.nlm.nih.gov/gene/257062):

> Predicted to be involved in flagellated sperm motility and sperm capacitation. Predicted to be located in plasma membrane. Predicted to be part of CatSper complex. Predicted to be active in sperm principal piece. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:28598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28598) · Entrez [257062](https://www.ncbi.nlm.nih.gov/gene/257062) · UniProt [Q86XM0](https://www.uniprot.org/uniprotkb/Q86XM0) · Ensembl [ENSG00000174898](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174898) · OMIM [617490](https://www.omim.org/entry/617490)

**PubMed**, as HGNC records for this gene — [21224844](https://pubmed.ncbi.nlm.nih.gov/21224844/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08381 |
| As a percentage | +5.98% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08910 / 0.08060 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.699 raw, 0.414 with 3 PCs removed |

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
