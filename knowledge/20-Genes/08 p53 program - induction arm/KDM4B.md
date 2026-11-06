---
symbol: KDM4B
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0876, TDRD14B]
gene_name: lysine demethylase 4B
locus: 19p13.3
locus_type: gene with protein product
gene_family: [PHD finger proteins, Tudor domain containing, Lysine demethylase 4 family]
family_siblings_here: [KDM4C, TAF3, TP53BP1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 177.92
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# KDM4B

*lysine demethylase 4B* — 19p13.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/KDM4B.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | lysine demethylase 4B |
| Also known as | KIAA0876, TDRD14B, tudor domain containing 14B |
| Locus | 19p13.3 — gene with protein product |
| Gene families | PHD finger proteins; Tudor domain containing; Lysine demethylase 4 family |
| Other genes here in those families | [[KDM4C]], [[TAF3]], [[TP53BP1]] |
| Previously named | jumonji domain containing 2B; lysine (K)-specific demethylase 4B |

**Function**, from UniProt [O94953](https://www.uniprot.org/uniprotkb/O94953) (reviewed):

> Histone demethylase that specifically demethylates 'Lys-9' of histone H3, thereby acting as a key regulator of nascent transcription (PubMed:16603238, PubMed:28262558). Does not demethylate histone H3 'Lys-4', H3 'Lys-27', H3 'Lys-36' nor H4 'Lys-20' (PubMed:16603238, PubMed:28262558). Only able to demethylate trimethylated H3 'Lys-9', with a weaker activity than KDM4A, KDM4C and KDM4D (PubMed:16603238, PubMed:28262558). Plays a critical role in the development of the central nervous system (CNS) (By similarity)

**Summary**, from NCBI Gene [23030](https://www.ncbi.nlm.nih.gov/gene/23030):

> Enables histone H3K36 demethylase activity and histone H3K9me2/H3K9me3 demethylase activity. Predicted to be involved in brain development; chromatin remodeling; and regulation of gene expression. Located in nucleoplasm. Implicated in autosomal dominant intellectual developmental disorder 65; breast cancer; colorectal cancer; malignant peripheral nerve sheath tumor; and stomach cancer. Biomarker of several diseases, including alopecia areata; lung cancer; medulloblastoma; prostate cancer; and stomach cancer. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:29136](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29136) · Entrez [23030](https://www.ncbi.nlm.nih.gov/gene/23030) · UniProt [O94953](https://www.uniprot.org/uniprotkb/O94953) · Ensembl [ENSG00000127663](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127663) · OMIM [609765](https://www.omim.org/entry/609765)

**PubMed**, as HGNC records for this gene — [10048485](https://pubmed.ncbi.nlm.nih.gov/10048485/), [15138608](https://pubmed.ncbi.nlm.nih.gov/15138608/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 177.92 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 67 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.045× |
| Wild-type minus altered | 1.050× |
| Compounds moving it up in WT lines | 78 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00553 |
| As a percentage | +0.38% |
| FDR, exposure-shuffle null | 0.0476 |
| In TP53-wild-type lines / altered lines | 0.00709 / 0.00459 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.244 raw, 0.070 with 3 PCs removed |

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
