---
symbol: MIR34AHG
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [lnc34a]
gene_name: MIR34A host gene
locus: 1p36.22
locus_type: RNA, long non-coding
gene_family: [MicroRNA non-coding host genes]
family_siblings_here: [MIR3659HG, MIR9-1HG, MIR924HG, PVT1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 21.83
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# MIR34AHG

*MIR34A host gene* — 1p36.22

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/MIR34AHG.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | MIR34A host gene |
| Also known as | lnc34a |
| Locus | 1p36.22 — RNA, long non-coding |
| Gene families | MicroRNA non-coding host genes |
| Other genes here in those families | [[MIR3659HG]], [[MIR9-1HG]], [[MIR924HG]], [[PVT1]] |

**Summary**, from NCBI Gene [106614088](https://www.ncbi.nlm.nih.gov/gene/106614088):

> Predicted to be involved in miRNA-mediated post-transcriptional gene silencing. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:51913](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51913) · Entrez [106614088](https://www.ncbi.nlm.nih.gov/gene/106614088) · Ensembl [ENSG00000228526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228526)

**PubMed**, as HGNC records for this gene — [17540599](https://pubmed.ncbi.nlm.nih.gov/17540599/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 21.83 CPM |
| Lines where detected | 43 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 62 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.140× |
| Wild-type minus altered | 1.164× |
| Compounds moving it up in WT lines | 79 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00757 |
| As a percentage | -0.52% |
| FDR, exposure-shuffle null | 0.3371 |
| In TP53-wild-type lines / altered lines | -0.01355 / -0.00416 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.335 raw, 0.038 with 3 PCs removed |

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
