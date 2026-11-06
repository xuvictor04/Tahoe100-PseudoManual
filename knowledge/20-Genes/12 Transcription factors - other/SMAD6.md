---
symbol: SMAD6
type: gene
tier: 2
pathway_role: transcription factor
aliases: [HsT17432]
gene_name: SMAD family member 6
locus: 15q22.31
locus_type: gene with protein product
gene_family: [SMAD family]
family_siblings_here: [SMAD4, SMAD5]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# SMAD6

*SMAD family member 6* — 15q22.31

> [!summary] In one line
> SMAD6 is an inhibitory SMAD: a BMP-induced brake that blocks signalling through its own pathway rather than transmitting it.

## What it is

SMAD6 and SMAD7 lack the C-terminal SSXS motif that makes receptor SMADs phosphorylation substrates, and work as antagonists. SMAD6 acts mainly on the BMP branch: it competes with [[SMAD4]] for binding to activated SMAD1, and recruits the ubiquitin ligase SMURF1 to receptors and SMADs. It is a BMP target gene, which closes a negative-feedback loop. A nuclear repressor role is also reported, with MH1-like DNA binding and recruitment of CtBP and histone deacetylases. Smad6-null mice have valve and outflow-tract defects, and rare human loss-of-function variants are associated with craniosynostosis and bicuspid aortic valve.

## Why it appears in this work

SMAD6 is scored as a transcription factor here and ranks at the negative extreme of the correlation with measured MG53. That direction is only interesting if the regulon means what it claims: a brake's inferred activity reads as the inverse of BMP tone, not as SMAD6 occupying promoters. See [[Transcription factor activity inference]].

## What is uncertain

SMAD6 is a weak case for regulon-based inference. It is not a classical sequence-specific activator; its direct DNA binding is reported in few systems, and most of its output is indirect, through sequestration and degradation. The curated target set is small and its signs are inherited from BMP-response experiments, so the inferred activity is as likely to report BMP tone as SMAD6. No link between SMAD6 and TRIM72 has been reported.

## References

- Imamura et al., 1997, Nature — identified Smad6 as an inhibitor of signalling by the TGF-beta superfamily.
- Hata et al., 1998, Genes & Development — Smad6 inhibits BMP/Smad1 signalling by competing with SMAD4.
- Galvin et al., 2000, Nature Genetics — Smad6-null mice show cardiovascular developmental defects.
- Timberlake et al., 2016, eLife — rare SMAD6 loss-of-function variants with a common BMP2 risk allele in midline craniosynostosis.

## What is on record

| | |
|---|---|
| Official name | SMAD family member 6 |
| Also known as | HsT17432 |
| Locus | 15q22.31 — gene with protein product |
| Gene families | SMAD family |
| Other genes here in those families | [[SMAD4]], [[SMAD5]] |
| Previously named | MAD, mothers against decapentaplegic homolog 6 (Drosophila); SMAD, mothers against DPP homolog 6 (Drosophila) |

**Function**, from UniProt [O43541](https://www.uniprot.org/uniprotkb/O43541) (reviewed):

> Acts as an inhibitory regulator of signaling mediated by the TGF-beta superfamily, with strong selectivity toward BMP-dependent pathways (PubMed:10647776, PubMed:10708948, PubMed:10708949, PubMed:16951688, PubMed:22275001, PubMed:30848080, PubMed:9436979, PubMed:9759503). Suppresses IL1R-TLR signaling through its direct interaction with PEL1, preventing NF-kappa-B activation, nuclear translocation and NF-kappa-B-mediated expression of pro-inflammatory genes (PubMed:16951688). Blocks the BMP-SMAD1 signaling pathway by competing with SMAD4 for receptor-activated SMAD1-binding (PubMed:30848080, PubMed:9436979). Associates with regulatory elements in target promoter regions (PubMed:16491121). Functions as an adapter protein that recruits ubiquitin ligases, including SMURF1 and, in some contexts, SMURF2, promoting proteasomal degradation of signaling components and transcription factors such as RUNX2, TBX6, BMPR1A and MYD88 (PubMed:16299379, PubMed:19561075, PubMed:28847510)

**Summary**, from NCBI Gene [4091](https://www.ncbi.nlm.nih.gov/gene/4091):

> The protein encoded by this gene belongs to the SMAD family of proteins, which are related to Drosophila 'mothers against decapentaplegic' (Mad) and C. elegans Sma. SMAD proteins are signal transducers and transcriptional modulators that mediate multiple signaling pathways. This protein functions in the negative regulation of BMP and TGF-beta/activin-signalling. Multiple transcript variants have been found for this gene.[provided by RefSeq, Sep 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:6772](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6772) · Entrez [4091](https://www.ncbi.nlm.nih.gov/gene/4091) · UniProt [O43541](https://www.uniprot.org/uniprotkb/O43541) · Ensembl [ENSG00000137834](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137834) · OMIM [602931](https://www.omim.org/entry/602931)

**PubMed**, as HGNC records for this gene — [9256479](https://pubmed.ncbi.nlm.nih.gov/9256479/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00330 |
| As a percentage | +0.23% |
| FDR, exposure-shuffle null | 0.6484 |
| In TP53-wild-type lines / altered lines | 0.00206 / 0.00411 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.340 raw, 0.001 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 18 targets |
| Activity vs MG53 across exposures (r) | -0.263 (q 2.34e-13) |
| With 3 principal components removed | -0.248 (q 5.05e-12) |
| Within line, across exposures (r) | -0.017 (q 0.150) |
| Percentile against all genes | 2.0 |

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
