---
symbol: TMEM68
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ32370, DIESL]
gene_name: transmembrane protein 68
locus: 8q12.1
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 26.26
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TMEM68

*transmembrane protein 68* — 8q12.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TMEM68.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | transmembrane protein 68 |
| Also known as | FLJ32370, DIESL, DGAT1/2-independent enzyme synthesizing storage lipids |
| Locus | 8q12.1 — gene with protein product |

**Function**, from UniProt [Q96MH6](https://www.uniprot.org/uniprotkb/Q96MH6) (reviewed):

> Catalytic subunit of the alternative triglyceride biosynthesis pathway, which mediates formation of triacylglycerol from diacylglycerol and membrane phospholipids (PubMed:37648867). Synthesizes triacylglycerol at the expense of membrane phospholipids, such as phosphatidylcholine (PC) and its ether-linked form (ePC), thereby altering the composition of membranes (PubMed:37648867). The alternative triglyceride biosynthesis pathway is probably required to provide the energy required for rapid growth when fuel sources are limiting (PubMed:37648867). It maintains mitochondrial function during periods of extracellular lipid starvation (PubMed:37648867). Can also use acyl-CoA as donor: acts as a acyl-CoA:monoacylglycerol acyltransferase (MGAT), but also shows acyl-CoA:diacylglycerol acyltransferase (DGAT) activity (By similarity)

**Summary**, from NCBI Gene [137695](https://www.ncbi.nlm.nih.gov/gene/137695):

> Enables phospholipid:diacylglycerol acyltransferase activity. Involved in triglyceride biosynthetic process. Is active in endoplasmic reticulum membrane. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:26510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26510) · Entrez [137695](https://www.ncbi.nlm.nih.gov/gene/137695) · UniProt [Q96MH6](https://www.uniprot.org/uniprotkb/Q96MH6) · Ensembl [ENSG00000167904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167904)

**PubMed**, as HGNC records for this gene — [28472192](https://pubmed.ncbi.nlm.nih.gov/28472192/), [36768334](https://pubmed.ncbi.nlm.nih.gov/36768334/), [37648867](https://pubmed.ncbi.nlm.nih.gov/37648867/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 26.26 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 17 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.084× |
| Wild-type minus altered | 1.065× |
| Compounds moving it up in WT lines | 85 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00121 |
| As a percentage | -0.08% |
| FDR, exposure-shuffle null | 0.6813 |
| In TP53-wild-type lines / altered lines | 0.00322 / -0.00390 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.063 raw, 0.031 with 3 PCs removed |

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
