---
symbol: IMPA1P1
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
gene_name: inositol monophosphatase 1 pseudogene 1
locus: 8q21.13
locus_type: pseudogene
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# IMPA1P1

*inositol monophosphatase 1 pseudogene 1* — 8q21.13

> [!summary] In one line
> IMPA1P1 is a transcribed pseudogene of inositol monophosphatase 1, with no known function of its own.

## What it is

The record is almost entirely annotation. IMPA1P1 lies on chromosome 8 near its parent gene IMPA1 and is classed as a transcribed unprocessed pseudogene with a single non-coding transcript. The parent enzyme is well characterised — IMPA1 recycles free inositol by dephosphorylating myo-inositol monophosphate, and is the classical candidate target of lithium — but none of that transfers to a pseudogene not expected to make protein. No function, pathway, partner or phenotype has been assigned to IMPA1P1, and no regulatory role of the kind shown for some other transcribed pseudogenes. What is attached to it is statistical: copy-number variants, and association signals in its interval more plausibly read as tagging IMPA1, which sits about 30 kb 5′ of it on the same strand.

## Why it appears in this work

IMPA1P1 is in the vault only because the genome-wide screen ranked it as tracking measured MG53 across exposures. It is not a curated p53 effector, not a transcription factor, and chromosome 8 puts it nowhere near TRIM72, so [[Readthrough spillover]] does not apply.

## What is uncertain

The first question is whether the measurement means anything. A pseudogene retaining high identity to a well-expressed parent is exactly where short reads cannot be assigned confidently, so the apparent signal may be IMPA1 reads landing on the wrong feature — and any correlation with MG53 would then be inherited from the parent locus. The transcript is low enough that ambient RNA is also live; see [[Why MG53 is hard to measure here]]. With no established function there is no mechanism against which a correlation could be judged. This note records a screen rank, not biology.

## References

No primary literature I can cite with confidence.

## What is on record

| | |
|---|---|
| Official name | inositol monophosphatase 1 pseudogene 1 |
| Also known as | — (no recorded alias) |
| Locus | 8q21.13 — pseudogene |
| Previously named | inositol(myo)-1(or 4)-monophosphatase 1 pseudogene |

NCBI Gene carries no summary paragraph for this gene.

**Accessions** — [HGNC:33956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33956) · Entrez [650747](https://www.ncbi.nlm.nih.gov/gene/650747) · Ensembl [ENSG00000251521](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251521)

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.09755 |
| As a percentage | +7.00% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.09943 / 0.09646 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.685 raw, 0.555 with 3 PCs removed |

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
