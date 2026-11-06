---
symbol: DNAI3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DIC3, FLJ30067, NYD-SP29]
gene_name: dynein axonemal intermediate chain 3
locus: 1p22.3
locus_type: gene with protein product
gene_family: [WD repeat domain containing, Dyneins, axonemal inner arm I1/f complex subunits, Dynein intermediate chains]
family_siblings_here: [COP1, DDB2, FBXW7, RIC1, TLE4, WDR48]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 5.31
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DNAI3

*dynein axonemal intermediate chain 3* — 1p22.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DNAI3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | dynein axonemal intermediate chain 3 |
| Also known as | DIC3, FLJ30067, NYD-SP29 |
| Locus | 1p22.3 — gene with protein product |
| Gene families | WD repeat domain containing; Dyneins, axonemal inner arm I1/f complex subunits; Dynein intermediate chains |
| Other genes here in those families | [[COP1]], [[DDB2]], [[FBXW7]], [[RIC1]], [[TLE4]], [[WDR48]] |
| Previously named | WD repeat domain 63 |

**Function**, from UniProt [Q8IWG1](https://www.uniprot.org/uniprotkb/Q8IWG1) (reviewed):

> Acts as a negative regulator of cell migration, invasion, and metastasis downstream of p53/TP53, through inhibition of Arp2/3 complex-mediated actin polymerization (PubMed:32128961). Via its association with the multisubunit axonemal dynein complex, is potentially involved in the regulation of cilia function (By similarity). May play a role in osteogenesis of dental tissue-derived mesenchymal stem cells (By similarity)

**Summary**, from NCBI Gene [126820](https://www.ncbi.nlm.nih.gov/gene/126820):

> Enables Arp2/3 complex binding activity. Involved in negative regulation of Arp2/3 complex-mediated actin nucleation and negative regulation of cell migration. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30711](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30711) · Entrez [126820](https://www.ncbi.nlm.nih.gov/gene/126820) · UniProt [Q8IWG1](https://www.uniprot.org/uniprotkb/Q8IWG1) · Ensembl [ENSG00000162643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162643) · OMIM [617968](https://www.omim.org/entry/617968)

**PubMed**, as HGNC records for this gene — [21953912](https://pubmed.ncbi.nlm.nih.gov/21953912/), [35006274](https://pubmed.ncbi.nlm.nih.gov/35006274/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 5.31 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 163 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.044× |
| Wild-type minus altered | 1.089× |
| Compounds moving it up in WT lines | 51 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01292 |
| As a percentage | +0.90% |
| FDR, exposure-shuffle null | 0.0330 |
| In TP53-wild-type lines / altered lines | 0.01256 / 0.01314 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.383 raw, -0.039 with 3 PCs removed |

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
