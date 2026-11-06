---
symbol: NAB2
type: gene
tier: 2
pathway_role: transcription factor
aliases: [MADER]
gene_name: NGFI-A binding protein 2
locus: 12q13.3
locus_type: gene with protein product
gene_family: [NGFI-A binding protein family]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# NAB2

*NGFI-A binding protein 2* — 12q13.3

> [!summary] In one line
> NAB2 encodes a transcriptional corepressor with no DNA-binding domain of its own, acting through EGR-family factors to shut down their output.

## What it is

NAB2 — NGFI-A-binding protein 2, also known as EGR1-binding protein 2 or MADER — was isolated as a repressor of NGFI-A (EGR1) and Krox20 (EGR2). Its first conserved domain binds the R1 region of NGFI-A, and repression is carried out at least partly by recruiting the CHD4 subunit of the NuRD remodelling and deacetylase complex. The circuit is a feedback loop: EGR factors bind sites in the NAB2 promoter and induce it, so NAB2 accumulates after the immediate-early burst and terminates it. The gene sits at 12q13.3, where a recurrent NAB2-STAT6 fusion defines solitary fibrous tumour.

## Why it appears in this work

NAB2 is scored as a factor in the regulon-based activity step. The thing to hold onto is that it has no targets of its own: its regulon is borrowed from EGR, so "NAB2 activity" is an immediate-early readout with an inverted sign. See [[Transcription factor activity inference]].

## What is uncertain

Its regulon in this collection holds only a handful of targets, which puts the score close to a single-gene measurement; and because NAB2 represses, whether coherent movement in those targets means high or low activity depends on sign conventions the collections apply inconsistently to repressors. Immediate-early signalling is also moved by the stress and translation-inhibiting compounds that drive [[Readthrough spillover]]. One practical trap: the yeast protein Nab2 is an unrelated poly(A)-RNA-binding protein, and much of what a literature search returns under this name concerns that.

## References

- Svaren et al., 1996, Molecular and Cellular Biology — identified NAB2 as a corepressor of NGFI-A and Krox20 induced by proliferative and differentiative stimuli.
- Robinson et al., 2013, Nature Genetics — identified recurrent NAB2-STAT6 fusions in solitary fibrous tumour.
- Chmielecki et al., 2013, Nature Genetics — independently found the recurrent NAB2-STAT6 fusion in solitary fibrous tumours.

## What is on record

| | |
|---|---|
| Official name | NGFI-A binding protein 2 |
| Also known as | MADER, EGR1 binding protein 2 |
| Locus | 12q13.3 — gene with protein product |
| Gene families | NGFI-A binding protein family |
| Previously named | NGFI-A binding protein 2 (EGR1 binding protein 2) |

**Function**, from UniProt [Q15742](https://www.uniprot.org/uniprotkb/Q15742) (reviewed):

> Acts as a transcriptional repressor for zinc finger transcription factors EGR1 and EGR2. Isoform 2 lacks repression ability (By similarity)

**Summary**, from NCBI Gene [4665](https://www.ncbi.nlm.nih.gov/gene/4665):

> This gene encodes a member of the family of NGFI-A binding (NAB) proteins, which function in the nucleus to repress transcription induced by some members of the EGR (early growth response) family of transactivators. NAB proteins can homo- or hetero-multimerize with other EGR or NAB proteins through a conserved N-terminal domain, and repress transcription through two partially redundant C-terminal domains. Transcriptional repression by the encoded protein is mediated in part by interactions with the nucleosome remodeling and deactylase (NuRD) complex. Alternatively spliced transcript variants have been described, but their biological validity has not been determined. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7627](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7627) · Entrez [4665](https://www.ncbi.nlm.nih.gov/gene/4665) · UniProt [Q15742](https://www.uniprot.org/uniprotkb/Q15742) · Ensembl [ENSG00000166886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166886) · OMIM [602381](https://www.omim.org/entry/602381)

**PubMed**, as HGNC records for this gene — [8668170](https://pubmed.ncbi.nlm.nih.gov/8668170/), [8649813](https://pubmed.ncbi.nlm.nih.gov/8649813/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00297 |
| As a percentage | -0.21% |
| FDR, exposure-shuffle null | 0.6468 |
| In TP53-wild-type lines / altered lines | -0.00355 / -0.00260 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.194 raw, 0.019 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 6 targets |
| Activity vs MG53 across exposures (r) | -0.377 (q 8.88e-28) |
| With 3 principal components removed | -0.365 (q 5.93e-27) |
| Within line, across exposures (r) | -0.066 (q 0.004) |
| Percentile against all genes | 0.6 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, negative rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
