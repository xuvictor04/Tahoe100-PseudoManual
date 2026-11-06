---
symbol: PDE4C
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
gene_name: phosphodiesterase 4C
locus: 19p13.11
locus_type: gene with protein product
gene_family: [Phosphodiesterases]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PDE4C

*phosphodiesterase 4C* — 19p13.11

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PDE4C.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | phosphodiesterase 4C |
| Also known as | phosphodiesterase E1 dunce homolog (Drosophila) |
| Locus | 19p13.11 — gene with protein product |
| Gene families | Phosphodiesterases |
| Previously named | phosphodiesterase 4C, cAMP-specific (dunce (Drosophila)-homolog phosphodiesterase E1); phosphodiesterase 4C, cAMP-specific |

**Function**, from UniProt [Q08493](https://www.uniprot.org/uniprotkb/Q08493) (reviewed):

> Hydrolyzes the second messenger cAMP, which is a key regulator of many important physiological processes

**Summary**, from NCBI Gene [5143](https://www.ncbi.nlm.nih.gov/gene/5143):

> The protein encoded by this gene belongs to the cyclic nucleotide phosphodiesterase (PDE) family, and PDE4 subfamily. This PDE hydrolyzes the second messenger, cAMP, which is a regulator and mediator of a number of cellular responses to extracellular signals. Thus, by regulating the cellular concentration of cAMP, this protein plays a key role in many important physiological processes. Alternatively spliced transcript variants encoding different isoforms have been described for this gene.[provided by RefSeq, Jul 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:8782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8782) · Entrez [5143](https://www.ncbi.nlm.nih.gov/gene/5143) · UniProt [Q08493](https://www.uniprot.org/uniprotkb/Q08493) · Ensembl [ENSG00000105650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105650) · OMIM [600128](https://www.omim.org/entry/600128)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07273 |
| As a percentage | +5.17% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06186 / 0.07833 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.608 raw, 0.315 with 3 PCs removed |

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
