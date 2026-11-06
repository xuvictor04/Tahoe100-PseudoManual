---
symbol: DGKA
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [DGK-alpha]
gene_name: diacylglycerol kinase alpha
locus: 12q13.2
locus_type: gene with protein product
gene_family: [EF-hand domain containing, Diacylglycerol kinase family]
family_siblings_here: [NECAB2]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 11.15
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# DGKA

*diacylglycerol kinase alpha* — 12q13.2

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/DGKA.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | diacylglycerol kinase alpha |
| Also known as | DGK-alpha |
| Locus | 12q13.2 — gene with protein product |
| Gene families | EF-hand domain containing; Diacylglycerol kinase family |
| Other genes here in those families | [[NECAB2]] |
| Previously named | diacylglycerol kinase, alpha (80kD); diacylglycerol kinase, alpha 80kDa |

**Function**, from UniProt [P23743](https://www.uniprot.org/uniprotkb/P23743) (reviewed):

> Diacylglycerol kinase that converts diacylglycerol/DAG into phosphatidic acid/phosphatidate/PA and regulates the respective levels of these two bioactive lipids (PubMed:15544348, PubMed:2175712). Thereby, acts as a central switch between the signaling pathways activated by these second messengers with different cellular targets and opposite effects in numerous biological processes (PubMed:15544348, PubMed:2175712). Also plays an important role in the biosynthesis of complex lipids (Probable). Can also phosphorylate 1-alkyl-2-acylglycerol in vitro as efficiently as diacylglycerol provided it contains an arachidonoyl group (PubMed:15544348). Also involved in the production of alkyl-lysophosphatidic acid, another bioactive lipid, through the phosphorylation of 1-alkyl-2-acetyl glycerol (PubMed:22627129)

**Summary**, from NCBI Gene [1606](https://www.ncbi.nlm.nih.gov/gene/1606):

> The protein encoded by this gene belongs to the eukaryotic diacylglycerol kinase family. It acts as a modulator that competes with protein kinase C for the second messenger diacylglycerol in intracellular signaling pathways. It also plays an important role in the resynthesis of phosphatidylinositols and phosphorylating diacylglycerol to phosphatidic acid. Several transcript variants encoding different isoforms have been identified for this gene. [provided by RefSeq, Apr 2017]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2849](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2849) · Entrez [1606](https://www.ncbi.nlm.nih.gov/gene/1606) · UniProt [P23743](https://www.uniprot.org/uniprotkb/P23743) · Ensembl [ENSG00000065357](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065357) · OMIM [125855](https://www.omim.org/entry/125855)

**PubMed**, as HGNC records for this gene — [8180475](https://pubmed.ncbi.nlm.nih.gov/8180475/), [7959783](https://pubmed.ncbi.nlm.nih.gov/7959783/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 11.15 CPM |
| Lines where detected | 48 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 109 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.025× |
| Wild-type minus altered | 1.067× |
| Compounds moving it up in WT lines | 56 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00364 |
| As a percentage | -0.25% |
| FDR, exposure-shuffle null | 0.4944 |
| In TP53-wild-type lines / altered lines | 0.00289 / -0.00747 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.359 raw, -0.102 with 3 PCs removed |

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
