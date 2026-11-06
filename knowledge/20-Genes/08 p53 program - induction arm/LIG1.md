---
symbol: LIG1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [LIGI, hLig1]
gene_name: DNA ligase 1
locus: 19q13.33
locus_type: gene with protein product
gene_family: [DNA ligases, Nucleotide excision repair]
family_siblings_here: [DDB2]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 31.64
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# LIG1

*DNA ligase 1* — 19q13.33

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/LIG1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | DNA ligase 1 |
| Also known as | LIGI, hLig1, DNA ligase I |
| Locus | 19q13.33 — gene with protein product |
| Gene families | DNA ligases; Nucleotide excision repair |
| Other genes here in those families | [[DDB2]] |
| Previously named | ligase I, DNA, ATP-dependent |

**Function**, from UniProt [P18858](https://www.uniprot.org/uniprotkb/P18858) (reviewed):

> DNA ligase that seals nicks in double-stranded during DNA repair (PubMed:30395541). Also involved in DNA replication and DNA recombination

**Summary**, from NCBI Gene [3978](https://www.ncbi.nlm.nih.gov/gene/3978):

> This gene encodes a member of the ATP-dependent DNA ligase protein family. The encoded protein functions in DNA replication, recombination, and the base excision repair process. Mutations in this gene that lead to DNA ligase I deficiency result in immunodeficiency and increased sensitivity to DNA-damaging agents. Disruption of this gene may also be associated with a variety of cancers. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6598](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6598) · Entrez [3978](https://www.ncbi.nlm.nih.gov/gene/3978) · UniProt [P18858](https://www.uniprot.org/uniprotkb/P18858) · Ensembl [ENSG00000105486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105486) · OMIM [126391](https://www.omim.org/entry/126391)

**PubMed**, as HGNC records for this gene — [1733856](https://pubmed.ncbi.nlm.nih.gov/1733856/), [11032816](https://pubmed.ncbi.nlm.nih.gov/11032816/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 31.64 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 102 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.055× |
| Wild-type minus altered | 1.049× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00458 |
| As a percentage | -0.32% |
| FDR, exposure-shuffle null | 0.2921 |
| In TP53-wild-type lines / altered lines | 0.00084 / -0.00786 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.190 raw, 2.99e-04 with 3 PCs removed |

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
