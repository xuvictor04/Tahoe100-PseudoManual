---
symbol: HTT
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [IT15]
gene_name: huntingtin
locus: 4p16.3
locus_type: gene with protein product
gene_family: [Receptor ligands, Armadillo like helical domain containing, Centriolar satellite proteins]
family_siblings_here: [ARFGEF1, ARFGEF2, ARMH3, ATM, FANCD2, HAP1, PPP4R3A, RALGAPB, RB1, SELPLG, TAF3]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 111.94
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# HTT

*huntingtin* — 4p16.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HTT.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | huntingtin |
| Also known as | IT15 |
| Locus | 4p16.3 — gene with protein product |
| Gene families | Receptor ligands; Armadillo like helical domain containing; Centriolar satellite proteins |
| Other genes here in those families | [[ARFGEF1]], [[ARFGEF2]], [[ARMH3]], [[ATM]], [[FANCD2]], [[HAP1]], [[PPP4R3A]], [[RALGAPB]], [[RB1]], [[SELPLG]], [[TAF3]] |
| Previously named | huntingtin (Huntington disease) |

**Function**, from UniProt [P42858](https://www.uniprot.org/uniprotkb/P42858) (reviewed):

> May play a role in microtubule-mediated transport or vesicle function

**Summary**, from NCBI Gene [3064](https://www.ncbi.nlm.nih.gov/gene/3064):

> Huntingtin is a disease gene linked to Huntington's disease, a neurodegenerative disorder characterized by loss of striatal neurons. This is thought to be caused by an expanded, unstable trinucleotide repeat in the huntingtin gene, which translates as a polyglutamine repeat in the protein product. A fairly broad range of trinucleotide repeats (9-35) has been identified in normal controls, and repeat numbers in excess of 40 have been described as pathological. The huntingtin locus is large, spanning 180 kb and consisting of 67 exons. The huntingtin gene is widely expressed and is required for normal development. It is expressed as 2 alternatively polyadenylated forms displaying different relative abundance in various fetal and adult tissues. The larger transcript is approximately 13.7 kb and is expressed predominantly in adult and fetal brain whereas the smaller transcript of approximately 10.3 kb is more widely expressed. The genetic defect leading to Huntington's disease may not necessarily eliminate transcription, but may confer a new property on the mRNA or alter the function of the protein. One candidate is the huntingtin-associated protein-1, highly expressed in brain, which has increased affinity for huntingtin protein with expanded polyglutamine repeats. This gene contains an upstream open reading frame in the 5' UTR that inhibits expression of the huntingtin gene product through translational repression. [provided by RefSeq, Jul 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4851) · Entrez [3064](https://www.ncbi.nlm.nih.gov/gene/3064) · UniProt [P42858](https://www.uniprot.org/uniprotkb/P42858) · Ensembl [ENSG00000197386](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197386) · OMIM [613004](https://www.omim.org/entry/613004)

**PubMed**, as HGNC records for this gene — [8458085](https://pubmed.ncbi.nlm.nih.gov/8458085/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 111.94 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 119 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.047× |
| Wild-type minus altered | 1.022× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00726 |
| As a percentage | -0.50% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | -0.00617 / -0.00792 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.149 raw, -0.236 with 3 PCs removed |

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
