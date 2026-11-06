---
symbol: CERS5
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [Trh4, MGC45411, FLJ25304]
gene_name: ceramide synthase 5
locus: 12q13.12
locus_type: gene with protein product
gene_family: [CERS class homeoboxes, Ceramide synthases]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 66.54
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CERS5

*ceramide synthase 5* — 12q13.12

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CERS5.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | ceramide synthase 5 |
| Also known as | Trh4, MGC45411, FLJ25304 |
| Locus | 12q13.12 — gene with protein product |
| Gene families | CERS class homeoboxes; Ceramide synthases |
| Previously named | LAG1 longevity assurance homolog 5 (S. cerevisiae); LAG1 homolog, ceramide synthase 5 |

**Function**, from UniProt [Q8N5B7](https://www.uniprot.org/uniprotkb/Q8N5B7) (reviewed):

> Ceramide synthase that catalyzes the transfer of the fatty acyl chain from fatty acyl-CoA to a sphingoid base, with high selectivity toward palmitoyl-CoA (hexadecanoyl-CoA; C16:0-CoA) (PubMed:16951403, PubMed:18541923, PubMed:22144673, PubMed:22661289, PubMed:23530041, PubMed:26887952, PubMed:29632068, PubMed:31916624). Can use different sphingoid bases as substrates for ceramide synthesis, such as sphinganine in de novo synthesis, and sphing-4E-enine (sphingosine), (4R)-hydroxysphinganine (phytosphingosine) or sphinga-4E,14Z-dienine in salvage pathways (PubMed:31916624). Other fatty acyl-CoAs such as long-chain saturated stearoyl-CoA (octadecanoyl-CoA; C18:0-CoA), myristoyl-CoA (tetradecanoyl-CoA; C14:0-CoA), and monounsaturated oleoyl-CoA (9Z-octadecenoyl-CoA; C18:1-CoA) can also act as acyl donors, but with less efficiency than hexadecanoyl-CoA (By similarity). Plays a role in de novo ceramide synthesis and surfactant homeostasis in pulmonary epithelia (By similarity)

**Summary**, from NCBI Gene [91012](https://www.ncbi.nlm.nih.gov/gene/91012):

> This gene encodes a protein that belongs to the TLC (TRAM, LAG1 and CLN8 homology domains) family of proteins. The encoded protein functions in the synthesis of ceramide, a lipid molecule that is involved in a several cellular signaling pathways. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:23749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23749) · Entrez [91012](https://www.ncbi.nlm.nih.gov/gene/91012) · UniProt [Q8N5B7](https://www.uniprot.org/uniprotkb/Q8N5B7) · Ensembl [ENSG00000139624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139624) · OMIM [615335](https://www.omim.org/entry/615335)

**PubMed**, as HGNC records for this gene — [16100120](https://pubmed.ncbi.nlm.nih.gov/16100120/), [26853464](https://pubmed.ncbi.nlm.nih.gov/26853464/), [37216827](https://pubmed.ncbi.nlm.nih.gov/37216827/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 66.54 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 93 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.039× |
| Wild-type minus altered | 1.037× |
| Compounds moving it up in WT lines | 67 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00296 |
| As a percentage | -0.21% |
| FDR, exposure-shuffle null | 0.2464 |
| In TP53-wild-type lines / altered lines | -0.00330 / -0.00276 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.418 raw, -0.015 with 3 PCs removed |

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
