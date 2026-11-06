---
symbol: CASK
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [LIN2, CAGH39, FGS4]
gene_name: calcium/calmodulin dependent serine protein kinase
locus: Xp11.4
locus_type: gene with protein product
gene_family: [Membrane associated guanylate kinases, PDZ domain containing, CASK family, SH3 domain containing]
family_siblings_here: [EPS8L2, HCLS1, MPP4, PRX, RAPGEF6]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 164.43
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# CASK

*calcium/calmodulin dependent serine protein kinase* — Xp11.4

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/CASK.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | calcium/calmodulin dependent serine protein kinase |
| Also known as | LIN2, CAGH39, FGS4 |
| Locus | Xp11.4 — gene with protein product |
| Gene families | Membrane associated guanylate kinases; PDZ domain containing; CASK family; SH3 domain containing |
| Other genes here in those families | [[EPS8L2]], [[HCLS1]], [[MPP4]], [[PRX]], [[RAPGEF6]] |
| Previously named | trinucleotide repeat containing 8; calcium/calmodulin-dependent serine protein kinase (MAGUK family) |

**Function**, from UniProt [O14936](https://www.uniprot.org/uniprotkb/O14936) (reviewed):

> Multidomain scaffolding Mg(2+)-independent protein kinase that catalyzes the phosphotransfer from ATP to proteins such as NRXN1, and plays a role in synaptic transmembrane protein anchoring and ion channel trafficking (PubMed:18423203). Contributes to neural development and regulation of gene expression via interaction with the transcription factor TBR1. Binds to cell-surface proteins, including amyloid precursor protein, neurexins and syndecans. May mediate a link between the extracellular matrix and the actin cytoskeleton via its interaction with syndecan and with the actin/spectrin-binding protein 4.1. Component of the LIN-10-LIN-2-LIN-7 complex, which associates with the motor protein KIF17 to transport vesicles containing N-methyl-D-aspartate (NMDA) receptor subunit NR2B along microtubules (By similarity)

**Summary**, from NCBI Gene [8573](https://www.ncbi.nlm.nih.gov/gene/8573):

> This gene encodes a calcium/calmodulin-dependent serine protein kinase. The encoded protein is a MAGUK (membrane-associated guanylate kinase) protein family member. These proteins are scaffold proteins and the encoded protein is located at synapses in the brain. Mutations in this gene are associated with FG syndrome 4, intellectual disability and microcephaly with pontine and cerebellar hypoplasia, and a form of X-linked intellectual disability. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2017]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:1497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1497) · Entrez [8573](https://www.ncbi.nlm.nih.gov/gene/8573) · UniProt [O14936](https://www.uniprot.org/uniprotkb/O14936) · Ensembl [ENSG00000147044](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147044) · OMIM [300172](https://www.omim.org/entry/300172)

**PubMed**, as HGNC records for this gene — [9722958](https://pubmed.ncbi.nlm.nih.gov/9722958/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 164.43 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 129 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.003× |
| Wild-type minus altered | 1.034× |
| Compounds moving it up in WT lines | 52 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00085 |
| As a percentage | -0.06% |
| FDR, exposure-shuffle null | 0.7452 |
| In TP53-wild-type lines / altered lines | 0.00086 / -0.00184 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.364 raw, 0.100 with 3 PCs removed |

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
