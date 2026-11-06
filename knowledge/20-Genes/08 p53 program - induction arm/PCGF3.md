---
symbol: PCGF3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [FLJ36550, DONG1, RNF3A, MGC40413]
gene_name: polycomb group ring finger 3
locus: 4p16.3
locus_type: gene with protein product
gene_family: [Ring finger proteins, Polycomb group ring fingers]
family_siblings_here: [COP1, MDM2, MDM4, MGRN1, RC3H1, TRIM72]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 52.27
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PCGF3

*polycomb group ring finger 3* — 4p16.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PCGF3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | polycomb group ring finger 3 |
| Also known as | FLJ36550, DONG1, RNF3A, MGC40413 |
| Locus | 4p16.3 — gene with protein product |
| Gene families | Ring finger proteins; Polycomb group ring fingers |
| Other genes here in those families | [[COP1]], [[MDM2]], [[MDM4]], [[MGRN1]], [[RC3H1]], [[TRIM72]] |
| Previously named | ring finger protein 3 |

**Function**, from UniProt [Q3KNV8](https://www.uniprot.org/uniprotkb/Q3KNV8) (reviewed):

> Component of a Polycomb group (PcG) multiprotein PRC1-like complex, a complex class required to maintain the transcriptionally repressive state of many genes, including Hox genes, throughout development. PcG PRC1 complex acts via chromatin remodeling and modification of histones; it mediates monoubiquitination of histone H2A 'Lys-119', rendering chromatin heritably changed in its expressibility. Within the PRC1-like complex, regulates RNF2 ubiquitin ligase activity (PubMed:26151332). Plays a redundant role with PCGF5 as part of a PRC1-like complex that mediates monoubiquitination of histone H2A 'Lys-119' on the X chromosome and is required for normal silencing of one copy of the X chromosome in XX females (By similarity)

**Summary**, from NCBI Gene [10336](https://www.ncbi.nlm.nih.gov/gene/10336):

> The protein encoded by this gene contains a C3HC4 type RING finger, which is a motif known to be involved in protein-protein interactions. The specific function of this protein has not yet been determined. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:10066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10066) · Entrez [10336](https://www.ncbi.nlm.nih.gov/gene/10336) · UniProt [Q3KNV8](https://www.uniprot.org/uniprotkb/Q3KNV8) · Ensembl [ENSG00000185619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185619) · OMIM [617543](https://www.omim.org/entry/617543)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 52.27 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 177 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.003× |
| Wild-type minus altered | 1.019× |
| Compounds moving it up in WT lines | 51 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | unstable (0-1 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00076 |
| As a percentage | -0.05% |
| FDR, exposure-shuffle null | 0.7585 |
| In TP53-wild-type lines / altered lines | -0.00224 / 0.00013 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.468 raw, -0.111 with 3 PCs removed |

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
