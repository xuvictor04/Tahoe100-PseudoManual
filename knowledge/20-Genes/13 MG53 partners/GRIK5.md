---
symbol: GRIK5
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [GluK5, KA2]
gene_name: glutamate ionotropic receptor kainate type subunit 5
locus: 19q13.2
locus_type: gene with protein product
gene_family: [Glutamate ionotropic receptor kainate type subunits]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# GRIK5

*glutamate ionotropic receptor kainate type subunit 5* — 19q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/GRIK5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | glutamate ionotropic receptor kainate type subunit 5 |
| Also known as | GluK5, KA2 |
| Locus | 19q13.2 — gene with protein product |
| Gene families | Glutamate ionotropic receptor kainate type subunits |
| Previously named | glutamate receptor, ionotropic, kainate 5 |

**Function**, from UniProt [Q16478](https://www.uniprot.org/uniprotkb/Q16478) (reviewed):

> Ionotropic glutamate receptor that functions as a cation-permeable ligand-gated ion channel, gated by L-glutamate and the glutamatergic agonist kainic acid. Cannot form functional channels on its own and produces channel activity only in heteromeric assembly with GRIK1 and GRIK2 subunits (PubMed:1321949, PubMed:14511640, PubMed:8730589). Can form functional heteromeric receptors with GRIK3 (By similarity)

**Summary**, from NCBI Gene [2901](https://www.ncbi.nlm.nih.gov/gene/2901):

> This gene encodes a protein that belongs to the glutamate-gated ionic channel family. Glutamate functions as the major excitatory neurotransmitter in the central nervous system through activation of ligand-gated ion channels and G protein-coupled membrane receptors. The protein encoded by this gene forms functional heteromeric kainate-preferring ionic channels with the subunits encoded by related gene family members. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4583) · Entrez [2901](https://www.ncbi.nlm.nih.gov/gene/2901) · UniProt [Q16478](https://www.uniprot.org/uniprotkb/Q16478) · Ensembl [ENSG00000105737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105737) · OMIM [600283](https://www.omim.org/entry/600283)

**PubMed**, as HGNC records for this gene — [7527545](https://pubmed.ncbi.nlm.nih.gov/7527545/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07538 |
| As a percentage | +5.36% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09819 / 0.06154 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.735 raw, 0.504 with 3 PCs removed |

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
