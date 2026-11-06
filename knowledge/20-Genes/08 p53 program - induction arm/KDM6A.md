---
symbol: KDM6A
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: lysine demethylase 6A
locus: Xp11.3
locus_type: gene with protein product
gene_family: [Tetratricopeptide repeat domain containing, Lysine demethylase 6 family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 244.94
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# KDM6A

*lysine demethylase 6A* — Xp11.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/KDM6A.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | lysine demethylase 6A |
| Also known as | — (no recorded alias) |
| Locus | Xp11.3 — gene with protein product |
| Gene families | Tetratricopeptide repeat domain containing; Lysine demethylase 6 family |
| Previously named | ubiquitously transcribed tetratricopeptide repeat, X chromosome; lysine (K)-specific demethylase 6A |

**Function**, from UniProt [O15550](https://www.uniprot.org/uniprotkb/O15550) (reviewed):

> Histone demethylase that specifically demethylates 'Lys-27' of histone H3, thereby playing a central role in histone code (PubMed:17713478, PubMed:17761849, PubMed:17851529). Demethylates trimethylated and dimethylated but not monomethylated H3 'Lys-27' (PubMed:17713478, PubMed:17761849, PubMed:17851529). Plays a central role in regulation of posterior development, by regulating HOX gene expression (PubMed:17851529). Demethylation of 'Lys-27' of histone H3 is concomitant with methylation of 'Lys-4' of histone H3, and regulates the recruitment of the PRC1 complex and monoubiquitination of histone H2A (PubMed:17761849). Plays a demethylase-independent role in chromatin remodeling to regulate T-box family member-dependent gene expression (By similarity)

**Summary**, from NCBI Gene [7403](https://www.ncbi.nlm.nih.gov/gene/7403):

> This gene is located on the X chromosome and is the corresponding locus to a Y-linked gene which encodes a tetratricopeptide repeat (TPR) protein. The encoded protein of this gene contains a JmjC-domain and catalyzes the demethylation of tri/dimethylated histone H3. Multiple alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Apr 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:12637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12637) · Entrez [7403](https://www.ncbi.nlm.nih.gov/gene/7403) · UniProt [O15550](https://www.uniprot.org/uniprotkb/O15550) · Ensembl [ENSG00000147050](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147050) · OMIM [300128](https://www.omim.org/entry/300128)

**PubMed**, as HGNC records for this gene — [9499428](https://pubmed.ncbi.nlm.nih.gov/9499428/), [9381176](https://pubmed.ncbi.nlm.nih.gov/9381176/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 244.94 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 123 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.125× |
| Wild-type minus altered | 1.034× |
| Compounds moving it up in WT lines | 81 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00196 |
| As a percentage | +0.14% |
| FDR, exposure-shuffle null | 0.3544 |
| In TP53-wild-type lines / altered lines | 0.00487 / 0.00011 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.025 raw, 0.036 with 3 PCs removed |

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
