---
symbol: PRKX
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [PKX1]
gene_name: protein kinase cAMP-dependent X-linked catalytic subunit
locus: Xp22.33
locus_type: gene with protein product
gene_family: [Protein kinase A family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 33.69
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PRKX

*protein kinase cAMP-dependent X-linked catalytic subunit* — Xp22.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PRKX.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | protein kinase cAMP-dependent X-linked catalytic subunit |
| Also known as | PKX1 |
| Locus | Xp22.33 — gene with protein product |
| Gene families | Protein kinase A family |
| Previously named | protein kinase X-linked |

**Function**, from UniProt [P51817](https://www.uniprot.org/uniprotkb/P51817) (reviewed):

> Serine/threonine protein kinase regulated by and mediating cAMP signaling in cells. Acts through phosphorylation of downstream targets that may include CREB, SMAD6 and PKD1 and has multiple functions in cellular differentiation and epithelial morphogenesis. Regulates myeloid cell differentiation through SMAD6 phosphorylation. Involved in nephrogenesis by stimulating renal epithelial cell migration and tubulogenesis. Also involved in angiogenesis through stimulation of endothelial cell proliferation, migration and vascular-like structure formation

**Summary**, from NCBI Gene [5613](https://www.ncbi.nlm.nih.gov/gene/5613):

> This gene encodes a serine threonine protein kinase that has similarity to the catalytic subunit of cyclic AMP dependent protein kinases. The encoded protein is developmentally regulated and may be involved in renal epithelial morphogenesis. This protein may also be involved in macrophage and granulocyte maturation. Abnormal recombination between this gene and a related pseudogene on chromosome Y is a frequent cause of sex reversal disorder in XX males and XY females. Pseudogenes of this gene are found on chromosomes X, 15 and Y. [provided by RefSeq, Feb 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9441) · Entrez [5613](https://www.ncbi.nlm.nih.gov/gene/5613) · UniProt [P51817](https://www.uniprot.org/uniprotkb/P51817) · Ensembl [ENSG00000183943](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183943) · OMIM [300083](https://www.omim.org/entry/300083)

**PubMed**, as HGNC records for this gene — [7633447](https://pubmed.ncbi.nlm.nih.gov/7633447/), [10026146](https://pubmed.ncbi.nlm.nih.gov/10026146/), [12082174](https://pubmed.ncbi.nlm.nih.gov/12082174/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 33.69 CPM |
| Lines where detected | 47 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 61 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.040× |
| Wild-type minus altered | 1.094× |
| Compounds moving it up in WT lines | 63 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00269 |
| As a percentage | -0.19% |
| FDR, exposure-shuffle null | 0.5147 |
| In TP53-wild-type lines / altered lines | -0.00465 / -0.00166 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.527 raw, -0.138 with 3 PCs removed |

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
