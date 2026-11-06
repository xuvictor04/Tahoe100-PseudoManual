---
symbol: FRS2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [SNT-1, FRS2alpha, SNT1, FRS2A]
gene_name: fibroblast growth factor receptor substrate 2
locus: 12q15
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 121.81
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# FRS2

*fibroblast growth factor receptor substrate 2* — 12q15

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/FRS2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | fibroblast growth factor receptor substrate 2 |
| Also known as | SNT-1, FRS2alpha, SNT1, FRS2A |
| Locus | 12q15 — gene with protein product |

**Function**, from UniProt [Q8WU20](https://www.uniprot.org/uniprotkb/Q8WU20) (reviewed):

> Adapter protein that links activated FGR and NGF receptors to downstream signaling pathways. Plays an important role in the activation of MAP kinases and in the phosphorylation of PIK3R1, the regulatory subunit of phosphatidylinositol 3-kinase, in response to ligand-mediated activation of FGFR1. Modulates signaling via SHC1 by competing for a common binding site on NTRK1

**Summary**, from NCBI Gene [10818](https://www.ncbi.nlm.nih.gov/gene/10818):

> Enables fibroblast growth factor receptor binding activity and neurotrophin TRKA receptor binding activity. Involved in negative regulation of cardiac muscle cell differentiation. Acts upstream of or within fibroblast growth factor receptor signaling pathway. Located in adherens junction. Biomarker of renal cell carcinoma. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:16971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16971) · Entrez [10818](https://www.ncbi.nlm.nih.gov/gene/10818) · UniProt [Q8WU20](https://www.uniprot.org/uniprotkb/Q8WU20) · Ensembl [ENSG00000166225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166225) · OMIM [607743](https://www.omim.org/entry/607743)

**PubMed**, as HGNC records for this gene — [8761293](https://pubmed.ncbi.nlm.nih.gov/8761293/), [9660748](https://pubmed.ncbi.nlm.nih.gov/9660748/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 121.81 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 43 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.083× |
| Wild-type minus altered | 1.031× |
| Compounds moving it up in WT lines | 72 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00245 |
| As a percentage | -0.17% |
| FDR, exposure-shuffle null | 0.1595 |
| In TP53-wild-type lines / altered lines | -0.00371 / -0.00168 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.028 raw, -0.029 with 3 PCs removed |

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
