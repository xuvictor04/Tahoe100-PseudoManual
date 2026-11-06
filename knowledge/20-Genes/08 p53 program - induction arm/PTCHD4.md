---
symbol: PTCHD4
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [PTCH53, SLC65C2, FLJ41841, dJ402H5.2]
gene_name: patched domain containing 4
locus: 6p12.3
locus_type: gene with protein product
gene_family: [Solute carrier family 65]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 7.03
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [direction-mixed, gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# PTCHD4

*patched domain containing 4* — 6p12.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/PTCHD4.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | patched domain containing 4 |
| Also known as | PTCH53, SLC65C2, FLJ41841, dJ402H5.2 |
| Locus | 6p12.3 — gene with protein product |
| Gene families | Solute carrier family 65 |
| Previously named | chromosome 6 open reading frame 138 |

**Function**, from UniProt [Q6ZW05](https://www.uniprot.org/uniprotkb/Q6ZW05) (reviewed):

> Could act as a repressor of canonical hedgehog signaling by antagonizing the effects of SMO, as suggested by down-regulation of hedgehog target genes, including GLI1, PTCH1, and PTCH2 in PTCHD4-expressing cells

**Summary**, from NCBI Gene [442213](https://www.ncbi.nlm.nih.gov/gene/442213):

> Predicted to be active in membrane. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:21345](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21345) · Entrez [442213](https://www.ncbi.nlm.nih.gov/gene/442213) · UniProt [Q6ZW05](https://www.uniprot.org/uniprotkb/Q6ZW05) · Ensembl [ENSG00000244694](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244694) · OMIM [616908](https://www.omim.org/entry/616908)

**PubMed**, as HGNC records for this gene — [25296753](https://pubmed.ncbi.nlm.nih.gov/25296753/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 7.03 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 11 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.124× |
| Wild-type minus altered | 1.218× |
| Compounds moving it up in WT lines | 60 of 98 |
| Direction mixed? | **yes** — it goes each way across compounds, so its direction is not a fact about the gene |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.01345 |
| As a percentage | +0.94% |
| FDR, exposure-shuffle null | 0.0935 |
| In TP53-wild-type lines / altered lines | 0.00750 / 0.01705 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.219 raw, 0.079 with 3 PCs removed |

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
