---
symbol: TM7SF3
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: transmembrane 7 superfamily member 3
locus: 12p11.23
locus_type: gene with protein product
gene_family: [7TM uncharacterized proteins]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 54.71
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# TM7SF3

*transmembrane 7 superfamily member 3* — 12p11.23

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/TM7SF3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | transmembrane 7 superfamily member 3 |
| Also known as | — (no recorded alias) |
| Locus | 12p11.23 — gene with protein product |
| Gene families | 7TM uncharacterized proteins |

**Function**, from UniProt [Q9NS93](https://www.uniprot.org/uniprotkb/Q9NS93) (reviewed):

> Involved in the inhibition of cytokine-induced death of pancreatic beta cells. Involved in the promotion of insulin secretion from pancreatic beta cells (PubMed:21853325). Is a downstream transcriptional target of p53/TP53, and acts as a pro-survival homeostatic factor that attenuates the development of cellular stress. Maintains protein homeostasis and promotes cell survival through attenuation of endoplasmic reticulum (ER) stress and the subsequent induction of unfolded protein response (UPR) (PubMed:27740623)

**Summary**, from NCBI Gene [51768](https://www.ncbi.nlm.nih.gov/gene/51768):

> Involved in cellular response to unfolded protein; negative regulation of programmed cell death; and positive regulation of insulin secretion. Located in cytosol; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:23049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23049) · Entrez [51768](https://www.ncbi.nlm.nih.gov/gene/51768) · UniProt [Q9NS93](https://www.uniprot.org/uniprotkb/Q9NS93) · Ensembl [ENSG00000064115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064115) · OMIM [605181](https://www.omim.org/entry/605181)

**PubMed**, as HGNC records for this gene — [10828615](https://pubmed.ncbi.nlm.nih.gov/10828615/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 54.71 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 117 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.064× |
| Wild-type minus altered | 1.059× |
| Compounds moving it up in WT lines | 67 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.01225 |
| As a percentage | -0.85% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | -0.01518 / -0.01047 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.168 raw, -0.328 with 3 PCs removed |

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
