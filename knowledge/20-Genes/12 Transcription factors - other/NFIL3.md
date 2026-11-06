---
symbol: NFIL3
type: gene
tier: 2
pathway_role: transcription factor
aliases: [E4BP4, NFIL3A, NF-IL3A]
gene_name: nuclear factor, interleukin 3 regulated
locus: 9q22.31
locus_type: gene with protein product
gene_family: [Basic leucine zipper proteins]
family_siblings_here: [CREBRF, XBP1]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# NFIL3

*nuclear factor, interleukin 3 regulated* — 9q22.31

> [!summary] In one line
> NFIL3 encodes E4BP4, a bZIP transcription factor that represses D-box promoter elements by competing with the PAR-family activators for the same sites.

## What it is

NFIL3 belongs to the proline- and acidic-amino-acid-rich (PAR) branch of the bZIP family but lacks the PAR activation domain its relatives carry, so it binds the shared D-box consensus and represses rather than activates. Its abundance oscillates in antiphase to DBP, HLF and TEF, and that competition is part of the circadian oscillator, with PER1 and PER2 among the repressed targets. It was isolated twice under different names — as E4BP4, a repressor of the adenovirus E4 promoter, and as an interleukin-3-regulated factor in haematopoietic survival. Its best-established requirement is developmental: Nfil3-deficient mice lack mature natural killer cells, and the factor acts early in the innate lymphoid lineage.

## Why it appears in this work

NFIL3 is one of the factors scored in the regulon-based activity step. For a reader of this study the question is whether an inferred factor could account for MG53's movement; a D-box repressor would do so by a route separate from p53, and showing it would need a D-box in the TRIM72 promoter, which has not been reported. See [[Transcription factor activity inference]].

## What is uncertain

Its regulon here is small, and its targets were curated largely from circadian and mouse lymphoid systems rather than epithelial tumour cells, so coherent movement need not report NFIL3. Because it represses, the direction of its inferred activity depends on sign conventions applied inconsistently to repressors. And unsynchronised proliferating cultures have scrambled circadian phase, removing the context in which D-box coherence is interpretable.

## References

- Cowell et al., 1992, Molecular and Cellular Biology — identified E4BP4 as a bZIP transcriptional repressor.
- Mitsui et al., 2001, Genes & Development — showed E4BP4 and the PAR activators act antagonistically at D-boxes in the circadian oscillator.
- Gascoyne et al., 2009, Nature Immunology — E4BP4 is essential for natural killer cell development.
- Kamizono et al., 2009, Journal of Experimental Medicine — Nfil3/E4bp4 is required for NK cell development and maturation in vivo.

## What is on record

| | |
|---|---|
| Official name | nuclear factor, interleukin 3 regulated |
| Also known as | E4BP4, NFIL3A, NF-IL3A, E4 promoter-binding protein, adenovirus E4 promoter region binding protein |
| Locus | 9q22.31 — gene with protein product |
| Gene families | Basic leucine zipper proteins |
| Other genes here in those families | [[CREBRF]], [[XBP1]] |
| Previously named | interleukin-3 binding protein 1 |

**Function**, from UniProt [Q16649](https://www.uniprot.org/uniprotkb/Q16649) (reviewed):

> Acts as a transcriptional regulator that recognizes and binds to the sequence 5'-[GA]TTA[CT]GTAA[CT]-3', a sequence present in many cellular and viral promoters. Represses transcription from promoters with activating transcription factor (ATF) sites. Represses promoter activity in osteoblasts (By similarity). Represses transcriptional activity of PER1 (By similarity). Represses transcriptional activity of PER2 via the B-site on the promoter (By similarity). Activates transcription from the interleukin-3 promoter in T-cells. Competes for the same consensus-binding site with PAR DNA-binding factors (DBP, HLF and TEF) (By similarity). Component of the circadian clock that acts as a negative regulator for the circadian expression of PER2 oscillation in the cell-autonomous core clock (By similarity). Protects pro-B cells from programmed cell death (By similarity). Represses the transcription of CYP2A5 (By similarity). Positively regulates the expression and activity of CES2 by antagonizing the repressive action of NR1D1 on CES2 (By similarity). Required for the development of natural killer cell precursors (By similarity)

**Summary**, from NCBI Gene [4783](https://www.ncbi.nlm.nih.gov/gene/4783):

> The protein encoded by this gene is a transcriptional regulator that binds as a homodimer to activating transcription factor (ATF) sites in many cellular and viral promoters. The encoded protein represses PER1 and PER2 expression and therefore plays a role in the regulation of circadian rhythm. Three transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Feb 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:7787](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7787) · Entrez [4783](https://www.ncbi.nlm.nih.gov/gene/4783) · UniProt [Q16649](https://www.uniprot.org/uniprotkb/Q16649) · Ensembl [ENSG00000165030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165030) · OMIM [605327](https://www.omim.org/entry/605327)

**PubMed**, as HGNC records for this gene — [7565758](https://pubmed.ncbi.nlm.nih.gov/7565758/), [1620116](https://pubmed.ncbi.nlm.nih.gov/1620116/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00603 |
| As a percentage | -0.42% |
| FDR, exposure-shuffle null | 0.1089 |
| In TP53-wild-type lines / altered lines | -0.00360 / -0.00751 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.026 raw, -0.182 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 21 targets |
| Activity vs MG53 across exposures (r) | -0.319 (q 2.07e-19) |
| With 3 principal components removed | -0.289 (q 6.59e-16) |
| Within line, across exposures (r) | -0.030 (q 0.013) |
| Percentile against all genes | 1.1 |

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
