---
symbol: SLC6A13
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [GAT2]
gene_name: solute carrier family 6 member 13
locus: 12p13.33
locus_type: gene with protein product
gene_family: [Solute carrier family 6]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SLC6A13

*solute carrier family 6 member 13* — 12p13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SLC6A13.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | solute carrier family 6 member 13 |
| Also known as | GAT2, GABA transporter 2 |
| Locus | 12p13.33 — gene with protein product |
| Gene families | Solute carrier family 6 |
| Previously named | solute carrier family 6 (neurotransmitter transporter, GABA), member 13; solute carrier family 6 (neurotransmitter transporter), member 13 |

**Function**, from UniProt [Q9NSD5](https://www.uniprot.org/uniprotkb/Q9NSD5) (reviewed):

> Mediates sodium- and chloride-dependent transport of gamma-aminobutyric acid (GABA) (PubMed:17502375, PubMed:22932902). Mediates transport of beta-alanine (PubMed:17502375). Can also mediate transport of taurine and hypotaurine (By similarity)

**Summary**, from NCBI Gene [6540](https://www.ncbi.nlm.nih.gov/gene/6540):

> Enables gamma-aminobutyric acid:sodium:chloride symporter activity. Involved in amino acid import across plasma membrane and monocarboxylic acid transport. Located in mitochondrion and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11046) · Entrez [6540](https://www.ncbi.nlm.nih.gov/gene/6540) · UniProt [Q9NSD5](https://www.uniprot.org/uniprotkb/Q9NSD5) · Ensembl [ENSG00000010379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010379) · OMIM [615097](https://www.omim.org/entry/615097)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.08364 |
| As a percentage | +5.97% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09681 / 0.07550 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.592 raw, 0.547 with 3 PCs removed |

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
