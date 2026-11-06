---
symbol: CSNK1G1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [CK1gamma1]
gene_name: casein kinase 1 gamma 1
locus: 15q22.31
locus_type: gene with protein product
gene_family: [Casein kinase 1 family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 163.03
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CSNK1G1

*casein kinase 1 gamma 1* — 15q22.31

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CSNK1G1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | casein kinase 1 gamma 1 |
| Also known as | CK1gamma1 |
| Locus | 15q22.31 — gene with protein product |
| Gene families | Casein kinase 1 family |
| Previously named | casein kinase 1, gamma 1 |

**Function**, from UniProt [Q9HCP0](https://www.uniprot.org/uniprotkb/Q9HCP0) (reviewed):

> Serine/threonine-protein kinase. Casein kinases are operationally defined by their preferential utilization of acidic proteins such as caseins as substrates. It can phosphorylate a large number of proteins. Participates in Wnt signaling. Regulates fast synaptic transmission mediated by glutamate (By similarity). Phosphorylates CLSPN

**Summary**, from NCBI Gene [53944](https://www.ncbi.nlm.nih.gov/gene/53944):

> This gene encodes a member of the casein kinase I gene family. This family is comprised of serine/threonine kinases that phosphorylate acidic proteins such as caseins. The encoded kinase plays a role in cell cycle checkpoint arrest in response to stalled replication forks by phosphorylating Claspin. A mutation in this gene may be associated with non-syndromic early-onset epilepsy (NSEOE). [provided by RefSeq, Jul 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2454) · Entrez [53944](https://www.ncbi.nlm.nih.gov/gene/53944) · UniProt [Q9HCP0](https://www.uniprot.org/uniprotkb/Q9HCP0) · Ensembl [ENSG00000169118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169118) · OMIM [606274](https://www.omim.org/entry/606274)

**PubMed**, as HGNC records for this gene — [11124537](https://pubmed.ncbi.nlm.nih.gov/11124537/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 163.03 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 8 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.091× |
| Wild-type minus altered | 1.055× |
| Compounds moving it up in WT lines | 88 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00025 |
| As a percentage | +0.02% |
| FDR, exposure-shuffle null | 0.9232 |
| In TP53-wild-type lines / altered lines | -0.00026 / 0.00056 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.023 raw, 0.076 with 3 PCs removed |

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
