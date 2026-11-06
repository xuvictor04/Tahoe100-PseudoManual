---
symbol: HSPA4L
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [APG-1, Osp94, HSPH3]
gene_name: heat shock protein family A (Hsp70) member 4 like
locus: 4q28.1
locus_type: gene with protein product
gene_family: [Heat shock 70kDa proteins]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 38.73
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# HSPA4L

*heat shock protein family A (Hsp70) member 4 like* — 4q28.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HSPA4L.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | heat shock protein family A (Hsp70) member 4 like |
| Also known as | APG-1, Osp94, HSPH3 |
| Locus | 4q28.1 — gene with protein product |
| Gene families | Heat shock 70kDa proteins |
| Previously named | heat shock 70kDa protein 4-like |

**Function**, from UniProt [O95757](https://www.uniprot.org/uniprotkb/O95757) (reviewed):

> Possesses chaperone activity in vitro where it inhibits aggregation of citrate synthase

**Summary**, from NCBI Gene [22824](https://www.ncbi.nlm.nih.gov/gene/22824):

> The protein encoded by this gene is heat shock inducible and may act as a chaperone. The encoded protein can protect the heat-shocked cell against the harmful effects of aggregated proteins. This gene is highly expressed in leukemia cells and may be a good target for therapeutic intervention. Several transcripts encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2015]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:17041](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17041) · Entrez [22824](https://www.ncbi.nlm.nih.gov/gene/22824) · UniProt [O95757](https://www.uniprot.org/uniprotkb/O95757) · Ensembl [ENSG00000164070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164070) · OMIM [619077](https://www.omim.org/entry/619077)

**PubMed**, as HGNC records for this gene — [10524232](https://pubmed.ncbi.nlm.nih.gov/10524232/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 38.73 CPM |
| Lines where detected | 48 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 114 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.129× |
| Wild-type minus altered | 1.073× |
| Compounds moving it up in WT lines | 80 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00383 |
| As a percentage | -0.27% |
| FDR, exposure-shuffle null | 0.3329 |
| In TP53-wild-type lines / altered lines | -0.00872 / -0.00063 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.302 raw, -0.142 with 3 PCs removed |

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
