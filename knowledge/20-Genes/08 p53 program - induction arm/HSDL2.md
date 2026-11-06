---
symbol: HSDL2
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [SDR13C1]
gene_name: hydroxysteroid dehydrogenase like 2
locus: 9q32
locus_type: gene with protein product
gene_family: [Short chain dehydrogenase/reductase superfamily, SCP2 domain containing]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 67.53
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# HSDL2

*hydroxysteroid dehydrogenase like 2* — 9q32

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/HSDL2.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | hydroxysteroid dehydrogenase like 2 |
| Also known as | SDR13C1, short chain dehydrogenase/reductase family 13C, member 1 |
| Locus | 9q32 — gene with protein product |
| Gene families | Short chain dehydrogenase/reductase superfamily; SCP2 domain containing |
| Previously named | chromosome 9 open reading frame 99 |

**Function**, from UniProt [Q6YN16](https://www.uniprot.org/uniprotkb/Q6YN16) (reviewed):

> Has apparently no steroid dehydrogenase activity (PubMed:19703561). Controls bile acid (BA) and lipid metabolism in response to nutritional cues (PubMed:38820148)

**Summary**, from NCBI Gene [84263](https://www.ncbi.nlm.nih.gov/gene/84263):

> Predicted to enable oxidoreductase activity. Involved in cholesterol homeostasis. Located in mitochondrion and peroxisome. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:18572](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18572) · Entrez [84263](https://www.ncbi.nlm.nih.gov/gene/84263) · UniProt [Q6YN16](https://www.uniprot.org/uniprotkb/Q6YN16) · Ensembl [ENSG00000119471](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119471)

**PubMed**, as HGNC records for this gene — [12834046](https://pubmed.ncbi.nlm.nih.gov/12834046/), [19027726](https://pubmed.ncbi.nlm.nih.gov/19027726/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 67.53 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 94 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.012× |
| Wild-type minus altered | 1.036× |
| Compounds moving it up in WT lines | 51 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00371 |
| As a percentage | -0.26% |
| FDR, exposure-shuffle null | 0.1049 |
| In TP53-wild-type lines / altered lines | -0.00279 / -0.00426 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | 0.090 raw, -0.113 with 3 PCs removed |

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
