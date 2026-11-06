---
symbol: DCP1B
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ31638]
gene_name: decapping mRNA 1B
locus: 12p13.33
locus_type: gene with protein product
gene_family: [RNA decapping and exonuclease complex subunits]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 20.2
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DCP1B

*decapping mRNA 1B* — 12p13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DCP1B.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | decapping mRNA 1B |
| Also known as | FLJ31638 |
| Locus | 12p13.33 — gene with protein product |
| Gene families | RNA decapping and exonuclease complex subunits |
| Previously named | DCP1 decapping enzyme homolog B (S. cerevisiae) |

**Function**, from UniProt [Q8IZD4](https://www.uniprot.org/uniprotkb/Q8IZD4) (reviewed):

> May play a role in the degradation of mRNAs, both in normal mRNA turnover and in nonsense-mediated mRNA decay. May remove the 7-methyl guanine cap structure from mRNA molecules, yielding a 5'-phosphorylated mRNA fragment and 7m-GDP (By similarity)

**Summary**, from NCBI Gene [196513](https://www.ncbi.nlm.nih.gov/gene/196513):

> This gene encodes a member of a family of proteins that function in removing the 5' cap from mRNAs, which is a step in regulated mRNA decay. This protein localizes to cytoplasmic foci which are the site of mRNA breakdown and turnover. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24451](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24451) · Entrez [196513](https://www.ncbi.nlm.nih.gov/gene/196513) · UniProt [Q8IZD4](https://www.uniprot.org/uniprotkb/Q8IZD4) · Ensembl [ENSG00000151065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151065) · OMIM [609843](https://www.omim.org/entry/609843)

**PubMed**, as HGNC records for this gene — [12417715](https://pubmed.ncbi.nlm.nih.gov/12417715/), [15067023](https://pubmed.ncbi.nlm.nih.gov/15067023/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 20.20 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 40 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.054× |
| Wild-type minus altered | 1.091× |
| Compounds moving it up in WT lines | 66 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.01057 |
| As a percentage | -0.73% |
| FDR, exposure-shuffle null | 0.0155 |
| In TP53-wild-type lines / altered lines | -0.00795 / -0.01216 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.346 raw, -0.110 with 3 PCs removed |

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
