---
symbol: ARHGAP30
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ00267]
gene_name: Rho GTPase activating protein 30
locus: 1q23.3
locus_type: gene with protein product
gene_family: [Rho GTPase activating proteins]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 1.68
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# ARHGAP30

*Rho GTPase activating protein 30* — 1q23.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ARHGAP30.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | Rho GTPase activating protein 30 |
| Also known as | FLJ00267 |
| Locus | 1q23.3 — gene with protein product |
| Gene families | Rho GTPase activating proteins |

**Function**, from UniProt [Q7Z6I6](https://www.uniprot.org/uniprotkb/Q7Z6I6) (reviewed):

> GTPase-activating protein (GAP) for RAC1 and RHOA, but not for CDC42

**Summary**, from NCBI Gene [257106](https://www.ncbi.nlm.nih.gov/gene/257106):

> Enables GTPase activator activity. Involved in negative regulation of Rho protein signal transduction. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:27414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27414) · Entrez [257106](https://www.ncbi.nlm.nih.gov/gene/257106) · UniProt [Q7Z6I6](https://www.uniprot.org/uniprotkb/Q7Z6I6) · Ensembl [ENSG00000186517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186517) · OMIM [614264](https://www.omim.org/entry/614264)

**PubMed**, as HGNC records for this gene — [21565175](https://pubmed.ncbi.nlm.nih.gov/21565175/), [25156493](https://pubmed.ncbi.nlm.nih.gov/25156493/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 1.68 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 66 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.048× |
| Wild-type minus altered | 1.141× |
| Compounds moving it up in WT lines | 52 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.03842 |
| As a percentage | +2.70% |
| FDR, exposure-shuffle null | 0.0007 |
| In TP53-wild-type lines / altered lines | 0.02996 / 0.04356 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.450 raw, 0.187 with 3 PCs removed |

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
