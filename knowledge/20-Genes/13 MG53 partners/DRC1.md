---
symbol: DRC1
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [MGC16372, FLJ32660, CILD21]
gene_name: dynein regulatory complex subunit 1
locus: 2p23.3
locus_type: gene with protein product
gene_family: [Dynein regulatory complex]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# DRC1

*dynein regulatory complex subunit 1* — 2p23.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DRC1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | dynein regulatory complex subunit 1 |
| Also known as | MGC16372, FLJ32660, CILD21 |
| Locus | 2p23.3 — gene with protein product |
| Gene families | Dynein regulatory complex |
| Previously named | chromosome 2 open reading frame 39; coiled-coil domain containing 164; dynein regulatory complex subunit 1 homolog (Chlamydomonas) |

**Function**, from UniProt [Q96MC2](https://www.uniprot.org/uniprotkb/Q96MC2) (reviewed):

> Component of the nexin-dynein regulatory complex (N-DRC) a key regulator of ciliary/flagellar motility which maintains the alignment and integrity of the distal axoneme and regulates microtubule sliding in motile axonemes (By similarity). Plays a critical role in the assembly of N-DRC and also stabilizes the assembly of multiple inner dynein arms and radial spokes (PubMed:23354437, PubMed:34169321). Coassembles with DRC2 to form a central scaffold needed for assembly of the N-DRC and its attachment to the outer doublet microtubules (PubMed:23354437)

**Summary**, from NCBI Gene [92749](https://www.ncbi.nlm.nih.gov/gene/92749):

> This gene encodes a central component of the nexin-dynein complex (N-DRC), which regulates the assembly of ciliary dynein. Mutations in this gene can cause ciliary dyskinesia. [provided by RefSeq, Aug 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24245) · Entrez [92749](https://www.ncbi.nlm.nih.gov/gene/92749) · UniProt [Q96MC2](https://www.uniprot.org/uniprotkb/Q96MC2) · Ensembl [ENSG00000157856](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157856) · OMIM [615288](https://www.omim.org/entry/615288)

**PubMed**, as HGNC records for this gene — [23354437](https://pubmed.ncbi.nlm.nih.gov/23354437/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06762 |
| As a percentage | +4.80% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06391 / 0.06987 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.655 raw, 0.386 with 3 PCs removed |

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
