---
symbol: PIDD1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MGC16925, DKFZp434D229]
gene_name: p53-induced death domain protein 1
locus: 11p15.5
locus_type: gene with protein product
gene_family: [ZU5 domain containing , Caspase-2 PIDDosome complex]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 3.07
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PIDD1

*p53-induced death domain protein 1* — 11p15.5

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PIDD1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | p53-induced death domain protein 1 |
| Also known as | MGC16925, DKFZp434D229 |
| Locus | 11p15.5 — gene with protein product |
| Gene families | ZU5 domain containing ; Caspase-2 PIDDosome complex |
| Previously named | leucine-rich repeats and death domain containing; p53-induced death domain protein |

UniProt [C0HMD6](https://www.uniprot.org/uniprotkb/C0HMD6) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [55367](https://www.ncbi.nlm.nih.gov/gene/55367):

> The protein encoded by this gene contains a leucine-rich repeat and a death domain. This protein has been shown to interact with other death domain proteins, such as Fas (TNFRSF6)-associated via death domain (FADD) and MAP-kinase activating death domain-containing protein (MADD), and thus may function as an adaptor protein in cell death-related signaling processes. The expression of the mouse counterpart of this gene has been found to be positively regulated by the tumor suppressor p53 and to induce cell apoptosis in response to DNA damage, which suggests a role for this gene as an effector of p53-dependent apoptosis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:16491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16491) · Entrez [55367](https://www.ncbi.nlm.nih.gov/gene/55367) · UniProt [C0HMD6](https://www.uniprot.org/uniprotkb/C0HMD6), [Q9HB75](https://www.uniprot.org/uniprotkb/Q9HB75) · Ensembl [ENSG00000177595](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177595) · OMIM [605247](https://www.omim.org/entry/605247)

**PubMed**, as HGNC records for this gene — [10825539](https://pubmed.ncbi.nlm.nih.gov/10825539/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 3.07 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 170 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.016× |
| Wild-type minus altered | 1.057× |
| Compounds moving it up in WT lines | 49 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00650 |
| As a percentage | +0.45% |
| FDR, exposure-shuffle null | 0.2910 |
| In TP53-wild-type lines / altered lines | -0.00604 / 0.01411 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.325 raw, 0.073 with 3 PCs removed |

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
