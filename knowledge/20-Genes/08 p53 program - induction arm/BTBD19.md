---
symbol: BTBD19
type: gene
tier: 3
pathway_role: p53 program, induction arm
gene_name: BTB domain containing 19
locus: 1p34.1
locus_type: gene with protein product
gene_family: [BTB domain containing]
family_siblings_here: [BTBD10, KLHL24]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 6.57
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program]
generated_by: knowledge/_build/build_vault.py
---

# BTBD19

*BTB domain containing 19* — 1p34.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/BTBD19.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | BTB domain containing 19 |
| Also known as | — (no recorded alias) |
| Locus | 1p34.1 — gene with protein product |
| Gene families | BTB domain containing |
| Other genes here in those families | [[BTBD10]], [[KLHL24]] |
| Previously named | BTB (POZ) domain containing 19 |

UniProt [C9JJ37](https://www.uniprot.org/uniprotkb/C9JJ37) carries no FUNCTION annotation.

NCBI Gene carries no summary paragraph for this gene.

**Accessions** — [HGNC:27145](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27145) · Entrez [149478](https://www.ncbi.nlm.nih.gov/gene/149478) · UniProt [C9JJ37](https://www.uniprot.org/uniprotkb/C9JJ37) · Ensembl [ENSG00000222009](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000222009)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 6.57 CPM |
| Lines where detected | 49 of 50 |
| Readthrough geometry | no readthrough geometry |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 59 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.072× |
| Wild-type minus altered | 1.088× |
| Compounds moving it up in WT lines | 65 of 98 |
| Direction mixed? | no |
| Program membership stability | stable (4-5 of 5 folds) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.02984 |
| As a percentage | +2.09% |
| FDR, exposure-shuffle null | 0.0006 |
| In TP53-wild-type lines / altered lines | 0.01954 / 0.03556 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.399 raw, 0.460 with 3 PCs removed |

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
