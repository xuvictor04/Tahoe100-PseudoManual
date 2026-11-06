---
symbol: CREBRF
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [LRF]
gene_name: CREB3 regulatory factor
locus: 5q35.1
locus_type: gene with protein product
gene_family: [Basic leucine zipper proteins]
family_siblings_here: [NFIL3, XBP1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 126.52
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CREBRF

*CREB3 regulatory factor* — 5q35.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CREBRF.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | CREB3 regulatory factor |
| Also known as | LRF, luman/CREB3 recruitment factor |
| Locus | 5q35.1 — gene with protein product |
| Gene families | Basic leucine zipper proteins |
| Other genes here in those families | [[NFIL3]], [[XBP1]] |
| Previously named | chromosome 5 open reading frame 41 |

**Function**, from UniProt [Q8IUR6](https://www.uniprot.org/uniprotkb/Q8IUR6) (reviewed):

> Acts as a negative regulator of the endoplasmic reticulum stress response or unfolded protein response (UPR). Represses the transcriptional activity of CREB3 during the UPR. Recruits CREB3 into nuclear foci

**Summary**, from NCBI Gene [153222](https://www.ncbi.nlm.nih.gov/gene/153222):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in several processes, including negative regulation of endoplasmic reticulum unfolded protein response; positive regulation of protein catabolic process; and regulation of transcription by RNA polymerase II. Located in cytoplasm and nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24050) · Entrez [153222](https://www.ncbi.nlm.nih.gov/gene/153222) · UniProt [Q8IUR6](https://www.uniprot.org/uniprotkb/Q8IUR6) · Ensembl [ENSG00000164463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164463) · OMIM [617109](https://www.omim.org/entry/617109)

**PubMed**, as HGNC records for this gene — [18391022](https://pubmed.ncbi.nlm.nih.gov/18391022/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 126.52 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 152 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.080× |
| Wild-type minus altered | 1.030× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00014 |
| As a percentage | +0.01% |
| FDR, exposure-shuffle null | 0.9756 |
| In TP53-wild-type lines / altered lines | 0.00449 / -0.00249 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.247 raw, 0.078 with 3 PCs removed |

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
