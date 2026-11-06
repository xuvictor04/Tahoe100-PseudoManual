---
symbol: TMEM131
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [CC28, YR-23, RW1, KIAA0257, PRO1048]
gene_name: transmembrane protein 131
locus: 2q11.2
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 209.96
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TMEM131

*transmembrane protein 131* — 2q11.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TMEM131.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | transmembrane protein 131 |
| Also known as | CC28, YR-23, RW1, KIAA0257, PRO1048 |
| Locus | 2q11.2 — gene with protein product |

**Function**, from UniProt [Q92545](https://www.uniprot.org/uniprotkb/Q92545) (reviewed):

> Collagen binding transmembrane protein involved in collagen secretion by recruiting the ER-to-Golgi transport complex TRAPPIII (PubMed:32095531). May play a role in the immune response to viral infection

**Summary**, from NCBI Gene [23505](https://www.ncbi.nlm.nih.gov/gene/23505):

> Enables collagen binding activity. Involved in collagen biosynthetic process. Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30366](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30366) · Entrez [23505](https://www.ncbi.nlm.nih.gov/gene/23505) · UniProt [Q92545](https://www.uniprot.org/uniprotkb/Q92545) · Ensembl [ENSG00000075568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075568) · OMIM [615659](https://www.omim.org/entry/615659)

**PubMed**, as HGNC records for this gene — [10996388](https://pubmed.ncbi.nlm.nih.gov/10996388/), [32095531](https://pubmed.ncbi.nlm.nih.gov/32095531/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 209.96 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 52 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.056× |
| Wild-type minus altered | 1.047× |
| Compounds moving it up in WT lines | 76 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00305 |
| As a percentage | -0.21% |
| FDR, exposure-shuffle null | 0.0808 |
| In TP53-wild-type lines / altered lines | -0.00326 / -0.00293 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.175 raw, 0.085 with 3 PCs removed |

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
