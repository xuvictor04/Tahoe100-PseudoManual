---
symbol: SIX1
type: gene
tier: 2
pathway_role: transcription factor
gene_name: SIX homeobox 1
locus: 14q23.1
locus_type: gene with protein product
gene_family: [SINE class homeoboxes]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# SIX1

*SIX homeobox 1* — 14q23.1

> [!summary] In one line
> SIX1 is a homeodomain transcription factor that, paired with an EYA cofactor, switches from repressor to activator and drives the embryonic muscle, otic and kidney programmes.

## What it is

SIX1 is a vertebrate homologue of Drosophila sine oculis. Bound through its homeodomain and SIX domain it recruits DACH proteins and co-repressors; when an EYA protein joins, the output flips to activation, EYA's phosphatase activity being part of the switch. The SIX1-EYA module sits near the top of the skeletal muscle hierarchy, required for normal PAX3 and myogenic-regulatory-factor expression and later for the fast-twitch programme, and it also builds the otic and nephric lineages — mutations disrupting the EYA1-SIX1-DNA interface cause branchio-oto-renal syndrome. In carcinomas it is often overexpressed and reported to promote epithelial-mesenchymal transition.

## Why it appears in this work

SIX1 is a native regulator of the muscle programme [[MG53 (TRIM72)]] belongs to, upstream of [[MYOD1]], [[MYF5]] and the MEF2 factors — but unlike the rest of that programme it is expressed in epithelial tumours, so it is one of few muscle-lineage factors that could act here. See [[Transcription factor activity inference]].

## What is uncertain

Its regulon here is among the smallest scored, so the score is near an average over a handful of transcripts, and small regulons reach a ranking's extremes cheaply. Those targets come from myogenic work, the context these lines lack, so what moved may belong to other regulators. No SIX element has been described at TRIM72; the characterised site there is a MEF2 element beside an E-box.

## References

- Ruf et al., 2004, PNAS — SIX1 mutations cause branchio-oto-renal syndrome by disrupting EYA1-SIX1-DNA complexes.
- Li et al., 2003, Nature — EYA phosphatase activity converts the SIX1-DACH-EYA complex from repression to activation.
- Grifone et al., 2005, Development — Six1 and Six4 are required for Pax3 and myogenic regulatory factor expression during myogenesis.
- Laclef et al., 2003, Development — Six1-null mice show altered myogenesis and muscle patterning defects.
- Micalizzi et al., 2009, Journal of Clinical Investigation — SIX1 overexpression promotes epithelial-mesenchymal transition via TGF-beta signalling.

## What is on record

| | |
|---|---|
| Official name | SIX homeobox 1 |
| Also known as | — (no recorded alias) |
| Locus | 14q23.1 — gene with protein product |
| Gene families | SINE class homeoboxes |
| Previously named | sine oculis homeobox (Drosophila) homolog 1; sine oculis homeobox homolog 1 (Drosophila); deafness, autosomal dominant 23 |

**Function**, from UniProt [Q15475](https://www.uniprot.org/uniprotkb/Q15475) (reviewed):

> Transcription factor that is involved in the regulation of cell proliferation, apoptosis and embryonic development (By similarity). Plays an important role in the development of several organs, including kidney, muscle and inner ear (By similarity). Depending on context, functions as a transcriptional repressor or activator (By similarity). Lacks an activation domain, and requires interaction with EYA family members for transcription activation (PubMed:15141091). Mediates nuclear translocation of EYA1 and EYA2 (PubMed:19497856). Binds the 5'-TCA[AG][AG]TTNC-3' motif present in the MEF3 element in the MYOG promoter and CIDEA enhancer (PubMed:15141091, PubMed:19497856, PubMed:23435380, PubMed:27923061). Regulates the expression of numerous genes, including MYC, CCND1 and EZR (By similarity). Acts as an activator of the IGFBP5 promoter, probably coactivated by EYA2 (By similarity). Repression of precursor cell proliferation in myoblasts is switched to activation through recruitment of EYA3 to the SIX1-DACH1 complex (By similarity). During myogenesis, seems to act together with EYA2 and DACH2 (By similarity). Regulates the expression of CCNA1 (PubMed:15123840). Promotes brown adipocyte differentiation (By similarity)

**Summary**, from NCBI Gene [6495](https://www.ncbi.nlm.nih.gov/gene/6495):

> The protein encoded by this gene is a homeobox protein that is similar to the Drosophila 'sine oculis' gene product. This gene is found in a cluster of related genes on chromosome 14 and is thought to be involved in limb development. Defects in this gene are a cause of autosomal dominant deafness type 23 (DFNA23) and branchiootic syndrome type 3 (BOS3). [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:10887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10887) · Entrez [6495](https://www.ncbi.nlm.nih.gov/gene/6495) · UniProt [Q15475](https://www.uniprot.org/uniprotkb/Q15475) · Ensembl [ENSG00000126778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126778) · OMIM [601205](https://www.omim.org/entry/601205)

**PubMed**, as HGNC records for this gene — [8617500](https://pubmed.ncbi.nlm.nih.gov/8617500/), [15141091](https://pubmed.ncbi.nlm.nih.gov/15141091/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00642 |
| As a percentage | +0.45% |
| FDR, exposure-shuffle null | 0.2553 |
| In TP53-wild-type lines / altered lines | 0.00745 / 0.00578 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.208 raw, 0.025 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 13 targets |
| Activity vs MG53 across exposures (r) | 0.282 (q 6.61e-17) |
| With 3 principal components removed | 0.385 (q 2.71e-29) |
| Within line, across exposures (r) | 0.013 (q 0.297) |
| Percentile against all genes | 98.3 |

## Links

- **Concepts:** [[Transcription factor activity inference]]
- **Findings:** [[Downstream of MG53]], [[Upstream of MG53]]
- **Why this gene is in the vault:** transcription factor, positive rank
- **Indexes:** [[Genes — Map of Content]]

## Sources

- Registry annotation: `knowledge/_build/annotations.json`, fetched from HGNC, NCBI Gene and UniProt by `knowledge/_build/fetch_annotations.py`
- Program and MG53 columns: `mg53_p53/findings/tables/tableD_p53_target_genes.csv`
- Genome-wide screen: `genome_wide/tables/c_screen_genes.csv.gz`
- Curated effector columns: `mg53_p53/findings/tables/p53_effectors_per_gene.csv`
- Transcription-factor activity: `upstream_tf/tables/a1a2_tf_summary.csv`
