---
symbol: COL20A1
type: gene
tier: 2
pathway_role: tracks MG53 genome-wide
aliases: [KIAA1510]
gene_name: collagen type XX alpha 1 chain
locus: 20q13.33
locus_type: gene with protein product
gene_family: [Fibronectin type III domain containing, Fibril associated collagens with interrupted triple helices]
family_siblings_here: [FNDC7, NPHS1]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# COL20A1

*collagen type XX alpha 1 chain* — 20q13.33

> [!summary] In one line
> COL20A1 encodes collagen XX, a barely characterised FACIT-family collagen known almost entirely from chick embryonic tissue.

## What it is

Collagen α1(XX) was cloned from chick cornea and assigned to the FACIT subfamily — fibril-associated collagens with interrupted triple helices. Interrupted collagenous stretches sit alongside fibronectin type III repeats and a von Willebrand factor A domain, the layout of a protein that decorates fibrils rather than forming them. In chick it was found in cornea, cartilage and tendon; the human gene lies at 20q13.33, expressed at low level and biased toward brain and testis. After that the record thins fast: no knockout phenotype, no validated partner, no demonstrated activity — the database annotations are inferred from domain content, and no gene-disease association is established.

## Why it appears in this work

COL20A1 is not a curated pathway member. It is here because the genome-wide screen ranked it as tracking measured [[MG53 (TRIM72)]] — an empirical hit with no prior reason to be one. At 20q13.33 it is nowhere near TRIM72, so [[Readthrough spillover]] cannot explain it.

## What is uncertain

Almost everything. The transcript sits low enough that ambient RNA is a live explanation, and the repetitive Gly-X-Y sequence shared across the collagen family is where multi-mapping reads land imprecisely. With no established function there is no mechanism to check a correlation against, and nothing here separates one from a few-line effect or from the covariates in [[Why MG53 is hard to measure here]]. A lead for a targeted assay, not a finding.

## References

- Koch et al., 2001, Journal of Biological Chemistry — cloned α1(XX) collagen from chick cornea and assigned it to the FACIT subfamily.

## What is on record

| | |
|---|---|
| Official name | collagen type XX alpha 1 chain |
| Also known as | KIAA1510, Collagen alpha-1(XX) chain |
| Locus | 20q13.33 — gene with protein product |
| Gene families | Fibronectin type III domain containing; Fibril associated collagens with interrupted triple helices |
| Other genes here in those families | [[FNDC7]], [[NPHS1]] |
| Previously named | collagen, type XX, alpha 1 |

**Function**, from UniProt [Q9P218](https://www.uniprot.org/uniprotkb/Q9P218) (reviewed):

> Probable collagen protein

**Summary**, from NCBI Gene [57642](https://www.ncbi.nlm.nih.gov/gene/57642):

> Predicted to be located in endoplasmic reticulum lumen and extracellular matrix. Predicted to be part of collagen type XX trimer. [provided by Alliance of Genome Resources, Jun 2026]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:14670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14670) · Entrez [57642](https://www.ncbi.nlm.nih.gov/gene/57642) · UniProt [Q9P218](https://www.uniprot.org/uniprotkb/Q9P218) · Ensembl [ENSG00000101203](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101203) · OMIM [619390](https://www.omim.org/entry/619390)

**PubMed**, as HGNC records for this gene — [10819331](https://pubmed.ncbi.nlm.nih.gov/10819331/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.09359 |
| As a percentage | +6.70% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.10733 / 0.08662 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.527 raw, 0.568 with 3 PCs removed |

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
