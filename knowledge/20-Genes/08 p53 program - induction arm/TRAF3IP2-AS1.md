---
symbol: TRAF3IP2-AS1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [C6UAS, BetaFAAR]
gene_name: TRAF3IP2 antisense RNA 1
locus: 6q21
locus_type: RNA, long non-coding
gene_family: [Antisense RNAs]
family_siblings_here: [ENSG00000225420, ENSG00000258851, ENSG00000285190, EPHA1-AS1, KCNMB2-AS1, PITRM1-AS1, PYCARD-AS1, ZNF503-AS1]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 47.54
mg53_verdict: none
tags: [gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TRAF3IP2-AS1

*TRAF3IP2 antisense RNA 1* — 6q21

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TRAF3IP2-AS1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | TRAF3IP2 antisense RNA 1 |
| Also known as | C6UAS, BetaFAAR, Beta-cell function and apoptosis regulator |
| Locus | 6q21 — RNA, long non-coding |
| Gene families | Antisense RNAs |
| Other genes here in those families | [[ENSG00000225420]], [[ENSG00000258851]], [[ENSG00000285190]], [[EPHA1-AS1]], [[KCNMB2-AS1]], [[PITRM1-AS1]], [[PYCARD-AS1]], [[ZNF503-AS1]] |
| Previously named | TRAF3IP2 antisense RNA 2 (non-protein coding); chromosome 6 open reading frame 3; non-protein coding RNA 248; TRAF3IP2 antisense RNA 1 (non-protein coding) |

NCBI Gene carries no summary paragraph for this locus, which is usual for a non-coding RNA.

**Accessions** — [HGNC:40005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40005) · Entrez [643749](https://www.ncbi.nlm.nih.gov/gene/643749) · Ensembl [ENSG00000231889](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231889)

**PubMed**, as HGNC records for this gene — [33941656](https://pubmed.ncbi.nlm.nih.gov/33941656/), [34183666](https://pubmed.ncbi.nlm.nih.gov/34183666/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 47.54 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 60 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.093× |
| Wild-type minus altered | 1.065× |
| Compounds moving it up in WT lines | 82 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00216 |
| As a percentage | -0.15% |
| FDR, exposure-shuffle null | 0.2652 |
| In TP53-wild-type lines / altered lines | -0.00180 / -0.00238 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.042 raw, 0.120 with 3 PCs removed |

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
