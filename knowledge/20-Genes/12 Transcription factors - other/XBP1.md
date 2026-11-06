---
symbol: XBP1
type: gene
tier: 2
pathway_role: transcription factor
gene_name: X-box binding protein 1
locus: 22q12.1
locus_type: gene with protein product
gene_family: [Basic leucine zipper proteins]
family_siblings_here: [CREBRF, NFIL3]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# XBP1

*X-box binding protein 1* — 22q12.1

> [!summary] In one line
> XBP1 is the bZIP transcription factor of the IRE1 branch of the unfolded protein response, switched on not by transcription but by unconventional cytoplasmic splicing of its own mRNA.

## What it is

Under ER stress the kinase/endoribonuclease IRE1-alpha excises a 26-nucleotide intron from XBP1 mRNA; the frameshifted product, XBP1s, is a potent activator that induces ER chaperones, ERAD components and lipid-biosynthesis genes to expand secretory capacity. The unspliced form, XBP1u, encodes a short-lived protein that negatively regulates XBP1s and ATF6. The decisive step is therefore post-transcriptional, unusual among mammalian transcription factors and consequential for anything inferred from expression. XBP1 is essential for plasma-cell differentiation, where secretory load drives the pathway constitutively; in cancer it supports survival under hypoxia and proteotoxic stress, and IRE1/XBP1 is an active drug target in myeloma.

## Why it appears in this work

XBP1 scores high in the transcription-factor step. ER stress is among the most generic consequences of drug exposure, so XBP1 sits near the centre of whatever stress response this panel shares. The useful inference is almost the opposite of a mechanism: the IRE1-XBP1 axis is a strong candidate for exactly the broad, compound-spanning variation that the principal-component adjustment exists to absorb. See [[Transcription factor activity inference]] and [[Tahoe-100M]].

## What is uncertain

Gene-level counts cannot distinguish XBP1u from XBP1s: the two differ by 26 nucleotides and standard quantification collapses them, so XBP1's measured level says little about whether the pathway is on. The regulon score sidesteps this by reading targets instead, but those overlap heavily with [[ATF4]]-, ATF6- and NRF2-driven programmes, so attributing them to XBP1 specifically is weak. Reported links between XBP1 and p53 are not consistent across systems, and nothing here tests them.

## References

- Yoshida et al., 2001, Cell — showed XBP1 mRNA is spliced by IRE1 to produce the active transcription factor.
- Calfon et al., 2002, Nature — showed IRE1 couples ER stress to XBP1 processing and ER chaperone induction.
- Reimold et al., 2001, Nature — XBP1 is required for plasma-cell differentiation.
- Chen et al., 2014, Nature — XBP1 supports triple-negative breast cancer survival under hypoxic stress.

## What is on record

| | |
|---|---|
| Official name | X-box binding protein 1 |
| Also known as | — (no recorded alias) |
| Locus | 22q12.1 — gene with protein product |
| Gene families | Basic leucine zipper proteins |
| Other genes here in those families | [[CREBRF]], [[NFIL3]] |

**Function**, from UniProt [P17861](https://www.uniprot.org/uniprotkb/P17861) (reviewed):

> Functions as a transcription factor during endoplasmic reticulum (ER) stress by regulating the unfolded protein response (UPR). Required for cardiac myogenesis and hepatogenesis during embryonic development, and the development of secretory tissues such as exocrine pancreas and salivary gland (By similarity). Involved in terminal differentiation of B lymphocytes to plasma cells and production of immunoglobulins (PubMed:11460154). Modulates the cellular response to ER stress in a PIK3R-dependent manner (PubMed:20348923). Binds to the cis-acting X box present in the promoter regions of major histocompatibility complex class II genes (PubMed:8349596). Involved in VEGF-induced endothelial cell (EC) proliferation and retinal blood vessel formation during embryonic development but also for angiogenesis in adult tissues under ischemic conditions. Also functions as a major regulator of the UPR in obesity-induced insulin resistance and type 2 diabetes for the management of obesity and diabetes prevention (By similarity)

**Summary**, from NCBI Gene [7494](https://www.ncbi.nlm.nih.gov/gene/7494):

> This gene encodes a transcription factor that regulates MHC class II genes by binding to a promoter element referred to as an X box. This gene product is a bZIP protein, which was also identified as a cellular transcription factor that binds to an enhancer in the promoter of the T cell leukemia virus type 1 promoter. It may increase expression of viral proteins by acting as the DNA binding partner of a viral transactivator. It has been found that upon accumulation of unfolded proteins in the endoplasmic reticulum (ER), the mRNA of this gene is processed to an active form by an unconventional splicing mechanism that is mediated by the endonuclease inositol-requiring enzyme 1 (IRE1). The resulting loss of 26 nt from the spliced mRNA causes a frame-shift and an isoform XBP1(S), which is the functionally active transcription factor. The isoform encoded by the unspliced mRNA, XBP1(U), is constitutively expressed, and thought to function as a negative feedback regulator of XBP1(S), which shuts off transcription of target genes during the recovery phase of ER stress. A pseudogene of XBP1 has been identified and localized to chromosome 5. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:12801](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12801) · Entrez [7494](https://www.ncbi.nlm.nih.gov/gene/7494) · UniProt [P17861](https://www.uniprot.org/uniprotkb/P17861) · Ensembl [ENSG00000100219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100219) · OMIM [194355](https://www.omim.org/entry/194355)

**PubMed**, as HGNC records for this gene — [1718857](https://pubmed.ncbi.nlm.nih.gov/1718857/), [2196176](https://pubmed.ncbi.nlm.nih.gov/2196176/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00072 |
| As a percentage | +0.05% |
| FDR, exposure-shuffle null | 0.8442 |
| In TP53-wild-type lines / altered lines | -0.00198 / 0.00229 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.044 raw, 0.262 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 42 targets |
| Activity vs MG53 across exposures (r) | 0.295 (q 3.21e-17) |
| With 3 principal components removed | 0.355 (q 4.74e-25) |
| Within line, across exposures (r) | 0.005 (q 0.882) |
| Percentile against all genes | 96.2 |

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
