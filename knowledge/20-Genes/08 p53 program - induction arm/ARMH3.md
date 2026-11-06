---
symbol: ARMH3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ13114, DGARM]
gene_name: armadillo like helical domain containing 3
locus: 10q24.32
locus_type: gene with protein product
gene_family: [Armadillo like helical domain containing]
family_siblings_here: [ARFGEF1, ARFGEF2, ATM, FANCD2, HTT, PPP4R3A, RALGAPB, TAF3]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 92.19
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ARMH3

*armadillo like helical domain containing 3* — 10q24.32

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ARMH3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | armadillo like helical domain containing 3 |
| Also known as | FLJ13114, DGARM, distal Golgi armadillo repeat protein |
| Locus | 10q24.32 — gene with protein product |
| Gene families | Armadillo like helical domain containing |
| Other genes here in those families | [[ARFGEF1]], [[ARFGEF2]], [[ATM]], [[FANCD2]], [[HTT]], [[PPP4R3A]], [[RALGAPB]], [[TAF3]] |
| Previously named | chromosome 10 open reading frame 76 |

**Function**, from UniProt [Q5T2E6](https://www.uniprot.org/uniprotkb/Q5T2E6) (reviewed):

> Involved in GBF1 recruitment, Golgi maintenance and protein secretion

**Summary**, from NCBI Gene [79591](https://www.ncbi.nlm.nih.gov/gene/79591):

> Involved in regulation of Golgi organization. Located in Golgi membrane and cytosol. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25788](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25788) · Entrez [79591](https://www.ncbi.nlm.nih.gov/gene/79591) · UniProt [Q5T2E6](https://www.uniprot.org/uniprotkb/Q5T2E6) · Ensembl [ENSG00000120029](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120029) · OMIM [620867](https://www.omim.org/entry/620867)

**PubMed**, as HGNC records for this gene — [31519766](https://pubmed.ncbi.nlm.nih.gov/31519766/), [31829496](https://pubmed.ncbi.nlm.nih.gov/31829496/), [38515862](https://pubmed.ncbi.nlm.nih.gov/38515862/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 92.19 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 120 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.001× |
| Wild-type minus altered | 1.019× |
| Compounds moving it up in WT lines | 57 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00345 |
| As a percentage | -0.24% |
| FDR, exposure-shuffle null | 0.0749 |
| In TP53-wild-type lines / altered lines | -0.00168 / -0.00453 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.599 raw, -0.124 with 3 PCs removed |

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
