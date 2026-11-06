---
symbol: RPL23AP53
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: ribosomal protein L23a pseudogene 53
locus: 8p23.3
locus_type: pseudogene
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 8.32
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RPL23AP53

*ribosomal protein L23a pseudogene 53* — 8p23.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RPL23AP53.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ribosomal protein L23a pseudogene 53 |
| Also known as | — (no recorded alias) |
| Locus | 8p23.3 — pseudogene |

NCBI Gene carries no summary paragraph for this gene.

**Accessions** — [HGNC:35921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35921) · Entrez [644128](https://www.ncbi.nlm.nih.gov/gene/644128) · Ensembl [ENSG00000223508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000223508)

**PubMed**, as HGNC records for this gene — [19123937](https://pubmed.ncbi.nlm.nih.gov/19123937/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 8.32 CPM |
| Lines where detected | 48 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 84 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.041× |
| Wild-type minus altered | 1.047× |
| Compounds moving it up in WT lines | 65 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00034 |
| As a percentage | -0.02% |
| FDR, exposure-shuffle null | 0.9582 |
| In TP53-wild-type lines / altered lines | -0.00229 / 0.00092 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.340 raw, 0.040 with 3 PCs removed |

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
