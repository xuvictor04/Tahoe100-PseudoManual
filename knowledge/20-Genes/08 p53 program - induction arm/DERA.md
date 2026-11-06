---
symbol: DERA
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [CGI-26, DEOC]
gene_name: deoxyribose-phosphate aldolase
locus: 12p12.3
locus_type: gene with protein product
gene_family: [Aldehyde lyases]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 52.47
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DERA

*deoxyribose-phosphate aldolase* — 12p12.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DERA.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | deoxyribose-phosphate aldolase |
| Also known as | CGI-26, DEOC |
| Locus | 12p12.3 — gene with protein product |
| Gene families | Aldehyde lyases |
| Previously named | 2-deoxyribose-5-phosphate aldolase homolog (C. elegans) |

**Function**, from UniProt [Q9Y315](https://www.uniprot.org/uniprotkb/Q9Y315) (reviewed):

> Catalyzes a reversible aldol reaction between acetaldehyde and D-glyceraldehyde 3-phosphate to generate 2-deoxy-D-ribose 5-phosphate. Participates in stress granule (SG) assembly. May allow ATP production from extracellular deoxyinosine in conditions of energy deprivation

**Summary**, from NCBI Gene [51071](https://www.ncbi.nlm.nih.gov/gene/51071):

> Enables deoxyribose-phosphate aldolase activity. Involved in 2'-deoxyribonucleoside catabolic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:24269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24269) · Entrez [51071](https://www.ncbi.nlm.nih.gov/gene/51071) · UniProt [Q9Y315](https://www.uniprot.org/uniprotkb/Q9Y315) · Ensembl [ENSG00000023697](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000023697) · OMIM [619668](https://www.omim.org/entry/619668)

**PubMed**, as HGNC records for this gene — [12546782](https://pubmed.ncbi.nlm.nih.gov/12546782/), [25229427](https://pubmed.ncbi.nlm.nih.gov/25229427/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 52.47 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 108 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.070× |
| Wild-type minus altered | 1.043× |
| Compounds moving it up in WT lines | 68 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00550 |
| As a percentage | -0.38% |
| FDR, exposure-shuffle null | 0.1092 |
| In TP53-wild-type lines / altered lines | -0.00381 / -0.00652 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.091 raw, -0.013 with 3 PCs removed |

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
