---
symbol: PRRG1
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [PRGP1]
gene_name: proline rich and Gla domain 1
locus: Xp21.1
locus_type: gene with protein product
gene_family: [Proline rich and Gla domain containing]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 54.08
mg53_verdict: none
tags: [direction-mixed, gene, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PRRG1

*proline rich and Gla domain 1* — Xp21.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PRRG1.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | proline rich and Gla domain 1 |
| Also known as | PRGP1 |
| Locus | Xp21.1 — gene with protein product |
| Gene families | Proline rich and Gla domain containing |
| Previously named | proline-rich Gla (G-carboxyglutamic acid) polypeptide 1 |

UniProt [O14668](https://www.uniprot.org/uniprotkb/O14668) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [5638](https://www.ncbi.nlm.nih.gov/gene/5638):

> This gene encodes a vitamin K-dependent, gamma-carboxyglutamic acid (Gla)-containing, single-pass transmembrane protein. This protein contains a Gla domain at the N-terminus, preceded by a propeptide sequence required for post-translational gamma-carboxylation of specific glutamic acid residues by a vitamin K-dependent gamma-carboxylase. The C-terminus is proline-rich containing PPXY and PXXP motifs found in a variety of signaling and cytoskeletal proteins. This gene is highly expressed in the spinal cord. Several alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Mar 2010]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9469) · Entrez [5638](https://www.ncbi.nlm.nih.gov/gene/5638) · UniProt [O14668](https://www.uniprot.org/uniprotkb/O14668) · Ensembl [ENSG00000130962](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130962) · OMIM [300935](https://www.omim.org/entry/300935)

**PubMed**, as HGNC records for this gene — [9256434](https://pubmed.ncbi.nlm.nih.gov/9256434/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 54.08 CPM |
| Lines where detected | 47 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 107 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.018× |
| Wild-type minus altered | 1.039× |
| Compounds moving it up in WT lines | 57 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00156 |
| As a percentage | +0.11% |
| FDR, exposure-shuffle null | 0.5774 |
| In TP53-wild-type lines / altered lines | 0.00195 / 0.00132 |
| Verdict | none |
| **Signed into p53-output units** | **none** |
| Co-regulation with MG53 across exposures (r) | -0.292 raw, -0.176 with 3 PCs removed |

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
