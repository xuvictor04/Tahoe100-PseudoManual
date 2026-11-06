---
symbol: FAM193A
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [RES4-22]
gene_name: family with sequence similarity 193 member A
locus: 4p16.3
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 223.08
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FAM193A

*family with sequence similarity 193 member A* — 4p16.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/FAM193A.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | family with sequence similarity 193 member A |
| Also known as | RES4-22 |
| Locus | 4p16.3 — gene with protein product |
| Previously named | chromosome 4 open reading frame 8; family with sequence similarity 193, member A |

**Function**, from UniProt [P78312](https://www.uniprot.org/uniprotkb/P78312) (reviewed):

> Acts as a positive regulator of p53/TP53 by interacting with p53 repressors MDM2 and MDM4 and destabilizing MDM4 which leads to enhanced p53 transcriptional activity

**Summary**, from NCBI Gene [8603](https://www.ncbi.nlm.nih.gov/gene/8603):

> Involved in positive regulation of signal transduction by p53 class mediator. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:16822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16822) · Entrez [8603](https://www.ncbi.nlm.nih.gov/gene/8603) · UniProt [P78312](https://www.uniprot.org/uniprotkb/P78312) · Ensembl [ENSG00000125386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125386) · OMIM [620037](https://www.omim.org/entry/620037)

**PubMed**, as HGNC records for this gene — [9734812](https://pubmed.ncbi.nlm.nih.gov/9734812/), [36897777](https://pubmed.ncbi.nlm.nih.gov/36897777/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 223.08 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 144 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.031× |
| Wild-type minus altered | 1.018× |
| Compounds moving it up in WT lines | 68 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00071 |
| As a percentage | +0.05% |
| FDR, exposure-shuffle null | 0.7573 |
| In TP53-wild-type lines / altered lines | -0.00069 / 0.00156 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.149 raw, 0.238 with 3 PCs removed |

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
