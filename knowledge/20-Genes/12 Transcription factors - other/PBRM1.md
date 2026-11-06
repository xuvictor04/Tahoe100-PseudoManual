---
symbol: PBRM1
type: gene
tier: 2
pathway_role: transcription factor
aliases: [BAF180, PB1, SMARCH1]
gene_name: polybromo 1
locus: 3p21.1
locus_type: gene with protein product
gene_family: [Bromodomain containing, PBAF complex subunits]
family_siblings_here: [CREBBP, EP300]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# PBRM1

*polybromo 1* — 3p21.1

> [!summary] In one line
> PBRM1 encodes BAF180, the subunit that defines the PBAF chromatin-remodelling complex and aims it at acetylated histones.

## What it is

BAF180 is a reader module built at scale: six bromodomains, two BAH domains and an HMG box, which together direct the PBAF form of the SWI/SNF remodelling complex to particular acetylated nucleosomes. It is a tumour suppressor, and in clear-cell renal cell carcinoma the most frequently mutated gene after VHL, usually by truncation; inactivating mutations also occur in breast cancer. Its link to p53 runs through transcription rather than through p53 itself: BAF180 binds the CDKN1A promoter and is required for p21 induction and G1 arrest after TGF-beta and ionising radiation, and BAF180 with BRD7 is needed for p53-dependent transcription of the targets that drive senescence.

## Why it appears in this work

PBRM1 is scored in the regulon-based activity step. The point to carry is that PBAF is a coactivator at a subset of p53 targets, p21 among them, so an inferred PBRM1 activity is not independent of p53's output — it partly re-reads the arm of [[The p53 pathway]] running through [[The p21-DREAM axis]].

## What is uncertain

The regulon here holds only a handful of targets and overlaps p53's own, so the score sits close to a re-reading of [[CDKN1A]] and collinear with [[TP53]]'s. The direction of PBRM1's effect on p21 is not settled either: required for induction where it was first shown, reported as restraining elsewhere, so context decides. mRNA is a weak proxy for a complex subunit whose function depends on assembly and on chromatin acetylation state.

## References

- Xia et al., 2008, Cancer Research — BAF180 binds the p21 promoter and is required for p21 induction and G1 arrest; truncating mutations found in breast cancer.
- Burrows et al., 2010, PNAS — BRD7 and BAF180 are required for p53-dependent transcription of targets driving replicative senescence.
- Varela et al., 2011, Nature — exome sequencing identified PBRM1 as the second major mutated gene in clear-cell renal cell carcinoma.
- Miao et al., 2018, Science — PBRM1 loss-of-function was associated with clinical benefit from immune checkpoint therapy in renal cell carcinoma; later cohorts have not reproduced this consistently.

## What is on record

| | |
|---|---|
| Official name | polybromo 1 |
| Also known as | BAF180, PB1, SMARCH1 |
| Locus | 3p21.1 — gene with protein product |
| Gene families | Bromodomain containing; PBAF complex subunits |
| Other genes here in those families | [[CREBBP]], [[EP300]] |

**Function**, from UniProt [Q86U86](https://www.uniprot.org/uniprotkb/Q86U86) (reviewed):

> Involved in transcriptional activation and repression of select genes by chromatin remodeling (alteration of DNA-nucleosome topology). Required for the stability of the SWI/SNF chromatin remodeling complex SWI/SNF-B (PBAF). Acts as a negative regulator of cell proliferation

**Summary**, from NCBI Gene [55193](https://www.ncbi.nlm.nih.gov/gene/55193):

> This locus encodes a subunit of ATP-dependent chromatin-remodeling complexes. The encoded protein has been identified as in integral component of complexes necessary for ligand-dependent transcriptional activation by nuclear hormone receptors. Mutations at this locus have been associated with primary clear cell renal cell carcinoma. [provided by RefSeq, Feb 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:30064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30064) · Entrez [55193](https://www.ncbi.nlm.nih.gov/gene/55193) · UniProt [Q86U86](https://www.uniprot.org/uniprotkb/Q86U86) · Ensembl [ENSG00000163939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163939) · OMIM [606083](https://www.omim.org/entry/606083)

**PubMed**, as HGNC records for this gene — [11078522](https://pubmed.ncbi.nlm.nih.gov/11078522/), [11483580](https://pubmed.ncbi.nlm.nih.gov/11483580/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | -0.00028 |
| As a percentage | -0.02% |
| FDR, exposure-shuffle null | 0.9165 |
| In TP53-wild-type lines / altered lines | 0.00233 / -0.00186 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | -0.007 raw, 0.174 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 8 targets |
| Activity vs MG53 across exposures (r) | 0.302 (q 1.62e-18) |
| With 3 principal components removed | 0.297 (q 3.55e-18) |
| Within line, across exposures (r) | -0.009 (q 0.527) |
| Percentile against all genes | 99.3 |

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
