---
symbol: NTPCR
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [MGC13186, HCR-NTPase, THEP1]
gene_name: nucleoside-triphosphatase, cancer-related
locus: 1q42.2
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 21.58
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# NTPCR

*nucleoside-triphosphatase, cancer-related* — 1q42.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/NTPCR.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | nucleoside-triphosphatase, cancer-related |
| Also known as | MGC13186, HCR-NTPase, THEP1, human cancer-related NTPase |
| Locus | 1q42.2 — gene with protein product |
| Previously named | chromosome 1 open reading frame 57 |

**Function**, from UniProt [Q9BSD7](https://www.uniprot.org/uniprotkb/Q9BSD7) (reviewed):

> Has nucleotide phosphatase activity towards ATP, GTP, CTP, TTP and UTP. Hydrolyzes nucleoside diphosphates with lower efficiency

**Summary**, from NCBI Gene [84284](https://www.ncbi.nlm.nih.gov/gene/84284):

> The protein encoded by this gene is a non-specific nucleoside triphosphatase that is slow-acting in vitro. This gene is overexpressed in many tumor tissues, and while it is not essential for the cell, overexpression is cytotoxic. However, the cytotoxicity is not related to its triphosphatase activity. [provided by RefSeq, Jul 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:28204](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28204) · Entrez [84284](https://www.ncbi.nlm.nih.gov/gene/84284) · UniProt [Q9BSD7](https://www.uniprot.org/uniprotkb/Q9BSD7) · Ensembl [ENSG00000135778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135778)

**PubMed**, as HGNC records for this gene — [17291528](https://pubmed.ncbi.nlm.nih.gov/17291528/), [19519914](https://pubmed.ncbi.nlm.nih.gov/19519914/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 21.58 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 31 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.022× |
| Wild-type minus altered | 1.078× |
| Compounds moving it up in WT lines | 57 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00880 |
| As a percentage | -0.61% |
| FDR, exposure-shuffle null | 0.0041 |
| In TP53-wild-type lines / altered lines | -0.01568 / -0.00462 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.438 raw, -0.443 with 3 PCs removed |

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
