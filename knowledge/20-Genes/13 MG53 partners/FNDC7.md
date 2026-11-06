---
symbol: FNDC7
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [FLJ35838]
gene_name: fibronectin type III domain containing 7
locus: 1p13.3
locus_type: gene with protein product
gene_family: [Fibronectin type III domain containing]
family_siblings_here: [COL20A1, NPHS1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# FNDC7

*fibronectin type III domain containing 7* — 1p13.3

> [!summary] In one line
> FNDC7 encodes a predicted secreted protein built from fibronectin type III repeats, and essentially nothing about its function is established.

## What it is

What is known is sequence and little else. The open reading frame predicts a signal peptide and a string of fibronectin type III domains — a module shared with fibronectin itself and many cell-surface proteins, and the only basis for any family assignment. Expression is low wherever surveyed, most consistently in testis. Everything functional is annotation, not observation: "secreted" and "extracellular region" come from domain content, not experiment. There is no published knockout, no identified ligand or receptor, no characterised partner, no replicated disease association. No connection has been reported between FNDC7 and p53, membrane repair, or [[MG53 (TRIM72)]].

## Why it appears in this work

FNDC7 is here only because the genome-wide screen ranked it as tracking measured MG53. It is not a curated p53 effector, not a transcription factor, and not near the TRIM72 locus, so [[Readthrough spillover]] does not account for it.

## What is uncertain

Everything. The transcript is near the detection floor, and a testis-biased gene reading as weakly present across a pooled cancer-line panel is as easily explained by ambient RNA or by reads shared with other FN3-domain paralogues as by real expression. With no established function there is no prediction to test and no mechanism against which a correlation could be judged. Nothing here separates an MG53 association from one driven by a few lines or by the covariates in [[Why MG53 is hard to measure here]]. This note records a screen rank, not biology.

## References

No primary literature I can cite with confidence.

## What is on record

| | |
|---|---|
| Official name | fibronectin type III domain containing 7 |
| Also known as | FLJ35838 |
| Locus | 1p13.3 — gene with protein product |
| Gene families | Fibronectin type III domain containing |
| Other genes here in those families | [[COL20A1]], [[NPHS1]] |

UniProt [Q5VTL7](https://www.uniprot.org/uniprotkb/Q5VTL7) carries no FUNCTION annotation.

**Summary**, from NCBI Gene [163479](https://www.ncbi.nlm.nih.gov/gene/163479):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:26668](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26668) · Entrez [163479](https://www.ncbi.nlm.nih.gov/gene/163479) · UniProt [Q5VTL7](https://www.uniprot.org/uniprotkb/Q5VTL7) · Ensembl [ENSG00000143107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143107)

**PubMed**, as HGNC records for this gene — [36626432](https://pubmed.ncbi.nlm.nih.gov/36626432/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.14084 |
| As a percentage | +10.25% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.13293 / 0.14564 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.863 raw, 0.761 with 3 PCs removed |

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
