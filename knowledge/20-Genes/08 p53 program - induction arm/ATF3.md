---
symbol: ATF3
type: gene
tier: 3
pathway_role: p53 program, induction arm
aliases: [ATF3]
gene_name: activating transcription factor 3
locus: 1q32.3
locus_type: gene with protein product
gene_family: [Activating transcription factor 3 family]
p53_direction: induced by p53
program_arm: P up (WT-selective induction)
median_line_cpm: 69.38
mg53_verdict: up with MG53
mg53_effect_on_p53_output: toward MORE p53 output
tags: [gene, mg53-associated, p53-induced, p53-program, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# ATF3

*activating transcription factor 3* — 1q32.3

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ATF3.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | activating transcription factor 3 |
| Also known as | — (no recorded alias) |
| Locus | 1q32.3 — gene with protein product |
| Gene families | Activating transcription factor 3 family |

**Function**, from UniProt [P18847](https://www.uniprot.org/uniprotkb/P18847) (reviewed):

> This protein binds the cAMP response element (CRE) (consensus: 5'-GTGACGT[AC][AG]-3'), a sequence present in many viral and cellular promoters. Represses transcription from promoters with ATF sites. It may repress transcription by stabilizing the binding of inhibitory cofactors at the promoter

**Summary**, from NCBI Gene [467](https://www.ncbi.nlm.nih.gov/gene/467):

> This gene encodes a member of the mammalian activation transcription factor/cAMP responsive element-binding (CREB) protein family of transcription factors. This gene is induced by a variety of signals, including many of those encountered by cancer cells, and is involved in the complex process of cellular stress response. Multiple transcript variants encoding different isoforms have been found for this gene. It is possible that alternative splicing of this gene may be physiologically important in the regulation of target genes. [provided by RefSeq, Apr 2011]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:785) · Entrez [467](https://www.ncbi.nlm.nih.gov/gene/467) · UniProt [P18847](https://www.uniprot.org/uniprotkb/P18847) · Ensembl [ENSG00000162772](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162772) · OMIM [603148](https://www.omim.org/entry/603148)

**PubMed**, as HGNC records for this gene — [7515060](https://pubmed.ncbi.nlm.nih.gov/7515060/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### How well it is measured

| | |
|---|---|
| Median level across the 50 lines | 69.38 CPM |
| Lines where detected | 50 of 50 |
| Readthrough geometry | no same-strand neighbour close enough to spill into it |

### What p53 does to it

| | |
|---|---|
| Direction | **induced by p53** |
| Source of the direction | data: the program arm it was selected into |
| Program arm | P up (WT-selective induction) |
| Rank in the program | 147 of 195 by p53 induction |
| Fold change under p53 activators, WT lines | 1.123× |
| Wild-type minus altered | 1.063× |
| Compounds moving it up in WT lines | 67 of 98 |
| Direction mixed? | no |
| Program membership stability | partial (2-3 of 5) |

> [!warning] These columns are circular
> Program membership, rank and the fold change were all selected using the TP53 genotype
> labels, so they describe the gene but cannot be used to argue about p53-specificity.

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.02205 |
| As a percentage | +1.54% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.02740 / 0.01880 |
| Verdict | up with MG53 |
| **Signed into p53-output units** | **toward MORE p53 output** |
| Co-regulation with MG53 across exposures (r) | 0.589 raw, 0.361 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 83 targets |
| Activity vs MG53 across exposures (r) | 0.171 (q 9.47e-07) |
| With 3 principal components removed | 0.160 (q 2.35e-06) |
| Within line, across exposures (r) | -0.007 (q 0.697) |
| Percentile against all genes | 87.8 |

## Links

- **Concepts:** [[The p53 pathway]], [[p53 program P]], [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** p53 program, induction arm
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
