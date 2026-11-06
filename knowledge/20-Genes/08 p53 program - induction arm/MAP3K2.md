---
symbol: MAP3K2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MEKK2B]
gene_name: mitogen-activated protein kinase kinase kinase 2
locus: 2q14.3
locus_type: gene with protein product
gene_family: [Mitogen-activated protein kinase kinase kinases, STE11 kinase family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 307.77
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# MAP3K2

*mitogen-activated protein kinase kinase kinase 2* — 2q14.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/MAP3K2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | mitogen-activated protein kinase kinase kinase 2 |
| Also known as | MEKK2B, MAP/ERK kinase kinase 2 |
| Locus | 2q14.3 — gene with protein product |
| Gene families | Mitogen-activated protein kinase kinase kinases; STE11 kinase family |

**Function**, from UniProt [Q9Y2U5](https://www.uniprot.org/uniprotkb/Q9Y2U5) (reviewed):

> Component of a protein kinase signal transduction cascade. Regulates the JNK and ERK5 pathways by phosphorylating and activating MAP2K5 and MAP2K7 (By similarity). Plays a role in caveolae kiss-and-run dynamics

**Summary**, from NCBI Gene [10746](https://www.ncbi.nlm.nih.gov/gene/10746):

> The protein encoded by this gene is a member of serine/threonine protein kinase family. This kinase preferentially activates other kinases involved in the MAP kinase signaling pathway. This kinase has been shown to directly phosphorylate and activate Ikappa B kinases, and thus plays a role in NF-kappa B signaling pathway. This kinase has also been found to bind and activate protein kinase C-related kinase 2, which suggests its involvement in a regulated signaling process. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6854) · Entrez [10746](https://www.ncbi.nlm.nih.gov/gene/10746) · UniProt [Q9Y2U5](https://www.uniprot.org/uniprotkb/Q9Y2U5) · Ensembl [ENSG00000169967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169967) · OMIM [609487](https://www.omim.org/entry/609487)

**PubMed**, as HGNC records for this gene — [8621389](https://pubmed.ncbi.nlm.nih.gov/8621389/), [10085062](https://pubmed.ncbi.nlm.nih.gov/10085062/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 307.77 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 132 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.037× |
| Wild-type minus altered | 1.016× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00495 |
| As a percentage | -0.34% |
| FDR, exposure-shuffle null | 0.0026 |
| In TP53-wild-type lines / altered lines | -0.00348 / -0.00584 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.259 raw, -0.132 with 3 PCs removed |

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
