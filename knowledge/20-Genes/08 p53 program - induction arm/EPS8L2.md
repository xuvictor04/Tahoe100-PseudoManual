---
symbol: EPS8L2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ21935, FLJ22171, MGC3088]
gene_name: EPS8 signaling adaptor L2
locus: 11p15.5
locus_type: gene with protein product
gene_family: [EPS8 signaling adaptor family, SH3 domain containing]
family_siblings_here: [CASK, HCLS1, MPP4]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 22.37
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# EPS8L2

*EPS8 signaling adaptor L2* — 11p15.5

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/EPS8L2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | EPS8 signaling adaptor L2 |
| Also known as | FLJ21935, FLJ22171, MGC3088, Epidermal growth factor receptor kinase substrate 8-like protein 2 |
| Locus | 11p15.5 — gene with protein product |
| Gene families | EPS8 signaling adaptor family; SH3 domain containing |
| Other genes here in those families | [[CASK]], [[HCLS1]], [[MPP4]] |
| Previously named | EPS8-like 2; EPS8 like 2 |

**Function**, from UniProt [Q9H6S3](https://www.uniprot.org/uniprotkb/Q9H6S3) (reviewed):

> Stimulates guanine exchange activity of SOS1. May play a role in membrane ruffling and remodeling of the actin cytoskeleton. In the cochlea, is required for stereocilia maintenance in adult hair cells (By similarity)

**Summary**, from NCBI Gene [64787](https://www.ncbi.nlm.nih.gov/gene/64787):

> This gene encodes a member of the EPS8 gene family. The encoded protein, like other members of the family, is thought to link growth factor stimulation to actin organization, generating functional redundancy in the pathways that regulate actin cytoskeletal remodeling. [provided by RefSeq, Dec 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:21296](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21296) · Entrez [64787](https://www.ncbi.nlm.nih.gov/gene/64787) · UniProt [Q9H6S3](https://www.uniprot.org/uniprotkb/Q9H6S3) · Ensembl [ENSG00000177106](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177106) · OMIM [614988](https://www.omim.org/entry/614988)

**PubMed**, as HGNC records for this gene — [12620401](https://pubmed.ncbi.nlm.nih.gov/12620401/), [26282398](https://pubmed.ncbi.nlm.nih.gov/26282398/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 22.37 CPM |
| Lines where detected | 37 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 69 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.006× |
| Wild-type minus altered | 1.075× |
| Compounds moving it up in WT lines | 57 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00912 |
| As a percentage | +0.63% |
| FDR, exposure-shuffle null | 0.1787 |
| In TP53-wild-type lines / altered lines | 0.00308 / 0.01184 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.267 raw, 0.089 with 3 PCs removed |

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
