---
symbol: REV3L
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [POLZ, REV3]
gene_name: REV3 like, DNA directed polymerase zeta catalytic subunit
locus: 6q21
locus_type: gene with protein product
gene_family: [DNA polymerases]
family_siblings_here: [POLH]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 201.03
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# REV3L

*REV3 like, DNA directed polymerase zeta catalytic subunit* — 6q21

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/REV3L.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | REV3 like, DNA directed polymerase zeta catalytic subunit |
| Also known as | POLZ, REV3, polymerase, DNA, zeta |
| Locus | 6q21 — gene with protein product |
| Gene families | DNA polymerases |
| Other genes here in those families | [[POLH]] |
| Previously named | REV3 (yeast homolog)-like, catalytic subunit of DNA polymerase zeta; REV3-like, catalytic subunit of DNA polymerase zeta (yeast); REV3-like, polymerase (DNA directed), zeta, catalytic subunit |

**Function**, from UniProt [O60673](https://www.uniprot.org/uniprotkb/O60673) (reviewed):

> Catalytic subunit of the DNA polymerase zeta complex, an error-prone polymerase specialized in translesion DNA synthesis (TLS). Lacks an intrinsic 3'-5' exonuclease activity and thus has no proofreading function

**Summary**, from NCBI Gene [5980](https://www.ncbi.nlm.nih.gov/gene/5980):

> The protein encoded by this gene represents the catalytic subunit of DNA polymerase zeta, which functions in translesion DNA synthesis. The encoded protein can be found in mitochondria, where it protects DNA from damage. Defects in this gene are a cause of Mobius syndrome. [provided by RefSeq, Jan 2017]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9968) · Entrez [5980](https://www.ncbi.nlm.nih.gov/gene/5980) · UniProt [O60673](https://www.uniprot.org/uniprotkb/O60673) · Ensembl [ENSG00000009413](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000009413) · OMIM [602776](https://www.omim.org/entry/602776)

**PubMed**, as HGNC records for this gene — [9618506](https://pubmed.ncbi.nlm.nih.gov/9618506/), [9925914](https://pubmed.ncbi.nlm.nih.gov/9925914/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 201.03 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 63 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.107× |
| Wild-type minus altered | 1.053× |
| Compounds moving it up in WT lines | 90 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00023 |
| As a percentage | +0.02% |
| FDR, exposure-shuffle null | 0.9350 |
| In TP53-wild-type lines / altered lines | -0.00004 / 0.00039 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.274 raw, 0.200 with 3 PCs removed |

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
