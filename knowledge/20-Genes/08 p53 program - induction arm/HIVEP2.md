---
symbol: HIVEP2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MBP-2, HIV-EP2, MIBP1, ZAS2, Schnurri-2, ZNF40B]
gene_name: HIVEP zinc finger 2
locus: 6q24.2
locus_type: gene with protein product
gene_family: [Zinc fingers C2H2-type]
family_siblings_here: [ZFPM1, ZNF195, ZNF37A, ZNF423, ZNF44, ZNF654, ZNF79, ZNF91]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 396.69
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# HIVEP2

*HIVEP zinc finger 2* — 6q24.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HIVEP2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | HIVEP zinc finger 2 |
| Also known as | MBP-2, HIV-EP2, MIBP1, ZAS2, Schnurri-2, ZNF40B, c-myc intron binding protein 1 |
| Locus | 6q24.2 — gene with protein product |
| Gene families | Zinc fingers C2H2-type |
| Other genes here in those families | [[ZFPM1]], [[ZNF195]], [[ZNF37A]], [[ZNF423]], [[ZNF44]], [[ZNF654]], [[ZNF79]], [[ZNF91]] |
| Previously named | human immunodeficiency virus type I enhancer-binding protein 2; human immunodeficiency virus type I enhancer binding protein 2 |

**Function**, from UniProt [P31629](https://www.uniprot.org/uniprotkb/P31629) (reviewed):

> This protein specifically binds to the DNA sequence 5'-GGGACTTTCC-3' which is found in the enhancer elements of numerous viral promoters such as those of SV40, CMV, or HIV1. In addition, related sequences are found in the enhancer elements of a number of cellular promoters, including those of the class I MHC, interleukin-2 receptor, somatostatin receptor II, and interferon-beta genes. It may act in T-cell activation

**Summary**, from NCBI Gene [3097](https://www.ncbi.nlm.nih.gov/gene/3097):

> This gene encodes a member of a family of closely related, large, zinc finger-containing transcription factors. The encoded protein regulates transcription by binding to regulatory regions of various cellular and viral genes that maybe involved in growth, development and metastasis. The protein contains the ZAS domain comprised of two widely separated regions of zinc finger motifs, a stretch of highly acidic amino acids and a serine/threonine-rich sequence. [provided by RefSeq, Nov 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:4921](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4921) · Entrez [3097](https://www.ncbi.nlm.nih.gov/gene/3097) · UniProt [P31629](https://www.uniprot.org/uniprotkb/P31629) · Ensembl [ENSG00000010818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010818) · OMIM [143054](https://www.omim.org/entry/143054)

**PubMed**, as HGNC records for this gene — [1733857](https://pubmed.ncbi.nlm.nih.gov/1733857/), [2022670](https://pubmed.ncbi.nlm.nih.gov/2022670/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 396.69 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 158 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.088× |
| Wild-type minus altered | 1.027× |
| Compounds moving it up in WT lines | 69 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00635 |
| As a percentage | +0.44% |
| FDR, exposure-shuffle null | 0.0560 |
| In TP53-wild-type lines / altered lines | 0.00739 / 0.00571 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.091 raw, 0.232 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 8 targets |
| Activity vs MG53 across exposures (r) | -0.025 (q 0.553) |
| With 3 principal components removed | -0.107 (q 0.003) |
| Within line, across exposures (r) | -0.014 (q 0.374) |
| Percentile against all genes | 35.9 |

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
