---
symbol: RAPGEF6
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [RA-GEF-2, PDZ-GEF2]
gene_name: Rap guanine nucleotide exchange factor 6
locus: 5q31.1
locus_type: gene with protein product
gene_family: [PDZ domain containing]
family_siblings_here: [CASK, MPP4, PRX]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 228.28
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# RAPGEF6

*Rap guanine nucleotide exchange factor 6* — 5q31.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/RAPGEF6.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | Rap guanine nucleotide exchange factor 6 |
| Also known as | RA-GEF-2, PDZ-GEF2 |
| Locus | 5q31.1 — gene with protein product |
| Gene families | PDZ domain containing |
| Other genes here in those families | [[CASK]], [[MPP4]], [[PRX]] |
| Previously named | PDZ domain containing guanine nucleotide exchange factor (GEF) 2; Rap guanine nucleotide exchange factor (GEF) 6 |

**Function**, from UniProt [Q8TEU7](https://www.uniprot.org/uniprotkb/Q8TEU7) (reviewed):

> Guanine nucleotide exchange factor (GEF) for Rap1A, Rap2A and M-Ras GTPases. Does not interact with cAMP

**Summary**, from NCBI Gene [51735](https://www.ncbi.nlm.nih.gov/gene/51735):

> Enables several functions, including GTP-dependent protein binding activity; guanyl-nucleotide exchange factor activity; and phosphatidic acid binding activity. Involved in positive regulation of microvillus assembly. Located in apical plasma membrane; cytosol; and endocytic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:20655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20655) · Entrez [51735](https://www.ncbi.nlm.nih.gov/gene/51735) · UniProt [Q8TEU7](https://www.uniprot.org/uniprotkb/Q8TEU7) · Ensembl [ENSG00000158987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158987) · OMIM [610499](https://www.omim.org/entry/610499)

**PubMed**, as HGNC records for this gene — [11524421](https://pubmed.ncbi.nlm.nih.gov/11524421/), [12095257](https://pubmed.ncbi.nlm.nih.gov/12095257/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 228.28 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 89 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.050× |
| Wild-type minus altered | 1.023× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00639 |
| As a percentage | +0.44% |
| FDR, exposure-shuffle null | 0.0077 |
| In TP53-wild-type lines / altered lines | 0.01236 / 0.00276 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.111 raw, 0.211 with 3 PCs removed |

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
