---
symbol: PILRA
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [FDF03]
gene_name: paired immunoglobin like type 2 receptor alpha
locus: 7q22.1
locus_type: gene with protein product
gene_family: [V-set domain containing]
family_siblings_here: [NECTIN4, NPHS1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PILRA

*paired immunoglobin like type 2 receptor alpha* — 7q22.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PILRA.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | paired immunoglobin like type 2 receptor alpha |
| Also known as | FDF03 |
| Locus | 7q22.1 — gene with protein product |
| Gene families | V-set domain containing |
| Other genes here in those families | [[NECTIN4]], [[NPHS1]] |
| Previously named | paired immunoglobin-like type 2 receptor alpha |

**Function**, from UniProt [Q9UKJ1](https://www.uniprot.org/uniprotkb/Q9UKJ1) (reviewed):

> Paired receptors consist of highly related activating and inhibitory receptors and are widely involved in the regulation of the immune system. PILRA is thought to act as a cellular signaling inhibitory receptor by recruiting cytoplasmic phosphatases like PTPN6/SHP-1 and PTPN11/SHP-2 via their SH2 domains that block signal transduction through dephosphorylation of signaling molecules. Receptor for PIANP

**Summary**, from NCBI Gene [29992](https://www.ncbi.nlm.nih.gov/gene/29992):

> Cell signaling pathways rely on a dynamic interaction between activating and inhibiting processes. SHP-1-mediated dephosphorylation of protein tyrosine residues is central to the regulation of several cell signaling pathways. Two types of inhibitory receptor superfamily members are immunoreceptor tyrosine-based inhibitory motif (ITIM)-bearing receptors and their non-ITIM-bearing, activating counterparts. Control of cell signaling via SHP-1 is thought to occur through a balance between PILRalpha-mediated inhibition and PILRbeta-mediated activation. These paired immunoglobulin-like receptor genes are located in a tandem head-to-tail orientation on chromosome 7. This particular gene encodes the ITIM-bearing member of the receptor pair, which functions in the inhibitory role. Alternative splicing has been observed at this locus and three variants, each encoding a distinct isoform, are described. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:20396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20396) · Entrez [29992](https://www.ncbi.nlm.nih.gov/gene/29992) · UniProt [Q9UKJ1](https://www.uniprot.org/uniprotkb/Q9UKJ1) · Ensembl [ENSG00000085514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000085514) · OMIM [605341](https://www.omim.org/entry/605341)

**PubMed**, as HGNC records for this gene — [10660620](https://pubmed.ncbi.nlm.nih.gov/10660620/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06339 |
| As a percentage | +4.49% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06799 / 0.06060 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.657 raw, 0.624 with 3 PCs removed |

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
