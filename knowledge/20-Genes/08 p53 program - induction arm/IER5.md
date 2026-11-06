---
symbol: IER5
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: immediate early response 5
locus: 1q25.3
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 34.73
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# IER5

*immediate early response 5* — 1q25.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/IER5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | immediate early response 5 |
| Also known as | — (no recorded alias) |
| Locus | 1q25.3 — gene with protein product |

**Function**, from UniProt [Q5VY09](https://www.uniprot.org/uniprotkb/Q5VY09) (reviewed):

> Plays a role as a transcription factor (PubMed:22132193, PubMed:25355627). Mediates positive transcriptional regulation of several chaperone genes during the heat shock response in a HSF1-dependent manner (PubMed:25355627, PubMed:25816751). Mediates negative transcriptional regulation of CDC25B expression (PubMed:22132193). Plays a role in the dephosphorylation of the heat shock factor HSF1 and ribosomal protein S6 kinase (S6K) by the protein phosphatase PP2A (PubMed:25816751, PubMed:26496226). Involved in the regulation of cell proliferation and resistance to thermal stress (PubMed:22132193, PubMed:25355627, PubMed:26496226). Involved in the cell cycle checkpoint and survival in response to ionizing radiation (PubMed:19238419, PubMed:22132193). Associates with chromatin to the CDC25B promoter (PubMed:22132193)

**Summary**, from NCBI Gene [51278](https://www.ncbi.nlm.nih.gov/gene/51278):

> This gene encodes a protein that is similar to other immediate early response proteins. In the mouse, a similar gene may play an important role in mediating the cellular response to mitogenic signals. Studies in rats found the expression of a similar gene to be increased after waking and sleep deprivation. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:5393](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5393) · Entrez [51278](https://www.ncbi.nlm.nih.gov/gene/51278) · UniProt [Q5VY09](https://www.uniprot.org/uniprotkb/Q5VY09) · Ensembl [ENSG00000162783](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162783) · OMIM [607177](https://www.omim.org/entry/607177)

**PubMed**, as HGNC records for this gene — [10049588](https://pubmed.ncbi.nlm.nih.gov/10049588/), [11102586](https://pubmed.ncbi.nlm.nih.gov/11102586/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 34.73 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 88 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.029× |
| Wild-type minus altered | 1.081× |
| Compounds moving it up in WT lines | 54 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01730 |
| As a percentage | +1.21% |
| FDR, exposure-shuffle null | 0.0013 |
| In TP53-wild-type lines / altered lines | 0.01640 / 0.01786 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.522 raw, 0.089 with 3 PCs removed |

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
