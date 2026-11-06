---
symbol: ASIC4
type: gene
tier: 3
pathway_role: tracks MG53 genome-wide
aliases: [BNAC4]
gene_name: acid sensing ion channel subunit family member 4
locus: 2q35
locus_type: gene with protein product
gene_family: [Acid sensing ion channel subunits]
tags: [gene]
generated_by: knowledge/_build/build_vault.py
---

# ASIC4

*acid sensing ion channel subunit family member 4* — 2q35

> [!abstract] No written note for this gene
> What follows is what the registries record and what this study measured — nothing is paraphrased or inferred on top of it. To add a written note, create `knowledge/_build/gene_knowledge/ASIC4.md` and rebuild; see [[How this vault is built]].

## What is on record

| | |
|---|---|
| Official name | acid sensing ion channel subunit family member 4 |
| Also known as | BNAC4 |
| Locus | 2q35 — gene with protein product |
| Gene families | Acid sensing ion channel subunits |
| Previously named | amiloride-sensitive cation channel 4, pituitary; acid-sensing (proton-gated) ion channel family member 4; acid sensing ion channel family member 4 |

**Function**, from UniProt [Q96FT7](https://www.uniprot.org/uniprotkb/Q96FT7) (reviewed):

> Does not exhibit measurable stand-alone pH-gated sodium channel activity but may form pH-gated heterotrimeric sodium channels. Its activity could also depend on alternative gating mechanisms

**Summary**, from NCBI Gene [55515](https://www.ncbi.nlm.nih.gov/gene/55515):

> This gene belongs to the superfamily of acid-sensing ion channels, which are proton-gated, amiloride-sensitive sodium channels. These channels have been implicated in synaptic transmission, pain perception as well as mechanoperception. This gene is predominantly expressed in the pituitary gland, and was considered a candidate for paroxysmal dystonic choreoathetosis (PDC), a movement disorder, however, no correlation was found between mutations in this gene and PDC. [provided by RefSeq, Feb 2012]

> [!note] Read NCBI's hedges literally
> Where that summary says "Predicted to …" or "Enables …", the annotation is inferred — from orthology, domain content or automated pipelines — not demonstrated for this gene.

**Accessions** — [HGNC:21263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21263) · Entrez [55515](https://www.ncbi.nlm.nih.gov/gene/55515) · UniProt [Q96FT7](https://www.uniprot.org/uniprotkb/Q96FT7) · Ensembl [ENSG00000072182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000072182) · OMIM [606715](https://www.omim.org/entry/606715)

**PubMed**, as HGNC records for this gene — [10852210](https://pubmed.ncbi.nlm.nih.gov/10852210/)

> [!note] What these are, and are not
> HGNC lists these against the gene's naming and characterisation. They are real identifiers,
> fetched rather than recalled. They are not a reading list chosen for this study, and the written sections above cite their own sources separately.

*Fetched from HGNC, NCBI Gene and UniProt on 2026-11-06 by `knowledge/_build/fetch_annotations.py`.*

## In this dataset

*Generated from the study's tables — do not edit by hand.*

### What MG53's level tracks, for this gene

| | |
|---|---|
| Slope, log2 of this gene per doubling of measured MG53 | 0.06749 |
| As a percentage | +4.79% |
| FDR, exposure-shuffle null | 5.64e-05 |
| In TP53-wild-type lines / altered lines | 0.06649 / 0.06807 |
| Verdict | — |
| Co-regulation with MG53 across exposures (r) | 0.243 raw, 0.435 with 3 PCs removed |

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
