---
symbol: SUSD6
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: sushi domain containing 6
locus: 14q24.1
locus_type: gene with protein product
gene_family: [Sushi domain containing]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 43.67
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SUSD6

*sushi domain containing 6* — 14q24.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SUSD6.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | sushi domain containing 6 |
| Also known as | — (no recorded alias) |
| Locus | 14q24.1 — gene with protein product |
| Gene families | Sushi domain containing |
| Previously named | KIAA0247 |

**Function**, from UniProt [Q92537](https://www.uniprot.org/uniprotkb/Q92537) (reviewed):

> May play a role in growth-suppressive activity and cell death (PubMed:24652652). May be involved in the production of chemokine molecules in umbilical vein endothelial cells (HUVECs) cultured in THP1 monocyte LPS-induced medium (PubMed:20236627). Plays a role in preventing tumor onset (By similarity)

**Summary**, from NCBI Gene [9766](https://www.ncbi.nlm.nih.gov/gene/9766):

> Involved in DNA damage response. Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:19956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19956) · Entrez [9766](https://www.ncbi.nlm.nih.gov/gene/9766) · UniProt [Q92537](https://www.uniprot.org/uniprotkb/Q92537) · Ensembl [ENSG00000100647](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100647) · OMIM [616761](https://www.omim.org/entry/616761)

**PubMed**, as HGNC records for this gene — [9039502](https://pubmed.ncbi.nlm.nih.gov/9039502/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 43.67 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 85 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.124× |
| Wild-type minus altered | 1.084× |
| Compounds moving it up in WT lines | 74 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00989 |
| As a percentage | -0.68% |
| FDR, exposure-shuffle null | 0.0080 |
| In TP53-wild-type lines / altered lines | -0.00990 / -0.00989 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.030 raw, -0.275 with 3 PCs removed |

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
