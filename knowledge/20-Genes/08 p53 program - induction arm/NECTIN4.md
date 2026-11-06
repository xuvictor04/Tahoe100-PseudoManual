---
symbol: NECTIN4
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [nectin-4, PRR4, LNIR]
gene_name: nectin cell adhesion molecule 4
locus: 1q23.3
locus_type: gene with protein product
gene_family: [V-set domain containing, C2-set domain containing, Nectins and nectin-like molecules]
family_siblings_here: [NPHS1, PILRA]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 2.25
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# NECTIN4

*nectin cell adhesion molecule 4* — 1q23.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NECTIN4.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | nectin cell adhesion molecule 4 |
| Also known as | nectin-4, PRR4, LNIR |
| Locus | 1q23.3 — gene with protein product |
| Gene families | V-set domain containing; C2-set domain containing; Nectins and nectin-like molecules |
| Other genes here in those families | [[NPHS1]], [[PILRA]] |
| Previously named | poliovirus receptor-related 4 |

**Function**, from UniProt [Q96NY8](https://www.uniprot.org/uniprotkb/Q96NY8) (reviewed):

> Seems to be involved in cell adhesion through trans-homophilic and -heterophilic interactions, the latter including specifically interactions with NECTIN1. Does not act as receptor for alpha-herpesvirus entry into cells

**Summary**, from NCBI Gene [81607](https://www.ncbi.nlm.nih.gov/gene/81607):

> This gene encodes a member of the nectin family. The encoded protein contains two immunoglobulin-like (Ig-like) C2-type domains and one Ig-like V-type domain. It is involved in cell adhesion through trans-homophilic and -heterophilic interactions. It is a single-pass type I membrane protein. The soluble form is produced by proteolytic cleavage at the cell surface by the metalloproteinase ADAM17/TACE. The secreted form is found in both breast tumor cell lines and breast tumor patients. Mutations in this gene are the cause of ectodermal dysplasia-syndactyly syndrome type 1, an autosomal recessive disorder. Alternatively spliced transcript variants have been found but the full-length nature of the variant has not been determined.[provided by RefSeq, Jan 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:19688](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19688) · Entrez [81607](https://www.ncbi.nlm.nih.gov/gene/81607) · UniProt [Q96NY8](https://www.uniprot.org/uniprotkb/Q96NY8) · Ensembl [ENSG00000143217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143217) · OMIM [609607](https://www.omim.org/entry/609607)

**PubMed**, as HGNC records for this gene — [11544254](https://pubmed.ncbi.nlm.nih.gov/11544254/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 2.25 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 100 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.028× |
| Wild-type minus altered | 1.115× |
| Compounds moving it up in WT lines | 50 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01118 |
| As a percentage | +0.78% |
| FDR, exposure-shuffle null | 0.2274 |
| In TP53-wild-type lines / altered lines | 0.00035 / 0.01775 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.184 raw, 0.024 with 3 PCs removed |

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
