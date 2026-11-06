---
symbol: INKA2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ31105]
gene_name: inka box actin regulator 2
locus: 1p13.2
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 5.67
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# INKA2

*inka box actin regulator 2* — 1p13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/INKA2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | inka box actin regulator 2 |
| Also known as | FLJ31105 |
| Locus | 1p13.2 — gene with protein product |
| Previously named | chromosome 1 open reading frame 183; family with sequence similarity 212, member B; family with sequence similarity 212 member B |

**Function**, from UniProt [Q9NTI7](https://www.uniprot.org/uniprotkb/Q9NTI7) (reviewed):

> Inhibitor of the serine/threonine-protein kinase PAK4. Acts by binding PAK4 in a substrate-like manner, inhibiting the protein kinase activity

**Summary**, from NCBI Gene [55924](https://www.ncbi.nlm.nih.gov/gene/55924):

> Enables protein kinase binding activity. Located in nucleolus and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:28045](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28045) · Entrez [55924](https://www.ncbi.nlm.nih.gov/gene/55924) · UniProt [Q9NTI7](https://www.uniprot.org/uniprotkb/Q9NTI7) · Ensembl [ENSG00000197852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197852) · OMIM [620403](https://www.omim.org/entry/620403)

**PubMed**, as HGNC records for this gene — [26292052](https://pubmed.ncbi.nlm.nih.gov/26292052/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 5.67 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 87 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.036× |
| Wild-type minus altered | 1.057× |
| Compounds moving it up in WT lines | 50 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01083 |
| As a percentage | +0.75% |
| FDR, exposure-shuffle null | 0.0591 |
| In TP53-wild-type lines / altered lines | -0.00458 / 0.02018 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.462 raw, 0.079 with 3 PCs removed |

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
