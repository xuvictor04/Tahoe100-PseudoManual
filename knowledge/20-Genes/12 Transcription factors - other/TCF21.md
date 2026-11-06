---
symbol: TCF21
type: gene
tier: 2
pathway_role: transcription factor
aliases: [POD1, bHLHa23]
gene_name: transcription factor 21
locus: 6q23.2
locus_type: gene with protein product
gene_family: [Basic helix-loop-helix proteins]
family_siblings_here: [ASCL1, MXI1, MYF5, MYF6, MYOD1, MYOG, TWIST1, TWIST2]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TCF21

*transcription factor 21* — 6q23.2

> [!summary] In one line
> TCF21 is a basic helix-loop-helix transcription factor of mesenchymal lineages — epicardium, kidney and lung mesenchyme, coronary smooth muscle — and a replicated coronary artery disease gene.

## What it is

TCF21, also called capsulin, Pod1 and epicardin, dimerises with E proteins and binds E-boxes. In development it is required for epicardium-derived fibroblasts, podocyte precursors and lung mesenchyme. Its best-worked adult role is in the artery wall: common variants at the locus are among the strongest coronary artery disease associations, and in coronary smooth muscle cells TCF21 drives the shift from contractile cells to fibroblast-like fibromyocytes, lowering smooth muscle markers and the myocardin-SRF axis — apparently protectively in that disease. Separately, its promoter is hypermethylated and the gene silenced in lung and head and neck carcinomas.

## Why it appears in this work

TCF21 ranks at the negative extreme of the factor-activity correlation. Its one mechanistic contact with this study is that it antagonises [[SRF]] and myocardin, and SRF is the candidate native-tissue regulator of [[MG53 (TRIM72)]] here, so an opposing sign is at least consistent — a thin thing to lean on. See [[Transcription factor activity inference]].

## What is uncertain

TCF21 carries the smallest regulon of any factor in this batch, so its position at the extreme is close to what a handful of transcripts can produce unaided. The myocardin-SRF antagonism was characterised in smooth muscle, not in epithelial lines where myocardin is absent and TCF21's own transcript is often low or methylated. The tumour-suppressor reading rests mainly on methylation surveys rather than functional rescue.

## References

- Wirka et al., 2019, Nature Medicine — single-cell analysis linking TCF21 to smooth muscle phenotypic modulation into fibromyocytes and to lower coronary disease risk.
- Nagao et al., 2019, Circulation Research — TCF21 inhibits smooth muscle differentiation by blocking the myocardin-SRF pathway.
- Smith et al., 2006, PNAS — TCF21 at 6q23-q24 is aberrantly methylated and silenced in lung and head and neck cancer.

## What is on record

| | |
|---|---|
| Official name | transcription factor 21 |
| Also known as | POD1, bHLHa23 |
| Locus | 6q23.2 — gene with protein product |
| Gene families | Basic helix-loop-helix proteins |
| Other genes here in those families | [[ASCL1]], [[MXI1]], [[MYF5]], [[MYF6]], [[MYOD1]], [[MYOG]], [[TWIST1]], [[TWIST2]] |

**Function**, from UniProt [O43680](https://www.uniprot.org/uniprotkb/O43680) (reviewed):

> Involved in epithelial-mesenchymal interactions in kidney and lung morphogenesis that include epithelial differentiation and branching morphogenesis. May play a role in the specification or differentiation of one or more subsets of epicardial cell types

**Summary**, from NCBI Gene [6943](https://www.ncbi.nlm.nih.gov/gene/6943):

> TCF21 encodes a transcription factor of the basic helix-loop-helix family. The TCF21 product is mesoderm specific, and expressed in embryonic epicardium, mesenchyme-derived tissues of lung, gut, gonad, and both mesenchymal and glomerular epithelial cells in the kidney. Two transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Jul 2008]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:11632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11632) · Entrez [6943](https://www.ncbi.nlm.nih.gov/gene/6943) · UniProt [O43680](https://www.uniprot.org/uniprotkb/O43680) · Ensembl [ENSG00000118526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118526) · OMIM [603306](https://www.omim.org/entry/603306)

**PubMed**, as HGNC records for this gene — [9507058](https://pubmed.ncbi.nlm.nih.gov/9507058/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 9 targets |
| Activity vs MG53 across exposures (r) | -0.210 (q 9.67e-10) |
| With 3 principal components removed | -0.196 (q 1.65e-08) |
| Within line, across exposures (r) | -0.011 (q 0.314) |
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
