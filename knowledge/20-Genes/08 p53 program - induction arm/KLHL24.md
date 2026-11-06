---
symbol: KLHL24
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DRE1, FLJ20059, KRIP6]
gene_name: kelch like family member 24
locus: 3q27.1
locus_type: gene with protein product
gene_family: [Kelch like, BTB domain containing]
family_siblings_here: [BTBD10, BTBD19]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 140.8
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# KLHL24

*kelch like family member 24* — 3q27.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/KLHL24.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | kelch like family member 24 |
| Also known as | DRE1, FLJ20059, KRIP6 |
| Locus | 3q27.1 — gene with protein product |
| Gene families | Kelch like; BTB domain containing |
| Other genes here in those families | [[BTBD10]], [[BTBD19]] |
| Previously named | kelch-like 24 (Drosophila) |

**Function**, from UniProt [Q6TFL4](https://www.uniprot.org/uniprotkb/Q6TFL4) (reviewed):

> Necessary to maintain the balance between intermediate filament stability and degradation, a process that is essential for skin integrity (PubMed:27889062). As part of the BCR(KLHL24) E3 ubiquitin ligase complex, mediates ubiquitination of KRT14 and controls its levels during keratinocytes differentiation (PubMed:27798626). Specifically reduces kainate receptor-mediated currents in hippocampal neurons, most probably by modulating channel properties (By similarity). Has a crucial role in cardiac development and function (PubMed:30715372)

**Summary**, from NCBI Gene [54800](https://www.ncbi.nlm.nih.gov/gene/54800):

> The protein encoded by this gene is a ubiquitin ligase substrate receptor and is regulated by autoubiquitination. Variations in the translation initiation codon of this gene have been found, which result in an N-terminally truncated but more stable protein due to loss of the autoubiquitination function. The more stable mutant protein causes an increased ubiquitin and degradation of keratin 14, which leads to skin fragility and the potentially life-threatening disease epidermolysis bullosa. The encoded protein is also involved in the regulation of kainate receptors. [provided by RefSeq, Mar 2017]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25947) · Entrez [54800](https://www.ncbi.nlm.nih.gov/gene/54800) · UniProt [Q6TFL4](https://www.uniprot.org/uniprotkb/Q6TFL4) · Ensembl [ENSG00000114796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114796) · OMIM [611295](https://www.omim.org/entry/611295)

**PubMed**, as HGNC records for this gene — [17254796](https://pubmed.ncbi.nlm.nih.gov/17254796/), [27889062](https://pubmed.ncbi.nlm.nih.gov/27889062/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 140.80 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 130 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.039× |
| Wild-type minus altered | 1.025× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00378 |
| As a percentage | -0.26% |
| FDR, exposure-shuffle null | 0.3155 |
| In TP53-wild-type lines / altered lines | -0.00037 / -0.00584 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.027 raw, -0.051 with 3 PCs removed |

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
