---
symbol: PCNX1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0995, KIAA0805, pecanex]
gene_name: pecanex 1
locus: 14q24.2
locus_type: gene with protein product
gene_family: [Pecanex family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 224.19
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PCNX1

*pecanex 1* — 14q24.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PCNX1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | pecanex 1 |
| Also known as | KIAA0995, KIAA0805, pecanex |
| Locus | 14q24.2 — gene with protein product |
| Gene families | Pecanex family |
| Previously named | pecanex-like 1 (Drosophila); pecanex homolog 1 (Drosophila) |

UniProt [Q96RV3](https://www.uniprot.org/uniprotkb/Q96RV3) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [22990](https://www.ncbi.nlm.nih.gov/gene/22990):

> This gene encodes an evolutionarily conserved transmembrane protein similar to the pecanex protein in Drosophila. The fly protein is a component of the Notch signaling pathway, which functions in several developmental processes. [provided by RefSeq, Jul 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:19740](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19740) · Entrez [22990](https://www.ncbi.nlm.nih.gov/gene/22990) · UniProt [Q96RV3](https://www.uniprot.org/uniprotkb/Q96RV3) · Ensembl [ENSG00000100731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100731) · OMIM [617655](https://www.omim.org/entry/617655)

**PubMed**, as HGNC records for this gene — [9244429](https://pubmed.ncbi.nlm.nih.gov/9244429/), [15777640](https://pubmed.ncbi.nlm.nih.gov/15777640/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 224.19 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 157 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.053× |
| Wild-type minus altered | 1.020× |
| Compounds moving it up in WT lines | 77 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00218 |
| As a percentage | -0.15% |
| FDR, exposure-shuffle null | 0.2688 |
| In TP53-wild-type lines / altered lines | -0.00221 / -0.00217 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.118 raw, -0.004 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
