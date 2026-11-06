---
symbol: SLC2A14
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [GLUT14]
gene_name: solute carrier family 2 member 14
locus: 12p13.31
locus_type: gene with protein product
gene_family: [Solute carrier family 2]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SLC2A14

*solute carrier family 2 member 14* — 12p13.31

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SLC2A14.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | solute carrier family 2 member 14 |
| Also known as | GLUT14 |
| Locus | 12p13.31 — gene with protein product |
| Gene families | Solute carrier family 2 |
| Previously named | solute carrier family 2 (facilitated glucose transporter), member 3 pseudogene 3; solute carrier family 2 (facilitated glucose transporter), member 14 |

**Function**, from UniProt [Q8TDB8](https://www.uniprot.org/uniprotkb/Q8TDB8) (reviewed):

> Hexose transporter that can mediate the transport of glucose and dehydroascorbate across the cell membrane

**Summary**, from NCBI Gene [144195](https://www.ncbi.nlm.nih.gov/gene/144195):

> Members of the glucose transporter (GLUT) family, including SLC2A14, are highly conserved integral membrane proteins that transport hexoses such as glucose and fructose into all mammalian cells. GLUTs show tissue and cell-type specific expression (Wu and Freeze, 2002 [PubMed 12504846]).[supplied by OMIM, Mar 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18301) · Entrez [144195](https://www.ncbi.nlm.nih.gov/gene/144195) · UniProt [Q8TDB8](https://www.uniprot.org/uniprotkb/Q8TDB8) · Ensembl [ENSG00000173262](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173262) · OMIM [611039](https://www.omim.org/entry/611039)

**PubMed**, as HGNC records for this gene — [12504846](https://pubmed.ncbi.nlm.nih.gov/12504846/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06498 |
| As a percentage | +4.61% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08351 / 0.05374 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.580 raw, 0.356 with 3 PCs removed |

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
