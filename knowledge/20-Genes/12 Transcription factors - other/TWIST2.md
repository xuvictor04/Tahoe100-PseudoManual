---
symbol: TWIST2
type: gene
tier: 2
pathway_role: transcription factor
aliases: [DERMO1, Dermo-1, bHLHa39]
gene_name: twist family bHLH transcription factor 2
locus: 2q37.3
locus_type: gene with protein product
gene_family: [Basic helix-loop-helix proteins]
family_siblings_here: [ASCL1, MXI1, MYF5, MYF6, MYOD1, MYOG, TCF21, TWIST1]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# TWIST2

*twist family bHLH transcription factor 2* — 2q37.3

> [!summary] In one line
> TWIST2, cloned originally as Dermo-1, is a basic helix-loop-helix protein closely related to TWIST1 that acts in dermal and mesenchymal lineages and was characterised from the start as a repressor rather than an activator.

## What it is

TWIST2 shares TWIST1's bHLH domain almost residue for residue, dimerises with the same E proteins and binds the same E-boxes. It was isolated as Dermo-1 in a two-hybrid screen for E12 partners; notably, the original work found it bound E-boxes with E12 but had no detectable activation capacity, repressing myogenic bHLH proteins instead. Expression rises in embryonic and neonatal dermis and falls in adult tissue. Human genetics has been the most informative source since: biallelic loss of function underlies Setleis syndrome, a recessive focal facial dermal dysplasia, while recurrent missense substitutions at one conserved glutamate in the DNA-binding basic domain cause Ablepharon-macrostomia and Barber-Say syndromes — a change of function rather than a loss, with the particular substitution predicting which phenotype appears.

## Why it appears in this work

TWIST2 scores near the top of the transcription-factor activity step, alongside [[TWIST1]]. The honest reading is that the two are one observation, not two: they bind the same motif and are frequently co-expressed. See [[Transcription factor activity inference]].

## What is uncertain

The main caveat is structural rather than biological: TWIST2's regulon overlaps TWIST1's by construction, so the adjacent high ranks are not independent support. Whether TWIST2 has outputs distinct from TWIST1 in any cell type remains partly open: the clean separations come from mouse expression domains and human syndromes, not distinct target sets. If the original characterisation as a repressor without intrinsic activation capacity holds, the activity convention here has the wrong sign for it. The Twist-box/p53 interaction was characterised for TWIST1; the twist box is conserved in TWIST2, but whether it does the same there is not established.

## References

- Li, Cserjesi & Olson, 1995, Developmental Biology — cloned Dermo-1 (TWIST2) as an E12 partner that binds E-boxes without detectable activation and represses myogenic bHLH proteins.
- Marchegiani et al., 2015, American Journal of Human Genetics — recurrent mutations in the basic domain of TWIST2 cause Ablepharon-macrostomia and Barber-Say syndromes.

## What is on record

| | |
|---|---|
| Official name | twist family bHLH transcription factor 2 |
| Also known as | DERMO1, Dermo-1, bHLHa39 |
| Locus | 2q37.3 — gene with protein product |
| Gene families | Basic helix-loop-helix proteins |
| Other genes here in those families | [[ASCL1]], [[MXI1]], [[MYF5]], [[MYF6]], [[MYOD1]], [[MYOG]], [[TCF21]], [[TWIST1]] |
| Previously named | twist homolog 2 (Drosophila); twist basic helix-loop-helix transcription factor 2 |

**Function**, from UniProt [Q8WVJ9](https://www.uniprot.org/uniprotkb/Q8WVJ9) (reviewed):

> Binds to the E-box consensus sequence 5'-CANNTG-3' as a heterodimer and inhibits transcriptional activation by MYOD1, MYOG, MEF2A and MEF2C. Also represses expression of pro-inflammatory cytokines such as TNFA and IL1B. Involved in postnatal glycogen storage and energy metabolism (By similarity). Inhibits the premature or ectopic differentiation of preosteoblast cells during osteogenesis, possibly by changing the internal signal transduction response of osteoblasts to external growth factors

**Summary**, from NCBI Gene [117581](https://www.ncbi.nlm.nih.gov/gene/117581):

> The protein encoded by this gene is a basic helix-loop-helix type transcription factor and shares similarity with Twist. This protein may inhibit osteoblast maturation and maintain cells in a preosteoblast phenotype during osteoblast development. This gene may be upregulated in certain cancers. Mutations in this gene cause focal facial dermal dysplasia 3, Setleis type. Two transcript variants encoding the same protein have been found. [provided by RefSeq, Apr 2014]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:20670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20670) · Entrez [117581](https://www.ncbi.nlm.nih.gov/gene/117581) · UniProt [Q8WVJ9](https://www.uniprot.org/uniprotkb/Q8WVJ9) · Ensembl [ENSG00000233608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233608) · OMIM [607556](https://www.omim.org/entry/607556)

**PubMed**, as HGNC records for this gene — [7589808](https://pubmed.ncbi.nlm.nih.gov/7589808/), [9061034](https://pubmed.ncbi.nlm.nih.gov/9061034/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00182 |
| As a percentage | +0.13% |
| FDR, exposure-shuffle null | 0.8566 |
| In TP53-wild-type lines / altered lines | -0.00684 / 0.00708 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.187 raw, 0.145 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 29 targets |
| Activity vs MG53 across exposures (r) | 0.351 (q 7.24e-25) |
| With 3 principal components removed | 0.311 (q 6.40e-20) |
| Within line, across exposures (r) | 0.026 (q 0.032) |
| Percentile against all genes | 99.7 |

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
