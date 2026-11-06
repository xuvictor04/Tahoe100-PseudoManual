---
symbol: PGAP1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ12377, Bst1, SPG67]
gene_name: post-GPI attachment to proteins inositol deacylase 1
locus: 2q33.1
locus_type: gene with protein product
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 80.47
mg53_verdict: down with MG53
mg53_effect_on_p53_output: toward LESS p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PGAP1

*post-GPI attachment to proteins inositol deacylase 1* — 2q33.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PGAP1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | post-GPI attachment to proteins inositol deacylase 1 |
| Also known as | FLJ12377, Bst1, SPG67, GPI inositol-deacylase |
| Locus | 2q33.1 — gene with protein product |
| Previously named | post-GPI attachment to proteins 1 |

**Function**, from UniProt [Q75T13](https://www.uniprot.org/uniprotkb/Q75T13) (reviewed):

> GPI inositol-deacylase that catalyzes the remove of the acyl chain linked to the 2-OH position of inositol ring from the GPI-anchored protein (GPI-AP) in the endoplasmic reticulum (PubMed:24784135, PubMed:38167496). Initiates the post-attachment remodeling phase of GPI-AP biogenesis and participates in endoplasmic reticulum (ER)-to-Golgi transport of GPI-anchored protein (PubMed:24784135, PubMed:38167496)

**Summary**, from NCBI Gene [80055](https://www.ncbi.nlm.nih.gov/gene/80055):

> The protein encoded by this gene functions early in the glycosylphosphatidylinositol (GPI) biosynthetic pathway, catalyzing the inositol deacylation of GPI. The encoded protein is required for the production of GPI that can attach to proteins, and this may be an important factor in the transport of GPI-anchored proteins from the endoplasmic reticulum to the Golgi. Defects in this gene are a cause an autosomal recessive form of cognitive impairment. [provided by RefSeq, Jul 2017]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:25712](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25712) · Entrez [80055](https://www.ncbi.nlm.nih.gov/gene/80055) · UniProt [Q75T13](https://www.uniprot.org/uniprotkb/Q75T13) · Ensembl [ENSG00000197121](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197121) · OMIM [611655](https://www.omim.org/entry/611655)

**PubMed**, as HGNC records for this gene — [14734546](https://pubmed.ncbi.nlm.nih.gov/14734546/), [17711852](https://pubmed.ncbi.nlm.nih.gov/17711852/), [24482476](https://pubmed.ncbi.nlm.nih.gov/24482476/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 80.47 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 116 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.054× |
| Wild-type minus altered | 1.042× |
| Compounds moving it up in WT lines | 74 of 98 |
| Direction mixed? | no |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00764 |
| As a percentage | -0.53% |
| FDR, exposure-shuffle null | 0.0128 |
| In TP53-wild-type lines / altered lines | -0.00711 / -0.00797 |
| Verdict | down with MG53 |
| **Signed into p53-output units** | **toward LESS p53 output** |
| Co-regulation with MG53 across exposures (r) | -0.215 raw, -0.252 with 3 PCs removed |

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
