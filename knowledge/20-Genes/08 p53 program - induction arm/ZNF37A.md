---
symbol: ZNF37A
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KOX21, ZNF37]
gene_name: zinc finger protein 37A
locus: 10p11.1
locus_type: gene with protein product
gene_family: [Zinc fingers C2H2-type, KRAB domain containing]
family_siblings_here: [HIVEP2, ZFPM1, ZNF195, ZNF423, ZNF44, ZNF654, ZNF79, ZNF91]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 71.66
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ZNF37A

*zinc finger protein 37A* — 10p11.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ZNF37A.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | zinc finger protein 37A |
| Also known as | KOX21, ZNF37 |
| Locus | 10p11.1 — gene with protein product |
| Gene families | Zinc fingers C2H2-type; KRAB domain containing |
| Other genes here in those families | [[HIVEP2]], [[ZFPM1]], [[ZNF195]], [[ZNF423]], [[ZNF44]], [[ZNF654]], [[ZNF79]], [[ZNF91]] |
| Previously named | zinc finger protein 37a (KOX 21) |

**Function**, from UniProt [P17032](https://www.uniprot.org/uniprotkb/P17032) (reviewed):

> May be involved in transcriptional regulation

**Summary**, from NCBI Gene [7587](https://www.ncbi.nlm.nih.gov/gene/7587):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:13102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13102) · Entrez [7587](https://www.ncbi.nlm.nih.gov/gene/7587) · UniProt [P17032](https://www.uniprot.org/uniprotkb/P17032) · Ensembl [ENSG00000075407](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075407) · OMIM [616085](https://www.omim.org/entry/616085)

**PubMed**, as HGNC records for this gene — [2014798](https://pubmed.ncbi.nlm.nih.gov/2014798/), [8464732](https://pubmed.ncbi.nlm.nih.gov/8464732/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 71.66 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 58 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.019× |
| Wild-type minus altered | 1.037× |
| Compounds moving it up in WT lines | 57 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00214 |
| As a percentage | -0.15% |
| FDR, exposure-shuffle null | 0.4027 |
| In TP53-wild-type lines / altered lines | -0.00409 / -0.00095 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.290 raw, 0.026 with 3 PCs removed |

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
