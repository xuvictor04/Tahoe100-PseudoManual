---
symbol: MED23
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [CRSP130, DRIP130, Sur2]
gene_name: mediator complex subunit 23
locus: 6q23.2
locus_type: gene with protein product
gene_family: [Mediator complex]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 72.76
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# MED23

*mediator complex subunit 23* — 6q23.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/MED23.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | mediator complex subunit 23 |
| Also known as | CRSP130, DRIP130, Sur2 |
| Locus | 6q23.2 — gene with protein product |
| Gene families | Mediator complex |
| Previously named | cofactor required for Sp1 transcriptional activation, subunit 3, 130kDa; mental retardation, non-syndromic, autosomal recessive, 18 |

**Function**, from UniProt [Q9ULK4](https://www.uniprot.org/uniprotkb/Q9ULK4) (reviewed):

> Required for transcriptional activation subsequent to the assembly of the pre-initiation complex (By similarity). Component of the Mediator complex, a coactivator involved in the regulated transcription of nearly all RNA polymerase II-dependent genes. Mediator functions as a bridge to convey information from gene-specific regulatory proteins to the basal RNA polymerase II transcription machinery. Mediator is recruited to promoters by direct interactions with regulatory proteins and serves as a scaffold for the assembly of a functional pre-initiation complex with RNA polymerase II and the general transcription factors. Required for transcriptional activation by adenovirus E1A protein. Required for ELK1-dependent transcriptional activation in response to activated Ras signaling

**Summary**, from NCBI Gene [9439](https://www.ncbi.nlm.nih.gov/gene/9439):

> The activation of gene transcription is a multistep process that is triggered by factors that recognize transcriptional enhancer sites in DNA. These factors work with co-activators to direct transcriptional initiation by the RNA polymerase II apparatus. The protein encoded by this gene is a subunit of the CRSP (cofactor required for SP1 activation) complex, which, along with TFIID, is required for efficient activation by SP1. This protein is also a component of other multisubunit complexes e.g. thyroid hormone receptor-(TR-) associated proteins which interact with TR and facilitate TR function on DNA templates in conjunction with initiation factors and cofactors. This protein also acts as a metastasis suppressor. Several alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jul 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2372](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2372) · Entrez [9439](https://www.ncbi.nlm.nih.gov/gene/9439) · UniProt [Q9ULK4](https://www.uniprot.org/uniprotkb/Q9ULK4) · Ensembl [ENSG00000112282](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112282) · OMIM [605042](https://www.omim.org/entry/605042)

**PubMed**, as HGNC records for this gene — [9989412](https://pubmed.ncbi.nlm.nih.gov/9989412/), [30847200](https://pubmed.ncbi.nlm.nih.gov/30847200/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 72.76 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 172 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.065× |
| Wild-type minus altered | 1.025× |
| Compounds moving it up in WT lines | 74 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00860 |
| As a percentage | -0.59% |
| FDR, exposure-shuffle null | 0.0002 |
| In TP53-wild-type lines / altered lines | -0.00777 / -0.00911 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.322 raw, -0.247 with 3 PCs removed |

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
