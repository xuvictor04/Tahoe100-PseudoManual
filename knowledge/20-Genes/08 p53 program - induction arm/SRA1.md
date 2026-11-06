---
symbol: SRA1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [SRA, STRAA1]
gene_name: steroid receptor RNA activator 1
locus: 5q31.3
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 36.12
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# SRA1

*steroid receptor RNA activator 1* — 5q31.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SRA1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | steroid receptor RNA activator 1 |
| Also known as | SRA, STRAA1, lncRNA SRA |
| Locus | 5q31.3 — gene with protein product |
| Previously named | steriod receptor RNA activator 1 |

**Function**, from UniProt [Q9HD15](https://www.uniprot.org/uniprotkb/Q9HD15) (reviewed):

> Functional RNA which acts as a transcriptional coactivator that selectively enhances steroid receptor-mediated transactivation ligand-independently through a mechanism involving the modulating N-terminal domain (AF-1) of steroid receptors. Also mediates transcriptional coactivation of steroid receptors ligand-dependently through the steroid-binding domain (AF-2). Enhances cellular proliferation and differentiation and promotes apoptosis in vivo. May play a role in tumorigenesis

**Summary**, from NCBI Gene [10011](https://www.ncbi.nlm.nih.gov/gene/10011):

> Both long non-coding and protein-coding RNAs are transcribed from this gene, and they represent alternatively spliced transcript variants. This gene was initially defined as a non-coding RNA, which is a coactivator for several nuclear receptors (NRs) and is associated with breast cancer. It has now been found that this gene is involved in the regulation of many NR and non-NR activities, including metabolism, adipogenesis and chromatin organization. The long non-coding RNA transcripts interact with a variety of proteins, including the protein encoded by this gene. The encoded protein acts as a transcriptional repressor by binding to the non-coding RNA. [provided by RefSeq, Mar 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11281) · Entrez [10011](https://www.ncbi.nlm.nih.gov/gene/10011) · UniProt [Q9HD15](https://www.uniprot.org/uniprotkb/Q9HD15) · Ensembl [ENSG00000213523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213523) · OMIM [603819](https://www.omim.org/entry/603819)

**PubMed**, as HGNC records for this gene — [10199399](https://pubmed.ncbi.nlm.nih.gov/10199399/), [30272285](https://pubmed.ncbi.nlm.nih.gov/30272285/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 36.12 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 82 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.058× |
| Wild-type minus altered | 1.043× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00776 |
| As a percentage | +0.54% |
| FDR, exposure-shuffle null | 0.0064 |
| In TP53-wild-type lines / altered lines | 0.00653 / 0.00851 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.422 raw, 0.333 with 3 PCs removed |

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
