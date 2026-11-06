---
symbol: PYGM
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [GSD5]
gene_name: glycogen phosphorylase, muscle associated
locus: 11q13.1
locus_type: gene with protein product
gene_family: [Glycogen phosphorylases]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# PYGM

*glycogen phosphorylase, muscle associated* — 11q13.1

> [!summary] In one line
> PYGM encodes muscle glycogen phosphorylase, the enzyme that releases glucose-1-phosphate from glycogen in skeletal muscle; its loss causes McArdle disease.

## What it is

One of the classical allosteric enzymes: a pyridoxal-phosphate-dependent homodimer, switched on covalently by phosphorylase kinase downstream of calcium and adrenergic signalling, and tuned allosterically by AMP and ATP. It is the muscle-specific member of a three-gene family, with liver PYGL and brain PYGB, and supplies the glycolytic flux that powers burst exercise. Recessive loss of function causes glycogen storage disease type V, McArdle disease: exercise intolerance, cramps, rhabdomyolysis, and the characteristic "second wind" as the body switches to oxidative fuel. The biochemistry is unusually well settled for a gene this specialised; the gene's own transcriptional control outside muscle differentiation has had little attention.

## Why it appears in this work

PYGM is one of the strongest genome-wide correlates of measured [[MG53 (TRIM72)]], and it is, like MG53, a skeletal-muscle gene. The tempting reading is a shared myogenic program — but the muscle master regulators [[MYOD1]] and [[MYOG]] fall below the atlas's expression floor in these lines, so there is no detectable myogenic program for the two genes to share.

## What is uncertain

Both are muscle transcripts detected at a trickle in non-muscle lines, so almost anything that shifts detection of one lowly expressed gene shifts the other: sequencing depth, ambient RNA, drug-induced changes in total RNA content. PYGM also carries the readthrough-geometry flag — it sits a short distance 3' of a much higher-expressed same-strand gene, so part of what is counted as PYGM may be its neighbour's transcription ([[Readthrough spillover]]). Measured MG53 has the same vulnerability ([[Why MG53 is hard to measure here]]), so nothing here separates co-regulation from co-measurement.

## References

- Tsujino et al., 1993, New England Journal of Medicine — identified mutations in muscle glycogen phosphorylase as the cause of McArdle disease.
- Nogales-Gadea et al., 2015, Human Mutation — curated the reported PYGM mutation spectrum in McArdle disease.

## What is on record

| | |
|---|---|
| Official name | glycogen phosphorylase, muscle associated |
| Also known as | GSD5, McArdle syndrome, glycogen storage disease type V, glycogen phosphorylase, muscle form, myophosphorylase |
| Locus | 11q13.1 — gene with protein product |
| Gene families | Glycogen phosphorylases |
| Previously named | phosphorylase, glycogen; muscle |

**Function**, from UniProt [P11217](https://www.uniprot.org/uniprotkb/P11217) (reviewed):

> Allosteric enzyme that catalyzes the rate-limiting step in glycogen catabolism, the phosphorolytic cleavage of glycogen to produce glucose-1-phosphate, and plays a central role in maintaining cellular and organismal glucose homeostasis

**Summary**, from NCBI Gene [5837](https://www.ncbi.nlm.nih.gov/gene/5837):

> This gene encodes a muscle enzyme involved in glycogenolysis. Highly similar enzymes encoded by different genes are found in liver and brain. Mutations in this gene are associated with McArdle disease (myophosphorylase deficiency), a glycogen storage disease of muscle. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Sep 2009]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:9726](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9726) · Entrez [5837](https://www.ncbi.nlm.nih.gov/gene/5837) · UniProt [P11217](https://www.uniprot.org/uniprotkb/P11217) · Ensembl [ENSG00000068976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000068976) · OMIM [608455](https://www.omim.org/entry/608455)

**PubMed**, as HGNC records for this gene — [2461546](https://pubmed.ncbi.nlm.nih.gov/2461546/), [25914343](https://pubmed.ncbi.nlm.nih.gov/25914343/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.09703 |
| As a percentage | +6.96% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09818 / 0.09633 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.668 raw, 0.699 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

## Links

- **Concepts:** [[The p53 pathway]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** tracks MG53 genome-wide
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
