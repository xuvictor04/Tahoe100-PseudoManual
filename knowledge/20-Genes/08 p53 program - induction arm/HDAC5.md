---
symbol: HDAC5
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [KIAA0600, NY-CO-9, FLJ90614]
gene_name: histone deacetylase 5
locus: 17q21.31
locus_type: gene with protein product
gene_family: [Histone deacetylases, class IIA]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 54.19
mg53_verdict: none
tags: [gene, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# HDAC5

*histone deacetylase 5* — 17q21.31

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HDAC5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | histone deacetylase 5 |
| Also known as | KIAA0600, NY-CO-9, FLJ90614 |
| Locus | 17q21.31 — gene with protein product |
| Gene families | Histone deacetylases, class IIA |

**Function**, from UniProt [Q9UQL6](https://www.uniprot.org/uniprotkb/Q9UQL6) (reviewed):

> In vitro, it deacetylates lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4) (PubMed:10220385). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Histone deacetylases act via the formation of large multiprotein complexes. Involved in muscle maturation by repressing transcription of myocyte enhancer MEF2C. During muscle differentiation, it shuttles into the cytoplasm, allowing the expression of myocyte enhancer factors. Involved in the MTA1-mediated epigenetic regulation of ESR1 expression in breast cancer. Serves as a corepressor of RARA and causes its deacetylation (PubMed:28167758). In association with RARA, plays a role in the repression of microRNA-10a and thereby in the inflammatory response (PubMed:28167758)

**Summary**, from NCBI Gene [10014](https://www.ncbi.nlm.nih.gov/gene/10014):

> Histones play a critical role in transcriptional regulation, cell cycle progression, and developmental events. Histone acetylation/deacetylation alters chromosome structure and affects transcription factor access to DNA. The protein encoded by this gene belongs to the class II histone deacetylase/acuc/apha family. It possesses histone deacetylase activity and represses transcription when tethered to a promoter. It coimmunoprecipitates only with HDAC3 family member and might form multicomplex proteins. It also interacts with myocyte enhancer factor-2 (MEF2) proteins, resulting in repression of MEF2-dependent genes. This gene is thought to be associated with colon cancer. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:14068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14068) · Entrez [10014](https://www.ncbi.nlm.nih.gov/gene/10014) · UniProt [Q9UQL6](https://www.uniprot.org/uniprotkb/Q9UQL6) · Ensembl [ENSG00000108840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108840) · OMIM [605315](https://www.omim.org/entry/605315)

**PubMed**, as HGNC records for this gene — [10220385](https://pubmed.ncbi.nlm.nih.gov/10220385/), [9610721](https://pubmed.ncbi.nlm.nih.gov/9610721/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 54.19 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 146 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.025× |
| Wild-type minus altered | 1.035× |
| Compounds moving it up in WT lines | 70 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00493 |
| As a percentage | -0.34% |
| FDR, exposure-shuffle null | 0.1529 |
| In TP53-wild-type lines / altered lines | -0.00275 / -0.00626 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.140 raw, -0.120 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 7 targets |
| Activity vs MG53 across exposures (r) | 0.030 (q 0.417) |
| With 3 principal components removed | 0.045 (q 0.200) |
| Within line, across exposures (r) | -0.003 (q 0.855) |
| Percentile against all genes | 52.0 |

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
