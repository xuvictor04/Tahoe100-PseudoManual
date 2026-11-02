---
symbol: CREBBP
type: gene
tier: 2
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# CREBBP

> [!summary] In one line
> CREBBP encodes CBP, a lysine acetyltransferase and transcriptional coactivator that many DNA-binding factors — p53 among them — depend on to reach chromatin.

## What it is

CBP and its paralogue p300 share a domain layout built for brokering: TAZ1 and TAZ2 zinc-binding regions, a KIX domain, a bromodomain and a central acetyltransferase. CBP acetylates histones — H3K27 at active enhancers — and many non-histone substrates, including lysines in the p53 C-terminus, where acetylation stabilises p53 on DNA and raises target induction. Because CBP is shared among many pathways and limited in amount, competition for it is regulatory. Germline heterozygous loss causes Rubinstein-Taybi syndrome; somatic inactivating mutations are frequent in B-cell lymphoma, relapsed acute lymphoblastic leukaemia and bladder cancer. CBP and p300 are partly redundant.

## Why it appears in this work

CREBBP is scored in the regulon-based activity step and ranks near the top. The point to hold onto: CBP is not a sequence-specific factor but a coactivator, so its regulon collects whatever its partners drive. Being also a p53 coactivator, its inferred activity is not independent of p53's output. See [[Transcription factor activity inference]] and [[The p53 pathway]].

## What is uncertain

Whether "CREBBP activity" is meaningful here is the first question. Its regulon in this collection is small and heterogeneous, so a coherent rise across it may report general enhancer acetylation rather than anything CBP-specific — which is also why its score is collinear with [[TP53]] and [[EP300]]. CBP mRNA is a poor proxy for function, since the biology is competition at the protein level. No link between CBP and the TRIM72 promoter is reported.

## References

- Petrij et al., 1995, Nature — mutations in CBP cause Rubinstein-Taybi syndrome.
- Gu & Roeder, 1997, Cell — acetylation of the p53 C-terminal domain by p300 activates its sequence-specific DNA binding.
- Avantaggiati et al., 1997, Cell — p300/CBP is recruited into p53-dependent transcriptional responses.
- Pasqualucci et al., 2011, Nature — recurrent inactivating mutations of CREBBP and EP300 in B-cell lymphoma.
- Mullighan et al., 2011, Nature — CREBBP mutations are enriched at relapse in acute lymphoblastic leukaemia.

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00232 |
| As a percentage | +0.16% |
| FDR, exposure-shuffle null | 0.2778 |
| In TP53-wild-type lines / altered lines | 0.00072 / 0.00329 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.104 raw, 0.233 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 29 targets |
| Activity vs MG53 across exposures (r) | 0.315 (q 8.44e-20) |
| With 3 principal components removed | 0.265 (q 1.67e-14) |
| Within line, across exposures (r) | 0.010 (q 0.534) |
| Percentile against all genes | 98.8 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, positive rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
