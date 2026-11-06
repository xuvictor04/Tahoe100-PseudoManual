---
symbol: PPP2CB
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [PP2Abeta]
gene_name: protein phosphatase 2 catalytic subunit beta
locus: 8p12
locus_type: gene with protein product
gene_family: [Protein phosphatase catalytic subunits, STRIPAK complex]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 119.05
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PPP2CB

*protein phosphatase 2 catalytic subunit beta* — 8p12

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PPP2CB.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | protein phosphatase 2 catalytic subunit beta |
| Also known as | PP2Abeta, protein phosphatase 2A catalytic subunit, beta isoform |
| Locus | 8p12 — gene with protein product |
| Gene families | Protein phosphatase catalytic subunits; STRIPAK complex |
| Previously named | protein phosphatase 2 (formerly 2A), catalytic subunit, beta isoform; protein phosphatase 2, catalytic subunit, beta isozyme |

**Function**, from UniProt [P62714](https://www.uniprot.org/uniprotkb/P62714) (reviewed):

> Catalytic subunit of protein phosphatase 2A (PP2A), a serine/threonine phosphatase involved in the regulation of a wide variety of enzymes, signal transduction pathways, and cellular events (Probable). PP2A can modulate the activity of phosphorylase B kinase, casein kinase 2, mitogen-stimulated S6 kinase, and MAP-2 kinase. Part of the striatin-interacting phosphatase and kinase (STRIPAK) complexes. STRIPAK complexes have critical roles in protein (de)phosphorylation and are regulators of multiple signaling pathways including Hippo, MAPK, nuclear receptor and cytoskeleton remodeling. Different types of STRIPAK complexes are involved in a variety of biological processes such as cell growth, differentiation, apoptosis, metabolism and immune regulation (PubMed:18782753)

**Summary**, from NCBI Gene [5516](https://www.ncbi.nlm.nih.gov/gene/5516):

> This gene encodes the phosphatase 2A catalytic subunit. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. This gene encodes a beta isoform of the catalytic subunit. [provided by RefSeq, Mar 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9300](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9300) · Entrez [5516](https://www.ncbi.nlm.nih.gov/gene/5516) · UniProt [P62714](https://www.uniprot.org/uniprotkb/P62714) · Ensembl [ENSG00000104695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104695) · OMIM [176916](https://www.omim.org/entry/176916)

**PubMed**, as HGNC records for this gene — [8383590](https://pubmed.ncbi.nlm.nih.gov/8383590/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 119.05 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 175 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.063× |
| Wild-type minus altered | 1.027× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00580 |
| As a percentage | +0.40% |
| FDR, exposure-shuffle null | 0.0125 |
| In TP53-wild-type lines / altered lines | 0.00712 / 0.00500 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.347 raw, 0.294 with 3 PCs removed |

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
