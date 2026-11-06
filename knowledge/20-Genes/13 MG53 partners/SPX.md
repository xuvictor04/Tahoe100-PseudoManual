---
symbol: SPX
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [MGC10946, NPQ, spexin, SPX1]
gene_name: spexin hormone
locus: 12p12.1
locus_type: gene with protein product
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# SPX

*spexin hormone* — 12p12.1

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/SPX.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | spexin hormone |
| Also known as | MGC10946, NPQ, spexin, SPX1, neuropeptide Q |
| Locus | 12p12.1 — gene with protein product |
| Previously named | chromosome 12 open reading frame 39 |

**Function**, from UniProt [Q9BT56](https://www.uniprot.org/uniprotkb/Q9BT56) (reviewed):

> Plays a role as a central modulator of cardiovascular and renal function and nociception. Also plays a role in energy metabolism and storage. Inhibits adrenocortical cell proliferation with minor stimulation on corticosteroid release (By similarity)

**Summary**, from NCBI Gene [80763](https://www.ncbi.nlm.nih.gov/gene/80763):

> The protein encoded by this gene is a hormone involved in modulation of cardiovascular and renal function. It has also been shown in rats to cause weight loss. Several transcript variants have been found for this gene. [provided by RefSeq, Feb 2016]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:28139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28139) · Entrez [80763](https://www.ncbi.nlm.nih.gov/gene/80763) · UniProt [Q9BT56](https://www.uniprot.org/uniprotkb/Q9BT56) · Ensembl [ENSG00000134548](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134548) · OMIM [619246](https://www.omim.org/entry/619246)

**PubMed**, as HGNC records for this gene — [22038051](https://pubmed.ncbi.nlm.nih.gov/22038051/), [24550067](https://pubmed.ncbi.nlm.nih.gov/24550067/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.07999 |
| As a percentage | +5.70% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.08906 / 0.07448 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.622 raw, 0.431 with 3 PCs removed |

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
