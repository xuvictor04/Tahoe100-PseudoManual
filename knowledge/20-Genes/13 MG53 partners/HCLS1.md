---
symbol: HCLS1
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [HS1, CTTNL]
gene_name: hematopoietic cell-specific Lyn substrate 1
locus: 3q13.33
locus_type: gene with protein product
gene_family: [SH3 domain containing]
family_siblings_here: [CASK, EPS8L2, MPP4]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# HCLS1

*hematopoietic cell-specific Lyn substrate 1* — 3q13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HCLS1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | hematopoietic cell-specific Lyn substrate 1 |
| Also known as | HS1, CTTNL, cortactin-like |
| Locus | 3q13.33 — gene with protein product |
| Gene families | SH3 domain containing |
| Other genes here in those families | [[CASK]], [[EPS8L2]], [[MPP4]] |

**Function**, from UniProt [P14317](https://www.uniprot.org/uniprotkb/P14317) (reviewed):

> Substrate of the antigen receptor-coupled tyrosine kinase. Plays a role in antigen receptor signaling for both clonal expansion and deletion in lymphoid cells. May also be involved in the regulation of gene expression

**Summary**, from NCBI Gene [3059](https://www.ncbi.nlm.nih.gov/gene/3059):

> Enables RNA polymerase II-specific DNA-binding transcription factor binding activity; protein kinase binding activity; and signaling adaptor activity. Involved in several processes, including granulocyte colony-stimulating factor signaling pathway; positive regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; and positive regulation of protein import into nucleus. Located in cytosol; nucleus; and plasma membrane. Part of transcription regulator complex. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4844) · Entrez [3059](https://www.ncbi.nlm.nih.gov/gene/3059) · UniProt [P14317](https://www.uniprot.org/uniprotkb/P14317) · Ensembl [ENSG00000180353](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180353) · OMIM [601306](https://www.omim.org/entry/601306)

**PubMed**, as HGNC records for this gene — [8978766](https://pubmed.ncbi.nlm.nih.gov/8978766/), [15710041](https://pubmed.ncbi.nlm.nih.gov/15710041/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07379 |
| As a percentage | +5.25% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.07743 / 0.07159 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.597 raw, 0.611 with 3 PCs removed |

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
