---
symbol: VWCE
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [URG11, FLJ32009, VWC1]
gene_name: von Willebrand factor C and EGF domains
locus: 11q12.2
locus_type: gene with protein product
gene_family: [Cysteine rich transmembrane BMP regulators]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# VWCE

*von Willebrand factor C and EGF domains* — 11q12.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/VWCE.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | von Willebrand factor C and EGF domains |
| Also known as | URG11, FLJ32009, VWC1 |
| Locus | 11q12.2 — gene with protein product |
| Gene families | Cysteine rich transmembrane BMP regulators |

**Function**, from UniProt [Q96DN2](https://www.uniprot.org/uniprotkb/Q96DN2) (reviewed):

> May be a regulatory element in the beta-catenin signaling pathway and a target for chemoprevention of hapatocellular carcinoma

**Summary**, from NCBI Gene [220001](https://www.ncbi.nlm.nih.gov/gene/220001):

> Predicted to enable calcium ion binding activity. Predicted to be involved in cellular response to virus. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:26487](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26487) · Entrez [220001](https://www.ncbi.nlm.nih.gov/gene/220001) · UniProt [Q96DN2](https://www.uniprot.org/uniprotkb/Q96DN2) · Ensembl [ENSG00000167992](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167992) · OMIM [611115](https://www.omim.org/entry/611115)

**PubMed**, as HGNC records for this gene — [12869306](https://pubmed.ncbi.nlm.nih.gov/12869306/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07533 |
| As a percentage | +5.36% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06184 / 0.08351 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.610 raw, 0.691 with 3 PCs removed |

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
