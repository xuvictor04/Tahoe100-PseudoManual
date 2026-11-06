---
symbol: STX6
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: syntaxin 6
locus: 1q25.3
locus_type: gene with protein product
gene_family: [Syntaxins]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 54.78
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# STX6

*syntaxin 6* — 1q25.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/STX6.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | syntaxin 6 |
| Also known as | — (no recorded alias) |
| Locus | 1q25.3 — gene with protein product |
| Gene families | Syntaxins |

**Function**, from UniProt [O43752](https://www.uniprot.org/uniprotkb/O43752) (reviewed):

> SNARE promoting movement of transport vesicles to target membranes. Targets endosomes to the trans-Golgi network, and may therefore function in retrograde trafficking. Together with SNARE STX12, promotes movement of vesicles from endosomes to the cell membrane, and may therefore function in the endocytic recycling pathway

**Summary**, from NCBI Gene [10228](https://www.ncbi.nlm.nih.gov/gene/10228):

> Predicted to enable SNAP receptor activity and SNARE binding activity. Involved in regulation of protein localization; retrograde transport, endosome to Golgi; and vesicle fusion. Acts upstream of or within endocytic recycling. Located in early endosome; perinuclear region of cytoplasm; and trans-Golgi network. Part of SNARE complex. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11441) · Entrez [10228](https://www.ncbi.nlm.nih.gov/gene/10228) · UniProt [O43752](https://www.uniprot.org/uniprotkb/O43752) · Ensembl [ENSG00000135823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135823) · OMIM [603944](https://www.omim.org/entry/603944)

**PubMed**, as HGNC records for this gene — [10080545](https://pubmed.ncbi.nlm.nih.gov/10080545/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 54.78 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 169 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.084× |
| Wild-type minus altered | 1.042× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00376 |
| As a percentage | -0.26% |
| FDR, exposure-shuffle null | 0.1914 |
| In TP53-wild-type lines / altered lines | -0.00476 / -0.00316 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.072 raw, -0.170 with 3 PCs removed |

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
