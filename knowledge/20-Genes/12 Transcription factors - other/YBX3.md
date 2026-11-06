---
symbol: YBX3
type: gene
tier: 2
pathway_role: transcription factor
aliases: [dbpA, ZONAB, CSDA1]
gene_name: Y-box binding protein 3
locus: 12p13.2
locus_type: gene with protein product
gene_family: [Y-box binding proteins, Cold shock domain containing]
tags: [gene, transcription-factor]
generated_by: knowledge/_build/build_vault.py
---

# YBX3

*Y-box binding protein 3* — 12p13.2

> [!summary] In one line
> YBX3 is a cold-shock-domain protein, the less-studied paralogue of YBX1 (also called DBPA or ZONAB), whose best-supported function is post-transcriptional rather than transcriptional.

## What it is

YBX3 carries a single cold-shock domain and a long charged tail, the same architecture as YBX1, and binds both single-stranded DNA and RNA. Early work treated it as a transcription factor: as ZONAB it was found bound to the tight-junction protein ZO-1 and regulating ErbB-2 expression, and later work from the same group had it sequestered by ZO-1 and released at low cell density to drive proliferation-associated transcription. The stronger recent evidence points the other way — YBX3 binds mRNAs directly and sets the abundance of solute-carrier transcripts, with depletion reducing amino-acid import, though which transporters are affected differs between cell systems. Beyond this the literature is genuinely thin next to YBX1's, with most claims resting on one or two systems.

## Why it appears in this work

YBX3 is in the vault only because the regulon step scored it, at the extreme negative end of the ranking. Nothing in its literature connects it to [[MG53 (TRIM72)]], to p53, or to the TRIM72 locus; its interest here is as a stress test of the method, not as a candidate regulator. See [[Transcription factor activity inference]].

## What is uncertain

Whether YBX3 is a sequence-specific transcription factor at all is unsettled. Cold-shock domains bind nucleic acid with modest specificity, so an inferred regulon may reflect co-expression with an RNA-binding programme rather than promoter occupancy. If YBX3 acts mainly by stabilising transcripts, "activity" read off target mRNA means something different for it than for a bona fide transcription factor. Its regulon also cannot be cleanly separated from YBX1, which is more abundant and more promiscuous. Extreme ends of a ranking are where artefacts concentrate, and this gene sits at one.

## References

- Balda & Matter, 2000, EMBO Journal — identified ZONAB (DbpA/YBX3) as a Y-box factor that binds the tight-junction protein ZO-1, and showed the two together regulate ErbB-2 expression.
- Cooke et al., 2019, Cell Reports — showed YBX3 binds mRNAs and controls amino-acid levels by setting SLC transporter transcript abundance.

## What is on record

| | |
|---|---|
| Official name | Y-box binding protein 3 |
| Also known as | dbpA, ZONAB, CSDA1, cold-shock domain containing A1 |
| Locus | 12p13.2 — gene with protein product |
| Gene families | Y-box binding proteins; Cold shock domain containing |
| Previously named | cold shock domain protein A |

**Function**, from UniProt [P16989](https://www.uniprot.org/uniprotkb/P16989) (reviewed):

> Binds to the GM-CSF promoter. Seems to act as a repressor. Also binds to full-length mRNA and to short RNA sequences containing the consensus site 5'-UCCAUCA-3'. May have a role in translation repression (By similarity)

**Summary**, from NCBI Gene [8531](https://www.ncbi.nlm.nih.gov/gene/8531):

> Enables RNA binding activity. Involved in cellular hyperosmotic response; cellular response to tumor necrosis factor; and negative regulation of programmed cell death. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:2428](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2428) · Entrez [8531](https://www.ncbi.nlm.nih.gov/gene/8531) · UniProt [P16989](https://www.uniprot.org/uniprotkb/P16989) · Ensembl [ENSG00000060138](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060138) · OMIM [603437](https://www.omim.org/entry/603437)

**PubMed**, as HGNC records for this gene — [2977358](https://pubmed.ncbi.nlm.nih.gov/2977358/), [8710501](https://pubmed.ncbi.nlm.nih.gov/8710501/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.00029 |
| As a percentage | +0.02% |
| FDR, exposure-shuffle null | 0.9324 |
| In TP53-wild-type lines / altered lines | 0.00026 / 0.00031 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.296 raw, 0.259 with 3 PCs removed |

> [!note] How to read the slope's sign
> It is in **this gene's** units. For a p53-induced gene, up with MG53 means more p53 output;
> for a p53-repressed gene it means *less*. The signed row above does that conversion; see
> [[Signing genes by p53 direction]].

### As a transcription factor, against MG53

| | |
|---|---|
| Regulon size used | 23 targets |
| Activity vs MG53 across exposures (r) | -0.322 (q 1.10e-21) |
| With 3 principal components removed | -0.286 (q 4.39e-17) |
| Within line, across exposures (r) | -0.076 (q 2.86e-09) |
| Percentile against all genes | 0.3 |

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
