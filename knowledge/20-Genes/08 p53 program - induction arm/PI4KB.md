---
symbol: PI4KB
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [PI4K-BETA, pi4K92]
gene_name: phosphatidylinositol 4-kinase beta
locus: 1q21.3
locus_type: gene with protein product
gene_family: [Phosphatidylinositol 4-kinase type 3 family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 48.88
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PI4KB

*phosphatidylinositol 4-kinase beta* — 1q21.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PI4KB.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | phosphatidylinositol 4-kinase beta |
| Also known as | PI4K-BETA, pi4K92 |
| Locus | 1q21.3 — gene with protein product |
| Gene families | Phosphatidylinositol 4-kinase type 3 family |
| Previously named | phosphatidylinositol 4-kinase, catalytic, beta |

**Function**, from UniProt [Q9UBF8](https://www.uniprot.org/uniprotkb/Q9UBF8) (reviewed):

> Phosphorylates phosphatidylinositol (PI) in the first committed step in the production of the second messenger inositol-1,4,5,-trisphosphate (PIP). May regulate Golgi disintegration/reorganization during mitosis, possibly via its phosphorylation. Involved in Golgi-to-plasma membrane trafficking (By similarity) (PubMed:10559940, PubMed:11277933, PubMed:12749687, PubMed:9405935). May play an important role in the inner ear development

**Summary**, from NCBI Gene [5298](https://www.ncbi.nlm.nih.gov/gene/5298):

> Enables 1-phosphatidylinositol 4-kinase activity and 14-3-3 protein binding activity. Involved in inner ear development and phosphatidylinositol phosphate biosynthetic process. Acts upstream of or within lysosome organization. Located in Golgi membrane. Is active in cytoplasmic side of trans-Golgi network membrane. Implicated in autosomal dominant nonsyndromic deafness 87. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:8984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8984) · Entrez [5298](https://www.ncbi.nlm.nih.gov/gene/5298) · UniProt [Q9UBF8](https://www.uniprot.org/uniprotkb/Q9UBF8) · Ensembl [ENSG00000143393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143393) · OMIM [602758](https://www.omim.org/entry/602758)

**PubMed**, as HGNC records for this gene — [9020160](https://pubmed.ncbi.nlm.nih.gov/9020160/), [9405938](https://pubmed.ncbi.nlm.nih.gov/9405938/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 48.88 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 49 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.061× |
| Wild-type minus altered | 1.040× |
| Compounds moving it up in WT lines | 76 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00173 |
| As a percentage | -0.12% |
| FDR, exposure-shuffle null | 0.4773 |
| In TP53-wild-type lines / altered lines | -0.00204 / -0.00154 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.132 raw, -0.045 with 3 PCs removed |

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
